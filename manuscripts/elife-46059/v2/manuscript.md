# Nanoresolution real-time 3D orbital tracking for studying mitochondrial trafficking in vertebrate axons in vivo

## Authors

- Fabian Wehnekamp<sup>1</sup>
- Gabriela Plucińska<sup>2</sup>
- Rachel Thong<sup>2</sup>
- Thomas Misgeld<sup>2</sup> ([ORCID: 0000-0001-9875-6794](https://orcid.org/0000-0001-9875-6794)) †
- Don C Lamb<sup>1</sup> ([ORCID: 0000-0002-0232-1903](https://orcid.org/0000-0002-0232-1903)) †

### Affiliations

1. Department of Chemistry Center for Nano Science (CENS), Center for Integrated Protein Science (CIPSM) and Nanosystems Initiative München (NIM), Ludwig Maximilians-Universität München Munich Germany
2. Munich Cluster for Systems Neurology (SNergy) Center for Integrated Protein Science (CIPSM), German Center for Neurodegenerative Diseases (DZNE), Institute of Neuronal Cell Biology, Technische Universität München Munich Germany

† Corresponding author

## Abstract

We present the development and in vivo application of a feedback-based tracking microscope to follow individual mitochondria in sensory neurons of zebrafish larvae with nanometer precision and millisecond temporal resolution. By combining various technical improvements, we tracked individual mitochondria with unprecedented spatiotemporal resolution over distances of >100 µm. Using these nanoscopic trajectory data, we discriminated five motional states: a fast and a slow directional motion state in both the anterograde and retrograde directions and a stationary state. The transition pattern revealed that, after a pause, mitochondria predominantly persist in the original direction of travel, while transient changes of direction often exhibited longer pauses. Moreover, mitochondria in the vicinity of a second, stationary mitochondria displayed an increased probability to pause. The capability of following and optically manipulating a single organelle with high spatiotemporal resolution in a living organism offers a new approach to elucidating their function in its complete physiological context.

## Introduction

Neurons critically depend on proper positioning of organelles along their axons. While the basic molecular players of the axonal transport machinery are well established (Hirokawa et al., 2010), the higher order levels of regulation that govern the overall ‘life cycle’ of axonal organelles are poorly understood (Misgeld and Schwarz, 2017; Plucińska and Misgeld, 2016). One example of this dearth of understanding is provided by mitochondria where their proper distribution and turn-over are of seminal importance for neuronal homeostasis (Chang and Reynolds, 2006; Sheng and Cai, 2012; MacAskill and Kittler, 2010; Saxton and Hollenbeck, 2012). Despite the well-established roles of specific kinesin and dynein motors in the long-distance transport of axonal mitochondria and some recent progress on the mechanisms of their local anchorage and degradation (MacAskill and Kittler, 2010; Saxton and Hollenbeck, 2012; Sheng, 2014; Ashrafi and Schwarz, 2013), many details regarding how the distribution of how mitochondria are established, maintained and regulated – especially in vivo – remain elusive. For example, the regulatory interplay of molecular motors that propel and brake mitochondria and give rise to their characteristic ‘saltatory’ movement (Morris and Hollenbeck, 1993) and additional ‘non-canonical’ movement behaviors (Chang and Reynolds, 2006; Morris and Hollenbeck, 1993; Ligon and Steward, 2000) is not well understood. Our understanding of the origin, travel range and final destination of transported mitochondria is only emerging (Misgeld et al., 2007; O'Toole et al., 2008), and how the local cellular microenvironment, such as activity or calcium levels, influences mitochondrial motility in axons with a realistic in vivo geometry and surrounding is only now starting to be explored (Faits et al., 2016; Sajic et al., 2013; Ohno et al., 2011; Smit-Rigter et al., 2016; Lewis et al., 2016).

In many respects, the gap in understanding between the well-established molecular underpinnings of mitochondrial transport gleaned from biophysical studies in vitro and the bigger picture of this organelle’s homeostasis in neurons in vivo can be attributed to a lack of techniques that can span the different spatial domains involved: Motors step on the scale of nanometers but propel organelles on the scale of many hundreds of micrometers. Here, we present an approach based on 3D single particle tracking (3D SPT) that is suitable to bridge this chasm and demonstrate the in vivo applicability of this tool to the zebrafish model of axonal transport (O'Donnell et al., 2013; Plucińska et al., 2012). This new approach will be instrumental in linking the biophysical understanding of single organelle dynamics to physiological and pathological neuronal changes in vivo.

In the past few years, a number of 3D SPT methods have been developed. They rely on different approaches like altering the shape of the point spread function (Spille et al., 2015; Kao and Verkman, 1994; Shechtman et al., 2015) or ‘lock-in’ feedback loops that re-center the laser focus onto the tracked particle (Welsher and Yang, 2014; Dupont et al., 2013; McHale et al., 2007; Perillo et al., 2015; Juette and Bewersdorf, 2010; Levi et al., 2005). These approaches have established 3D SPT as a powerful tool to study the dynamics of subcellular structures. However, these techniques have largely remained restricted to cells in dissociated culture and other reductionist models due to technical limitations. To successfully track individual mitochondria inside an intact organism, such as a live zebrafish larva, several points have to be considered. First, due to fusion and fission events, the shape of each mitochondrion is changing during the transport along the neuron and thus the tracking technique must be resilient to such shape changes. Second, transport in axons, even in a small organism like a fish larva, potentially extends over distances of hundreds of micrometers. Thus, the available tracking range has to be expanded well beyond a single field of view. Third, to achieve prolonged trajectories of single moving mitochondria against a dense back-drop of resting organelles, the fluorescence of each mitochondrion has to be individually controlled. Finally, the recorded trajectories have to be contextualized by vistas of the cellular environment in which the organelle traveled.

Here, we present a 3D SPT method based on real-time 3D orbital tracking that is able to overcome these challenges: The method combines high spatial (XY:<5 nm Z:<30 nm) and temporal resolution (100 Hz) with simultaneous wide-field imaging and local photo-activation. A feedback loop recurrently re-centers the specimen on top of the microscope once a tracked particle approaches the edge of the field of view. In combination with previously developed genetic tools (Plucińska et al., 2012), we are capable of tracking single neuronal mitochondria in vivo over distances of more than 100 µm. The exquisite spatiotemporal resolution of the microscope system allowed us to discriminate not only the canonical fast components during active motion, but also revealed a previously undetected motional state in both the antero- and retrograde directions. This state has a slower velocity and was engaged when mitochondria undergo temporary directional changes. A detailed examination of transitions between motion states and pause durations showed a complex pattern governing such transient changes in mitochondrial motility. The combination of trajectory and ‘environmental’ data (i.e. wide-field images of the region surrounding the tracked particle) allowed us to analyze the influence of other mitochondria present in the axon and showed that stationary mitochondria can act as roadblocks that initiate the slower motional state in passing organelles, a potential mechanism for overcoming such physiological obstacles.

## Results

### In vivo 3D orbital tracking in zebrafish

To track organelles with nanometer precision and millisecond temporal resolution in zebrafish larvae, we further developed the 3D orbital SPT microscope described previously (Dupont et al., 2013; Katayama et al., 2009) (Figure 1) to overcome four essential limitations for 3D in vivo SPT applications: (I) We obtained precise hardware synchronization using a field programable gate array as well as sub millisecond timing of the tracking feedback loop algorithm by executing the algorithm on a real-time operating system. (II) We increased the lateral tracking range to centimeters by amending the 3D orbital tracking algorithm with a long-range tracking feature that automatically re-centers the sample stage before the particle exits the field-of-view. (III) We incorporated multiple laser lines into the orbit light path – including a 405 nm laser for controlled photo-activation, which allows single organelle tracking in a densely labeled background. (IV) To decrease photobleaching and phototoxicity, we implemented dark orbits, where only a subset of orbits is illuminated by the excitation laser, which significantly extends experiment duration in exchange for a moderate decrease in temporal resolution. This combination of technical advances makes it possible to track single organelles in a living organism in 3D with nanometer scale spatial resolution, millisecond scale temporal resolution and over lateral distances of centimeters.

![Figure 1.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig1-v2.jpg)

**Figure 1.:** (a) Light microscopy transmission image of the zebrafish and a zoom in on the tail with a typical Rohon-Beard neuron labeled by a membrane-targeted fluorescent protein (shown in yellow). The typical tracking area (orange box), soma (orange arrow) and notochord (orange asterisks) are indicated to provide a contextual overview (scale bar, 200 μm). (b) Schematic of the custom-built 3D real-time orbital tracking microscope consisting of a confocal tracking channel and a wide-field channel for simultaneous environmental observation. (c) A confocal reconstruction of a sensory neuron is shown where both the membrane and the individual mitochondria, indicated schematically as red points, are fluorescently labeled (scale bar, 100 µm). The imaging sites in the stem axon are shown in gray with the multiple boxes indicating the re-location of the field of view during long-range tracking. Images of TagRFP (in red)/PA-GFP-labeled (in yellow) axonal mitochondria before (upper image pair) and after (lower image pair) photo-activation of a single mitochondrion are shown (scale bar, 5 µm). (d) Schematic representation of the 3D orbital tracking approach. Different particle locations are indicated through spheres of varying color. Lateral localization is performed by orbiting the laser focus around the particle of interest (top left). The amplitude and peak position of the intensity orbit depends on the position of the particle in relation to the center of the orbit (top right). The color of the line represents the signal coming from the object of the corresponding color in the left panels. The axial localization is achieved by using two confocal detection volumes placed equidistant above and below the focal plane (bottom left), so the intensity ratio between the two planes is proportional to the axial position of the particle (bottom right). (e) A trajectory of an anterograde moving mitochondrion (100 Hz, 20,000 data points). Zoom-ins illustrate the actual density of the acquired data points. (f) Autocorrelation carpet (top) of the angle between consecutive orbits. The black box indicates the lag time τ region averaged for the plot shown in the middle panel. Dashed line marks the threshold that was used to separate stationary phases (red points in bottom panel) from directed motion (green data points) in the lower plot. The lower plot is the same as shown in the maximum zoom-in in panel e). Galvo: galvanometer mirrors; APD, avalanche photodiode.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) The localization of a stationary particle (190 nm multifluorescent bead, Spherotech) at a countrate of >1600 photons per orbit (i.e. 320 kHz) is shown as a function of time (acquisition rate 200 Hz) for x, y and z in black, dark gray and light gray, respectively. The localization precision, determined from the standard deviation of the position of the stationary particle, was <3 nm laterally and <21 nm axially. (b) The localization precision for a moving particle (with a maximum velocity of 6.2 μm/s). An immobilized particle was moved along a sinusoidal path using a 3-axis piezo stage and the position recorded as a function of time (acquisition rate, 200 Hz) in x, y or z shown in black, dark gray and light gray respectively. A sinusoidal fit was performed (green lines) and the standard deviation of the residuals was used to determine the precision. For a count rate of >1600 photons per orbit (i.e. 320 kHz), a localization precision of <3 nm laterally and 21 nm axially was measured. (c) Count-rate dependent localization precision (average values from stationary and dynamic particles, acquisition rate 200 Hz). The values for x, y and z are shown in black, dark gray and light gray, respectively. (d) Velocity-dependent localization precision for a particle moving along the x, y and z axes. The decreased accuracy of the x axis compared to the y axis at velocities above 5 μm/s is a result of a ~ 0.1 ms delay in updating the position of the particle at the starting point of the new orbit (ϕ = 0°). (e) To measure the in vivo localization precision of the orbital tracking approach, a stationary mitochondrion inside the zebrafish was tracked at a count rate of 500 photons per orbit (i.e. 100 kHz). The trajectory data along the x axis (minor axis of the mitochondria) shows a localization precision of ~21 nm. (f) To determine the dynamic localization precision, the stationary mitochondrion was externally moved along the minor axis using a piezo stage. Similar to the dynamic precision measurement using beads, the resulting trajectory was fit using a sine wave and the standard deviation of the residuals showed a localization precision of 42 nm. The localization precision for moving mitochondria, which are usually smaller than stationary ones, was estimated from the standard deviation of the y orbit displacement, which averages 4.6 nm after removing high frequency noise by smoothing the trajectory data by five points.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (a) Depending on the vicinity of the neuron cell to larger blood vessels, motion due to the heartbeat of the zebrafish larvae could be detected. By subtracting a smoothed trajectory (50 points = 0.5 s) from the raw data, low-frequency components (the underlying axonal structure) are filtered out and a sinusoidal signal in the y component (perpendicular to the direction of motion) of a measured trajectory becomes visible. (b) A frequency analysis of this signal revealed an underlying signal of 2.38 Hz, which corresponds to the heartbeat of a zebrafish embryo of 120–180 bpm (black bars). (c) After surgically isolating the tail of the same larvae used to acquire the trajectory from a), a second trajectory was measured. The sinusoidal signal disappeared from the trajectory b) (gray bars). (d) By subtracting the frequency spectrums from b), the heartbeat contribution to the spatial frequencies can be identified. Although motion due to the heartbeat of the zebrafish larvae can be detected, its impact on the analysis of mitochondrial transport is negligible.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (a) The first effect that could bias the localization precision is the size of the tracked particle. Moving mitochondria are small (~700 nm along the major axis, left) when compared to stationary ones (>1 µm along the major axis, right). The rotation of the point spread function (gray) along the orbit (black) covers a circle with a diameter of ~1 µm and entirely covers small mitochondria. However, larger mitochondria do not fall completely within the orbit of the laser, which can result in no change in fluorescence signal upon movement and thus a bias in localization upon directional changes. The second effect is the shape of the tracked particle. The intensity orbit is converted to the frequency space for further calculation and only the zero and first order Fourier coefficients are used to calculate the location of the particle. Since the shape of the particle is encoded in higher Fourier coefficients, it does not influence the localization precision. (b) To determine if the mitochondria size is influencing localization precision, individual stationary mitochondria were moved externally in a sinusoidal pattern with amplitude 2.5 µm using an xyz piezo stage. The amplitude of sinusoidal motion along the minor axis (orange triangles) could be completely recovered. Motion along the major axis (orange circles) of mitochondria longer than ~1.4 µm showed a significant reduction of the sinusoidal amplitude. For comparison, the size of the minor and major axes of moving mitochondria determined from the wide-field images are shown above the plot in black. Due to the small size of the moving mitochondria, the recorded localization data are unbiased. Mitochondria sizes were determined using the FWHM from a Gaussian fit to the intensity distribution from confocal (stationary mitochondria) and wide-field images (moving mitochondria).

We applied orbital tracking to a previously published zebrafish model (Plucińska et al., 2012). To do so, we co-expressed mitochondrially targeted red fluorescent protein (mitoTagRFP-T) and photo-activatable green fluorescent protein (mitoPAGFP) in sensory (Rohon-Beard) neurons using the Gal4/UAS system (see Materials and methods). At 3 days post fertilization (dpf), we photo-activated a moving mitochondrion in the axon near the soma with a confined xy scan of the 405 nm laser beam (Figure 1a–c), which enabled tracking of the targeted (photo-converted) organelle unambiguously in the GFP channel against the backdrop of the numerous (non-photo-converted) mitochondria visible in the RFP channel. Trajectories of moving mitochondria were derived from recordings of orbit and stage displacements needed to follow the organelle through the axon. A wide-field view of the tracked mitochondria was recorded in parallel. The combined technical improvements to expand tracking range and reduce phototoxicity allowed us to acquire mitochondrial trajectories of >100 µm with ~5 nm precision using a 5 ms orbit (Figure 1d,e,SI, Figure 1—figure supplement 1, Video 1 and 2). Given the extremely high spatiotemporal resolution of the data, different precautions had to be made. For example, stem axons nearby blood vessels exhibited low-amplitude fluctuations perpendicular to mitochondrial movement due to the heartbeat (Figure 1—figure supplement 2). This artifact could be minimized by choice of the recording site. Trajectories that were significantly impacted by blood flow could be easily identified and discarded based on the amplitude and frequency characteristics of the heartbeat. We also verified that the shape of the mitochondria did not impact our tracking precision (Material and methods and Figure 1—figure supplement 3).

![Video 1.](https://cdn.elifesciences.org/articles/46059/elife-46059-video1.mp4.jpg)

**Video 1.:** (Left) Wide-field video showing the anterograde transport of a photo-activated mitochondrion along a single axon. Color-coding of the trailing points indicate different movement states (green – fast anterograde, yellow – slow anterograde, orange – slow retrograde, red – stationary state; scale bar 5 µm). (Top right) Mean photon count rate of both detection channels. Downward spikes indicate long range tracking events where the tracking software is not able to track the particle for ~35–70 ms (axis dependent). The laser intensity was occasionally increased manually to ensure high tracking accuracy. (Bottom right) 3D trajectory of the moving mitochondrion. The field of view of the EMCCD camera is indicated by the gray square box, the threshold for the long-range tracking in black. Gray vertical lines indicate the position of stationary mitochondrion. After 145 s, the tracking algorithm switches to a brighter, stationary mitochondrion.

![Video 2.](https://cdn.elifesciences.org/articles/46059/elife-46059-video2.mp4.jpg)

**Video 2.:** (Left) Wide-field video showing the retrograde transport of a photo-activated mitochondrion along a single axon. Color-coding of the trailing points indicate different movement states (blue – fast retrograde, orange – slow retrograde, yellow – slow anterograde, red – stationary state; scale bar 5 µm). (Top right) Mean photon count rate of both detection channels. Downward spikes indicate long range tracking events where the tracking software is not able to track the particle for ~35–70 ms (axis dependent).

### Two types of motion drive mitochondrial transport

To differentiate between active phases of transport along the axon and stationary phases (pauses), we used an autocorrelation analysis of the angle between two consecutive localizations in the trajectory (Figure 1f). Within a window of 64 data points, the autocorrelation amplitude for active phases approached a value of one, while, in the stationary state, this value dropped below 0.30 (a threshold value generated from randomization of the individual trajectory data, see Materials and methods). The stationary state does not imply that the motors are not intact or that the mitochondria are immobile, only that no net progress is observed in any particular direction over a time window of hundreds of milliseconds. Indeed, from conventional time-lapse imaging experiments, different behaviors of stationary mitochondria are also known (such as a local ‘wiggling’ as opposed to a fully immobile state, Misgeld et al., 2007 – which likely represent different modes or extents of anchorage; Gutnick et al., 2019; however, here we focused on the translocation behavior of mitochondria).

Analysis of the 3D trajectories revealed that antero- and retrograde-directed phases of active movement were composed of two distinct fast and slow movement states, which differed significantly in speed and processivity (Figure 2, Figure 2—figure supplement 1, Table 1). To validate the measured values, we compared the average velocities of motion in the anterograde and retrograde direction with results of a previous study (Plucińska et al., 2012). The obtained values of the 3D Orbital tracking approach are consistent with the previous study when accounting for the difference in time resolution (10 ms versus 500 ms, leading to the inability to properly discriminate between fast and slow components in the previous study) and temperature (25°C here versus 28°C in Plucińska et al., 2012, Table 2). Fast states are responsible for long-distance trafficking of the mitochondria with average velocities of 0.62 µm/s for anterograde motion and 0.72 for retrograde motion. The slow states carry out movements over shorter distances and shorter timescales (Figure 2c–f). The characteristics of the slow movement states (i.e. duration, displacement and velocity) are similar in both directions (Figure 2c). Although the average travel distances and times for the slow movement states are small, the orbit displacement (Figure 2c) and velocity histograms (Figure 2—figure supplement 1a,b) clearly indicate directional motion, which demonstrates a proper separation of these processes from the stationary state.

![Figure 2.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig2-v2.jpg)

**Figure 2.:** (a) Representation of an anterograde (top) and retrograde (bottom) trajectory. Color coding indicates phases of fast motion (green - anterograde; blue - retrograde), slow motion (yellow - anterograde; orange - retrograde) and stationary phases (red). (b) Kymographs of the trajectories shown in panel a. (c–f) Population properties determined from 43 mitochondrial trajectories collected from 16 embryos. (c) Orbit displacement histograms for the anterograde direction (fast: 5.8 ± 5.0 nm, n = 83,272 orbits; slow: 3.4 ± 3.7 nm, n = 27,638), the retrograde direction (fast: −7.1 ± 5.3 nm, n = 61,217; slow: −3.7 ± 4.4 nm, n = 21,984) and the stationary states (0.0 ± 3.9 nm, n = 1,153,949). Dashed lines indicate the center of the Gaussian distributions. (d) Durations of anterograde (fast: 2.5 ± 1.5 s; n = 331 states; slow 0.46 ± 0.11 s; n = 416) and retrograde motion states (fast: 2.6 ± 1.0 s; n = 220; slow 0.45 ± 0.20 s; n = 339). (e) XY displacement during anterograde (fast: 1.5 ± 1.0 µm; n = 331; slow 0.30 ± 0.15 µm; n = 416) and retrograde motion states (fast: 2.1 ± 1.0 µm; n = 220; slow 0.27 ± 0.15 µm; n = 339). (f) Lateral velocity during anterograde (fast: 0.62 ± 0.09 µm/s; n = 331; slow 0.36 ± 0.08 µm/s; n = 416) and retrograde states (fast: 0.76 ± 0.08 µm/s; n = 331; slow 0.42 ± 0.11 µm/s; n = 416). Box plot shows the average, as wells as 25 and 75 percentile; error bars indicate standard deviation. Asterisks indicate significance levels (determined by a two-sided t-test) of *: p<0.01, **: p<0.005 and ***: p<0.001. (Table 1).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a,b) From each region of active transport, an average velocity is determined. The distribution of velocities for the trajectories plotted in Figure 2 is given, which clearly shows two populations. The distribution of transport velocities from a trajectory were fit to two Gaussian functions using a maximum likelihood approach as shown for a) a retrograde and b) an anterograde moving mitochondrion. (c,d) Based on the mean velocities of the maximum likelihood fit, each active phase is assigned to either the fast or slow population (blue – fast retrograde, orange – slow retrograde, green – fast anterograde, yellow – slow anterograde).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Left and right figures: A transition probability diagram is shown for retrograde and anterograde moving mitochondria respectively. The probability of transitions between different movement phases are given in the left and right diagrams (n = 1234 transitions). The distributions of pause duration (middle plots) between transitions involving the fast motion states show mono exponential decay constants of 1.94 s (fast-fast transitions) and 1.97 s (fast-slow transitions). The distribution of pause duration for transitions between slow states show a decay constant of 3.2 s. Directional transitions between the fast and slow states are rare events and no statistical relevant results could be obtained for these types of transitions.

