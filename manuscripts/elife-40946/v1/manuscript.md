# Cellular cartography of the organ of Corti based on optical tissue clearing and machine learning

## Authors

- Shinji Urata<sup>1</sup> ([ORCID: 0000-0002-5947-6842](https://orcid.org/0000-0002-5947-6842))
- Tadatsune Iida<sup>1</sup>
- Masamichi Yamamoto<sup>3</sup>
- Yu Mizushima<sup>2</sup> ([ORCID: 0000-0002-8184-4437](https://orcid.org/0000-0002-8184-4437))
- Chisato Fujimoto<sup>2</sup>
- Yu Matsumoto<sup>2</sup>
- Tatsuya Yamasoba<sup>2</sup> †
- Shigeo Okabe<sup>1</sup> ([ORCID: 0000-0003-1216-8890](https://orcid.org/0000-0003-1216-8890)) †

### Affiliations

1. Department of Cellular Neurobiology, Graduate School of Medicine The University of Tokyo Tokyo Japan
2. Department of Otolaryngology, Graduate School of Medicine The University of Tokyo Tokyo Japan
3. Department of Nephrology, Graduate School of Medicine Kyoto University Kyoto Japan

† Corresponding author

## Abstract

The highly organized spatial arrangement of sensory hair cells in the organ of Corti is essential for inner ear function. Here, we report a new analytical pipeline, based on optical clearing of tissue, for the construction of a single-cell resolution map of the organ of Corti. A sorbitol-based optical clearing method enabled imaging of the entire cochlea at subcellular resolution. High-fidelity detection and analysis of all hair cell positions along the entire longitudinal axis of the organ of Corti were performed automatically by machine learning–based pattern recognition. Application of this method to samples from young, adult, and noise-exposed mice extracted essential information regarding cellular pathology, including longitudinal and radial spatial characteristics of cell loss, implying that multiple mechanisms underlie clustered cell loss. Our method of cellular mapping is effective for system-level phenotyping of the organ of Corti under both physiological and pathological conditions.

## Introduction

A complete understanding of auditory perception and transduction relies on an accurate reconstruction of the intact, three-dimensional structure of the cochlea. The spatial organization of the organ of Corti, the mammalian auditory sensory epithelium, determines the cochlear tonotopic map, which associates the positions of the inner hair cells (IHCs) in the cochlea with local characteristic frequencies. The basic pattern of the tonotopic map is simple, with higher frequencies on the base of the cochlear spiral and lower frequencies on the apex (von Békésy and Peake, 1990). However, multiple structural and cell biological factors influence the actual shape of the tonotopic map (Temchin and Ruggero, 2014).

In humans, age-related (Chien and Lin, 2012) and noise-induced hearing loss (Nelson et al., 2005) are prevalent health problems that require early prevention (Cunningham and Tucci, 2017). However, the field awaits the development of appropriate model animals that recapitulate human pathology (Wang et al., 2002; Yamasoba et al., 1998; Zheng et al., 1999). Moreover, the complexities of cochlear structure have prohibited a comprehensive cellular cartography, and current histological techniques are far from satisfactory for comprehensive analyses. Therefore, new methods that enable simultaneous examination of molecular signatures and subcellular structures across the entire cochlea would greatly accelerate the progress of research on auditory mechanisms.

Optical access to the properties of cells within highly complex tissues and organs is an important technical goal of modern cell biology. Advancements in optical tissue clearing have enabled the acquisition of structural and molecular information from large volumes of tissues and organs (Chung et al., 2013; Dodt et al., 2007; Hama et al., 2015; Renier et al., 2014; Susaki et al., 2014). Recent reports showed that both organic solvent– and hydrophilic solution–based clearing methods could be optimized in clearing hard tissues that contain large proportions of extracellular matrix (Berke et al., 2016; Cai et al., 2018; Calve et al., 2015; Greenbaum et al., 2017; Jing et al., 2018; Tainaka et al., 2018; Treweek et al., 2015). The accumulating knowledge and technologies should be helpful in development of effective clearing and labeling protocols for the inner ear inside the temporal bone (Nolte et al., 2017; Tinne et al., 2017). To date, however, an integrated method of tissue processing, labeling, and imaging techniques with single cell resolution has not yet been developed and optimized for the inner ear.

Here, we report an analytical pipeline for the construction of a single-cell resolution map of the organ of Corti taken from C57BL/6J mice at postnatal day (PND) 5, 60, 120 and 360. The method is based on optical tissue clearing technology and automatic cell detection using a machine learning algorithm. In this method, a series of fixation, permeabilization, immunolabeling, and clearing processes transform the inner ear into optically transparent samples suitable for volume imaging at single-cell resolution. Automated high-fidelity recording and analysis of hair cell positions along the entire length of the organ of Corti were achieved based on machine learning–based cell detection. Application of this method to pathological samples revealed distinct impacts of aging and noise on spatial features of sensory hair cell pathology. Our method of cellular mapping is highly effective for system-level phenotyping of the organ of Corti.

## Results and discussion

### Analytical pipeline for cellular cartography of the organ of Corti

Our analytical pipeline for sensory hair cell mapping in the cochlea followed three steps. First, the mouse temporal bone was isolated at PND 60 and processed for clearing and immunolabeling of the sensory hair cells (Figure 1A and Figure 1—figure supplement 1). Tissue clearing and immunolabeling were optimized for tissue transparency and antibody accessibility. After tissue preparation, three-dimensional two-photon excitation microscopy generated image stacks covering the entire structure of the organ of Corti, with an average size of 1200 × 1200 × 800 μm (Figure 1B). The image data were processed by custom-made software to stitch and linearize the sensory epithelium, followed by detection of cell positions (Figure 1C). The software automatically generated a spatial map of the total hair cells and estimated the positions of putative lost cells. The entire experimental procedure could be completed within 5 days, with 4 days for tissue clearing and labeling, 4 hr for image acquisition, and 30 min for automated analysis.

![Figure 1.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig1-v1.jpg)

**Figure 1.:** (A) Time course and individual steps of tissue clearing with or without immunostaining. (B) Three-dimensional imaging of the organ of Corti within the temporal bone. Top view (left), lateral view (middle), and the schematic presentation of the organ of Corti with its axis parallel to the modiolus. The size of the organ of Corti is indicated in the X, Y, and Z coordinates. Scale bar, 500 μm. (C) Computational processes of linearization, cell detection, and modeling. (D) Side-by-side comparison of 3DISCO, iDISCO, CLARITY, and CUBIC. Transmitted light images of samples before and after clearing, together with MYO7A staining. Scale bar, 500 μm. (E) Manual dissection of the iDISCO-processed sample confirmed MYO7A staining in the sensory epithelium. Scale bars, 500 μm (upper image) and 100 μm (lower image). (F) Lateral and horizontal views of the reconstructed three-dimensional images of the organ of Corti stained with anti-MYO7A. CUBIC with decalcification and original ScaleS failed to detect the deepest part of the organ of Corti (green dotted lines). With modified ScaleS, the entire structure of the organ of Corti could be visualized. Scale bar, 500 μm. (G) Modified ScaleS sample of the organ of Corti stained with anti-MYO7A antibody, together with transmitted light images before (upper left) and after (upper right) treatment. Scale bar, 500 μm. (H) Three steps of the modified ScaleS protocol. The initial decalcification step is followed by a clearing step, which mainly removes lipids from the extracellular matrix. Finally, the RI of the sample is matched with mounting solution. (I) Preservation of GFP fluorescence after modified ScaleS treatment. Scale bar, 10 μm. (J) Preservation of rhodamine-phalloidin signal after modified ScaleS treatment, which includes sorbitol to stabilize cytoskeletal polymers. Scale bar, 10 μm. IHC, inner hair cell; OHC, outer hair cell; RI, refractive index.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Comparison of optical transparency of mouse brain samples using 3DISCO, iDISCO, CLARITY and CUBIC. Scale, 3 mm. (B) Relationship between imaging depths and RIs using the decalcified cochlea as a sample. (n = 5 samples. Dunnet’s multiple comparison test, *p < 0.05; ***p < 0.001; ns; not significant, p > 0.05.) (C) Time course and individual steps of modified Sca/eS compared to the previous protocols of cochlear tissue preparations. (D) Macroscopic images of the cochlea through the steps of decalcification, clearing, and RI matching. Each image corresponds to the time points (i) to (viii) shown in (A). Scale bar, 1 mm. (E) Mouse brain sections with 100 μm thickness were treated with urea and guanidine solutions at varying concentrations. After tissue clearing, tissue volume expansion and optical transmittance were measured. Scale bar, 5 mm. (n = 5 samples for each condition. One-way ANOVA with Bonferroni’s post hoc test, *p < 0.05; ***p < 0.001; ns; not significant, p > 0.05.) RI, refractive index.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Tubular bone samples were treated with modified ScaleS and CB-perfusion. CB-perfusion was designed for whole-body imaging (see Appendix 1 for the detail). Transmitted light Images before and after clearing procedures were presented. The trabecular regions of the tubular bone (boxed regions of the low magnification images with transmitted light) stained with anti-vascular endothelial (VE)-cadherin were imaged through the surface of the compact bone. Boxed regions in fluorescence images were further enlarged for presentation of vasculature details. Scale bar, 5 mm (transmission images), 100 μm (fluorescence images). The graph shows the maximal depth at which the VE-cadherin signals could be detected from the surface. (n = 3 samples for each condition. Two-tailed unpaired t test, *p < 0.05.) (B) Application of modified ScaleS to multiple biological samples. To test the effectiveness of modified ScaleS for clearing the non-osseous tissue, multiple organs (brain, heart, stomach, lung, liver, kidney, intestine and spleen) were processed with modified ScaleS and CB-perfusion. Performance of CB-perfusion was better than modified ScaleS in stomach, lung, liver, kidney and spleen. This difference can be explained by better performance of CB-perfusion in elimination of blood cells by perfusion and effective delipidation and decolorization by aminoalcohol. Scale bar, 5 mm.

### Optimization of imaging of the whole intact cochlea

The mouse inner ear forms complex and intricate structures inside the temporal bone. To achieve deeper and clearer imaging of the organ of Corti, it was necessary to overcome two hurdles. First, an inorganic component of the bone, mainly composed of calcium phosphate, had to be removed. Second, refractive index (RI) matching had to be fine-tuned to decrease optical aberration induced by heterogenous tissue components (Acar et al., 2015; Berke et al., 2016). The existence of multiple methods for optical tissue clearing provided us with an opportunity to perform a side-by-side comparison of their applicability to the organ of Corti. We tested five independent, well-established clearing and labeling protocols (3DISCO (Ertürk et al., 2012), iDISCO (Renier et al., 2014), CLARITY (Chung et al., 2013), CUBIC (Susaki et al., 2014), and ScaleS (Hama et al., 2015)) for their performance in detection of total hair cells. Myosin 7a (MYO7A), specifically expressed in IHCs and outer hair cells (OHCs), was utilized as a standard marker for hair cells. We found that performances of different protocols were comparable when they were applied to adult mouse brains, but the efficiencies for clearing the temporal bone were variable (Figure 1D and Figure 1—figure supplement 1). We failed to detect MYO7A-immunopositive hair cells in samples processed by 3DISCO, iDISCO, CLARITY, or CUBIC (Figure 1D). Microdissection of the membrane labyrinth of the iDISCO-processed samples confirmed the presence of MYO7A-immunopositive hair cells, suggesting that the surrounding bone tissue prevented the detection of fluorescence (Figure 1E). When CUBIC was combined with decalcification, MYO7A fluorescence could be detected down to 180 μm from the surface, but the combined method still did not enable imaging of the deeper part of the organ of Corti (Figure 1F). Among the pre-existing tissue clearing methods, ScaleS combined with decalcification yielded the best results (Figure 1F). However, this method still missed hair cells at the cochlear base, more than 500 μm away from the bone surface.

By modifying the original ScaleS method, we achieved efficient in situ detection of all MYO7A-positive hair cells in the organ of Corti (Figure 1G and Figure 1—figure supplement 1). In the new protocol, we first decalcified the samples with EDTA (Figure 1H). In the subsequent clearing step, a combination of a nonionic detergent (Triton X-100) and an ionic chaotropic reagent (guanidine) was effective in increasing transparency. The ScaleS and CUBIC1 protocols use urea instead of guanidine (Hama et al., 2015; Susaki et al., 2015), but high concentrations of urea can induce tissue expansion (Tainaka et al., 2016). By contrast, our guanidine-based clearing solution did not induce detectable tissue expansion (Figure 1—figure supplement 1). Although guanidine treatment denatures GFP and reduces its fluorescence intensity (Huang et al., 2007), this fluorescence quenching could be reversed by incubation in phosphate-buffered saline (PBS). Finally, we tested the solutions with RIs from 1.41 to 1.56 for their performance in tissue clearing by measuring the maximal depth of detectable MYO7A-positive hair cells from the temporal bone surface (Figure 1—figure supplement 1). We found that a RI matching solution with a RI of 1.47 was most effective for detecting MYO7A-positive hair cells away from the bone surface. This RI lies between that of bone matrix (RI = 1.56) and tissue with scarce extracellular matrix (RI = 1.38). The new protocol for the in situ detection of all MYO7A-positive hair cells in the organ of Corti could be completed within 4 to 6 days (Figure 1A,H, and Figure 1—figure supplement 1), and effectively detected GFP-based reporter molecules and F-actin by rhodamine phalloidin (Figure 1I,J). The presence of sorbitol in the clearing solution improved F-actin stabilization. The protocol could also be applied to detection of cellular components in other types of bone-containing samples (Figure 1—figure supplement 2).

### Machine learning–based automated detection of sensory hair cells

To obtain information about hair cell distribution along the entire longitudinal axis of the organ of Corti, we applied our optimized tissue clearing and labeling methods to samples from naïve C57BL/6J mice, and detected sensory hair cells with anti-MYO7A antibody. The combination of a widely used marker of sensory hair cells (MYO7A) and a standard mouse line (C57BL/6J) should facilitate replication of this protocol in other laboratories and comparative studies. Multiple image stacks that cover the entire structure of the organ of Corti were obtained by two-photon microscopy with voxel sizes of 0.99 × 0.99 × 1.0 μm for high-resolution imaging (Figure 2A). Spatially confined two-photon excitation effectively decreased photobleaching after repetitive imaging. To adjust the local fluorescence intensity of MYO7A-immunopositive hair cells, we controlled both excitation laser power and the cut-off range of pixel intensities.

![Figure 2.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig2-v1.jpg)

**Figure 2.:** (A) Detection of single hair cells stained with anti-MYO7A. The border between hair cells can be clearly detected. Scale bar, 10 μm. (B) Sequential steps in reconstruction of the linearized voxel image of the organ of Corti. The linearized voxel image was generated using the row of IHCs as a structural reference of the longitudinal axis of the organ of Corti. Scale bar, 100 μm. (C) Plot of the total longitudinal length of the organ of Corti against the total number of IHCs. (D) Plot of radial distance of IHCs from the modiolus. (E) Plot of hair cell positions along the vertical axis of the organ of Corti. (F) Normalization of heterogeneity in hair cell positions. Before normalization, both x and y axes represent physical positions of OHCs. After normalization, the coordinates are arbitrary units and are equalized in x and y axes. (G) Transformation of the positions of hair cells to fit the standardized template. The template is a two-dimensional grid parallel to the surface of the sensory epithelium (upper image). This transformation is useful for estimation of lost hair cells based on the calculation of cell-free space. The accuracy of estimation by this method was comparable to the performance of manual estimation (lower plot). [n = 161 samples for each. Paired t-test; ns, not significant (p > 0.05).] IHC, inner hair cell; OHC, outer hair cell; PND, postnatal day; RI, refractive index.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Numbers of total IHCs and OHCs of C57BL/6J mice at PND 5, PND 60, and PND 360. (n = 4 (PND 5), 4 (PND 60), and 3 (PND 360). One-way ANOVA with Bonferroni's post hoc test, ***p < 0.001.) (B) ABR thresholds (left) and the numbers of lost OHCs (right) were compared between C57BL/6J (mouse model of age-related hearing loss) and CBA/Ca mice (control mice) at PND 60. (C) The effect of acoustic overexposure stimulus on ABR thresholds (left) and OHC loss (right) measured at PND 60. Acoustic overexposure stimulus induced an increase in ABR threshold and loss of OHCs. ABR, auditory brainstem response; IHC, inner hair cell; OHC, outer hair cell; PND, postnatal day.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Positions of Inner hair cells were sampled with regular intervals and the position data from different samples were overlaid. Hair cells from different samples were plotted as dots with different colors. Spiral directions of samples from right ears were converted to those of left ears for alignment of samples from both sides. PND, postnatal day.

To achieve automated detection of both IHCs and OHCs, we developed a series of custom-made MATLAB scripts (Figure 2B and Table 1, also see Appendices 1 and 2). Because loss of IHCs is rare even in pathological conditions, such as aging and noise exposure, the row of IHCs was used as a guide for linearization of the spiral sensory epithelium. First, multiple image stacks containing portions of the organ of Corti were assembled into a single image stack. Our image acquisition protocol was designed to obtain image stacks covering the volume of the entire cochlea. We also designed that the two adjacent imaged stacks always have the overlapping volume. With these image acquisition rules, the entire tissue volume containing the whole sensory epithelium could be easily reconstructed. Second, the best-fit arcs of the single IHC row were calculated to create a spiral that could be used as a structural reference for the entire organ of Corti. Third, a linearized voxel image was reconstructed using the best-fit spiral and the normal vectors of the plane fitted to the segments of the sensory epithelium. Finally, we employed machine learning models to perform an exhaustive search of all hair cells and recorded their positions as Cartesian coordinates. The search process by machine learning technique consists of two parts: the first step of signal-noise discrimination and the second step for the recovery of false negatives. The details are provided in Table 1 and Appendix 2. (LeCun et al., 1989; Friedman et al., 2000; Breiman, 2001)

**Table 1.**
 Details of machine learning models (related to Figure 2).


<table>
  <thead>
    <tr>
      <th>Models</th>
      <th>Type‡</th>
      <th>Algorithm</th>
      <th>Configuration</th>
      <th>Use</th>
      <th>Predictor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IHC* 1</td>
      <td>Binary</td>
      <td>Gentle Boost</td>
      <td>300 classification trees</td>
      <td>Reduction of noise</td>
      <td>Area, barycentric coordinates, maximum correlation coefficients, maximum intensity, same data set of the nearest neighbor group and relative position of the nearest neighbor group</td>
    </tr>
    <tr>
      <td>IHC* 2</td>
      <td>Binary</td>
      <td>Random Forest</td>
      <td>300 classification trees</td>
      <td>Detection of cells</td>
      <td>Adding to the above, prediction score by ‘IHC* 1’ of itself and that of adjacent groups in six directions¶, relative position of the adjacent groups, and cropped image††</td>
    </tr>
    <tr>
      <td>OHC† 1</td>
      <td>Binary</td>
      <td>Gentle Boost</td>
      <td>300 classification trees</td>
      <td>Reduction of noise</td>
      <td>Same as ‘IHC* 1’</td>
    </tr>
    <tr>
      <td>OHC† 2</td>
      <td>Binary</td>
      <td>Random Forest</td>
      <td>300 classification trees</td>
      <td>Detection of cells</td>
      <td>Same as ‘IHC* 2’</td>
    </tr>
    <tr>
      <td>OHC† 3</td>
      <td>Multiclass</td>
      <td>Convolutional Neural Network</td>
      <td>From the input, convolutional layer (filter size 5, number 60), ReLU§ layer, fully connected layer, Softmax Layer (three classes), and output.</td>
      <td>Estimation of belonging row</td>
      <td>Cropped image (39 × 69 pixels in width and height)</td>
    </tr>
    <tr>
      <td>OHC† 4</td>
      <td>Binary</td>
      <td>Convolutional Neural Network</td>
      <td>From the input, convolutional layer (filter size 5, number 60), ReLU§ layer, convolutional layer (filter size 5, number 20), ReLU§ layer, fully connected layer, Softmax Layer (two classes), and output.</td>
      <td>Detection of cells in spaces</td>
      <td>Cropped image (39 × 69 pixels in width and height)</td>
    </tr>
  </tbody>
</table>

_*. IHC, inner hair cell.†. OHC, outer hair cell.‡. Classification type.§. Rectified Linear Unit.¶. Adjacent groups in direction of 0–60°, 60–120°, 120–180°, 180–240°, 240–300°, 300–360° with the y-axis as an initial line in the x-y plane.††. Initial image size is 21 × 69 pixels in width and height. The image is resized in 7 × 23 then reshaped in 1 × 161._

To test the ability of our automated cell detection protocol to reliably record hair cell positions, we studied its performance by comparing its outputs with manually identified OHC positions in four independent samples of the organ of Corti labeled with anti-MYO7A antibody. The automated detection protocol recovered 98.8 ± 0.6% of manually identified hair cells. In turn, 99.7 ± 0.2% of hair cells identified by the algorithm were also scored as hair cells by human operators, with the remaining 0.3% representing false positives (Table 2). The detection efficiency of our protocol was much higher than a standard imaging processing protocol based on three-dimensional watershed ((Soille and Vincent, 1990; Table 2 and Appendix 2).

**Table 2.**
 Detection efficiency of hair cells (related to Figure 2).*


<table>
  <tbody>
    <tr>
      <td></td>
      <td colspan="5">Inner hair cell</td>
    </tr>
    <tr>
      <td></td>
      <td>Detect. (n)†</td>
      <td>Undetect. (n)‡</td>
      <td>Err. detect. (n)§</td>
      <td>Recover Rate¶</td>
      <td>Accuracy rate††</td>
    </tr>
    <tr>
      <td>Our Method</td>
      <td>576 ± 33</td>
      <td>13 ± 12</td>
      <td>2 ± 2</td>
      <td>0.979 ± 0.021</td>
      <td>0.997 ± 0.003</td>
    </tr>
    <tr>
      <td>3D Watershed</td>
      <td>424 ± 98</td>
      <td>152 ± 82</td>
      <td>110 ± 78</td>
      <td>0.733 ± 0.149</td>
      <td>0.818 ± 0.100</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="5">Outer hair cell</td>
    </tr>
    <tr>
      <td></td>
      <td>Detect. (n)†</td>
      <td>Undetect. (n)‡</td>
      <td>Err. Detect. (n)§</td>
      <td>Recover Rate¶</td>
      <td>Accuracy rate††</td>
    </tr>
    <tr>
      <td>Our Method‡‡</td>
      <td>1989 ± 133</td>
      <td>24 ± 13</td>
      <td>6 ± 4</td>
      <td>0.988 ± 0.006</td>
      <td>0.997 ± 0.002</td>
    </tr>
    <tr>
      <td>Principle 1 Only§§</td>
      <td>1925 ± 131</td>
      <td>69 ± 41</td>
      <td>16 ± 13</td>
      <td>0.966 ± 0.021</td>
      <td>0.992 ± 0.006</td>
    </tr>
    <tr>
      <td>3D Watershed</td>
      <td>1493 ± 197</td>
      <td>496 ± 111</td>
      <td>760 ± 381</td>
      <td>0.748 ± 0.064</td>
      <td>0.682 ± 0.103</td>
    </tr>
  </tbody>
</table>

_*. Data from 10 samples (PND30: two sample, PND60: three sample, ACL: two sample, NCL: three sample). Data are expressed as means ± SD.†. Detection number.‡. Undetected number.§. Erroneous detection number.¶. Recover rate of manually identified hair cells by the automated detection algorithm (almost synonymous with recall).††. The number of hair cells identified by both manual and automated detection divided by the number of hair cells identified by automated detection (almost synonymous with precision).‡‡.The proposed method in this study (principle 1 + principle 2).§§. The method using the first half of the proposed method. For details please see ‘Principles of auto-detection by machine learning’ in Appendix 2._

### Automated detection of hair cells in samples with hair cell pathology

Pathological changes in the sensory epithelium associated with aging or noise exposure can impair the hearing functions of the inner ear. Previous studies provided qualitative evidence showing that the cellular changes associated with age-associated or noise-induced hearing loss partially overlap, but also have distinct characteristics. C57BL/6J mice are widely used for aging research and exhibit the classic pattern of age-related hearing loss, with the loss of both hair cells and neurons starting from the base (Hunter and Willott, 1987). The increase in auditory brainstem–evoked response (ABR) threshold starts at the age of 10 weeks (Ison et al., 2007). Manual counting of lost cells in C57BL/6J mice at PND 5, 60, and 360 confirmed age-related cell loss (ACL) (Figure 2—figure supplement 1). For the assessment of noise-induced cell loss (NCL), we applied acoustic overexposure stimulus to C57BL/6J mice at PND 60 to induce a moderate threshold shift (Figure 2—figure supplement 1), as previously reported (Mizushima et al., 2017; Tuerdi et al., 2017). The cellular pathology varied from nearly normal appearance to severe hair cell damage in the basal end of the cochlea, and exhaustive screening of hair cell loss in this context should be useful.

To appropriately interpret cell position data from samples harvested under physiological and pathological conditions, it is necessary to evaluate variation in the morphology of the organ of Corti. Variation may also exist among samples collected under identical experimental conditions, potentially confounding data interpretation. To evaluate such variation in morphology, we performed the following three types of measurements (Appendix 2). First, we measured the total longitudinal length of the IHC row and the number of IHCs. The plot of IHC number vs. the length of the IHC row for multiple samples is useful for evaluating the longitudinal sizes of the organ of Corti (Figure 2C). The plot shows that data from young control samples (PND 30) scattered in the range of 550–650 IHCs, indicating the presence of physiological variation. Variation in the length and the cell number did not show a specific trend between samples from different ages. However, the data from noise-exposed mice exhibited a tendency of higher variation, potentially due to selective loss of hair cells at the basal end in some NCL samples. Second, we projected the position of IHCs onto a plane perpendicular to the modiolus and plotted the distance of IHCs from the modiolus (Figure 2D). This plot revealed small variation in IHC position among experimental groups. Third, the positions of IHCs were projected onto the axis of the modiolus, and the relative positions of every 25 IHCs were plotted (Figure 2E). The IHC distributions along the axis of the modiolus in all samples were similar. In summary, these measurements confirmed that the overall spatial distribution of IHCs can be maintained under pathological conditions (Figure 2—figure supplement 2). Hence, we performed further analysis of the pattern of hair cell loss using a standardized template of cell positions.

To simplify the treatment of hair cell position in the subsequent analysis, the Cartesian coordinates of hair cell positions were transformed and normalized to match the standardized template, which consisted of the normalized two-dimensional grids parallel to the surface of the sensory epithelium (Figure 2F,G). The first axis was defined by the line of detected IHCs, and the second was set perpendicular to the first axis. This simplified presentation is useful for measuring the space unoccupied by the hair cells. We hypothesized that the area of the unoccupied space reflects the space previously occupied by hair cells that were subsequently lost. By dividing the areas that were not occupied by existing OHCs by the average area of a single OHC, we could estimate the number of OHCs lost. Comparison of the performances of trained operators and automated calculation confirmed that adequate estimation of hair cell loss could be achieved by automated calculation; indeed, the two methods were similarly effective (Figure 2G and Table 3). The total number of lost OHCs was 26.3 ± 6.3, 34.6 ± 5.1, 55.8 ± 4.5, and 49.3 ± 17.3 (mean ±SD) in wild-type C57BL/6J mice at PND 30, 60, and 120, and PND 60 plus noise exposure. These data are consistent with previous estimates of hair cell loss based on manual counting in rats and chinchillas (Hu et al., 2012; Yang et al., 2004). Therefore, our protocol is suitable for quantitative analysis of IHCs and OHCs, including detection and counting of lost hair cells.

**Table 3.**
 Inter-operator percent match in void space detection (related to Experimental procedures).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">Inter-operator percent match</th>
      <th colspan="3">Number of detected void space</th>
    </tr>
    <tr>
      <th>Sample number</th>
      <th>A¶-B¶</th>
      <th>B¶-C¶</th>
      <th>A¶-C¶</th>
      <th>Auto††-HC‡‡</th>
      <th>Both</th>
      <th>Auto††-only</th>
      <th>HC‡‡-only</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1*</td>
      <td>0.960</td>
      <td>0.880</td>
      <td>0.917</td>
      <td>0.920</td>
      <td>24</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2†</td>
      <td>0.898</td>
      <td>0.917</td>
      <td>0.906</td>
      <td>0.952</td>
      <td>84</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td>3‡</td>
      <td>0.923</td>
      <td>0.885</td>
      <td>0.958</td>
      <td>0.889</td>
      <td>24</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4§</td>
      <td>0.923</td>
      <td>0.882</td>
      <td>0.846</td>
      <td>0.926</td>
      <td>50</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>0.916</td>
      <td>0.898</td>
      <td>0.897</td>
      <td>0.931</td>
      <td>182</td>
      <td>9</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

_*. Sample 1, two months old, total loss rate of OHCs: 1.7%.†. Sample 2, two months old with noise exposure, total loss rate of OHCs: 8.1%.‡. Sample 3, one month old, total loss rate of OHCs: 2.2%.§. Sample 4, four months old, total loss rate of OHCs: 4.2%.¶. Skilled human operators (A, B, and C).††. Auto, automated OHC loss counting program.‡‡. HC, human consensus._

### Spatial characteristics of hair cell loss

Presentation of lost cell density in the form of two-dimensional grids facilitates side-by-side comparison of hair cell loss along the longitudinal axis of the organ of Corti (Figure 3A and Figure 3—figure supplement 1). In samples from young mice not exposed to noise, small numbers of hair cells were lost along both the longitudinal and radial axes (Figure 3A and Figure 3—figure supplement 1). Samples of aged mice had a higher density of lost cells at both ends of the organ of Corti (Figure 3B). The difference between adult and aged mice was confirmed by comparison across ages. In particular, the age-dependent increase in lost cell density was prominent at the apical end (PND 60: 0.0596 ± 0.0048, PND 120: 0.116 ± 0.0150, Welch’s t-test, p < 0.01, t = 3.59, df = 9.68). By contrast, previous studies reported a higher rate of ACL in the basal portion, but failed to detect a prominent increase in the proportion of lost cells in the apical region. This difference may be due to the fact that our tissue clearing technique enabled complete visualization of hair cells at the helicotrema (Figure 3C). ACL also had spatial features along the radial axis, with a higher density at positions distal to the modiolus (Figure 3D). This trend along the radial axis was already present in cochleae at PND 60, indicating that ACL may represent acceleration of a pathology already present in the early stage of life. In summary, the method we developed was well suited for comprehensive analysis of ACL.

![Figure 3.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig3-v1.jpg)

**Figure 3.:** (A) Pseudo-color presentation of hair cell loss along the longitudinal axis of the organ of Corti (PND 30, 60, and 120 and noise exposure at PND 60). Each row represents a single cochlear sample. Numbers of lost hair cells within 50 μm segments along the longitudinal axis were measured. For samples with higher cell loss in the basal portion, it was difficult to define the basal end of the sensory epithelium. These samples with ambiguous starting points of the epithelium were marked by thin red lines in rows of noise-exposed samples. The raw fluorescence image shows the definition of directions (distal and proximal, apex and base) relative to the sensory epithelium. (B) Distribution of lost cells along the longitudinal axis of the organ of Corti in three experimental groups. PND 60 and 120, and noise exposure at PND 60, exhibit distinct patterns of hair cell loss (Kruskal–Wallis test with Steel–Dwass test). (C) Detection of hair cell loss at the helicotrema. Scale bar, 100 μm. (D) Distribution of lost cells along the radial axis of the organ of Corti. Samples from PND 60 and 120 exhibit gradients of cell loss. (Paired t-test followed by Bonferroni’s correction, *p < 0.05; ***p < 0.001.) Number of samples; n = 10 (PND 30), 14 (PND 60), 9 (PND 120), and 10 (Noise), except for n = 7 in segment ‘a’ of Noise in (B). *p < 0.05; **p < 0.01; ***p < 0.001. PND, postnatal day.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Pseudo-color presentation of the OHC loss frequency along the radial axis. Each row represents a single cochlear sample. The sample IDs were written on the left of the map. Note that the direction of comparison (proximal to distal) is perpendicular to the map shown in Figure 3A. Samples were arranged according to the extent of total cell loss in each experimental group from the highest to the lowest. The radial positions were divided into 15 sections and the scores were averaged within the sections. (B) Principal-component analysis (PCA) of the lost cell distribution in samples at PND 120 and at PND 60 with noise exposure (left). PCA was performed with the local OHC loss frequencies as variables. Frequencies of cell loss were calculated in individual segments set along the longitudinal and the radial axes. The percent variation explained by each principal component (PC) is indicated in parentheses. A dotted line indicates the decision boundary of the linear discriminant analysis. Coefficients of the first principal component (middle) and the second principal component (right) were presented from basal to apical and from proximal to distal. PND, postnatal day.

The cellular pathology of NCL was more complex than that of ACL, exhibiting a highly variable pattern among samples. This may be inevitable in our paradigm of NCL, because this protocol is expected to induce milder insults to the sensory epithelium (Figure 3A and Figure 3—figure supplement 1). Our comprehensive analysis was useful in detecting higher variability of cell loss at the basal end after noise exposure (position ‘a’ against ‘e’ in Figure 3; p < 0.001, F(6,9) = 15.5) and also in aged mice, (position ‘a’ against ‘e’ in Figure 3; p < 0.05, F(8, 8)= 5.69), suggesting that vulnerability at the basal end may be intrinsically variable. Principal component analysis applied to the spatial pattern of cell loss was helpful in isolating ACL- and NCL-related parameters (Figure 3—figure supplement 1), and the results revealed that NCL had a weaker impact in the apical portion. Thus, distinct mechanisms of cellular pathology may be responsible for ACL and NCL.

### Model-based analysis of hair cell loss

The positions of putative lost cells revealed spatial clustering above the level that would be expected by chance, regardless of age and the presence or absence of noise exposure (Figure 4A). To evaluate the spatial patterns of clustering, we constructed two distinct mechanistic models (Figure 4B). In the first model, cell loss occurs stochastically, but the probability increases if adjacent cells have been lost (neighborhood effect model). In the second model, the frequency of cell loss depends on adverse factors localized along the longitudinal axis of the organ of Corti (position effect model).

![Figure 4.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig4-v1.jpg)

**Figure 4.:** (A) Evaluation of the extent of clustered cell loss by comparison with the extent of clustering based on a model of random cell loss. The extent of cell clustering in the experimental data was much higher than would have been expected from random cell loss (99% confidence intervals within two lines) (Welch’s t-test, ***p < 0.001). (B) Construction of two models of hair cell loss (upper: neighborhood effect model; lower: position effect model). Virtual cell loss data were generated from the models and compared with the experimental data (measured). (C) Evaluation of the goodness-of-fit of the two models to the experimental data using the error score, which measures the extent of deviation of the clustering properties generated by the models from those observed in real samples. (D) Assessment of the relative contributions of the two models (neighborhood effect and position effect) to achieve the best fit to the experimental data. The two models contribute differentially under various conditions. The color code shows the proportion of lost OHCs against the total OHCs. (E) Overall pattern of contribution from two models. Note that the neighborhood effect makes a stronger contribution in young adult mice, whereas the position effect makes a stronger contribution in aged mice (means ± SD). Number of samples; n = 10 (PND 30), 14 (PND 60), 9 (PND 120), and 10 (Noise). PND, postnatal day.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) A pair of ‘probability matrix’ (upper panel) and ‘cell matrix’ (lower panel). The intensities of elements in the ‘probability matrix’ indicate the probability of cell loss for the next round of the simulation runs for individual cells. White pixels in the ‘cell matrix’ indicate the locations of already lost cells in previous rounds of the simulation runs. (B) An example of simulated histograms with different amounts of two effects (neighborhood effect and position effect). These histograms indicate the frequency distribution of cell loss clusters with different sizes. (C) Comparison of experimental data and simulation results for a given cochlear sample (No. 517). A heat map (right) shows the relative similarities between the experimental data and the simulation result (reverse of the error score in Figure 4C) when the weights of the neighborhood effect and the position effect were systematically changed. The weighted average point indicated by the red dot was taken as the estimated contributions of two effects to this sample.

Fitting of the two models was comparable in samples from aged mice or after noise exposure (Figure 4C), suggesting the complex relationship between lost cell clustering, various hair cell pathologies, and the extent of cell loss. Therefore, we developed a two-component model in which both the neighborhood effect and the position effect induced cell loss, but with different weights. By controlling the weights of the two effects, it was possible to improve fitting to the experimental data. The combinations of the two effects yielding the best fit to the experimental data were plotted along with a color code for the extent of cell loss (Figure 4D and Figure 4—figure supplement 1). The overall pattern of data distribution suggests a higher contribution of the neighborhood effect in young and adult mice not exposed to noise (Figure 4E). With age, the contribution of the position effect increased, whereas noise exposure in adult mice resulted in a variable extent of damage; data points were dispersed, with highly damaged sensory epithelium experiencing a greater contribution from the position effect.

### Automatic evaluation of cell damage and detection of multiple intracellular components

Fluorescence-based detection of cytoskeletal components, such as F-actin, enabled us to obtain information about the integrity of subcellular structure in hair cells. We evaluated F-actin integrity of OHCs at multiple positions of the organ of Corti, specified by the extent of cell loss and clustering of lost cells (Figure 5A). This approach is useful for automatic evaluation of the extent of stereocilia damage at multiple points of the organ of Corti. The reduction of F-actin content in hair cells near to lost hair cells supports the neighborhood effect model of lost cell clustering, described above.

![Figure 5.](https://cdn.elifesciences.org/articles/40946/elife-40946-fig5-v1.jpg)

**Figure 5.:** (A) Automated detection of areas with variable degrees of hair cell loss, combined with evaluation of subcellular pathology. All sites of hair cell loss (white squares) were selected, and changes in the F-actin content were evaluated (upper image). White squares with dotted lines are representative analysis areas, and are enlarged at lower left. Hair cells surrounded by intact hair cells (crosses) or next to lost cells (asterisks) were compared for their F-actin content (lower right). The graph reveals loss of F-actin in hair cells adjacent to lost cells. Scale bars, 100 μm (upper) and 10 μm (lower). [n = 108 (PND 60) and 103 (Noise), paired t-test for comparison within the group, Welch’s t-test with Bonferroni’s correction for comparison of cell groups between different experimental conditions, ***p < 0.001; ns, not significant, p > 0.05.] (B) Modified ScaleS technique can be adapted to multiple immunohistochemistry of cellular and subcellular components at PND 5. Antibodies against CtBP2, VGLUT3, NF200, and SOX2 were used to detect multiple components in situ. Scale bars, 10 μm. HC, hair cell; IHC, inner hair cell; OHC, outer hair cell; PND, postnatal day.

We also tried to image subcellular components in hair cells using specific antibodies against presynaptic ribbons (C-terminal-binding protein 2, CtBP2) and synaptic vesicles (vesicular glutamate transporter type 3, VGLUT3). Similar immunocytochemical approaches were applied to other components of the organ of Corti, including axons immunopositive for high–molecular weight neurofilament protein (NF200) and supporting cells positive for SRY (sex determining region Y)-box 2 (SOX2) immunoreactivity (Oesterle et al., 2008) (Figure 5B). These results suggest that this method can be applicable to analysis of multiple cellular components in the cochlea. In this study we utilized a water immersion objective with moderate numerical aperture (NA). In future, modification of our method with an objective lens with higher NA may enable more precise imaging of intracellular structure in a scale of the entire cochlea.

In this study, we developed a rapid method for optical tissue clearing, labeling, and automated image analysis of the inner ear. Currently available tissue clearing and labeling technologies have limited applicability to hard tissues, including bone, tooth, cartilage, and tendon. Effective removal of fine hydroxyapatite crystals in hard tissues is a key to establishing clearing methods. Here, we demonstrated that our modified ScaleS method represents a powerful approach for exhaustive analysis of expression profiles in hair cells along the entire organ of Corti, using multiple antibodies. This technique can be directly applied to the characterization of genetic and environmental models of hearing loss. In future, the analytical pipeline we developed will be integrated with active elimination of bone mineral and organic components by physical principles (Lee et al., 2016). To further increase efficiency, the decalcification solution should be elaborated. Rapid decalcification can be achieved by combining EDTA with formic or hydrochloric acid (Treweek et al., 2015). A recent report also examined multiple conditions of clearing hard tissues and recommended lowering pH of the EDTA-containing decalcification solution (Tainaka et al., 2018). However, prolonged sample treatment with high concentrations of acid can reduce immunoreactivity and accelerate quenching of fluorescent proteins. Future investigations should seek to establish clearing and labeling methods optimized for a wide spectrum of hard tissue components.

System-level analysis of the organ of Corti is important for extracting the operating principles of mechanosensory transduction. In parallel, generation of a variety of model mice harboring mutations in genes involved in hearing function will facilitate functional studies. While the functional consequences of gene mutation can be assessed using standardized protocols, such as ABR, at present we have no widely approved format for the assessment of cellular pathology. The method we developed in this study may be useful for standardization of cell-based analysis. A recent study of in situ two-photon imaging of the organ of Corti revealed the detailed architecture of the mechanical framework in the sensory epithelium (Soons et al., 2015). The method described here could be combined with information about mechanical characteristics. By integrating position-specific mechanical property, fluid dynamics, and hair cell physiology, such an approach would be useful for modeling of cochlear function (Liu et al., 2015). Manual identification of more than 2500 hair cells per sample and subsequent analysis of cell loss is not possible for large sets of cleared samples from animals of different ages, genetic backgrounds, and experimental conditions. Accordingly, the analytical pipeline described here was designed to minimize manual processing. Objective comparison of position-dependent cell pathology among multiple mouse models of hearing loss will facilitate identification of critical molecular signatures associated with cochlear pathology.

## Materials and methods

For detailed procedures, see Appendix 1 and 2.

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
      <td>Genetic reagent (M. musculus)</td>
      <td>C57BL/6J</td>
      <td>Sankyo Lab (JAPAN)</td>
      <td>PRID:MGI:5658686</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>CBA/Ca</td>
      <td>Sankyo Lab (JAPAN)</td>
      <td>PRID:MGI:2159826</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Thy1-GFP line-M</td>
      <td>Jackson Lab</td>
      <td>PRID:MGI:3766828</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic  reagent (M. musculus)</td>
      <td>GO-Ateam</td>
      <td>PMID: 19720993</td>
      <td></td>
      <td>Dr. M Yamamoto (Kyoto University, Japan)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti- Myosin VIIa</td>
      <td>Proteus Biosciences</td>
      <td>cat# 25–6790 PRID:AB_10013626</td>
      <td>IHC (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Neurofilament 200</td>
      <td>SIGMA</td>
      <td>cat# N5389 PRID:AB_260781</td>
      <td>IHC (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-SOX-2</td>
      <td>EMD Millipore</td>
      <td>cat# MAB4343 PRID:AB_827493</td>
      <td>IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-CTBP2</td>
      <td>BD Bioscience</td>
      <td>cat# 612044 PRID:AB_399431</td>
      <td>IHC (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Guinea pig polyclonal anti-VGLUT3</td>
      <td>PMID: 20034056</td>
      <td></td>
      <td>IHC (1:500), Dr. H Hioki (Juntendo University, Japan)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488-conjugated mouse monoclonal anti-VE cadherin</td>
      <td>eBioscience</td>
      <td>cat# 16-1441-81 PRID:AB_15604224</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Rhodamine phalloidin</td>
      <td>Invitrogen</td>
      <td>cat# R415</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Triton X-100</td>
      <td>Nakalai-tesque</td>
      <td>cat# 12967–45</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Urea</td>
      <td>SIGMA</td>
      <td>cat# U0631-1KG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical  compound, drug</td>
      <td>N,N,N',N'-Tetrakis (2-eydroxypropyl) ethylendiamine</td>
      <td>TCI</td>
      <td>cat# T0781</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>D-sucrose</td>
      <td>Wako</td>
      <td>cat# 196–00015</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2,2',2''-nitrilotriethanol</td>
      <td>Wako</td>
      <td>cat# 145–05605</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dichloromethane</td>
      <td>SIGMA</td>
      <td>cat# 270997–100 ML</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tetrahydrofuran</td>
      <td>SIGMA</td>
      <td>cat# 186562–100 ML</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dibenzyl Ether</td>
      <td>Wako</td>
      <td>cat# 022–01466</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Methanol</td>
      <td>Wako</td>
      <td>cat# 132–06471</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>D-glucose</td>
      <td>SIGMA</td>
      <td>cat# G8270-100G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>D-sorbitol</td>
      <td>SIGMA</td>
      <td>cat# S1816-1KG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Thiodiethanol</td>
      <td>Wako</td>
      <td>cat# 205–00936</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Acrylamide</td>
      <td>Wako</td>
      <td>cat# 011–08015</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Bis-acrylamide</td>
      <td>SIGMA</td>
      <td>cat# 146072–100G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>VA-044 initiator</td>
      <td>Wako</td>
      <td>cat# 225–02111</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium dodecyl sulfate</td>
      <td>TCI</td>
      <td>cat# I0352</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FocusClear</td>
      <td>CelExplorer Labs</td>
      <td>cat# F101-KIT</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glycerol</td>
      <td>Wako</td>
      <td>cat# 075–00616</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dimethyl sulfoxide</td>
      <td>Wako</td>
      <td>cat# 043–07216</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>N-acetyl-L-hydroxyproline</td>
      <td>TCI</td>
      <td>cat# A2265</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Methyl-β-cyclodextrin</td>
      <td>TCI</td>
      <td>cat# M1356</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>γ-cyclodextrin</td>
      <td>TCI</td>
      <td>cat# C0869</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tween-20</td>
      <td>Wako</td>
      <td>cat# 167–11515</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>NIH</td>
      <td>PRID: SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism 6</td>
      <td>GraphPad Software</td>
      <td>PRID: SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>PRID: SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Microsoft Excel</td>
      <td>Microsoft</td>
      <td>PRID: SCR_016137</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Illustrator</td>
      <td>Adobe</td>
      <td>PRID: SCR_010279</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Signal processor</td>
      <td>Nihon Kouden</td>
      <td>Neuropack MEB2208</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>MATLAB codes</td>
      <td>This paper</td>
      <td></td>
      <td>https://github.com/okabe-lab/cochlea-analyzer</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>25x water- immersion objective lens</td>
      <td>Nikon</td>
      <td>N25X-APO-MP</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>25x water- immersion objective lens</td>
      <td>Olympus</td>
      <td>XPLN25XWMP</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Sound speaker</td>
      <td>TOA</td>
      <td>HDF-261–8</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Power amplifier</td>
      <td>TOA</td>
      <td>IP-600D</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Condenser microphone</td>
      <td>RION</td>
      <td>UC-31 and UN14</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Sound calibrator</td>
      <td>RION</td>
      <td>NC-74</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Noise generator</td>
      <td>RION</td>
      <td>AA-61B</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Dual channel programmable filter</td>
      <td>NF corporation</td>
      <td>3624</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Tissue acquisition

After euthanasia, mice were perfused transcardially with 4% paraformaldehyde in PBS. Osteochondral samples (cochlea embedded in temporal bones and femurs) and other soft tissues (brain, heart, stomach, lung, liver, kidney, intestine, and spleen) were isolated by standard dissection techniques.

### Decalcification

Samples were washed for 30 to 180 min in PBS containing 0.1% Triton X-100 with continuous rocking at 40 rpm. Decalcification was performed by incubating samples for 48 to 120 hr in 500 mM EDTA in PBS at 37°C, and terminated by washing samples several times with PBS.

### Tissue extraction

Samples were placed in a solution containing 3 M guanidinium chloride, 35% (w/v) D-sorbitol, 15% (w/v) D-glucose, and 4% (w/v) Triton X-100 in PBS (pH 6.0–8.0) and incubated at 37°C for 2 to 12 hr.

### Labeling with antibodies and small molecules

After tissue extraction, samples were washed with PBS containing 0.1% Triton X-100 for 30 min with continuous rocking at 40 rpm. Samples were incubated for 2 to 48 hr in a solution containing primary antibodies or small molecules (details provided in Appendix 1) with appropriate dilutions at 37°C. Unbound antibodies or small molecules were removed by washing for 30 min with PBS containing 0.1% Triton X-100, with continuous rocking at 40 rpm. Primary antibodies were detected by incubation for 12 to 48 hr with a solution containing secondary antibodies at 37°C, followed by washing as described for removal of primary antibodies. Duration of antibody incubation was adjusted depending on the size of the sample and the affinity and specificity of the antibodies.

### Adjustment of RI

For the adjustment of tissue RI, samples were incubated for 15 min to 2 hr at 37°C in a RI matching solution. The duration of this step was adjusted depending on the size and properties of the sample. Our optimized RI matching solution (RI = 1.47) contained 3 M guanidinium chloride (or 4 M urea), 60% (w/v) D-sorbitol, and 0.1% (w/v) Triton X-100 in PBS (pH 7.1). For the optimization of RI, we tested multiple RI matching solutions with their RIs ranging from 1.41 to 1.56. The RI matching solutions with their RI lower than 1.47 were made by diluting the RI matching solution with RI = 1.47 with water. The final RIs were confirmed by a refractometer. The RI matching solutions with RI = 1.52 and 1.57 were thiodiethanol and dibenzyl ether, respectively. After RI adjustment, samples were placed in a chamber with the same RI matching solution, covered by a coverslip, and imaged by a two-photon microscope. The same cochlear sample was imaged repetitively in the RI matching solutions with increasing RIs. The maximal image depth was determined by measuring the distance from the bone surface to the deepest position where fluorescence signal of MYO7A-positive hair cells can be detected (Figure 1—figure supplement 1). In total, five independent cochlear preparations were imaged.

### Microscopy and image acquisition

Imaging of IHCs and OHCs of the organ of Corti was performed on a two-photon microscope (Nikon A1MP) equipped with a mode-locked Ti:sapphire laser (Mai Tai Deep See, Spectra Physics) operated at 800 nm with a 25 × water immersion objective lens (NA = 1.10). A chamber containing the sample was filled with the RI matching solution, covered by a glass coverslip, and placed under the objective lens. The size of single horizontal images was set to 512 × 512, with pixel sizes of 0.99 × 0.99 μm and z-spacing of 1 μm. Images were successively acquired with 10–40% overlap. Image processing was performed using the ImageJ software (National Institute of Health), and three-dimensional rotation was performed using Imaris (Bitplane), FluoRender (Version 2.18, the University of Utah), and NIS-Element AR (Version 4.51, Nikon). Adjustment of fluorescence intensity along the longitudinal axis of the organ of Corti was performed using a MATLAB script written in-house (MathWorks).

### Automated cell-count and three-dimensional morphology analysis

Hair cell detection and analysis were performed automatically using custom MATLAB scripts (R2017b, MathWorks); details are provided in Appendix 2. MATLAB source code is available on GitHub (Iida, 2018a; copy archived at https://github.com/elifesciences-publications/cochlea-analyzer).

#### Step 1: Stitching of multiple image stacks into a single stack

Multiple image stacks containing portions of the organ of Corti were assembled into a single image stack. Shifts of coordinates between image stacks were calculated based on cross-correlation (MATLAB ‘normxcorr2’ function). After image stitching, a blending algorithm (Rankov et al., 2005) was applied to remove sharp intensity changes in the zone of overlap.

#### Step 2: Reconstruction of linearized image

Hair cells in each image stack were detected as local intensity peaks (MATLAB ‘imregionalmax’ function). Single-linkage clustering (maximal distance of connection, 25 μm) was effective for eliminating or reducing the number of false positives. A stretch of local peaks corresponding to the entire row of hair cells were divided into segments of 200–300 μm in length. In each segment, the best-fit plane was calculated (MATLAB ‘pca’ function), together with the best-fit arc along the rows of hair cells. The multiple best-fit arcs were stitched into a continuous curve (Figure 2B). A voxel image containing the entire straightened row of hair cells was reconstructed from the image stacks, based on the stitched-fit curve and the normal vectors of the fit planes.

#### Step 3: Automated detection of IHCs

First, local correlation between the hair cell template and the voxel image of linearized epithelium was calculated by template matching (MATLAB ‘normxcorr2’ function), and the peaks of the correlation were detected. Pixels corresponding to detected peaks were grouped according to the physical size of the IHCs via connected-component labeling. These connected pixel groups (hereinafter called ‘cell candidates’) were used as a first approximation of IHC positions linked to other attributes, including correlation values and local intensity distributions.

The cell candidates were further evaluated to eliminate false positives using two successive machine learning models. The first ensemble learning method created the model for selection with predictor data consisting of areas, barycentric coordinates, correlation values, the intensities of the peaks, and the corresponding values of nearby cell candidates (MATLAB ‘fitensemble’ function with ‘GentleBoost’ method) (Friedman et al., 2000). The model was trained to calculate posterior probability (prediction score), and cell candidates with a high prediction score (~1000 candidates out of initial ~50,000) were selected and further analyzed by the second ensemble learning method (MATLAB ‘fitensemble’ function with ‘Bag’ method) (Breiman, 2001). This method was based on expanded predictors (the prediction score from the first step of the candidate and nearby candidates, and the local intensity distribution centered on the barycentric coordinates of the peaks). The cell candidates after the second selection were connected sequentially, subject to the physical constraint that the IHCs must form a single row with roughly constant intervals of more than 6 μm. The resulting putative positions of IHCs were used for fine readjustment of image linearization and three-dimensional structural analysis.

#### Step 4: Automated detection of OHCs

The image processing applied for IHCs in Step 3 was also applied to OHCs. Detection accuracy was improved by two additional evaluations based on machine learning. First, physical constraints of OHC alignment were introduced into three rows. A multiclass classification model, based on the convolutional neural network method [Neural Network Toolbox of MATLAB (LeCun et al., 1989)], sorted cell candidates into respective rows using input images each containing three rows of four or five OHCs. If the distance between two adjacent cell candidates in the same row exceeded 1.5 times the average distance, the presence of additional cells in the gap was assessed by the fourth model based on the convolutional neural network method. Input images for machine learning were sampled by placing small rectangular areas at equal distances from one another within the gap. If the model predicted the existence of additional cells in the gap, the nearest peaks of the correlation coefficient from the first template matching were recovered.

### Frameworks of machine learning models

Details of the models used in the detection are shown in Table 1 and Table 4 (Sokolova and Lapalme, 2009). Ensemble learning methods were applied to a one-dimensional predictor data set, and the convolutional neural network method was applied to a two-dimensional predictor data set (images). For the first ensemble learning in Steps 3 and 4, the GentleBoost algorithm was selected because of its superior training performance on large data sets relative to the Random Forest algorithm [GentleBoost, MATLAB ‘fitensemble’ function with ‘GentleBoost’ method (Friedman et al., 2000); Random Forest, ‘Bag’ method in MATLAB (Breiman, 2001)].

**Table 4.**
 Number of training and test dataset, and performance evaluation of machine learning models (related to Figure 2).


<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th colspan="2">Training</th>
      <th colspan="2">Test</th>
      <th rowspan="2">Recall</th>
      <th rowspan="2">Precision</th>
      <th rowspan="2">F score</th>
    </tr>
    <tr>
      <th>Total (n)</th>
      <th>Positive labels (n)</th>
      <th>Total (n)</th>
      <th>Positive labels (n)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IHC* 1</td>
      <td>607,954</td>
      <td>5906</td>
      <td>578,851</td>
      <td>5741</td>
      <td>0.961</td>
      <td>0.941</td>
      <td>0.951</td>
    </tr>
    <tr>
      <td>IHC* 2</td>
      <td>37,576</td>
      <td>11,977</td>
      <td>18,104</td>
      <td>5753</td>
      <td>0.977</td>
      <td>0.986</td>
      <td>0.981</td>
    </tr>
    <tr>
      <td>OHC† 1</td>
      <td>1,112,659</td>
      <td>20,576</td>
      <td>1,099,519</td>
      <td>19,959</td>
      <td>0.978</td>
      <td>0.914</td>
      <td>0.945</td>
    </tr>
    <tr>
      <td>OHC† 2</td>
      <td>28,702</td>
      <td>20,576</td>
      <td>27,185</td>
      <td>19,959</td>
      <td>0.959</td>
      <td>0.979</td>
      <td>0.969</td>
    </tr>
    <tr>
      <td>OHC† 3</td>
      <td>20,416</td>
      <td>Row1: 6706 Row2: 6745 Row3: 6965</td>
      <td>19,594</td>
      <td>Row1: 6421 Row2: 6450 Row3: 6723</td>
      <td>0.993‡</td>
      <td>0.993‡</td>
      <td>0.993‡</td>
    </tr>
    <tr>
      <td>OHC† 4</td>
      <td>4114</td>
      <td>1365</td>
      <td>2990</td>
      <td>905</td>
      <td>0.920</td>
      <td>0.946</td>
      <td>0.933</td>
    </tr>
  </tbody>
</table>

_*. IHC, inner hair cell.†. OHC, outer hair cell.‡. Calculated by micro-average of recall and precision (Sokolova M and Lapalme G, 2009)_

### Evaluation of automated detection system for hair cells

The detection efficiency of the system is shown in Table 2. The models used in the system were trained on ten cochleae as described above, and the efficiency of the trained system was evaluated on ten other cochleae. The results of auto-detection were compared against a reference created by independent manual counting by three human operators. The reference contains fluorescent objects judged to be hair cells by at least two operators.

### Analysis of spatial distribution of OHCs

Loss of OHCs results in formation of spatial gaps. To evaluate the extent of cell loss, conventional manual counting estimates the number of lost cells based on the sizes of spatial gaps. In this study, a method that can directly and systematically evaluate the sizes of holes without assuming horizontal rows of hair cells was introduced. The first step of this method was equalization of the coordinates of detected cells throughout the cochlear. Cell positions were adjusted to normalize the average intercellular distance both horizontally and vertically, and to normalize the intercellular distances along the entire organ of Corti. Subsequent placement of square areas with positions matched to the normalized coordinates of detected hair cells left connected pixel groups corresponding to the spaces of putative lost cells. Details of these analyses are provided in Appendix 2.

### Principal component analysis on OHC loss frequency

Principal component analysis was performed on the OHC loss frequency along the longitudinal and radial axes of NCL and ACL samples. Variables were the frequency of OHC loss in specific spatial segments. These spatial segments were 13 longitudinal and 15 radial segments that equally divide the total area. A singular value decomposition algorithm was utilized for the calculation of coefficients for the first and second principal components (‘svd’ option of MATLAB ‘pca’ function).

### Analysis of the three-dimensional structure of the cochlea

The spiral structure of the cochlea was analyzed based on the three-dimensional spatial distribution of IHCs because these cells formed a row that was rarely disturbed. Details of these analyses are provided in Appendix 2.

### Simulation analysis of clustered cell loss

It was observed that lost OHCs tended to be clustered. Simulation analysis was performed to evaluate two independent factors that could be responsible for such clustering. (1) A lost cell increases the probability that neighboring cells will be lost (Model 1; neighborhood effect). (2) Cell loss takes place with a probability that is a function of the local environment of the sensory epithelium (Model 2; position effect). The simulation was performed on each cochlea sample, using the measured ratio of cell loss, the number of clusters, and the cluster sizes. The simulation was performed on two matrices, the ‘cell matrix’ and ‘probability matrix’, with sizes of 3 rows × 600 columns corresponding to the distribution of OHCs (Figure 4—figure supplement 1). The cell matrix recorded the positions of cell loss, and the probability matrix recorded the probabilities of cell loss in each step of the simulation.

Each operation started with a cell matrix with no lost cells and a probability matrix with or without an initial position effect. In each step, a single cell was selected for removal with a probability given by the probability matrix, and the position was recorded in the cell matrix. The operation was stopped when the total number of lost cells reached the number of cells lost in a given sample.

The neighborhood effect was created by adding an additional weight to the adjacent probability matrix elements. To introduce the position effect, random numbers were generated according to a power-law distribution calculated by the following function.

$$
P(x)=0.1\timesp\timesX^{(1−0.1\timesp)},
$$

where p is the parameter controlling the shape of distribution. The values along the row of the probability matrix were obtained from the function P(x), with input x drawn from a uniform distribution between 0 and 1. Values in the same column were set to be identical. Gaussian filtering was applied to the probability matrix to broaden the peak width.

A panel of 16 simulated histograms was created for each sample by changing the relative weights of two effects (neighborhood and position effects) (Figure 4—figure supplement 1). The operation was repeated 500 times for each parameter set. A histogram of cluster size was constructed, and similarity to the measured data was evaluated (Figure 4—figure supplement 1). The extent of histogram dissimilarity between measured and simulation results was calculated by the sum of squared errors (error score), and a two-dimensional heat map was created (Figure 4—figure supplement 1). The weighted average of the top three combinations of weights was calculated and taken to represent the relative contribution of two factors to cell loss events.
