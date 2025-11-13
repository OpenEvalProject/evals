# Cell-accurate optical mapping across the entire developing heart

## Authors

- Michael Weber<sup>1</sup> ([ORCID: 0000-0001-8007-9975](https://orcid.org/0000-0001-8007-9975))
- Nico Scherf<sup>1</sup>
- Alexander M Meyer<sup>4</sup>
- Daniela Panáková<sup>4</sup> ([ORCID: 0000-0002-8739-6225](https://orcid.org/0000-0002-8739-6225))
- Peter Kohl<sup>6</sup>
- Jan Huisken<sup>1</sup> ([ORCID: 0000-0001-7250-3756](https://orcid.org/0000-0001-7250-3756)) †

### Affiliations

1. Max Planck Institute of Molecular Cell Biology and Genetics Dresden Germany
2. Harvard Medical School Boston United States
3. Max Planck Institute for Human Cognitive and Brain Sciences Leipzig Germany
4. Max-Delbrück-Center for Molecular Medicine in the Helmholtz Association Berlin Germany
5. DZHK (German Centre for Cardiovascular Research) partner site Berlin Germany
6. Institute for Experimental Cardiovascular Medicine University Heart Centre Freiburg - Bad Krozingen, Faculty of Medicine, Albert-Ludwigs University Freiburg Germany
7. Morgridge Institute for Research Madison United States

† Corresponding author

## Abstract

Organogenesis depends on orchestrated interactions between individual cells and morphogenetically relevant cues at the tissue level. This is true for the heart, whose function critically relies on well-ordered communication between neighboring cells, which is established and fine-tuned during embryonic development. For an integrated understanding of the development of structure and function, we need to move from isolated snap-shot observations of either microscopic or macroscopic parameters to simultaneous and, ideally continuous, cell-to-organ scale imaging. We introduce cell-accurate three-dimensional Ca2+-mapping of all cells in the entire electro-mechanically uncoupled heart during the looping stage of live embryonic zebrafish, using high-speed light sheet microscopy and tailored image processing and analysis. We show how myocardial region-specific heterogeneity in cell function emerges during early development and how structural patterning goes hand-in-hand with functional maturation of the entire heart. Our method opens the way to systematic, scale-bridging, in vivo studies of vertebrate organogenesis by cell-accurate structure-function mapping across entire organs.

## Introduction

Organogenesis builds on cell–cell interactions that shape tissue properties, and tissue-level cues that control maturation of cell structure and function. During cardiogenesis, region-specific heterogeneity in cellular activity patterns evolves as the heart undergoes large-scale morphological changes: The spontaneously active heart tube develops into the mature heart, in which pacemaker cells near the inflow site initiate the rhythmic excitation that spreads with differential velocities through distinct regions of the myocardium. This controlled cardiac activation gives rise to an orderly sequence of atrial and ventricular calcium release and contraction. An integrated understanding of cardiogenesis at the systems level requires simultaneous cell and organ scale imaging, under physiological conditions in vivo. Here, we present a high-speed light sheet microscopy and data analysis pipeline to measure fluorescent reporters of cardiomyocyte location and activity across the entire electro-mechanically uncoupled heart in living zebrafish embryos during the crucial looping period from 36 to 52 hr post fertilization (hpf). By noninvasively reconstructing the maturation process of the myocardium in its entirety at cellular resolution, our approach offers an integrative perspective on tissue and cell levels simultaneously, which has previously required separate experimental setups and specimens. Our method opens a new way towards systematic assessment of the mutual interrelations between cell- and tissue properties during organogenesis.

## Results

The zebrafish is an appealing vertebrate model system with a simple, yet functionally conserved heart. Light sheet microscopy has proven to be supremely suited for obtaining in vivo recordings of the intact embryonic zebrafish heart (Chi et al., 2008; Scherz et al., 2008; Arnaout et al., 2007; Trivedi et al., 2015). Whole cardiac cycles have been reconstructed in 4D (3D + time) using post-acquisition synchronization of high-speed light sheet movies in a z-stack. The resulting effective temporal resolution of about 400 volumes per second (Mickoleit et al., 2014) is unmatched by other in vivo volumetric imaging techniques such as light sheet microscopy with electrically focus-tunable lenses or swept, confocally-aligned planar excitation (Bouchard et al., 2015; Fahrbach et al., 2013; Hou et al., 2014; Liebling et al., 2005). We built a light sheet microscope tailored for high-speed imaging of the heart in the living zebrafish embryo. By fine-tuning the magnification and restricting camera readout to the center area of the chip, we balanced the field of view and the spatial and temporal sampling to record cardiac activation in the entire heart with cellular precision (Materials and methods).

We investigated whether post-acquisition synchronization could be extended to visualizing calcium transients in cardiac myocytes across the entire heart of living embryonic zebrafish expressing the fluorescent calcium reporter GCaMP5G under the myl7 promoter (Figure 1a, Figure 1—figure supplement 1). The genetically expressed calcium reporter provides a specific, consistent and non-invasive readout of cardiomyocyte activity in vivo (Figure 1b, Videos 1 and 2). In a side-by-side comparison, the calcium signal had good and stable fluorescent yield at low excitation power, superior to genetically expressed voltage reporters. Importantly, the calcium signal faithfully reports presence and timing of cell activation (Figure 1—figure supplement 2) (Kralj et al., 2011). To prevent interference of tissue movement and deformation with observed signals, we decoupled electrical excitation and mechanical contraction by inhibiting the formation of the calcium-sensitive regulatory complex within sarcomeres, using a morpholino against tnnt2a (Materials and methods). By mounting zebrafish embryos in low concentration agarose inside polymer tubes, we could position the embryos for precise optical investigation without anesthesia (Figure 1—figure supplement 1a,b). To attribute calcium dynamics to individual cardiomyocytes, we also recorded a fluorescent nuclear marker (myl7:H2A-mCherry). The high temporal (400 Hz) and spatial sampling (0.5 µm pixel size) was adequate for computing normalized average calcium transients throughout the cardiac cycle for each cell across the entire heart (Figure 1—figure supplement 3, Video 3, Materials and methods).

![Figure 1.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-v1.jpg)

**Figure 1.:** (a) Transmitted light microscopy image with ~250 µm-sized, two-chambered heart (shown as fluorescence image with light sheet illumination path). (b) Genetically encoded fluorescent markers expressed in myocardial cells report calcium transient activity and cell positions. Volumetric movies were reconstructed from multiple high-speed movies, each with a temporal resolution of 2.5 ms and a voxel size of 0.5 µm in xy and 1 µm in z. Image data are available at Weber et al. (2017). (c’) Normalized fluorescence plot of every cell’s calcium transient over one cardiac cycle. The network’s activation timing (tact) is visualized in 3D based on the time-point of 10% calcium transient amplitude in every individual cell (right, same color scale). (c’’) Normalized fluorescence plot of all calcium transients, aligned in time based on the timing of deviation from minimal fluorescence intensity (3D network, same color scale). (d) Biological conduction speed, expressed as cells activated per unit of time, is visualized on the 3D network. (e) The basis vectors of the local coordinate system (tangent – black, normal – grey, and binormal – blue) are shown, moving along the centerline. The initial and final orientation of the moving reference frame is shown in a zoomed version at inflow and outflow sites. Outer curvature regions of atrium and ventricle are highlighted in green. (f) The unrolled cylinder results in a representation of 3D network function in a 2D map. Projections show conduction speed across the entire myocardium; iso-velocity lines (Δv = 50 cells/s) are shown in black. Outer curvature regions in atrium and ventricle are highlighted in green.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) A zebrafish embryo is mounted in agarose inside a fluorinated ethylene propylene (FEP) tube. (B) Section view of the sample holder with mounted zebrafish embryo placed inside the medium-filled sample chamber. The embryo is placed in the field of view of the detection objective and illuminated with a static light sheet from one of two sides. (C) Top view of the high-speed light sheet microscope for in vivo cardiac imaging. The laser module combines a 488 and a 561 nm laser line and sends the beam into the two illumination arms. Both arms generate identical light sheets from two opposite sides. The motor unit positions the sample holder with the mounted zebrafish embryo at the intersection of illumination and detection path. Fluorescence emission is split and recorded with an sCMOS camera running at up to 400 Hz.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) Optical section across the atrium of a zebrafish embryo at 52 hpf expressing GCaMP5G and Arch(D95N) in cardiomyocytes. Both channels are recorded simultaneously. Smaller images: raw data recorded at the lowest (I) and highest (II) fluorescence signal, as indicated in the intensity plots. Note how intensity plots illustrate the known slight delay between intensity maxima of calcium versus voltage traces, and the overall excellent capture by both reporters of presence and temporal dynamics of cell activation. Larger images: results of image I subtracted from image II, presenting the maximum intensity difference (image brightness adjusted independently for better visibility). Plots show mean raw intensities over time measured along the myocardium visible in the images. (b) Laser powers in the field of view (measured at the back pupil of the illumination objective) used for the experiment presented in (a) and their impact on the heart rate (n = 3 zebrafish embryos). Arch(D95N) required 10x more laser power than GCaMP5G, yielded a very low signal with about 20 gray levels dynamic range across one cardiac cycle, and was affected by bleaching. Zebrafish embryos showed increased heart rate when illuminated with the high laser power needed for Arch(D95N) imaging. GCaMP5G showed a dynamic range of about 300 gray levels at an order of magnitude lower laser power, with no signs of visible photobleaching or illumination-induced increase in heart rate.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** Optical sections across the silenced heart of a 2 days post fertilization (dpf) zebrafish embryo expressing GCaMP5G and H2A-mCherry in cardiomyocytes, recorded at 50 to 3200 Hz (exposure times 20 to 0.3 ms) with a constant pixel size of (0.5 µm)2. Raw image data of H2A-mCherry are shown to mark cell positions. Red markers indicate location of peak fluorescence intensities across a single cardiac cycle. Gray areas in 800 Hz and 3200 Hz images indicate the proportion of the field of view that could not be recorded, as the number of lines imaged is the speed-limiting factor on the sCMOS camera. Plots show normalized fluorescence intensity over time, measured in a sub region with GCaMP5G signal. Circles show data points from the measurement at 50 Hz as reference. Higher recording speed results in a better representation of the calcium transient until 400–800 Hz, especially during the initial rise in intensity. At an even higher rate of 3200 Hz, noise deteriorates the signal. Peak intensities could be traced with cellular precision at 400 and 800 Hz, before signal noise reduced precision.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (a) The centerline is traced in 3D from inflow (blue) to outflow (red), providing the base for a canonical ordering of the cells. Color code indicates position of cell along midline. (b) Populations of cells with different rise times can be distinguished close to the inflow tract, in the atrium and in the ventricle (indicated by different linear fits), with a pronounced discontinuity in the atrio-ventricular canal (AVC). Color code indicates position of cell along midline. (c) Distribution of biological conduction speeds across the heart, from inflow (blue circle) to outflow (red disk), mean and standard deviation. The inset shows the mean conduction speed for three different hearts at 52 hpf.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** (a) Cell positions are indicated by points at the optically identified location of their nucleus in 3D. Potential neighbors for each cell are identified by taking nearest neighbors with respect to their Euclidean distance in 3D. A sample cell is highlighted in blue and the respective nearest neighbors by large gray dots. (b) The centroids are locally projected into a 2D plane and the Delaunay triangulation (gray and blue lines) is computed to extract the topological connectivity between cells. Edges connecting the reference cell with its neighbors in the 2D projection are highlighted in blue. (c) The connections between the reference cell and its neighbors (blue) are projected back into the original 3D space. Iterating this procedure for all cells yields the final topology (gray edges).

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** (a) Biophysical conduction speed, expressed in μm/ms, is visualized on the 3D network. (b) Visualization of biological conduction speed, expressed as cells activated per unit of time (ms) on the same topology as (a). (c, d) Projection show biophysical (c) and biological (d) conduction speed across the entire myocardium. Same color code as in (a, b). (e, f) Descriptive statistics of conduction speeds in (manually defined) regions corresponding to atrial (blue), AVC (gray), and ventricular part (orange) of myocardium for biophysical (e) and biological (f) conduction speed. (g) Scatterplot showing chamber-specific differences in correlation of biological (x-axis) vs. biophysical (y-axis) conduction speed for atrial (blue), AVC (gray) and ventricular (orange) cells.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp7-v1.jpg)

**Figure 1—figure supplement 7.:** (a, b) Pacemaker cells (shown as colored disks), are located in a ring-like region at the atrial inflow region, shown in front (a) and bottom view (b).

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp8-v1.jpg)

**Figure 1—figure supplement 8.:** Maximum intensity projections of point-scanning confocal and two-photon microscopy z-stacks recorded from a transgenic zebrafish embryo expressing myl7:H2A-mCherry and myl7:lck-EGFP in the myocardium. Scale bars: 50 µm. (a) Positions of myocardial nuclei (myl7:H2A-mCherry) across the heart. (b) Myocardial cell membranes (myl7:lck-EGFP). (c) Color overlay of cell membranes (cyan) and nuclei (red). (c1-3) Detailed view (rotated by −15 degrees about x–axis) of the cell morphologies in inflow, inner curvature and outer curvature regions of the atrium, as indicated in panel (c).

![Figure 1—figure supplement 9.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig1-figsupp9-v1.jpg)

**Figure 1—figure supplement 9.:** Global distribution of cellular activation times shown as 2D projections, illustrate planar activation in spite of increasingly complex chamber morphology and heterogeneity in individual cell properties. Isochronal lines shown in black (Δt = 20 ms).

![Video 1.](https://cdn.elifesciences.org/articles/28307/elife-28307-video1.mp4.jpg)

**Video 1.:** Fluorescence signal recorded at 400 Hz at three different depths (50, 90 and 140 μm along the optical axis) in the heart of a living Tg(myl7:GCaMP5G) zebrafish at 52 hpf using the described imaging setup.

![Video 2.](https://cdn.elifesciences.org/articles/28307/elife-28307-video2.mp4.jpg)

**Video 2.:** Raw data from Video 1 after completed post-acquisition synchronization.

![Video 3.](https://cdn.elifesciences.org/articles/28307/elife-28307-video3.mp4.jpg)

**Video 3.:** (1) 4D reconstruction of calcium activation from the synchronized planar movies recorded in the heart of a living Tg(myl7:GCaMP5G) zebrafish embryo at 52 hpf. The number of slices used in the reconstruction is indicated by n. Raw GCaMP5G signal is shown in orange. Time is indicated in ms. (2) Cell detection: The raw fluorescence signal of myl7:H2A-mCherry is overlaid with the centroids of detected nuclei. (3) Calcium mapping: The raw myl7:GCaMP5G signal is shown. The dots indicate the extracted cellular positions. (4) Cell-specific transients: The normalized GCaMP5G transients are shown for two sample cells (one atrial and one ventricular cell).

To map cellular activation timings onto a 3D structural representation of the heart, we identified every single cell’s activity (Figure 1c’) and quantified dynamic characteristics of all cardiac myocytes across space and time. The distribution of calcium transient rise times (from 10% to 90% of calcium transient peak amplitude) revealed the emergence of distinct upstroke characteristics in different locations within the 3D network (by 52 hpf). Rise times were shortest for atrial muscle cells, intermediate in the atrio-ventricular canal (AVC), and longest for ventricular cardiomyoctes (Figure 1c’’), in keeping with higher vertebrates where atrial myocyte contraction is faster than that of ventricular cells (Brandenburg et al., 2016).

To get a more quantitative understanding of the 3D distribution of activity patterns, a canonical description of cell locations was needed. We traced and parameterized the myocardium’s centerline (Figure 1—figure supplement 4a, Materials and methods), along which we assigned a unique position to each cell between inflow and outflow. We identified a positive correlation between rise time and position of cells along the midline, with a clear discontinuity at the AVC (Figure 1—figure supplement 4b), illustrating emergence of chamber-specific patterns of individual cell activation properties across the heart.

Next, we studied the spatial patterns of sequential cell activation, as a read-out for the speed of electrical conduction across the heart. While cardiac activation in the early linear heart tube is slow and near-uniform, the chambered heart shows areas of elevated conduction velocity (Dehaan, 1961; de Jong et al., 1992; Moorman et al., 1998; Chi et al., 2008; Panáková et al., 2010). Common imaging-based methods for determining cell conduction speed tend to deliver only a metric, or ‘biophysical speed’ of conduction (distance over time). To reflect biological progression of activation between cells (of potentially different or – in contracting tissue – dynamically changing size), we assessed local cell topology across the entire heart (Figure 1d, Figure 1—figure supplement 5, Materials and methods) to also calculate the ‘biological speed’ (number of activated cells over time) of conduction (Video 4). Our analysis revealed that biophysical and biological conduction velocities show differences between and within anatomical regions of the heart (Figure 1—figure supplement 6). Either descriptor identifies particularly slow conduction between the most proximal atrial cells and between the cells of the AVC, while faster conduction is seen among working myocardial cells of the atrium and ventricle. In the atrium, there is a bias towards higher biophysical speeds, due to larger cell dimensions (Figure 1d, Figure 1—figure supplement 4c).

![Video 4.](https://cdn.elifesciences.org/articles/28307/elife-28307-video4.mp4.jpg)

**Video 4.:** (1) Activation timing: Cell positions are indicated by gray dots. Activated cells are highlighted in yellow. Time is shown in ms. (2) Network reconstruction: Estimated local topology is shown as gray edges connecting neighboring cells. (3) Activation across network: Activated cells in the network are highlighted in yellow. (4) Cell–cell conduction speed: The average conduction speed is shown for each cell after activation of its neighbors in the network. Color code indicates conduction speed (red - high, blue - low).

The activation sequence in the pacemaker region is of particular importance to heart physiology and function, yet individual cells that give rise to earliest activation were difficult to identify with previous methods (Van Mierop, 1967; Arrenberg et al., 2010; Christoffels et al., 2010; Tessadori et al., 2012). We found that, at 52 hpf, less than 10 cells per heart serve as activation origins. They are located in the sinus venosus at the heart’s inflow side, which is a homologue of the primary cardiac pacemaker region in adult heart (Poon and Brand, 2013). Our data further show that the ring-like arrangement of pacemaker cells (Figure 1—figure supplement 7), together with a preferential orientation of myocardial cells in that region perpendicular to the inflow-outflow direction (Auman et al., 2007) (Figure 1—figure supplement 8), generates the initial planar ‘ring-like’ activation front that propagates evenly into the atrium.

To visualize the 3D conduction pattern, the heart can be represented as a curved cylinder with varying diameter and s-shaped deformations in the coronal and in the sagittal plane. We used the position along the midline (τ) and the local Frenet-Serret frame as intrinsic coordinates (ɸ, z) (Figure 1e and Video 5, Materials and methods). Interestingly, by following the orientation of this reference system along the midline, we noticed torsion associated with the cardiac looping, which is most pronounced around the AVC (Männer, 2000; Christoffels et al., 2000; Harvey, 2002). Establishing the intrinsic coordinates of the curved cylinder allows straightening and untwisting by implicitly removing the morphological torsion. Neglecting the actual distance to the midline and plotting the position along the midline (τ) against the angle (ɸ), we obtained a 2D projection (Figure 1e,f and Video 5, Materials and methods), in which the two outer curvature regions of atrium and ventricle are located side-by-side. A clear asymmetry in conduction speeds between cells at the inner and the outer curvatures was apparent in this representation (Figure 1f). Irrespective of these differences, however, the activation wave travelled smoothly in a ring-like fashion along the heart, as indicated by the isochronal lines in the cylindrical projection (Figure 1—figure supplement 9).

![Video 5.](https://cdn.elifesciences.org/articles/28307/elife-28307-video5.mp4.jpg)

**Video 5.:** (1) Tracing of midline: The black line traces the center of the myocardium from inflow to outflow. Cellular positions are shown as gray spheres. (2) Moving reference frame: The intrinsic reference frame is shown along the extracted midline. The three axes represent the tangent (black), normal (gray), and binormal (blue) vectors. The trace of the binormal vector is shown as blue band behind the moving trihedron. (3) Untwisting: The heart is successively untwisted by reducing the torsion of the midline to 0. The gray lines indicate traces of cells during this process. (4) Straightening: The heart is straightened by reducing the remaining curvature of the midline to 0. (5) Projection to cylinder. Each cell is projected to the same radial distance from the straightened midline resulting in a cylindrical reference system. (6) Unrolling: The cylinder is unfolded into the 2D plane, resulting in the 2D plots used in the main text. Color code in the final frame indicates biological conduction speed.

In order to document how heterogeneity in cardiac function arises during cardiac looping, we extended our 3D optical mapping towards earlier developmental stages. During the crucial period between 36 and 52 hpf, ventricular cell number increased by about 45%, the initial heart tube developed into a two-chambered organ, the midline of the heart became increasingly curved and twisted (Figure 2—figure supplement 1), and the activation frequency increased – all signs of organ maturation. In spite of a net increase in cell numbers, the time required for activation to propagate from inflow to outflow decreased. A progressive crowding of calcium transient activation dynamics indicated maturation of cells, with two groups differentiating from the early more homogeneous pattern: working cardiomyocytes in atrium and ventricle (Figure 2a–f). At 36 hpf, activation propagated evenly across the myocardium, compatible with peristalsis. Subsequently, calcium dynamics became increasingly structured. By 52 hpf, propagation of activation was fast across atrium and ventricle, while it remained slow in the AVC (Figure 2—figure supplement 2a). With organ maturation during these 16 hr, cells in the ventricular part of the network showed longer calcium transient rise time (Figure 2—figure supplement 2b) but faster inter-cellular spread of activation (Figure 2g–l, Figure 2—figure supplement 2c). Conduction also changed within chambers, such as along the outer curvature in the atrium. Increasing deformation and twisting of the cardiac tissue was associated with changes in cell shape (cf. Figure 2d–f) and in conduction (Figure 2—figure supplement 3).

![Figure 2.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig2-v1.jpg)

**Figure 2.:** (a–c) Normalized calcium transients of all cells are shown at three different time-points: (a) 36, (b) 44, and (c) 52 hpf. The shortening of black arrows indicates the decrease in time between earliest and latest activation of cells along the whole heart. The gradual formation of atrial (1) and ventricular (2) populations with increasingly different calcium transients is highlighted by the dashed lines at 52 hpf. The color of each transient indicates its activation time (all three plots use the same color scale). (d–f) Changes in cardiac and cellular morphology at each developmental time point. Estimated cell shapes are visualized as scaled ellipsoids. The color of each ellipsoid indicates activation time (relative to the first-activated cell); color code as in (a–c). Two main populations of cells corresponding to highlighted clusters in (c) are indicated by numbers. (g–i) 3D pattern of biological conduction speeds across the heart. The formation of outer curvature clusters of cells over time is highlighted by arrows. (j–l) Development of conduction speeds across the myocardium, shown as 2D projections for the three time points. The color code indicates conduction speed. Isovelocity lines are shown in black (Δv = 50 cells/s). Corresponding outer curve cell populations are highlighted by arrows.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (a) One and the same developing heart, imaged at three different time-points (36 (a), 44 (b), and 52 hpf (c), scale bar 50 μm. The fitted centerline visualizes the re-shaping of the myocardium during the ongoing looping/twisting process in early cardiac development. Local coordinate systems are shown along the midline (tangent – black, normal – grey, binormal – color), the twisting point is highlighted by an arrow. Total and chamber-specific cell numbers are indicated for each stage of development (A - atrial cells, V - ventricular cells).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (a) The distribution of activation times is shown for three time points: 36, 44 and 52 hpf. Dots indicate individual cell activation times. Smooth regression profiles are depicted as solid lines and show faster activation with progressive organogenesis. (b) The distribution of rise times during development. The probability density function of each developmental stage is shown by a smooth kernel density. The ordinate axis shows cell numbers and illustrates progressive emergence of cell sub-populations with different calcium transient properties. (c) The distribution of each cell’s conduction speed along the midline is shown as dots. Solid lines indicate smooth regression profiles for each stage. All hearts were normalized to a standard length, showing how speed of biological conduction in working myocardium rises by comparison with early developmental stages, whereas AVC conduction velocity is unchanged.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/28307/elife-28307-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Cell shapes in the atrium are represented by scaled ellipsoids for the same heart at 36 hpf (a), 44 hpf (b), and 52 hpf (c). Ventricular cells are shown with reduced opacity. (d, e, f) The same cells as in (a, b, c) with additional color code indicating cell size. Smaller cells are shown in blue, larger cells in red, highlighting the increase in cell size, in particular along the larger curvature of the atrium. Changes in cell size shown as 2D projections for 36 (g), 44 (h), and 52 hpf (i). The color code indicates normalized cell size as in (d, e, f). Isosize lines shown in black (ΔA = 0.1).

## Discussion

By noninvasively reconstructing the maturation process of the myocardium in its entirety at cellular resolution, our approach offers an integrative perspective on tissue and cell levels simultaneously. We show functional maturation in line with structural patterning of the heart muscle during development: starting from similar initial states, functionally distinct characteristics of calcium transients and conduction properties develop with a highly reproducible pattern relative to the cell locations (cf. Figure 1—figure supplement 8). Myocardial cells in the two chambers remodel and specialize into functional tissue of working atrial and ventricular cardiomyocytes, while cells in the pacemaker and AVC regions continue to resemble the earlier phenotype from the tubular stage.

We demonstrate that myocardial activity can be recorded and analyzed with cellular detail across the entire embryonic heart. Future technological advancements can extend the scope of our approach: First, genetically expressed voltage reporters with improved dynamic range may provide a direct readout of myocardial electrical activity. Second, cameras with higher speed and sensitivity would enhance the recording frequency of rapid volume scanning, needed to explore aberrant myocardial activation during arrhythmias. Third, the integration of an algorithm capable of tracking cells in 3D during cardiac contractions would allow investigations in fully functional hearts. Fourth, the addition of optically gated actuators, such as light-activated ion channels or photo-pharmacological probes, would enable contact-free stimulation to probe the roles of individual cells or groups of cells in pacemaking, conduction, and arrhythmogenesis.

Our work further highlights the value of the zebrafish as a vertebrate model system for in vivo cardiology, especially when combined with high-speed light sheet microscopy and suitable data analysis pipelines. It opens the way to systematic, scale-bridging, in vivo studies of organogenesis by facilitating cell-accurate measurements across entire organs.

## Materials and methods

### Fish husbandry and lines

Zebrafish (Danio rerio) were kept at 28.5°C and handled according to established protocols (Nusslein-Volhard and Dahm, 2002) and in accordance with EU directive 2011/63/EU as well as the German Animal Welfare Act. Transgenic zebrafish lines Tg(myl7:GCaMP5G-Arch(D95N)) (Hou et al., 2014), Tg(myl7:H2A-mCherry) (Schumacher et al., 2013) and Tg(myl7:lck-EGFP)md71 were used. The lck sequence was PCR amplified from pN1-Lck-GCaMP3 (Addgene, #26974) with In-Fusion primers 5’-GCAAAAGATCTGCCACCATGGGCTGTGGCTGC-3’ (forward) and 5’-GCAAAGGGCCCCGAGATCCTTATCGTCATCGT-3’ (reverse) designed with http://bioinfo.clontech.com/infusion/convertPcrPrimersInit.do and cloned into pEGFP-N1 (Clontech, #6085–1). PCR product generated from attB-flanked BP primers 5’-GGGGACAAGTTTGTACAAAAAAGCAGGCTGGATGGGCTGTGGCTGCAGCTCAAACC-3’ (forward) and 5’-GGGGACCACTTTGTACAAGAAAGCTGGGTCTTACTTGTACAGCTCGTCCATGCCGAG-3’ (reverse) was BP Clonase II cloned into Gateway pDONR221 (ThermoFisher Scientific, #12536017) to generate the middle entry clone that was further assembled with p5E_myl7, p3E_SV40polyA (Tol2kit #302), and pDEST.Cryst.YFP76 (Mosimann et al., 2015) into Tol2 transgene plasmid using MultiSite Gateway assembly. See supplementary files for detailed digital plasmid maps of these vectors. To generate Tg(myl7:lck-EGFP)md71 Tol2-mediated zebrafish transgenesis was performed by injecting 25 ng/ml transgene plasmid together with 25 ng/ml capped Tol2 transposase mRNA, followed by subsequent screening of positive F0 founders. During the 1 cell stage, embryos were injected with morpholinos against tnnt2a to uncouple electrical and mechanical activity (Sehnert et al., 2002).

### Sample preparation for light sheet microscopy

Before imaging, fluorescent embryos were selected for absence of cardiac malformations and contractions, using an Olympus stereomicroscope equipped with an LED for transmitted light microscopy and a metal-halide light source and filter sets that match the excitation and emission spectra of GCaMP5G and mCherry for fluorescence excitation. Embryos were mounted in either 0.1 or 1.5% low gelling temperature agarose (Sigma A9414) inside cleaned polymer tubes (FEP tubing, inner/outer diameter 0.8/1.6 mm, BOLA S1815-04).

### Light sheet microscopy

We built a light sheet microscope for in vivo cardiac imaging in zebrafish embryos, based on a previously published design (Mickoleit et al., 2014). Imaging was performed in live zebrafish embryos between 36 and 52 hr post-fertilization (hpf) at a temperature of 24°C. Heart rate at this temperature is 2 Hz, about 0.5 Hz lower than at the temperature recommended for breeding of 28.5°C (Baker et al., 1997; Kopp et al., 2005). Embryos were kept in a custom imaging chamber filled with E3 fish medium and illuminated with a static light sheet generated from Coherent Sapphire LP lasers (488 and 561 nm) using a cylindrical lens and a Zeiss 10x/0.2 air illumination objective. Laser power was kept at or below 2 mW in the field of view (measured at the back aperture of the illumination objective) to exclude thermal effects on heart rate (an increase in heart rate was detected at laser powers of 5 mW and above). Fluorescence was collected and recorded using a Zeiss W Plan-Apochromat 20x/1.0 objective, a Zeiss 0.63x camera adapter, a Hamamatsu W-View image splitter and a Hamamatsu Flash 4.0 v2 sCMOS camera. Embryos were held in place by a Zeiss Lightsheet Z.1 sample holder and oriented using motorized translation and rotation stages (Physik Instrumente GmbH, Karlsruhe, Germany). For imaging of GCaMP5G, a z-stack of movies covering the entire heart was recorded by moving each embryo through the light sheet (488 nm excitation, band-pass 525/50 nm emission filter, 2.5 ms exposure time = 400 Hz, 600 frames = 1.5 s/movie, 1 µm z-steps). To ensure an efficient recording and the best possible synchronization (see below), the embryo was rotated by about 30 degrees, such that both atrium and ventricle were visible in the imaging plane for the majority of the z-stack. For imaging of H2A-mCherry, a matching z-stack was recorded immediately afterwards (561 nm excitation, long-pass 565 nm emission filter, 20 ms exposure time = 50 Hz, 1 µm z-steps). Image acquisition was controlled by a custom program written in LabView (National Instruments). Images were streamed onto a RAID-0 array of four 512 GB solid-state drives.

### Data analysis

#### Synchronization of z-stacks of movies

The recorded z-stacks of movies were synchronized in time starting at the middle plane and iterating in two independent threads towards first and last plane, respectively. A full cardiac cycle was selected randomly in the middle plane, and Pearson’s correlation coefficients were calculated for every cycle in the adjacent plane. The cycle with the highest correlation was selected as the best fit. As demonstrated before, the presence of both atrial and ventricular myocardium in the majority of planes minimized the risk of false synchronization (Mickoleit et al., 2014).

#### Visualization of synchronized movies

The synchronized movies were visualized (Video 2) using custom scripts (Scherf, 2017) for Mathematica 11.1 (Wolfram Research Inc., Champaign, Illinois). The raw calcium signal stacks for each time point were normalized and visualized in 3D using direct volume rendering of the resulting intensities. The 3D volume visualizations were then projected to 2D using a standard perspective transform from a defined viewpoint. Animations were created by a smooth interpolation between different viewpoints.

#### Segmentation of cell nuclei

Volumes of cell nuclei were extracted from the H2A channel of the raw image volumes using grayscale blob detection (Lindeberg, 1998). To resolve potential errors in automated processing (false detection, missing cells), cell positions were manually curated using an in-house software (Scherf, 2017) facilitating evaluation, addition and deletion of nuclear positions in the 3D data sets. Curated nuclei positions were used for further processing.

#### Signal extraction and processing

From the measured nuclear positions, a reference volume was extracted for each cell by computing the Euclidean distance transform and thresholding the distance field around each centroid (nucleus) at a radius of 5 voxels. For each thus identified ‘cell volume’, a calcium transient was extracted by averaging the signal over all voxel within the reference volume at each time step. The resulting transients were processed using a low pass filter (with a cutoff frequency of 5 Hz) to reduce noise, and finally normalized to the range [0,1].

#### Extraction of midline

The heart’s midline was manually traced using an in-house software. The user could draw the midline in two different 2D projections (front and top view) by placing discrete points that were connected across the different projections. The final midline was then obtained by a 4th order B-Spline interpolation to facilitate subsequent computation of intrinsic geometric characteristics such as curvature and torsion.

#### Frenet-Serret frame

To describe each cell’s position within the myocardium, we established a curved cylindrical coordinate system. The position along the midline (τ) was calculated for each cell by finding the closest point on the midline for the respective centroid. The moving coordinate system along the midline was then computed using the Frenet-Serret frame (Kreyszig, 1959), calculating the local tangent ($T→$), normal ($N→$), and binormal ($B→$) vectors:

$$
T→(t)=\frac{r→(\tau)}{|r→(\tau)|}
$$



$$
N→(t)=\frac{T'→(\tau)}{|T→^{'}\tau|}
$$



$$
B→(t)=T→(\tau)\timesN→(\tau)
$$

with $r→(\tau)\inR^{3}$ being the actual 3D position vector on the midline parameterized by τ. Then each cell’s position was mapped to this new coordinate system as (τ, ɸ, z), where τ was the position along the midline (normalized to 0 and 1 after reparameterization), ɸ the angle with respect to the local binormal vector (in the local N-B plane), and z the radial distance of the centroid from the midline.

#### Cylindrical 2D map projections

To map cell positions from 3D to 2D, we projected the curved cylindrical coordinates to the first two components $(\tau,ɸ,z)→(\tau,ɸ),$discarding the radial distance from the midline. This projection facilitates global visualization of the myocardium, irrespective of its looping stage, in a single flat projection by cutting the cylinder at $ɸ=\pm\pi$ and plotting the coordinates in a rectangular coordinate system in the range $\tau\in[0,1$] and $ɸ\in[-\pi,\pi$], respectively.

#### Topology reconstruction

The myocardial topology (local connectivity of cells) was estimated by projecting the 3D centroid positions of each cell and its nearest neighbors locally into the 2D Euclidean plane using Singular Value Decomposition (Bronshtein, 2007) of the 3D centroid positions. In each local 2D projection, the cellular connectivity was estimated by computing the 2D Delaunay triangulation (Delaunay, 1934). The estimated edges $e_{ij}$ between cells and the original 3D centroid positions of each cell $v_{i}$ were used to abstractly represent the myocardium as an undirected graph $G=(V,E)$ where $v_{i}\inV,e_{ij}\inE$.

#### Computation of biological conduction speed

As the spread of activation in cardiac tissue is governed by cell activation and time delay at gap junctions between cells, we used the graph representation to estimate the average local cell-to-cell conduction speed $cs_{i}$in terms of (dimensionless) links traversed per unit of time. Thus, at each cell’s position the (harmonic) mean of the number of traversed edges per time was computed over all paths from the cell to its neighbors:

$cs_{i}=n(\sumj\frac{dt(i,j)}{e(i,j)})^{-1}$ for all neighbors j of cell i with dt(i,j) being the temporal difference in activation time and e(i,j) the number of edges between cell i and cell j.

#### Computation of metric conduction speed

For comparison, the metric conduction speed at each cell’s position, the (harmonic) mean of the distance travelled by the activation per time, were computed over all paths from the cell to its neighbors:

$cs_{i}=n(\sum_{j}^{}\frac{dt(i,j)}{d(i,j)})^{-1}$ for all neighbors j of cell i with dt(i,j) being the temporal difference in activation time and d(i,j) the 3D Euclidean distance (along the ‘surface’ defined by the neighborhood graph) between cell i and cell j.

#### Estimation of cell size and shape

We further used the graph representation to extract an estimate of a cell’s shape by computing the principal components of the distribution of neighboring nuclei around each cell. Thus, each cell is represented as an ellipsoidal region defined by the eigenvectors $υ_{i}$ and eigenvalues $\lambda_{i}$ of the local principal value decomposition. Cell shape was then approximated as the fractional anisotropy of each ellipsoidal region:

$\sqrt{\frac{3}{2}}\frac{\sqrt{(\lambda_{1}-\lambda^)^{2}+(\lambda_{2}-\lambda^)^{2}+(\lambda_{3}-\lambda^)^{2}}}{\sqrt{\lambda_{1}^{2}+\lambda_{2}^{2}+\lambda_{3}^{2}}}$ , with $\lambda^$ being the average eigenvalue.

Cell size was approximated as the volume $\frac{4}{3}\pi\lambda_{1}\lambda_{2}\lambda_{3}$ of each ellipsoid.

#### Pacemaker identification

Pacemaker cells were defined as the cells that showed earliest activation (activation time shorter than the 0.05-quantile of overall distribution of activation times) and that conducted slowly (conduction speed slower than the median conduction speed within the cell population). All cells falling within this category were labeled as potential pacemaker cells.

### Sample preparation for confocal and two-photon microscopy

Transgenic zebrafish embryos expressing myl7:H2A-mCherry and myl7:lck-eGFP in the myocardium were screened for absence of cardiac malformations and contractions using an Olympus stereomicroscope at 2 dpf. Selected embryos were mounted in 1.5% low-melting point agarose (Sigma A9414) inside glass capillaries using plungers (Brand 20 μl Transferpettor caps and piston rod). After a few minutes, mounted embryos were carefully transferred onto a custom 3D-printed sample holder with their heart facing up. Once positioned, they were fixed in place using drops of agarose at both ends of the agarose column. The sample holder was placed in a 52 mm plastic dish and covered with E3 fish medium.

### Confocal and two-photon microscopy

Confocal and two-photon microscopy was performed with an upright Zeiss LSM 780 NLO equipped with a Zeiss W Plan-Apochromat 20x/1.0 objective lens, a Coherent Chameleon multiphoton laser set to 920 nm, a Coherent HeNe 594 nm laser and gallium arsenide phosphide (GaAsP) detectors. The fluorescence reporter myl7:H2A-mCherry was recorded using single-photon excitation at 594 nm, a descanned GaAsP detector and a confocal pinhole set to one airy unit. Two-photon excitation at 920 nm and a non-descanned GaAsP detector were used for the fluorescence reporter myl7:lck-eGFP. The pixel size was 0.148 µm2 and z-stacks were recorded with a 1 µm step size. The total acquisition time of one z-stack was about 60 min.