**Table 1.**
 Dynamic states properties of untreated zebrafish embryos.Numerical values and statistics of zebrafish embryos for data shown in Figure 2c–f. Values are gives as the average ±s.d. Significance levels were determined using a two-sided t-test). The left and right cells highlighted by the gray boxes indicate the value pair used to determine the respective p values.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Fast anterograde</th>
      <th>Slow anterograde</th>
      <th>Fast retrograde</th>
      <th>Slow retrograde</th>
      <th>Stationary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Duration</td>
      <td>2.53 ± 1.48 [s]</td>
      <td>0.46 ± 0.11 [s]</td>
      <td>2.62 ± 0.98 [s]</td>
      <td>0.45 ± 0.20 [s]</td>
      <td></td>
    </tr>
    <tr>
      <td>n</td>
      <td>331</td>
      <td>416</td>
      <td>220</td>
      <td>339</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">p</td>
      <td colspan="2">1.7e-3</td>
      <td colspan="2">5.1e-5</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">0.88</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">0.92</td>
      <td></td>
    </tr>
    <tr>
      <td>XY Displacement</td>
      <td>1.47 ± 0.96 [µm]</td>
      <td>0.30 ± 0.15 [µm]</td>
      <td>2.07 ± 0.97 [µm]</td>
      <td>0.27 ± 0.15 [µm]</td>
      <td></td>
    </tr>
    <tr>
      <td>n</td>
      <td>331</td>
      <td>416</td>
      <td>220</td>
      <td>339</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">p</td>
      <td colspan="2">3.9e-3</td>
      <td colspan="2">2.2e-4</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">0.18</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">0.67</td>
      <td></td>
    </tr>
    <tr>
      <td>XY Velocity</td>
      <td>0.62 ± 0.09 [µm/s]</td>
      <td>0.36 ± 0.08 [µm/s]</td>
      <td>0.76 ± 0.08 [µm/s]</td>
      <td>0.42 ± 0.11 [µm/s]</td>
      <td></td>
    </tr>
    <tr>
      <td>n</td>
      <td>331</td>
      <td>416</td>
      <td>220</td>
      <td>339</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">p</td>
      <td colspan="2">2.7e-6</td>
      <td colspan="2">1.0e-6</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">1.6e-3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">0.14</td>
      <td></td>
    </tr>
    <tr>
      <td>X Orbit Displacement</td>
      <td>5.8 ± 5.0 [nm]</td>
      <td>3.4 ± 3.7 [nm]</td>
      <td>−7.1 ± 5.3 [nm]</td>
      <td>−3.7 ± 4.4 [nm]</td>
      <td>0.0 ± 3.9 [nm]</td>
    </tr>
    <tr>
      <td>n</td>
      <td>83272</td>
      <td>27638</td>
      <td>61217</td>
      <td>21984</td>
      <td>1153949</td>
    </tr>
    <tr>
      <td rowspan="4">p</td>
      <td colspan="2">2.8e-5</td>
      <td colspan="2">1.3e-7</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">6.1e-7</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">5.3e-7</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">0.49</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Velocity comparison.Comparison of velocities between the orbital tracking analysis and the wide-field analysis used in a previous study (Plucińska et al., 2012). The comparison between the wide-field analyses at 25°C and 28°C showed a 40% reduction in velocity, which is attributed to the reduced temperature. Due to the low time and spatial resolution, the wide-field analysis can only extract the velocity for a single population. This velocity value represents an average of the fast, slow and short stationary states, due to the inability of the wide-field analysis to reliably discriminate between these states. Values are given as the average ±s.d.


