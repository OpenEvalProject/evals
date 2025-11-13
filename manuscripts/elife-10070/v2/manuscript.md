# Untwisting the Caenorhabditis elegans embryo

## Authors

- Ryan Patrick Christensen<sup>1</sup> †
- Alexandra Bokinsky<sup>2</sup>
- Anthony Santella<sup>3</sup>
- Yicong Wu<sup>1</sup>
- Javier Marquina-Solis<sup>4</sup>
- Min Guo<sup>1</sup>
- Ismar Kovacevic<sup>3</sup>
- Abhishek Kumar<sup>1</sup>
- Peter W Winter<sup>1</sup>
- Nicole Tashakkori<sup>1</sup>
- Evan McCreedy<sup>2</sup>
- Huafeng Liu<sup>5</sup>
- Matthew McAuliffe<sup>2</sup>
- William Mohler<sup>6</sup>
- Daniel A Colón-Ramos<sup>4</sup>
- Zhirong Bao<sup>3</sup>
- Hari Shroff<sup>1</sup>

### Affiliations

1. Section on High Resolution Optical Imaging, National Institute of Biomedical Imaging and Bioengineering National Institutes of Health Bethesda United States
2. Biomedical Imaging Research Services Section, Center for Information Technology National Institutes of Health Bethesda United States
3. Developmental Biology Program Sloan-Kettering Institute New York United States
4. Program in Cellular Neuroscience, Neurodegeneration and Repair, Department of Cell Biology Yale University School of Medicine New Haven United States
5. State Key Laboratory of Modern Optical Instrumentation, College of Optical Science and Engineering Zhejiang University Hangzhou China
6. Department of Genetics and Developmental Biology University of Connecticut Health Center Farmington United States

† Corresponding author

## Abstract

