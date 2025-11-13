# Hippocampal ensemble dynamics timestamp events in long-term memory

## Authors

- Alon Rubin<sup>1</sup>
- Nitzan Geva<sup>1</sup>
- Liron Sheintuch<sup>1</sup>
- Yaniv Ziv<sup>1</sup> †

### Affiliations

1. Department of Neurobiology Weizmann Institute of Science Rehovot Israel

† Corresponding author

## Abstract

The capacity to remember temporal relationships between different events is essential to episodic memory, but little is currently known about its underlying mechanisms. We performed time-lapse imaging of thousands of neurons over weeks in the hippocampal CA1 of mice as they repeatedly visited two distinct environments. Longitudinal analysis exposed ongoing environment-independent evolution of episodic representations, despite stable place field locations and constant remapping between the two environments. These dynamics time-stamped experienced events via neuronal ensembles that had cellular composition and activity patterns unique to specific points in time. Temporally close episodes shared a common timestamp regardless of the spatial context in which they occurred. Temporally remote episodes had distinct timestamps, even if they occurred within the same spatial context. Our results suggest that days-scale hippocampal ensemble dynamics could support the formation of a mental timeline in which experienced events could be mnemonically associated or dissociated based on their temporal distance.

## Materials and methods

### Animals and surgical procedures

All procedures were approved by the Weizmann Institute IACUC. Five male C57BL/6 mice aged 8-12 weeks at the start were used in this study. Mice were housed with 1-4 cage-mates in cages with running wheels, and underwent two surgical procedures under isoflurane anesthesia (1.5-2% volume). First, we injected into the CA1, 400 nL of the viral vector AAV2/5-CaMKIIα-GCaMP6s or AAV2/5-CaMKIIα-GCaMP6f (~2 × 1013 particles per ml, packed by University of North Carolina Vector Core)(Chen et al., 2013). Stereotatic coordinates were: -1.9 mm anterio-posterior, -1.4 mm mediolateral, -1.6 mm dorsoventral from bregma. The second surgery, which took place at least one week after the viral injection, was the implantation of a glass guide tube directly above the CA1. We used a trephine drill to remove a circular part of the skull centered posterio-lateral to the viral injection site. We removed the dura and cortex above the CA1 by suction with a 29 gauge blunt needle while constantly washing the exposed tissue with sterile PBS. We then implanted an optical guide tube with its window just dorsal to, but not within, area CA1, and sealed the space between the skull and guide tube using 1.5% agarose in PBS. The exposed areas of the skull were then sealed with Metabond (Parkell, Edgewood, NY) and dental acrylic.

### Ca2+ imaging and behavioral setup

For time-lapse imaging in freely behaving mice using an integrated miniature fluorescence microscope (nVistaHD, Inscopix), we followed a previously established protocol (Ziv et al., 2013). Briefly, at least three weeks after guide tube implantation, we imaged water restricted mice under isoflurane anesthesia using a two-photon microscope (Ultima IV, Bruker, Germany), equipped with a tunable Ti:Sapphire laser (Insight, Spectra Physics, Santa Clara, CA). We inserted a ‘microendoscope’ consisting of a single gradient refractive index lens (0.44 pitch length, 0.47 NA, GRINtech GmbH, Germany) into the guide tube, and examined Ca2+ indicator expression and tissue health. We selected for further imaging only those mice that exhibited homogenous GCaMP6 expression and healthy appearance of the tissue. For the selected mice, we then affixed the microendoscope within the guide tube using ultraviolet-curing adhesive (Norland, NOA81, Edmund Optics, Barrington, NJ). Next, we attached the microscope’s base plate to the dental acrylic cap using light cured acrylic (Flow-It ALC, Pentron, Orange, CA). After a few days, we began training the mice to run back and forth on two elevated linear tracks (Environments A and B). Environment A was a straight 96 cm long track and Environment B was an L-shaped track consisting of two 48 cm long arms. Each environment had distinct sets of visual and tactile cues, overhead lights, flavored liquid rewards, and odor cues. Before the beginning of each pre-training or imaging session we wiped the tracks with differently scented paper towels (0.5% acetic acid for environment A and 10% ethanol for environment B). We trained the mice to run back and forth along the track by giving them a measured amount of water sweetened with commercial fruit juice concentrate, lemon flavored for track A and raspberry flavored for track B, with 2% added sugar by weight. The water reward was dispensed using a custom-made computer controlled device. To record mouse behavior, we used an overhead camera (DFK 33G445, The Imaging Source, Germany), which we synchronized with the integrated microscope. Ca2+ imaging was performed at 20Hz. Before beginning with Ca2+ imaging, we pre-trained the mice for 8–11 days, until the mice ran at least 60 times the entire length of each track in two consecutive days. Pre-training and imaging sessions consisted of five 3-min-long trials, with an inter-trial interval of 3 min. We imaged a total of 5 mice (two that were injected with AAV2/5-CaMKIIα-GCaMP6f and three that were injected with AAV2/5-CaMKIIα-GCaMP6s) every other day for 15 days, making for 8 recording days. Each day of the experiment consisted of two sessions (AM and PM) separated by 4–5 hr. Remapping tests within a single session were performed on days 16–17. At the end of the experiment we removed the base plate by drilling away the top acrylic cap and re-examined the health of the CA1 neurons by imaging the mice under isoflurane anesthesia using a two-photon microscope as described above.