<table>
  <thead>
    <tr>
      <th colspan="4">Lateral velocity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Population</td>
      <td>Tracking analysis 25°C</td>
      <td>Wide-field recording analysis 25°C</td>
      <td>Wide-field analysis (after Plucinska et al.) 28°C</td>
    </tr>
    <tr>
      <td colspan="4">Retrograde</td>
    </tr>
    <tr>
      <td>Fast</td>
      <td>0.76 ± 0.08 [µm/s]</td>
      <td rowspan="2">0.55 ± 0.07 [µm/s]</td>
      <td rowspan="2">0.92 ± 0.02 [µm/s]</td>
    </tr>
    <tr>
      <td>Slow</td>
      <td>0.42 ± 0.11 [µm/s]</td>
    </tr>
    <tr>
      <td colspan="4">Anterograde</td>
    </tr>
    <tr>
      <td>Fast</td>
      <td>0.62 ± 0.09 [µm/s]</td>
      <td rowspan="2">0.45 ± 0.08 [µm/s]</td>
      <td rowspan="2">0.77 ± 0.01 [µm/s]</td>
    </tr>
    <tr>
      <td>Slow</td>
      <td>0.36 ± 0.08 [µm/s]</td>
    </tr>
  </tbody>
</table>

Mitochondria typically showed sustained phases of fast antero- or retrograde motion, which were interspersed by short-term pauses and periods of slow directed motion where the direction of motion can reverse. After a short period of time, the mitochondria continued to travel fast in the original direction of transport. This stereotypical sequence of events suggests a high level of coordination between the motion states. To quantify this, we analyzed the frequency and transition time between the different states (Figure 2—figure supplement 2). A number of trends became apparent from this analysis. First, an analysis of the pause durations suggests two different pausing mechanisms: Pauses involving fast motion states (fast-fast or fast-slow/slow-fast transitions) show mono-exponential distributions with decay constants of 1.94 s and 1.97 s, whereas pauses between two slow states show a longer duration with a decay constant of 3.2 s (Figure 2—figure supplement 2). Very long pauses (>20 s) were always (98% of n = 97) associated with transitions involving the slow motion states and had a high probability of involving a change in directionality (56% of n = 97). For pauses <20 s, a change in direction was only detected in 19% (of n = 1137) of the events. Second, there is a clear directionality of motion in the overall trajectory determined by the direction of fast motion. We did not observe any transitions between fast anterograde and fast retrograde states within one track, not even multi-step transitions that would involve the slow state. Moreover, moving mitochondria – irrespective of their speed – have a high probability of continuing in the same direction after a pause (77% or higher depending on the mode of motion, Figure 2—figure supplement 2). Approximately half of the time, the mitochondria remain in the same motional state (i.e. direction and velocity) and directional changes between fast and slow motion were unlikely (~6% of all pauses). In summary, the probability diagram of possible transitions (Figure 2—figure supplement 2) is substantially more complex than anticipated from previous in vitro and in vivo reports (Misgeld et al., 2007; Plucińska et al., 2012; Obashi and Okabe, 2013) and suggests that a number of mechanisms might influence the different state transitions along a mitochondrion’s axonal trajectory.

