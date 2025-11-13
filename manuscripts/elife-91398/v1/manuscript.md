# Machine learning of dissection photographs and surface scanning for quantitative 3D neuropathology

## Authors

- Harshvardhan Gazula<sup>1</sup>
- Henry FJ Tregidgo<sup>2</sup> ([ORCID: 0000-0002-3509-8154](https://orcid.org/0000-0002-3509-8154))
- Benjamin Billot<sup>3</sup>
- Yael Balbastre<sup>1</sup>
- Jonathan Williams-Ramirez<sup>1</sup>
- Rogeny Herisse<sup>1</sup>
- Lucas J Deden-Binder<sup>1</sup>
- Adria Casamitjana<sup>2</sup>
- Erica J Melief<sup>5</sup>
- Caitlin S Latimer<sup>5</sup>
- Mitchell D Kilgore<sup>5</sup> ([ORCID: 0000-0003-1101-6924](https://orcid.org/0000-0003-1101-6924))
- Mark Montine<sup>5</sup>
- Eleanor Robinson<sup>2</sup>
- Emily Blackburn<sup>2</sup>
- Michael S Marshall<sup>6</sup>
- Theresa R Connors<sup>6</sup>
- Derek H Oakley<sup>6</sup>
- Matthew P Frosch<sup>6</sup>
- Sean I Young<sup>1</sup>
- Koen Van Leemput<sup>1</sup>
- Adrian V Dalca<sup>1</sup>
- Bruce Fischl<sup>1</sup>
- Christine L MacDonald<sup>8</sup>
- C Dirk Keene<sup>5</sup> ([ORCID: 0000-0002-5291-1469](https://orcid.org/0000-0002-5291-1469))
- Bradley T Hyman<sup>6</sup> ([ORCID: 0000-0002-7959-9401](https://orcid.org/0000-0002-7959-9401))
- Juan E Iglesias<sup>1</sup> ([ORCID: 0000-0001-7569-173X](https://orcid.org/0000-0001-7569-173X)) †

### Affiliations

1. Martinos Center for Biomedical Imaging, MGH and Harvard Medical School Charlestown United States ([ROR:002pd6e78](https://ror.org/002pd6e78))
2. Centre for Medical Image Computing, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))
3. Computer Science and Artificial Intelligence Laboratory, MIT Cambridge United States ([ROR:042nb2s44](https://ror.org/042nb2s44))
4. Biomedical Imaging Group, Universitat Politècnica de Catalunya Barcelona Spain ([ROR:03mb6wj31](https://ror.org/03mb6wj31))
5. BioRepository and Integrated Neuropathology (BRaIN) Laboratory and Precision Neuropathology Core, UW School of Medicine Seattle United States ([ROR:00cvxb145](https://ror.org/00cvxb145))
6. Massachusetts Alzheimer Disease Research Center, MGH and Harvard Medical School Charlestown United States ([ROR:002pd6e78](https://ror.org/002pd6e78))
7. Neuroscience and Biomedical Engineering, Aalto University Espoo Finland ([ROR:020hwjq30](https://ror.org/020hwjq30))
8. Department of Neurological Surgery, UW School of Medicine Seattle United States ([ROR:00cvxb145](https://ror.org/00cvxb145))

† Corresponding author

## Abstract

We present open-source tools for three-dimensional (3D) analysis of photographs of dissected slices of human brains, which are routinely acquired in brain banks but seldom used for quantitative analysis. Our tools can: (1) 3D reconstruct a volume from the photographs and, optionally, a surface scan; and (2) produce a high-resolution 3D segmentation into 11 brain regions per hemisphere (22 in total), independently of the slice thickness. Our tools can be used as a substitute for ex vivo magnetic resonance imaging (MRI), which requires access to an MRI scanner, ex vivo scanning expertise, and considerable ﬁnancial resources. We tested our tools on synthetic and real data from two NIH Alzheimer’s Disease Research Centers. The results show that our methodology yields accurate 3D reconstructions, segmentations, and volumetric measurements that are highly correlated to those from MRI. Our method also detects expected diﬀerences between post mortem conﬁrmed Alzheimer’s disease cases and controls. The tools are available in our widespread neuroimaging suite ‘FreeSurfer’ (https://surfer.nmr.mgh.harvard.edu/fswiki/PhotoTools).

## Introduction

Morphometric measurements such as cortical thickness and subcortical volumetry can be used as surrogate biomarkers of aging (Salat et al., 2004; Walhovd et al., 2005; Coupé et al., 2017) and disease (Lerch et al., 2005; Desikan et al., 2009; Dickerson et al., 2009; Blanken et al., 2017) via conﬁrmed histopathological changes. Integrating neuroimaging tools with neuropathological assessments can enable neuropathological–neuroimaging correlations for studying neurodegenerative diseases, that is, connecting macroscopic imaging with histological ground truth derived from microscopic imaging (Webster et al., 2021). While ante mortem magnetic resonance imaging (MRI) studies provide accurate and reliable morphometric data, they are often unavailable or occur too long before death, impeding reliable histopathological correlation. Cadaveric MRI can circumvent these challenges, but logistic and legal issues often complicate this procedure.

An alternative to cadaveric imaging is ex vivo MRI, which enables high-resolution image acquisition free of subject motion and other physiological noise (Edlow et al., 2019). However, ex vivo MRI also has disadvantages, including: tissue degradation due to bacteria and autolysis from death to initiation of tissue ﬁxation; cross-linking of proteins due to ﬁxation that dramatically changes MRI properties of the tissue; and image artifacts caused by magnetic susceptibility interfaces that do not occur in vivo (Shatil et al., 2016).

While ex vivo MRI is relatively uncommon in brain banks that seek to establish neuropathological–neuroimaging correlations (Ravid, 2009; Love, 2005), dissection photography is routine in nearly every brain bank. Collected specimens are typically dissected into coronal slices and photographed before further blocking and histological analysis. These photographs, often underutilized, are an invaluable information resource that, if leveraged appropriately, can play a vital role in advancing our understanding of various brain functions and disorders — mainly when ex vivo MRI is unavailable. To this end, we propose a novel software suite that, for the ﬁrst time, enables three-dimensional (3D) reconstruction and quantitative 3D morphometry of dissection photographs, powered by modern machine learning techniques (Goodfellow et al., 2016) and 3D surface scanning (Salvi et al., 2004). Provided that the photographs satisfy some basic requirements (presence of a ruler or ﬁducial markers to estimate pixel sizes), our tools enable volumetric analysis of brain structures from the photographs, computationally guided dissection via automated segmentation, and accurate spatial mapping for neuropathological–neuroimaging correlation.

Our suite is freely available and includes three modules. The ﬁrst module is a set of preprocessing routines for the photographs that enables the correction of perspective and calibration of pixel sizes. The second module is a joint image registration algorithm that allows 3D reconstruction of the photographs using a 3D surface scan of the brain as a reference. This module can also use a probabilistic atlas as a reference for the reconstruction, thus circumventing the need for a surface scanner. This scan-free mode enables retrospective analysis of photographs without corresponding 3D scans, albeit with lower accuracy than if surface scanning was available. The third and ﬁnal modules use machine learning to provide a high-resolution 3D image segmentation of the reconstructed stack. This module combines a state-of-the-art deep segmentation neural network (a U-Net, Ronneberger et al., 2015) with a domain randomization approach (Billot et al., 2023a), thus enabling analysis of photographs with diﬀerent intensity proﬁles, for example, acquired under various illumination conditions, with diﬀerent cameras or camera settings, or from ﬁxed or fresh tissue. Moreover, the machine learning method enables the estimation of ‘smooth’, isotropic segmentations that accurately interpolate across the gaps between the coronal planes captured in the photographs.

We note that this article extends our previous conference paper (Tregidgo et al., 2020) by (1) improving upon the 3D reconstruction methods; (2) using machine learning (rather than Bayesian methods) to produce segmentations that are more accurate and also isotropic (i.e., provide labels in between slices); and (3) providing extensive experiments on diﬀerent synthetic and real datasets. The rest of this article is organized as follows. First, we present results on three diﬀerent datasets, both synthetic (which enable ﬁne-grained analysis with known ground truth) and real (which enables evaluation in real-world scenarios). Next, we discuss these results and their impact on quantitative post mortem neuroimaging without MRI. Finally, the Methods section elaborates on the technicalities of the preprocessing steps, the reconstruction algorithm, and the deep learning segmentation method.

## Results

### Volumetric group study of post mortem conﬁrmed Alzheimer’s disease

One of the main use cases of our tools is the volumetric analysis of diﬀerent cerebral regions of interest (ROIs) from dissection photographs, without requiring cadaveric or ex vivo MRI. We used our tools to analyze 21 post mortem conﬁrmed Alzheimer’s disease (AD) cases from the Massachusetts Alzheimer’s Disease Research Center (MADRC), as well as 12 age-matched controls (N = 33 in total). We note that these cases comprise thick (∼10 mm) slabs, sliced by hand, without cutting guides – as cutting on anatomic landmarks was prioritized over consistent slice thickness. Therefore, this dataset is representative of a challenging, real-world scenario.

Examples of the inputs and outputs of the pipeline can be found in Figure 1 and Video 1 in the supplementary material (also available at https://youtu.be/wo5meYRaGUY). The 3D surface scan (Figure 1a) reveals the coarse shape of the specimen, in this case a left hemisphere. Our preprocessing tools correct for the perspective and pixel size of routine dissection photographs (b). Then, the 3D reconstruction tool uses information from the surface scan to produce a 3D reconstruction of the photographs into an imaging volume (c). This volume consists of highly anisotropic voxels, since the slice thickness is much larger than the pixel size of the photograph. The 3D reconstruction is fed to our machine learning segmentation method (Photo-SynthSeg), which produces a high-resolution, isotropic segmentation (d, e), independently of the slice thickness. The segmentations are then used to compare the volumes of brain ROIs between the two groups (e.g., the hippocampus, as in Figure 1f).

![Video 1.](https://cdn.elifesciences.org/articles/91398/elife-91398-video1.mp4.jpg)

![Figure 1.](https://cdn.elifesciences.org/articles/91398/elife-91398-fig1-v1.jpg)

**Figure 1.:** (a) Three-dimensional (3D) surface scan of left human hemisphere, acquired prior to dissection. (b) Routine dissection photography of coronal slabs, after pixel calibration, with digital rulers overlaid. (c) 3D reconstruction of the photographs into an imaging volume. (d) Sagittal cross-section of the volume in (c) with the machine learning segmentation overlaid. The color code follows the FreeSurfer convention. Also, note that the input has low, anisotropic resolution due to the large thickness of the slices (i.e., rectangular pixels in sagittal view), whereas the 3D segmentation has high, isotropic resolution (squared pixels in any view). (e) 3D rendering of the 3D segmentation into the diﬀerent brain regions, including hippocampus (yellow), amygdala (light blue), thalamus (green), putamen (pink), caudate (darker blue), lateral ventricle (purple), white matter (white, transparent), and cortex (red, transparent). (f) Distribution of hippocampal volumes in post mortem conﬁrmed Alzheimer’s disease vs controls in the MADRC dataset, corrected for age and gender.

Table 1 shows the area under the receiver operating characteristic curve (AUROC) and the p-value for non-parametric Wilcoxon rank sum tests (Mann and Whitney, 1947) comparing the ROI volumes of AD vs controls; we leave the accumbens area and ventral diencephalon out of the analysis as their segmentations are not reliable due to poor contrast (Fischl et al., 2002). We note that the AUROC is the non-parametric equivalent of the eﬀect size; a value of 0.5 represents chance, while 1.0 represents perfect separation. Age and gender were corrected with a general linear model, whereas volumes of contralateral ROIs were averaged when full brains (rather than hemispheres) were available. Our method successfully captures well-known atrophy patterns of AD, such as hippocampal atrophy and ventricle enlargement.

**Table 1.**
 Area under the receiver operating characteristic curve (AUROC) and p-value of a non-parametric Wilcoxon rank sum test comparing the volumes of brain regions for Alzheimer’s cases vs controls.The volumes were corrected by age and sex using a general linear model. We note that the AUROC is bounded between 0 and 1 (0.5 is chance) and is the non-parametric equivalent of the eﬀect size (higher AUROC corresponds to larger diﬀerences). The sample size is $N=33$.


<table>
  <thead>
    <tr>
      <th>Region</th>
      <th>Wh matter</th>
      <th>Cortex</th>
      <th>Vent</th>
      <th>Thal</th>
      <th>Caud</th>
      <th>Putamen</th>
      <th>Pallidum</th>
      <th>Hippoc</th>
      <th>Amyg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AUROC</td>
      <td>0.45</td>
      <td>0.52</td>
      <td>0.73</td>
      <td>0.48</td>
      <td>0.65</td>
      <td>0.64</td>
      <td>0.77</td>
      <td>0.75</td>
      <td>0.77</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>0.666</td>
      <td>0.418</td>
      <td>0.016</td>
      <td>0.596</td>
      <td>0.086</td>
      <td>0.092</td>
      <td>0.005</td>
      <td>0.009</td>
      <td>0.007</td>
    </tr>
  </tbody>
</table>

### Quantitative evaluation of segmentation with Photo-SynthSeg

While the AD experiment illustrates the ability of our method to detect diﬀerences in real-world data, it is crucial to speciﬁcally assess the accuracy of our segmentation and 3D reconstruction methods. To evaluate Photo-SynthSeg, we 3D reconstructed the brain volumes from the photographs of 24 cases from the AD Research Center at the University of Washington (UW-ADRC), which were cut into uniform 4 mm thick slices. Crucially, isotropic FLAIR MRI scans were acquired for these specimens ex vivo prior to dissection, which enables the use of MRI as gold standard.

We compare Photo-SynthSeg against ‘SAMSEG’, which is (to the best of our knowledge) the only available competing method. SAMSEG is a segmentation algorithm which we originally conceived for brain MRI (Puonti et al., 2016), and which employs Bayesian techniques to segment MRI scans irrespective of their contrast and pulse sequence. As we showed in Tregidgo et al., 2020, this technique can be adapted to 3D reconstructed photographs. Figure 2 shows the segmentation of an UW-ADRC case using both methods. As opposed to SAMSEG, Photo-SynthSeg eﬀectively ‘interpolates’ the segmentation in between slices, independently of their thickness, and is more robust against uneven intensities than the Bayesian method. Photo-SynthSeg also includes a volumetric parcellation of the cortex based on the original SynthSeg pipeline (Billot et al., 2023a), which relies on the Desikan–Killiany atlas (Desikan et al., 2006).

![Figure 2.](https://cdn.elifesciences.org/articles/91398/elife-91398-fig2-v1.jpg)

**Figure 2.:** Note that Photo-SynthSeg supports subdivision of the cortex with tools of the SynthSeg pipeline.

To evaluate Photo-SynthSeg and SAMSEG quantitatively, we computed Dice scores against manual segmentations made on a single selected slice per subject. This slice is visually chosen to be close to the mid-coronal plane, while maximizing visibility of subcortical structures; an example of such slice, along with the manual and automated segmentations, is shown in Appendix 1—figure 3. The Dice scores are displayed in Figure 3; as in the previous analysis, the accumbens area and ventral diencephalon are left out of the analysis. The ﬁgure also shows two ablations: using a probabilistic atlas instead of the case-speciﬁc reference; and using a version of Photo-SynthSeg dedicated to 4 mm slice thickness (i.e., the thickness of the UW-ADRC dataset, rather than using the general, thickness-agnostic model). The former assesses the impact of having to rely on a generic atlas when surface scans are not available, whereas the latter evaluates the ability of our neural network to adapt to thicknesses that are not known a priori (thanks to our domain randomization approach). The results show that Photo-SynthSeg generally outperforms SAMSEG, producing Dice scores over 0.8 for all structures except the amygdala – even though SAMSEG is better at segmenting the ventricles, thanks to their large size and strong contrast. The plots also show that using the probabilistic atlas produces realistic enough reconstructions, such that the two-dimensional (2D) Dice scores remain high. Finally, the results also show the superiority of the thickness randomization strategy over the ﬁxed spacing strategy, even if the latter had access to the ground truth spacing of the photographs. Even though the reader may initially ﬁnd this result counterintuitive, it is consistent with our previous ﬁndings in MRI segmentation, where domain randomization strategies also outperformed targeted simulations (Billot et al., 2020).

![Figure 3.](https://cdn.elifesciences.org/articles/91398/elife-91398-fig3-v1.jpg)

**Figure 3.:** Box plots are shown for SAMSEG, Photo-SynthSeg, and two ablations: use of probabilistic atlas and targeted simulation with 4 mm slice spacing. Dice is computed in two-dimensional (2D), using manual segmentations on select slices. We also note that the absence of extracerebral tissue in the images contributes to high Dice for the cortex.

This evaluation with Dice scores above is direct, but: (1) is based on a relatively small number of slices, and (2) disregards the ultimate purpose of segmentation, which is downstream analysis in 3D (e.g., volumetry). For this purpose, we also indirectly evaluated the methods by analyzing the volumes of brain ROIs derived from the segmentations of the whole stack. Speciﬁcally, we correlated these volumes with silver standard values derived from the isotropic FLAIR MRI scans using our ‘standard’ SynthSeg for MRI (Billot et al., 2023a). Table 2 shows the correlations and p-values for Steiger tests comparing the correlation coeﬃcients achieved by SAMSEG and Photo-SynthSeg – while considering their dependency due to the common ground truth sample. The results show once more that Photo-SynthSeg outperforms SAMSEG for nearly every structure – and in the few cases in which it does not, the Steiger test does not yield statistically signiﬁcant diﬀerences. We note that the correlations are above 0.8 for most brain structures, indicating that the 3D reconstructed photographs yield usable volumes in volumetric analysis. We also note that the correlations are slightly but consistently lower for the reconstructions with the probabilistic atlas, yielding correlations close to 0.8 for most brain regions.

**Table 2.**
 Correlations of volumes of brains regions estimated by SAMSEG and Photo-SynthSeg from the photographs against the ground truth values derived from the magnetic resonance imaging (MRI).The p-values are for Steiger tests comparing the correlations achieved by the two methods (accounting for the common sample).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">Mask from MRI as reference</th>
      <th colspan="3">Probabilistic atlas as reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>SAMSEG</td>
      <td>Photo-SynthSeg</td>
      <td>p-value</td>
      <td>SAMSEG</td>
      <td>Photo-SynthSeg</td>
      <td>p-value</td>
    </tr>
    <tr>
      <td>White matter</td>
      <td>0.935</td>
      <td>0.981</td>
      <td>0.0011</td>
      <td>0.886</td>
      <td>0.935</td>
      <td>0.0117</td>
    </tr>
    <tr>
      <td>Cortex</td>
      <td>0.930</td>
      <td>0.979</td>
      <td>0.0001</td>
      <td>0.889</td>
      <td>0.920</td>
      <td>0.0366</td>
    </tr>
    <tr>
      <td>Ventricle</td>
      <td>0.968</td>
      <td>0.988</td>
      <td>0.0004</td>
      <td>0.980</td>
      <td>0.993</td>
      <td>0.0006</td>
    </tr>
    <tr>
      <td>Thalamus</td>
      <td>0.812</td>
      <td>0.824</td>
      <td>0.4350</td>
      <td>0.812</td>
      <td>0.824</td>
      <td>0.4252</td>
    </tr>
    <tr>
      <td>Caudate</td>
      <td>0.719</td>
      <td>0.779</td>
      <td>0.2525</td>
      <td>0.733</td>
      <td>0.792</td>
      <td>0.2062</td>
    </tr>
    <tr>
      <td>Putamen</td>
      <td>0.904</td>
      <td>0.779</td>
      <td>0.9923</td>
      <td>0.872</td>
      <td>0.792</td>
      <td>0.9598</td>
    </tr>
    <tr>
      <td>Pallidum</td>
      <td>0.727</td>
      <td>0.694</td>
      <td>0.6171</td>
      <td>0.676</td>
      <td>0.658</td>
      <td>0.5698</td>
    </tr>
    <tr>
      <td>Hippocampus</td>
      <td>0.830</td>
      <td>0.757</td>
      <td>0.8873</td>
      <td>0.764</td>
      <td>0.776</td>
      <td>0.4293</td>
    </tr>
    <tr>
      <td>Amygdala</td>
      <td>0.598</td>
      <td>0.703</td>
      <td>0.1663</td>
      <td>0.576</td>
      <td>0.763</td>
      <td>0.0221</td>
    </tr>
  </tbody>
</table>

### Quantitative evaluation of reconstruction with digitally sliced MRI data

In addition to the segmentation, it is also desirable to evaluate the 3D reconstruction algorithm with the registration error (in mm). Measuring such error with real data would require manual annotation of pairs of matching landmarks, which is labor-intensive, error-prone, and not reproducible. Instead, we use simulated (digitally sliced) data created from MRI scans. While errors estimated this way may be optimistic compared with real sliced tissue, this approach enables us to analyze the error as a continuous function of slice thickness without manual annotation eﬀort.

For this purpose, we used 500 subjects from the Human Connectome Project (HCP) dataset, which includes T1- and T2-weighted MRI scans acquired at 0.7 mm isotropic resolution. After skull stripping with FreeSurfer (Fischl, 2012), we simulated dissection photographs and matching surface scans by: (1) digitally slicing the T2 scans and (2) using the surface of the T1 as a 3D reference to reconstruct the T2 slices. Speciﬁcally, we simulated slices with $S\times0.7$ mm thickness ($S=2,4,8,16$), including random aﬃne transforms and illumination ﬁelds for every simulated slice (see example in Appendix 1—figure 1). While we could use a nonlinear model, the results would depend heavily on the strength of the simulated deformation. Instead, we keep the warps linear as we believe that the value of this experiment lies in the trends that the errors reﬂect, that is, their relative rather than absolute value.

After digitally distorting the images, we used our method to 3D reconstruct the slices into their original shape. The registration error was calculated as the mean voxel displacement in mm between the reconstructed and ground truth T2 slices. Additionally, to test the robustness of the reconstruction algorithm to uneven slice spacing during dissection, we also analyze the error when a random variation of the nominal thickness (thickness jitter) is introduced for every slice.

Figure 4 shows the box plot for the mean reconstruction error as a function of the slice spacing and thickness jitter. The results show that the reconstruction error is reasonably robust to increased slice spacing. On the other hand, thickness jitter yields greater increases in reconstruction error, particularly at larger slice spacings. This result highlights the importance of keeping the slice thickness as constant as possible during acquisition.

![Figure 4.](https://cdn.elifesciences.org/articles/91398/elife-91398-fig4-v1.jpg)

**Figure 4.:** The ﬁgure shows box plots for the mean reconstruction error as a function of spacing and thickness jitter. A jitter of $j$ means that the nth slice is randomly extracted from the interval $[n−j,n+j]$ (rather than exactly $n$). The center of each box represents the median; the edges of the box represent the ﬁrst and third quartiles; and the whiskers extend to the most extreme data points not considered outliers (not shown, in order not to clutter the plot).

## Discussion

Neuroimaging to neuropathology correlation studies explore the relationship between gold-standard pathological diagnoses and imaging phenotypes by transferring the microscopic signatures of pathology to in vivo MRI. A signiﬁcant impediment to this eﬀort is the lack of quantitative tools for post mortem tissue analysis. For example, quantitative measurements such as cortical thickness and speciﬁc regional atrophy are often estimated qualitatively from 2D coronal slices during gross examination. A solution to this problem is leveraging dissection photography of these coronal slices routinely acquired before histology. By designing algorithms to reconstruct 3D volumes from 2D photographs and subsequently segment them, we have enabled a cost-eﬀective and time-saving link between morphometric phenotypes and neuropathological diagnosis.

Our new tools are publicly available and utilize modern deep learning techniques and surface scanning. Being available as part of FreeSurfer makes the tools easy to use by anyone with little or no training. Furthermore, the absence of tunable parameters in Photo-SynthSeg makes the results produced by our methods highly reproducible, and the robustness of the tools enables widespread application to heterogeneous datasets. This robustness has been demonstrated by applying the tools to images from two diﬀerent biobanks, with diﬀerent slice thickness, tissue processing, and photographic setup. On the UW-ADRC dataset, for which MRI scans were available, we achieved correlations above 0.8 between the volumes derived from the photographs and the ground truth obtained from the MRI.

Retrospective reconstruction of datasets with no accompanying surface scan available can be achieved with a probabilistic atlas. However, such a reconstruction is laden with ambiguities because the probabilistic atlas does not have access to the true shape of the tissue – which the surface scan directly measures. Whether the increased reconstruction error is tolerable depends on the downstream task, for example, shape analysis vs volumetry.

While deep learning segmentation tools are increasingly common in medical imaging research, their practical applicability in modalities with highly varying appearance (like dissection photography) has been hindered by their limited generalization ability. Photo-SynthSeg circumvents this problem by building on our recent work on domain randomization (Billot et al., 2023a), and can segment 3D reconstructed stacks of photographs irrespective of the thickness of the slices and of the contrast properties of the tissue. Compared with SAMSEG, Photo-Synthseg also has the advantage of estimating the segmentation in between slices (Figure 2). Moreover, Photo-Synthseg inherits the computational eﬃciency of neural networks, and can segment a whole case in a few seconds (or tens of seconds if no graphics processing unit [GPU] is available) without any special requirements on machine learning expertise – thus enabling broad applicability.

While registration and volumetric segmentation enable morphometry and neuropathology–neuroimaging correlation, precise white matter and pial surface placement on 3D reconstructed photographs are crucial for accurate cortical analyses – for example, producing topologically correct segmentations, as opposed to volumetric segmentations that can, for example, leak across gyri. In the future, we will extend Photo-SynthSeg to enable surface analysis for cortical placement and parcellation. While the convoluted nature of cortical surfaces makes this task diﬃcult for photographic volumes, integrating the triangular mesh provided by the surface scanner could enable accurate surface placement.

Another direction of future work will be extending the tools to axial and sagittal slices of the cerebellum and brainstem. While adapting the 3D reconstruction (Equation 1) is straightforward, the U-Net will need additional image synthesis and manual labeling eﬀorts – particularly if one wishes to include new regions, such as brainstem nuclei. Additional future analyses will include: correlating the segmentation-derived volumes with clinical scores, disease subtypes, and disease duration; using techniques like SynthSR (Iglesias et al., 2023) to improve the resolution of the reconstructed volumes; exploring nonlinear deformation models for the 3D reconstruction; fully automatizing tissue segmentation from the background using neural networks; and extending the tools to 3D analysis of histological sections.

Leveraging the vast amounts of dissection photographs available at brain banks worldwide to perform morphometry is a promising avenue for enhancing our understanding of various neurodegenerative diseases. Our new tools will allow extraction of quantitative phenotypical information from these photographs – and thus augmentation of histopathological analysis. We expect this new methodology to play a crucial role in the discovery of new imaging markers to study neurodegenerative diseases.

## Materials and methods

### Datasets

#### MADRC

Dissection photography of ﬁxed tissue and companion surface scans for 76 cases from the Massachusetts Alzheimer’s Research Center (18 whole cerebrums and 58 hemispheres). Ruling out cases with frontotemporal dementia and other comorbidities, as well as subjects that did not pass manual quality control (by JWR, RH, and LJD), led to a ﬁnal sample size of $N=33$ (21 post mortem conﬁrmed Alzheimer’s and 12 controls). The surface scans were acquired using a turntable with an Einscan Pro HD scanner (Shining 3D, Hangzhou, China, 0.05 mm point accuracy). Slices with variable thickness were cut with a dissecting knife on a predeﬁned set of landmarks and photographed with a 15.1 MP Canon EOS 50D Digital SLR camera. Further details on the dissection and processing of the specimens can be found in Appendix 1.

#### UW-ADRC

Dissection photography of ﬁxed tissue and companion ex vivo MRI scans for 24 cases (all of them with both hemispheres) from the Alzheimer’s Disease Research Center at the University of Washington. The MRI scans were acquired at 0.8 mm isotropic resolution using a FLAIR sequence. Coronal slices were cut with 4 mm thickness using a modiﬁed deli slicer and photographed with a 35 Megapixel (MP) camera. While no 3D surface scanning was available for this dataset, we obtained surfaces by skull stripping the MRI scans and meshing the brain surface. This dataset enables us to compute volumetric measurements from the 3D reconstructed photographs and compare them with reference values obtained from the corresponding MRI scans. Furthermore, two experienced labelers manually traced the contour of nine brain regions (white matter, cortex, lateral ventricle, thalamus, caudate, putamen, pallidum, hippocampus, and amygdala) in one slice per case, which enables computation of 2D Dice scores. Further details on the dissection and processing of the specimens can be found in Appendix 1 and Latimer et al., 2023.

#### HCP

T1- and T2-weighted MRI scans of 500 subjects from the Human Connectome Project, acquired at 0.7 mm isotropic resolution. The scans were skull stripped using FreeSurfer (Fischl, 2012). We use these scans to simulate dissection photographs and matching surface scans by digitally slicing the T2 scans and using the T1 as a 3D reference to reconstruct the T2 slices. Further details on the MRI acquisition can be found in Van Essen et al., 2012.

#### T1-39

39 T1-weighted MRI scans at 1 mm isotropic resolution, with manual volumetric segmentations for 36 brain structures, which we used to train Photo-SynthSeg. We note that this is the labeled dataset that was used to build the probabilistic atlas in FreeSurfer (Fischl et al., 2002). The 36 structures include 22 that are segmented by Photo-Synthseg: left and right white matter, cortex, ventricle, thalamus, caudate, putamen, pallidum, hippocampus, amygdala, accumbens area, and ventral diencephalon. The remaining 14 labels include: four labels for the cerebellum (left and right cortex and white matter); the brainstem; ﬁve labels for cerebrospinal ﬂuid regions that we do not consider; the left and right choroid plexus; and two labels for white matter hypointensities in the left and right hemispheres.

### Surface scanning

Surface scanning (also known as ‘proﬁlometry’) is a technology that is becoming increasingly inexpensive (a few thousand dollars), mainly via structured light technology (Salvi et al., 2004). The preferred version of our proposed pipeline relies on a surface scan of the specimen (Figure 1a) acquired before slicing. This surface scan, represented by a triangular mesh, is used as an external reference to guide the 3D reconstruction of the photographs (details below). While there are no speciﬁc technical requirements for the surface scan (e.g., minimum resolution), minimizing geometric distortion (i.e., deformation) between scanning and subsequent slicing is crucial. The surface scan may be acquired with a handheld scanner with the specimen placed on a table, or with the scanner on a tripod and the sample on a turntable. As mentioned earlier, our pipeline does not strictly require the surface scan, as it can be replaced with a probabilistic atlas with a slight loss of accuracy (as shown in the Results section).

### Tissue slicing and photography

In preparation for the downstream 3D reconstruction, some requirements exist for the dissection and photography of the brain slabs. Speciﬁcally, our pipeline assumes that approximately parallel slices are cut in coronal direction – which is the standard practice in most brain banks. We further assume that the thickness of these slices is approximately constant, as ‘thickness jitter’ has a detrimental eﬀect on the results (Figure 4).

Moreover, we require the presence of ﬁducials to enable pixel size calibration and perspective correction. Ideally, four ﬁducials are placed on the corners of a rectangle of known dimensions (Figure 5a). In the absence of such ﬁducials, we require the presence of at least a ruler or two orthogonal rulers; the former enables pixel size calibration via image scaling, whereas the latter enables approximate perspective correction by ﬁtting an aﬃne transform.

![Figure 5.](https://cdn.elifesciences.org/articles/91398/elife-91398-fig5-v1.jpg)

**Figure 5.:** (a) Dissection photograph with brain slices on black board with ﬁducials. (b) Scale-invariant feature transform (SIFT) features for ﬁducial detection. (c) Photograph from (a) corrected for pixel size and perspective, with digital ruler overlaid. (d) Segmentation against the background, grouping pieces of tissue from the same slice. (e) Sagittal slice of the initialization of a three-dimensional (3D) reconstruction. (f) Corresponding slice of the ﬁnal 3D reconstruction, obtained with a surface as reference (overlaid in yellow). (g) Corresponding slice of the 3D reconstruction provided by a probabilistic atlas (overlaid as a heat map); the real surface is overlaid in light blue for comparison.

Our pipeline allows for multiple slices to be present in one photograph but requires that all photographs are of the same side of the slices (either anterior or posterior) and that the inferior–superior direction of the anatomy is approximately aligned with the vertical axis of the image (as in Figure 5a). Ideally, the slices should be photographed on a ﬂat board with a solid background color that stands out from the brain tissue, as stronger contrast between tissue and background greatly facilitates image segmentation when preprocessing the photographs (further details below).

### Preprocessing of photographs

Image preprocessing starts with geometric correction, that is, pixel size calibration and perspective correction. In the ideal scenario with four ﬁducials, the widespread widespread scale-invariant feature transform (SIFT, Lowe, 1999) is used to detect such ﬁducials (Figure 5b) and compute a spatial transform that corrects for perspective distortion and calibrates the pixel size – see Figure 5c, where the pixel size calibration enables superimposition of a digital ruler.

Our software also supports a manual mode where the user clicks on two, three, or four landmarks: two points with a known distance in between (enables approximate pixel size calibration); three points at the ends of two rulers plus their intersection (enables approximate perspective correction with an aﬃne transform); or four points on the corners of a rectangle of known dimensions (enables full perspective correction). This manual mode is useful when no ﬁducials are present, but the user can still identify features with known dimensions in the photograph, for example, on an imprinted grid pattern, or along rulers.

After geometric correction, our methods require a binary segmentation of the brain tissue, separating it from the background. While our tools do not have any speciﬁc requisites in terms of background, using a solid background with a distinct color (e.g., a ‘green screen’) can greatly facilitate segmentation; otherwise, more extensive manual intervention may be needed. In our experiments, using a ﬂat black background enabled us to automatically segment the tissue with a combination of thresholding and morphological operations, keeping manual edits to a minimum (a couple of minutes per photograph, mostly to erase bits of cortical surface that are sometimes visible around the edge of the face of the slice).

Given this binary mask, the ﬁnal preprocessing step requires the user to specify the order of the slices within the photograph – which may be anterior to posterior or vice versa, but must be consistent within and across photographs of the same case. Moreover, the user also needs to specify whether two connected components belong to the same slice, which often happens around the temporal pole. This can be quickly accomplished with a dedicated graphical user interface that we distribute with our tools (Figure 5d).

### 3D volumetric reconstruction from photographs

Recovering a 3D volume from a stack of 2D images entails a consistent 3D reconstruction of the stack via joint image alignment – known as ‘registration’ (Maintz and Viergever, 1998; Pluim et al., 2003; Zitová and Flusser, 2003; Sotiras et al., 2013). We pose 3D reconstruction as a joint optimization problem (Pichat et al., 2018; Mancini et al., 2019) and use a 3D reference volume for the registration. This volume is ideally a binary 3D mask obtained by rasterizing (ﬁlling) the triangular mesh from the surface scan. If a surface scan is not available, one can instead use a probabilistic atlas (Shattuck et al., 2008) of brain shape, which provides a rough reference for the reconstruction. However, this reference cannot drive the reconstruction toward the actual shape of the specimen nor correct deviations from the user-provided slice thickness.

Given $N$ photographed slices and their corresponding masks, the goal of this optimization framework is to simultaneously identify: (1) a set of $N$ 2D aﬃne geometric transforms ${ϕ_{n}}_{n=1,…,N}$ (rotation, translation, shear, and scaling for each slice); (2) a scaling factor $s$ in the anterior–posterior direction shared by all slices; and (3) a rigid 3D transform $Ψ$ for the reference (rotation and translation). These transforms seek to align the slices with each other and with the reference volume.

We note that aﬃne transforms (rather than rigid) are required for the photographs due to imperfections in the image preprocessing of the previous section; nevertheless, we expect the shear and scaling of these transforms to be small. Furthermore, we use aﬃne rather than nonlinear transforms because the latter compromise the robustness of the registration, as they introduce huge ambiguity in the space of solutions (e.g., one could add an identical small nonlinear deformation to every slice almost without changing the feature of the 3D reconstruction). This aﬃne model makes it particularly important to place connected components of the same slice in a correct relative position when there is more than one, for example, in the temporal pole. We further note that the scaling $s$ in the anterior–posterior direction is required to correct deviations from the slice thickness speciﬁed by the user, which in practice is never completely exact.

The optimal set of transforms is obtained by maximizing the objective function $F$ in Equation 1. This objective encodes four desired attributes of the reconstructed data, with relative weights α, β, γ, and υ:

$$
F(Ψ,{Φ_{n}})=\alphaD(M[x;{Φ_{n}},s],R[x;Ψ])+\beta\frac{1}{N−1}\sumn=1N−1C(S_{n}[x;Φ_{n},s],S_{n+1}[x;Φ_{n+1},s])+\gamma\frac{1}{N−1}\sumn=1N−1D(M_{n}[x;Φ_{n},s],M_{n+1}[x;Φ_{n+1},s])−ν\frac{1}{N}\sumn=1Nf(Φ_{n})
$$

Mathematically, overlap in Equation 1 is measured with the soft Dice coeﬃcient $D$ (Dice, 1945; Sorensen, 1948; Milletari et al., 2016); image similarity is measured with the normalized cross-correlation $C$; and the scaling and shearing are measured with the absolute value of the logarithm of the determinant of the aﬃne matrices, that is, $f(Φ_{n})$ is the absolute log-determinant of the 3 × 3 matrix encoding $Φ_{n}$. The relative weights $\alpha,\beta,\gamma,ν$ are set via visual inspection of the output on a small pilot dataset. For the surface reference, we used: $\alpha=.95,\beta=\gamma=.025,ν=\gamma/100$. For the probabilistic atlas, we trust the reference less and also use more regularization to prevent excessive deformation of slices: $\alpha=.8,\beta=\gamma=ν=.1$. Either way, the 3D reconstruction is in practice not very sensitive to the exact value of these parameters. We also note that, as opposed to the preprocessing described in the previous section, SIFT is not a good candidate for matching consecutive slices: while it is resilient against changes in pose (e.g., object rotation), perspective, and lightning, it is not robust against changes in the object itself – such as changes between one slice to the next.

The objective function $F$ is minimized with standard numerical methods – speciﬁcally the limited-memory Broyden–Fletcher–Goldfarb–Shanno (LBFGS) algorithm (Fletcher, 1987). The LBFGS optimizer is initialized by stacking the photographs with their centers of gravity on coordinate (0,0), and then matching the center of gravity of the whole stack with the center of gravity of the 3D reference (as illustrated in Video 1 in the supplement, see also https://youtu.be/wo5meYRaGUY).

If a probabilistic atlas is used instead of the surface scan, the same objective function is used but with a slightly diﬀerent search space. Since we can no longer trust the external reference to correct for ﬁne shape correction: (1) we keep the scaling factor of the anterior–posterior direction ﬁxed to $s=1$ (i.e., we trust the slice thickness speciﬁed by the user); (2) we use rigid rather than aﬃne transforms ${ϕ_{n}}$ for the slices (which also has the eﬀect of making the regularizer equal to zero); and (3) we use a full 3D aﬃne transform $Ψ$ for the reference. Sample reconstructions of a case with a 3D surface and a probabilistic atlas are shown in Figure 5e–g. The probabilistic atlas produces a plausible reconstruction, which is however far from the real shape of the specimen given by the surface (Figure 5g). An additional example from the MADRC dataset is shown in Appendix 1—figure 2. We note that 3D reconstruction is implemented in PyTorch, and runs eﬃciently on a GPU – less than 5 min on a Nvidia Quadro RTX 6000.

### Segmentation

The 3D reconstructed photographs have various applications (e.g., volumetry, computationally guided dissection) that require image segmentation, that is, assigning neuroanatomical labels to every spatial location (Pham et al., 2000; Despotović et al., 2015; Akkus et al., 2017). There are two main challenges when segmenting the 3D reconstructed photographs. First, the appearance of the images varies widely across cases due to diﬀerences in camera hardware (sensor, lens), camera settings, illumination conditions, and tissue preparation (e.g., ﬁxed vs fresh). And second, accurate volumetry requires estimating the segmentation not only on the planes of the photographs but also in between slices.

In our previous work (Tregidgo et al., 2020), we adopted a Bayesian segmentation strategy that handled the ﬁrst issue but not the second. Here, we extend a machine learning approach based on domain randomization (Tobin et al., 2017) that we have successfully applied to segment clinical brain MRI scans with large slice spacing (Billot et al., 2020; Billot et al., 2023a; Billot et al., 2023b). Speciﬁcally, our newly proposed approach ‘Photo-SynthSeg’ trains a convolutional neural network for image segmentation (a 3D U-Net, Ronneberger et al., 2015; Çiçek et al., 2019) with synthetic data as follows.

‘Photo-SynthSeg’ starts from a training dataset (the T1-39 dataset) that comprises a pool of 3D segmentations of brain images at isotropic 3D resolution (Figure 6a). At every iteration during training, one of these 3D segmentations is randomly selected and geometrically deformed with a random nonlinear transform, which simulates imperfect 3D reconstruction by including a ‘deformation jitter’ in the coronal direction, that is, small but abrupt deformations from one coronal slice to the next (Figure 6b). This deformed isotropic segmentation is used to generate a synthetic 3D image (also at isotropic resolution) using a Gaussian mixture model conditioned on the segmentation (Figure 6c). Crucially, we randomize the Gaussian parameters (means and variances) to make the neural network robust against variations in image appearance. This synthetic isotropic image is then ‘digitally sliced’ into a 3D stack of synthetic coronal photographs, each of which is independently corrupted by a random 2D smooth illumination ﬁeld that simulates inhomogeneities in the illumination of the photographs (Figure 6d). Importantly, we also randomize the thickness of the simulated slices in every iteration and introduce small stochastic variations in thickness around the central value within each simulation. This strategy makes the network agnostic to the slice thickness of the reconstructed 3D stack at test time. Finally, the simulated stack, which has anisotropic resolution (e.g., 1 mm in-plane and several mm in slice thickness), is resampled to the original isotropic resolution of the (deformed) 3D segmentation (Figure 6e) – typically 1 mm isotropic.

![Figure 6.](https://cdn.elifesciences.org/articles/91398/elife-91398-fig6-v1.jpg)

**Figure 6.:** (a) Randomly sampled input label map from the training set. (b) Spatially augmented input label map; imperfect 3D reconstruction is simulated with a deformation jitter across the coronal plane. (c) Synthetic image obtained by sampling from a Gaussian mixture model conditioned on the segmentation, with randomized means and variances. (d) Slice spacing is simulated by downsampling to low resolution. This imaging volume is further augmented with a bias ﬁeld and intensity transforms (brightness, contrast, gamma). (e) The ﬁnal training image is obtained by resampling (d) to high resolution. The neural network is trained with pairs of images like (e) (input) and (b) (target).

This generative process mimics the image formation process in the real world and has two crucial aspects. First, the super-resolution component: Photo-SynthSeg is a U-Net that will produce a high-resolution (1 mm) isotropic 3D segmentation for every input at test time, independently of the slice spacing of the 3D reconstructed stack of photographs (Figure 2). And second, domain randomization: sampling diﬀerent Gaussian parameters, illumination ﬁelds, and slice thicknesses at every iteration beyond realistic limits (as in Figure 6, where even contralateral regions have diﬀerent appearance) forces the U-Net to learn features that are independent of the intensity proﬁles of the photographs, as well as of the spacing between slices. This process makes the U-Net robust against changes in the acquisition. We note that the Gaussian distributions are univariate rather than trivariate, that is, they model grayscale rather than red–green–blue triplets; we tried training a U-Net with the latter, but the performance on color images was worse than when converting them to grayscale and using the U-Net trained with univariate Gaussians.

During training, resampled stacks and corresponding segmentations (Figure 6b–e) are fed to a U-Net. The U-Net architecture is the same as in our previous works with synthetic scans (Billot et al., 2020; Billot et al., 2023a): it consists of ﬁve levels, each separated by a batch normalization layer (Ioﬀe and Szegedy, 2015) along with a max-pooling (contracting path) or an upsampling operation (expanding path). All levels comprise two convolution layers with 3 × 3 × 3 kernels. Every convolutional layer is associated with an Exponential Linear Unit activation (Clevert et al., 2016), except for the last one, which uses a softmax. While the ﬁrst layer comprises 24 feature maps, this number is doubled after each max-pooling, and halved after each upsampling. Following the original U-Net architecture, skip connections are used across the contracting and expanding paths. The network is trained with a soft Dice loss (Milletari et al., 2016) and the Adam optimizer (Kingma and Ba, 2014). The deep learning model is implemented in Keras (Chollet, 2015) with a Tensorﬂow backend (Abadi et al., 2016) and runs on a few seconds on a Nvidia Quadro RTX 6000 GPU. Training takes around 7 days on the same GPU.

Finally, we note that there are two diﬀerent versions of Photo-SynthSeg: one for full cerebra and one for single hemispheres. The later is trained with left hemispheres and ﬂipped right hemispheres, and can thus be used as is for left hemispheres. To process a right hemisphere, we simply left–right ﬂip it, segment it, and ﬂip the results back. While the default Photo-SynthSeg pipeline segments the cerebral cortex as a whole (i.e., as in Figure 6a), our tool also oﬀers the option of subdividing it into parcels as deﬁned by the Desikan–Killiany atlas (Desikan et al., 2009), like in Figure 2. This is achieved with the cortical parcellation module (Segmenter S3) of our tool ‘SynthSeg’ (Billot et al., 2023a), which is also distributed with FreeSurfer.