### Processing of Ca2+ imaging data

We processed imaging data using commercial software (Mosaic, Inscopix) and custom MATLAB routines as previously described (Ziv et al., 2013). To increase computation speed, we spatially down-sampled the data by a factor of two in each dimension. To correct for non-uniform illumination both in space and time, we normalized the images by dividing each pixel by the corresponding value in a smoothed version. The smoothed version was obtained by applying a Gaussian filter with a radius of 40 pixels on the videos. Normalization enhanced the appearance of the blood vessels, which were later used as stationary fiducial markers for image registration. We used rigid body image registration to correct for lateral displacements of the brain. This procedure was performed on a high contrast subregion of the normalized movies for which the blood vessels were most prominent. The registered movies were transformed to relative changes in fluorescence, $\frac{\DeltaF'(t)}{F_{0}}=(F'(t)−F'_{0})/F'_{0}$, where $F^{'}_{0}$ is the value for each pixel averaged over time. For the purpose of cell identification the movies were downsampled in time by a factor of five. We identified spatial filters corresponding to individual cells using an established cell-sorting algorithm that applies principal and independent component analyses (PCA and ICA) (Mukamel et al., 2009). For each spatial filter, we used a threshold of 50% of the filter’s maximum intensity and each pixel that did not cross the threshold was set to zero. After the cells were identified, further cell sorting was performed to find the spatial filters that follow a typical cellular structure. This was done by measuring the filters’ area and circularity and discarding those whose radius was smaller than 5 μm or larger than 14 μm, or which had a circularity smaller than 0.8. In some cases, the output of the PCA/ICA algorithm included more than one component that corresponded to a single cell. To eliminate such incidents, we examined all cells whose centroids were less than 18 μm apart and whenever their traces had correlation > 0.9, the cell with the lower average peak amplitude was discarded.

### Detection of Ca2+ events

Ca2+ activity was extracted by applying the thresholded spatial filters to the full temporal resolution (20Hz) $\DeltaF'(t)/F_{0}$ videos. Baseline fluctuations were removed by subtracting the median trace (20 s sliding window). The Ca2+ traces were smoothed with a low-pass filter with a cutoff frequency of 2Hz. Ca2+ candidate events were detected whenever the amplitude crossed a threshold of 4 or 5 median absolute deviations (MAD), for GCaMP6s or GCaMP6f, respectively. Cellular Ca2+ events are characterized by fast rise and slow decay times. To capture these characteristics in our data we considered for further analysis only candidate Ca2+ events that followed typical indicator decay time, and decay-to-rise time ratios. In order to avoid the detection of several peaks for a single Ca2+ event, only peaks that were 4 or 5 MAD higher than the previous peak (within the same candidate event) and 2 or 2.5 MAD higher than the next peak for GCaMP6s or GCaMP6f, respectively, were regarded as true events. We set the Ca2+ event occurrence to the time of the peak fluorescence. To mitigate the effects of crosstalk (i.e., spillover of Ca2+ fluorescence from neighboring cells), we adopted a conservative approach, allowing only one cell of a group of neighbors (cells whose centroids are less than 18 μm apart) to register a Ca2+ event in a 200 msec time window. If multiple Ca2+ events occurred within ~200 msec in neighboring cells, we retained only the events with highest peak $\DeltaF'(t)/F_{0}$ value. If two neighboring cells had correlation > 0.9 in their events, the cell with the lower average peak amplitude was discarded.

### Registration of cells across sessions

For each session we projected centroids of all thresholded filters onto a single image. We computed the spatial cross-correlation among the projections from all sessions to align them according to a reference session. Because changing the reference did not change the alignment output, we chose the first session as the reference. This step corrected slight translations and rotation changes between sessions and yielded each cell’s location in the reference coordinate system. Next, we searched for cells from different sessions that might be the same neuron. This was performed using two separate methods based on either spatial correlations or centroids distances (Figure 1—figure supplement 2). Figures 1 and 2, Figure 1—figure supplement 3, and Figure 2—figure supplements 2–6 show longitudinal data for which we used the spatial correlations-based registration method. Figure 2—figure supplement 5 shows longitudinal data for which we used the centroids distances-based registration method. Within each session, the nearest neighbors spatial correlations were always < 0.6 (Figure 1—figure supplement 2A,C) and the centroids distances were always > 6 μm (Figure 1—figure supplement 2B,D). Between sessions, however, a large amount of cell pairs had spatial correlations > 0.6 and centroid distances < 6 μm. Pairs with spatial correlation > 0.7 or distance < 5 μm were registered as the same neuron. In cases with more than one candidate, the cells with the minimal distance or maximal correlation were assigned to be the same neuron. Analyzing the data using a range of different thresholds demonstrated the robustness of our registration process to the choice of the threshold (Figure 2—figure supplement 5).

### Place fields

We analyzed mouse behavior videos using a custom MATLAB (Mathworks) routine that detected the mouse’s center of mass in each frame, calculated its velocity and applied a rectangular smoothing window of 250 msec. For place field analysis, we considered periods when the mouse ran >1 cm s−1. We divided each track into 24 bins (4 cm each) and excluded the last 2 bins at both ends of the tracks where water rewards were consumed and the mouse was generally stationary (Ziv et al., 2013). We computed the time spent in each bin, and the number of Ca2+ events per bin, and smoothed these two maps (‘occupancy’ and ‘Ca2+ event number’) using a truncated Gaussian kernel (σ = 1.5 bins, size = 5 bins). We then computed the place field map for each neuron by dividing the two smoothed maps of Ca2+ event number and occupancy. We separately considered place fields for left and right running directions and normalized each place field by its maximum value. We defined each place field's position at its peak value. For each place field with >5 events for a given session, we computed the spatial information (in bits per event) using the unsmoothed events-rate map of each cell, as previously described (Markus et al., 1994):

$$
Spatial Information=\sumip_{i}(r_{i}/r¯)log_{2}(r_{i}/r¯)
$$

Where ri is the Ca2+ event rate of the neuron in the ith bin; pi is the probability of the mouse being in the ith bin (time spent in ith bin/total session time); r̄ is the overall mean Ca2+ event rate; and i running over all the bins. We then performed 1000 distinct shuffles of animal locations during Ca2+ events, accounting for the spatial coverage statistics at the relevant session and direction, and calculated the spatial information for each shuffle. This yielded the p value of the measured information relative to the shuffles. Place fields with p ≤ 0.05 were considered significant.

### Population vector correlation

To determine the level of similarity between representations of the different environments, we calculated the mean population vector correlation between them (Leutgeb et al., 2005). For each spatial bin (excluding the last 2 bins at both ends of the tracks) we defined the population vector as the mean event rate for each neuron given that bin’s occupancy. We computed the correlation between the population vector in one environment with that of the matching location in the other environment, and averaged the scores over all positions. Since there are two edges to each of the two linear tracks there are two possible transformations between them. Therefore, we used the one that resulted in higher global population vector correlation.

### Statistical analysis

We generated the null hypothesis for place fields' displacements between a pair of days by taking the measured centers of place fields in the same environment on the two days and shuffling cells' identities on each of the days. We calculated the distribution of all displacements and averaged them over 10,000 distinct pairs of shuffles. Figure 1F shows the mean null hypothesis for the displacement curve found by averaging over all pairs of days for a given elapsed time. For the analyses shown in Figure 1G,H, and Figure 1—figure supplement 3A-E we used analysis of variance (ANOVA) with repeated measures. Greenhouse-Geisser estimates of sphericity were used for degrees of freedom adjustment.

### Time decoders

To capture the temporal information encoded in the hippocampal neural representations of different episodes we constructed three types of time decoders: (1) ordinal time decoder, (2) within-environment time decoder, and (3) across environments time decoder. The time decoders estimated the true order of the recording days from sets of eight episodes (sessions or trials) from the different days in the experiment. Decoding analyses were performed separately for five mice. Vectors of ensemble activity patterns were constructed where each element corresponded to the total number of events of one neuron within an episode. We notated the full-session ensemble activity pattern in day d in environment E as $V_{d}^{E}$, and the ensemble activity pattern in the tth trial on day d in environment E as $v_{d,t}^{E}$. To quantify the similarities between ensemble activity patterns of different episodes we calculated the Pearson correlation between the activity vectors. For the within and between environments time decoders, we normalized each correlation value between a test-data pattern and a training-data pattern by subtracting the average correlation of the training-data vector over all the vectors.

#### Ordinal time decoder

To sort shuffled, unlabeled activity patterns according to their ordinal positions (chronological order), we sought to maximize the average of all correlations between activity patterns taken on neighboring days in the shuffled test-data. This was achieved by calculating the average correlation between activity patterns for all 20,160 possible permutations of the eight recording days (8!/2) (see Figure 2—figure supplement 2A and Figure 2—figure supplement 5B). The decoder output the day-ordering that maximized the average correlation:

$$
O^({V_{i}^{E}}_{i=1:8})=argmax<d_{1},d_{2},d_{3}…d_{8}>\frac{1}{7}\sumj=17corr(V_{d_{j}}^{E},V_{d_{j+1}}^{E})
$$

Where $O^({V_{i}^{E}}_{i=1:8})$ is the inferred days order for a set of eight ensemble activity patterns in environment E, <d1,d2,d3...d8> is a possible ordering of the eight patterns, and $V_{i}^{E}$ is the ensemble activity pattern of the ith full-session in environment E (environment A, environment B, or both environments together).

To obtain the significance of the ordinal time decoder performance versus chance level, we divided the number of permutations with a mean correlation that is equal or greater than the mean correlation for the correct order by the total number of possible days’ permutations.

#### Within environment time decoder

Within environment time decoder inferred the time in which episodes (single trials) in one environment were recorded by comparing their ensemble activity patterns to the activity patterns in all the sessions from the same environment. Specifically, we calculated the normalized correlations between single-trial ensemble activity patterns in one environment (test-data) and each of the full-session activity patterns in all the sessions from the same environment (training-data). To evade bias, in addition to the exclusion of test trials from their sessions in the training-data, we also excluded the corresponding trials from the rest of the sessions in the training-data. Then, the decoder output the time of the session that maximized the correlation with the test-data:

$$
d^(v_{i,j}^{E})=argmaxdcorr(v_{i,j}^{E},V_{d}^{E}−v_{d,j}^{E})−Ed'corr(v_{d',j}^{E},V_{d}^{E}−v_{d,j}^{E})
$$