### Influence of obstacles

Utilizing the wide-field information that complements our trajectories, we analyzed the dynamic behavior of moving mitochondria in the context of the surrounding axonal environment (Figure 3a). Here, the influence of stationary mitochondrion became evident, as suggested previously (Ohno et al., 2011; Figure 3a, Video 1 and 2). Mitochondria moving along a ‘free’ track spend the majority of time in fast movement states (Figure 3b). However, when stationary mitochondria were present on the track, the time spent in the stationary state substantially increased in both directions (anterograde: 34% to 58%, retrograde: 40% to 58%). Notably, for anterograde transport, the time spent in the fast movement state decreased substantially at sites occupied by resting mitochondria (ratio fast/slow movement states: free track - 56%/10% = 5.6 vs. occupied track - 27%/14% = 1.9). For transport in the retrograde direction, this switch was absent (free track - 52%/8% = 6.5 vs. occupied track - 37%/4% = 9.3). This is in line with previous observations that retrograde transport might be less sensitive towards obstacles than anterograde transport (Mallik et al., 2004), suggesting that the slow movement state might be 'a shift to low gear' used to circumvent obstacles that the driving forces of the fast transport states have a hard time overcoming.

![Figure 3.](https://cdn.elifesciences.org/articles/46059/elife-46059-fig3-v2.jpg)

**Figure 3.:** (a) Mapping of the trajectory of a single mitochondrion (black arrow) onto the inverted wide-field images (scale bar, 5 µm). Bottom panel, kymograph color coded according to motion state, location of stationary mitochondria depicted in gray. (b) Pie charts indicating the fraction of time spent in each motion state related to the local presence or absence of a mitochondrion in retrograde (left) or anterograde (right) direction (n = 16 trajectories, nine fish). (c) Repetitive tracking of mitochondria over the same stretch of an axon. Upper Panel: Wide field image of the ROI showing the location of stalled mitochondria on a section of microtubules. Middle panel: The time a mitochondrion needed to transverse 100 nm is plotted as a function of position along the axon. Gray boxes indicate the presence of stationary mitochondria. The red line indicates the threshold level to identify bins of slow movement. Dashed black lines indicate locations where multiple mitochondria were observed to pause (see lower panel). Lower panel: Fraction of trajectories (plotted in 1 µm bins from mitochondria moving in both directions) along the axon showing crossing times of more than 10 s for 1 µm.

It is known that road-blocks or local influences exist along the axon that may provide external determinants of pausing (Hirokawa et al., 2009; Conde and Cáceres, 2009; Bálint et al., 2013). To explore the possibility of preferred pausing sites and check whether pausing is localized at specific points or randomly distributed along the axon, we took advantage of the fact that, with a slight modification of our approach, we can observe the same axon segment with several distinct cargoes (rather than following one cargo over an extended axon length). For these measurements, we used a combination of mitoTagRFP-T and mitoDendra2. This allowed us to create a 'red only' field-of-view by taking advantage of the swift conversion of Dendra2’s green to a red state using 405 nm excitation (Chudakov et al., 2007). In this field-of-view, the incoming mitochondria appear green and were easily tracked. We acquired trajectories of 16 mitochondria along the same region. When we plotted the time needed to advance 100 nm against the position of the repeatedly sampled axon stretch, a clear pattern emerged (Figure 3c): While progress along most of the axonal length was relatively steady (t < 1 s for traveling 100 nm), there were distinct foci where progress was slower. Incorporating wide-field information into the analysis, we observed that, in many instances, the pauses coincided as expected with the presence of stationary mitochondria. However, other pause foci appear on ‘free’ segments – suggesting that there are additional retaining influences that can induce pausing, and that the clustering of pauses near stationary mitochondria might not only be merely due to geometrical constraints, but could be due to the local structure of the cytoskeleton (Bálint et al., 2013) or attractive milieu influences, such as local calcium hot spots (MacAskill and Kittler, 2010) or areas of substrate availability (Pekkurnaz et al., 2014).

## Discussion

In summary, this new application of orbital tracking microscopy with nanoscopic spatial precision and millisecond temporal resolution to zebrafish neurons in vivo provides unprecedented detail of subcellular trafficking in an intact organismic context. While this is the first time a feedback-based 3D SPT approach was used for tracking particles in vivo, we want to point out that this is not the only technique capable of such measurements (Shechtman et al., 2015; McHale et al., 2007), and further improvements are conceivable. For example, two-photon excitation-based tracking might in principle be more favorable for deep tissue imaging than our one-photon approach (Helmchen and Denk, 2005). Still, the method presented here is less costly and – given the broad two-photon absorption cross-section of many fluorophores – more versatile as far as wavelength multiplexing is concerned. Moreover, the specific implementation of 3D SPT that we detail here overcomes field-of-view limitations of many other approaches, allows flexible integration of photo-activation lasers and easy modulation of the tracking laser, which together can further increase the tracking range. Finally, simultaneous wide-field detection provides cellular and histological context, which is important in interpreting local signaling that might affect organelle trafficking.

Capitalizing on these technical advances, we reveal that beyond the expected three major movement states of mitochondria (resting, antero- and retrograde) previously reported in zebrafish and many other settings (Plucińska and Misgeld, 2016; Saxton and Hollenbeck, 2012), we observed two components, a fast and a slow transport process in both the antero- and retrograde directions. The fast components are consistent with the known characteristics of classical kinesin- and dynein-mediated transport reported in vivo (Misgeld and Schwarz, 2017), and – even though the dynamics of organelles result from complex motor combinations and interactions – are on the order of speeds measured for these motors in reconstitution assays (0.7–1.0 μm/s; Toba et al., 2006; King and Schroer, 2000; Milo and Phillips, 2016). While we do not currently know the molecular underpinnings of these slow movement states, our observations reveal a number of properties that deserve note: The slow movement states appeared – in contrast to the fast movements – symmetrical in speed. Moreover, the transition into and out of these slow movement states was not random, but followed a defined set of rules. Finally, these state transitions seemed to be impacted by external influences, such as local obstacles within the axon. Notably, atthe typical sampling rates used in kymography recordings of mitochondrial transport in vitro or in vivo (i.e. 1–2 Hz), the slow state is on the verge of detectability (duration ~0.45 s; Table 2) – and hence might sometimes be subsumed in either the moving speeds or convolved with pause length and frequency. There are a number of possible interpretations of the slow movement states. One would be shape changes of mitochondria as they encounter obstacles or are partially tethered in the axon. For instance, one end of the mitochondria could encounter an obstacle and stop moving while the other end continues to move. As the orbital tracking measures the position of the center of fluorescence signal, compression or expansion of the mitochondria would convert into a slower change in the center position. However, this explanation is unlikely as the average displacement in the slow movement state is approximately 300 nm, which would be equivalent to a 600 nm change in the overall shape of the mitochondria. This is on the order of the size of moving mitochondria (Figure 1—figure supplement 3b). In addition, we use the presence of a stationary state to separate regions of active transport. In the current implementation of the analysis, we would not be able to detect a direct switch between the fast and slower motional states. If the slow movement state were due to anchoring of one end, it would mean that the entire mitochondria first stops moving and then only one side continues. Still, we would like to note that the orbital tracking method also has the potential to investigate shapes changes during tracking by analyzing higher order Fourier components of the orbital tracking signal or by adding a second, small amplitude higher frequency oscillation to the orbit (Lanzano et al., 2011). Thus, a more formal investigation of possible shape changes of mitochondria during different behaviors will become possible in the future.

Given our present data, more likely explanations of the slow movement states in our view involve changes in the engaged molecular transport machinery. Options include: (I) the engagement of additional motors beyond kinesins and dyneins (the known speed characteristics of which matched the fast movement states, as expected – see Table 1), (II) the concomitant engagement of an anchor (such as syntaphilin) and kinesin/dynein motors, or (III) the existence of an unappreciated regulation that can switch the known mitochondrial motors into specific ‘slow’ states. The fact that the slow states had the same speed distribution in both directions leads us to favor the first hypothesis; however, the nature of the involved motors remain elusive as of now. One possibility would be the involvement of actin-based motors in mitochondrial movements, as previously suggested for example based on pharmacological experiments in vitro and genetically in flies (Ligon and Steward, 2000; Morris and Hollenbeck, 1995; Pathak et al., 2010). Thus far, myosin-actin interactions have been mostly linked to reduced mitochondrial motility (Pathak et al., 2010) and specific stationary states, as recently demonstrated using a new opto-chemical crosslinking approach (Gutnick et al., 2019). Still, our data show a complex and orchestrated sequence of motility changes at transitions from fast moving into stationary states that, in many prior analyses, would go undetected and hence be subsumed in other movement states. Thus, a role for a transient slow actin-dependent movement phase that at the same time is compatible with the residual slow motility of mitochondria in microtubule-depleted axons in vitro (Morris and Hollenbeck, 1995), as well as the acceleration of transport seen after myosin knock-down in flies (Pathak et al., 2010), seems like a plausible explanation of our observations. The slow movement state engaged preferentially when a moving mitochondrion encountered a local obstacle such as an anchored mitochondrion in the axon shaft. This could be an indication that these putative actin-dependent mitochondria translocations are important for local positioning and movement between microtubule tracks (Gutnick et al., 2019; Atkinson et al., 1992; Langford, 1995) and the notion that myosin-actin interactions increase mitochondrial pause frequencies (Morris and Hollenbeck, 1995; Pathak et al., 2010). While this specific molecular interpretation remains speculative, the convenience of gene overexpression and deletion in zebrafish combined with 3D orbital tracking now allows testing of this hypothesis.

In any case, while the exact molecular nature and role of the slow movement phases of mitochondrial trafficking remain to be resolved, the observation of new movement states for a well-studied organelle such as mitochondria testifies to the power of the in vivo 3D SPT approach. Indeed, we foresee a range of applications, including investigations using neurological disease models, such as tauopathies, where transitions of movement states and hence the duty cycle between movement and stationary phases seem to be especially affected (Plucińska et al., 2012; Fatouros et al., 2012; Devireddy et al., 2015). Possible applications of the technique described here go well beyond simple in vivo observations of physiological and pathological organelle behavior. For instance, the ability to visualize the cellular surroundings of a trafficking organelle will allow a detailed determination of how neuronal landmarks known to be preferentially associated with mitochondria, such as branch points (Faits et al., 2016; Courchet et al., 2013; Spillane et al., 2013) or presynaptic terminals (Lewis et al., 2016; Obashi and Okabe, 2013), modulate mitochondrial behavior. This approach can be readily combined with a rapidly expanding set of organelle-targeted biosensors (Breckwoldt et al., 2014) and optogenetic actuators of organelle physiology (Rost et al., 2015; Ashrafi et al., 2014), as well as motor (Gutnick et al., 2019; van Bergeijk et al., 2015) and track (Borowiak et al., 2015) composition. As the laser beam is orbited about a single organelle, it provides optical selectively and will enable a detailed correlation between the physiological state of a trafficking organelle and its movement behavior. This remains a largely unresolved aspect of organelle dynamics that can now be addressed by ‘multi-parametric’ analysis in vivo beyond the capabilities offered by previous approaches.

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
      <td>Biological sample (Danio rerio)</td>
      <td>Roy</td>
      <td>(Ren et al., 2002)</td>
      <td>mpv17a9/a9</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Biological sample (Danio rerio)</td>
      <td>Isl2b:Gal4</td>
      <td>(Ben Fredj et al., 2010)</td>
      <td>Tg(−17.6isl2b:GAL4-VP16,myl7:EGFP)zc60</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Genetic reagent (UAS Constructs)</td>
      <td>UAS:mitoTagRFP-T; UAS:mitoPAGFP; UAS:memYFP; UAS:mitoDendra2</td>
      <td>(Köster and Fraser, 2001)</td>
      <td>Identified as in B - there are no specific identifiers</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Analysis Software</td>
      <td>this paper</td>
      <td>https://gitlab.com/groups/3d-spt-orbital-tracking/-/shared</td>
      <td>self-written, Matlab 2015b</td>
    </tr>
  </tbody>
</table>

### Animals

We used a mutant zebrafish line (Roy) with impaired production of silver pigment (Ren et al., 2002), which we crossed with the transgenic driver line Isl2b:Gal4 (kept at a heterozygous background Roy +/-). This line contains a specific promoter that drives expression of the Gal4 transcription factor in zebrafish sensory neurons (Ben Fredj et al., 2010). Fish were maintained, mated, and raised as previously described (Mullins et al., 1994). Embryos were kept in 0.3x Danieau’s solution at 28.5°C and staged as described (Kimmel et al., 1995). No randomization or blinding in the selection of zebrafish embryos was used in this study. All experiments with zebrafish larvae were performed according to institutional and government regulations.

### Labeling constructs, screening and mounting

To achieve mosaic labeling, UAS constructs were co-injected (each at a concentration of 10 ng/µl) into fertilized eggs of the Isl2b:Gal4 x Roy fish as described before (Godinho, 2011). At 24 hr post-fertilization (hpf), embryos were transferred to 1% N-phenylthiourea (PTU) to inhibit pigmentation. At 2 dpf, embryos were anesthetized using tricaine (at a final concentration of 0.75 mM) and embedded in low melting agarose (0.7–0.8%, Sigma) for screening. Embryos showing a suitable expression pattern (mitoTagRFP-T expressed in isolated sensory neurons in the tail fin) were removed from agarose and allowed to recover in PTU solution overnight. The next day they were again anesthetized and mounted in agarose for imaging. PTU/Tricaine remained present throughout the experiment. When using photosensitive proteins, embryos were maintained in a dark environment and mounted under a dissection microscope with blue light excluding filters. A list of constructs and identifiers are given in the Key resource table.

### Experimental setup

#### Microscope design

The instrument used in this work was designed based on a previously described microscope (Dupont et al., 2013; Katayama et al., 2009). To enhance the response of the system for tracking at high speeds, we replaced the piezo mirror, which had a long response time (>10 ms), with galvanometric mirrors resulting in orbit repetition rates up to 333 Hz. In addition, we replaced the previously used software (SIMFCS, LFD University of California – Irvine, US) with a self-written code written in LabVIEW 2014. The program runs on the host computer and on a deterministic processing unit, consisting of a field-programmable gate array (FPGA) and a real-time processor (cRIO 9082, National Instruments). This upgrade enabled us to achieve real-time control of the system with a jitter of less than 100 μs, implement new modes of operation and to synchronize all hardware components. In the current configuration, the system has a localization precision of 3 nm laterally and ~20 nm axially using 190 nm beads as a calibration sample, depending on the count rate (Figure 2—figure supplement 2). Stationary mitochondria in the stem axon were used to measure the localization precision. Using the same calibration procedure, the system achieved an average lateral localization precision of 31.5 nm (21 nm stationary accuracy, 42 nm dynamic accuracy). The lateral localization precision for smaller moving mitochondria (after removing high frequency oscillations by averaging over five localizations) can be estimated through the standard deviations of the orbit displacement histograms and averages 4.6 nm (Figure 2c). The accessible tracking area of the microscope is limited by the travel range of the z-objective piezo (100 µm) and the travel range of the sample stage on top of the microscope (>10 cm, using the long-range tracking mode). The tracking algorithm was implemented using a combination of a field programmable gate array (FGPA), a real-time computer and a standard personal computer. This combination allowed us to achieve accurate timing on the submillisecond time scale and a synchronized operation of the microscope as discussed below.

### Tracking software

To achieve accurate timing on the submillisecond time scale, we separated the execution of the tracking code between a host computer (not deterministic) and a deterministic processing unit. The host computer (Intel Core-i7, 16 GB Ram, Solid State Disc for image acquisition) is used to record video frames, to visualize the data, to control the deterministic unit and to receive and save the data. The deterministic unit contains an FPGA and a real-time computer on a single device. The FPGA records incoming TTL pulses, generates the voltages for the galvanometer mirrors and the z-piezo and synchronizes the AOTFs and the EMCCD camera with TTL signals. Furthermore, it sends photon counts, through a direct memory access first-in first-out buffer (DMA-FIFO), to the real-time computer. The communication between the FPGA and the real-time computer occurs instantaneously (with respect to time scales relevant for tracking) as they are mounted on the same device. The communication between the real-time and the host computer occurs over a gigabit Ethernet network, which ensures lossless data transmission. Defining a tracking area on a previously acquired confocal image is the starting point for the tracking algorithm. All necessary orbit properties (orbit size, orbit time, the intensity threshold, starting point of the tracking, etc.) are transferred separately before the experiment or directly before starting the tracking algorithm. The FPGA initiates the orbit around the particle and measures the intensity in 16 sectors of each orbit. After measuring each sector, the photon counts are binned, transferred to the real-time computer and stored in two FIFO buffers, one for each detector. When all 32 elements are available (16 bins × 2 detectors), the buffers are read out and the positioning algorithm calculates the new position of the particle. The calculation is described in detail in the Tracking Algorithm Section. This takes between 100 µs and 700 µs. Depending on whether a particle is detected, which is determined from the current count rate, the positioning algorithm performs two different tasks. If the current count rate is below the user-defined threshold, a searching modus is started. It performs a spiral motion laterally around the starting point until the count rate rises above the threshold, which indicates that a particle has been found. When the count-rate is above the threshold, the position of the particle is determined by the real-time computer. The new position data is written into variables on the FPGA, which are continually read out during the orbit and provide the feedback control of the orbit. Since the new orbit is started directly after the previous one, the first point is biased with the position from the old one. In practice, it is more convenient to choose this ‘on the fly’ update, which causes no measurable performance loss, than to wait for the positioning algorithm to finish the calculations. Depending on the chosen settings, the positioning algorithm performs additional tasks, which are explained in detail in the following paragraphs. After the new position was sent to the FPGA, the real-time computer has a certain wait time until the FIFO buffers with the intensity data from a new orbit can be read out again. This time is used to send several data values over the gigabit network to the host computer. These data values include the three-dimensional position, the count rate of both APDs, the time for each orbit, if a particle was tracked during the orbit, the current camera frame and the direction of a recentering event, when long-range tracking is used. When the host computer receives these values, the data is visualized in a user interface and allows the user to follow the particle and to take action, if desired. The algorithm continues to track the particle until the count rate drops below a given threshold. The user can then decide whether she/he wants to continue tracking another particle that diffuses into the search area or stop the tracking experitment. When the user wants to stop the tracking proceedure while the intensity is above threshold, a command is sent over the network to the real-time computer and the FPGA and the data acquisition are stopped.

### Tracking algorithm

The tracking algorithm is implemented in several steps. For the lateral localization of the particle, the signals from both detection channels are summed together. The intensity counts from 16 bins per orbit can be described by a Fourier series:

$$
I(\phi,r)=\frac{a_{o}(r)}{2}+\sumk=1n(a_{k}(r)cos⁡(k\phi)+b_{k}(r)sin⁡(k\phi) )
$$

Only the zero- and first-order coefficients are relevant for the localization and are extracted using a Fast Fourier Transformation. The angular position, ϕ, and the distance to the center of the orbit, dr, are given by:

$$
\phi=arctan\frac{b_{1}(r)}{a_{1}(r)}d_{r}=r_{Orbit}∗f(r)∗Mod(xy)
$$



$$
Mod(xy)=\frac{\sqrt{a_{1}^{2}(r)+b_{1}^{2}(r)}}{a_{0}(r)}
$$

Localization in z is performed through the intensity ratio between the two detection planes. The particle’s axial position in relation to the focal plane dz is given as:

$$
d_{z}= Δz_{APD1−APD2}∗g(z)∗Mod(z)Mod(z)=\frac{I_{APD 1}−I_{APD 2}}{I_{APD 1}+I_{APD 2}}
$$

To minimize the calculation time, both scaling functions, f(r) and g(z), are implemented with a combination of a look-up table and a binary search, which ensures a rapid determination of the new orbit position. The two look-up tables were generated through simulations (Matlab 2012b) in units of the orbit radius (rOrbit) and the distance between the two detection planes (ΔzAPD1-APD2). Both look up tables are stored on the real-time computer and loaded into the random access memory for reliable and fast accessing during the experiment.

### Simultaneous wide-field imaging

To determine the location of the tracked particle within the specimen, we use a wide-field microscope coupled to the tracking system whose image plane is aligned to the focal plane of the confocal orbital tracking system (Katayama et al., 2009). The new tracking software externally triggers each frame of the EMCCD camera and thus allows a temporal synchronization between the tracking coordinates and the wide-field images. Spatial synchronization is achieved through a mapping procedure and subsequent coordinate transformation. A second-order polynomial transformation matrix is created by removing the emission filter and recording the back reflection of the tracking laser at the coverslip for 25 known locations on the EMCCD camera.

### Long-range tracking

One of the advantages of orbital tracking is that it is a feedback approach and can, in theory, follow the particle throughout the whole specimen. In practice, however, as particles travel away from the initial position along the optical axis of the microscope, imperfections in the optics and alignment process lead to a relative shift between the two detection planes. This mismatch between the detection planes results in a loss of localization precision and ultimately to failing of the tracking capability. Furthermore, the field-of-view of the EMCCD camera is limited, in our case to an area of 35 × 35 µm². For particles that travel outside of this area, the environmental information is lost. To overcome these difficulties, other groups use a feedback loop to move the sample stage rather than the laser beam (Welsher and Yang, 2014; Lessard et al., 2007). However, this leads to a decrease in the response time. The approach we have undertaken is to incorporate a second feedback loop into the tracking software that recenters the sample with an additional stage when the particle reaches a predefined distance from the center of the optical axis. Each axis is handled independently. In this way, we keep the fast response of laser scanning for the majority of the trajectory while increasing the accessible tracking area in x and y to several cms. During such a recentering event, the corresponding galvanometer mirror is moved back to the resting position and the tracking algorithm waits until the stage movement is complete. Depending on the axis, this takes 35 ± 16 ms (y-axis) to 63 ± 5 ms (x-axis). Afterwards the tracking algorithm continues to follow the particle.

### Dark orbits

When the temporal resolution of the microscope is higher than necessary for tracking the particles of interest, photobleaching can be reduced by either decreasing the laser power and the orbital frequency or by turning off the laser during consecutive orbits, a feature coined ‘dark orbits’. As the FPGA controls the AOTF as well as the galvanometer mirrors, we can utilize only one out of every nth orbit to excite the particle and to determine its location. The laser is turned off for the remaining n-1 orbits, thereby effectively reducing the exposure time of the particle and allowing the collection of longer trajectories. When using dark orbits, the bias of the first data point observed when updating ‘on the fly’ is no longer an issue as there is ample time to center the orbit on the new location of the particle.

### Data collection

#### 3D tracking and wide-field imaging

At 3 dpf, selected larvae positive for mitoTagRFP-T were prepared for imaging. Larvae were mounted in low melting agarose in glass-bottom petri dishes. During the experiment, the temperature was maintained at 25° to decrease mechanical drift. Each fish was screened for the expression of mitoPAGFP prior to the experiment by photoconverting a small subset of mitochondria outside the region of interest. Once we identified embryos positive for PAGFP, we activated individual mitochondria with blue light using a xy scanning pattern (405 nm, 80µW measured before the objective; 34.6 × 34.6 µm², that is a region of 256 × 256 pixels of 135 × 135 nm² per pixel; 30µs pixel dwell time). To estimate the photoactivation contrast, we converted five sensory neurons and measured the PAGFP and TagRFP-T channels before and after photoactivation. This resulted in a ~ 25 fold change in ratio (27.8 ± 2.3; red channel, before-to-after: 0.7 ± 0.05; green channel: 20.6 ± 1.5; mean ±sem = 5 cells). We tracked each activated mitochondrion in the green channel (488 nm excitation) with an acquisition speed of 100 Hz (a 5 ms orbit +one 5 ms dark orbit) and simultaneously observed it via the wide-field microscope in the red channel (561 nm excitation, 2 Hz). We stabilized the count rate at approximately 500 photons per orbit (or 100 kHz) by manually adjusting the laser power during the measurement to achieve a constant localization precision of <5 nm in xy and ~30 nm in z. The laser power ranged from <1 µW in the beginning to up to 25 µW, measured before the objective, at the end of a measurement. The feedback loop for the long-range tracking was activated every time a mitochondrion traveled further than 10 µm away from the center of the tracking area. Mitochondria were tracked until the intensity counts fell beneath the background threshold level (adjusted individually for each fish). In total, we collected 43 trajectories from 16 individual zebrafish larvae. Trajectories where the algorithm was switching between different mitochondria during the experiment were discarded.

### Repetitive tracking

We investigated the propensity of mitochondria to pause at particular locations along an axon by tracking the motion of several mitochondria along the same region of a neurite. For these experiments, selected larvae positive for mitoDendra2 and mitoTagRFP-T were prepared for imaging at 3 dpf as described above. A stretch of a neurite (approximately 35 µm in length) was repeatedly irradiated using 405 nm light (80µW measured before the objective; 34.6 × 34.6 µm², that is a region of 256 × 256 pixels of 135 × 135 nm² per pixel; 30µs pixel dwell time) to convert mitoDendra2 from green to red. Any new mitochondria entering the photoconverted region were tracked (100 Hz, a 5 ms orbit +one 5 ms dark orbit) using 488 nm excitation until they either left the field-of-view or were fully photoconverted from the 488 nm excitation laser to red fluorescence and thus could no longer be tracked in the green channel. After each recorded trajectory, a 405 nm scan was repeated to erase any residual or reemerging fluorescence. Simultaneous wide-field observation was only possible for the first trajectory due to the high rates of mitoTagRFP-T bleaching caused by the 405 nm laser. In total, we recorded 50 trajectories from three neurons (three embryos).

### Tracking precision

#### Tracking precision, in vitro

Tracking precision depends on both the signal-to-noise ratio of the measurement as well as the mobility of the particle. We first tested the localization accuracy of stationary particles. 190 nm multifluorescent beads (Spherotech) were imbedded in a polymer and tracked using various laser powers. Data are shown in Figure 1—figure supplement 1. From the standard deviation of the particle position, we estimate the tracking accuracies to be <3 nm laterally and <21 nm axially for count rates above 200 photons per orbit (or 40 kHz). Next, we tested the precision of tracking of a mobile particle by using a 3-axis piezo stage mounted on the microscope to move the sample with immobilized particles in a sinusoidal pattern over ±2 µm. The particle position was fit to a sinusoidal function and the standard deviation of the residuals used to estimate the tracking precision. For count rates of 1600 photons per orbit (or 320 kHz), no significant degradation of the tracking was observed up to velocities of >25 µm/s laterally and 15 µm/s axially. The slight decrease in accuracy of the x axis compared to the y axis at velocities above 5 μm/s is a result of the ~0.1 ms delay in updating the position of the particle ‘on the fly’ at the starting point of the new orbit (ϕ = 0°).

#### Tracking precision, in vivo

To estimate the tracking precision for following mitochondria under in vivo conditions, we tracked immobilized mitochondria in zebrafish embryos. For a count rate of 500 photons per orbit (100 kHz), we measured a localization precision along the minor axis of the mitochondrion of 21 nm (Figure 1—figure supplement 1e). When using a piezo stage to move the stationary mitochondria (similarly to the dynamic precision measurements using beads), we determined a tracking precision of 42 nm (Figure 1—figure supplement 1f). Moving mitochondria are typically smaller than stationary ones. If we analyzed the standard deviation of the y orbit displacement (Figure 2c), we achieve an average localization precision of 4.6 nm after removing high-frequency noise by smoothing the trajectory data by five points. Thus, the system is capable of measuring moving mitochondria in vivo with millisecond-and nanometer resolution over substantial parts of axonal arbors.

### Impact of mitochondrial shape

While mitochondria typically have an elliptical shape, which can decrease localization precision in other tracking techniques (Kao and Verkman, 1994), our 3D orbital tracking approach is not very sensitive to the shape as the recorded fluorescent signal during each orbit is converted into the frequency domain using a Fourier transformation. This is true as long as the object is on the size of the orbit or smaller. The lateral particle location is determined by the center-of-mass of the fluorescent signal represented in the first- and zero-order Fourier coefficients. Shape information is encoded in higher order Fourier coefficients, which are not used to calculate particle position. When the objects are much larger than the diameter of the orbit and homogenous in labeling, motion of the particle would not lead to a modulation in signal (Figure 1—figure supplement 3a). To investigate the influence of shape on orbital tracking, stationary mitochondria were externally moved using a piezo stage and tracked. The imposed trajectories could be completely recovered for mitochondria shorter than 1.2 µm (Figure 1—figure supplement 3b). As moving mitochondria in zebrafish show an average length of 0.71 ± 0.13 µm, we can rule out an influence of the mitochondrial shape on localization precision.

### Data analysis

Data and video analyses were performed using a self-written analysis software program in Matlab 2015b (The Mathworks, Inc).

### Trajectory analysis

To differentiate between active transport and stationary phases in each trajectory, we used a correlation approach. The sample was mounted such that the axons where extended roughly along the x axis. The lateral angle, φ, respective to the x axis between two consecutive orbits, was correlated along the trajectory using a sliding window of 64 points leading to a time dependent correlation function given by:

$$
Cor(t,\tau)= \frac{1}{(n−\tau)}\sumtt+64−\tau(\phi_{t})(\phi_{t−\tau})
$$

To reduce the dimension of the correlation carpet Cor(t,τ), we calculated the mean value of the interval Cor (t,τ = 0.03 s) to Cor(t,τ = 0.06 s) (Figure 1e). For a purely active transport process, the correlation amplitude approaches 1. The correlation amplitude decreases for stationary phases. To estimate the correlation amplitude given by stationary phases, we randomized the trajectory. However, as many trajectories have a clear direction of motion, particular angles of x occur more frequently and pure randomization of the trajectory is insufficient. Hence, we took the array of angles between consecutive positions in the trajectory and added a copy of the array where the sign of the angles had been reversed. The total array was then randomized and the same correlation analysis was applied. The mean plus five times the standard deviations was used as a threshold level and values above this value were assigned to regions of active transport. The assignment of active and stationary states was then shifted by half the size of the sliding correlation window (64/2 data points) to remove the delay caused by the size of the correlation window. To remove any artifacts introduced by a long-range tracking event, active phases shorter than 150 ms (twice the duration of recentering) are marked as stationary. The trajectory was smoothed after the correlation by five points (50 ms) to reduce high-frequency noise caused by the tracking algorithm. Using simulated data, we tested the analysis method and verified that >90% of the data points are correctly assigned by the analysis.

Each detected active phase was assigned to one of four dynamic populations. To do this, each active phase was first assigned to the retrograde or anterograde direction based on the motion with respect to the cell nucleus. As all fish were roughly aligned along the x axis, classification was determined through the direction of the total movement in x for each active phase. In the next step, the average velocity from each active phase was determined from the distance traveled and duration of the phase. Two velocity histograms, one for retrograde motion and one for anterograde motion, were then generated from all active phases for an individual trajectory (Figure 2—figure supplement 1). As fast motion is active in only one direction for a single mitochondrion trajectory, velocity histograms in the direction of fast motion were fitted with a two component Gaussian distribution using a maximum likelihood approach. Each active phase was then assigned to either the fast transport process (when above a threshold calculated as the mean of the two Gaussian centers) or to the slow state (when below the threshold, Figure 2—figure supplement 1).

### Wide-field analysis

We investigated whether the data presented in this study yields results consistent with previously published results (Plucińska et al., 2012). A direct comparison was not possible as the measurements were performed at different temperatures and the spatial and temporal resolution of the wide-field data is insufficient for detecting the different transport populations observed using orbital tracking. Thus, we analyzed our simultaneously acquired wide-field images similarly to what was done previously using an ImageJ plugin, MTrackJ (Meijering et al., 2012). A comparison of the wide-field data at 25°C with the orbital tracking analysis showed that the wide-field data is an average of the fast, slow and stationary populations (Table 2). As expected, a lower average anterograde and retrograde speed of mitochondria in Rohon-Beard sensory neurons was measured at lower temperatures (25°C compared to 28°C).

To investigate whether mitochondria have a tendency to pause in the vicinity of another mitochondrion, we performed a colocalization analysis using the wide-field images and the orbital tracking data. The positions and lengths of stationary mitochondria were extracted from the simultaneously acquired wide-field video. Moving mitochondria were removed from the video I(x,y,t) using the following equations.

$$
ΔI(x,y,t)=I(x,y,t+10)−I(x,y,t)
$$



$$
ΔI(x,y,t)={ΔI(x,y,t),ifΔI(x,y,t)<00,ifΔI(x,y,t)>0
$$



$$
I_{stationary}x,y,t=Ix,y,t+\DeltaI(x,y,t)
$$

As the analysis requires a stationary field-of-view, we analyzed regions between recentering events separately. For a video containing m long-range tracking events, m + 1 mean images of all the frames between two recentering events were calculated. The mean image after the last long-range event usually contained a very long (>1 min) stationary phase and was discarded. The m mean images were smoothed frame-wise by five pixels in x and y and converted to binary images (threshold: μ +5*σ of each image). To remove artifacts arising from autofluorescence, other mitochondria and other labeled neurites, a mask was applied that excludes all values outside of a 51 × 11 pixel area around the trajectory of the tracked mitochondria. With the built-in Matlab function „regionprobs’, we then extract the position and length of each stationary mitochondrion and combined this information with the measured trajectory using the coordinate transformation determined during the calibration (Figure 3a,b).

### Statistics

Statistical values were generated by dividing each set of data into 10 equally sized bins and fitting the data either to a Gaussian distribution (xy Velocity) or to a single exponential decay (Duration, xy Displacement). The average, percentiles, standard deviations and significance levels (two-sided t-test) were then calculated from the center of the Gaussian functions or the decay constants determined through the fit. The statistical values for the x orbit displacement were obtained through directly fitting a Gaussian function to each data set.

### Software availability

The tracking and analysis software used in this study is available at https://gitlab.com/groups/3d-spt-orbital-tracking/-/shared (Wehnekamp, 2015; copy archived at https://github.com/elifesciences-publications/Orbital-Tracking-Zebrafish2019-).
