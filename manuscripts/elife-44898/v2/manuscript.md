# Computational 3D histological phenotyping of whole zebrafish by X-ray histotomography

## Authors

- Yifu Ding<sup>1</sup> ([ORCID: 0000-0002-4629-5858](https://orcid.org/0000-0002-4629-5858))
- Daniel J Vanselow<sup>1</sup> ([ORCID: 0000-0002-9221-8634](https://orcid.org/0000-0002-9221-8634))
- Maksim A Yakovlev<sup>1</sup> ([ORCID: 0000-0003-1846-3751](https://orcid.org/0000-0003-1846-3751))
- Spencer R Katz<sup>1</sup> ([ORCID: 0000-0002-5586-3562](https://orcid.org/0000-0002-5586-3562))
- Alex Y Lin<sup>1</sup> ([ORCID: 0000-0002-1653-4168](https://orcid.org/0000-0002-1653-4168))
- Darin P Clark<sup>4</sup>
- Phillip Vargas<sup>5</sup>
- Xuying Xin<sup>1</sup>
- Jean E Copper<sup>1</sup>
- Victor A Canfield<sup>1</sup> ([ORCID: 0000-0002-4359-1790](https://orcid.org/0000-0002-4359-1790))
- Khai C Ang<sup>1</sup> ([ORCID: 0000-0001-7695-9953](https://orcid.org/0000-0001-7695-9953))
- Yuxin Wang<sup>6</sup>
- Xianghui Xiao<sup>7</sup>
- Francesco De Carlo<sup>8</sup>
- Damian B van Rossum<sup>1</sup>
- Patrick La Riviere<sup>5</sup> ([ORCID: 0000-0003-3415-9864](https://orcid.org/0000-0003-3415-9864))
- Keith C Cheng<sup>1</sup> ([ORCID: 0000-0002-5350-5825](https://orcid.org/0000-0002-5350-5825)) †

### Affiliations

1. The Jake Gittlen Laboratories for Cancer Research Penn State College of Medicine Hershey United States
2. Division of Experimental Pathology, Department of Pathology Penn State College of Medicine Hershey United States
3. Medical Scientist Training Program Penn State College of Medicine Hershey United States
4. Center for In Vivo Microscopy Duke University Durham United States
5. Department of Radiology The University of Chicago Chicago United States
6. Imaging Group Omnivision Technologies, Inc. Santa Clara United States
7. National Synchrotron Light Source II Brookhaven National Laboratory Upton United States
8. Advanced Photon Source Argonne National Laboratory Lemont United States

† Corresponding author

## Abstract

Organismal phenotypes frequently involve multiple organ systems. Histology is a powerful way to detect cellular and tissue phenotypes, but is largely descriptive and subjective. To determine how synchrotron-based X-ray micro-tomography (micro-CT) can yield 3-dimensional whole-organism images suitable for quantitative histological phenotyping, we scanned whole zebrafish, a small vertebrate model with diverse tissues, at ~1 micron voxel resolutions. Micro-CT optimized for cellular characterization (histotomography) allows brain nuclei to be computationally segmented and assigned to brain regions, and cell shapes and volumes to be computed for motor neurons and red blood cells. Striking individual phenotypic variation was apparent from color maps of computed densities of brain nuclei. Unlike histology, the histotomography also allows the study of 3-dimensional structures of millimeter scale that cross multiple tissue planes. We expect the computational and visual insights into 3D cell and tissue architecture provided by histotomography to be useful for reference atlases, hypothesis generation, comprehensive organismal screens, and diagnostics.

## Introduction

Histology has been used for over a century to visualize cellular composition and tissue architecture in millimeter- to centimeter-scale tissues from diverse multicellular organisms (Virchow, 1860). Its diagnostic power is dependent on the detection and description of changes in cell and tissue architecture. Normal and abnormal cytological features indicative of physical, inflammatory, and neoplastic causes of disease are readily distinguished using established staining procedures (Kumar et al., 2015).

Despite its power, histology has practical limitations in throughput and quantitative phenotyping of cell and tissue volume and shape. Physical sectioning introduces tissue loss and distortions that compromise complete reconstruction of tissues from serial histology sections (Arganda-Carreras et al., 2010). The technical demands and physical properties of paraffin blocks limit slice thickness to ~5 µm, leading to incomplete sampling and imperfect visualization of elongated structures such as vessels and large cells that extend beyond the section thickness. As a result, only a small fraction of any given tissue sample is studied in histology. Moreover, it is intractable to generate complete sets of sections for large numbers of whole organisms (as needed for a genetic or chemical screen) and impractical to align them for volumetric analysis. A routine method for histological phenotyping that avoids these problems and enables comprehensive three-dimensional (3D) analysis of whole organisms would transform large-scale studies.

X-ray micro-tomography (micro-CT) is a potential means of achieving complete, 3D histological phenotyping for large numbers of specimens. Micro-CT is commonly used to study hard, mineralized tissues like bones and fossils (Donoghue et al., 2006; Ketcham and Carlson, 2001). Soft-tissue imaging typically requires contrast-enhancing, heavy-metal stains such as osmium tetroxide, iodine, phosphotungstic acid (PTA), or gallocyanin-chromalum (Betz et al., 2007; Metscher, 2009a; Metscher, 2009b). Phase-based synchrotron imaging of unstained samples allows the study of development in live whole Xenopus embryos over time (Moosmann et al., 2013) and of dense human cerebellar tissue (Töpperwien et al., 2018). Commercial micro-CT devices have been used to interrogate soft-tissue structure in diverse stained specimens (Badea et al., 2008; Batiste et al., 2004; Cheng et al., 2016a; Metscher, 2009a; Staedler et al., 2013), but these devices utilize polychromatic, low-flux X-ray tube sources that limit resolution and throughput. Synchrotron X-ray sources have monochromatic, high-flux beams (Winick, 1994) that allow rapid imaging of mm-scale samples such as insects (Betz et al., 2007; Mizutani et al., 2013; van de Kamp et al., 2018), vertebrate embryos (Khonsari et al., 2014; Raj et al., 2014), zebrafish (Seo et al., 2015), and mouse somatosensory cortex (Dyer et al., 2017). Micro-CT of larger samples such as whole mice or whole mouse organs have lacked adequate tissue contrast and/or resolution (~10 µm3) for histological phenotyping (Busse et al., 2018; Hsu et al., 2016). Conversely, nano-CT enables imaging at higher resolution (~100 nm3) but does not provide sufficient field-of-view for mm-scale samples. To our knowledge, no existing method has the combination of throughput, resolution, field-of-view, and soft-tissue contrast necessary for whole-organism 3D phenotypic screens that are inclusive of histopathological evaluation.

Here, we present a 3D quantitative histological analysis of features of whole fixed and stained zebrafish, at sub-micron resolution, using synchrotron micro-CT optimized for soft tissue differentiation (histotomography). We chose zebrafish, the largest established vertebrate model to fit in our field-of-view (juveniles are <3 mm in diameter), to determine conditions for attaining a degree of tissue contrast required for histopathological analysis across a range of tissues. X-ray histotomography as developed here is pan-cellular, like histology, allowing for the creation of histology-like virtual sections, but unlike histology, can be used to study millimeter-scale phenotypes involving convoluted and branched structures such as gills, gut, vessels, and nerve tracts. Histotomographic images provide a mechanism for quantitative histopathological analysis that facilitates the objective and reproducible study of volume, shape, and texture of cells across organisms and tissue types. Histotomography’s potential throughput and analytical power may be applied to computational histological phenotyping of whole organisms to probe the diversity of organismal tissue architecture and relationships between genotype, environment, and microanatomy (Austin et al., 2004; Cheng et al., 2016b; Varshney et al., 2013).

## Results

### Whole-Organism synchrotron X-ray histotomography

Synchrotron based micro-CT was chosen based on two demands of phenome projects: the potential to achieve resolutions and contrast required for histological evaluations, and high-throughput potential for phenotyping whole organisms. Fine-tuning of X-ray energies and bandwidth, and adjustment of sample-to-scintillator distance, were used to optimize volumetric reconstructions of optically-opaque zebrafish at isotropic resolutions (equal in all three dimensions) for histopathological interpretations. Synchrotron X-ray flux is orders of magnitude more brilliant than commercial tube sources, allowing imaging times short enough for high sample-number imaging projects (Winick, 1994).

Micro-CT studies were performed on the sector two bending magnet, hutch B (2-BM-B) of the Advanced Photon Source at Argonne National Laboratory for both single-energy and multi-energy acquisitions (Figure 1). Beam energies for monochromatic imaging were optimized for contrast-to-noise ratio across a range of sample diameters and concentrations of tungsten (Figure 1—figure supplement 1). A beam energy of 13.8 keV was used for the smaller, larval samples and 16.2 keV for juveniles due to their greater thickness (see Materials and methods). Sample-to-scintillator distance was adjusted to optimize the magnitude of phase contrast-based edge enhancement (Figure 1—figure supplement 2). A 30 mm sample-to-scintillator distance provided sufficient edge enhancement to achieve histology-like contrast. For whole-organism imaging, the zebrafish were vertically translated to capture segments over the full length of the sample. Each zebrafish segment was reconstructed and the multiple segments stitched into a single 3D volume (Video 1).

![Figure 1.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig1-v2.jpg)

**Figure 1.:** Quasi-parallel X-rays from beamline 2-BM-B are used to acquire projection images of an intact, fixed, and PTA-stained whole zebrafish. Total imaging time is ~20 min per monochromatic acquisition (sample-to-scintillator distance = 30 mm) and ~20 s per pink-beam acquisition (sample-to-scintillator distance = 25 mm). Each fish requires 3 to 5 acquisitions. The top inset shows the relative sizes of a juvenile (left), a larva (right), and a dime (diameter = 17.9 mm). Fish are shown embedded in acrylic resin with the polyimide tubing removed. Removal of the polyimide tubing is necessary for natural color light photography, but not for successful X-ray image acquisition. Scale bars in the specimen insets are 1 mm.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** X-ray energy was modeled for different sample sizes and metal concentrations. (Left) Analytic contrast-to-noise ratio (CNR) for tungsten contrast detail in water background assuming ρW= 0.06 g/cm3, dW = 0.36 mm, ρH20= 1.0 g/cm3 and dH20 varying from 1 to 5 mm. (Right) Analytic contrast-to-noise ratio for tungsten for contrast detail in water background assuming ρW varying from 0.01 to 0.2 g/cm3, dW = 0.36 mm, ρH20 = 1.0 g/cm3 and dH20 = 1 mm. The plots indicate that over a wide range of sample sizes and metal concentrations, an optimal energy range is ~12 to 16 keV.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** A range of sample-to-scintillator distances (SSD) was surveyed for phase contrast enhancement of edges in larval samples. A line profile (A) is drawn through the retinal region as denoted by the yellow line in (B) to highlight differences in voxel intensity at edges. Zoomed insets (C) show the photoreceptor layer aligned with the attenuation profile in (A). The attenuation range (maximum attenuation– minimum attenuation) is shown in (D) for homogenous (lens, inner plexiform layer) and variable (photoreceptor layer) regions. The attenuation range increases for variable regions but remains constant for homogenous regions as SSD increases, demonstrating the effects of phase contrast edge enhancement. A SSD of 30 mm provided a level of edge perception resembling that found in traditional glass slide histology and was used for all subsequent acquisitions.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** A juvenile (33 dpf) zebrafish was scanned using pink-beam (A) and monochromatic (B) sources. Insets show the ability for pink-beam (C) and monochromatic beam (D) to resolve the fine detail found in zebrafish photoreceptor layer. Signal-to-noise ratio (SNR) in high (eye lens) and low attenuation (brain) tissues was compared for both images (E). The monochromatic beam image has a higher SNR than the pink-beam image in both cases. While the noise in the pink beam image could be reduced by increasing acquisition times, the contrast in the monochromatic image is inherently better. A line profile (F) through the photoreceptor layer shows that the monochromatic beam is superior for discerning edges, which can be attributed to the phase contrast optimization done in Figure 1—figure supplement 1. Under these pink-beam imaging conditions, phase-contrast enhancement, which is energy-dependent, gets averaged out.

![Video 1.](https://cdn.elifesciences.org/articles/44898/elife-44898-video1.mp4.jpg)

**Video 1.:** This video demonstrates the relationship between multi-angle projection data and sinograms, which are used in reconstruction to backproject single axial slices that are combined to generate a volume (online viewing available from, https://youtu.be/MjobFBLc5m8). Best if viewed at highest quality setting.

Large-scale phenotyping studies, such as those focusing on series of mutants or chemical exposures, require short imaging times to facilitate throughput. Monochromatic acquisitions took ~20 min,~36 fold faster than acquisition by commercial tabletop sources (e.g.,~720 min for Xradia 500 series machines) (Metscher, 2009b). The use of polychromatic ‘pink-beam’ increases X-ray flux, which greatly reduces exposure times. Each pink-beam acquisition took ~20 s,~60 fold faster than monochromatic acquisition and ~2,000 fold faster than commercial sources. Monochromatic acquisitions have better image quality than pink-beam, as defined by signal-to-noise ratio and pixel intensity profile (Figure 1—figure supplement 3). Notably, no image degradation over years of repetitive synchrotron imaging was detected (Lin et al., 2018). This high degree of sample stability across multiple scans suggests the potential use of pink-beam pre-screening followed by higher resolution monochromatic reacquisition.

### Digital 3D zebrafish at cell resolution

Digital zebrafish were reconstructed from projections after staining all tissues with PTA. The similarity of digital slices to conventional histological outputs is demonstrated by representative transverse (axial), sagittal, and coronal cross-sections for larval (4 days post-fertilization, dpf) and juvenile (33 dpf) zebrafish imaged at 0.743 and 1.43 µm3 isotropic voxel resolution, respectively (Figure 2). Volume renderings illustrate the orientation of individual planes of section in 3D. Full sets of cross-sections of the zebrafish in the sagittal orientation illustrate one way to use micro-CT data to phenotype full tissue volumes (Videos 2–3).

![Figure 2.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig2-v2.jpg)

**Figure 2.:** Coronal (A, H), sagittal (B, I), and axial (C–F, J–M) cross sections of 4 dpf larval (A–G) and 33-dpf juvenile (H–N) wild-type zebrafish acquired using synchrotron X-ray micro-tomography at 0.743 μm3 and 1.43 μm3 isotropic voxel resolution, respectively. 3D volume renderings (G, N) show the cross-sections in relation to the whole organism. In contrast to histology, the cross sections are a single voxel in thickness and can be obtained in any plane (including oblique cuts) after imaging. Complete cross-sections in the orthogonal directions for both fish are provided (Videos 2 and 3). Images are presented to match histological convention of dark cell nuclei (higher attenuation is darker).

![Video 2.](https://cdn.elifesciences.org/articles/44898/elife-44898-video2.mp4.jpg)

**Video 2.:** This video shows full cross-sections of the larval (five dpf) zebrafish from the sagittal orientation (0.743 micron slice thickness) for histology-like phenotyping and qualitative analysis (online viewing available from, https://youtu.be/hyyZu2_75Qc). Intensity histogram of the dataset was inverted and locally adjusted to better discern originally faint or overlapping structures. Best if viewed at highest quality setting.

![Video 3.](https://cdn.elifesciences.org/articles/44898/elife-44898-video3.mp4.jpg)

**Video 3.:** This video shows full cross-sections of the juvenile (33 dpf) zebrafish from the sagittal orientation (1.4 micron slice thickness) for histology-like phenotyping and qualitative analysis (online viewing available from, https://youtu.be/gyxmFJGU1RY). Intensity histogram of the dataset was inverted and locally adjusted to better discern originally faint or overlapping structures. Best viewed at highest quality setting.

Notably, the z-axis resolution of histotomography, presented here at 0.74 or 1.43 microns, is superior to the ~5 micron slice thickness of histology’s conventional paraffin sections. Increased z-axis resolution decreases the likelihood of two separate nuclei being scored as one when they are crowded, as is the case in the retinal and brain neurons of larval zebrafish. The problem of overlapping nuclei in the z-axis makes it difficult to accurately count nuclei from traditional histological images. Our x-y histotomographic resolution is comparable with that of optical microscopy using a 10X objective lens (Figure 3). When direct comparisons between histotomography and histology are desired, maximum intensity projections (MIPs) totaling ~5 microns in thickness can be created from image stacks. Just as in hematoxylin and eosin (H and E) stained sections from ~3.5 mm-long larval (five dpf) (Figure 3A) and ~1 cm-long juvenile (33 dpf) zebrafish (Figure 3C), cell and tissue types can be recognized histologically from five micron MIPS of age-matched fish (Figure 3B and D). As an internal measure of resolution, we calculated the spacing of striations in skeletal muscle fibers encircling the larval swim bladder (Figure 3—figure supplement 1). The average of 293 measures = 2.16 μm (SD = 0.55 μm) is comparable with published values (Burghardt et al., 2016; Dou et al., 2008).

![Figure 3.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig3-v2.jpg)

**Figure 3.:** Top: Comparison of larval (five dpf) zebrafish obtained from a 5 μm thick histology section and micro-tomography data (A and B, respectively). The larval micro-tomograph is 0.743 μm3 in isotropic voxel resolution, and a maximum intensity projection (MIP) of 7 slices, totalling 5.20 μm, resembling the appearance of ~5 μm thick histological sections. Bottom: Comparison of juvenile (33 dpf) zebrafish i5 μm histology section and micro-tomographic MIPs (C and D, respectively). Juvenile scan data is of 1.43 μm3 isotropic voxel resolution, and a MIP of 3 slices, totalling 4.29 μm thickness, is shown. Insets show detail of brain cell nuclei (A–B) and delicate gill structure (C–D). The images demonstrate the near histological resolution of X-ray histotomography. While natural variation in the size of specific features is observed in age matched fish (panel C length = 7.8 mm, panel D length = 10 mm) individual histological features are consistent.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The biological validation of imaging resolution was performed through measurement of distances between Z-lines in the swim bladder striated muscle strands. Cross sections of striated muscle surrounding the swim bladder diagonally in larval (five dpf) zebrafish (A) was used to generate pixel intensity profiles (B). Measurement of pixel distances between local intensity maxima assuming 0.743 μm3 isotropic voxel resolution yielded an average sarcomere length of 2.16 μm (SD = 0.55 μm for 293 distance measurements), consistent with published sarcomere lengths in larval zebrafish (Burghardt et al., 2016; Dou et al., 2008).

### Forms of analysis of zebrafish microanatomy enabled by histotomography

While both traditional histology and histotomography have the resolution needed to distinguish cellular features in 2D slices, only the latter is able to reveal elongated, complex 3D tissue structures such as vessels, nerve tracts, and bones. These advantages are particularly well-illustrated by the study of gill architecture (Figure 3C and D, insets). Histotomography makes it possible to interrogate primary and secondary lamellae from multiple angles without spatial distortion, revealing the delicate leaf-like structure of gill filaments on any pharyngeal arch and even bulges in epithelial cells caused by their nuclei (Video 4). Whole animal histotomographic reconstructions thus provide a level of organismal and anatomical context that is not practical using histology alone.

![Video 4.](https://cdn.elifesciences.org/articles/44898/elife-44898-video4.mp4.jpg)

**Video 4.:** The gill structure is visualized in a whole juvenile (33 dpf) zebrafish in order to demonstrate the ability of soft tissue synchrotron micro-CT to resolve the complex structure of 3D tissues in detail (online viewing available from, https://youtu.be/16sZpZZj9GU). Best viewed at highest quality setting.

The isotropic nature of histotomography enables reslicing in any plane of section without distortion. Dynamic reslicing (cutting the same volume digitally in multiple planes) allows the study of either longitudinal, perpendicular, or other planar virtual sections of the gut at cellular resolution (Figure 4). As far as we are aware, the ability to generate full sets of cross-sections of convoluted structures (such as the gut of juvenile zebrafish) for histological phenotyping within a single modality is unprecedented. This approach can be applied to any convoluted structure requiring thorough evaluation.

![Figure 4.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig4-v2.jpg)

**Figure 4.:** A 3D rendering of a whole juvenile (33 dpf) zebrafish is presented with highlighted gastrointestinal (GI) tract (A). The GI tract exemplifies a convoluted structure for that can be unraveled for histological analysis. The isolated GI tract is displayed (B). Isotropic resolution of data permits virtual slicing at any angle (B1–B3) without a decrease in resolution, allowing comprehensive histology-like visualization despite its tortuous nature. A spline-based reslicing method for visualizing serpentine organs across their entire path is also shown (C). A nonlinear cutting plane (blue) follows the structure of interest, allowing the cut to render a structure’s total length onto a single plane (D).

Virtual sectioning and 3D rendering can be used to study any tissue in the fish, as illustrated for the neuronal cells in the eye, cartilaginous elements of the notochord, the squamous patch of the dorsum of the pharynx, nucleated red blood cells in the heart, and the pneumatic duct and goblet cells of the intestine of whole juvenile (33 dpf) and larval (five dpf) specimens in Figure 5 and Figure 6, respectively. In sum, our digital zebrafish allow tissues and cell nuclei to be visualized across organ systems, including the integumentary, hematopoietic, respiratory, genitourinary, musculoskeletal, gastrointestinal, cardiovascular, nervous and sensory systems (Figure 5—figure supplement 1, Video 5).

![Figure 5.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig5-v2.jpg)

**Figure 5.:** Top: Cutout visualization of a juvenile (33 dpf) zebrafish stained with PTA showing detail in many soft tissue structures. Bottom: Cell types and structures that can be visualized include neuronal cells in the eye (A), cartilaginous rudiments of the squamous patch dorsum (arrow) of the pharynx (B), nucleated red blood cells and heart chambers (C), nephrons of the kidney (D), brain nuclei and motor neurons in spinal nerve cord (E, F). Curved multiplanar slicing, as used for Figure 4D, was used to display the full length of the pneumatic duct (proximal and distal ends noted by an ‘*' and arrow, respectively) (G). Panels A and E represent individual slices (1.43 μm in thickness) while panels B, C, D represent maximum intensity projections of 5 μm thick sections to visualize larger 3D structures. F represents a 7 μm thick projection.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Orthogonal views (middle), a zoomed view (top), and a projection zoom view (bottom, 36 slice, 50 µm projection) of the head of a juvenile (33 dpf) zebrafish are presented. Sagittal, coronal, and transverse sections are denoted by red, yellow, and blue lines, respectively.

![Figure 6.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig6-v2.jpg)

**Figure 6.:** Top: Cutout visualization of both wild-type and huli hutu larval (five dpf) zebrafish stained with PTA showing detail in many soft tissue structures. Bottom: Cell types and structures that can be visualized include neuronal cells in the eye (A), cartilaginous rudiments of the squamous patch on the dorsal (arrow) pharynx (B), nucleated red blood cells (C), intact pneumatic duct (* to arrow) and goblet cells in the gut (D), and cross-striations of bands of muscles encircling the swim bladder (E). Panels A and D represent individual slices (0.743 μm in thickness) while B, C, E represent maximum intensity projections of 5 μm thick sections to visualize larger 3D structures. Compared to age matched wild-type larval zebrafish (top), the number of neuronal cells in the eye are markedly reduced (A’), chondrocytes appear cytologically normal, but formation of cartilaginous structures is markedly reduced (B’), the myocardium is thickened and, as is evident from a survey through all the sections of the heart (a single slice shown here) contains a markedly reduced number of nucleated red blood cells, consistent with anemia and abnormal hematopoiesis (C’). We are able determine the absence of the pneumatic duct and swim bladder in hht due to the ability to scan through the full volume of the sample. D’ shows degenerate tissue and E’ other tissues where those organs normally lie. A’, B’ and D’ represent individual slices (0.743 μm in thickness) while C’ and E’ represent maximum intensity projections of 5 μm thick sections to visualize structures of larger dimension.

![Video 5.](https://cdn.elifesciences.org/articles/44898/elife-44898-video5.mp4.jpg)

**Video 5.:** Tissue structure of a juvenile (33 dpf) zebrafish stained with PTA and imaged with synchrotron micro-CT are visualized through a core-like cut from the center of the digitized sample (online viewing available from, https://youtu.be/FNG-NwXsGHA). Best viewed at highest quality setting.

### Detection of histopathological features in whole-fish histotomography

Successful histopathological analysis requires the detection of subtle differences in the characteristics of specific micron-scale structures. To probe the potential ability of X-ray histotomography to detect subtle histopathological change in a whole organism, we used a mutant, huli hutu (hht), that is known to show a range of subtle to obvious histological changes across all cell types and tissues (Mohideen et al., 2003) (Figure 6, Video 6). Reconstructions of larval hht at 0.743 µm3 voxel resolution allowed us to detect all of hht’s known histological changes, including nuclear fragmentation (karyorrhexis) that is associated with cell death, nuclear atypia (increased size, deviation from typical ovoid shape, and irregular nuclear membrane contour) in the gut, and tissue degeneration. Nuclear fragments are commonly two microns or less in diameter. We were able to reliably establish the absence of an easily missed, micron-scale structure, the pneumatic duct, since every virtual slice of entire fish is available at sub-micron resolution. This structure cannot be reliably assessed by histology on account of its small size and tortuous shape. Age-matched wild-type and hht fish (2, 3, 4 and 5 dpf) can be examined, using our web-based data sharing interface, to visually track progression of the histopathological changes characteristic of hht (Table 1). Additionally, computational detection of nuclei allows global assessment of the density of nuclei across the entire animal (second half of Video 6).

**Table 1.**
 ViewTool database.Scans listed are available for viewing on ViewTool at http://3D.fish and are PTA stained unless otherwise noted. Raw scans are available on request. Note: The wild-type larval five dpf samples, used for quantitative analysis, were imaged on the same day. *Only the cranial section (head) is presented.


<table>
  <thead>
    <tr>
      <th>Zebrafish specimen</th>
      <th>Age (dpf)</th>
      <th>Segments</th>
      <th>12-bit projections (GB)</th>
      <th>32-bit reconstructions (GB)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">Larval (wildtype)</td>
      <td>2</td>
      <td>2</td>
      <td>25.2</td>
      <td>64</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2</td>
      <td>25.2</td>
      <td>64</td>
    </tr>
    <tr>
      <td>4</td>
      <td>3</td>
      <td>37.8</td>
      <td>96</td>
    </tr>
    <tr>
      <td>5</td>
      <td>3</td>
      <td>37.8</td>
      <td>96</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1*</td>
      <td>12.6</td>
      <td>32</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1*</td>
      <td>12.6</td>
      <td>32</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1*</td>
      <td>12.6</td>
      <td>32</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1*</td>
      <td>12.6</td>
      <td>32</td>
    </tr>
    <tr>
      <td rowspan="4">Larval (huli hutu)</td>
      <td>2</td>
      <td>1*</td>
      <td>12.6</td>
      <td>32</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1*</td>
      <td>12.6</td>
      <td>32</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1*</td>
      <td>12.6</td>
      <td>32</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2</td>
      <td>25.2</td>
      <td>64</td>
    </tr>
    <tr>
      <td>Juvenile</td>
      <td>33</td>
      <td>5</td>
      <td>63.0</td>
      <td>160</td>
    </tr>
  </tbody>
</table>

![Video 6.](https://cdn.elifesciences.org/articles/44898/elife-44898-video6.mp4.jpg)

**Video 6.:** This video shows full cross-sections of the huli hutu mutant larval (five dpf) zebrafish from the sagittal orientation (0.743 micron slice thickness) for histology-like phenotyping and qualitative analysis (online viewing available from, https://youtu.be/KbVnamIMPiA). Neuronal cell nuclei probabilities of the mutant are also shown along with a wild-type comparison. The intensity histogram of the dataset was inverted and locally adjusted to enhance the visibility of faint or overlapping structures. Best viewed at highest quality setting.

### Distribution of cell nuclei reveals phenotypic variation between the brains of larval zebrafish

Due to the combination of histotomography’s field-of-view and resolution, we are able to compute features of individual cells and pattern of cells throughout the whole organism. Anatomic pathologists use cytological characteristics in qualitative tissue assessments (Al-Abbadi, 2011; Cheng and Bostwick, 2002). Quantitative assessment of these morphological attributes is best-accomplished in 3D, bringing added precision in distinguishing disease states from the range of normal tissue and cellular architecture. To evaluate the power of computational phenotyping enabled by histotomography, we combined regional segmentation with automated cell detection for characterization of the zebrafish brain (Figure 7).

![Figure 7.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig7-v2.jpg)

**Figure 7.:** Developing larval (five dpf) zebrafish brains were divided into 10 quantifiable anatomically relevant regions by registering sample brains to the Vibe-Z volume-based zebrafish brain atlas and referencing to an immunohistochemistry BrdU based neuroanatomy atlas. Sample landmark selection is shown for equivalent slices between the ViBE-Z atlas data and a five dpf micro-CT for registration-based segmentation (A). Overlay of ViBE-Z atlas embryo (red) over five dpf data (blue) post-registration (B). Semi-automated brain segmentation presented for a five dpf sample in its anatomic context in a representative slice (C). Neuronal cell nuclei detection and validation using a supervised random forest classifier (D). Nuclear detection visualized as a point map for a typical five dpf sample in its anatomic context (E). Semi-automated brain segmentation overlaid onto classifier-based nuclei detection (F). Brain density was calculated by counting every nucleus within a ~ 22 micron (30 voxel) radius surrounding each voxel of the brain (G)..This dimension waschosen because it covers about 5 cell diameters, an estimate of the width of a small brain region.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** 75 × 75×75 µm regions were selected on each fish to validate detection of nuclei: sample regions R1, R2 and R3 are presented (A). 3D visualizations of thresholded original data (B–a) and nuclear probabilities based on the trained classifier (B–b) in Region two are shown. 3D rendering of validation is presented in (B–c); green denotes true positive, blue false positive, orange false negative. Good agreement between manual and automated segmentation is shown on regional 3D rendering and f1 scores (C) across all specimens.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** PTA and osmium staining in (A) micro-CT and (B) transmission electron microscopy images (Hildebrand et al., 2017) both allow the nuclei of individual cells to be distinguished. Automated object detection applied to these images show similar regional patterning and counts of nuclei in corresponding brain slices (C, D).

For example, brain cell nuclei can be distinguished from other stained objects based on shape (elongation) and volume. Elongation is measured as the ratio of the major axis over the minor axis of a 3D object. As anticipated, computational measurements of shape and volume of manually segmented red blood cells (RBCs) and motor neurons (n = 20 each) were different, in agreement with morphological differences that are readily apparent in histology (Figure 8A). In addition, RBCs and motor neurons are more elongated than typical brain nuclei, which are more spherical. Specifically, RBCs are typically flat and oval, while motor neurons are more ‘tear drop’ shaped. Other cell differences include the volume, with motor neurons being larger than typical brain nuclei. The PTA staining patterns of the cytoplasm of RBCs and motor neurons are different in appearance from those of other cells. From the measurements shown, it is apparent that our current resolution is sufficient to readily distinguish cell types.

![Figure 8.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig8-v2.jpg)

**Figure 8.:** Shape and volume of manually detected brain cell nuclei varies between red blood cells (RBCs) and motor neurons (n = 20 cells each) (A, B). The mean elongation was 1.9, 1.3, and 1.1 for RBCs, motor neurons, and brain nuclei, respectively. The mean volume was 99, 102, and 13 µm3 for RBCs, motor neurons, and brain nuclei, respectively. These releative values are consistent with what is visually apparent in both histology (C1 and C3) and histotomography (C2 and C4). Volumes of motor neuron and erythrocytes include both nuclei and cytoplasm. Differences in the distribution of brain nuclei were also observed. Cell nuclei were also identified across whole zebrafish samples via a manually trained classifier and segregated by registering brain regions for five five dpf samples (D). The regions identified through anatomical landmarks include olfactory epithelium, telencephalon, diencephalon, mesencephalon, metencephalon, myelencephalon, hypothalamus, spinal cord, and white matter. The proportion of cells per brain region as percentage of total cell counts, agree in rank order between samples (E). Computed elongation and volumes showed no significant difference between individual fish (F, G).

We have assigned brain nuclei to major brain regions including the olfactory epithelia, telencephalon, diencephalon, hypothalamus, mesencephalon, metencephalon, myelencephalon, white matter, and spinal cord by cross-atlas registration (Raj et al., 2018; Ronneberger et al., 2012; Wullimann and Mueller, 2005). In addition, cell nuclei were automatically detected from head scans of intact fish using a supervised learning approach with a random forest classifier. Three 75 µm3 regions of neural cell nuclei were manually annotated and compared against classifier results for location and counts. The F1 score, optimized for probability threshold to balance precision and recall, showed ~90% correspondence between manual and automated detections (Figure 7—figure supplement 1). The distribution of cell nuclei in our samples corresponded well with those seen in 54 nm thick transmission electron microscopy sections (Hildebrand et al., 2017) (Figure 7—figure supplement 2).

Whole-animal histotomography enables quantitative analyses of both individual cells and groups of cells. The average number of nuclei in the brain region out of 5 larvae studied was 75,413 (SD = 8,547) (Table 2). This number corresponds well to the ~80,000 reported brain cell ROIs in similarly-aged zebrafish imaged with light sheet microscopy (Chen et al., 2018). In contrast to the general agreement of size and elongation distributions of brain cell nuclei between individual fish (Figure 8), nuclear density varied between brain regions, as reflected by cell density distributions and 3D patterning (Figure 9). Notably, heat-maps of cell densities revealed obvious differences between five wild-type siblings. Comparatively, fish 1 and 2 exhibit a shift towards lower cell density as compared with fish 3, 4, and 5, which correlates with the larger brain volumes of fish 1 and 2 (Tables 2–3). These differences in cell density may be explained by differences in exact developmental stage.

![Figure 9.](https://cdn.elifesciences.org/articles/44898/elife-44898-fig9-v2.jpg)

**Figure 9.:** Cellular density varies between individual brain regions and carries distinct signals consistent between individual samples (A). 3D renderings of whole-brain densities with identical transparency settings are presented for each fish (B) and reflects signal differences presented in (A).

**Table 2.**
 Cell nuclei counts in different five dpf zebrafish brain regions.Major divisions of the zebrafish brain and the number of cell nuclei in each division (counts) are shown across five fish. Mean total cell nuclei count is 75,413 and relative standard deviation ±11.3%.


<table>
  <thead>
    <tr>
      <th>Major brain divisions</th>
      <th colspan="5">Brain region cell nuclei (Counts)</th>
    </tr>
    <tr>
      <th>Specimen number</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Olfactory Epithelium</td>
      <td>855</td>
      <td>398</td>
      <td>1103</td>
      <td>1158</td>
      <td>1257</td>
    </tr>
    <tr>
      <td>Telencephalon</td>
      <td>3696</td>
      <td>4735</td>
      <td>4576</td>
      <td>3704</td>
      <td>4570</td>
    </tr>
    <tr>
      <td>Diencephalon</td>
      <td>6323</td>
      <td>6076</td>
      <td>7390</td>
      <td>7718</td>
      <td>8134</td>
    </tr>
    <tr>
      <td>Hypothalamus</td>
      <td>2096</td>
      <td>2342</td>
      <td>3392</td>
      <td>3047</td>
      <td>2680</td>
    </tr>
    <tr>
      <td>Mesencephalon</td>
      <td>17,377</td>
      <td>15,993</td>
      <td>21,161</td>
      <td>21,448</td>
      <td>22,275</td>
    </tr>
    <tr>
      <td>Metencephalon</td>
      <td>876</td>
      <td>1025</td>
      <td>1012</td>
      <td>2865</td>
      <td>1713</td>
    </tr>
    <tr>
      <td>Myelencephalon</td>
      <td>27,899</td>
      <td>28,691</td>
      <td>30,991</td>
      <td>37,769</td>
      <td>34,766</td>
    </tr>
    <tr>
      <td>White Matter</td>
      <td>5633</td>
      <td>5955</td>
      <td>5810</td>
      <td>4524</td>
      <td>5181</td>
    </tr>
    <tr>
      <td>Spinal Cord</td>
      <td>1408</td>
      <td>1570</td>
      <td>1850</td>
      <td>1712</td>
      <td>2312</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>66,163</td>
      <td>66,785</td>
      <td>77,285</td>
      <td>83,945</td>
      <td>82,888</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Brain Volumes by Region for five dpf Zebrafish Brain.Major divisions of the zebrafish brain and their volumes (μm3) are shown across five zebrafish. Mean total volume is 15,507,461 and relative standard deviation ± 11.9%.


<table>
  <thead>
    <tr>
      <th>Major brain divisions</th>
      <th colspan="5">Brain region volumes (µm3)</th>
    </tr>
    <tr>
      <th>Specimen number</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Olfactory Epithelium</td>
      <td>293,251</td>
      <td>171,459</td>
      <td>164,338</td>
      <td>131,459</td>
      <td>111,195</td>
    </tr>
    <tr>
      <td>Telencephalon</td>
      <td>1,117,500</td>
      <td>1,021,518</td>
      <td>956,493</td>
      <td>826,273</td>
      <td>672,572</td>
    </tr>
    <tr>
      <td>Diencephalon</td>
      <td>1,440,447</td>
      <td>1,300,518</td>
      <td>1,097,698</td>
      <td>1,134,753</td>
      <td>1,046,486</td>
    </tr>
    <tr>
      <td>Hypothalamus</td>
      <td>813,210</td>
      <td>702,116</td>
      <td>732,073</td>
      <td>608,018</td>
      <td>575,387</td>
    </tr>
    <tr>
      <td>Mesencephalon</td>
      <td>4,353,108</td>
      <td>3,442,415</td>
      <td>3,663,909</td>
      <td>3,183,413</td>
      <td>2,885,684</td>
    </tr>
    <tr>
      <td>Metencephalon</td>
      <td>324,562</td>
      <td>273,699</td>
      <td>388,409</td>
      <td>529,656</td>
      <td>296,336</td>
    </tr>
    <tr>
      <td>Myelencephalon</td>
      <td>4,982,069</td>
      <td>4,636,451</td>
      <td>3,977,877</td>
      <td>4,550,207</td>
      <td>3,850,373</td>
    </tr>
    <tr>
      <td>White Matter</td>
      <td>4,783,477</td>
      <td>4,358,188</td>
      <td>4,119,302</td>
      <td>3,963,126</td>
      <td>3,529,787</td>
    </tr>
    <tr>
      <td>Spinal Cord</td>
      <td>78,092</td>
      <td>97,609</td>
      <td>117,260</td>
      <td>109,808</td>
      <td>125,722</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>18,185,716</td>
      <td>16,003,973</td>
      <td>15,217,359</td>
      <td>15,036,713</td>
      <td>13,093,542</td>
    </tr>
  </tbody>
</table>

## Discussion

Large-scale studies of the effects of genes and environment on phenotype (phenome projects) are ideally comprehensive and quantitative in nature, covering all cell and tissue types across length scales. We pursued synchrotron micro-CT to enable the vision of computationally phenotyping small organisms in 3D, at a throughput and resolution that is compatible with phenome projects (Cheng et al., 2011). Other groups have utilized X-ray micro-CT for quantitative morphometric analyses of juvenile and adult teleost fish (Babaei et al., 2016; Seo et al., 2015; Weinhardt et al., 2018). Histological analysis across cell types would add significant powerful to phenotypic screens, but would require higher resolution and contrast-to-noise ratios than available at the time. This need motivated us to systematically optimize details of sample preparation, sample mounting, imaging acquisition settings, X-ray optics, image processing, and visualization parameters to make highly informative histological signatures apparent.

Histotomography offers resolving power over more than four orders of magnitude, providing both anatomical and cellular detail from single images that encompass, for zebrafish, the whole organism. High-throughput adaptations would be necessary for whole-organism chemical and genetic phenome projects. Genetic phenomics may involve, for example, the study of mutants for each zebrafish protein-encoding gene (>26,000) and non-coding functional element. By our estimates, screening 10,000 zebrafish mutants in replicate would require ~20 years with a monochromatic synchrotron source and, if fully optimized, <1 year using pink-beam X-rays. High-throughput primary screens by pink-beam could be followed by higher-contrast monochromatic imaging of samples that show evidence of phenotypic change. The fact that some 70% of human protein-coding genes have at least one zebrafish orthologue makes this throughput potential relevant to disease modeling and the probing of human gene function (Howe et al., 2013). The unprecedented depth of zebrafish tissue phenotyping enabled by histotomography has the potential to enrich conclusions from mouse phenome projects (Dickinson et al., 2016; Hsu et al., 2016). Plastic embedding of specimens, while not essential for synchrotron micro-CT, adds sample stability (Lin et al., 2018) f image re-acquisition with improved micro-CT implementations.

Optical imaging modalities such as light sheet fluorescence microscopy are ideal for in vivo studies (McDole et al., 2018), and resolve 3D sub-micron features. Fluorescence-based imaging, however, depends on sample transparency, and for optically more opaque samples, dissection and/or physical slicing to maintain resolution without diffraction or loss of signal (Chung et al., 2013; Hama et al., 2011; Susaki et al., 2014; Watson et al., 2017). Image quality is compromised in the presence of significant melanin pigmentation, even in transparent samples with diameters of more than about a millimeter. The molecular specificity of fluorescence-based phenotyping is poorly suited for large-scale screens that require phenotyping across all cell types.

Three-dimensional tissue imaging methods based on ultrathin serial tissue sections or block-face imaging have ultrastructural cellular resolution, but becomes intractable for large scale studies of specimens larger than ~1 cubic millimeter in minimum dimension. Serial block-face scanning electron microscopy has been used to image and reconstruct a mouse neocortex (Kasthuri et al., 2015) and the larval zebrafish brain at nanometer-scale (56.4 × 56.4 × 60 nm3 resolution from 16,000 sections) (Hildebrand et al., 2017). These studies made it possible to define precise neurological and circulatory relationships across the entire brain. However, 3D reconstructions based on serial sectioning are time-consuming enough to be infeasible for interrogating all tissues in the numbers of specimens required for toxicology or genetic screens. For example, a multi-beam scanning electron microscope, imaging a single cubic mm of tissue at 20 nm3 resolution can require ~3 months of continuous imaging (Dyer et al., 2017).

Ideal comprehensive anatomical phenotyping would include quantitative characterization of tissue architecture and cellular features in addition to measures of larger features such as organ size, vascular structure, nerve structure, and body shape. Striking individual phenotypic variation was revealed here by the computational measurement of cell density across larval zebrafish brains. This finding illustrates how histotomography’s unique combination of field-of-view and resolution can be useful for distinguishing individual from experimentally-determined phenotypic variation.

Imaging and analysis of multiple specimens at multiple ages is necessary to establish a knowledge of normal statistical variation in gross and microscopic anatomy across organ systems that is needed for automated detection of ‘abnormal’ phenotypes. Comprehensive computational phenotyping will thus require the development of detailed 3D atlases. Whole specimen histotomography datasets are well-suited for automated organ and cellular level detection that can be used as a scaffold for morphological lifespan atlases, capturing the extent of normal phenotypic variation at cellular, tissue, and organismal scales. The pan-cellular nature of histotomography makes it ideal for cross-referencing with images from focused (e.g. fluorescence-based) modalities involving transgenic or whole-mount stained organisms; this would involve fixation, staining and histotomographic imaging of the fluorescently studied specimens. Conversely, the addition of tissue-, cell-, and/or protein-specific micro-CT stains would enable targeted analyses and cross-atlas comparisons of explicit constituents within the full context of a scanned sample or organism (Metscher and Müller, 2011). Further optimization will be needed to resolve a key characteristic of proliferating cells: mitotic chromosomes. Condensed chromosomes are about one micron in diameter, requiring true 0.5 micron pixel/voxel resolution for detection. Increasing field-of-view beyond ~2.7 mm (used for histotomography of juveniles at 1.4 micron isotropic voxel resolution) will be needed to image of the full width of mature zebrafish, and will be facilitated by larger imaging chip arrays.

The work shown here approaches the ideal of comprehensive and quantitative phenotyping for tissue samples and model organisms that lie in the mm-to-cm length scale, such as the zebrafish. Indeed, X-ray histotomography allows for full volume imaging of replicate samples at cellular resolution, distinguishing neighboring cells and resolving nuclear morphologies in optically opaque larval and juvenile zebrafish specimens. Extending this work to Drosophila, C. elegans, and Arabidopsis, and to tissue samples from larger organisms such as mouse and human would enable cross-species phenotypic analyses, leading to a more universal understanding of tissue architecture and morphological phenotype.

To make our data accessible to users with standard computational resources, we have developed an open-access, web-based data sharing platform, ViewTool, that allows 2D and 3D visualizations of full sample volumes. Histotomographic data are also ideal for real-time visualization using virtual reality technologies such as syGlass (Pidhorskyi et al., 2018). Beyond data exploration, the rate of development of methods and tools for computational analysis can be enhanced by long-term accessibility of histotomographic data through an internationally available portal analogous to those used for DNA or transcriptome-based resources. Repositories of high-resolution images from a full complement of human and other organismal tissues would facilitate cross-correlations between model system and human phenotypes (Regev et al., 2017; Rozenblatt-Rosen et al., 2017). Such a resource would have the potential to increase analytical precision, sensitivity, reproducibility, and data sharing as we address important questions across basic and clinical sciences.

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
      <td>Strain (Danio rerio)</td>
      <td>Wild-type Ekkwill</td>
      <td>ZFIN ID: ZDB-GENO -990520–2</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Danio rerio)</td>
      <td>huli hutu</td>
      <td>Mohideen et al., 2003</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>10% neutral buffered formalin</td>
      <td>Fisher Scientific</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EMBed-812</td>
      <td>Electron Microscopy Sciences</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ethyl alcohol</td>
      <td>Pharmco-Aaper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Finquel (MS-222, tricaine-S)</td>
      <td>Argent Chemical Laboratories</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>glycol methacrylate</td>
      <td>Polysciences</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Kapton tubing</td>
      <td>Small Parts</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>phosphate-buffered saline</td>
      <td>Sigma-Aldrich</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>phosphotungstic acid</td>
      <td>VWR</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ovadine</td>
      <td>Syndel</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Avizo</td>
      <td>Thermo Fisher Scientific</td>
      <td>SCR_014431</td>
      <td>version 9.4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Elastix</td>
      <td>http://elastix.isi.uu.nl/</td>
      <td>SCR_009619</td>
      <td>version 4.8</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji/ImageJ2</td>
      <td>https://fiji.sc/</td>
      <td>SCR_002285</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Ilastik</td>
      <td>Sommer et al., 2011 (http://ilastik.org/)</td>
      <td>SCR_015246</td>
      <td>version 1.3</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ITK-SNAP</td>
      <td>Yushkevich et al., 2006 (http://www.itksnap.org)</td>
      <td>SCR_002010</td>
      <td>version 3.4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OpenSeaDragon</td>
      <td>https://openseadragon.github.io/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>TomoPy</td>
      <td>Argonne National Labs (http://tomopy.readthedocs.io)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>VGStudio Max 2.1</td>
      <td>Volume Graphics</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Zebrafish husbandry and sample preparation

Wild-type zebrafish (Ekkwill strain) and the huli hutu mutant (Mohideen et al., 2003) were reared at an average temperature of 28°C in a recirculating system with a 14:10 hr light:dark cycle (Copper et al., 2018). Fish were fed three times a day a diet consisting of brine shrimp and flake food. All fish were staged according to the zebrafish developmental staging series of Kimmel et al. (1995).

After staging, larval (2, 3, 4, and 5 dpf) and juvenile (33 dpf) zebrafish specimens were euthanized in pre-chilled 2x Finquel (MS-222 or tricaine-S, 400 mg/L) solution (Argent Chemical Laboratories, Redmond, WA) buffered in 1% phosphate-buffered saline (PBS), and fixed in chilled 10% neutral buffered formalin (NBF) (Fisher Scientific, Allentown, PA) overnight in flat-bottom containers at room temperature. To improve fixation and reduce the volume of gut contents, we starved juvenile fish for at least 24 hr for a 10 mm specimen. Fixed zebrafish specimens were rinsed 3 times in 1X PBS for 10 min followed by being submerged in 35% ethyl alcohol (EtOH) for 20 min at room temperature with gentle agitation. The samples were then submerged in 50% EtOH for 20 min at room temperature with gentle agitation. Specimens were stained with 0.3% phosphotungstic acid (PTA) (diluted from a 1% w/v stock solution at a ratio of 3:7 in 100% EtOH) for 24 hr at room temperature with gentle agitation. This metallic stain is used widely in histology and electron microscopy for staining collagen and other connective tissue (Bloom and Aghajanian, 1968; Bulmer, 1962). The complete infiltration and embedding protocol is described elsewhere (Lin et al., 2018). Briefly, after staining, each specimen was infiltrated by sequential submerging in increasing concentrations of EtOH (70%, 90%, 95%, and 100%) for 30 min intervals at room temperature with gentle agitation. The samples were then embedded in glycol methacrylate (Polysciences, Inc, Warrington, PA) or EMBed-812 (Electron Microscopy Sciences, Hatfield, PA) in Kapton tubing (Small Parts, Inc, Logansport, IN). The tubing provides structural support with high thermal stability. Total sample preparation time takes 5 days. All procedures on live animals were approved by the Institutional Animal Care and Use Committee (IACUC) at the Pennsylvania State University.

Generation of the ENU-mutagenized mutant hht was previously described (Mohideen et al., 2003). The hht line was maintained as heterozygotes due to the recessive larval-lethal nature of the mutation. Mating was carried out by placing male and female heterozygotes in Aquatic Habitat breeding tanks with dividers the afternoon prior to egg collection. Collected eggs were disinfected in 10% Ovadine (Syndel) for 1 min at room temperature followed by three washes with charcoal-filtered water. Larvae were incubated at 28.5°C to maintain consistent speed of development. Homozygous mutant larvae were identified by a combination of gross phenotypes, including small eyes, small head, dorsally curved body, and enlarged yolk, that are easily detected under a low-power stereomicroscope at ≥3 dpf. Gross mutant phenotype at two dpf is limited to small eyes and requires screening at 40X.

### Image acquisition

Synchrotron micro-CT studies were performed on the beamline 2-BM-B Advanced Photon Source at Argonne National Laboratory. The beamline’s quasi-parallel X-rays were used to acquire projection images of larval and juvenile zebrafish in sets of 2048 digital slices. After passing through the object, the X-rays impinge on a thin scintillator, which converts X-rays to optical photons that are magnified by a microscope objective lens onto a cooled CCD. The volumetric field of view was 1.5 mm3 for 0.743 µm3 voxels using a 10X objective lens, and 3 mm3 with 1.43 µm3 voxels using a 5X objective. A vertical stage was used to translate the sample between multiple acquisitions.

### Monochromatic imaging

For monochromatic imaging, a multilayer monochromator with bandwidth ΔE/E ~ 1.5%, or 200–250 eV, was used to obtain discrete X-ray energies. 1501 projections were obtained over 180 degrees (1 projection every 0.12 degrees) with a 2048-by-2048 pixel CoolSnap HQ CCD camera (Photometrics, AZ, USA). Larval and juvenile zebrafish scans were obtained at 13.8 keV and 16.2 keV, respectively. Additionally, two flat-field (gain) images (one at the beginning and one at the end of the acquisition) and one dark-field image are also acquired. Flat-field and dark-field corrections, ring artifact reduction, and image reconstruction were done using the open source TomoPy toolkit. Reconstructing the projection data generates a 3D data set comprised of a 2048-by-2048-by-2048 voxel cube. A voxel in the PTA-stained larval zebrafish has nominal 0.743 µm x 0.743 µm x 0.743 µm resolution, while a voxel in the juvenile zebrafish has a nominal 1.43 µm x 1.43 µm x 1.43 µm resolution, corresponding with larval and juvenile zebrafish fields-of-view of 1.5 mm x 1.5 mm x 1.5 mm and 3 mm x 3 mm x 3 mm, respectively. Whole-organism zebrafish reconstructions were created by combining series of segmental reconstructions at each vertical position along the full length of each specimen. Exposures of 400 ms per projection yielded acquisitions of ~20 min. Whole zebrafish scans take 3–5 acquisitions, depending on asample size.

### Polychromatic imaging

A polychromatic ‘pink-beam’ covering 10–30 keV, was used to obtain 1600 projections over 192 degrees (1 per 0.12 degrees) with a 2048-by-2048 pixel CoolSnap HQ CCD camera. Whole-organism imaging polychromatic reconstructions were generated from segmental reconstructions over its full length, taking ~20 s per segment. Stripes present in the raw pink-beam projection data were removed using a Fourier-Wavelet based method with a Haar filter and sigma of 3 pixels (Münch et al., 2009). Rings and bands were corrected in the polar transform domain of the reconstructed images. Free parameters in this method were optimized by using minimum entropy approaches.

### Estimates of the suitability of synchrotron micro-CT for phenome projects

The acquisition times using monochromatic or polychromatic ‘pink-beam’ sources are about 20 min or 20 s per scanned segment, respectively. Assuming: (i) a 5 min set up time per specimen, (ii) 10 replicates per condition, (iii) three scans per fish, (iv) a synchrotron availability of 100 scanning days per year and 10 hr of scanning time per scanning day, and (v) ability to multiplex five larval specimens at a time without increasing acquisition time, screening 20,000 larval mutants would require ~40 years with monochromatic source or ~1 year using pink-beam. There is potential for higher throughput via robotic sample swapping for monochromatic and polychromatic sources and/or increased multiplexing with pink-beam. Estimates of throughput would also be affected by the proportion of specimens that are juvenile or adult, since those are likely to be imaged individually, and require either multiple segmental scans per fish or spiral CT as used for humans.

### Energy optimization

In X-ray based imaging modalities, including micro-CT, the choice of imaging energy determines both the contrast between different tissue types and the noise level in the image. The contrast is based on the difference in energy-dependent absorption coefficient between the materials of interest, and the noise is determined by the transmitted flux of X-rays. In medical imaging, the contrast is often maximized at lower energies, for which differential absorption is maximized, while relative noise is reduced at higher energies, for which transmitted flux is maximized. A contrast-to-noise ratio (CNR) is generally maximized at some intermediate energy that depends on the concentration and amounts of various tissues present. Metal-stained tissue tomography is associated with the potential addition of X-ray absorption edges introducing additional structure into the energy-dependence of attenuation coefficients.

To investigate these tradeoffs, we made use of a simple but powerful model from Spanne (1989) that assumes the presence of a small circular contrasting detail at the center of a circular absorbing background. The background linear attenuation coefficient for energy E, $\mu_{1}E=\mu_{bg}E.$The attenuation coefficient for the contrasting material $\mu_{2}E=\mu_{bg}E+\mu_{c}E$. Note that each attenuation coefficient is given by the product of the material density in g/cm3 and of a tabulated mass-attenuation coefficient in cm2/g, that is $\mu_{c}E=ρ_{c}\frac{\mu}{ρ}_{c}(E)$.

The contrast detail is assumed to be large enough that blurring during reconstruction does not bias the reconstructed attenuation coefficient from its true value. The reconstructed noise variances at the center of the image in the presence and absence of the contrast detail are denoted $var\mu_{1}E$ and $var\mu_{2}E$, respectively. Because of circular symmetry, the variance at the center of a reconstructed image can be calculated in closed form (Kak and Slaney, 1988) and shown to be inversely proportional to the transmitted intensity.

$$
var{\mu_{i}(E)}∝\frac{1}{I¯_{i}(E)} ,
$$

where $I-_{1}E=I_{0}Eexp-\mu_{bg}Et_{bg}$ and $I-_{2}E=I_{0}Eexp-\mu_{bg}Ed_{bg}+\mu_{c}Ed_{c}$ are the transmitted intensities in the absence and presence of the contrast detail, respectively. Here $I_{0}E$ is the incident intensity at energy $E$ and $d_{c}$ and $d_{bg}$ are the diameters of the contrast detail and background circle, respectively. With this model, we can then readily calculate a CNR defined as

$$
CNRE=\frac{\mu_{1}E-\mu_{2}(E)}{\sqrt{var\mu_{1}E+var\mu_{2}E}}.
$$

We used this model to calculate CNR ratios for the PTA stain as a function of background material thickness and tungsten contrast detail concentration. These are shown in Figure 1—figure supplement 1 and both sets of plots show a clear optimal energy range just above the tungsten L1 edge at 12 keV with strong fall off below the L3 edge at 10.2 and again above about 16 keV. We thus chose to acquire all PTA stained larval data at the pre-calibrated 13.8 keV monochromator setting. For larger juvenile fish of diameter >3 mm, the CNR peak is broader, justifying the use of higher, more penetrating X-ray energies. Therefore, we chose the 16.2 keV monochromator setting for juvenile specimens.

### Phase contrast optimization

The coherence of synchrotron radiation allows for imaging that is sensitive to phase shifts in the incident X-ray wave front caused by variations in the real part of the complex index of refraction. A variety of approaches have been explored for performing quantitative phase-contrast tomography involving the use of grating analyzers or multiple measurements with different sample-scintillator distances (Paganin, 2006). The latter techniques rely on the fact that interference fringes develop in the transmitted intensity pattern as it propagates beyond the sample. Here, we were seeking a degree of edge perception resembling that seen in histology rather than quantitative phase-contrast. Juvenile (33 dpf) reconstructions at sample-to-scintillator distances (SSDs) of 10, 40, and 80 mm are reported in La Rivière et al. (2010). Herein, we generated larval (five dpf) reconstructions at SSDs of 20, 30, 40 and 50 mm. We focused on the zebrafish eye to take advantage of the periodicity of retinal photoreceptors (Figure 1—figure supplement 2). The SSD of 20 mm caused edges of nuclei to appear blurry. SSDs of 30 or 40 mm yielded a degree of edge perception resembling that achieved in glass slide histology. Subjectively SSDs of 50 mm and larger (data not shown) caused edge effects to begin to look ‘artificial’ compared with traditional histology and transmission electron microscopy. Exaggerated phase effects can diminish perceived resolution. Notably, an ‘ideal’ SSD depends upon the specific structures being defined. Line profiles through the periodic retinal cells show that higher SSDs give rise to line profiles with a higher modulation depth, with the greatest benefit achieved around 30 and 40 mm SSD and strong evidence of overshooting and bias above 50 mm SSD. Based on these considerations, we used an SDD of 30 mm for all subsequent acquisitions.

### Image reconstruction, Image Processing and Visualization

CT reconstruction was done using TomoPy, an open-source package from Argonne National Labs (http://tomopy.readthedocs.io). Some of the image processing was conducted in Fiji/ImageJ2 (https://fiji.sc/). Software used for volumetric visualizations in this manuscript include Avizo version 9.4 (Thermo Fisher Scientific, Waltham, MA) and VGStudio Max 2.1 (Volume Graphics, Heidelberg, Germany). Videos 1 and 4 were generated in Avizo. Videos 2, 3, 5 and 6 were generated in VGStudio Max 2.1 using an intensity histogram adjusted to better discern otherwise faint or overlapping structures.

### ViewTool

The file sizes associated with synchrotron micro-CT are on the order of ~100 GB per larval or juvenile zebrafish, making scans difficult to view for people with standard computational resources. To allow users to inspect the data without having to download the full resolution volumes, we developed ViewTool, an open-access and web-based multiplanar viewer (http://3D.fish) (Figure 5—figure supplement 1). ViewTool is partly based on the open-access project OpenSeaDragon (https://openseadragon.github.io/), and combines radiology and digital pathology workflows into a seamless experience to provide user-friendly access to our 3D data. Orthogonal image z-stacks are downsampled using JPG compression before being served to end users through Amazon Web Services’ Simple Storage Service (AWS 3). For bandwidth considerations, only every fourth slice is currently shown in the viewer by default. These images are presented in three windows in a user’s browser that are spatially linked to the user’s mouse or multi-touch interface. The two planes orthogonal to the interrogated plane sync to the corresponding x,y mouse location. ViewTool’s code was written in client-side JavaScript, HTML and CSS, requires no download, and has no server requirement to run the basic implementation.

### Landmark-based Cross-Atlas registration

Semi-automated segmentation was performed using Elastix version 4.8, an open-source registration software (Klein 2010, http://elastix.isi.uu.nl/). All registrations were performed in two parts: an affine registration for optimizing initialization positions of both images followed by a landmark based thin-plate spline registration. Landmarks were manually marked on corresponding anatomical regions. The detected brain regions were derived from segmented volumes of the larval (4 dpf) reference fish from the ViBE-Z zebrafish brain atlas (Ronneberger et al., 2012), which was used for the primary registration onto one of our 5 dpf samples. Validation of region detection was performed by cross-referencing to a histology-based developmental brain atlas (Wullimann and Mueller, 2005) and manual segmentation was used to correct areas of inaccurate registration. This process generated a foundation for the detection of brain regions in our remaining larval (5 dpf) specimens (n = 5 total samples). All other registrations used this segmented 5 dpf sample as the moving image for better detection accuracy with less extensive manual segmentation. Manual segmentations were performed using the open-source software, ITK-SNAP version 3.4 (Yushkevich et al., 2006) (http://www.itksnap.org). The ViBE-Z database and atlas are publicly available (http://vibez.informatik.uni-freiburg.de/) (Ronneberger et al., 2012).

### Cell detection and counting

Using a supervised learning approach, we distinguished brain cell nuclei from background by training examples using Ilastik version 1.3 (Sommer et al., 2011), a simple, user-friendly, open-source tool for interactive image classification, segmentation and analysis (http://ilastik.org/). Specifically, three 75 µm3 regions were selected for training across the larval (5 dpf) zebrafish brain and notochord regions. Nuclei were manually segmented in 2D in each of three orthogonal views (sagittal, coronal, and axial). Features that were used in the classification including intensity (pixel value with various smoothing), edges (gradient, Laplacian of Gaussian, and difference of Gaussians) and texture (structured tensor of eigenvalues, Hessian of Gaussian eigenvalues). The random forest classifier assigned a probability of being a nucleus to any given pixel. We combined probabilities assigned from each orthogonal plane to obtain the probabilities in a given volume, $P_{total}(x,y,z)=P_{coronal}(x,y,z)\timesP_{saggital}x,y,z\timesP_{transverse}(x,y,z)$. Original data were thresholded to show approximate locations of nuclei and their probabilities. The results of nuclear labeling based on the nuclear training set demonstrate that, as expected, brain cell nuclei have high probabilities, while blood vessels and background have low probabilities. From these measures, a probability threshold and size filter (80% or higher probability containing at least 8 voxels,~3.5 µm3) were used to detect individual cell nuclei. Cell nuclei in the same training regions were manually segmented in order to assess the accuracy of the automated segmentation results and to justify the probability threshold and size filter settings. Automatically detected cell nuclei were checked against those manually detected and categorized as true-positive (manual and automatic detected), false negative (manually detected but automatically undetected), or false positive (manually undetected but automatically detected). F1 score was optimized over different settings to balance precision and recall between manual and automated segmentation.

### Resource sharing

ViewTool is publically available (http://3D.fish). Digital histology is publicly available from our Zebrafish Lifespan Atlas (http://bio-atlas.psu.edu) (Cheng, 2004). Registered and unregistered 8-bit reconstructions of the heads of five zebrafish larvae involved in analysis are available on the Dryad Digital Repository (https://doi.org/10.5061/dryad.4nb12g2), along with scripts written for cell nuclei detection, analysis, and sample registration. Other code used for analysis can be also be downloaded from the Dryad repository. Full resolution scans, including raw projection data, are available from researchers upon request as a download or by transfer to physical media.
