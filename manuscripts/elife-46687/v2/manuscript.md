# A geometric attractor mechanism for self-organization of entorhinal grid modules

## Authors

- Louis Kang<sup>1</sup> ([ORCID: 0000-0002-5702-2740](https://orcid.org/0000-0002-5702-2740)) †
- Vijay Balasubramanian<sup>1</sup> ([ORCID: 0000-0002-6497-3819](https://orcid.org/0000-0002-6497-3819))

### Affiliations

1. David Rittenhouse Laboratories University of Pennsylvania Philadelphia United States
2. Redwood Center for Theoretical Neuroscience University of California, Berkeley Berkeley United States

† Corresponding author

## Abstract

Grid cells in the medial entorhinal cortex (MEC) respond when an animal occupies a periodic lattice of ‘grid fields’ in the environment. The grids are organized in modules with spatial periods, or scales, clustered around discrete values separated on average by ratios in the range 1.4–1.7. We propose a mechanism that produces this modular structure through dynamical self-organization in the MEC. In attractor network models of grid formation, the grid scale of a single module is set by the distance of recurrent inhibition between neurons. We show that the MEC forms a hierarchy of discrete modules if a smooth increase in inhibition distance along its dorso-ventral axis is accompanied by excitatory interactions along this axis. Moreover, constant scale ratios between successive modules arise through geometric relationships between triangular grids and have values that fall within the observed range. We discuss how interactions required by our model might be tested experimentally.

## Introduction

A grid cell has a spatially modulated firing rate that peaks when an animal reaches certain locations in its environment (Hafting et al., 2005). These locations of high activity form a regular triangular grid with a particular length scale and orientation in space. Every animal has many grid cells that collectively span a wide range of scales, with smaller scales enriched dorsally and larger scales ventrally along the longitudinal axis of the MEC (Stensola et al., 2012). Instead of being smoothly distributed, grid scales cluster around particular values and thus grid cells are partitioned into modules (Stensola et al., 2012). Consecutive pairs of modules have scale ratios in the range 1.2–2.0 (Stensola et al., 2012; Barry et al., 2007; Krupic et al., 2015). The scale ratio averaged across animals is constant from one pair of modules to the next and lies in the interval 1.4 (Stensola et al., 2012) to 1.7 (Barry et al., 2007; Krupic et al., 2015), suggesting that the grid system favors a universal scale ratio in this range.

Encoding spatial information through grid cells with constant scale ratios is thought to provide animals with an efficient way of representing their position within an environment (Moser et al., 2008; Fiete et al., 2008; Mathis et al., 2012; Wei et al., 2015; Stemmler et al., 2015; Sanzeni et al., 2016; Mosheiff et al., 2017). Moreover, periodic representations of space permit a novel mechanism for precise error correction against neural noise (Sreenivasan and Fiete, 2011) and are learned by machines seeking to navigate open environments (Cueva and Wei, 2018; Banino et al., 2018). These findings provide motivation for forming a modular grid system with a constant scale ratio, but a mechanism for doing so is unknown. Continuous attractor networks (Fuhs and Touretzky, 2006; Burak and Fiete, 2009), a leading model for producing grid cells, would currently require discrete changes in scales to be directly imposed as sharp changes in parameters, as would the oscillatory interference model (Burgess et al., 2007; Hasselmo et al., 2007) or hybrid models (Bush and Burgess, 2014). In contrast, many sensory and behavioral systems have smooth tuning distributions, such as preferred orientation in visual cortex (Issa et al., 2008) and preferred head direction in the MEC (Taube et al., 1990). A self-organizing map model with stripe cell inputs (Grossberg and Pilly, 2012) and a firing rate adaptation model with place cell inputs (Urdapilleta et al., 2017) can generate discrete grid scales, but their ratios are not constant or constant-on-average unless explicitly tuned.

Here, we present a simple extension of the continuous attractor model that adds excitatory connections between a series of attractor networks along the dorso-ventral axis of the MEC, accompanied by an increase in the distance of inhibition. The inhibition gradient drives an increase in grid scale along the MEC axis. Meanwhile, the excitatory coupling discourages changes in grid scale and orientation unless they occur through geometric relationships with defined scale ratios and orientation differences. Competition between the effects of longitudinal excitation and lateral inhibition self-organizes the complete network into a discrete hierarchy of modules. Certain grid relationships are geometrically stable, which makes them, and their associated scale ratios, insensitive to perturbations. The precise ratios that appear depend on the balance between excitation and inhibition and how it varies along the MEC axis. We show that sampling across a range of these parameters leads to a distribution of scale ratios that matches experiment and is, on average, constant from the smallest to the largest pair of modules.

Continuous attractors are a powerful general method for self-organizing neural dynamics. To our knowledge, our results are the first demonstration of a mechanism for producing a discrete hierarchy of modules in a continuous attractor system.

## Results

### Standard grid cell attractors are not modular

We assemble a series of networks along the longitudinal MEC axis, numbering them z = 1, 2, ..., 12 from dorsal to ventral (Figure 1A). Each network contains the standard 2D continuous attractor architecture of the Burak-Fiete model (Burak and Fiete, 2009). Namely, neurons are arranged in a 2D sheet with positions (x,y), receive broad excitatory drive (Bonnevie et al., 2013 and Figure 1B), and inhibit one another at a characteristic separation on the neural sheet (Figure 1C; see Materials and methods for a complete description). In our model, this inhibition distance l is constant within each network but increases from one network to the next along the longitudinal axis of the MEC. With these features alone, the population activity in each network self-organizes into a triangular grid whose lattice points correspond to peaks in neural activity (Figure 2A). Importantly, the scale of each network’s grid, which we call λ(z), is proportional to that network’s inhibition distance l(z) (‘uncoupled’ simulations in Figure 3A). Also, network grid orientations θ show no consistent pattern across scales and among replicate simulations with different random initial firing rates.

![Figure 1.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig1-v2.jpg)

**Figure 1.:** (A) Each network z corresponds to a region along the dorso-ventral MEC axis and contains a 2D sheet of neurons with positions (x,y). (B) Neurons receive excitatory drive a(x,y) that is greatest at the network center and decays toward the edges. (C) Neurons inhibit neighbors within the same network with a weight w(x,y;z) that peaks at a distance of l(z) neurons, which increases as a function of z. Each neuron has its inhibitory outputs shifted slightly in one of four preferred network directions and receives slightly more drive when the animal moves along its preferred spatial direction. (D) Each neuron at position (x,y) in network z excites neurons located within a spread d of (x,y) in network z – 1.

![Figure 2.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig2-v2.jpg)

**Figure 2.:** (A–D) A representative simulation without coupling. (A) Network activities at the end of the simulation. (B) Activity overlays between adjacent networks depicted in A. In each panel, the network with smaller (larger) z is depicted in magenta (green), so white indicates activity in both networks. (C) Spatial rate map of a single neuron for each z superimposed on the animal’s trajectory. (D) Spatial autocorrelations of the rate maps depicted in C. (E–H) Same as A–D but for a representative simulation with coupling. Standard parameter values provided in Table 1. White scale bars, 50 neurons. Black scale bars, 50 cm.

![Figure 3.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig3-v2.jpg)

**Figure 3.:** (A–C) Data from 10 replicate uncoupled and coupled simulations. (A) Left: network grid scales λ(z). For each network, there are 10 closely spaced red circles and 10 closely spaced blue squares corresponding to replicate simulations. Inset: λ(z) divided by the inhibition distance l(z). Middle: histogram for λ collected across all networks. Right: network grid orientations θ relative to the network in the same simulation with largest scale. (B) Left: spatial grid scales Λ(z). For each z, there are up to 30 red circles and 30 blue squares corresponding to three neurons recorded during each simulation. Inset: Λ(z) divided by the inhibition distance l(z). Middle: histogram for Λ collected across all networks. In the coupled model, grid cells are clustered into three modules. Right: spatial grid orientations Θ relative to the grid cell in the same simulation with largest scale. (C) Spatial scale ratios and orientation differences between adjacent modules for the coupled model. (D) Activity overlays enlarged from Figure 2F to emphasize lattice relationships. In each panel, the network with smaller (larger) z is depicted in magenta (green), so white indicates activity in both networks. Standard parameter values provided in Table 1.

**Table 1.**
 Main model parameters and their values unless otherwise noted.


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
      <td>Number of networks</td>
      <td>h</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Number of neurons per network</td>
      <td>n×n</td>
      <td>160 × 160</td>
    </tr>
    <tr>
      <td>Neurons recorded per network</td>
      <td></td>
      <td>3</td>
    </tr>
    <tr>
      <td>Animal speed</td>
      <td>|𝐕|</td>
      <td>0–1 m/s</td>
    </tr>
    <tr>
      <td>Diameter of enclosure</td>
      <td></td>
      <td>180 cm</td>
    </tr>
    <tr>
      <td>Simulation time</td>
      <td></td>
      <td>500 s</td>
    </tr>
    <tr>
      <td>Simulation timestep</td>
      <td>Δ⁢t</td>
      <td>1 ms</td>
    </tr>
    <tr>
      <td>Neural relaxation time</td>
      <td>τ</td>
      <td>10 ms</td>
    </tr>
    <tr>
      <td>Broad input strength</td>
      <td>amag</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Broad input falloff</td>
      <td>afall</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Inhibition distance minimum</td>
      <td>lmin</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Inhibition distance maximum</td>
      <td>lmax</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Inhibition distance exponent</td>
      <td>lexp</td>
      <td>–1</td>
    </tr>
    <tr>
      <td>Inhibition strength</td>
      <td>wmag</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td>Subpopulation shift</td>
      <td>ξ</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Coupling spread</td>
      <td>d</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Coupling strength</td>
      <td>umag</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td>Velocity gain</td>
      <td>α</td>
      <td>0.3 s/m</td>
    </tr>
  </tbody>
</table>

Following the standard attractor model (Burak and Fiete, 2009), the inhibitory connections in each network are slightly modulated by the animal’s velocity such that the population activity pattern of each network translates proportionally to animal motion at all times (Materials and methods). This modulation allows each network to encode the animal’s displacement through a process known as path-integration, and projects the network grid pattern onto spatial rate maps of single neurons. That is, a recording of a single neuron over the course of an animal trajectory would show high activity in spatial locations that form a triangular grid with scale Λ (Figure 2C). Moreover, Λ(z) for a neuron from network z is proportional to that network’s population grid scale λ(z), and thus also proportional to its inhibition distance l(z) (uncoupled simulations in Figure 3B). To be clear, we call Λ the ‘spatial scale’; it corresponds to a single neuron’s activity over the course of a simulation and has units of physical distance in space. By contrast, λ, the ‘network scale’ described above, corresponds to the population activity at a single time and has units of separation on the neural sheet. Similarly, Θ(z) describes the orientation of the spatial grid of a single neuron in the network z; we call Θ the ‘spatial orientation.’ Like the network orientations θ discussed above, spatial orientations of grids show no clustering (uncoupled simulations in Figure 3B).

With an inhibition distance l(z) that increases gradually from one network to the next (Figure 1C), proportional changes in network and spatial scales λ(z) and Λ(z) lead to a smooth distribution of grid scales (uncoupled simulations in Figure 3A,B). To reproduce the experimentally observed jumps in grid scale between modules, the inhibition distance would also have to undergo discrete, sharp jumps between certain adjacent networks. In summary, a grid system created by disjoint attractor networks will not self-organize into modules.

### Coupled attractor networks produce modules

Module self-organization can be achieved with one addition to the established features listed above: we introduce excitatory connections from each neuron to those in the preceding network with approximately corresponding neural sheet positions (Figure 1D; see Materials and methods for a complete description). That is, a neuron in network z (more ventral) with position (x,y) will excite neurons in network z – 1 (more dorsal) with positions that are within a distance d of position (x,y). In other words, the distance d is the ‘spread’ of excitatory connections, and we choose a constant value across all networks comparable to the inhibition distance l(z).

The self-organization of triangular grids in the neural sheet and the faithful path-integration that projects these grids onto single neuron spatial rate maps persist after introduction of inter-network coupling (Figure 2G). Network and spatial scales λ(z) and Λ(z) still increase from network z = 1 (dorsal) to network z = 12 (ventral). Yet, Figure 3A,B shows that for the coupled model, these scales exhibit plateaus that are interrupted by large jumps, disrupting their proportionality to inhibition distance l(z), which is kept identical to that of the uncoupled system (Figure 1C). Collecting scales across all networks illustrates that they cluster around certain values in the coupled system while they are smoothly distributed in the uncoupled system. We identify these clusters with modules M1, M2, and M3 of increasing scale. Note that multiple networks at various depths z can belong to the same module. Moreover, coupling causes grid cells that cluster around a certain scale to also cluster around a certain orientation (Figure 3A,B), as seen in experiment (Stensola et al., 2012). The uncoupled system does not demonstrate co-modularity of orientation with scale, that is two networks with similar grid scales need not have similar orientations unless this is imposed by an external constraint.

In summary, excitatory coupling between grid attractor networks dynamically induces discreteness in grid scales that is co-modular with grid orientation, as observed experimentally (Stensola et al., 2012), and as needed for even coverage of space by the grid map (Sanzeni et al., 2016).

### Modular geometry is determined by lattice geometry

Not only does excitatory coupling produce modules, it can do so with consistent scale ratios and orientation differences. For the coupled system depicted in Figure 2, scale ratios and orientation differences between pairs of adjacent modules consistently take values 1.74 ± 0.02 and 29.5 ± 0.4°, respectively (mean ± s.d.; Figure 3C). These values are robust to a variety of parameter perturbations, coupling architectures, and sources of noise. We can make the inhibition distance profile l(z) less or more concave (Figure 4A,B), or we can implement excitatory connections with different properties by reversing their direction (Figure 4C), including connections in both directions (Figure 4D), or allowing the coupling spread to vary with network depth (Figure 4E). In each case, the same scale ratio of ≈1.7 and orientation difference of ≈30° persist. We can also reduce the number of neurons by a factor of 9 without affecting the scale ratio and orientation difference (Figure 4F). Similar results are obtained with neural inputs corrupted by independent Gaussian noise (Figure 4G) and with randomly shifted excitatory connections, which adds another form of coupling imprecision in addition to spread (Figure 4H). Finally, simulations with spiking dynamics following Burak and Fiete (2009) also demonstrate a preference for scale ratios of ≈1.7 and orientation differences of ≈30°, albeit with greater variability (Figure 4I).

![Figure 4.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig4-v2.jpg)

**Figure 4.:** Data from 10 replicate simulations in each subfigure, which shows spatial grid scales Λ(z) and scale ratios and orientation differences between modules. (A) Left: less concave inhibition distance profile l(z) (dark) compared to Figure 1C (light). (B) Same as A, but for a more concave l(z). (C) Dorsal-to-ventral coupling from each network z to network z + 1. (D) Bidirectional coupling from each network z to networks z – 1 and z + 1. (E) Left: coupling spread d(z) set to l(z) (dark) instead of a constant d (light). (F) Grid system with fewer networks h = 6 of smaller size n × n = 76 × 76. (G) Independent noise added to each neuron’s firing rate at each timestep. (H) Coupling outputs randomly shifted for each neuron by one neuron in both x- and y-directions. (I) Spiking simulations with spikes generated by an independent Poisson process. Detailed methods for each system provided in Appendix 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Top row of each subfigure: network activities at the end of the simulation. Second row: activity overlays between adjacent networks depicted in the top row. In each panel, the network at smaller (larger) z is depicted in magenta (green), so white indicates regions of activity in both networks. Third row: spatial rate map of a single neuron for each z superimposed on the animal’s trajectory. Bottom row: spatial autocorrelations of the rate maps depicted in the third row. (A) Corresponding to Figure 4A. (B) Corresponding to Figure 4B. (C) Corresponding to Figure 4C. White scale bars, 50 neurons. Black scale bars, 50 cm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Panels same as in Figure 4–Figure supplement 1. (A) Corresponding to Figure 4D. (B) Corresponding to Figure 4E. (C) Corresponding to Figure 4F. White scale bars, 50 neurons. Black scale bars, 50 cm.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Panels same as in Figure 4–Figure supplement 1. (A) Corresponding to Figure 4G. (B) Corresponding to Figure 4H. (C) Corresponding to Figure 4I. White scale bars, 50 neurons. Black scale bars, 50 cm.

We can intuitively understand this robust modularity through the competition between lateral inhibition within networks and longitudinal excitation across networks. In the uncoupled system, grid scales decrease proportionally as the inhibition distance l(z) decreases from z = 12 to z = 1. However, coupling causes areas of high activity in network z to preferentially excite corresponding areas in network z – 1, which encourages adjacent networks to share the same grid pattern (z = 10 & 11 in Figure 3D). Thus, coupling adds rigidity to the system and provides an opposing ‘force’ against the changing inhibition distance that attempts to drive changes in grid scale. This rigidity produces the plateaus in network and spatial scales λ(z) and Λ(z) that delineate modules across multiple networks.

At interfaces between modules, coupling can no longer fully oppose the changing inhibition distance, and the grid pattern changes. However, the rigidity fixes a geometric relationship between the grid patterns of the two networks spanning the interface. In the coupled system of Figure 2 and Figure 3, module interfaces occur between networks z = 4 and 5 and between z = 9 and 10. The network population activity overlays of Figure 3D reveal overlap of many activity peaks at these interfaces. However, the more dorsal network (with smaller z) at each interface contains additional small peaks between the shared peaks. In this way, adjacent networks still share many corresponding areas of high activity, as favored by coupling, but the grid scale changes, as favored by a changing inhibition distance. Pairs of grids whose lattice points demonstrate regular registry are called commensurate lattices (Chaikin and Lubensky, 1995) and have precise scale ratios and orientation differences, here respectively $\sqrt{3}$ ≈ 1.7 and 30°, which match the results in Figure 3C and Figure 4.

In summary, excitatory coupling can compete against a changing inhibition distance to produce a rigid grid system whose ‘fractures’ exhibit stereotyped commensurate lattice relationships. These robust geometric relationships lead to discrete modules with fixed scale ratios and orientation differences.

In our model, commensurate lattice relationships naturally lead to field-to-field firing rate variability in single neuron spatial rate maps (z = 8 in Figure 2G, for example), another experimentally observed feature of the grid system (Ismakov et al., 2017; Dunn et al., 2017; Diehl et al., 2017). At interfaces between two commensurate lattices, only a subset of population activity peaks in the grid of smaller scale overlap with, and thus receive excitation from, those in the grid of larger scale. The network with smaller grid scale will contain activity peaks of different magnitudes; this heterogeneity is then projected onto the spatial rate maps of its neurons.

### Excitation-inhibition balance sets lattice geometry

Adjusting the balance between excitatory coupling and a changing inhibition distance produces other commensurate lattice relationships, each of which enforces a certain scale ratio and orientation difference. To explore this competition systematically, we use a smaller coupled model with just two networks, z = 1 and 2, and vary three parameters: the coupling spread d, the coupling strength umag, and the ratio of inhibition distances between the two networks l(2)/l(1) (Appendix 1). For each set of parameters, we measure network scale ratios and orientation differences produced by multiple replicate simulations (Figure 5—figure supplement 1 and Figure 5—figure supplement 2). We find that as the excitation-inhibition balance is varied by changing umag and l(2)/l(1), a number of discretely different relationships appear, which can be summarized in ‘phase diagrams’ (Figure 5A,B).

![Figure 5.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig5-v2.jpg)

**Figure 5.:** In models with only two networks z = 1 and 2, we vary the coupling strength umag and the ratio of inhibition distances l(2)/l(1) for two different coupling spreads d. (A, B) Approximate phase diagrams based on 10 replicate simulations for each set of parameters, with the mean of l(1) and l(2) fixed to be 9. The most frequently occurring scale ratio and orientation difference are indicated for each region; coexistence between multiple lattice relationships may exist at drawn boundaries. (A) Phase diagram for small coupling spread d = 6. Solid lines separate four regions with different commensurate lattice relationships labeled by scale ratio and orientation difference, and dotted lines mark one region of discommensurate lattice relationships. (B) Phase diagram for large coupling spread d = 12. There are five different commensurate regions, a discommensurate region, as well as a region containing incommensurate lattices (gray). (C) Network activity overlays for representative observed (left) and idealized (right) commensurate relationships. Numbers at the top right of each image indicate network scale ratios λ(2)/λ(1) and orientation differences θ(2) − θ(1). Networks z = 1 and 2 in magenta and green, respectively, so white indicates activity in both networks. (D) Expanded region of B displaying discommensurate lattice statistics. For each set of parameters, a representative overlay for the most prevalent discommensurate lattice relationship is shown. The number in the lower right indicates the proportion of replicate simulations with scale ratio within 0.02 and orientation difference within 3° of the values shown at top right. In one overlay, discommensurations are outlined by white lines. (E) The discommensurate relationships described in D demonstrate positive correlation between scale ratio and the logarithm of orientation difference (Pearson’s ρ = 0.91, p ∼ 10–26 ; Spearman’s ρ = 0.92, p ∼ 10–27 ). Simulation details provided in Appendix 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Two-network model with coupling spread d = 6. (A) Network scale ratios λ(2)/λ(1). (B) Network orientation differences θ(2) − θ(1). For each l(2)/l(1) and umag, 10 replicate simulations subject are represented by circles with colors corresponding across the two subfigures. Small horizontal offsets are introduced for clarity, and each set of replicate simulations is ordered by θ(2) − θ(1). Gray lines track mean values as a function of l(2)/l(1).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Panels same as in Figure 5—figure supplement 1, but for coupling spread d = 12.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Two-network model with no noise, activity noise as in Figure 4G, and coupling noise as in Figure 4H. (A, B) Network parameters that, in accordance with Figure 5, produce a predominance of the $[\sqrt{3},30^{∘}]$ commensurate relationship. (A) Representative activity overlays. Networks z = 1 and 2 in magenta and green, respectively, so white indicates activity in both networks. Prevalence is the proportion of replicate simulations with scale ratio within 0.02 and orientation difference within 3° of the values shown at top right. (B) Network scale ratios and orientation differences for 10 replicate simulations per noise condition. (C, D) Same as A, B, but for parameters that produce a predominance of the $[\sqrt{7}/2,19^{∘}]$ commensurate relationship. (E, F) Same as A, B, but for parameters that produce a predominance of discommensurate relationships with scale ratio ≈1.24 and orientation difference ≈0°. Note that for each set of parameters, the predominant lattice relationship is maintained in the presence of noise. Data for the no noise condition taken from Figure 5—figure supplement 1 and Figure 5—figure supplement 2.

In many regions of the phase diagrams, these lattice relationships are commensurate, each with a characteristic scale ratio and orientation difference (Figure 5C). When parameters are chosen near a boundary between two regions, replicate simulations may adopt either lattice relationship or occasionally be trapped in other metastable relationships due to variations in random initial conditions (Figure 5—figure supplement 2). At larger umag in both phase diagrams, there are fewer regions as l(2)/l(1) varies because a higher excitatory coupling strength provides more rigidity against gradients in inhibition distance (Figure 5A,B). However, a larger coupling spread d would cause network z = 2 to excite a broader set of neurons in network z = 1, softening the rigidity imposed by coupling and producing a wider variety of lattices in Figure 5B than Figure 5A. Also in Figure 5B, when excitation is weak and approaching the uncoupled limit, there is a noticeable region dominated by incommensurate lattices, in which the two grids lack consistent registry or relative orientation, and grid scale is largely determined by inhibition distance (Figure 5—figure supplement 2).

Figure 5B also contains a larger region of discommensurate lattices (although strictly speaking, in condensed matter physics, they would be termed commensurate lattices with discommensurations; Chaikin and Lubensky, 1995). Discommensurate networks have closely overlapping activities in certain areas that are separated by a mesh of regions lacking overlap called discommensurations (Figure 5D). They exhibit ranges of scale ratios 1.1–1.4 and orientation differences 0°–10° that ultimately arise from a single source: the density of discommensurations, whose properties can also be explained through excitation-inhibition competition. Stronger coupling drives more activity overlap, which favors sparser discommensurations and lowers the scale ratio and orientation difference. However, a larger inhibition distance ratio drives the two networks to differ more in grid scale, which favors denser discommensurations. To better accommodate the discommensurations, grids rotate slightly as observed previously in a crystal system (Wilson, 1990). Figure 5E confirms that scale ratios and orientation differences vary together as the discommensuration density changes.

Thus, by changing the balance between excitation and inhibition, a two-network model yields geometric lattice relationships with various scale ratios and corresponding orientation differences. All the commensurate relationships (Figure 5C) and almost the entire range of discommensurate relationships (Figure 5D) have scale ratios that fall in the range of experimental measurements, which is roughly 1.2–2.0 (Stensola et al., 2012; Barry et al., 2007; Krupic et al., 2015). The scale ratios and orientation differences in both the commensurate and discommensurate cases are robust against activity noise and coupling noise (Figure 5—figure supplement 3).

### Discommensurate lattices produce distinct modular geometries but with more variation

As mentioned above, discommensurate lattices have a range of allowed geometries (Figure 5D,E), but they can still produce modules in a full 12-network grid system with a preferred scale ratio and orientation difference. However, these values do not cluster as strongly as they do for a commensurate relationship, which is geometrically precise.

The phase diagrams of Figure 5 provide guidance for modifying a 12-network system that exhibits a $[\sqrt{3},30^{∘}]$ relationship to produce discommensurate relationships instead. We make the inhibition distance profile l(z) shallower (Figure 6A) and increase the coupling spread d by 50%. Network activity overlays of these new simulations reveal grids obeying discommensurate relationships (Figure 6B,C), which are projected onto single neuron spatial rate maps through faithful path-integration (Figure 6—figure supplement 1A). Across replicate simulations with identical parameter values but different random initial firing rates, the discommensurate system demonstrates greater variation in scale and orientation (Figure 6D) than the commensurate system of Figure 3 does. Nevertheless, analysis of each replicate simulation reveals clustering with well-defined modules (Figure 6E and Figure 6—figure supplement 1B). These modules have scale ratio 1.39 ± 0.10 and orientation difference 6.7 ± 3.5° (mean ± s.d.; Figure 6F). The preferred scale ratio agrees well with the mean value observed experimentally in Stensola et al. (2012).

![Figure 6.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig6-v2.jpg)

**Figure 6.:** (A) We use a shallower inhibition distance profile l(z) (dark) compared to Figure 1C (light). (B) Large activity overlays from a representative simulation that emphasize discommensurate lattice relationships. (C) All activity overlays from the representative simulation in B between adjacent networks z in magenta and green, so white indicates activity in both networks. Scale bar, 50 neurons. (D–F) Data from 10 replicate simulations. (D) Left: spatial grid scales Λ(z). For each network, there are up to 30 red circles corresponding to three neurons recorded during each simulation. Middle: histogram for Λ collected across all networks. Right: spatial orientations Θ relative to the grid cell in the same simulation with largest scale. (E) Clustering of spatial scales and orientations for three representative simulations. Due to sixfold lattice symmetry, orientation is a periodic variable modulo 60°. Different colors indicate separate modules. (F) Spatial scale ratios and orientation differences between adjacent modules. (G) Representative activity overlay demonstrating defect with low activity overlap. Maximum inhibition distance lmax = 10, coupling spread d = 12. We use larger network size n × n = 230 × 230 to allow for discommensurate relationships whose periodicities span longer distances on the neural sheets. Other parameter values are in Table 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Representative network activities and single neuron rate maps for the discommensurate system. Top row: network activities at the end of the simulation. Second row: activity overlays between adjacent networks depicted in the top row. In each panel, the network at smaller (larger) z is depicted in magenta (green), so white indicates regions of activity in both networks. Third row: spatial rate map of a single neuron for each z superimposed on the animal’s trajectory. Bottom row: spatial autocorrelations of the rate maps depicted in the third row. White scale bars, 50 neurons. Black scale bars, 50 cm. (B) Clustering of spatial scales and orientations for all replicate simulations. Due to sixfold lattice symmetry, orientation is a periodic variable modulo 60°. Different colors indicate separate modules.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) Sample experimentally recorded single neuron rate map adapted from Figure 1a of Dunn et al. (2017). (B) Sample single neuron rate map from a simulation with the same parameters as in Figure 6 that exhibits discommensurate lattice relationships. Note that firing rate decreases across fields from the bottom left to the top right of both A and B; the presence of firing rate modulation over long distances has been considered by Stemmler and Herz (2017). In B, the fields at the top right correspond to a discommensuration on the neural sheet and the fields at the bottom left correspond to a region in between discommensurations that exhibits activity overlap. A comprehensive test requires analysis with experiments using circular enclosures to eliminate confounding boundary effects (see Discussion).

Conceptually, we can interpret the greater spread of scales and orientations in terms of coupling rigidity. Excitatory coupling, especially when the spread is larger, provides enough rigidity in the discommensurate system to cluster scale ratios and orientation differences but not enough to prevent variations in these values. The degree of variability observed in Figure 6D,E appears consistent with experimental measurements, which also demonstrate spread (Stensola et al., 2012; Barry et al., 2007).

A few module pairs in Figure 6F exhibit a large orientation difference >10°. This is not expected from a discommensurate relationship, and indeed, inspecting the network activities reveals adjacent networks trapped in a relationship with low activity overlap and large orientation difference (Figure 6G). In the context of a grid system that otherwise obeys commensurate or discommensurate geometries containing more overlap, we call this less common relationship a ‘defect.’ We distinguish between these relationships and the incommensurate lattices discussed above, which also have low activity overlap. Defects arise when the excitatory coupling is strong, and incommensurate lattices arise when this coupling is weak. Also, defects have smaller scale ratios <1.1 and larger orientation differences >10°, whereas incommensurate lattices have larger scale ratios >1.3 and any orientation difference (Figure 5B and Figure 5—figure supplement 2).

Thus, networks governed by discommensurate relationships also cluster into modules with a preferred scale ratio and orientation difference within the experimental range (Stensola et al., 2012; Krupic et al., 2015). Due to lower coupling rigidity compared to commensurate grid systems, they exhibit increased variability and occasional defects across replicate simulations.

As in the commensurate case, discommensurate lattice relationships also create field-to-field firing rate variability in single neuron spatial rate maps. At interfaces between two discommensurate lattices, population activity peaks lack overlap at discommensurations and exhibit overlap in between them. Thus, only a subset of peaks in the grid of smaller scale receive excitation from the grid of larger scale; those located at discommensurations do not. As activity patterns translate on the neural sheets during path-integration, a grid cell in the network with smaller scale will have lower firing rate when a discommensuration moves through it, leading to firing rate variability (see Figure 6—figure supplement 2 for an example).

### A diversity of lattice geometries maintains constant-on-average scale ratios

So far, each set of 12-network simulations contained replicates with identical parameter values and exhibited a single dominant lattice relationship. We now present results with different parameter values to imitate biological network variability across animals. This procedure leads to modules with different commensurate and discommensurate relationships (Figure 7A and Figure 7—figure supplement 1). There is no longer a single preferred scale ratio or orientation difference (Figure 7B), but patterns emerge due to the predominance of discommensurate and commensurate relationships. Recall from Figure 6F that discommensurate module pairs exhibit scale ratios ≈1.4 and orientation differences ≈7﻿°. Combined with $[\sqrt{3}≈1.7,30^{∘}]$ module pairs, we find a bimodal distribution of orientation differences around 7° and 30°, consistent with experimental data (Krupic et al., 2015), and positive correlation between scale ratio and orientation difference. Modules with low scale ratio but high orientation difference decrease this correlation; they arise from defects (Figure 6G). Figure 7—figure supplement 2 illustrates how modules observed experimentally may be governed by a variety of lattice relationships.

![Figure 7.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig7-v2.jpg)

**Figure 7.:** Data from five replicate simulations for each set of parameters, encompassing 51 total module pairs. (A) Clustering of spatial scales and orientations for one representative simulation (left) and lattice relationship distribution across all pairs of adjacent modules (right) for each set of parameters. (B) Spatial scale ratios and orientation differences between adjacent modules with respective histograms to the right and above. Scale ratios and orientation differences exhibit positive rank correlation (Spearman’s ρ = 0.44, p = 0.001). (C) Spatial scale ratios. Means indicated by lines. Medians compared through the Mann-Whitney U test with reported p-value. (D) Spatial scale differences normalized by the scale of the first module (M1) in each simulation. Same interpretation of lines and p-value as in C. The umag = 2.6 and lmax = 10 data are taken from simulations in Figure 5. Some simulations produced only two modules M1 and M2; one simulation produced four modules, and M4 was excluded from further analysis. Coupling spread d = 12 and network size n × n = 230 × 230. Other parameter values are in Table 1.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Clustering of scales and orientations for all replicate simulations spanning a range of parameters. Due to 6-fold lattice symmetry, orientation is a periodic variable modulo 60°. Different colors indicate separate modules. Simulations use network size n × n = 230 × 230 and coupling spread d = 12.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (A) Sample single neuron autocorrelation maps of grid cells belonging to four modules from Figure 1c of Stensola et al. (2012). (B) Overlays between sheared triangular lattices extracted from the maps in A (see Appendix 1 for details). In each panel, the lattice with smaller (larger) scale is depicted in magenta (green), so white indicates activity in both lattices. (C) Measured scale ratios and orientation differences, which involves averaging over lattice vectors because the triangular lattices are sheared, and comparable lattice relationships by our model with predicted values. For the left panel, a discommensurate relationship is assigned by visual identification of discommensurations in the left panel of B. Because discommensurate lattices allow for a range of scale ratios with corresponding orientation differences, we performed linear regression on Figure 5E to obtain the predicted orientation difference that corresponds to the measured scale ratio. For the middle and right panels, commensurate lattice relationships are assigned by identifying the lattice points in the middle and right panels of B closest to, but not including, the center that exhibit significant overlap and comparing with the idealized relationships in Figure 5C. Note that our predicted values do not account for the shearing observed in the experimental grids, which will change scale ratios and orientation differences from their unsheared values even for idealized lattice relationships. Shearing may result from tethering of grids to environmental boundaries, perhaps through interactions with border cells (Keinath et al., 2018; Krupic et al., 2015; Stensola et al., 2015). (D–F) Same as A–C, but for two modules from Figure 2d of Krupic et al. (2015). A comprehensive test requires analysis of experiments using circular enclosures to eliminate confounding boundary effects (see Discussion).

Scale ratios across the assorted simulations span a range of values, but their averages are constant across module pairs. That is, the median scale ratio does not change between the pair of modules with smaller scales and the larger pair (Figure 7C). Similarly, mean values are respectively 1.52 ± 0.05 and 1.53 ± 0.05 (mean ± s.e.m.) for module pairs M2 and M1 and M3 and M2. Combining data from both module pairs gives scale ratio 1.52 ± 0.03 (mean ± s.e.m.), which agrees well with the mean value of 1.56 from Krupic et al. (2015). Stensola et al. (2012) reports a slightly smaller mean value of 1.42 ± 0.17 (mean ± s.d.; re-analyzed by Wei et al., 2015), but its broad distribution of scale ratios overlaps considerably with ours. Moreover, we find that the normalized scale difference does change its median across module pairs (Figure 7D). This result that scale ratios are constant on average but scale differences are not matches experiment (Stensola et al., 2012).

Thus, although our model can produce modules with fixed scale ratios, allowing for a range of network parameters also produces modules with a range of scale ratios. Nevertheless, the scale ratio averaged over these parameters is still constant across module pairs, a key feature of the grid system that holds even if scales are not governed by a universal ratio (Stensola et al., 2012).

### Testing for coupling: a mock lesion experiment

Excitatory coupling locks networks into scales and orientations imposed by more ventral networks. Disrupting the coupling frees networks from this rigidity, which can change scales and orientations far from the disruption. We demonstrate this effect by inactivating one network z = 7 midway through the simulation (Figure 8A). This corresponds experimentally to disrupting excitatory connections at one location along the dorsoventral MEC axis.

![Figure 8.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig8-v2.jpg)

**Figure 8.:** (A) Lesion protocol. The lesion inactivates network z = 7. (B) A representative simulation before the lesion. Top row: network activities at the end of the pre-lesion simulation. Second row: activity overlays between adjacent networks depicted in the top row. In each panel, the network with smaller (larger) z is depicted in magenta (green), so white indicates activity in both networks. Third row: spatial rate map of a single neuron for each z superimposed on the animal’s trajectory. White scale bars, 50 neurons. Black scale bars, 50 cm. (C) Same as B but after the lesion. Spatial rate maps are recorded from the same neurons as in B. (D, E) Data from 10 replicate simulations. (D) Left: spatial grid scales Λ(z) before and after the lesion. Middle: histogram for Λ collected across all networks. Right: spatial orientations Θ relative to the grid cell in the same simulation with largest scale. (E) Spatial scale ratios and orientation differences between adjacent modules. Standard parameter values provided in Table 1.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/46687/elife-46687-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A–C) A regional lesion of network z = 7 that spares the lower left quadrant. (A) A representative post-lesion simulation. Top row: network activities at the end of the post-lesion simulation. Second row: activity overlays between adjacent networks depicted in the top row. In each panel, the network with smaller (larger) z is depicted in magenta (green), so white indicates activity in both networks. Third row: spatial rate map of a single neuron for each z superimposed on the animal’s trajectory. Bottom row: spatial autocorrelations of the rate maps depicted in the third row. White scale bars, 50 neurons. Black scale bars, 50 cm. (B) Left: spatial grid scales Λ(z) before and after the lesion. Middle: histogram for Λ collected across all networks. Right: spatial orientations Θ relative to the grid cell in the same simulation with largest scale. For each z, two neurons are selected from the lower left quadrant and two neurons are selected from elsewhere. (C) Spatial scale ratios and orientation differences between adjacent modules. (D) A representative post-lesion simulation of a decimation of network n = 7 that spares the top left neuron in every 3 × 3 block. Rows same as the top three rows of A.

After the lesion, grid cells ventral to the lesion location (z ≥ 8) are unaffected, but those dorsal to the lesion location (z ≤ 6) change scale and orientation and form a single module (Figure 8B–D). Network z = 6 is no longer constrained by larger grids of more ventral networks, so its scale decreases. The coupling that remains from z = 6 to 1 then rigidly propagates the new grid down to network z = 1. This post-lesion module M1 has larger scale and 30º orientation difference compared to the pre-lesion M1; these changes also appear as corresponding changes in the scale ratio and orientation difference between modules M2 and M1 (Figure 8E).

Immediate changes in grid scale and/or orientation observed at one location along the longitudinal MEC axis due to a lesion at another location would strongly support the presence of the excitatory coupling predicted by our model. Moreover, the anatomical distribution of the changes would indicate the directionality of coupling; those in grid cells dorsal to the lesion would indicate ventral-to-dorsal coupling and those ventral to the lesion would indicate dorsal-to-ventral coupling.

We have also considered the consequences of certain incomplete lesions. A regional lesion, in which a corner of the lesioned network z = 7 is preserved, causes each more dorsal network to contain regions with different scales (Figure 8—figure supplement 1 and Figure 8—video 1). These differences are not large enough to create a new module close to the lesioned network (z = 5 and 6), so scale ratios and orientations are not strongly affected. However, different regions of each network will independently transition to the smallest module farther away from the lesioned network (z = 1 to 4). Thus, one network corresponding to a single location along the dorso-ventral MEC axis can contain grid cells belonging to two modules. Experimentally, grid modules do overlap in their anatomic extent along the MEC axis (Stensola et al., 2012); our model predicts that this overlap may be enhanced by a regional lesion. Note that some neurons also appear to show band-like spatial rate maps (z = 4 and 6 in Figure 8—figure supplement 1A), whose experimental observation has been reported (Krupic et al., 2012) but disputed (Navratilova et al., 2016). We also performed a decimation-type lesion, in which one neuron of every 3 × 3 block is preserved in the lesioned network. This impedes the motion of the grid pattern on the neural sheet in more dorsal networks (Figure 8—video 2) and thus destroys single neuron grid responses in those networks (Figure 8—figure supplement 1D).

## Discussion

We propose that the hierarchy of grid modules in the MEC is self-organized by competition in attractor networks between excitation along the longitudinal MEC axis and lateral inhibition. We showed that such an architecture, with an inhibition distance that increases smoothly along the MEC axis, reproduces a central experimental finding: grid cells form modules with scales clustered around discrete values (Stensola et al., 2012; Barry et al., 2007; Krupic et al., 2015).

The distribution of scales across modules in our model quantitatively matches experiments. Different groups have reported mean scale ratios of 1.64 (6 module pairs), 1.42 (24 module pairs), and 1.56 (11 module pairs) (Barry et al., 2007; Stensola et al., 2012; Krupic et al., 2015). These data could be interpreted as an indication that the grid system has a preferred scale ratio roughly in range of 1.4–1.7. As we showed, our model naturally produces a hierarchy of modules with scale ratios in this range; its network parameters lead to both commensurate and discommensurate grids (Figure 5). On the other hand, the data on scale ratios between individual pairs of modules actually span a range of values in the different experiments: 1.6–1.9, 1.1–1.8, and 1.2–2.0 (Barry et al., 2007; Stensola et al., 2012; Krupic et al., 2015). This suggests that the underlying mechanism that produces grid modules must be capable of producing different scale ratios as its parameters vary. This is indeed the case for our model, in which variation of network parameters produces a realistic range of scale ratios (Figure 7). Despite variability across individual scale ratios, experiments strikingly reveal that the average scale ratio is the same from the smallest pair of modules to the largest pair, whereas the average scale difference changes across the hierarchy (Stensola et al., 2012). Our model robustly reproduces this observation (Figure 7C,D) because its fundamental mechanism of geometric coordination between grids enforces constant-on-average scale ratios even with variation in parameters among individual networks.

Our model requires that grid orientation be co-modular with scale, as observed in experiment (Stensola et al., 2012). Studies characterizing the statistics of orientation differences between modules are limited, but values seem to span the entire range 0°–30°, with some preference for values at the low and high ends of this range (Krupic et al., 2015). Our model can capture the entire range of orientation differences with discommensurate relationships favoring small differences and commensurate relationships favoring large differences (Figure 5). Overall, our model predicts a positive correlation between scale ratio and orientation difference (Figure 5E and Figure 7B), which can be tested experimentally. Existing datasets (Stensola et al., 2012; Krupic et al., 2015) have a confound—animals are tested in square and rectangular enclosures which have distinguishable orientations marked by the corners. Grid orientations can anchor to such features (Stensola et al., 2015), either through the integration of visual and external cues (Raudies and Hasselmo, 2015; Savelli et al., 2017), or through interaction with boundaries (Bush and Burgess, 2014; Krupic et al., 2016; Giocomo, 2016; Evans et al., 2016; Hardcastle et al., 2017; Keinath et al., 2018; Ocko et al., 2018). Experiments in circular or other non-rectangular environments may help disambiguate the effects of such anchoring. Our model also predicts that orientation differences between modules will be preserved between environments with different geometries since the differences are internally generated by the dynamics of the network. This effect has been observed (Krupic et al., 2015).

Our model produces consistent differences in firing rate from one grid field to another for some grid cells. This variability is structured because it arises at module interfaces from the selective excitation of some network activity peaks in the smaller-scale grid by the overlapping activity peaks of the larger-scale grid. Such an explanation for firing rate variability has been suggested by Ismakov et al. (2017). Signatures of structured variability can be sought in experimental grid cell recordings (see Figure 6—figure supplement 2 for an example). However, these signatures may be obscured by other sources of grid variability, such as proposed inputs from place cells (Dunn et al., 2017) and the observed modulation of grid fields by reward (Butler et al., 2019; Boccara et al., 2019), which may in turn be also related to hippocampal input.

Our model requires excitatory coupling between grid cells at different locations along the longitudinal MEC axis, either through direct excitation or disinhibition (Fuchs et al., 2016). Short-range excitatory connections between principal neurons in superficial MEC layers have been discovered recently through patch clamp experiments (Fuchs et al., 2016; Winterer et al., 2017). These neurons also make long-range projections to superficial layers of the contralateral MEC (Varga et al., 2010; Fuchs et al., 2016), where they connect to other principal cells (Zutshi et al., 2018). The validity of our model would be bolstered if similar connections were found between locations along the MEC that correspond to different grid modules.

The presence of excitatory coupling can also be tested indirectly. We predict that the destruction of grid cells, or inactivation of excitatory coupling (Zutshi et al., 2018), at a given location along the axis will change grid scales and/or orientations at other locations (Figure 8). The presence of noise correlations across modules, as previously investigated but not fully characterized (Mathis et al., 2013; Tocker et al., 2015), would suggest connections between modules. Such correlations, and perhaps even lattice relationships, could be observed via calcium imaging of the MEC (Heys et al., 2014; Gu et al., 2018). The effect of environmental manipulations on grid relationships has been suggested to demonstrate both independence (Stensola et al., 2012) and dependence (Krupic et al., 2015) across modules. However, (Keinath et al., 2018) showed that apparent deformations of grids after changes in environmental shape may result in part from learned interactions with boundaries, perhaps mediated by border cells. Thus, environmental deformation paradigms may not be ideal tests of our model due to confounding boundary effects (Keinath et al., 2018; Ocko et al., 2018).

Our predictions may be altered by synaptic plasticity, which we do not implement in our model. Spike-timing-dependent plasticity rules are capable of creating the recurrent inhibitory architecture required by continuous attractor models of a single grid module (Widloski and Fiete, 2014). As for our model with multiple modules, synaptic plasticity within the inhibitory connections may resolve the competition between excitation and inhibition by adjusting the inhibition distance in each network to the value favored by the rigidity of excitatory coupling. In that case, lesioning one network would not affect the grid scales of other networks, although changes in orientation differences may be observed over time due to attractor drift. Nevertheless, our proposed geometric mechanism could still govern the initial formation of modules with certain scale ratios before plasticity fully takes effect.

Since spatial grid scales are both proportional to inhibition distance l and inversely proportional to velocity gain $\alpha$ (Burak and Fiete, 2009 and Materials and methods), we also simulated excitatorily coupled networks with a depth-dependent velocity gain α(z) and a fixed inhibition distance l (Appendix 2). In contrast to simulations in one dimension (J Widloski and I Fiete, personal communication, October 2017), while we observed module self-organization, the system gave inconsistent results among replicate simulations and lacked fixed scale ratios. Moreover, recent calcium imaging experiments suggest that activity on the MEC is arranged a deformed triangular lattice (Gu et al., 2018), as predicted by the continuous attractor model (Burak and Fiete, 2009), and that regions with activity separated by larger anatomic distances contain grid cells of larger spatial scale. These observations support a changing inhibition distance over a changing velocity gain as a mechanism for producing different grid scales, under the assumption that anatomic and network distances correspond to each other.

Our results differ from previous work on mechanisms for forming grid modules. Grossberg and Pilly hypothesize that grid cells arise from stripe cells in parasubiculum, and that discreteness in the spatial period of stripe cells leads to modularity of grid cells (Grossberg and Pilly, 2012). However, stripe cells have only been observed once (Krupic et al., 2012; Navratilova et al., 2016), and the origin of discrete periods with constant-on-average ratios in stripe cells would then need to be addressed. Urdapilleta, Si, and Treves propose a model in which discrete modules self-organize from smooth gradients in parameters in a model where grid formation is driven by firing rate adaptation in single cells (Urdapilleta et al., 2017). They also utilize excitatory coupling among grid cells along the longitudinal MEC axis. However, this model does not have a mechanism to dynamically enforce the average constancy of grid scale ratios, which is a feature of the grid system (Stensola et al., 2012). Furthermore, it produces modules with orientation differences near zero and does not demonstrate values near 30° (Krupic et al., 2015). Our model naturally produces constant-on-average scale ratios and allows for a wide range of orientation differences. Moreover, over the past few years, multiple reports have provided independent experimental support for the importance of recurrent connections among grid cells (Couey et al., 2013; Dunn et al., 2015; Fuchs et al., 2016; Zutshi et al., 2018) and for the continuous attractor model in particular (Yoon et al., 2013; Heys et al., 2014; Gu et al., 2018). Our work establishes that continuous attractor networks can produce a discrete hierarchy of modules with a constant-on-average scale ratio.

The competition generated between excitatory and inhibitory connections bears a strong resemblance to the Frenkel-Kontorova model of condensed matter physics, in which a periodic potential of one scale acts on particles that prefer to form a lattice of a different, competing scale (Kontorova and Frenkel, 1938). This model has a rich literature with many deep theoretical results, including the calculation of complicated phase diagrams involving ‘devil’s staircases’ (Bak, 1982; Chaikin and Lubensky, 1995) which mirror those of our model (Figure 5). Under certain conditions, our model produces networks with quasicrystalline approximant grids that are driven by networks with standard triangular grids at other scales (Appendix 3). Quasicrystalline order lacks periodicity, but contains more nuanced positional order (Levine and Steinhardt, 1986). This phenomenon wherein quasicrystalline structure is driven by crystalline order in a coupled system was recently observed for the first time in thin-film materials that contain Frenkel-Kontorova-like interactions (Förster et al., 2013; Förster et al., 2016; Paßens et al., 2017).

Commensurate and discommensurate lattice relationships are a robust and versatile mechanism for self-organizing a grid system whose scale ratios are constant or constant on average across a hierarchy of modules. We demonstrated this mechanism in a basic extension of the continuous attractor model with excitatory connections between networks. This model is amenable to extensions that capture other features of the grid system, such as fully spiking dynamics, learning of synaptic weights (Widloski and Fiete, 2014), the union of our separate networks into a single network spanning the entire MEC, and the addition of border cell inputs or recurrent coupling between modules to correct path-integration errors or react to environmental deformations (Hardcastle et al., 2015; Keinath et al., 2018; Ocko et al., 2018; Pollock et al., 2017; Mosheiff and Burak, 2019).

## Materials and methods

### Model setup and dynamics

We implemented the Burak-Fiete model (Burak and Fiete, 2009) as follows (Source code 1). Networks $z=1,…,h$ each contain a 2D sheet of neurons with indices $𝐫=(x,y)$, where $x=1,…,n$ and $y=1,…,n$. Neurons receive broad excitatory input $a⁢(𝐫)$ from the hippocampus, and, to prevent edge effects, those toward the center of the networks receive more excitation than those toward the edges. Each neuron also inhibits others that lie around a length scale of $l⁢(z)$ neurons away in the same network $z$. Moreover, every neuron belongs to one of four subpopulations that evenly tile the neural sheet. Each subpopulation is associated with both a preferred direction $𝐞^$ along one of the network axes $\pm𝐱^$ or $\pm𝐲^$ and a corresponding preferred direction $𝐄^$ along an axis $\pm𝐗^$ or $\pm𝐘^$ in its spatial environment. A neuron at position $𝐫$ in network $z$ has its inhibitory outputs $w⁢(𝐫;z)$ shifted slightly by $ξ$ neurons in the $𝐞^⁢(𝐫)$ direction and its broad excitation modulated by a small amount proportional to $𝐄^⁢(𝐫)⋅𝐕$, where $𝐕$ is the spatial velocity of the animal. Note that lowercase letters refer to attractor networks at each depth $z$ in which distances have units of neurons, and uppercase letters refer to the animal’s spatial environment in which distances have physical units, such as centimeters.

In addition to these established features (Burak and Fiete, 2009), we introduce excitatory connections $u⁢(𝐫)$ from every neuron $𝐫$ in network $z$ to neurons located within a spread $d$ of the same $𝐫$ but in the preceding network with depth $z−1$. $u⁢(𝐫)$ is constant for all networks. These components lead to the following dynamical equation for the dimensionless neural firing rates $s⁢(𝐫,z,t)$:

$$
\tau\frac{s(r,z,t+Δt)−s(r,z,t)}{Δt}+s(r,z,t)={\sumr^{′}w(r−r^{′}+ξe^(r^{′});z)s(r^{′},z,t)+\sumr^{′}u(r−r^{′})s(r^{′},z+1,t)+a(r)[1+\alphaE^(r)⋅V(t)]}_{+}.
$$

Inputs to each neuron are rectified by ${c}_{+}=0$ for $c<0$, $c$ for $c\geq0$. $Δt$ is the simulation time increment, $\tau$ is the neural relaxation time, and $\alpha$ is the velocity gain that describes how much the animal’s velocity $𝐕$ modulates the broad inputs $a⁢(𝐫)$. Note that $s$ can be treated as a dimensionless variable because Equation 1 is invariant to scaling of $s$ and $a$ by the same factor.

We use velocities $𝐕⁢(t)$ corresponding to a real rat trajectory (Hafting et al., 2005; Burak and Fiete, 2009). Details are provided in Appendix 1.

### Inhibitory and excitatory connections

The broad excitatory input is

$$
a(r)={a_{mag}e^{−a_{fall}r_{scaled}^{2}}r_{scaled}<10r_{scaled}\geq1,
$$

where $r_{scaled}=\sqrt{(x−\frac{n+1}{2})^{2}+(y−\frac{n+1}{2})^{2}}/\frac{n}{2}$ is a scaled radial distance for the neuron at $𝐫=(x,y)$, $a_{mag}$ is the magnitude of the input, and $a_{fall}$ is a falloff parameter. The inhibition distance for network $z$ is

$$
l⁢(z)=[l_{min}^{l_{exp}}+(l_{max}^{l_{exp}}-l_{min}^{l_{exp}})⁢\frac{z-1}{h-1}]^{1/l_{exp}},
$$

which ranges from $l_{min}=l⁢(1)$ to $l_{max}=l⁢(h)$ with concavity tuned by $l_{exp}$. More negative values of $l_{exp}$ lead to greater concavity; for $l_{exp}=0$, we use the limiting expression $l⁢(z)=l_{min}^{(h-z)/(h-1)}⁢l_{max}^{(z-1)/(h-1)}$. The recurrent inhibition profile for network $z$ is

$$
w(r;z)={−\frac{w_{mag}}{l(z)^{2}}\frac{1−cos⁡[\pir/l(z)]}{2}r<2l(z)0r\geq2l(z),
$$

where $w_{mag}$ is the magnitude of inhibition. We scale this magnitude by $l⁢(z)^{-2}$ to make the integrated inhibition constant across $z$. The excitatory coupling is

$$
u(r)={\frac{u_{mag}}{d^{2}}\frac{1+cos⁡[\pir/d]}{2}r<d0r\geqd,
$$

where $u_{mag}$ and $d$ are the magnitude and spread of coupling, respectively. In analogy to $w_{mag}$, we scale $u_{mag}$ by $d^{-2}$.

### Overview of data analysis techniques

To determine spatial grid scales, orientations, and gridness, we consider an annular region of the spatial autocorrelation map that contains the six peaks closest to the origin. Grid scale is the radius with highest value, averaging over angles. Grid orientation and gridness are determined by first averaging over radial distance and analyzing the sixth component of the Fourier series with respect to angle (Weber and Sprekeler, 2019). The power of this component divided by the total Fourier power measures ‘gridness’ and its complex phase measures the orientation. Grid cells are subject to a gridness cutoff of 0.6. For each replicate simulation, we cluster its grid cells with respect to scale and orientation using a $k$-means procedure with $k$ determined by kernel smoothed densities (Stensola et al., 2012). See Appendix 1 for full details.