Where $d^(x)$ is the inferred day for ensemble activity pattern $x$, $Ed^{'}[·]$ is the average over all $d^{'}$, $v_{i,j}^{E}$ is the ensemble activity pattern in the jth trial of the ith day in environment E and $V_{i}^{E}$ is the ensemble activity pattern in the ith full-session in environment E. For the results presented in Figure 2—figure supplement 3 and 4 we applied the same decoder while excluding from the training-data the session from the day of the test-data.

#### Across environments time decoder

Across environments time decoder inferred the time in which episodes (trials or sessions) in one environment were recorded, by comparing their ensemble activity patterns to the activity patterns in all the sessions in the other environment. Decoding was done at the trial level as for the within environment time decoder. For across environments time decoder, decoding was done at the session level as well. Specifically, we calculated the normalized correlation between the full-session ensemble activity pattern in one environment (test-data) and the full-session activity patterns in all the sessions in the other environment (training-data). Then, the decoder output the time of the session that maximized the correlation with the test-data:

Trial-based:

$$
d^(v_{i,j}^{E_{1}})=argmaxdcorr(v_{i,j'}^{E_{1}} V_{d}^{E_{2}}−v_{d,j}^{E_{2}})−Ed'corr(v_{d',j'}^{E_{1}}V_{d}^{E_{2}}−v_{d,j}^{E_{2}})
$$

Session-based:

$$
d^(V_{i}^{E_{1}})=argmaxd corr(V_{i}^{E_{1}},V_{d}^{E_{2}})−Ed'corr(V_{d'}^{E_{1}},V_{d}^{E_{2}})
$$