The nematode Caenorhabditis elegans possesses a simple embryonic nervous system with few enough neurons that the growth of each cell could be followed to provide a systems-level view of development. However, studies of single cell development have largely been conducted in fixed or pre-twitching live embryos, because of technical difficulties associated with embryo movement in late embryogenesis. We present open-source untwisting and annotation software (http://mipav.cit.nih.gov/plugin_jws/mipav_worm_plugin.php) that allows the investigation of neurodevelopmental events in late embryogenesis and apply it to track the 3D positions of seam cell nuclei, neurons, and neurites in multiple elongating embryos. We also provide a tutorial describing how to use the software (Supplementary file 1) and a detailed description of the untwisting algorithm (Appendix). The detailed positional information we obtained enabled us to develop a composite model showing movement of these cells and neurites in an 'average' worm embryo. The untwisting and cell tracking capabilities of our method provide a foundation on which to catalog C. elegans neurodevelopment, allowing interrogation of developmental events in previously inaccessible periods of embryogenesis.

## Introduction

Understanding how complex neural circuits and entire nervous systems form is one of the fundamental goals of neuroscience. While substantial progress has been made in identifying guidance factors in neurodevelopment (Kolodkin and Tessier-Lavigne, 2011; Dudanova and Klein, 2013; Chilton, 2006; O'Donnell et al., 2009), how known factors interact to direct the formation of complex neural circuits remains mysterious (Dudanova and Klein, 2013). Examining the entirety of neurodevelopment in intact, living samples would be useful in understanding larger scale principles that orchestrate nervous system formation. Unfortunately, technological limitations and inherent nervous system complexity have hindered our ability to capture a 'systems-level' view of the developing brain.

One model organism well-suited to systems-level neuroscience research is Caenorhabditis elegans, which possesses a simple nervous system comprising 302 neurons (White et al., 1986), 222 of which form during embryogenesis (Sulston et al., 1983). The adult connectome has been reconstructed, and the morphology of all adult neurons has been mapped at electron-microscopy resolution (White et al., 1986); the genome sequenced (C. elegans Sequence Consortium, 1998); and the organism is genetically tractable and transparent at all life stages, enabling investigation with light microscopy. The simplicity of the C. elegans nervous system, its experimental accessibility, and the extensive knowledge base make it a promising candidate for following the development of all neurons in the embryo, and eventually understanding associated molecular mechanisms. The resulting 'neurodevelopmental atlas' would represent the first view of how an entire nervous system forms.

Despite the potential of the nematode as a model, imaging neurodevelopment (Wu et al., 2013a) throughout embryogenesis is challenging due to embryonic sensitivity to photodamage and photobleaching, limiting imaging to several hours on most systems; the need for subcellular spatial resolution due to the small size of the embryo; and motion blur caused by rapid embryo movement after muscular twitching begins. Once images are captured, data analysis poses new problems: while it would be easy to assemble an atlas of neuronal positions and morphology if all cells were easily identifiable in one animal, techniques that allow imaging with single-cell contrast (such as Brainbow [Livet et al., 2007]) are unavailable in the nematode. Currently, any attempt to build a neurodevelopmental atlas would require imaging small numbers of non-overlapping, easily distinguishable neurons, and finding methods to combine the data from multiple embryos into a composite whole. To our knowledge, comprehensive solutions to these problems do not yet exist.

Recent advances in light-sheet fluorescence microscopy (LSFM [Santi, 2011]) have solved many of the imaging problems outlined above. LSFM sweeps a thin sheet of light through the sample, relying on perpendicular detection of fluorescence. This geometry allows far more rapid imaging and reduced phototoxicity relative to confocal microscopy (Huisken et al., 2004; Holekamp et al., 2008), enabling the use of LSFM in a variety of transformative applications. These include recording whole-brain calcium signaling in larval zebrafish (Ahrens et al., 2013; Ito, 2013), and imaging (Wu et al., 2011; Keller et al., 2008) and tracking (Amat et al., 2014; Bao, 2006; Santella et al., 2010) large numbers of cells in developing embryos. Multiple LSFM implementations now obviate the problems of motion blur and photo damage in worm embryos (Wu et al., 2011; Wu et al., 2013; Kumar et al., 2014; 2015), and also offer sufficient spatiotemporal resolution (sub-μm in all three spatial dimensions, sub-second volumetric imaging [Wu et al., 2013; Kumar et al., 2014]) that subcellular morphology may be observed over the entire 14-hour period of embryogenesis. Despite these advances, morphological changes still pose problems when trying to follow individual cells, or when combining data from multiple embryos.

To address these problems, we have generated a nematode strain that expresses fluorescent markers within specific cells, and designed software that uses these markers to computationally 'untwist' the embryo, resulting in straightened volumes that significantly ease the tracking of developmental events in later embryonic stages (described briefly in a preliminary conference proceeding [Christensen, 2015]). Our open-source software is based on the NIH’s Medical Image Processing, Analysis, and Visualization (MIPAV [McAuliffe, 2001; Haak et al., 2015]) platform, implemented as a standalone plugin (http://mipav.cit.nih.gov/plugin_jws/mipav_worm_plugin.php). Computational untwisting algorithms have previously been used to straighten images of L1 larval worms for use in tracking nuclear position (Peng et al., 2008; Long et al., 2009) in both two and three dimensions, but to our knowledge, these algorithms are not suitable for the nematode embryo. In addition to the untwisting capability, our plugin includes the ability to annotate and track 3D positions over time, allowing semi-automated quantification of cell and neurite positions in twisted (and untwisted) embryos. The positional data so derived also facilitate comparison and combination of information from multiple embryos, allowing us to create a composite model of development.

We demonstrate the capabilities of our method by computationally untwisting eight nematode embryos; tracking the position of seam cell nuclei, the canal-associated neuron (CAN), ALA, and AIY neuron cell bodies, and the growing neurites of the ALA neuron in the untwisted reference frame; and combining the data from multiple embryos to model the time-evolution of all these elements within the elongating embryo. We find that seam cell nuclear positions are highly stereotyped across different embryos, while the rate of elongation varies according to position along the embryo. Of the neurons we examined, ALA and AIY move in concert with neighboring seam cell nuclei, suggesting they are passively 'dragged' with the rest of the elongating worm embryo, while the CAN neurons actively migrate at a faster rate than the surrounding seam cell nuclei. Tracking ALA neurites reveals that anterior-posterior neurite outgrowth starts toward the end of elongation and continues after cells reach their final positions. Our method is the first to track cell positions in the context of the entire embryo, from the beginning of twitching until hatching. We anticipate that our software will significantly further the ability to examine C. elegans development in the post-twitching regime and lay a foundation for understanding the formation of the C. elegans nervous system.

## Results

In order to computationally straighten an embryo, an essential first step is defining limits of the growing worm body, thus specifying how the embryo folds inside the eggshell. Nematode embryos undergo both bending and helical twisting around the nose-to-tail axis (Figure 1—figure supplement 1) posing challenges in untwisting the embryo relative to larval or adult nematodes. Our approach uses fluorescent markers driven by cell-specific promoters to define the boundaries of the worm body. We use a seam cell marker (SCM::GFP) to label the 20–22 seam cell nuclei, identifying the left and right sides of the worm; and a dlg-1::GFP fusion protein to label apical gut junctions and hypodermal junctions, revealing the locations of the anterior tip of the pharynx (hereafter referred to as the nose), tail, midline, and hypodermal cell boundaries (Figure 1A,B). This combination of markers allows automated segmentation of seam cells and manual identification of the nose, tail, and sides of the worm, thus enabling us to model the twisted, bent embryo within the eggshell, and serving as a basis for computationally untwisting the worm (Figure 1C).

![Figure 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig1-v2.jpg)

**Figure 1.:** (A) An image of a threefold embryo in the twisted state, showing the untwisting markers. (B) The same image as in (A) with the untwisting markers labeled. Asterisks mark seam cell nuclei, and the dashed line indicates the midline marker. (C) The same embryo as in (A, B), after untwisting. Asterisks and dashed line as in B. (D–F) Further detail lattice creation and splines that model embryo. (D) Left: same embryo volume as in (A). Right: accompanying schematic showing the seam cell nuclei in the twisted embryo (black circles) and midline (interior black line). (E) Lattice creation. As diagrammed in right schematic, parts (1) and (2), the user adds points to create a lattice (blue and yellow lines). After the lattice is built, the algorithm generates splines defining the edges of the worm (orange and purple lines) automatically. The midline is also defined with a spline (red line at left). (F) The embryo volume and accompanying schematic showing a completed lattice and model. (G) The embryo volume and accompanying schematic after untwisting. All scale bars: 10 μm.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Evidence for helical twisting, highlighted on four pairs of consecutive seam cell nuclei. If no helical twisting occurs, yellow lines (connecting seam cell nucleus pairs) should appear parallel to each other when sighting down the midline of the worm (red line). If helical twisting is present, yellow lines should appear to twist about the midline. Arrows denote the direction of lines for four pairs of consecutive seam cell nuclei: note obvious and apparent angular twist between pairs 1 and 4. (B) Side view showing same data as in (A). As before, nuclei pairs 1 and 4 appear in close to perpendicular orientation to each other, despite the roughly parallel midline. Scale bar: 10 μm.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Coarse features such as seam cell nuclei are visible in single view iSPIM (A), but finer features such as junctions between hypodermal cells labeled with DLG-1::GFP are better resolved in the diSPIM (B), particularly in the axial direction (lower row). Scale bar: 10 μm. diSPIM, dual-view Selective Plane Illumination Microscopy; iSPIM, inverted Selective Plane Illumination Microscopy.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) XZ and YZ views of an untwisted worm embryo using a lattice comprised of every other seam cell nucleus, a total of 12 points. This lattice fails to capture bends in the animal and does not create smooth left and right edges in the untwisted worm embryo. (B) Same as (A) but using a lattice built with all seam cell nuclei and the nose, a total of 22 points. This lattice still fails to capture some bends in the worm, and the extension of the tail. (C) Same as (A) but using a lattice built with all seam cell nuclei as well as additional points in highly bent regions in the worm embryo, plus a pair of points marking the tail, for a total of 28 points. Bends are accurately captured in the resulting untwisted volume. (D) Several additional lattice points were added to the lattice in (C), along the edges of the animal, for a total of 36 points. No noticeable improvements are apparent. Scale bar: 10 μm.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) The twisted L2 larval volume displayed in the MIPAV volume renderer. (B) The twisted L2 larva after lattice-building. (C) The L2 larval worm after untwisting. See also Video 7. MIPAV, Medical Image Processing, Analysis, and Visualization

We used a dual-view selective plane illumination microscopy (diSPIM) implementation of LSFM to capture images of developing embryos (Wu et al., 2013; Kumar et al., 2014). The diSPIM was chosen due to the combination of high-imaging speed and isotropic resolution that it provides, making the identification of cells and cellular structures in a twisted-up embryo significantly easier than with lower resolution alternatives (such as single-view light-sheet microscopy, Figure 1—figure supplement 2). After images are acquired in the diSPIM, registered, and deconvolved, a user begins untwisting by downloading and running our software (http://mipav.cit.nih.gov/plugin_jws/mipav_worm_plugin.php, Supplementary file 1).

First, seam cell nuclei are automatically detected, segmented, and paired to create candidate lattices. Seam cell segmentation and lattice-building are manually verified by a user, who can also incorporate additional information derived from pharyngeal and hypodermal markers, which are difficult to automatically segment (Figure 1D,E). Several possible lattices are generated, and the five most likely to be correct are displayed to the user for selection and editing of the correct lattice. The resulting lattice is used to generate a 3D model of the worm volume (Figure 1F, Video 1). In cases where automated lattice-building fails, lattices can be built manually by marking the positions of seam cell nuclei, nose, bends in the embryo, and tail. When manually building lattices, minimally 22 +2B lattice points are recommended (22 is the number of lattice points corresponding to seam cell nuclei, plus a pair of points to mark the nose, and B is the number of bends between seam cell nuclei in the embryo). Fewer lattice points than the number of seam cell nuclei gives unphysical, short volumes, and more than ~32 points does not noticeably improve quality in the untwisted volumes (Figure 1—figure supplement 3).

![Video 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-media1.mp4.jpg)

**Video 1.:** This animation provides a graphical representation of the computational steps used to segment seam cells, build a lattice, and straighten embryo volumes. For additional information refer to Supplementary file 1 and Appendix.

The first step in creating the 3D model is to generate curves defining the center and sides of the worm. The centerline curve is uniformly sampled to generate a series of planes extending along and normal to the curve, while avoiding overlap within the model. This series of restricted planes comprises the worm model and is updated as new lattice points are added. To generate a straightened volume, the voxels in the original image that intersect with the sampling planes in the worm model are captured, and the sampling planes and associated voxels are concatenated in the head-to-tail direction to generate a straightened volume (Figure 1G, Video 1). The same process can be used to straighten images of older animals (such as L2 larvae, Figure 1—figure supplement 4). More details are provided in Supplementary file 1 and Appendix.

In addition to untwisting, it is also useful to obtain the 3D position of a cell or point of interest within the nematode embryo. Thus, our software also includes an annotation capability, allowing a user to define points within the embryo for which they would like to obtain 3D coordinates both before and after untwisting (Supplementary file 1). The user adds annotations similarly to lattice points, marking the volume location where the desired point should appear. The user must also add an origin point from which the relative 3D position of all other points is calculated from. As pharyngeal labeling is consistent and bright in most diSPIM volumes, we use the nose as a standard origin in all datasets described in the paper. Once the origin and annotation points have been defined, the user can untwist the worm and obtain the 3D coordinates of each annotation point in a spreadsheet file.

In order to ensure that our algorithm did not alter the distance between portions of the embryo during the untwisting process, we compared the apparent 3D distance between, or along, landmark features within twisted and untwisted embryo volumes (embryos 1–6, Figure 2). First, we determined the distances between nuclei in seam cell pairs (Figure 2A,B). If untwisting did not effect morphology, we reasoned that these distance should be conserved regardless of whether the embryo is twisted or untwisted. We measured the difference between pair distance in twisted- and untwisted datasets at every fifth or tenth time point for both the first (H0) and last (T) pairs of seam cells in six different embryos, reasoning that the difference should be close to 0. The apparent untwisted distance between seam cell pairs H0 and T closely mirrored the values in the twisted worm, with the population average difference across timepoints and embryos (<μDifference, time>embryo ± population standard deviation <σDifference, time>embryo) for H0 0.4 µm ± 0.3 µm, and for T 0.3 ± 0.2 µm (Figure 2C, Figure 2—figure supplement 1, Supplementary file 5, Materials and methods). The largest difference at any individual timepoint between twisted and untwisted values was 1.7 µm for H0 and 1.2 µm for T.

![Figure 2.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig2-v2.jpg)

**Figure 2.:** Distances between seam cell nuclei (left) and pharyngeal lengths (right) were compared in twisted (A) and untwisted (B) worm embryos. All scalebars: 10 µm. (C) Comparative 3D distance measurements of seam cell nuclei pairs H0 and T (left graphs) and pharyngeal lengths (right graphs) for one representative embryo (a comparison across six different embryos is presented in Figure 2—figure supplement 1). In all cases, distance measurements in the twisted case are within 5 μm of distance measurements in the untwisted case.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Comparative 3D distance measurements of seam cell nuclei pairs H0 and T (left graphs) and pharyngeal lengths (right graphs) for six embryos. In all cases, distance measurements in the twisted case are within 10 μm of distance measurements in the untwisted case.

Since the model of the twisted embryo is based on positional coordinates of the seam cell nuclei, we would expect these paired distances in twisted- and untwisted embryos to agree. For a more stringent control, we also assessed the apparent distance between nose and the pharynx-gut transition (effectively the pharyngeal contour length) in twisted and untwisted embryos (Figure 2A,B). Although the pharynx is not used as a landmark for defining the worm model used in untwisting, we still expect its contour length to be conserved despite untwisting. Here, too, we measured a close correspondence (typically less than 5% of the total pharyngeal length). The population <μDifference, time>embryo ± <σDifference, time>embryo between twisted and untwisted pharyngeal lengths was 2.5 µm ± 1.6 µm (with the maximum difference between the untwisted and twisted values for any individual timepoint being 8.8 µm, Figure 2C, Figure 2—figure supplement 1). We conclude that our untwisting procedure accurately captures distances present in the twisted embryo.

The combination of untwisting and annotation capabilities we developed allows the analysis of overall morphological changes in a developing embryo and the precise tracking of positions for individual cells or subcellular structures. We first examined overall morphological changes in the nematode embryo. Embryos lengthened (from 86 ± 5 µm at early 1.5-fold, measured from the nose to the tail, to 162 ± 19 µm within the last 30 min before hatching, measured from the nose to the last pair of seam cells, mean ± standard deviation [SD], 5 embryos) and narrowed in width (measured diameter across the widest cross-section 22 ± 1 µm at early timepoints, and 16 ± 1 µm at late timepoints, mean ± SD, 5 embryos) as they progressed from comma stage to late-3 fold (Figure 3A–H, Figure 3—figure supplement 1; Figure 3—figure supplement 2; Video 2). We used our software to manually annotate and extract the positional trajectories of seam cell nuclei during this time period, as they moved relative to the nose of the animal (Figure 3J–3L, Figure 3—figure supplement 1). We note that seam cell V5 divides late in the threefold embryo into Q and V5 daughters; in such cases, we tracked the anteriormost daughter, Q, and thus refer to V5 as Q/V5 in our paper. The motion of seam cell nuclei followed relatively simple trends that were easily evident, despite the noise present in the raw untwisted trajectories. During elongation, seam cell nuclei moved laterally (‘X’ motion, Figure 3J) towards the midline, while maintaining a relatively fixed dorso-ventral position (‘Y’ motion, Figure 3K). Along the axial, head-to-tail axis, the displacement of seam cell nuclei was biphasic, showing a fast, approximately linear dependence on time, followed by a slower plateau (‘Z’ motion, Figure 3L) (Priess and Hirsh, 1986; Chin-Sang and Chisholm, 2000; Ding et al., 2004; Norman and Moerman, 2002). While embryo elongation has been examined before (Priess and Hirsh, 1986), our method is the first that allows 3D interrogation of whole, live, untwisted nematodes at arbitrary timepoints in embryogenesis (Figure 3, Video 2).

![Figure 3.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig3-v2.jpg)

**Figure 3.:** Selected volumetric timepoints pre (A–D) and post (E–H) untwisting, with canonical state of embryo indicated at bottom. See also Video 2. (I) Cartoon of untwisted embryo, indicating coordinate system. (J–L) X, Y, and Z movements of circled seam cell nucleus in (I). Measurements are indicated relative to the animal’s nose, fixed as the origin in all untwisted datasets. All scalebars: 10 μm.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Comparative timepoints were selected based on the H1R seam cell shifts. Max projections of volumetric images are shown. Note the underlying similarity in overall shape across animals. Scalebar: 5 μm.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Comparative timepoints were selected based on the H1R seam cell shifts. Max projections of volumetric images are shown. Note the underlying similarity in overall shape and seam cell positions across animals. Scalebar: 5 μm.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Before fitting, raw data are treated to remove obvious outliers (top row) and to fill in missing data (mid, bottom rows). In both cases, outliers and ‘gaps’ within data are found manually, and replaced by averaging the data points immediately preceding or following the outlier or gap. Examples of raw data prior to this linear interpolation are shown at left, and examples of processed data at right. The example axial distance data shown here are derived from seam cell 3. Red arrows indicate outliers or gaps. Data shown are from the left H2 seam cell nucleus.

![Video 2.](https://cdn.elifesciences.org/articles/10070/elife-10070-media2.mp4.jpg)

**Video 2.:** Despite errors in individual untwisted volumes, the overall pattern of embryonic development and elongation is clear.

The strong qualitative similarities in seam cell nuclear trajectories among the five embryos we inspected led us to investigate whether data from different embryos could be combined to yield a composite model of development representing growth in an 'average' embryo. Initial examination of the axial (nose-to-tail) seam cell nuclear trajectories from different embryos suggested a high degree of stereotypy; except for a relative shift in time, the trajectories displayed very similar shapes (Figure 4A). We thus shifted the axial data in time until the trajectories from multiple embryos overlaid (Figure 4B, Figure 4—figure supplement 1). We determined the amount of shift by using a three parameter logistic function to fit the raw axial displacement data (Figure 4—figure supplement 2, Tables 1, 2, Materials and methods), overlaying the data from various embryos until the inflection points in each curve were identical.

![Figure 4.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig4-v2.jpg)

**Figure 4.:** (A,B) Axial seam cell nuclear trajectories from different embryos are similar in shape, but shifted in time. (C,D) Shifting in time aligns the trajectories. (E, F) Averaging the shifted trajectories. (G, H) Fitting the shifted trajectories. Left graphs: cartoon schematic, Right graphs: data. For clarity, we have shown the shifting, averaging, and fitting process for two embryos, but note that to construct our 'composite' model of seam cell nucleus behavior we have applied the same process to five embryos (see 'Materials and methods' for further details).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Data from two embryos are shown before (top) and after (bottom) temporal alignment. The data derived from embryo 4 was shifted 5 timepoints to the right, following the procedure described in 'Materials and methods'. Data shown are the z positions from the right V3 seam cell nucleus. Only a portion of the data, at early timepoints, is shown to highlight the shifting procedure.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Different fitting models (see also Table 2) for embryonic axial displacement are plotted (red curves), against raw data (blue diamonds). Also shown on each plot are quantitative measures of goodness of fit: the squared sum of residuals (SSR), the Akaike Information Criterion (AIC), and the Schwarz Criterion (SC). Of the three-parameter fits, the three-parameter logistic provides the best overall fit, both from visual inspection and quantitatively (lowest SSR, AIC, and SC scores). The four-parameter Morgan Mercer Flodin and Logistic curves show slightly better qualitative fits, especially at early time points, but require careful tuning of the initial parameters to converge. For all axial displacement data shown elsewhere in the paper, the three-parameter logistic curve was used as a fitting function. Although the axial displacement data shown here are derived from the left seam cell nucleus H0, we observed the same trends for all seam cells.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Comparisons in axial position vs. time for a seam cell nucleus (right H1, upper graph) and for CANL (lower graph). For most nuclei, as in the upper graph, positions were stereotyped to within 4.6 μm (as quantified by <<σZ>time>seam cell; see also 'Materials and methods'). As indicated in the lower graph, we noticed CANs in embryo 5 traveled a shorter distance than in other embryo datasets (resulting in a larger value of <σZ>time for CANL, see Supplementary file 2). Data are shown after applying the shifting procedure described in 'Materials and methods'.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Examples of raw, averaged data (derived from 4 to 5 embryos, blue dots) and fits (black lines). Linear, power, and three-parameter logistic curve examples were taken from the right H0 seam cell nucleus, the quartic polynomial example from AIYL, and the smoothing fits from CANR. See also Table 1. Note the different ranges in ordinate axes.

We applied the same time shift to the X- and Y- seam cell nuclear coordinates, finding that seam cell nuclear positions followed similar trajectories throughout elongation (average SD calculated across all 20 seam cell nuclei and all timepoints, <<σX>time>seam cell 0.8 µm, <<σY>time>seam cell 0.7 µm, <<σZ>time>seam cell 4.6 µm, see also Figure 4—figure supplement 3, Table 1, and 'Materials and methods'). After shifting, we averaged (Figure 4C) and fitted (Figure 4D, Figure 4—figure supplement 4, Table 1, Supplementary file 2) the embryo XYZ trajectories, thus generating positions representing the noise-free time evolution of seam cell nuclei. We note that the choice of fitting functions is somewhat arbitrary. For axial positions, the growth that we and others (Priess and Hirsh, 1986) have observed leads to a sigmoidal fitting function. Amongst the various three-parameter sigmoidal functions (Table 2), we found that the three-parameter logistic function gave the best qualitative and quantitative (Figure 4—figure supplement 2) agreement with the data. We fitted lateral (‘X’) seam cell nuclei positions with a two parameter power law function, and dorso-ventral (‘Y’) positions with a linear function, as empirically these functions described our data well. Despite the ad hoc nature of these fits, we found that fitted values were within 1.5 µm of the X, Y averaged data, and within 7.5 µm of the Z averaged data (Supplementary file 3). For reference, the total length of the untwisted embryo at the final time point was 162.0 ± 18.7 µm (mean ± SD, 5 embryos), measured from the nose to the last pair of seam cells, and the corresponding diameter at the last time point 16.1 ± 1.3 µm, measured at the widest cross-section in the animal.

**Table 1.**
 Fitting functions tested for describing axial displacement. Equations are used in Figure 4—figure supplement 2. L: length; t: time. Other parameters and their meaning are listed in the table. For all axial coordinates in this paper, a three-parameter logistic function was used.


<table>
  <thead>
    <tr>
      <th>Fitting type</th>
      <th>Equation</th>
      <th>Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>von Bertalanffy</td>
      <td>L = A(1-exp[-B(t-C)])</td>
      <td>A: upper asymptotic length B: growth rate C: time at which L = 0</td>
    </tr>
    <tr>
      <td>Exponential</td>
      <td>L = A-(A-B)exp(-Ct)</td>
      <td>A: upper asymptotic length B: lower asymptotic length C: growth rate</td>
    </tr>
    <tr>
      <td>Three-parameter Gompertz</td>
      <td>L = A[exp(-exp(-B(t-C)))]</td>
      <td>A: upper asymptotic length B: growth rate C: time at which L = 0</td>
    </tr>
    <tr>
      <td>Three-parameter logistic</td>
      <td>L = A/[1+exp(-B(t-C))]</td>
      <td>A: upper asymptotic length B: growth rate C: inflection point</td>
    </tr>
    <tr>
      <td>Four-parameter Morgan Mercer Flodin</td>
      <td>L = A – (A-B)/(1+(Ct)D)</td>
      <td>A: upper asymptotic length B: length at t = 0 C: growth rate D: inflection parameter</td>
    </tr>
    <tr>
      <td>Four-parameter logistic</td>
      <td>L = B + (A-B)/{1+exp[(C-t)/D]}</td>
      <td>A: upper asymptotic length B: lower asymptotic length C: growth rate D: steepness parameter</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Fitting functions for each cell type. X, Y, Z trajectories were fitted as indicated functions of time (t).’ 50-point smoothing’ refers to smoothing the input data with a 50-point span, using weighted linear least squares and linear fitting.


<table>
  <thead>
    <tr>
      <th>Cell type</th>
      <th>X fit</th>
      <th>Y fit</th>
      <th>Z fit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Seam cell nucleus</td>
      <td>Power X = atb+c</td>
      <td>Linear Y = p1*t + p2</td>
      <td>Three-parameter logistic Z = A/(1+exp(-B(t-C)))</td>
    </tr>
    <tr>
      <td>CANR/L</td>
      <td>50-point smoothing</td>
      <td>50-point smoothing</td>
      <td>Three-parameter logistic Z = A/(1+exp(-B(t-C)))</td>
    </tr>
    <tr>
      <td>AIYR/L</td>
      <td>4th degree polynomial X = p4*t4+p3*t3+p2*t2+p1*t+p0</td>
      <td>Linear Y = p1*t + p2</td>
      <td>Three-parameter logistic Z = A/(1+exp(-B(t-C)))</td>
    </tr>
    <tr>
      <td>ALA ALA xR1/xL1 ALA xR2/xL2</td>
      <td>Linear X = p1*t + p2</td>
      <td>Linear Y = p1*t + p2</td>
      <td>Three-parameter logistic Z = A/(1+exp(-B(t-C)))</td>
    </tr>
  </tbody>
</table>

The averaged, fitted seam cell nuclei data allowed us to inspect the relative relationships among seam cell nuclei in an elongating embryo (Figure 5A, Videos 3,4). Since we fixed the nose as the stationary origin in our untwisting procedure, this location does not move in 4D representations of the fitted embryo. In this 'nose-centric' reference frame, points further from the origin also appear to move faster and farther than points closer to the origin. To better understand the growth rates of individual seam cell nuclei in relation to their neighbors, and the overall length changes within the elongating embryo in a frame-independent manner, we also computed the differences in position between adjacent pairs of nearest-neighbor seam cell nuclei over time (Figure 5B–D, Figure 5—figure supplement 1). In ‘X’ and ‘Y’ dimensions, seam cell nuclei exhibited similar movement patterns, remaining largely stationary in ‘Y’ (Figure 5—figure supplement 1), and moving inwards (toward the origin) in ‘X’ (Figure 5—figure supplement 1) at similar rates. In contrast, seam cell nuclei movement along the ‘Z’ direction was more heterogeneous. For example, the distance between the origin and nuclei of seam cell pair H0, measured from the fitted data, changed from 2.4 µm to 23.8 µm over elongation (Figure 5B), while the distance between seam cell nuclear pairs V6 and T remained essentially constant, at 22.5 µm (Figure 5D). Thus, the rate of increase in distance between the origin and H0 was significantly greater than the increase in distance between V6 and T, over the same period. Other adjacent nuclear pairs separated at roughly similar rates from start to end of elongation (these pairs increased in distance 6.8 ± 2.8 µm, mean ± SD from 7 adjacent pairs of seam cell nuclei, again derived from the fitted data in Figure 5C). These trends were not the results of artifacts in our fitting procedure, as they were evident also in the raw, averaged data (compare left and right graphs in Figure 5B-D). The apparent differences in X- and Z- pre- and post-elongating seam cell nuclei positions that we observe are consistent with the asymmetric morphology of the pre-elongating embryo. Since the embryo starts out in a tadpole-like shape with the head larger than the tail, the seam cell nuclei in the head must move a greater distance than the nuclei in the tail to achieve a uniform diameter in the elongated embryo.

![Video 3.](https://cdn.elifesciences.org/articles/10070/elife-10070-media3.mp4.jpg)

**Video 3.:** The positions shown in the rendering are averaged, fitted values derived from five embryos, using the averaging and fitting procedure described in the text; the rendering thus represents a composite, 'best-guess' view as to seam cell evolution in a developing embryo. Times are indicated relative to the first fitted volume, and are 2.5 min apart.

![Video 4.](https://cdn.elifesciences.org/articles/10070/elife-10070-media4.mp4.jpg)

![Figure 5.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig5-v2.jpg)

**Figure 5.:** (A) Snapshots of the elongating embryo near start (Volume 30, left) and end (Volume 113) of elongation. Seam cell nuclei volumes are indicated as filled spheres, L/R axes are as indicated, seam cell nuclear identities indicated at the side of each snapshot, as is the origin (nose, ‘O’). See also Videos 3,4. Scalebar: 10 μm. (B–D) Axial differences over the course of elongation between adjacent seam cell nucleus pairs, sorted into greatest (B), intermediate (C), and least (D) bins, corresponding to red, gray, and blue coloring indicated in (A). Left graphs: raw, averaged data (as in Figure 4E, 4F). Right graphs: fitted data (as in Figure 4G, 4H).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A–D) Snapshots of the elongating embryo at start (above dashed line) and end (below dashed line) of elongation, as shown in lateral (X motion, A) and dorsal-ventral (Y motion, C) views. Distances from the origin in X (B, C) and Y (E,F) are also shown for each seam cell nucleus. Both averaged (B, E) and fitted (C, F) distances are displayed. Scalebars: 10 μm.

Embryo elongation is thought to be dependent on an actin-based contractile mechanism (Priess and Hirsh, 1986). The complex, position-dependent motion we observed is likely inconsistent with a simple, uniform contraction, as this phenomena cannot explain our finding that different regions of the embryo elongate at markedly different rates. To our knowledge, current models of embryo elongation have not taken into account the differential elongation we observed across the worm body. We expect that incorporating additional data derived from cell positions and subcellular markers (especially cytoskeletal [Priess and Hirsh, 1986; Gally et al., 2009]) in the embryo would help further refine existing models (Ciarletta et al., 2009) of embryo elongation.

Currently, building a composite model of neuronal positions and morphological development in the embryo depends on pooling distinct datasets from many independent embryos. Given our experience tracking seam cell nuclei, we next turned our attention to modeling the 4D motion of neurons and neurite outgrowth in the elongating worm embryo as a proof of concept for a neurodevelopmental atlas (Figure 6A, Videos 5,6). Four of the five embryos used in constructing our seam cell model also had neuronal cell bodies marked with a pceh-10::GFP construct; neurons included AIYL/R, CANL/R, and ALA. We manually annotated the position of these neuronal cell bodies, then temporally aligned, averaged, and fitted the positions as we did the seam cell nuclei (Figure 4). The axial motion of these neurons was qualitatively similar to the seam cell nuclei and could be well described by the three parameter logistic function. However, their XY motion appeared different than the seam cell nuclei. For example, the lateral motion of CANs could not be easily described by a simple function, so we used a 50 point smoothing of the averaged data as our 'fit'. The ALA X motion was better described by a 4th degree polynomial than a power law, so we used the former function to fit the data (Figure 4—figure supplement 4, Table 1). As evident by their axial displacements, ALA and AIYL/R moved similarly to nearby seam cell nuclei (Figure 6B). In contrast, CANs moved faster than adjacent seam cell nuclei, suggesting a more 'active' mode of migration (Figure 6C). Finally, the motion of ALA and CANs (especially CANL) were considerably more variable between datasets than the seam cell nuclei (Figure 4—figure supplement 3, Supplementary files 2,3,4). While it is currently unclear whether this variability is strain-dependent or reflects underlying biology, this observation underscores the need to study multiple embryos and assess the degree to which cellular motion is stereotyped in elongating embryos.

![Video 5.](https://cdn.elifesciences.org/articles/10070/elife-10070-media5.mp4.jpg)

**Video 5.:** As in these videos, all positions are averaged, fitted values derived from multiple embryos. View is from dorsal perspective. Red spheres represent CAN cell bodies, yellow spheres represent AIY cell bodies, and blue spheres and lines correspond to ALA and its neurites. ALA and AIY cell bodies appear to closely track neighboring seam cells during elongation, while the CAN neurons actively migrate. ALA neurite outgrowth starts toward the end of elongation and continues after most other morphological changes have ceased. Times are indicated relative to the first fitted volume, and are 2.5 min apart.

![Video 6.](https://cdn.elifesciences.org/articles/10070/elife-10070-media6.mp4.jpg)

To examine neurite outgrowth clearly, we created a two-color strain with GFP-labeled untwisting markers and a pceh-10::mCh construct to label neuronal cell bodies and neurites. We observed substantial mosaicism in terms of which cells were labeled from one embryo to the next with this strain. Although neurons were labeled with an extrachromosomal array and a certain degree of mosaicism could be anticipated, labeling differences from one animal to the next hindered our ability to track both ALA and CAN outgrowths. Nevertheless, we were able to obtain two datasets where the ALA neuron was labeled throughout most of our imaging period.

ALA is a single neuron with a cell body located in the dorsal portion of the head; a pair of long neurites extend ventrally from this cell body into the nerve ring, and then turn and extend posteriorly along the lateral nerve cord (White et al., 1986). Left and right ALA outgrowths could be readily identified and annotated in both twisted and untwisted embryos (Figure 6D, Figure 6—figure supplement 1). In modeling the left and right neurite shapes, we simplified them by annotating them as three distinct points (ALA: cell body; AxR1 or AxL1: point at which the neurite turns to extend posteriorly; AxR2/L2: neurite terminus; Figure 6E). We then measured the 3D displacements (relative to the nose, as before) of each independent point, shifting, averaging and fitting the data derived from two embryos (as outlined in Figure 4 and illustrated in Figure 6—figure supplement 1), to yield a noise-free representation of the neurite (Table 1). Aligning the fitted neurites to our reference embryo allowed inspection of ALA neurite growth in the context of the elongating embryo (Figure 6A, Videos 5,6), revealing that neurite outgrowth continued to occur for ~240 min after the other cells assumed their final positions at the end of elongation. We also segmented growing ALA neurites at several points in development to demonstrate that straightened images can be used to generate volumetric reconstructions of cell morphology throughout development (Figure 6—figure supplement 2.) We are unaware of any other work that has modeled the growth and positions of neurites in the post-twitching embryonic regime (for C. elegans or any other model organism).

![Figure 6.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig6-v2.jpg)

**Figure 6.:** (A) Early (left) and late (snapshots) in the elongating embryo. Gray spheres: seam cell nuclei; ALA cell body: blue sphere; ALA neurites: blue lines; AIY cell bodies: yellow spheres; CAN cell bodies: red spheres. Compare to Videos 5,6. (B) ALA (top), AIYR (middle), and CANR (bottom) axial trajectories (red curves) in relation to neighboring seam cells (blue curves). ALA and AIY cells maintain their relative position with respect to the rest of the elongating body, while CANs migrate faster than neighboring seam cells. (C) ALA cell body and neurite in the twisted embryo, highlighting morphological features (ALA: ALA cell body; AxL1/R1: junction between ventral and posterior neurite extension; AxL2/R2: posterior tip of the ALA neurites). (D) Axial trajectory of ALA neurite tip in relation to indicated seam cells. (E) Top and side models of ALA in untwisted reference frame, indicating neurite bend and terminus. Compare to Figure 6—figure supplement 2.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Axial distance (measured from the origin point) of the ALA cell body for two ALA datasets. Similar to seam cells, axial distance increases during elongation and then plateaus once elongation has finished. (B) ALA axial distance, derived from averaging the axial distances of the shifted ALA datasets. (C) A fitted curve describing axial motion of ALA, after averaging in (B). (D–F) Shifting, averaging, and fitting of axial motion for the AxR1 point in the ALA neurite (the position at which the ventral growth of the neurite changes to posterior growth). As there is little axial growth in this part of the neurite, axial movement mirrors that of the ALA cell body. (G–I) Shifting, averaging, and fitting of axial motion for AxR2, the tip of the posteriorly-growing ALA neurite. The posterior-ward axial extension of the neurite leads to a different pattern of axial movement than for the R1 point or the ALA cell body.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/10070/elife-10070-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) Exemplary data for a twofold embryo. Left column: raw data. Right column: segmented data. The red neuron is RMED, the orange neuron is ALA, and the purple neurons are the cell bodies of the AIY neurons. At this point in embryonic development, the ALA neurites have extended ventrally and begun extending posteriorly, but have not undergone much extension. (B) Same embryo and color-scheme as in (A), but now early threefold stage. More ALA neurite extension is evident. (C) Same as in (B), but at a later stage. The ALA neurites have extended approximately 1/3 of the way to the tail at this point. In addition, neurite extension can also be observed in the AIY and RMED neurons. Scalebar: 10 μm.

## Discussion

The C. elegans cell lineage is invariant (Sulston et al., 1983), and tracking cells in the L1 larva has revealed that cellular positions in post-hatching animals are relatively stereotyped (Long et al., 2009). Our work suggests that this positional stereotypy extends to the cells in the late embryo as well. However, we also found that in the case of cells or structures which actively migrate, such as the CAN neurons and ALA neurites, there seems to be greater variability in terms of end position and growth rate. To some extent this is not surprising; as these cells and neurites move longer distances than most other cells, and depend on actively finding their way in a complex environment (as opposed to passive movement in response to elongation), there may be more room for variability in how they travel and reach their destinations.

On a more general level, we also observed variability in the temporal shifts necessary to align each elongating embryo to the reference dataset (embryo 1). Some of this variability may be due to relatively mundane explanations: embryos were at slightly different ages when imaging began, and temperature was moderately controlled (to within 2 to 3°C both during imaging and strain growth). Intrinsic developmental variability, caused by maternal effects or exposure to imaging could also have played a role in the slightly different patterns of development we observed across embryos.

Expanding the work we describe here to other migrating and non-migrating neurons should make clear whether there actually is a difference in positional variability between migrating and non-migrating cells. Adding additional data to our 4D model is conceptually straightforward: strains with distinguishable neurons can be crossed into the untwisting background, untwisted, trajectories of cells and outgrowths fitted, and subsequently registered with previously derived data. 'Filling in' the positions of all neurons and outgrowths in the developing embryo would form the basis of the 4D atlas of neurodevelopment, and could be combined with functional activity mapping and gene expression data to provide a more comprehensive picture of animal development in late embryogenesis.

Our untwisting and annotation plugin is designed to be flexible, so that it can be applied to most problems involving tracking position and morphology of distinguishable structures in the nematode embryo. The core of the plugin relies on defining the sides of the worm embryo; although our work uses a specific set of markers, we note that any other markers which define the edges of the worm body should also work. The annotation capability is also flexible; as it is based on manual annotation, almost any distinct structure can be annotated. Finally, while the isotropic resolution of the diSPIM is very helpful in resolving fine embryonic detail (Figure 1—figure supplement 2), our untwisting algorithm is compatible with other high-resolution imaging methods. For example, we used a super-resolution two-photon instant structured illumination microscope (2P ISIM) (Winter, 2014) to image and untwist a bent L2 larval worm, obtaining clear images of this relatively large specimen (Figure 1—figure supplement 4, Video 7). Our plugin is designed specifically for untwisting nematode embryos, and as such is unlikely to be immediately applicable to other biological systems without substantial modification (we know of few non-nematode systems that have the same vermiform shape and degree of twisting and movement). However, some of the more general concepts we implement, such as the benefit of aligning and pooling information derived different datasets to generate an overall 4D view of development, are likely applicable to more systems than just the worm.

![Video 7.](https://cdn.elifesciences.org/articles/10070/elife-10070-media7.mp4.jpg)

**Video 7.:** The image was imported into ImageJ and the Magenta LUT was applied to the stack. The volume shown here corresponds to the untwisted volume in Figure 1—figure supplement 4.

Despite the power of our semi-automated approach, several areas for improvement remain. Automated lattice-building assumes the embryo has 20-22 seam cell nuclei on which the lattice is based; in early periods of elongation (especially the 1.5- to 2-fold transition) expression is absent in some seam cell nuclei, requiring manual lattice-building. In addition, time spent in editing automatic segmentation and lattice generation results in ~8 hr of manual work when untwisting an embryo spanning 100–150 timepoints. Fully automated untwisting is not currently feasible, but the development of alternative markers may enable this goal. Second, although the positions of cells and neurites in the growing embryo can be determined with micron-scale precision, and placed in context with their neighbors, additional methods are needed to place the full morphological volume of a given cell within the untwisted embryo. While our data are of sufficient quality to segment such morphology in an untwisted animal (Figure 6—figure supplement 2, Video 8), the general question about how to combine morphological segmentations from distinct, untwisted embryos remains. New methods developed for pre-twitching embryos may prove useful in this regard (Santella et al., 2015).

![Video 8.](https://cdn.elifesciences.org/articles/10070/elife-10070-media8.mp4.jpg)

**Video 8.:** The volume was segmented and rendered in Imaris.

A more significant and long-term set of technical problems for completing the neurodevelopmental atlas relates to the generation of fluorescent markers and strains that provide sparse, optically resolvable neurons. Most fluorescent strains label multiple neurons that are too close in space and time to be easily resolved – possible strategies to 'separate' these neurons might include 'Brainbow' (Livet et al., 2007) (spectral separation of densely labeled neurons) or heat-shock-based approaches (Halfon et al., 1997; Bacaj and Shaham, 2007) (temporal separation of densely labeled cells). Even if such strains are built, the identity of the resulting neurons will need to be verified. As lineaging (Bao, 2006) in C. elegans has been carried out to just before twitching begins (Giurumescu et al., 2012), in principle neurons can be identified by matching early expression to lineage data. If expression turns on after twitching, lineaging would also need to be extended into the post-twitching regime. Such 'deep lineaging', or tracking the coordinates of all nuclei through twitching would be a valuable and complementary effort to untwisting. Finally, we note that the expression pattern of fluorescent proteins within individual neurons could be further optimized. For almost all strains (except DCR4209 which contained membrane-targeted mCherry), fluorescent proteins were expressed cytoplasmically. An improved strategy would combine such cytoplasmic labeling with membrane targeting, better filling out very thin neuronal outgrowths that otherwise might be missed due to low expression; a similar strategy was adopted in super-resolution microscopy to trace thin neurites (Lakadamyali et al., 2012).

## Materials and methods

### Strains

Nematode strains were kept at 20°C, and grown on NGM media plates seeded with E. coli OP50. The untwisting strain is SLS1 xnIS17 [dlg-1::GFP + rol-6]; wIS51 [SCM::GFP]. Strains used to construct SLS1 were FT63 [xnIS17 dlg-1::GFP + rol-6] (Totong et al., 2007) and JR667 [wIS51 SCM::GFP] (Terns et al., 1997; Koh and Rothman, 2001). Strains were crossed together to generate an animal containing these transgenes. Strains imaged for the paper include SLS1, DCR4209, and DCR4221. Strain DCR4209 contained the following transgenes: olaex2457 [P.ceh-10::mCh-PHd (25 ng/μL) + unc122::RFP (30ng/μL)]; xnIS17 [dlg-1::GFP + rol-6]; wIS51 [SCM::GFP]. To create olaEX2457, 4132 bp upstream of the transcriptional start site were isolated using the following promoters: Forward AGC TCC TGC ACT CTT CTG ATC; Reverse CAC AAG AGA AAA GTG GCT GCT TAT C. Strain DCR4221 contained the following transgenes: lqIS4 (Wenick and Hobert, 2004) [ceh-10promA::GFP]; xnIs17 [dlg-1::GFP + rol-6]; wIs51 [SCM::GFP]. Detailed subcloning information for olaex 2457 can be provided upon request.

### Sample preparation

As previously described, worm samples were prepared for diSPIM (Wu et al., 2011; Bao and Murray, 2010; Kumar et al., 2014): adult animals were placed in buffer and cut to liberate embryos, embryos transferred to poly-L-lysine-coated coverslips in the diSPIM imaging chamber, and imaged once they reached the bean-to-comma stage of embryonic development.

### Data acquisition

All data were acquired on either a first-generation diSPIM (Wu et al., 2013) or a more recent fiber-coupled version (Kumar et al., 2014). Dual-color data were taken sequentially (first the 488-nm excitation for the GFP channel, and then 561-nm excitation for the mCherry channel) in a plane-by-plane (5 ms GFP collection, 5 ms mCherry collection per axial position in the embryo) fashion. Given 50 planes per view, and two perpendicular views, this resulted in an acquisition time of 1 s per 2-color diSPIM volume. For most datasets in this paper (embryos 2-8, as referred to elsewhere in the text), single-color volumes were acquired every 5 min, but for one datastet (embryo 1), single-color volumes were acquired every 2.5 min. Dual-color acquisitions were used to track ALA neurite outgrowth (embryos 7 and 8). Acquisition code, written in LabVIEW, is available at http://www.wormguides.org/dispim/dispim-downloads.

For 2P ISIM imaging, we used 900-nm excitation and two 680-nm short-pass filters (Semrock, FF01-680/SP-25) in our emission path to filter illumination light. L2 larvae of strain SLS1 were immobilized with 50 mM levamisole (Sigma-Aldrich; St Louis, MO) and imaged on an agarose pad sandwiched between two #1.5 coverslips. Volumetric images of the entire specimen were acquired by manual XY translation of the stage between fields of view. Each raw frame was acquired in 200 ms; data used in this paper were derived by averaging six raw frames per axial position. Axial positions were spaced 0.333 μm apart. Individual 3D image stacks were stitched and overlaid to reconstruct the entire L2 stage worm using a custom plugin developed for MIPAV (available online at www.cit.nih.gov/mipav). After stitching, the reconstructed L2 stage worm volume was further processed with 40 iterations of Richardson-Lucy deconvolution.

### Shifting and averaging trajectories derived from different embryos

Cells from different embryo datasets exhibited qualitatively and quantitatively similar trajectories, so we aligned and then combined them to generate averaged, noise-free trajectories. First, coordinate trajectories (X, Y, or Z positions (Figure 3I) as a function of time) were 'cleaned' to remove obvious outliers, or to linearly interpolate gaps in the raw data (Figure 3—figure supplement 3). Second, the axial (‘Z’) coordinate of each cell was fitted to a three parameter logistic function (Table 2) using Growth II (Pisces Conservation) or MATLAB (Mathworks) software, as this function provided a better fit than other three parameter growth curves, and did not require careful tuning of initial parameter values, as did the four parameter growth curves we tested (Figure 4—figure supplement 4, Table 1). Third, we aligned datasets from embryos 2-5 (volumes recorded every 5 min) to embryo 1 (volumes recorded every 2.5 min), by (i) determining the inflection time point (‘C’ in Table 1, 2) for each cell’s fitted axial position and (ii) shifting the data an integral number of time points so that the inflection time points from embryos 2-5 agreed with the inflection point for embryo 1. For example, for the data shown in Figure 4—figure supplement 1 for seam cell V3R nuclei, embryo 1 had inflection point 42.6, and embryo 4 had inflection point 37.7, so the V3R trajectory for embryo 4 was shifted 42.6-37.7 = 5 timepoints to the right, to match the trajectory for embryo 1. The same integer time point shift was then applied to the corresponding ‘X’ and ‘Y’ coordinate trajectories for each cell. Fourth, after shifts were applied, coordinate trajectories were averaged. Finally, to generate noise-free trajectories, the average trajectories were fitted (functions chosen for the fits are shown in Figure 4—figure supplement 4 and Table 1).

To examine the degree to which embryo positions agreed after the shifting procedure, we computed SD between embryo positions at each time point (Supplementary file 2). With the exceptions of the CAN neurons, the X and Y positions of cells were stereotyped to within 2 μm, and the Z positions within 10 μm.

### Validating fits for each embryo

The majority of cells’ coordinate trajectories were well described by power (X coordinate), linear (Y coordinate), and three-parameter logistic (Z coordinate) functions (Figure 4—figure supplement 4, Tables 1, 2, Supplementary file 3). However, two cell types, CAN and AIY, were not well described by any of the common fitting functions we surveyed (e.g. power, exponential, Gaussian, rational functions). For these cells, we instead used 50 point smoothing (for CAN X and Y coordinates) or a quartic polynomial function (for AIY X coordinates) to reduce noise in the shifted, averaged trajectories. To estimate how well the curve fitting described the averaged trajectories, we calculated the absolute differences between averaged and fitted coordinates at each time point, and then calculated the means and SD of these differences across time. These data are recorded in Supplementary file 3 as μ avg-fit, time and σ avg-fit, time. We also computed the average over all seam cell nuclei of these average differences to generate <μ Xavg-Xfit, time>seam cell; <μ Yavg-Yfit, time>seam cell; and <μ Zavg-Zfit, time>seam cell resulting in values of 0.5 µm, 0.6 µm, and 3.7 µm. In XY, similar average statistics were found for all cell types. In the Z coordinate, CANL stood out as more variable, as its μ Zavg-Zfit, time was 10.2 µm (with a corresponding SD of 9.3 µm). We suspect the deviation between CANL data and fit arises more from the inherent variability with CAN cells (Supplementary file 2) than inherent problems with the fitting function choice.

### Population statistics

In several locations, we report population averages taken across some combination of seam cell nuclei, time, or embryos. We use μ and s to denote mean and SD, and <X>Y indicates an average of quantity X, across Y. For example, <μX>embryo stands for the population average across embryos, of mean X coordinate positions (each derived from an individual embryo).

For untwisting control measurements, we measured the difference between twisted and untwisted volumes for various distance metrics (between seam cells and along the pharynx). For each embryo, we computed the mean difference μDifference,time and standard deviation σDifference, time across time, and averaged these quantities to calculate a population <μDifference, time>embryo and population <σDifference, time>embryo across embryos.

To estimate inter-embryo and inter-seam cell nuclei positional (X, Y, and Z coordinates) variability over elongation, we shifted data from embryos until they overlaid in time, and next computed the SD between embryo positions at each aligned timepoint. Mean standard deviations <σX>time; <σY>time; and <σZ>time over all timepoints were calculated, and are reported in Supplementary file 2. To compute <<σX>time>seam cell; <<σY>time>seam cell and <<σZ>time>seam cell, we averaged mean SD across the 20 seam cell nuclei.

### Supplementary datasets

In accordance with eLife policy, we have made our raw annotation data and quality control measurements available: Supplementary file 4 contains the 3D positions of seam cell nuclei, neurons, and growing ALA axons. These data were used in Figures 3–6. Data are provided before outlier removal, shifting, and fitting. Supplementary file 5 contains the quality control measurements (distances between seam cell nuclei in the H0 and T pairs before and after untwisting, and pharyngeal contour lengths before and after untwisting) used to generate Figure 2.
