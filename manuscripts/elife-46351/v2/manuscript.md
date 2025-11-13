# Replay as wavefronts and theta sequences as bump oscillations in a grid cell attractor network

## Authors

- Louis Kang<sup>1</sup> ([ORCID: 0000-0002-5702-2740](https://orcid.org/0000-0002-5702-2740)) †
- Michael R DeWeese<sup>1</sup>

### Affiliations

1. Redwood Center for Theoretical Neuroscience, Helen Wills Neuroscience Institute University of California, Berkeley Berkeley United States
2. Department of Physics University of California, Berkeley Berkeley United States

† Corresponding author

## Abstract

Grid cells fire in sequences that represent rapid trajectories in space. During locomotion, theta sequences encode sweeps in position starting slightly behind the animal and ending ahead of it. During quiescence and slow wave sleep, bouts of synchronized activity represent long trajectories called replays, which are well-established in place cells and have been recently reported in grid cells. Theta sequences and replay are hypothesized to facilitate many cognitive functions, but their underlying mechanisms are unknown. One mechanism proposed for grid cell formation is the continuous attractor network. We demonstrate that this established architecture naturally produces theta sequences and replay as distinct consequences of modulating external input. Driving inhibitory interneurons at the theta frequency causes attractor bumps to oscillate in speed and size, which gives rise to theta sequences and phase precession, respectively. Decreasing input drive to all neurons produces traveling wavefronts of activity that are decoded as replays.

## Introduction

The hippocampal region contains spatially tuned cells that generally encode an animal’s position in its spatial environment. Place cells in the hippocampal formation fire at one or a few locations (O'Keefe and Dostrovsky, 1971), and grid cells in the medial entorhinal cortex (MEC) fire at many locations that form a triangular lattice in space (Hafting et al., 2005). However, at short timescales, these neurons fire in coordinated sequences that represent trajectories away from the current animal position.

The first type of sequence occurs when the animal is moving and the local field potential (LFP) of the hippocampal region is dominated by an oscillation of 5–11 Hz, the theta range (Vanderwolf, 1969; O'Keefe, 1976; Vinogradova, 1995). During every cycle of this oscillation, neurons corresponding to locations slightly behind the animal fire first, followed by those corresponding to the current location and finally locations ahead of the animal (Skaggs et al., 1996; O'Neill et al., 2017). These so-called theta sequences involving many neurons are related to a single-neuron phenomenon called phase precession (O'Keefe and Recce, 1993; Hafting et al., 2008). When an animal first enters the firing field of a place or grid cell, the neuron spikes late in the theta cycle. As the animal moves through the field, subsequent spikes tend to arrive at smaller theta phase, or earlier within a cycle. Thus, activity within each theta cycle starts with neurons whose peak firing occurs behind the animal and ends with neurons whose peak firing occurs ahead of the animal, which is a theta sequence (Skaggs et al., 1996).

The second type of sequence occurs when the animal is idle and not moving, a state called quiet wakefulness or quiescence; it also occurs during slow wave sleep, which will not concern us here. During idle periods, the LFP of the hippocampal region loses theta oscillations but is instead intermittently punctuated by sharp-wave ripples with power across 140–200 Hz (Buzsáki, 1986; Chrobak and Buzsáki, 1996). During these events, spatially tuned neurons fire in coordinated bursts that represent rapid, long-distance trajectories. These replays are well-established in place cells (Lee and Wilson, 2002; Foster and Wilson, 2006) and have recently been observed in grid cells within superficial layers of the MEC (O'Neill et al., 2017). Note that replays can also involve grid cells within deep layers of the MEC (Ólafsdóttir et al., 2016); these findings, which have been disputed (Trimper et al., 2017), will not be addressed by this work.

Hippocampal experiments on theta sequences and replay have established a rich phenomenology, which includes their properties near branch points of a maze (Wu and Foster, 2014; Belchior et al., 2014), their modulation by reward history (Johnson and Redish, 2007; Wikenheiser and Redish, 2015a; Ambrose et al., 2016; Wu et al., 2017), their ability to predict future actions (Pfeiffer and Foster, 2013; Singer et al., 2013; Wikenheiser and Redish, 2015b; Xu et al., 2019), and their potential role in disease pathogenesis (Middleton et al., 2018). These findings suggest that hippocampal sequences facilitate many cognitive functions, such as memory consolidation, credit assignment, and action planning (Foster, 2017; Ólafsdóttir et al., 2018; Zielinski et al., 2018). However, the mechanisms that produce theta sequences and replay among place and grid cells are still unclear.

Meanwhile, a mechanism for producing grid cells themselves, the continuous attractor model, has been accumulating experimental support (Couey et al., 2013; Yoon et al., 2013; Heys et al., 2014; Dunn et al., 2015; Fuchs et al., 2016; Zutshi et al., 2018; Gu et al., 2018). This class of networks posits particular configurations of synapses within the MEC that are local and symmetric (Burak and Fiete, 2009; Widloski and Fiete, 2014). By incorporating key biological features such as fully spiking neural dynamics, we find that new phenomena emerge in this recurrent architecture: grid cells will exhibit either theta sequences or replays depending on the external input provided by other brain regions. These inputs correspond to experimentally measured changes between active and inactive behavior (Steriade et al., 2001; Simon et al., 2006) and do not involve changes in connectivity. From this perspective, the same architecture that produces grid cells causes them to participate in sequences that may be leveraged by other brain regions, such as the hippocampus, to pursue desired cognitive goals.

## Results

### Our fully spiking continuous attractor model produces grid cells

We first describe our implementation of a continuous attractor network and demonstrate that it reproduces classic grid responses when a simulated animal explores a 2D open field. Model details are provided in Materials and methods and Table 1. We simulate a single grid module—that is, grid cells of one scale and orientation (Stensola et al., 2012)—with a continuous attractor network based on Burak and Fiete (2009) and Widloski and Fiete (2014). Neurons are assembled in a 2D sheet with five overlapping populations, of which four represent excitatory principal cells and one represents inhibitory interneurons (Figure 1A). Each excitatory neuron excites its neighbors across all populations, and each inhibitory neuron inhibits only excitatory neurons located a certain distance away. We will address the purpose of having four slightly different excitatory populations shortly.

**Table 1.**
 Main model parameters and their values unless otherwise noted.Values that change between runs, idle periods, and allocentric corrections are indicated accordingly.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Variable</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Neurons per population</td>
      <td>n×n</td>
      <td>232×232</td>
    </tr>
    <tr>
      <td>Simulation timestep</td>
      <td>Δ⁢t</td>
      <td>1 ms</td>
    </tr>
    <tr>
      <td>Exc. membrane time constant</td>
      <td>τm+</td>
      <td>40 ms</td>
    </tr>
    <tr>
      <td>Inh. membrane time constant</td>
      <td>τm-</td>
      <td>20 ms</td>
    </tr>
    <tr>
      <td>Exc.-to-exc. synaptic delay</td>
      <td>τs++</td>
      <td>5 ms</td>
    </tr>
    <tr>
      <td>Exc.-to-inh. synaptic delay</td>
      <td>τs-+</td>
      <td>2 ms</td>
    </tr>
    <tr>
      <td>Inh. synaptic delay</td>
      <td>τs-</td>
      <td>2 ms</td>
    </tr>
    <tr>
      <td>Exc. drive maximum</td>
      <td>amax+</td>
      <td>{2.0runs1.6idle2.0allo.</td>
    </tr>
    <tr>
      <td>Exc. drive minimum</td>
      <td>amin+</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>Exc. drive scaled spread</td>
      <td>ρa+</td>
      <td>{1.2runs0.9idle</td>
    </tr>
    <tr>
      <td>Inh. drive magnitude</td>
      <td>amag-</td>
      <td>{0.72runs0.0idle0.72allo.</td>
    </tr>
    <tr>
      <td>Inh. drive theta amplitude</td>
      <td>ath-</td>
      <td>{0.2runs0idle0allo.</td>
    </tr>
    <tr>
      <td>Inh. drive theta frequency</td>
      <td>f</td>
      <td>8 Hz</td>
    </tr>
    <tr>
      <td>Exc. synaptic strength</td>
      <td>wmag+</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Exc. synaptic spread</td>
      <td>rw+</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Inh. synaptic strength</td>
      <td>wmag-</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td>Inh. synaptic distance</td>
      <td>rw-</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Exc. synaptic shift</td>
      <td>ξ</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Exc. velocity gain</td>
      <td>α</td>
      <td>0.25 s/m</td>
    </tr>
    <tr>
      <td>Exc. noise magnitude</td>
      <td>Var[ζP(r,t)]</td>
      <td>0.0022</td>
    </tr>
    <tr>
      <td>Inh. noise magnitude</td>
      <td>Var[ζ−(r,t)]</td>
      <td>0.0022</td>
    </tr>
  </tbody>
</table>

![Figure 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig1-v2.jpg)

**Figure 1.:** (A) Our model consists of a neural sheet with five overlapping populations, four of them excitatory—N, W, S, and E—and one inhibitory. Each density plot depicts the synaptic outputs in the sheet of a neuron at the origin. (B) Each neuron is driven to a particular membrane potential, which exceeds the spiking threshold for excitatory neurons at the center of the sheet and oscillates at 8 Hz for inhibitory neurons while the animal is running. (C) Snapshot of neural activity showing S and inhibitory populations separately; other excitatory populations have activity patterns similar to that of the S population. Each pixel is a neuron and dark colors indicate recent spiking. (D) Left, segment of a 2D open field trajectory. Right, neural activity over the course of the segment with each neuron colored according to the position at which it attained its maximum firing rate. Each attractor bump moves in synchrony with animal motion. (E) Left, two sample grid cells with spikes shown as colored dots superimposed on the animal’s trajectory. Each neuron’s location in the sheet is indicated by a circle of corresponding color in D. Right, autocorrelation of rate maps calculated from spikes at left. Black scale bars, 50 neurons. White scale bars, 50 cm.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Spatial firing maps for a 2D open field trajectory. Twenty grid cells are selected from the simulation depicted in Figure 1D,E across all four excitatory populations. For each grid cell, spikes superimposed on the animal’s trajectory (left) and autocorrelation of rate maps calculated from spikes (right).

To accurately simulate rapid sequences of spikes, we implement fully spiking grid cells that obey leaky integrate-and-fire dynamics. Each neuron has a membrane potential that tends toward a steady-state value called the drive, which represents a combination of resting potential and broad input from other brain regions (Figure 1B). If the potential exceeds a threshold of 1 in arbitrary units, a spike is emitted, the potential is reset to 0, and the neuron’s targets experience a postsynaptic jump in potential after a brief synaptic delay. During locomotion, excitatory principal cells are driven to fire by various cortical and subcortical inputs (Kerr et al., 2007; Bonnevie et al., 2013). Thus, their drive exceeds threshold at the center of the neural sheet; it decays towards the edges to avoid edge effects that disrupt continuous attractor dynamics (Burak and Fiete, 2009). Meanwhile, inhibitory interneurons have subthreshold drive that oscillates at a theta frequency of 8 Hz due to input from the medial septum (Brandon et al., 2011; Koenig et al., 2011; Gonzalez-Sulser et al., 2014; Unal et al., 2015). With this architecture and random initial membrane potentials, the neural sheet naturally develops local regions of activity, called bumps, that are arranged in a triangular lattice and are coherent across populations (Figure 1C and Figure 1—video 1). This self-organized grid is an attractor state of the network.

How do we produce neurons with grid-like spatial tuning from the grid-like activity pattern on the neural sheet? This transformation is performed by the four excitatory populations, each of which corresponds to a perpendicular direction along the neural sheet and a perpendicular direction in the spatial environment. Excitatory neurons have output synapses biased in their preferred sheet direction (Figure 1A), and they receive more input when the animal moves along their preferred spatial direction. When the animal moves along, say, the 'North' direction, neurons in the N population have increased drive; since their outputs are biased in the 'up' direction on the neural sheet, the activity pattern moves up. In this way, the activity pattern on the sheet moves synchronously with the animal’s 2D trajectory (Figure 1D), and the grid pattern is projected onto single neuron spatial responses (Figure 1E and Figure 1—video 2). Each active neuron in the sheet is a grid cell with the same scale and orientation (Figure 1—figure supplement 1).

### Grid cells are spatially tuned and theta-modulated along a linear track

For the rest of the paper, we simulate 1D trajectories consisting of runs along a linear track separated by idle periods at either end (Figure 2A). As in the 2D case, attractor bumps on the neural sheet move synchronously with animal motion. But over the course of a simulation, the grid-like pattern on the neural sheet drifts (Burak and Fiete, 2009) such that for a given track position, the corresponding bump locations on the neural sheet slowly change. This drift introduces errors in path-integration (Hardcastle et al., 2015), which are believed to be corrected by allocentric input from border cells (Ocko et al., 2018; Keinath et al., 2018), boundary vector cells (Evans et al., 2016), or landmark cells (Raudies and Hasselmo, 2015; Savelli et al., 2017). Thus, we implement brief allocentric corrections in our model. Attractor bump locations on the neural sheet that correspond to either end of the track are learned during simulation setup. They are periodically reintroduced during the main simulation as excitatory input between idle periods and runs (Figure 2A,B; see Materials and methods). In Appendix 2, we present a version of our model without allocentric corrections that still demonstrates many of our results, though to a weaker degree.

![Figure 2.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig2-v2.jpg)

**Figure 2.:** (A) Trajectory consisting of runs along a track separated by idle periods at either end. Between the end of an idle period and the start of a run, the network receives brief allocentric input. (B) Allocentric input corrects the location of attractor bumps on the neural sheet (Materials and methods). (C) Left, track diagram. Right, neural activity over runs with each neuron colored according to the track position at which it attained maximum firing rate. Red circles indicate regions of recording. Scale bar, 50 neurons. (D) Firing fields of recorded grid cells sorted by position of maximum rate. (E) Multiunit activity of neurons in D averaged over theta cycles, which span from one trough of the oscillating inhibitory drive to the next. Data is repeated over two cycles for clarity.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Firing fields of recorded grid cells along a 1D track. Fields are sorted by position of maximum rate. (A) Representative simulations exhibiting one field. (B) Representative simulations exhibiting two fields.

Grid cells at different locations in the sheet generally correspond to different positions along the track (Figure 2C). From four regions in the sheet chosen for recording, we select up to 150 excitatory neurons whose spatial firing fields are stable from lap to lap and collectively tile the track (Figure 2D; Materials and methods). Over replicate simulations with different random initial membrane potentials, many simulations contain only grid cells with single fields as in Figure 2D. In other replicates, the attractor grid self-organizes on the neural sheet with an orientation such that two attractor bumps pass over recorded neurons and produce two fields (Figure 2—figure supplement 1; Appendix 1). All of our single-simulation examples presented below in the main text correspond to the simulation depicted in Figure 2D that exhibits single fields. Similarly, the grid cells in O'Neill et al. (2017), with which we will primarily compare our results, often possess a single dominant field along an arm of a T-maze. However, both types of simulations contribute to our results, and we will provide examples for simulations exhibiting two fields in our figure supplements.

At the theta timescale, grid cell activity is highest when the oscillating inhibitory drive is lowest and excitatory cells are most disinhibited (Figure 2E). This observation allows us identify theta phases in our simulations with those defined through LFP measurements. Experimentally, grid cells (Hafting et al., 2008) and place cells (Buzsáki, 2002; Feng et al., 2015) are most active at troughs of the theta-filtered LFP, which can be explained in terms of extracellular currents generated by neural activity (Buzsáki et al., 2012). O'Neill et al. (2017) define theta cycles to span from trough to trough of the LFP. Accordingly, we align our theta cycles to start with phase 0° at troughs of the inhibitory drive (Figure 2E).

### Theta phase precession arises from oscillations in attractor bump size

#### Phase precession results

During runs, activity passes through recorded neurons as attractor bumps move along the neural sheet (Figure 3A, Figure 3—figure supplement 1, and Video 1). However, spike trains from single neurons exhibit finer temporal organization with respect to the theta oscillation in a variety of ways (Figure 3B, Figure 3—figure supplement 2, and Figure 3—figure supplement 3). Many neurons are phase-independent and fire throughout the theta cycle. Some are phase-locking and strongly prefer to fire at 360° (equivalently, 0° or 720°). Finally, some exhibit phase precession with a preferred phase that starts around 360° when the animal enters a grid field but decreases as the animal progresses through it.

![Figure 3.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-v2.jpg)

**Figure 3.:** (A) Grid cell spike rasters for four laps along the track. Vertical blue lines indicate theta cycle boundaries. (B) Relationship between animal position along the track and theta phase for representative neurons. Dots represent spikes during runs in the directions indicated by arrows, with each spike repeated at two equivalent phases for clarity. Lines indicate fit by circular-linear regression. Numbers in each panel from top left to top right indicate magnitudes of correlation coefficients, regression fit scores, and regression slopes. (C–E) Data across all replicate simulations. (C) Magnitudes of circular-linear correlation coefficients. Mean ± s.d.: 0.17 ± 0.11. (D) Fit scores for circular-linear regression. (E) Regression slopes in units of field size for neurons with fit score >0.4. The predominance of negative values for rightward runs and positive for leftward runs indicates decreasing phase as the animal traverses grid fields in either direction. (F) Spike densities for different subgroups. An animal enters a grid field at progress 0% and exits it at 100%.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Vertical blue lines indicate theta cycle boundaries. (A) Representative simulation exhibiting one field. (B) Representative simulation exhibiting two fields.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Relationship between animal position along the track and theta phase during rightward runs. Dots represent spikes during runs in the directions indicated by arrows, with each spike repeated at two equivalent phases for clarity. Lines indicate fit by circular-linear regression. Numbers in each panel from top left to top right indicate magnitudes of correlation coefficients, regression fit scores, and precession ranges. (A) Representative neurons from simulations exhibiting one field. (B) Representative neurons from simulations exhibiting two fields.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Relationship between animal position along the track and theta phase during leftward runs. Panels same as in Figure 3—figure supplement 2.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Further analysis of subgroups of phase-independent, phase-locking, and phase-precessing neurons. (A,B) Distributions of regression slopes using a fit score cutoff different from 0.4, which was used in Figure 3. (C) Neural sheet locations of neurons belonging to each subgroup for the simulation described in Figure 3A,B. Data encompassing recording areas shown in Figure 2C and recording areas offset by 45° on the neural sheet. Left, track diagram. Right, neural activity over runs with each neuron colored according to the track position at which it attained maximum firing rate. Scale bar, 50 neurons. (D–G) Distribution of neurons in each subgroup with respect to various properties. Medians for each subgroup indicated by dashed lines. Medians for phase-locking and phase-precessing subgroups compared by the Mann-Whitney U test with reported p-value. (D) Mean firing rate. (E) Distance from the center of the neural sheet divided by the half the neural sheet size n. (F) Angle on the neural sheet relative to the right direction, or $+𝐱^$. (G) Location relative to attractor bumps in units of relative firing rate. A value of 1 means that the center of a bump passes over the neuron, and a value of 0 means that no part of a bump passes over the neuron (Appendix 1).

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** Box-whisker plots with lines at medians, boxes between first to third quartiles, and whiskers between the entire data range excluding outliers lying more than 1.5 times the interquartile distance beyond the first or third quartile. Medians compared by the Mann-Whitney U test with reported p-values. (A–F) Analysis of phase relationships with respect to excitatory population. For these simulations, the direction of animal velocity is 0°, which means that runs are aligned to the E and W directions. The ‘along’ category corresponds to both the E population when the animal is running towards E and the W population when the animal is running towards W. The ‘against’ category corresponds to the E and W populations during the opposite running directions. The ‘perp.’ category corresponds to the N and S directions. (A) Number of valid recorded neurons. Note that there are very few ‘against’ neurons due to low firing rate, and this category is excluded from further analysis. (B) Number of spikes per neuron. (C) Magnitude of correlation coefficient. (D) Fraction of phase locking neurons. (E) Fraction of phase precessing neurons. (F) Phase precession range. (G–J) Analysis of phase relationships with respect to number of fields exhibited by a simulation. (G) Magnitude of correlation coefficient. (H) Fraction of phase locking neurons. (I) Fraction of phase precessing neurons. (J) Phase precession range.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** Correlation coefficient magnitude, precession range, fraction of phase-locking neurons, and fraction of precessing neurons as functions of various simulation parameters. Points at mean values with bars indicating s.d. over replicate simulations. Small horizontal offsets added for clarity. (A) Animal speed and track orientation relative to the E direction, or $+𝐗^$. (B) Excitatory drive and recording distance from the center of the neural sheet divided by the half the neural sheet size.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** Same as Figure 3—figure supplement 6, except as functions of different parameters. (A) Inhibitory theta amplitude and inhibitory drive. (B) Inhibitory and excitatory membrane time constants.

![Video 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-video1.mp4.jpg)

**Video 1.:** Left, position of the animal (black square) along a 1D track. Right, neural activity of the E population. Each pixel is a neuron, with black corresponding to current spikes and lightest gray corresponding to spikes 40 ms ago. Red circles indicate regions of recording.

We first quantify these relationships using circular-linear correlation (Equation 13), which indicates whether theta phase changes with position (Kempter et al., 2012). Our correlation magnitudes 0.17 ± 0.11 (mean ± s.d.; Figure 3C) are low compared to experiments, which report grid cells with mean ≈0.3 and place cells with mean ≈0.4 (O'Neill et al., 2017). This difference arises from two sources. Figure S10 of O'Neill et al. (2017) shows some highly correlated neurons with magnitudes up to 0.8; these are absent from our simulations. It also shows fewer neurons with correlation value close to 0, which corresponds to either phase-independent or phase-locking neurons. Since both subgroups lack a preferred theta phase that consistently changes with position, circular-linear correlation cannot distinguish between them (Figure 3B, top two rows).

To further characterize phase behavior, we use circular-linear regression (Kempter et al., 2012), which can differentiate between all three subgroups of phase relationships presented in Figure 3B. Phase-independent neurons are defined to have a regression fit score less than a cutoff of 0.4 (Figure 3D; Equation 11). Neurons with high fit score are then distinguished as either phase-locking or precessing by the absolute value of their regression slope in units of field size, which is called the phase precession range (Figure 3E). We use a range of 60° as the cutoff. Experimentally, phase-locking and precessing neurons are found in Layers III and II (LIII and LII), respectively (Hafting et al., 2008). A wide variety of phase precession ranges are reported across subtypes of LII neurons with medians spanning from 50° for pyramidal cells (Ebbesen et al., 2016) to 170° for stellate cells (Reifenstein et al., 2016). Our cutoff is close to the lower limit of this span. Yet, regardless of the cutoff value, regression slopes are biased towards negative values for rightward laps and positive values for leftward laps, which means that the preferred firing phase tends to decrease as an animal moves through a grid field. This directional tendency is a key biological feature of phase precession seen experimentally (Hafting et al., 2008), and it is also maintained for other cutoff values applied to the fit score (Figure 3–Figure Supplement 4A,B).

We also construct spike density plots using all neurons in each subgroup (Figure 3F). These plots show that phase-locking neurons have a preferred phase around 360° throughout the field and that phase-precessing neurons have a preferred phase also around 360° at field entry. This value corresponds to theta troughs when excitatory neurons are most disinhibited (Figure 2E) and matches measurements for LIII and LII neurons (Hafting et al., 2008; note that their phase convention differs from ours by 180°). More detailed features also seem to agree between phase-precessing neurons in our simulations and LII neurons in experiments. First, the peak density decreases by ≈75° over the first 50% of field progress, and second, there is a smaller density at around 60% field progress and 140° theta phase (Figure 3F; Hafting et al., 2008). This second density has been separately related to bursting (Climer et al., 2013) and a second source of neural input (Yamaguchi et al., 2002; Chance, 2012); further investigation is required to reconcile these assertions with its origin in our model.

The dependence of phase behavior on simulation features and parameters is explored in detail in the figure supplements of Figure 3. We will briefly list a few key results interspersed with experimental findings that support them. Phase precession statistics do not depend on the direction of animal motion (Figure 3–Figure Supplement 5E,F); in experiments, Climer et al. (2013) report omnidirectional precession in a 2D environment. Precession range and correlation magnitude increase with animal speed (Figure 3–Figure Supplement 6A, p = 0.002 and 0.0006 for precession range and correlation magnitude, respectively, by pooling data across track orientations and applying the Krushal-Wallis H test); in experiments, Jeewajee et al. (2014) report that faster motion is associated with steeper precession slopes and higher correlation magnitudes (Figure 3a, results for pdcd, which corresponds to field progress defined in this paper).

To summarize our phase precession results, our simulation produces a subgroup of phase-locking neurons akin to MEC LIII neurons and a subgroup of phase-precessing neurons akin to MEC LII neurons. Further consideration of correlation coefficients and precession ranges, with connections to measurements, will be provided in the Discussion.

#### Attractor bump oscillations explain phase precession

We can understand the emergence of phase precession through the effect of oscillating inhibitory drive on attractor bumps. Higher inhibitory drive suppresses the activity of the excitatory grid cells and decreases the size of bumps (Figure 4A,B). Imagine we record from a single neuron as a bump of activity moves through it on the neural sheet. As an attractor bump moves, its size oscillates with inhibitory drive (Figure 4C, top, and Figure 4—video 1). The activity bump will most likely first reach the grid cell when it is large and growing in size, which corresponds to the end of the theta cycle when the inhibitory drive is decreasing towards its lowest point. Thus, as an animal enters a grid field, the first spike will likely have large theta phase slightly less than 360°. During the next theta cycle, the center of the bump has moved closer to the neuron, so the edge of the bump will reach the neuron when it is growing in size but not as large. Thus, the next spike will have slightly smaller theta phase. This is the origin of phase precession in our model. We continue generating spikes with simplified dynamics in which the neuron fires when it is contained within the bump, but there is a 40 ms refractory period corresponding to membrane potential building up towards threshold after it is reset. This procedure represents one lap along the track at constant velocity.

![Figure 4.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig4-v2.jpg)

**Figure 4.:** (A,B) Data from simulations with fixed inhibitory drive and constant animal velocity. (A) Snapshots of neural activity. Scale bar, 50 neurons. (B) The diameter of bumps on the neural sheet decreases linearly with inhibitory drive (linear regression $R^{2}=0.90$, ANOVA $p∼10^{-9}$). (C) Phase precession in a conceptual model with bump size oscillations. We imagine an attractor bump, with size oscillations described by B, passing through a recorded grid cell. Top, a single lap. The recorded neuron is at location 0 and fires a spike (black dot) whenever contained within the bump (gray area), subject to a 40 ms refractory period. Bottom, relationship between theta phase and time across multiple laps with different initial phases. Spikes occur around 360° (equivalently, 0°) at the start of the field, and their phase generally decreases with time within in the grid field. (D) Attractor bump shape at different theta phases averaged over theta cycles and individual bumps (Appendix 1). Grays scaled separately for each theta phase. Scale bar, three neurons. (E,F) Phase behavior in a simplified model using average bump dynamics. (E) We imagine the average attractor bump passing through a recorded grid cell. Top, a single lap. The recorded neuron is at location 0 and stochastically fires a spike (black dot) with rate proportional to bump activity, subject to a 40 ms refractory period. Bottom, relationship between time and theta phase across multiple laps with different initial phases. (F) Relationship between time and theta phase using average bumps whose activity has been rescaled to different maximum values: 40, 50, and 100 spikes/s. Dots represent spikes generated according to E. Lines indicate fit by circular-linear regression. Numbers in each panel from top left to top right indicate magnitude of correlation coefficient, regression fit score, and regression slope.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Simplified model of phase precession using average bump dynamics. Bump activity is rescaled to different maximum values. (A–D) Neurons exhibit phase locking under low bump activity with maximum value 40 spikes/s. Statistics from 1000 neurons simulated according to Figure 4E. (A) Relationship between animal position along the track and theta phase for representative neurons. Dots represent spikes. Lines indicate fit by circular-linear regression. Numbers in each panel from top left to top right indicate magnitude of correlation coefficient, regression fit score, and regression slope. (B) Magnitudes of circular-linear correlation coefficients. (C) Fit scores for circular-linear regression. (D) Regression slopes for neurons with fit score >0.4. (E–H) Neurons exhibit phase precession under medium bump activity with maximum value 50 spikes/s. Panels same as A–D. (I–K) Neurons exhibit phase independence under high bump activity with maximum value 100 spikes/s. Panels same as A–C.

We represent additional laps by performing the same simplified procedure as above, but with different shifts in theta phase, since the animal does not always enter the grid field at the same initial phase. Spikes accumulated across laps show phase precession (Figure 4C, bottom), though the effect is strongest at the beginning of the field. In the middle of the field, spikes still precess, but they cluster around values of both 360° and 180°. At the end of the field, a few spikes even precess in the opposite direction, increasing in phase with time. Thus, bump oscillations alone can explain the direction of phase precession and the preferred phase at field entry, but spike phases do not decrease perfectly linearly with progress through the field.

To analyze attractor bump oscillations more precisely, we calculate the average bump shape as a function of theta phase (Figure 4D and Figure 4—video 2; Appendix 1). We now imagine that this average bump passes multiple times through a recorded neuron whose spiking probability is proportional to bump activity (Figure 4E). Each instance of this stochastic process produces a phase-locking, phase-precessing, or phase-independent neuron. By explicitly rescaling the activity of the average bump without otherwise changing its time-varying shape, we can generate neurons enriched in one of these phase relationships (Figure 4F and Figure 4—figure supplement 1). Under high activity, neurons are driven to fire across all theta phases and exhibit phase independence. Under low activity, neurons only fire during the most permissive theta phase and exhibit phase locking at 360°. Under intermediate levels of activity, neurons can respond to oscillations in bump size as demonstrated in Figure 4C and exhibit phase precession.

This finding on how activity level influences phase behavior is supported by the experimental report that higher spike counts are associated with steeper precession slopes (Jeewajee et al., 2014, Figure 3b, results for pdcd, which corresponds to field progress defined in this paper). Our main model also reflects this finding: neurons with low, medium, and high firing rates have increased likelihoods for phase locking, precession, and independence (Figure 3–Figure Supplement 4D). Thus, the heterogeneous phase behaviors observed in our main simulations arise, at least in part, from heterogeneous levels of bump activity. Three factors that determine the level of activity experienced by a neuron are its distance to the center of the neural sheet, its sheet location relative to attractor bumps, and its preferred firing direction relative to animal motion. Accordingly, the prevalence of different phase behaviors varies with these factors (Figure 3–Figure Supplement 4E,G and Figure 3–Figure Supplement 5B,D).

### Theta sequences arise from oscillations in attractor bump speed

Next, we use the firing fields illustrated in Figure 2D to decode the animal’s position from the population activity presented in Figure 3A (Materials and methods). The decoded position generally matches the animal’s actual position (Figure 5A and Figure 5—figure supplement 1), but at the theta timescale, there are deviations whose regularities are revealed by averaging over theta cycles.

![Figure 5.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig5-v2.jpg)

**Figure 5.:** (A) Decoded position for four laps along the track corresponding to Figure 3A. Vertical blue lines indicate theta cycle boundaries. (B) Decoded position shifted by actual position and averaged over theta cycles. The thick black fit line indicates the time window with the steepest increase in decoded position. Vertical thin black lines indicate theta cycle boundaries. (C) Mean actual run speed (error bars indicate s.d. over time) and mean theta sequence speed, as indicated by the slope of the thick black line in B (error bars indicate s.d. over replicate simulations). (D) Difference between the maximum likelihood decoded position from B and the actual animal position as a function of time. Within each theta cycle, the segment from the smallest to the largest value is emphasized as a theta sequence.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Decoded position over multiple runs corresponding to Figure 3—figure supplement 1. Vertical blue lines indicate theta cycle boundaries. Orange line indicates the actual animal trajectory. (A) Representative simulation exhibiting one field. (B) Representative simulation exhibiting two fields.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Vertical black lines indicate theta cycle boundaries. (A) Representative simulations exhibiting one field. (B) Representative simulations exhibiting two fields.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Theta sequence speed divided by mean actual speed for different numbers of fields and parameter values. (A) Dependence of theta speed on number of fields. Box-whisker plot with line at medians, box between first to third quartiles, and whiskers between the entire data range excluding outliers lying more than 1.5 times the interquartile distance beyond the first or third quartile. p-value calculated by the Mann-Whitney U test. (B–E) Theta sequence speed divided by mean actual speed as a function of various simulation parameters. Points at mean values with bars indicating s.d. over replicate simulations. (B) Animal speed and track orientation relative to the E direction, or $+𝐗^$. (C) Excitatory drive and recording distance from the center of the neural sheet divided by the half the neural sheet size. (D) Inhibitory theta amplitude and inhibitory drive. (E) Inhibitory and excitatory membrane time constants.

To do so, we take quadruplets of consecutive theta cycles, ignoring those whose decoded positions are close to the ends of the track and reversing those corresponding to right-to-left motion (Materials and methods). We align the decoded positions with respect to the actual position of the animal midway through each theta quadruplet, and we average these shifted decoded positions over theta quadruplets. This average decoded trajectory generally increases across the quadruplet, corresponding to the animal’s actual forward motion (Figure 5B and Figure 5—figure supplement 2). However, within each theta cycle, the decoded position increases rapidly, before retreating at cycle boundaries. We identify these forward sweeps as theta sequences, which represent motion at 0.88 ± 0.15 m/s, approximately twice the actual speed of 0.50 ± 0.05 m/s (mean ± s.d.; Figure 5C). This matches experimental observations of average theta sequence speed ≈1 m/s compared to the animal’s speed of ≈0.4–0.5 m/s (O'Neill et al., 2017). We also illustrate these sequences by comparing the maximum likelihood decoded position and the actual position as a function of time (Figure 5D). Averaged over theta cycles, the decoded position lags behind the actual position at cycle boundaries and then advances ahead of it midcycle.

Theta sequences, like phase precession, arise naturally in our model from an effect of oscillating inhibitory drive on attractor bumps. In addition to determining bump size, inhibitory drive also affects the speed at which bumps move along the neural sheet—higher inhibitory drive produces faster bump motion for a given animal speed (Figure 6A,B). At the middle of theta cycles, inhibitory drive is highest, so attractor bumps move quickly and represent fast animal trajectories. These theta sequences are faster than the animal’s actual speed, which is approximately constant within a theta cycle and thus encoded as the average bump speed over the entire cycle. We can also see the origin of theta sequences directly from the average dynamics of attractor bumps (Figure 4D, Figure 6C, and Figure 4—video 2). The location of peak activity moves with a sawtooth-like pattern that, over a theta cycle, lags behind the overall motion of the bump and advances ahead of it (Figure 6D). These forward surges produce the sequences in decoded position (Figure 5D).

![Figure 6.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig6-v2.jpg)

**Figure 6.:** (A,B) Data from simulations with fixed inhibitory drive and constant animal velocity. (A) Snapshots of neural activity. Scale bar, 50 neurons. (B) The speed of bumps on the neural sheet increases linearly with inhibitory drive (linear regression $R^{2}=0.91$, ANOVA $p∼10^{-9}$). Thus, the average decoded position in Figure 5B advances most rapidly around the middle of the theta cycle. (C) Activity of the average attractor bump depicted in Figure 4D along its central axis. (D) Top, peak activity location from C as a function of time. Bottom, peak activity position relative to constant bump motion as a function of time. Within each theta cycle, the segment from the smallest to the largest value is emphasized and corresponds to a theta sequence in Figure 5D.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Attractor bump size and speed are not generally correlated over changes in multiple simulation parameters, but both are negatively correlated with the amount of inhibition produced by inhibitory neurons. (A) Legend for simulations with fixed inhibitory drive. Each simulation is performed at different values of inhibitory drive $a_{mag}^{-}$, inhibitory synaptic strength $w_{mag}^{-}$, and inhibitory membrane time constant $\tau_{m}^{-}$. Other parameters are set at the values used for main simulation runs (Table 1). (B–F) Relationships between pairs of attractor bump properties across parameters displayed in A. Rank correlation computed by Spearman’s $ρ$ with p-values indicated. Attractor bump properties are diameter, speed, the multiunit activity of inhibitory neurons (inhibitory MUA), and a metric for the amount of inhibition produced by inhibitory neurons ($inhibitory MUA\timesw_{mag}^{-}$). Note that B indicates no overall correlation between bump size and speed, but increasing $a_{mag}^{-}$ (following blue–cyan–green) increases bump speed and decreases bump diameter, as seen in Figure 4B and Figure 6B.

Our model’s mechanism for theta sequences can explain why their speed is roughly twice the actual speed, as observed experimentally (O'Neill et al., 2017). Suppose the theta oscillation spends roughly the same amount of time at its peaks, when attractor bumps move at maximal speed, and at its troughs, when bumps do not move at all. Then, the average bump speed, which encodes the actual animal speed, is half the maximal bump speed, which encodes the theta sequence speed. Indeed, simulations whose grid cells contain two fields, whose track is oriented differently, whose trajectory is faster or slower, or whose parameters are chosen differently all have theta sequence speeds between 1.2 and 2.5 times the actual speed (Figure 5—figure supplement 3).

### Replay arises from traveling wavefronts of activity

We now simulate idle periods at either end of the track. We would like to know how external inputs to the MEC change at transitions between active and quiescent states, but these measurements have not been performed to our knowledge. Thus, we instead adapt experimental findings taken during slow wave sleep, which resembles the quiescent state in many behavioral and electrophysiological ways (Buzsáki, 1996). The neocortex, which activates MEC principal cells, is broadly less active during slow wave sleep (Steriade et al., 2001), and the medial septum, which inhibits MEC interneurons, increases its firing rate while losing most of its oscillatory nature (Simon et al., 2006). We model these effects respectively as decreased excitatory drive and decreased inhibitory drive without oscillations (Figure 7A). The network rapidly switches between these inputs and those of Figure 1B, which represent the active state, as the animal transitions between quiescence and runs.

![Figure 7.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig7-v2.jpg)

**Figure 7.:** (A) During idle periods at either end of the track, excitatory and inhibitory drives decrease, and the latter no longer oscillates. (B) Snapshot of neural activity showing S and inhibitory populations separately. Red circles indicate regions of recording. Scale bar, 50 neurons. (C) Grid cell spike rasters for four idle periods. (D) Decoded position corresponding to C. Rapid trajectory sweeps arise from traveling wavefronts as depicted by the S population in B. (E) Replays from one simulation with cyan fit lines. (F) Number of replays across simulations. (G) Mean actual run speed (error bars indicate s.d. over time) and mean replay speed, as indicated by the slopes of cyan lines in E (error bars indicate s.d. over replays).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Representative simulation exhibiting one field. (B) Representative simulation exhibiting two fields.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** Decoded position over multiple idle periods corresponding to Figure 7—figure supplement 1. (A) Representative simulation exhibiting one field. (B) Representative simulation exhibiting two fields.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Replays with cyan fit lines. (A) Representative replays from simulations exhibiting one field. (B) Representative replays from simulations exhibiting two fields. Note that two or three parallel lines participate in the fit (Appendix 1).

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** (A–D) Dependence of replay count and speed on number of fields. Box-whisker plot with line at medians, box between first to third quartiles, and whiskers between the entire data range excluding outliers lying more than 1.5 times the interquartile distance beyond the first or third quartile. p-value calculated by the Mann-Whitney U test. (A) Replay count. (B) Replay speed divided by mean actual speed. (C,D) Same as A,B, but we detect replays in simulations exhibiting two fields with the same method used for single fields. (E–H) Replay count and replay speed divided by mean actual speed as functions of various simulation parameters. Points at mean values with bars indicating s.d. over replicate simulations. (E) Velocity gain and animal speed. (F) Excitatory and inhibitory drive. (G) Excitatory-to-excitatory synaptic delay and noise magnitude for both excitatory and inhibitory neurons. (H) Inhibitory and excitatory membrane time constants.

During quiescence, attractor bumps still form a lattice at the center of the neural sheet, where excitatory drive still exceeds threshold (Figure 7B and Video 1). However, these bumps vanish toward the edge of the sheet, where they are replaced by traveling wavefronts of activity. These wavefronts cannot be solely sustained by excitatory drive, which is subthreshold in this outer region; instead, they must be nucleated and then self-sustained through excitatory-to-excitatory connections. In our model, nucleation occurs at activity bumps toward the edge of the sheet (Video 1). Once nucleated, the wavefront propagates freely through the outer region because inhibitory neurons, with low drive, are not activated by the wavefront. In contrast, wavefronts cannot propagate in the center region, because excitatory neurons there receive enough drive to spike vigorously and activate nearby inhibitory neurons (Figure 7B, inhibitory population). These interneurons, with their surround distribution of synaptic outputs (Figure 1A), constrain neural activity to localized bumps and prevent wavefront propagation.

When a wavefront passes through a region of recorded neurons, it can appear as a sequence of spikes (Figure 7C and Figure 7—figure supplement 1) that is decoded as a rapid trajectory (Figure 7D and Figure 7—figure supplement 2). We identify these events as replays, which traverse much of the track over ~100 ms (Figure 7E and Figure 7—figure supplement 3). Due to the stochastic nature of wavefront generation, the number of detected replays can vary considerably across laps (Figure 7—figure supplement 2) and across replicate simulations (Figure 7F). However, replays have a characteristic speed determined by that of wavefront propagation; it is 7.0 ± 2.6 m/s, which is about 14 times faster than the actual speed of 0.50 ± 0.05 m/s (mean ± s.d.; Figure 7G). This agrees with experiments, which measure replays at ≈4–6 m/s and actual motion at ≈0.4–0.5 m/s (O'Neill et al., 2017). Replay speed depends on the number of grid fields and the values of simulation parameters (Figure 7—figure supplement 4). In fact, grid cells with two fields encode two different track positions, so replays among them can have their distribution of decoded position split between parallel lines (Figure 7—figure supplement 3). We have implemented two different detection methods that yield slightly different replay speeds: one that is identical to the single-field case, and another in which multiple lines participate in the fit (Figure 7—figure supplement 4A-D; Appendix 1). Nevertheless, across all simulation parameters and detection methods, replays are always much faster than both the actual animal speed and the theta sequence speed, as observed experimentally (O'Neill et al., 2017). This happens because traveling wavefronts lack inhibition and should be the network phenomenon that propagates fastest.

### Replay properties under different network configurations

#### Lower velocity gain produces replays with directional bias

Under the main parameter values in Table 1, attractor bumps travel long distances on the neural sheet when the animal moves from one end of the track to another (Figure 2C). These distances are longer than the grid scale, so different positions on the track can correspond to the similar locations on the neural sheet, preventing a consistent correspondence between neural sheet location and track position (yellow and purple areas in Figure 2C). With lower velocity gain, attractor bumps travel shorter distances, and such a correspondence is apparent (yellow and purple areas in Figure 8A).

![Figure 8.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig8-v2.jpg)

**Figure 8.:** (A–C) With lower velocity gain, neural sheet locations have a clear one-to-one correspondence with track positions, which allows replays to exhibit a directional bias. (A) Left, track diagram with animal idle at 0 cm. Right, corresponding snapshot of neural activity superimposed on a background colored according to the position at which each neuron attains its maximum firing rate (cf. Figure 2C, right panel). Red circles indicate regions of recording. Attractor bumps still represent the animal position, and a wavefront can be seen emanating from one bump at the top right. (B) Direction of replay propagation across simulations. For each actual position and replay direction, width of gray bars indicates the number of simulations with a particular replay count. Means indicated with lines. p-values from the Mann-Whitney U test show that a significantly greater number of replays propagate away from either actual position. (C) Distances between actual position and decoded position at the start or end of replays. Paired medians compared by the Wilcoxon rank-sum test with indicated p-value. (D–G) With periodic boundary conditions and uniform excitatory drive, attractor bumps and activity wavefronts appear throughout the neural sheet. (D,E) Excitatory drive during runs and idle periods. (F,G) Snapshots of neural activity during runs and idle periods showing S and inhibitory populations. Each pixel is a neuron and dark colors indicate recent spiking. Red circles indicate regions of recording. Scale bars, 50 neurons.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) Grid cell spike rasters for four idle periods. (B) Decoded position corresponding to A. (C) Replays across multiple simulations with cyan fit lines. (D) Number of replays across simulations. (E) Actual run speed 0.50 ± 0.05 m/s (mean ± s.d. over time) and replay speed 7.4 ± 2.3 m/s (mean ± s.d. over replays).

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** Same as Figure 8—figure supplement 1, but for simulations with periodic boundary conditions and uniform excitatory drive. Replay speed is 8.0 ± 2.2 m/s (mean ± s.d. over replays).

![Figure 8—figure supplement 3.](https://cdn.elifesciences.org/articles/46351/elife-46351-fig8-figsupp3-v2.jpg)

**Figure 8—figure supplement 3.:** (A) Grid cell spike rasters for four runs. Vertical blue lines indicate theta cycle boundaries. (B) Decoded position corresponding to A. (C) Relationship between animal position and theta phase for representative neurons. Dots represent spikes during runs in the directions indicated by arrows. Lines indicate fit by circular-linear regression. Numbers in each panel from top left to top right indicate magnitudes of correlation coefficients, regression fit scores, and regression slopes. (D–F) Data across all replicate simulations. (D) Magnitudes of circular-linear correlation coefficients. Mean ± s.d.: 0.14 ± 0.09. (E) Fit scores for circular-linear regression. (F) Regression slopes for neurons with fit score >0.4. (G) Decoded position averaged over theta cycles. Thick black line fit to theta sequence. (H) Actual run speed 0.50 ± 0.05 m/s (mean ± s.d. over time) and theta sequence speed 0.90 ± 0.11 m/s (mean ± s.d. over replicate simulations).

When an animal is idle at either end of the track, attractor bumps are still located at neurons that represent the current position (Figure 8A and Figure 8—video 1). Recall that replays are nucleated at attractor bumps (Video 1 and Figure 8A). As a wavefront radiates from a bump, it will likely first activate neurons whose firing fields represent nearby positions, followed by those with increasingly distant fields, due to the correspondence between neural sheet locations and track positions (Figure 8—video 1). Thus, the decoded position tends to start near the actual position of the animal and travel away from it (Figure 8B). Accordingly, the decoded starting position of replays are closer to the actual position than the decoded ending position (Figure 8C).

However, replays are not all detected immediately after wavefront nucleation; wavefronts traveling for some time may pass through a region of recorded neurons from any direction. Thus, despite the predominance of replays directed away from the actual animal position, some start at the opposite side of the track and travel toward the actual position (Figure 8B). This directional bias has not been directly assessed for grid cells, but it appears in experiments on hippocampal replay (Diba and Buzsáki, 2007; Davidson et al., 2009).

#### Periodic boundary conditions and uniform drive produces replays throughout the neural sheet

Our main model has nonperiodic boundary conditions, which requires excitatory drive to decrease towards the edge of the neural sheet to prevent boundary effects that disrupt path integration (Burak and Fiete, 2009). During idle periods, the persistence of attractor bumps at the center of the sheet maintain a representation of the animal’s position (Figure 7B). With periodic boundaries that eliminate edges, we can implement uniform excitatory drive during both runs and idle periods (Figure 8D,E). This allows the entire neural sheet to exhibit attractor bumps during runs and activity wavefronts during idle periods (Figure 8F,G and Figure 8—video 2). Thus, replays can be recorded from anywhere on the neural sheet. Note that allocentric input at the end of each idle period is essential in this case because positional information in the form of attractor bumps completely disappears. Simulations with periodic boundary conditions and uniform drive produce all the essential replay and theta-related phenomena observed in our main model (Figure 8—figure supplement 2 and Figure 8—figure supplement 3).

## Discussion

### Summary of our results

Decades of hippocampal experiments have established theta phase precession, theta sequences, and replay as central features of place cell dynamics (O'Keefe, 1976; Buzsáki, 1986; Skaggs et al., 1996; Lee and Wilson, 2002; Foster and Wilson, 2006). Evidence has been accumulating that grid cells, discovered more recently, also exhibit these phenomena (Hafting et al., 2008; Ólafsdóttir et al., 2016; O'Neill et al., 2017). These three phenomena appear to be similar to one another in many ways, but experiments have also demonstrated important discordances. Theta sequences have been understood as the direct consequence of individually phase-precessing neurons (O'Keefe and Recce, 1993; Skaggs et al., 1996). However, place cell experiments show that phase precession can appear without theta sequences (Feng et al., 2015). Theta sequences and replays both represent temporally compressed trajectories, and both seem important for memory consolidation and planning (Foster and Knierim, 2012; Zielinski et al., 2018). Yet, replay trajectories are significantly faster than theta sequences, and theta sequences only propagate in the direction of motion whereas replays can propagate in any direction relative to the resting animal (Davidson et al., 2009; Feng et al., 2015; Zheng et al., 2016; O'Neill et al., 2017).

We unify phase precession, theta sequences, and replay under a single model while maintaining distinctions among them. Phase precession and theta sequences arise naturally from oscillations in attractor bump size and speed, respectively, which are both consequences of medial septum input. However, bump size and speed are not generally correlated across changes in other model parameters (Figure 6—figure supplement 1). Thus, it is conceivable that one theta-related phenomenon can exist without the other under certain conditions. Replays in our model arise from the disappearance of attractor bumps and their replacement by traveling wavefronts of activity. Wavefront propagation involves dynamical processes that are fundamentally different from attractor bump motion, and thus has led to different decoded speeds and directions for replays and theta sequences.

Crucially, we produce these phenomena in a continuous attractor network that can still generate 2D grid cells through path integration. Our implementation shares similarities with an early version of the model (Burak and Fiete, 2009) and a version whose connectivity can be learned (Widloski and Fiete, 2014). However, there are three key differences. First, we use fully spiking neurons, which are rarely used in grid cell attractor models—we have only found them utilized in English (2017) and Bush and Burgess (2014), the latter of which combines an attractor network with the oscillatory interference model for grid cells (Burgess et al., 2007; Hasselmo et al., 2007). Typically, neural dynamics are founded on firing rates, which can be used to generate spike trains through a memoryless Poisson process (Burak and Fiete, 2009; Widloski and Fiete, 2014); these models do not capture the strong short-time anticorrelation in spiking due to the reset of membrane potential. Second, we include excitatory-to-excitatory connections in accordance with their recent experimental discovery (Fuchs et al., 2016; Winterer et al., 2017; Schmidt et al., 2017; Zutshi et al., 2018). These connections allow wavefronts to propagate among excitatory neurons while nearby inhibitory neurons remain silent. Third, we vary the external input to the network between active and quiescent behavioral states in accordance with observations (Steriade et al., 2001; Simon et al., 2006). Consequently, the network can instantly switch between operating regimes that exhibit either theta-related phenomena or replays.

Our model presents a distinct conception of entorhinal replay that can be tested experimentally. Direct observation of propagating wavefronts can be pursued by calcium imaging of the MEC (Heys et al., 2014; Diehl et al., 2019). Otherwise, tetrode recordings of grid cell replay in open field environments may be analyzed for wavefront dynamics. In two dimensions, wavefronts would not represent a single trajectory, but instead a manifold of positions that sweep out a plane through space. New decoding techniques that permit the grid cell population to simultaneously represent inconsistent locations would be required to distinguish between these two possible representations of motion.

### Relationships to experiments and other models

We chose to build a continuous attractor model that can produce theta-related behavior and replay with as simple an architecture as possible, but we imagine that more complex network geometries are possible. For example, during quiescence, our model maintains activity bumps at the center of network and only exhibits replays at the edges; with alternative implementations of excitatory drive, multiple areas may contain persistent attractor bumps that nucleate wavefronts. We have also ignored other known components of the grid system. We do not model multiple grid modules (Stensola et al., 2012; Urdapilleta et al., 2017; Kang and Balasubramanian, 2019). During runs, spike frequency adaptation (Yoshida et al., 2013) would reduce the number of spikes late in the grid field, which could enhance phase precession according to the conceptual model presented in Figure 4 and increase correlation magnitude. During quiescence, the MEC exhibits Up and Down states marked by high and low levels of activity; perhaps transitions between these states, which is associated with CA1 ripples (Hahn et al., 2012), can nucleate multiple wavefronts that propagate in synchrony. Moreover, simulation features used to study gamma oscillations in grid cells (Nolan, 2018; Chrobak and Buzsáki, 1998; Colgin et al., 2009) can be introduced to elucidate the role of gamma during theta-related phenomena and replays (Pfeiffer and Foster, 2015; Ramirez-Villegas et al., 2018).

Our model does not explicitly implement biophysical distinctions between LII and LIII neurons or between stellate and pyramidal cells within LII. These neural subpopulations have different characteristic ranges of phase precession that even vary between experimental reports. Ebbesen et al. (2016) found the median precession range of LII stellate and pyramidal cells to be ≈130° and ≈50°, respectively, which is smaller than the values of ≈110° and ≈170° found by Reifenstein et al. (2016). Meanwhile, LIII grid cells, which often possess conjunctive head direction tuning (Sargolini et al., 2006) like the neurons in our model, predominantly exhibit phase-locking with phase precession range close to 0° according to Hafting et al. (2008). However, Reifenstein et al. (2014) reports small, but significant precession in LIII, and single-lap analyses by Ebbesen et al. (2016) finds that LIII neurons precess even more than LII pyramidal cells. O'Neill et al. (2017) does not distinguish between these cell types and observes all of these phase behaviors; this heterogeneity is dynamically captured by the excitatory principal cells in our model. Simulations implementing multiple types of principal cells would be required to precisely assign the distinctions in theta phase properties to the appropriate cell type.

Other models have been proposed for theta phase precession (Tsodyks et al., 1996; Thurley et al., 2008; Navratilova et al., 2012; Thurley et al., 2013) and replay (Ponulak and Hopfield, 2013; Azizi et al., 2013; Bayati et al., 2015; Chenkov et al., 2017; Gönner et al., 2017; Haga and Fukai, 2018). For example, one grid cell model uses after-spike depolarization within a 1D continuous attractor network to generate phase precession and theta sequences (Navratilova et al., 2012). This experimentally observed feature pulls attractor bumps back to recently active locations every theta cycle. A place cell model combines an oscillating membrane potential, as found in our model, with synaptic facilitation (Thurley et al., 2008). These features could be added to our model to strengthen theta-related phenomena and potentially increase correlation magnitude, but they not required. Previously proposed replay models were all intended to address place cells, not grid cells. Several of them encode replay trajectories into synaptic weights, either through hard-wiring or a learning mechanism (Chenkov et al., 2017; Gönner et al., 2017; Haga and Fukai, 2018). Two models have suggested that replays originate from wavefronts of activity propagating through networks of place cells (Ponulak and Hopfield, 2013; Bayati et al., 2015; Palmer et al., 2017). These wavefronts then enhance connections through the network though spike-timing-dependent plasticity rules, which could account for the ability of reward to modulate hippocampal replay (Pfeiffer and Foster, 2013; Ambrose et al., 2016; Palmer and Gong, 2013).

### Possible implications

Although phase precession, theta sequences, and replay arise without learning in our model, they are not necessarily epiphenomenal in the sense that they serve no cognitive purpose. Grid cells are thought to provide a spatial representation that is immediately available upon entering an environment and that remains stable over days of experience (Hafting et al., 2005; Leutgeb et al., 2007; Diehl et al., 2019). They provide spatial information to the hippocampus (Cheng and Frank, 2011; Hales et al., 2014), whose place cells associate location with environmental context (Wilson and McNaughton, 1993; Anderson and Jeffery, 2003) and reward (Hollup et al., 2001; Mamad et al., 2017) to aid the animal in pursuing its goals. In this vein, we envision that superficial MEC layers act as a pattern generator for phase precession, theta sequences, and replay, especially in new environments. These phenomena are then presented to the hippocampus to be refined by experience and modulated by reward.

The concept that sequences in hippocampus arise from superficial MEC layers has been experimentally substantiated for theta phenomena: lesioning the MEC disrupts phase precession and theta sequences in place cells (Schlesiger et al., 2015), but grid cell phase precession is not affected by hippocampal inactivation (Hafting et al., 2008). Driving place cell replays with grid cell replays would require temporal coordination between the two, for which experimental support is mixed. O'Neill et al. (2017) does not find coordination between grid cell replays in superficial MEC layers and sharp-wave-ripples (SWRs) in CA1, during which place cell replays appear. However, Ólafsdóttir et al. (2016) and Ólafsdóttir et al. (2017) report that hippocampal replays represent trajectories coherently with grid cell activity in deep MEC layers, and Yamamoto and Tonegawa (2017) reports that SWRs in CA1 are preceded by SWRs in superficial MEC layers. Further investigation would help to elucidate the temporal relationships between hippocampus and MEC. Also, note that we do not exclude the possibility that place cell replays can also be initiated within the hippocampus or by subcortical nuclei (Stark et al., 2014; Schlingloff et al., 2014; Oliva et al., 2016; Angulo-Garcia et al., 2018; Sasaki et al., 2018).

Place cell activity appears to contain an abundance of certain short sequences that represent contiguous locations in novel environments and participate frequently in replays (Liu et al., 2018). This finding is related to the disputed (Silva et al., 2015) observation of hippocampal preplay (Dragoi and Tonegawa, 2011; Grosmark and Buzsáki, 2016; Liu et al., 2019). From the perspective of our model, such preexisting sequences may arise from wavefronts generated intrinsically by grid cells, which then drive corresponding place cells. After experience, hippocampal plasticity supplements the sequences with additional place cells to enhance their representation of meaningful trajectories (Grosmark and Buzsáki, 2016; Drieu et al., 2018). In this way, wavefronts in the MEC can accelerate learning by providing a scaffold for the hippocampus to modify and improve. Meanwhile, the MEC maintains a symmetric representation of space, so the next experience, possibly with different spatial properties, can be learned equally well.

Yet, we emphasize that our model focuses on the mechanistic origins of grid cell sequences and its results hold regardless of whether the suggested relationships between MEC and hippocampus are borne out by future experiments.

## Materials and methods

This section provides an overview of our simulation methods. Full details are provided in Appendix 1.

### Model architecture and dynamics

Our architecture is inspired by Burak and Fiete (2009) and Widloski and Fiete (2014). A 2D neural sheet contains five overlapping populations, each with neurons at $𝐫=(x,y)$, where $x=1,…,n$ and $y=1,…,n$. There are four excitatory populations: N, S, W, and E; we index them by $P$ and use the symbol $+$ for parameters common to all of them. There is one inhibitory population $-$.

Each excitatory neuron is described by a membrane potential $ϕ^{P}⁢(𝐫,t)$ and a spike indicator $s^{P}⁢(𝐫,t)$, which equals either 1 if neuron $𝐫$ in population $P$ spiked at time $t$ or 0 otherwise. When the potential exceeds a threshold of 1 in arbitrary units, the neuron fires a spike and its potential is reset to 0:

$$
ϕ^{P}⁢(𝐫,t)←0 and s^{P}⁢(𝐫,t)←1.
$$

We prevent $ϕ^{P}⁢(𝐫,t)$ from decreasing past –1 as a limit on hyperpolarization. The same definitions and dynamics apply to the inhibitory population $-$.

Membrane potentials follow leaky integrator dynamics. The excitatory neurons obey

$$
\tau_{m}^{+}\frac{ϕ^{P}(r,t+Δt)−ϕ^{P}(r,t)}{Δt}+ϕ^{P}(r,t)=\sumP^{′},r^{′}w^{+}(r−r^{′}−ξe^^{P^{′}})s^{P^{′}}(r^{′},t−\tau_{s}^{++})+\sumr^{′}w^{−}(r−r^{′})s^{−}(r^{′},t−\tau_{s}^{−})+a^{+}(r)[1+\alphaE^^{P}⋅V(t)]+ζ^{P}(r,t).
$$

And the inhibitory neurons obey

$$
\tau_{m}^{−}\frac{ϕ^{−}(r,t+Δt)−ϕ^{−}(r,t)}{Δt}+ϕ^{−}(r,t)=\sumP^{′},r^{′}w^{+}(r−r^{′}−ξe^^{P^{′}})s^{P^{′}}(r^{′},t−\tau_{s}^{−+})+a^{−}(t)+ζ^{−}(r,t).
$$

Neural drive is given by $a$, which is modulated by the animal’s velocity $𝐕⁢(t)$ for excitatory neurons. Each excitatory population $P$ prefers a perpendicular direction in space $𝐄^^{P}$, which we call North, South, West, and East for the populations N, S, W, and E. Neural connectivity is given by $w$. Each excitatory population $P$ has its synaptic outputs shifted by a small amount $ξ$ in a preferred direction $𝐞^^{P}$ on the neural sheet, which we call up, down, left, and right for the populations N, S, W, and E. Spikes produce an instantaneous change in postsynaptic membrane potential after a synaptic delay $\tau_{s}$, which is longer for excitatory-to-excitatory connections ($\tau_{s}^{++}$) than for excitatory-to-inhibitory connections ($\tau_{s}^{-+}$) based on axon morphology (Schmidt et al., 2017). Independent, zero-mean, normally distributed noise $ζ$ is added to each neuron at each timestep. See Table 1 for complete variable definitions and values.

### Drive and connectivity

The drive to excitatory populations is

$$
a^{+}(r)={a_{min}^{+}+(a_{max}^{+}−a_{min}^{+})\frac{1+cos⁡(\piρ/ρ_{a^{+}})}{2}ρ<ρ_{a^{+}}a_{min}^{+}ρ\geqρ_{a^{+}},
$$

where $ρ=\sqrt{(x−\frac{n+1}{2})^{2}+(y−\frac{n+1}{2})^{2}}/\frac{n}{2}$ is a scaled radial distance for the neuron at $𝐫=(x,y)$. It equals 0 at the center of the neural sheet and approximately one at the midpoint of an edge. The drive to inhibitory subpopulations is

$$
a^{-}⁢(t)=a_{mag}^{-}-a_{th}^{-}⁢cos⁡(2⁢\pi⁢f⁢t+ψ_{0}),
$$

where $ψ_{0}$ is a phase offset chosen randomly at the start of each lap.

The synaptic connectivity from excitatory neurons to all neurons is based on the symmetric function

$$
w^{+}(r)={w_{mag}^{+}\frac{1+cos⁡(\pir/r_{w^{+}})}{2}r<r_{w^{+}}0r\geqr_{w^{+}},
$$

where $r=|𝐫|$. The synaptic connectivity from inhibitory neurons to excitatory neurons is

$$
w^{−}(r)={−w_{mag}^{−}\frac{1−cos⁡(\pir/r_{w^{−}})}{2}r<2r_{w^{−}}0r\geq2r_{w^{−}}.
$$

There is no connectivity from inhibitory neurons to other inhibitory neurons.

See Table 1 for complete variable definitions and values.

### Brief allocentric correction

The grid-like pattern of excitatory drive during brief allocentric corrections (Figure 2B) represents inputs from neurons with allocentric responses, such as border, boundary vector, or landmark cells (Evans et al., 2016; Raudies and Hasselmo, 2015; Savelli et al., 2017). Interactions between allocentric neurons and grid cells have also been implemented in other continuous attractor models (Ocko et al., 2018; Keinath et al., 2018). In our model, allocentric input is learned in an accelerated manner during simulation setup. Immediately before the main simulation phase, we simulate one run in each track direction followed by a learning period at either end of the track. The locations of attractor bumps during learning periods are stored by tallying the number of spikes produced at each neural sheet location. These tallies are linearly rescaled to serve as the allocentric drive to excitatory populations.

### Single neuron recording and decoding

We simulate our model 10 times with slightly different run trajectories randomly generated by fractional Brownian motion processes, followed by 10 more times with the same trajectories but reversed velocities. These simulations produce spike trains for all neurons in the network. To match multiunit tetrode recordings, we select two sets of up to 150 excitatory neurons in each simulation. Each of these sets is an independent recording to be analyzed separately, which we call a ‘simulation’ in our results.

We select neurons for recording as follows. For the first set, we choose four points on the neural sheet whose distance from the center is 95 neurons and whose angular positions, or clock positions, are random but equally spaced. From circular areas of radius 12 centered at these points, we randomly select up to 150 excitatory neurons whose firing fields are stable across laps. For the second set, we choose the four circular areas with the same distance from the center of the sheet and with angular positions offset 45° from the first four areas. We again select up to 150 neurons with stable firing fields. All single-simulation results reported in the main text come from the same simulation.

We use grid cell firing fields accrued from all laps in both directions to decode the animal’s position from the population activity of its recorded neurons. We use the standard Bayesian decoding procedure that assumes independent, Poisson-distributed spike counts and a uniform prior (Zhang et al., 1998; O'Neill et al., 2017).