Where $d^(x)$ is the inferred day for ensemble activity pattern $x$, $Ed'[·]$ is the average over all $d'$, $v_{i,j}^{E}$ is the ensemble activity pattern in the jth trial of the ith day in environment E and $V_{i}^{E}$ is the ensemble activity pattern in the ith full-session in environment E. For the results presented in Figure 2—figure supplement 3 we applied the same decoder while excluding from the training-data the session from the day of the test-data.

### Measures of divergence

We used two measures of divergence between the representations of the two environments: ‘activity divergence’ and ‘peak displacement’.

#### Activity divergence

The ratio of the average absolute difference in event rate between trials in different environments divided by the average absolute difference in average event rate between trials in the same environment:

$$
Activity Divergence(d)=\frac{<|r_{n,d,t}^{E}−r_{n,d,t'}^{E'}|>_{n,t,t'}^{D}}{<|r_{n,d,t}^{E}−r_{n,d,t'}^{E}|>_{n,t,t'}^{S}}
$$

where $r_{n,d,t}^{E}$ is the event rate of the nth cell in the tth trial of the dth day in environment E, $<·>^{D}_{n,t,t'}$ denotes the average over all cells and over all pairs of trials $(t and t')$ from different environments $(E and E')$, $<·>^{S}_{n,t,t^{'}}$ denotes the average over all cells and over all pairs of trials from the same environment and |x| denotes the absolute value of x. We modified this analysis from (Lever et al., 2002) to be suited for Ca2+ imaging data.

#### Peak displacement

The average distance between locations of peak activity in different environments:

$$
Peak Displacement(d)=<|p_{n,d}^{E}−p_{n,d}^{E^{'}}|>_{n}
$$

where $p_{n,d}^{E}$ is the location of the peak event rate of the $n^{th}$ cell in the $d^{th}$ day in environment $E$,$<·>_{n}$ denotes the average over all place cells from different environments $(E and E')$, and |x| denotes the absolute value of x (distance for 1-dimnesional environments). Note that there are two possible transformations between the two environments and here we used the one that resulted in higher global population vector correlation.

### Cell-level dynamics

To investigate cell-level dynamics we analyzed the changes in event rates over time for each cell. We applied these analyses separately for each of the two environments.

#### Maximal monotonic sequence

For each cell we calculated the difference in event rates between consecutive recording days, resulting in a sequence of seven difference values per cell. We then found the longest sub-sequence with the same trend (either monotonic increase or decrease in event rates) and compared the distribution of these lengths obtained from all cells to the distribution of lengths obtained from shuffled data (per-cell random permutation of the order of eight recording days).

#### Monotonicity score

In order to check whether single cells exhibit monotonic behavior that is obscured by noise we derived a more relaxed definition of monotonicity. For each cell we calculated the difference between the number of day-pairs in which the later had a higher event rate, and the number of day-pairs in which the earlier had a higher event rate, normalized by the total number of day-pairs (28). This resulted in a measure that ranges from -1 for monotonically decreasing cells and +1 for monotonically increasing cells.

#### Coefficient of variation (CV)

For the cells that were active in all the sessions (in one environment) we calculated the average and the standard deviation of event rates over all eight sessions in that environment. We then compared the distribution of event rates’ CV for those cells to the CV distribution of a population of simulated cells with equivalent average event rates that follow a stationary Poisson model of activity.

#### Population monotonicity

We aligned each cell’s activity to the day of its maximal event rate and normalized the activity of all days by the maximum event rate. Consequently, the obtained activity level in day-0 is 1 for all cells. Shuffled data was obtained by a per-cell random permutation of the order of eight recording days (Figure 2— figure supplement 1D). To separate the effect of event rate dynamics from cell recruitment dynamics we repeated this procedure for subgroups of cells according to the maximal number of consecutive days in which they were active (2–8 days). For each subgroup we extracted the maximal segment and computed the normalized event rates only for this segment (Figure 2— figure supplement 1E).
