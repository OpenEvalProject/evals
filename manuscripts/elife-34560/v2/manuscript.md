# Learning place cells, grid cells and invariances with excitatory and inhibitory plasticity

## Authors

- Simon Nikolaus Weber<sup>1</sup> ([ORCID: 0000-0002-1169-9879](https://orcid.org/0000-0002-1169-9879)) †
- Henning Sprekeler<sup>1</sup> ([ORCID: 0000-0003-0690-3553](https://orcid.org/0000-0003-0690-3553)) †

### Affiliations

1. Modelling of Cognitive Processes, Institute of Software Engineering and Theoretical Computer Science Technische Universität Berlin Berlin Germany

† Corresponding author

## Abstract

Neurons in the hippocampus and adjacent brain areas show a large diversity in their tuning to location and head direction, and the underlying circuit mechanisms are not yet resolved. In particular, it is unclear why certain cell types are selective to one spatial variable, but invariant to another. For example, place cells are typically invariant to head direction. We propose that all observed spatial tuning patterns – in both their selectivity and their invariance – arise from the same mechanism: Excitatory and inhibitory synaptic plasticity driven by the spatial tuning statistics of synaptic inputs. Using simulations and a mathematical analysis, we show that combined excitatory and inhibitory plasticity can lead to localized, grid-like or invariant activity. Combinations of different input statistics along different spatial dimensions reproduce all major spatial tuning patterns observed in rodents. Our proposed model is robust to changes in parameters, develops patterns on behavioral timescales and makes distinctive experimental predictions.

## Introduction

Neurons in the hippocampus and the adjacent regions exhibit a broad variety of spatial activation patterns that are tuned to position, head direction or both. Common observations in these spatial dimensions are localized, bell-shaped tuning curves (O'Keefe, 1976; Taube et al., 1990), periodically repeating activity (Fyhn et al., 2004; Hafting et al., 2005) and invariances (Muller et al., 1994; Burgess et al., 2005), as well as combinations of these along different spatial dimensions (Sargolini et al., 2006a; Krupic et al., 2012). For example, head direction cells are often invariant to location (Burgess et al., 2005), and place cells are commonly invariant to head direction (Muller et al., 1994). The cellular and network mechanisms that give rise to each of these firing patterns are subject to extensive experimental and theoretical research. Several computational models have been suggested to explain the emergence of grid cells (Fuhs and Touretzky, 2006; McNaughton et al., 2006; Franzius et al., 2007a; Burak and Fiete, 2009; Couey et al., 2013; Burgess et al., 2007; Kropff and Treves, 2008; Bush and Burgess, 2014; Castro and Aguiar, 2014; Dordek et al., 2016; Stepanyuk, 2015; Giocomo et al., 2011; Zilli, 2012; D'Albis and Kempter, 2017; Monsalve-Mercado and Leibold, 2017), place cells (Tsodyks and Sejnowski, 1995; Battaglia and Treves, 1998; Arleo and Gerstner, 2000; Solstad et al., 2006; Franzius et al., 2007b; Burgess and O'Keefe, 2011; Franzius et al., 2007a) and head direction cells (McNaughton et al., 1991; Redish et al., 1996; Zhang, 1996; Franzius et al., 2007a). Most of these models are designed to explain the spatial selectivity of one particular cell type and do not consider invariances along other dimensions, although the formation of invariant representations is a non-trivial problem (DiCarlo and Cox, 2007). In view of the variety of spatial tuning patterns, the question arises of whether differences in tuning of different cells in different areas reflect differences in microcircuit connectivity, single cell properties or plasticity rules, or whether there is a unifying principle. In this paper we suggest that both the observed spatial selectivities and invariances can be explained by a common mechanism – interacting excitatory and inhibitory synaptic plasticity – and that the observed differences in the response profiles of grid, place and head direction cells result from differences in the spatial tuning of excitatory and inhibitory synaptic afferents. Here, we explore this hypothesis in a computational model of a feedforward network of rate-based neurons. Simulations as well as a mathematical analysis indicate that the model reproduces the large variety of response patterns of neurons in the hippocampal formation and adjacent areas and can be used to make predictions for the input statistics of each cell type.

## Results

We study the development of spatial representations in a network of rate-based neurons with interacting excitatory and inhibitory plasticity. A single model neuron that represents a cell in the hippocampal formation or adjacent areas receives feedforward input from excitatory and inhibitory synaptic afferents. As a simulated rat moves through an environment, these synaptic afferents are weakly modulated by spatial location and in later sections also by head direction. This modulation is irregular and non-localized with multiple maxima (Buetfering et al., 2014); see Figure 1a and Materials and methods. Importantly, different inputs show different modulation profiles and each profile is temporally stable. We also show results for localized, that is, place cell-like, input (O'Keefe and Dostrovsky, 1971; Marshall et al., 2002; Wilent and Nitz, 2007). The output rate is given by a weighted sum of the excitatory and inhibitory inputs.

![Figure 1.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig1-v2.jpg)

**Figure 1.:** (a) Network model for a linear track. A threshold-linear output neuron (gray) receives input from excitatory (red) and inhibitory (blue) cells, which are spatially tuned (curves on top and bottom). (b) Spatially tuned input with smoother inhibition than excitation. The fluctuating curves (top) show two exemplary spatial tunings (one is highlighted) of excitatory and inhibitory input neurons. Interacting excitatory and inhibitory synaptic plasticity gradually changes an initially random response of the output neuron (firing rate $r^{out}$) into a periodic, grid cell-like activity pattern. (c) If the spatial tuning of inhibitory input neurons is less smooth than that of excitatory input neurons, the interacting excitatory and inhibitory plasticity leads to a spatially invariant firing pattern. The output neuron fires close to the target rate of 1 Hz everywhere. (d) For very smooth or spatially untuned inhibitory inputs, the output neuron develops a single firing field, reminiscent of a place cell. (e) The mechanism, illustrated for place cell-like input. When a single excitatory weight is increased relative to the others, the balancing inhibitory plasticity rule leads to an immediate increase of inhibition at the associated location. If inhibitory inputs are smoother than excitatory inputs, the resulting approximate balance creates a center surround field: a local overshoot of excitation (firing field) surrounded by an inhibitory corona. The next firing field emerges at a distance where the inhibition has faded out. Iterated, this results in a spatially periodic arrangement of firing fields. (f) Inputs with place field-like tuning. Gaussian curves (top) show the spatial tuning of excitatory and inhibitory input neurons (one neuron of each kind is highlighted, 20 percent of all inputs are displayed). A grid cell firing pattern emerges from an initially random weight configuration. (g) Grid spacing $ℓ$ scales with inhibitory tuning width $\sigma_{I}$. Simulation results (dots) agree with a mathematical bifurcation analysis (solid). Output firing rate examples at the two indicated locations are shown at the bottom. (h) Inhibitory smoothness $\sigma_{I,corr}$ controls grid spacing; arrangement as in (d). Note that the time axes in (b,c,d,f) are different, because the speed at which the patterns emerge is determined by both the learning rates of the plasticity and the firing rate of the input neurons. We kept the learning rate constant and adjusted the simulation times to achieve convergence. Choosing identical simulation times, but different learning rates, leads to identical results (Figure 1—figure supplement 2). Rat clip art from [https://openclipart.org/detail/216359/klara; 2015].

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Depicted are the standard deviation (STD) and the coefficient of variation (CV) of excitatory (left) and inhibitory (right) weights as a function of the number of place fields per input neuron. The values are computed after the output neuron has established a stable grid pattern on a linear track. For excitatory weights, the CV decreases significantly with non-localized input. This indicates that different firing patterns in the output neuron are closer in ‘weight space’ for non-localized input. In other words, to obtain a different firing pattern, the weights must be modified by a lesser amount, that is, the configuration and thus the output pattern is less robust: An explanation for the defects in grids with non-localized input.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Top row: Each simulation with the same parameters as in Figure 1. Number of time steps and learning rates are indicated close to each plot.Bottom row: Same simulations as in top row, but with different excitatory and inhibitory learning rates and different number of simulation time steps.The two rows show basically identical time evolutions for the firing pattern of the output cell.As expected from the mathematical analysis, scaling the excitatory and inhibitory learning rates does not have an influence on the firing pattern of the output neuron, as long as learning is sufficiently slow.

In our model, both excitatory and inhibitory synaptic weights are subject to plasticity. The excitatory weights change according to a Hebbian plasticity rule (Hebb, 1949) that potentiates the weights in response to simultaneous pre- and postsynaptic activity. The inhibitory synapses evolve according to a plasticity rule that changes their weights in proportion to presynaptic activity and the difference between postsynaptic activity and a target rate (1 Hz in all simulations). This rule has previously been shown to balance excitation and inhibition such that the firing rate of the output neuron approaches the target rate (Vogels et al., 2011; D'Amour and Froemke, 2015). We assume the inhibitory plasticity will act fast enough to track changes of excitatory weights, so that excitation and inhibition are approximately balanced at all times.

### Relative spatial smoothness of the excitatory and inhibitory input determines the firing pattern of the output neuron

We first simulate a rat that explores a linear track (Figure 1). The spatial tuning of each input neuron is stable in time and depends smoothly on the location of the animal, but is otherwise random (e.g. Figure 1a). As a measure of smoothness, we use the spatial autocorrelation length. In the following, this is the central parameter of the input statistics, which is chosen separately for excitation and inhibition. In short, we assume that temporally stable spatial information is presynaptically present but we have minimal requirements on its format, aside from the spatial autocorrelation length.

At the beginning of each simulation, all synaptic weights are random. As the animal explores the track, the excitatory and inhibitory weights change in response to pre- and postsynaptic activity, and the output cell gradually develops a spatial activity pattern. We find that this pattern is primarily determined by whether the excitatory or inhibitory inputs are smoother in space. If the inhibitory tuning is smoother than the excitatory tuning (Figure 1b), the output neuron develops equidistant firing fields, reminiscent of grid cells on a linear track (Hafting et al., 2008). If instead the excitatory tuning is smoother, the output neuron fires close to the target rate of 1 Hz everywhere (Figure 1c); it develops a spatial invariance. For spatially untuned inhibitory afferents (Grienberger et al., 2017), the output neuron develops a single firing field, reminiscent of a one-dimensional place cell (Figure 1d); (cf. Clopath et al., 2016).

The emergence of these firing patterns can be best explained in the simplified scenario of place field-like input tuning (Figure 1e,f). The spatial smoothness is then given by the size of the place fields. Let us assume that the output neuron fires at the target rate everywhere (see Materials and methods). From this homogeneous state, a small potentiation of one excitatory weight leads to an increased firing rate of the output neuron at the location of the associated place field (highlighted red curve in Figure 1e). To bring the output neuron back to the target rate, the inhibitory learning rule increases the synaptic weight of inhibitory inputs that are tuned to the same location (highlighted blue curve in Figure 1e). If these inhibitory inputs have smaller place fields than the excitatory inputs (Figure 1c), this restores the target rate everywhere (Vogels et al., 2011). Hence, inhibitory plasticity can stabilize spatial invariance if the inhibitory inputs are sufficiently precise (i.e. not too smooth) in space. In contrast, if the spatial tuning of the inhibitory inputs is smoother than that of the excitatory inputs, the target firing rate cannot be restored everywhere. Instead, the compensatory potentiation of inhibitory weights increases the inhibition in a spatial region at least the size of the inhibitory place fields. This leads to a corona of inhibition, in which the output neuron cannot fire (Figure 1e, blue region). Outside of this inhibitory surround the output neuron can fire again and the next firing field develops. Iterated, this results in a periodic arrangement of firing fields (Figure 1f and Figure 7b for a depiction of the input currents). Spatially untuned inhibition corresponds to a large inhibitory corona that exceeds the length of the linear track, so that only a single place field remains. From a different perspective, spatially untuned input can also be understood as a limit case of vanishing spatial variation in the firing rate rather than a limit of infinite smoothness. Consistent with this view, a development of grid patterns or invariance requires a sufficiently strong spatial modulation of the inhibitory inputs (Materials and methods).

The argument of the preceding paragraph can be extended to the scenario where input is irregularly modulated by space. For non-localized input tuning (Figure 1b,c,d), any weight change that increases synaptic input in one location will also increase it in a surround that is given by the smoothness of the input tuning (see Materials and methods for a mathematical analysis). In the simulations, the randomness manifests itself in occasional defects in the emerging firing pattern (Figure 1h, bottom, and Figure 1—figure supplement 1). The above reasoning suggests that the width of individual firing fields is determined by the smoothness of the excitatory input tuning, while the distance between grid fields, that is, the grid spacing, is set by the smoothness of the inhibitory input tuning. Indeed, both simulations and a mathematical analysis (Materials and methods) confirm that the grid spacing scales linearly with the inhibitory smoothness in a large range, both for localized (Figure 1g) and non-localized input tuning (Figure 1h). The analysis also reveals a weak logarithmic dependence of the grid spacing on the ratio of the learning rates, the mean firing rates and the number of afferents of the excitatory and inhibitory population (Equation 78 and Figure 8b).

In summary, the interaction of excitatory and inhibitory plasticity can lead to spatial invariance, spatially periodic activity patterns or single place fields depending on the spatial statistics of the excitatory and inhibitory input.

### Emergence of hexagonal firing patterns

When a rat navigates in a two-dimensional arena, the spatial firing maps of grid cells in the medial entorhinal cortex (mEC) show pronounced hexagonal symmetry (Hafting et al., 2005; Fyhn et al., 2004) with different grid spacings and spatial phases. To study whether a hexagonal firing pattern can emerge from interacting excitatory and inhibitory plasticity, we simulate a rat in a quadratic arena. The rat explores the arena for 10 hr, following trajectories extracted from behavioral data (Sargolini et al., 2006b); Materials and methods. To investigate the role of the input statistics, we consider three different classes of input tuning: (i) place cell-like input (Figure 2a), (ii) sparse non-localized input, in which the tuning of each input neuron is given by the sum of 100 randomly located place fields (Figure 2b and (iii) dense non-localized input, in which the tuning of each input is a random function with fixed spatial smoothness (Figure 2c). For all input classes, the spatial tuning of the inhibitory inputs is smoother than that of the excitatory inputs.

![Figure 2.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig2-v2.jpg)

**Figure 2.:** (a,b,c) Columns from left to right: Spatial tuning of excitatory and inhibitory input neurons (two examples each); spatial firing rate map of the output neuron and corresponding autocorrelogram before and after spatial exploration of 10 hr. The number on the correlogram shows the associated grid score. Different rows correspond to different spatial tuning characteristics of the excitatory and inhibitory inputs. For all figures the spatial tuning of inhibitory input neurons is smoother than that of excitatory input neurons. (a) Each input neuron is a place cell with random location. (b) The tuning of each input neuron is given as the sum of 100 randomly located place fields. (c) The tuning of each input neuron is a random smooth function of the location. This corresponds to the sum of infinitely many randomly located place fields. Before learning, the spatial tuning of the output neuron shows no symmetry. After 10 hr of spatial exploration the output neuron developed a hexagonal pattern. (d) Grid score histogram for 500 output cells with place cell-like input. Before learning (light blue), 33% of the output cells have a positive grid score. After 10 hr of spatial exploration (dark blue), this value increases to 86%. Two example rate maps are shown. The arrows point to the grid score of the associated rate map. Even for low grid scores the learned firing pattern looks grid-like. (e,f) Grid score histograms for input tuning as in (b,c), arranged as in (d). (g) Fraction of neurons with positive grid score before (light blue) and after learning (dark blue) as a function of the number of fields per input neuron. Note that to learn within 10 hr of exploration time, we used different learning rates for different input scenarios. Using identical learning rates for all input scenarios but adjusting the simulation times to achieve convergence leads to identical results (Figure 2—figure supplement 6).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Box plot of the cross correlations of the rate maps after learning of 500 simulations (i.e. $(500^{2}-500)/2=124750$ cross correlations). For each set of 500 simulations, only the parameter that is indicated on the $x-$axis was varied. A high cross correlation indicates that different simulations lead to similar grids and thus points towards a low influence of the varied parameter on the final grid pattern. We conclude that the influence on the final grid pattern in decreasing order is given by the parameters: Initial synaptic weights, trajectory of the rat, input tuning (i.e. locations of the randomly located input tuning curves). As expected, the correlation is lowest, if all parameters are different in each simulation (rightmost box). Each box extends from the first to the third quartile, with a dark blue line at the median. The lower whisker reaches from the lowest data point still within 1.5 IQR of the lower quartile, and the upper whisker reaches to the highest data point still within 1.5 IQR of the upper quartile, where IQR is the inter quartile range between the third and first quartile. Dots show flier points. See Appendix 1 for details on how trajectories, synaptic weights and inputs are varied.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (a) Arrangement as in Figure 2a but with place cell-like excitatory input and sparse non-localized inhibitory input (sum of 50 randomly located place fields). A hexagonal pattern emerges, comparable with that given in Figure 2a,b,c. (b) Grid score histogram of 500 realizations with mixed input statistics as in (a). Arrangement as in Figure 2d.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (a) Simulations in a square box with input place fields that are arranged on a symmetric grid. From top to bottom: Firing rate map and corresponding autocorrelogram for an example grid cell; peak locations of 36 grid cells. The clusters at orientation of 0, 30, 60 and 90 degrees (red lines) indicate that the grids tend to be aligned to the boundaries. (b) Simulations in a circular box with input place fields that are arranged on a symmetric grid. Arrangement as in (a). The grids show no orientation preference, indicating that the orientation preference in (a) is induced by the square shape of the box. (c) Simulations in a square box with input place fields that are arranged on a distorted grid (see Figure 2—figure supplement 5). Arrangement as in (a). The grids show no orientation preference, indicating that the influence of the boundary on the grid orientation is small compared with the effect of randomness in the location of the input centers.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** In all simulations in the main text we used quadratic multiplicative normalization for the excitatory synaptic weights – a conventional normalization scheme. This choice was not crucial for the emergence of patterns. (a) Firing rate map of a cell before it started exploring its surroundings. (b) From left to right: Firing rate of the output cell after 1 hr of spatial exploration for inactive, linear multiplicative, quadratic multiplicative and linear subtractive normalization. (c) Time evolution of excitatory and inhibitory weights for the simulations shown in (b). The colored lines show 200 individual weights. The black line shows the mean of all synaptic weights. From left to right: Inactive, linear multiplicative, quadratic multiplicative and linear subtractive normalization. Without normalization, the mean of the synaptic weights grows strongest and would grow indefinitely. On the normalization schemes: Linear multiplicative normalization keeps the sum of all weights constant by multiplying each weight with a factor in each time step. Linear subtractive normalization keeps the sum of all weights roughly constant by adding or subtracting a factor from all weights and ensuring that negative weights are set to zero. Quadratic multiplicative normalization is explained in Materials and methods.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Black square box: Arena in which the simulated rat can move (side length $L$). Blue circles: Locations of input firing fields. To create random place field locations that cover the space densely, we use locations from a distorted lattice. To this end we first create a symmetric lattice with $N_{x}$ locations along the $x$-direction and $N_{y}$ locations along the $y$-direction. To reduce boundary effects, these centers can lie a certain distance outside the boundary (typically taken as threefold the width of the Gaussian input fields). We then add noise from a uniform distribution (blue square) to each location and obtain a distorted lattice (right). See Appendix 1 for more details on the choice of input functions.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** This is the same figure as Figure 2a,b,c but with identical learning rates for all three input scenarios: $η_{E}=2\times10^{−6}$, $η_{I}=8\times10^{−6}$. To obtain similar results to those in Figure 2, we need to increase the simulation times. The exploration times for the three scenarios, from top to bottom, are: 335, 10 and 50 hr. Longer simulation times are needed for inputs with lower mean firing rate, because this corresponds to an effectively lower learning rate; compare to mathematical analysis. Note that 100 fields per neurons have a larger mean firing rate than the Gaussian random fields, because the Gaussian random fields are scaled to have a mean firing rate of 0.5 Hz (see Materials and methods). As in in one dimension, scaling the excitatory and inhibitory learning rates does not have an influence on the firing pattern of the output neuron, as long as learning is sufficiently slow. Note that the patterns here are not identical to the patterns in Figure 2 because of a different random initialization.

Initially, all synaptic weights are random and the activity of the output neuron shows no spatial symmetry. While the rat forages through the environment, the output cell develops a periodic firing pattern for all three input classes, reminiscent of grid cells in the mEC (Fyhn et al., 2004; Hafting et al., 2005) and typically with the same hexagonal symmetry. This hexagonal arrangement is again a result of smoother inhibitory input tuning, which generates a spherical inhibitory corona around each firing field (compare Figure 1e). These center-surround fields are arranged in a hexagonal pattern – the closest packing of spheres in two dimensions; (cf. Turing, 1952). We find that the spacing of this pattern is determined by the inhibitory smoothness. The similarity between cells in terms of orientation and phase of the grid depends – in decreasing order – on whether they receive the same inputs, on the trajectories on which the tuning was learned and on the initial synaptic weights (Figure 2—figure supplement 1). Two grid cells can thus have different phase and orientation, even if they share a large fraction or all of their inputs.

For the linear track, the randomness of the non-localized inputs leads to defects in the periodicity of the grid pattern. In two dimensions, we find that the randomness leads to distortions of the hexagonal grid. To quantify this effect, we simulated 500 random trials for each of the three input scenarios and plotted the grid score histogram (Appendix 1) before and after 10 hr of spatial exploration (Figure 2d,e,f). Different trials have different trajectories, different initial synaptic weights and different random locations of the input place fields (for sparse input) or different random input functions (for dense input). For place cell-like input, most of the output cells develop a positive grid score during 10 hr of spatial exploration (33% before to 86% after learning, Figure 2d). Even for low grid scores, the firing rate maps look grid-like after learning but exhibit a distorted symmetry (Figure 2d). For sparse non-localized input, the fraction of output cells with a positive grid score increases from 35% to 87% and for dense non-localized input from 16% to 68% within 10 hr of spatial exploration (Figure 2e,f). The excitatory and inhibitory inputs are not required to have the same tuning statistics. Grid patterns also emerge when excitation is localized and inhibition is non-localized (Figure 2—figure supplement 2).

In summary, the interaction of excitatory and inhibitory plasticity leads to grid-like firing patterns in the output neuron for all three input scenarios. The grids are typically less distorted for sparser input (Figure 2g).

### Rapid appearance of grid cells and their reaction to modifications of the environment

In unfamiliar environments, neurons in the mEC exhibit grid-like firing patterns within minutes (Hafting et al., 2005). Moreover, grid cells react quickly to changes in the environment (Fyhn et al., 2007; Savelli et al., 2008; Barry et al., 2012). These observations challenge models for grid cells that require gradual synaptic changes during spatial exploration. In principle, the time scale of plasticity-based models can be augmented arbitrarily by increasing the synaptic learning rates. For stable patterns to emerge, however, significant weight changes must occur only after the animal has visited most of the environment. To explore the edge of this trade-off between speed and stability, we increased the learning rates to a point where the grids are still stable but where further increase would reduce the stability (Figure 3—figure supplement 1). For place cell-like input, periodic patterns can be discerned within 10 min of spatial exploration, starting with random initial weights (Figure 3a,b). The pattern further emphasizes over time and remains stable for many hours (Figure 3c and Figure 3—figure supplement 2).

![Figure 3.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig3-v2.jpg)

**Figure 3.:** (a,b) Rat trajectories with color-coded firing rate of a cell that receives place cell-like input. The color depicts the firing rate at the time of the location visit, not after learning. Bright colors indicate higher firing rates. The time interval of the trajectory is shown above each plot. Initially all synaptic weights are set to random values. Parts (a) and (b) show two different realizations with a good (red star) and a bad (orange triangle) grid score development. After a few minutes a periodic structure becomes visible and enhances over time. (c) Time course of the grid score in the simulations shown in (a) (red) and (b) (orange). While the periodic patterns emerge within minutes, the manifestation of the final hexagonal pattern typically takes a couple of hours. Once the pattern is established it remains stable for many hours. The gray scale shows the cumulative histogram of the grid scores of 500 realizations (black = 0, white = 1). The solid white and black lines indicate the 20% and 80% percentiles, respectively. (d) Histogram of grid scores of the 500 simulations shown in (c). Initial histogram in light blue, histogram after 1 hr and after 3 hr in dark blue. Numbers show the fraction of cells with positive grid score at the given time. Rat trajectories taken from Sargolini et al., 2006b).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** We showed that stable grid patterns emerge within minutes of behavioral rat trajectories (Figure 3) for high learning rates. Our model requires thorough spatial exploration of the rat, before significant weight changes occur. Accordingly, no stable patterns should emerge if the learning rate of the rat is too high. Left column: Same data as shown in Figure 3c with three different individual traces (top). Grid score histogram of 500 realizations before (light blue) and after 10 hr of spatial exploration (dark blue). Right column: The same simulations as shown on the left, but with twice the learning rates for excitatory and inhibitory synapses. The high learning rate leads to flickering unstable grids, as expressed in the large fluctuations in the grid score. The histogram after 10 hr of spatial exploration shows that fewer cells develop a hexagonal pattern if the learning rates are very high.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (a) A grid is learned from random initial weights and place cell-like input. After 1 hr the grid pattern is apparent. After 5 hr we remap a fraction (number above arrows) of the input, that is, the field locations of a fraction of place fields are changed to new random locations. A remapping fraction of 0 indicates that the input is unchanged and 1 indicates that all input neurons have a new place field location. The synaptic weights are not changed in this ‘input remapping’. After the remapping, the rat explores and continues learning. For all four remapping scenarios, a periodic pattern is visible shortly after the remapping. For remapping fractions less than 1, it occurs faster than during the initial learning from random weights. (b) Time courses of the grid scores for four different input remapping fractions as in (a) (Remap. frac.; shown above). The gray scale shows the cumulative histogram of the grid scores of 500 realizations (black = 0, white = 1). The solid white and black lines indicate the 20% and 80% percentiles, respectively. Colored lines show three individual traces. The red traces correspond to the simulations shown in (a). Varying a substantial fraction of the input often does not destroy the hexagonality of the grid patterns: Note the small dip in the 80% percentile for a remapping fraction of 0.5. (c) Time course of the Pearson correlation of a developing rate map with the rate map of the same simulation at 5 hr (right before the input was modified) for the same simulations as in (b), using the same color scheme and labeling. The stronger the input remapping, the lower the correlation of the grid after remapping with the grid before remapping. Note that the grid spacing is comparable for all grids, because the spatial autocorrelation length of the input is not modified during the remapping. Thus, for complete input remapping (fraction = 1) the new grid could be realigned with the old grid by a rotation and a phase shift.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (a) Sparse non-localized input (sum of 100 randomly located place fields) as in Figure 2b. (b) Dense non-localized input (random function with fixed spatial smoothness) as in Figure 2c. While the emergence of the final patterns takes roughly an hour – and thus longer than for place cell-like inputs (Figure 3) – the early firing fields are still present in the final grid, as observed in experiments (Hafting et al., 2005).

To investigate the robustness of this phenomenon, we ran 500 realizations with different trajectories, initial synaptic weights and locations of input place fields. In all simulations, a periodic pattern emerged within the first 30 min, and a majority of patterns exhibited hexagonal symmetry after 3 hr (increasing from 33% to 81%, Figure 3c,d). For non-localized input, the emergence of the final grids typically takes longer, but the first grid fields are also observed within minutes and are still present in the final grid, as observed in experiments (Hafting et al., 2005); (Figure 3—figure supplement 3).

Above, we modeled the exploration of a previously unknown room by assuming the initial synaptic weights to be randomly distributed. If the rat had previous exposure to the room or to a similar room, a structure might already have formed in some of the synaptic weights. This structure could aid the development of the grid in similar rooms or hinder it in a novel room. To study this, we simulate a network that first learns the synaptic weights in one room. We then introduce a graded modification of the room by remapping the firing fields of a fraction of input neurons to random locations. We find that the output firing pattern is robust to such perturbations, even if more than half of the inputs are remapped (Figure 3—figure supplement 2). If all inputs are changed, corresponding to a novel room, a grid pattern is learned anew. The strong initial pattern in the weights does not hinder this development (Figure 3—figure supplement 2).

Recently, Wernle et al., 2018 discovered that in an arena separated by a wall, single grid cells form two independent grid patterns — one on each side of the wall — that coalesce once the wall is removed. They find that grid fields close to the partition wall move to establish a more coherent pattern. In contrast, fields far away from the partition wall do not change their locations. Rosay et al. reproduced this experimental finding by simulating grid fields as interacting particles (Rosay et al., in preparation). They also demonstrated how it could be reproduced by a feedforward model for grid cells based on firing rate adaptation (Rosay et al., in preparation; Kropff and Treves, 2008). Inspired by these experiments and simulations, we simulate a rat that first explores one half of a quadratic arena and then the other half, for 2.5 hr each (Figure 4a). A grid pattern emerges in each compartment (Figure 4b,c). We then remove the partition wall and the rat explores the entire arena for another 5 hr (Figure 4a). As observed experimentally, grid fields close to the former partition line rearrange to make the two grids more coherent and grid fields far away from the partition line basically stay where they were (Figure 4d).

![Figure 4.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig4-v2.jpg)

**Figure 4.:** (a) Illustration of the experiment. A quadratic arena (gray box) is divided into two rectangular compartments by a wall (black line). The animal explores one compartment (A) and then the other compartment (B) for 2.5 hr each. Then the wall is removed and the rat explores the entire arena (AB) for 5 hr. (b) Firing rate maps. From left to right: After learning in A; after learning in B; the maps from A and B shown side by side (A|B); after learning in AB. (c) Autocorrelograms of the rate maps shown in (b). The number inside the correlogram shows the grid score. (d) Box plot of the correlations of the firing rate map A|B with the firing rate map AB as a function of distance from the partition wall. Close to the partition wall the correlation is low, far away from the partition wall it is high. This indicates that grid fields rearrange only locally. Each box extends from the first to the third quartile, with a dark blue line at the median. The lower whisker reaches from the lowest data point still within 1.5 IQR of the lower quartile, and the upper whisker reaches to the highest data point still within 1.5 IQR of the upper quartile, where IQR is the inter quartile range between the third and first quartile. Dots show flier points. Data: 100 realizations of experiments as in (a,b,c). For simulation details see Appendix 1. Mouse clip art from lemmling, https://openclipart.org/detail/17622/simple-cartoon-mouse-1; 2006.

In summary, periodic patterns emerge rapidly in our model and the associated time scale is limited primarily by how quickly the animal visits its surroundings, that is, by the same time scale that limits the experimental recognition of the grids.

### Place cells, band cells and stretched grids

In addition to grids, the mEC and adjacent brain areas exhibit a plethora of other spatial activity patterns including spatially invariant (Burgess et al., 2005), band-like (periodic along one direction and invariant along the other) (Krupic et al., 2012), and spatially periodic but non-hexagonal patterns (Krupic et al., 2012; Hardcastle et al., 2017; Diehl et al., 2017). Note that it is currently debated whether or not some of the observed spatially periodic but non-hexagonal firing patterns are artifacts of poorly isolated single cell data in multi-electrode recordings (Navratilova et al., 2016; Krupic et al., 2015b). In contrast to spatially periodic tuning, place cells in the hippocampus proper are typically only tuned to a single or few locations in a given environment (O'Keefe and Dostrovsky, 1971; Moser et al., 2008; Leutgeb et al., 2005). If the animal traversed the environment along a straight line, all of these cells would be classified as periodic, localized or invariant (Figure 1), although the classification could vary depending on the direction of the line. Based on this observation, we hypothesized that all of these patterns could be the result of an input autocorrelation structure that differs along different spatial directions.

We first verified that also in a two-dimensional arena, place cells emerge from a very smooth inhibitory input tuning (Figure 5a,b). The emergence of place cells is independent of the exact shape of the excitatory input. Non-localized inputs (Figure 5a) lead to similar results as those from grid cell-like inputs of different orientation and grid spacing (Figure 5b, Methods and materials); for other models for the emergence of place cells from grid cells see (Solstad et al., 2006; Franzius et al., 2007b; Rolls et al., 2006; Molter and Yamaguchi, 2008; Ujfalussy et al., 2009; Savelli and Knierim, 2010). Next we verified that also in two dimensions, spatial invariance results when excitation is broader than inhibition (Figure 5c). We then varied the smoothness of the inhibitory inputs independently along two spatial directions. If the spatial tuning of inhibitory inputs is smoother than the tuning of the excitatory inputs along one dimension but less smooth along the other, the output neuron develops band cell-like firing patterns (Figure 5d). If inhibitory input is smoother than excitatory input, but not isotropic, the output cell develops stretched grids with different spacing along two axes (Figure 5e). For these anisotropic cases, stretched hexagonal grids and rectangular arrangements of firing fields appear similarly favorable (compare Figure 5e, second row and column). A hexagonal arrangement is favored by a dense packing of inhibitory coronas, whereas a rectangular arrangement would maximize the proximity of the excitatory centers, given the inhibitory corona (Figure 5—figure supplement 1).

![Figure 5.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig5-v2.jpg)

**Figure 5.:** (a,b,c,d) Arrangement as in Figure 2. (a,b) Place cells emerge if the inhibitory autocorrelation length exceeds the box length or if the inhibitory neurons are spatially untuned. The type of tuning of the excitatory input is not crucial: Place cells develop for non-localized input (a) as well as for grid cell input (b). (c) The output neuron develops an invariance if the spatial tuning of inhibitory input neurons is less smooth than the tuning of excitatory input neurons. (d) Band cells emerge if the spatial tuning of inhibitory input is asymmetric, such that its autocorrelation length is larger than that of excitatory input along one direction (here the $y$-direction) and smaller along the other (here the $x$-direction). (e) Overview of how the shape of the inhibitory input tuning determines the firing pattern of the output neuron. Each element depicts the firing rate map of the output neuron after 10 hr. White ellipses of width $2\sigma_{I},_{x}$ and $2\sigma_{I},_{y}$ in $x-$ and $y-$direction indicate the direction-dependent standard deviation of the spatial tuning of the inhibitory input neurons. For simplicity, the width of the excitatory tuning fields, $\sigma_{E}$, is the same in all simulations. It determines the size of the circular firing fields. The red circle at the axis origin is of diameter $2⁢\sigma_{E}$.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a) For ellipsoidal spatial autocorrelation structures of inhibitory input (blue line), we observed band cell-like firing patterns or stretched grids (Figure 5e). Interestingly, the resulting patterns alternate between two different symmetries. This can be understood by two competing arrangements of ellipsoids. (b) A dense packing of ellipsoids maximizes the area with non-zero firing and is favored by the inhibitory learning rule. This leads to stretched grids. (c) Maximizing the overlap between excitatory input fields is favored by the excitatory learning rule and leads to quadratic grids with different periodicities along different directions. (d) Some simulations show a combination of both patterns; compare Figure 5e. The observed alignment of excitatory firing fields in (c) is particularly favored, if inhibition is very smooth along one direction. This could lead to alignment of the head direction of individual grid fields in the simulations shown in Figure 6.

In summary, the relative spatial smoothness of inhibitory and excitatory input determines the symmetry of the spatial firing pattern of the output neuron. The requirements for the input tuning that support invariance, periodicity and localization apply individually to each spatial dimension, opening up a combinatorial variety of spatial tuning patterns.

### Spatially tuned input combined with head direction selectivity leads to grid, conjunctive and head direction cells

Many cells in and around the hippocampus are tuned to the head direction of the animal (Taube et al., 1990; Taube, 1995; Chen et al., 1994). These head direction cells are typically tuned to a single head direction, just like place cells are typically tuned to a single location. Moreover, head direction cells are often invariant to location (Burgess et al., 2005), just like place cells are commonly invariant to head direction (Muller et al., 1994). There are also cell types with conjoined spatial and head direction tuning. Conjunctive cells in the mEC fire like grid cells in space, but only in a particular head direction (Sargolini et al., 2006a), and many place cells in the hippocampus of crawling bats also exhibit head direction tuning (Rubin et al., 2014). To investigate whether these tuning properties could also result in our model, we simulated a rat that moves in a square box, whose head direction is constrained by the direction of motion (Appendix 1). Each input neuron is tuned to both space and head direction (see Figure 6 for localized and Figure 6—figure supplement 1 for non-localized input).

![Figure 6.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig6-v2.jpg)

**Figure 6.:** (a,b,c) Columns from left to right: Spatial tuning and head direction tuning (polar plot) of excitatory and inhibitory input neurons (one example each); spatial firing rate map of the output neuron before learning and after spatial exploration of 10 hr with corresponding autocorrelogram; head direction tuning of the output neuron after learning. The numbers in the polar plots indicate the peak firing rate at the preferred head direction after averaging over space. (a) Wider spatial tuning of inhibitory input neurons than of excitatory input neurons combined with narrower head direction tuning of inhibitory input neurons leads to a grid cell-like firing pattern in space with invariance to head direction, that is, the output neuron fires like a pure grid cell. (b) The same spatial input characteristics combined with head direction-invariant inhibitory input neurons leads to grid cell-like activity in space and a preferred head direction, that is, the output neuron fires like a conjunctive cell. (c) If the spatial tuning of inhibitory input neurons is less smooth than that of excitatory neurons and the concurrent head direction tuning is wider for inhibitory than for excitatory neurons, the output neuron is not tuned to space but to a single head direction, that is, the output neuron fires like a pure head direction cell. (d) Head direction tuning and grid score of 10 simulations of the three cell types. Each symbol represents one realization with random input tuning. The markers correspond to the tuning properties of the input neurons as depicted in (a,b,c): grid cell (triangles), conjunctive cell (squares), head direction cell (circles). The values that correspond to the output cells in (a,b,c) are shown as filled symbols. (e) In our model, the head direction tuning of individual grid fields is sharper than the overall head direction tuning of the conjunctive cell. Depicted is a rate map of a conjunctive cell (left) and the corresponding head direction tuning (right, dashed). For three individual grid fields, indicated with colored squares, the head direction tuning is shown in the same polar plot. The overall tuning of the grid cell (dashed) is a superposition of the tuning of all grid fields. Numbers indicate the peak firing rate (in Hz) averaged individually within each of the four rectangles in the rate map.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Arrangement as in Figure 6.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (a) Spike locations of a grid cell color-coded with the head direction of the rat at the moment the respective spike was fired. Circular mean and circular standard deviation of head directions at spike firing (‘spike head directions’ in the following) shown above. (b) Polar histogram of spike head directions (filled fan) and trajectory head directions (black fan) for all spikes of the grid cell. $N$: Number of spikes. $v$: Sum of $N$ unit vectors whose orientation is given by the spike head directions, normalized by $N$. The larger this number, the more precise the head direction tuning. $U^{2}$: Watson’s $U^{2}$ value (Appendix 1). The larger this number, the more the distribution of spike head directions deviates from the distribution of trajectory head directions. (c) Same arrangement as in (b) but for individual grid fields. Each plot corresponds to a different grid field. The colors of the filled fans correspond to the colors of the circles around grid fields in (a). Only spikes within these circles are considered. Individual grid fields often exhibit a sharper head direction tuning than the entire cell; compare the larger $v$ values. However, the trajectory often exhibits a strong head direction bias; compare the directionality of black fans. The head direction tuning of a grid field tends to align with this bias; compare the smaller $U^{2}$ values. Quantitative statements about the head direction tuning of individual grid fields would be easier for cells with more firing fields, because the head direction bias of rodents is less pronounced in central parts of the arena (Rubin et al., 2014); compare the grid field in the light green circle. From the publicly available data, we did not come to a conclusive answer on the tuning of individual grid fields. Data obtained from (Sargolini et al., 2006a; Sargolini et al., 2006b).

In line with the previous observations, we find that the spatial tuning of the output neuron is determined by the relative spatial smoothness of the excitatory and inhibitory inputs, and the head direction tuning of the output neuron is determined by the relative smoothness of the head direction tuning of the inputs from the two populations. If the head direction tuning of excitatory input neurons is smoother than that of inhibitory input neurons, the output neuron becomes invariant to head direction (Figure 6a). If instead only the excitatory input is tuned to head direction, the output neuron develops a single activity bump at a particular head direction (Figure 6b,c). The concurrent spatial tuning of the inhibitory input neurons determines the spatial tuning of the output neuron. For spatially smooth inhibitory input, the output neuron develops a hexagonal firing pattern (Figure 6a,b), and for less smooth inhibitory input the firing of the output neuron is invariant to the location of the animal (Figure 6c).

In summary, the relative smoothness of inhibitory and excitatory input neurons in space and in head direction determines whether the output cell fires like a pure grid cell, a conjunctive cell or a pure head direction cell (Figure 6d).

We find that the overall head direction tuning of conjunctive cells is broader than that of individual grid fields (Figure 6e). This results from variations in the preferred head direction of different grid fields. Typically, however, these variations remain small enough to preserve an overall head direction tuning of the cell, because individual grid fields tend to align their head direction tuning (compare with Figure 5—figure supplement 1, but in three dimensions). Whether or not a narrower head direction of individual grid fields or a different preferred direction for different grid fields is present also in rodents is not resolved (Figure 6—figure supplement 2).

## Discussion

We presented a self-organization model that reproduces the experimentally observed spatial and head direction tuning patterns in the hippocampus and adjacent brain regions. Its core mechanism is an interaction of Hebbian plasticity in excitatory synapses and homeostatic Hebbian plasticity in inhibitory synapses (Vogels et al., 2011; D'Amour and Froemke, 2015). The main prediction of the model is that the spatial autocorrelation structure of excitatory and inhibitory inputs determines – and should thus be predictable from – the output pattern of the cell. Investigations of the tuning of individual cells (Wertz et al., 2015) or even synapses (Wilson et al., 2016) that project to spatially tuned cells would thus be a litmus test for the proposed mechanism.

### Origin of spatially tuned synaptic input

The origin of synaptic input to spatially tuned cells is not fully resolved (van Strien et al., 2009). Given that our model is robust to the precise properties of the input, it is consistent with input from higher sensory areas (Tanaka, 1996; Quiroga et al., 2005) that could inherit spatial tuning from their sensory tuning in a stable environment (Arleo and Gerstner, 2000; Franzius et al., 2007a). This is in line with the observation that grid cells lose their firing profiles in darkness (Chen et al., 2016; Pérez-Escobar et al., 2016) and that the hexagonal pattern rotates when a visual cue card is rotated (Pérez-Escobar et al., 2016).

The input could also stem from within the hippocampal formation, where spatial tuning has been observed in both excitatory (O'Keefe, 1976) and inhibitory (Marshall et al., 2002; Wilent and Nitz, 2007; Hangya et al., 2010) neurons. For example, the notion that mEC neurons receive input from hippocampal place cells is supported by several studies: Place cells in the hippocampus emerge earlier during development than grid cells in the mEC (Langston et al., 2010; Wills et al., 2010), grid cells lose their tuning pattern when the hippocampus is deactivated (Bonnevie et al., 2013) and both the firing fields of place cells and the spacing and field size of grid cells increase along the dorso-ventral axis (Jung et al., 1994; Brun et al., 2008b; Stensola et al., 2012). Moreover, entorhinal stellate cells, which often exhibit grid-like firing patterns, receive a large fraction of their input from the hippocampal CA2 region (Rowland et al., 2013), where many cells are tuned to the location of the animal (Martig and Mizumori, 2011).

Inhibition is usually thought to arise from local interneurons – but see (Melzer et al., 2012) – suggesting that spatially tuned inhibitory input to mEC neurons originates from the entorhinal cortex itself. Interneurons in mEC display spatial tuning (Buetfering et al., 2014; Savelli et al., 2008; Frank et al., 2001) that could be inherited from hippocampal place cells, other grid cells (Couey et al., 2013; Pastoll et al., 2013; Winterer et al., 2017) or from entorhinal cells with nongrid spatial tuning (Diehl et al., 2017; Hardcastle et al., 2017). The broader spatial tuning required for the emergence of spatial selectivity could be established, for example by pooling over cells with similar tuning or through a non-linear input-output transformation in the inhibitory circuitry. If inhibitory input is indeed local, the increase in grid spacing along the dorso-ventral axis (Brun et al., 2008b) suggests that the tuning of inhibitory interneurons gets smoother along this axis. For smoother tuning functions, fewer neurons are needed to cover the whole environment, in accordance with the decrease in interneuron density along the dorso-ventral axis (Beed et al., 2013).

The excitatory input to hippocampal place cells could originate from grid cells in entorhinal cortex (Figure 5b), which is supported by anatomical (van Strien et al., 2009) and lesion studies (Brun et al., 2008a). The required untuned inhibition could arrive from interneurons in the hippocampus proper that often show very weak spatial tuning (Marshall et al., 2002). In addition to grid cell input, place cells are also thought to receive inputs from other cell types, such as border cells (Muessig et al., 2015) and other brain regions such as the medial septum (Wang et al., 2015) .

### Dissociation from continuous attractor network models

The observed spatial tuning patterns have also been explained by other models. In continuous attractor networks (CAN), each cell type could emerge from a specific recurrent connectivity pattern, combined with a mechanism that translates the motion of the animal into shifts of neural activity on an attractor. How the required connectivity patterns – which lie at the core of any CAN model – could emerge is subject to debate (Widloski and Fiete, 2014). Our model is qualitatively different in that it does not rely on attractor dynamics in a recurrent neural network, but on experience-dependent plasticity of spatially modulated afferents to an individual output neuron (Mehta et al., 2000). A measurable distinction of our model from CAN models is its response to a rapid global reduction of inhibition. While a modification of inhibition typically changes the grid spacing in CAN models of grid cells (Couey et al., 2013; Widloski and Fiete, 2015), the grid field locations generally remain untouched in our model. The grid fields merely change in size, until inhibition is recovered by inhibitory plasticity (Figure 7a). This can be understood by the colocalization of the grid fields and the peaks in the excitatory membrane current (Figure 7b,c). A reduction of inhibition leads to an increased protrusion of these excitatory peaks and thus to wider firing fields. Grid patterns in mEC are temporally stable in spite of dopaminergic modulations of GABAergic transmission (Cilz et al., 2014) and the spacing of mEC grid cells remains constant during the silencing of inhibitory interneurons (Miao et al., 2017). Both observations are in line with our model. Moreover, we found that for localized input tuning, the inhibitory membrane current typically also peaks at the locations of the grid fields. This co-tuning breaks down for non-localized input (Figure 7b). In contrast, CAN models predict that the inhibitory membrane current has the same periodicity as the grid (Schmidt-Hieber and Häusser, 2013), but possibly phase shifted.

![Figure 7.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig7-v2.jpg)

**Figure 7.:** (a) Reducing the strength of inhibitory synapses to a fraction of its initial value (from left to right: 1, 1/2, 1/4) leads to larger grid fields but unchanged grid spacing in our model. In continuous attractor network models, the same reduction of inhibition would affect not only the field size but also the grid spacing. (b) Excitatory (red) and inhibitory (blue) membrane current to a cell with grid-like firing pattern (gray) on a linear track. The currents are normalized to a maximum value of 1. Different rows correspond to different spatial tuning characteristics of the input neurons. From top to bottom: Place cell-like tuning, sparse non-localized tuning (sum of 100 randomly located place fields), dense non-localized tuning (Gaussian random fields). Peaks in excitatory membrane current are co-localized with grid fields (shaded area) for all input statistics. In contrast, the inhibitory membrane current is not necessarily correlated with the grid fields for non-localized input. Moreover, the dynamic range of the membrane currents is reduced for non-localized input. A reduction of inhibition as shown in (a) corresponds to a lowering of the inhibitory membrane current. (c) Excitatory and inhibitory membrane current to a grid cell receiving sparse non-localized input (sum of 100 randomly located place fields) in two dimensions. Top: Tuning of output firing rate, normalized excitatory and inhibitory membrane current. Bottom: Autocorrelograms thereof. The grid pattern is more apparent in the spatial tuning of the excitatory membrane current than in the inhibitory membrane current.

The grid patterns of topologically nearby grid cells in the mEC typically have the same orientation and spacing but different phases (Hafting et al., 2005). Moreover, the coupling between anatomically nearby grid cells – for example their difference in spatial phase – is more stable to changes of the environment than the firing pattern of individual grid cells (Yoon et al., 2013). These properties are immanent to CAN models. In contrast, single cell models (Burgess et al., 2007; Kropff and Treves, 2008; Castro and Aguiar, 2014; Stepanyuk, 2015; Dordek et al., 2016; D'Albis and Kempter, 2017; Monsalve-Mercado and Leibold, 2017) require additional mechanisms to develop a coordination of neighboring grid cells. The challenge for any mechanism is to correlate the grid orientations, but leave the grid phases uncorrelated. The most obvious candidate, recurrent connections among different grid cells (Si et al., 2012), requires an intricate combination of mechanisms to perform this balancing act. We assume that an appropriate recurrent connectivity would not be simpler in our model.

CAN models predict that all grid fields in a conjunctive (grid x head direction) cell have the same head direction tuning, whereas our model predicts that there could be differences between different grid fields (Figure 6e). Our preliminary analysis suggests that an in-depth evaluation would require data for central grid fields without trajectory biases (Figure 6—figure supplement 2), which are at present not publicly available.

In addition, CAN models require that conjunctive (grid x head direction) cells are positively modulated by running speed. Such modulation has been observed in experiments (Kropff et al., 2015). In our model, we could introduce a running speed dependence, for example as a global modulation of the input signals. We expect that in this case, the output neuron would inherit speed tuning from the input but would otherwise develop similar spatial tuning patterns.

A recent analysis has shown that periodic firing of entorhinal cells in rats that move on a linear track can be assessed as slices through a hexagonal grid (Yoon et al., 2016), which arises naturally in a two-dimensional CAN model. In our model, we would obtain slices through a hexagonal grid if the rat learns the output pattern in two dimensions and afterwards is constrained to move on a linear track that is part of the same arena. If the rat learns the firing pattern on the linear track from scratch, the firing fields would be periodic.

### Rapid appearance and rearrangement of grids

Models that learn grid cells from spatially tuned input do not have to assume a preexisting connectivity pattern or specific mechanisms for path integration (Burgess et al., 2007), but are challenged by the fast emergence of hexagonal firing patterns in unfamiliar environments (Hafting et al., 2005). Most plasticity-based models require slow learning, such that the animal explores the whole arena before significant synaptic changes occur. Therefore, grid patterns typically emerge slower than experimentally observed (Dordek et al., 2016). This delay is particularly pronounced in models that require an extensive exploration of both space and movement direction (Kropff and Treves, 2008; Franzius et al., 2007a; D'Albis and Kempter, 2017). In contrast to these models, which give center stage to the temporal statistics of the animal’s movement, our approach relies purely on the spatial statistics of the input and is hence insensitive to running speed.

For the mechanism we suggested, the self-organization was very robust and allowed rapid pattern formation on short time scales, similar to those observed in rodents (Figure 3). This speed could be further increased by accelerated reactivation of previous experiences during periods of rest (Lee and Wilson, 2002). By this means, the exploration time and the time it takes to activate all input patterns could be decoupled, leading to a much faster emergence of grid cells in all trajectory-independent models with associative learning. Other models that explain the emergence of grid patterns from place cell input through synaptic depression and potentiation also develop grid cells in realistic times (Castro and Aguiar, 2014; Stepanyuk, 2015; Monsalve-Mercado and Leibold, 2017). These models differ from ours in that they do not require inhibition, but instead specific forms of rate-dependent synaptic depression and potentiation that change the synaptic weights such that place cell-like input leads to grid cell-like output. How these models generalize to potentially non-localized input is yet to be shown.

Learning the required connectivity in CAN models can take a long time (Widloski and Fiete, 2014). However, as soon as the required connectivity and translation mechanism is established, a grid pattern would be observed immediately, even in a novel room. For different rooms this pattern could have different phases and orientations, but similar grid spacing (Fyhn et al., 2007). Similarly, we found that room switches in our model lead to grid patterns of the same grid spacing but different phases and orientations. The pattern emerges rapidly, but is not instantaneously present (Figure 3—figure supplement 2). It would be interesting to study whether rotation of a fraction of the input would lead to a bimodal distribution of grid rotations: No rotation and co-rotation with the rotated input, as recently observed in experiments where distal cues were rotated but proximal cues stayed fixed (Savelli et al., 2017).

Recently, it was discovered that in an arena separated by a wall, single grid cells form two independent grid patterns – one on each side – that coalesce once the wall is removed (Wernle et al., 2018; Rosay et al., in preparation). This coalescence is local, that is, grid fields close to the partition wall readjust, whereas grid fields far away do not change their locations. Feedforward models like ours can explain such a local rearrangement (Figure 4; Rosay et al., in preparation).

### Boundary effects

Experiments show that the pattern and the orientation of grid cells is influenced by the geometry of the environment. In a quadratic arena, the orientation of grid cells tends to align – with a small offset – to one of the box axes (Stensola et al., 2015). In trapezoidal arenas, the hexagonality of grids is distorted (Krupic et al., 2015a). We considered quadratic and circular arenas with rat trajectories from behavioral experiments and found that the boundaries also distort the grid pattern in our simulations, particularly for localized inputs (Figure 2—figure supplement 3). In trapezoidal geometries, we expect this to lead to non-hexagonal grids. However, we did not observe a pronounced alignment to quadratic boundaries if the input place fields were randomly located (Figure 2—figure supplement 3).

### Conclusion

We found that interacting excitatory and inhibitory plasticity serves as a simple and robust mechanism for rapid self-organization of stable and symmetric patterns from spatially modulated feedforward input. The suggested mechanism ports the robust pattern formation of attractor models from the neural to the spatial domain and increases the speed of self-organization of plasticity-based mechanisms to time scales on which the spatial tuning of neurons is typically measured. It will be interesting to explore how recurrent connections between output cells can help to understand the role of local inhibitory (Couey et al., 2013; Pastoll et al., 2013) and excitatory connections (Winterer et al., 2017) and the presence or absence of topographic arrangements of spatially tuned cells (O'Keefe et al., 1998; Stensola et al., 2012; Giocomo et al., 2014). We illustrated the properties and requirements of the model in the realm of spatial representations. As invariance and selectivity are ubiquitous properties of receptive fields in the brain, the interaction of excitatory and inhibitory synaptic plasticity could also be essential to form stable representations from sensory input in other brain areas (Constantinescu et al., 2016; Clopath et al., 2016).

## Materials and methods

### Code availability

The code for reproducing the essential findings of this article is available at https://github.com/sim-web/spatial_patterns (Weber, 2018) under the GNU General Public License v3.0. A copy is archived at https://github.com/elifesciences-publications/spatial_patterns.

### Network architecture and neuron model

We study a feedforward network where a single output neuron receives synaptic input from $N_{E}$ excitatory and $N_{I}$ inhibitory neurons (Figure 1a) with synaptic weight vectors $w^{E} \in R^{N_{E}}$, $w^{I} \in R^{N_{I}}$ and spatially tuned input rates $r^{E}(x)\inR^{N_{E}}$, $r^{I}(x)\inR^{N_{I}}$, respectively. Here $x\inR^{dimensions}$ denotes the location and later also the head direction of the animal. For simplicity and to allow a mathematical analysis we use a rate-based description for all neurons. The firing rate of the output neuron is given by the rectified sum of weighted excitatory and inhibitory inputs:

$$
r^{out}(x(t))=[\sumi=1N_{E}w_{i}^{E}(t)r_{i}^{E}(x(t))−\sumj=1N_{I}w_{j}^{I}(t)r_{j}^{I}(x(t))]_{+},
$$

where $[⋅]$+ denotes a rectification that sets negative firing rates to zero. To comply with the notion of excitation and inhibition, all weights are constrained to be positive. In most simulations we use $N_{E}=4N_{I}$. Simulation parameters are shown in Tables 1–3 for the main figures and in Tables 4–6 for the supplementary figures.

**Table 1.**
 Parameters for excitatory inputs for all figures in the manuscript.$N_{E}^{f}=∞$ indicates that the excitatory input is a Gaussian random field.


<table>
  <thead>
    <tr>
      <th></th>
      <th>[σE,x,σE,y,σE,z]</th>
      <th>NE</th>
      <th>ηE</th>
      <th>wE,init</th>
      <th>NEf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1b</td>
      <td>0.05</td>
      <td>2000</td>
      <td>2 × 10−6</td>
      <td>1</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 1c</td>
      <td>0.08</td>
      <td>2000</td>
      <td>2 × 10−6</td>
      <td>1</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 1d</td>
      <td>0.06</td>
      <td>2000</td>
      <td>2 × 10−6</td>
      <td>1</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 1f</td>
      <td>0.04</td>
      <td>160</td>
      <td>2 × 10−6</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 1g</td>
      <td>0.03</td>
      <td>1600</td>
      <td>3.6 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 1h</td>
      <td>0.03</td>
      <td>10000</td>
      <td>3.5 × 10−7</td>
      <td>1</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 2a</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>6.7 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2b</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>2 × 10−6</td>
      <td>1</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Figure 2c</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>6 × 10−6</td>
      <td>1</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 3a–d</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>2 × 10−4</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 4</td>
      <td>[0.05, 0.05]</td>
      <td>2 × 4900</td>
      <td>1.3 × 10−4</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 5a</td>
      <td>[0.07, 0.07]</td>
      <td>4900</td>
      <td>6 × 10−6</td>
      <td>0.5</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 5b</td>
      <td>[0.07, 0.07]</td>
      <td>400</td>
      <td>1.3 × 10−4</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 5c</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>1.1 × 10−6</td>
      <td>0.0455</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 5d</td>
      <td>[0.08, 0.08]</td>
      <td>4900</td>
      <td>6 × 10−6</td>
      <td>0.5</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 5e</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>6.7 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6a</td>
      <td>[0.07, 0.07, 0.2]</td>
      <td>37500</td>
      <td>1.5 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6b</td>
      <td>[0.08, 0.08, 0.2]</td>
      <td>50000</td>
      <td>10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6c</td>
      <td>[0.1, 0.1, 0.2]</td>
      <td>50000</td>
      <td>10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 7a</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>6.7 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 7b</td>
      <td>0.04</td>
      <td>2000</td>
      <td>5 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>0.04</td>
      <td>2000</td>
      <td>5 × 10−7</td>
      <td>1.0</td>
      <td>100</td>
    </tr>
    <tr>
      <td rowspan="2">Figure 7c</td>
      <td>0.05</td>
      <td>2000</td>
      <td>5 × 10−6</td>
      <td>0.5</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>2 × 10−6</td>
      <td>1</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Figure 8b</td>
      <td>0.03</td>
      <td>800</td>
      <td>3.3 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Parameters for inhibitory inputs for all figures in the manuscript.indicates that the inhibitory input is a Gaussian random field. We denote spatially untuned inhibition with: σI = ∞.


<table>
  <thead>
    <tr>
      <th></th>
      <th>[σI,x,σI,y,σI,z]</th>
      <th>NI</th>
      <th>ηI</th>
      <th>wI,init</th>
      <th>NIf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1b</td>
      <td>0.12</td>
      <td>500</td>
      <td>2 × 10−5</td>
      <td>4:4</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 1c</td>
      <td>0.07</td>
      <td>2000</td>
      <td>2 × 10−5</td>
      <td>1.1</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 1d</td>
      <td>∞</td>
      <td>500</td>
      <td>2 × 10−5</td>
      <td>4.39</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 1f</td>
      <td>0.13</td>
      <td>40</td>
      <td>2 × 10−5</td>
      <td>1.31</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 1g</td>
      <td>From 0.08 to 0.3 in 0.02 steps</td>
      <td>400</td>
      <td>3.6 × 10−4</td>
      <td>Equation 111</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 1h</td>
      <td>From 0.08 to 0.3 in 0.02 steps</td>
      <td>2500</td>
      <td>7 × 10−6</td>
      <td>4.03</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 2a</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2b</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>8 × 10−6</td>
      <td>1.52</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Figure 2c</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>6 × 10−5</td>
      <td>4.0</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 3a–d</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>8 × 10−4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 4</td>
      <td>[0.1, 0.1]</td>
      <td>2 × 1225</td>
      <td>5.3 × 10−4</td>
      <td>1.51</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 5a</td>
      <td>[∞, ∞]</td>
      <td>1225</td>
      <td>6 × 10−5</td>
      <td>2</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 5b</td>
      <td>[∞, ∞]</td>
      <td>1</td>
      <td>5.3 × 10−4</td>
      <td>69.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 5c</td>
      <td>[0.049, 0.049]</td>
      <td>1225</td>
      <td>4.4 × 10−5</td>
      <td>0.175</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 5d</td>
      <td>[0.3, 0.07]</td>
      <td>1225</td>
      <td>6 × 10−5</td>
      <td>2</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>Figure 5e</td>
      <td>[0.049, 0.049]</td>
      <td>4900</td>
      <td>2.7 × 10−4</td>
      <td>1.02</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[0.2, 0.1]; [0.1, 0.2]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.04</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[2, 0.1]; [0.1, 2]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>2.74</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[2, 0.2]; [0.2, 2]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.38</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[0.2, 0.2]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>0.709</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[2, 2]</td>
      <td>1225</td>
      <td>2.7 × 10*−4</td>
      <td>0.259</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[0.1, 0.049]; [0.049, 0.1]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>2.48</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>[0.2, 0.049]; [0.049, 0.2]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.74</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">Figure 6a</td>
      <td>[2, 0.049]; [0.049, 2]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>5.56</td>
      <td>1</td>
    </tr>
    <tr>
      <td>[0.15, 0.15, 0.2]</td>
      <td>9375</td>
      <td>1.5 × 10−4</td>
      <td>1.55</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6b</td>
      <td>[0.12, 0.12, 1.5]</td>
      <td>3125</td>
      <td>10−4</td>
      <td>5.68</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6c</td>
      <td>[0.09, 0.09, 1.5]</td>
      <td>12500</td>
      <td>10−4</td>
      <td>2.71</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6d</td>
      <td>Same as</td>
      <td>Figure 6a,b,c</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 7a</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 7b</td>
      <td>0.12</td>
      <td>500</td>
      <td>5 × 10−4</td>
      <td>1.6</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>0.12</td>
      <td>500</td>
      <td>5 × 10−6</td>
      <td>1.62</td>
      <td>100</td>
    </tr>
    <tr>
      <td rowspan="2">Figure 7c</td>
      <td>0.12</td>
      <td>500</td>
      <td>5 × 10−5</td>
      <td>1.99</td>
      <td>∞</td>
    </tr>
    <tr>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>8 × 10−6</td>
      <td>1.52</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Figure 8b</td>
      <td>0.1</td>
      <td>varied</td>
      <td>varied</td>
      <td>varied</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Simulation time $t_{sim}$ and system size $L$ for all figures in the manuscript.


<table>
  <thead>
    <tr>
      <th></th>
      <th>tsim</th>
      <th>L</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1b</td>
      <td>2,000,000</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Figure 1c</td>
      <td>2,000,000</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Figure 1d</td>
      <td>400,000</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Figure 1f</td>
      <td>20,000,000</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Figure 1g</td>
      <td>80,000,000</td>
      <td>14</td>
    </tr>
    <tr>
      <td>Figure 1h</td>
      <td>40,000,000</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Figure 2a,b,c</td>
      <td>1,800,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 3a,b,c,d</td>
      <td>540,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 4</td>
      <td>1,800,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 5a,c,d,e</td>
      <td>1,800,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 5b</td>
      <td>180,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6a,b,c,d</td>
      <td>1,800,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 7a,c</td>
      <td>1,800,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 7b</td>
      <td>400,000</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Figure 8b</td>
      <td>40,000,000</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Parameters for excitatory inputs in supplement figures.$N_{E}^{f}=∞$ indicates that the excitatory input is a Gaussian random field.


<table>
  <thead>
    <tr>
      <th></th>
      <th>[σE,x,σE,y,σE,z]</th>
      <th>NE</th>
      <th>ηE</th>
      <th>wE,init</th>
      <th>NEf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1—figure supplement 1</td>
      <td>0.04</td>
      <td>2000</td>
      <td>5 × 10−7</td>
      <td>1</td>
      <td>varied</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 2</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>6.7 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 3</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>6.7 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 4</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>2 ×10−4</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 6</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 2</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>3.3 × 10−5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 1</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 3</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 2</td>
      <td>[0.05, 0.05]</td>
      <td>4900</td>
      <td>1.3 ×10−4</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6—figure supplement 1</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Parameters for inhibitory inputs in supplement figures.$N_{I}^{f}=∞$ indicates that the inhibitory input is a Gaussian random field. We denote spatially untuned inhibition with: σI = ∞.


<table>
  <thead>
    <tr>
      <th></th>
      <th>[σI,x,σI,y,σI,z]</th>
      <th>NI</th>
      <th>ηI</th>
      <th>wI,init</th>
      <th>NIf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1—figure supplement 1</td>
      <td>0.12</td>
      <td>500</td>
      <td>5 × 10−6</td>
      <td>1.61</td>
      <td>varied</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 2</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 3</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>2.7 × 10−4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 4</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>8× 10-4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 6</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 2</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>5.3 × 10−6</td>
      <td>0.03</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 1</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 3</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 2</td>
      <td>[0.1, 0.1]</td>
      <td>1225</td>
      <td>5.3×10-4</td>
      <td>1.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 6—figure supplement 1</td>
      <td>see</td>
      <td>caption</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Simulation time $t_{sim}$ and system size $L$ for supplement figures.


<table>
  <thead>
    <tr>
      <th></th>
      <th>tsim</th>
      <th>L</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1—figure supplement 1</td>
      <td>48,000,000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Figure 1—figure supplement 2</td>
      <td>see</td>
      <td>caption</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1</td>
      <td>1,800,000</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 3</td>
      <td>1,800,000</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 4</td>
      <td>180,000</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 6</td>
      <td>see</td>
      <td>caption</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 2</td>
      <td>1,800,000</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 1</td>
      <td>see</td>
      <td>caption</td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 3</td>
      <td>see</td>
      <td>caption</td>
    </tr>
    <tr>
      <td>Figure 3—figure supplement 2</td>
      <td>1,800,000</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Figure 6—figure supplement 1</td>
      <td>see</td>
      <td>caption</td>
    </tr>
  </tbody>
</table>

### Excitatory and inhibitory plasticity

In each unit time step ($Δ⁢t=1$), the excitatory weights are updated according to a Hebbian rule:

$$
Δw^{E}=η_{E}r^{E}(x)r^{out}(x)(and normalization).
$$

The excitatory learning rate $η_{E}$ is a constant that we chose individually for each simulation. To avoid unbounded weight growth, we use a quadratic multiplicative normalization, that is, we keep the sum of the squared weights of the excitatory population $\sum_{i=1}^{N_{E}}(w_{i}^{E})^{2}$ constant at its initial value, by rescaling the weights after each unit time step. However, synaptic weight normalization is not a necessary ingredient for the emergence of firing patterns (Figure 2—figure supplement 4). We model inhibitory synaptic plasticity using a previously suggested learning rule (Vogels et al., 2011):

$$
Δw^{I}=η_{I}r^{I}(x)(r^{out}(x)−ρ_{0}),
$$

with inhibitory learning rate $η_{I}$ and target rate $ρ_{0}$ = 1 Hz. Negative inhibitory weights are set to zero.

### Rat trajectory

In the linear track model (one dimension, Figures 1 and 7), we create artificial run-and-tumble trajectories $x⁢(t)$ constrained on a line of length $L$ with constant velocity $v$ = 1 cm per unit time step and persistence length $L/2$ (Appendix 1).

In the open arena model (two dimensions, Figures 2, 3, 5 and 7), we use trajectories $x(t)$ from behavioral data (Sargolini et al., 2006b) of a rat that moved in a 1 m × 1 m quadratic enclosure (Appendix 1). In the simulations with a separation wall (Figure 4), we create trajectories as a two-dimensional persistent random walk (Appendix 1). In the model for neurons with head direction tuning (three dimensions, Figure 6), we use the same behavioral trajectories as in two dimensions and model the head direction as noisily aligned to the direction of motion (Appendix 1).

### Spatially tuned inputs

The firing rates of excitatory and inhibitory synaptic inputs $r_{i}^{E},r_{j}^{I}$ are tuned to the location $𝐱$ of the animal. In the following, we use $x$ and $y$ for the first and second spatial dimension and $z$ for the head direction.

For place field-like input, we use Gaussian tuning functions with standard deviation $\sigma_{E}$, $\sigma_{I}$ for the excitatory and inhibitory population, respectively. In Figure 5 the standard deviation is chosen independently along the $x$ and $y$ direction. The centers of the Gaussians are drawn randomly from a distorted lattice (Figure 2—figure supplement 5). This way we ensure random but spatially dense tuning. The lattice contains locations outside the box to reduce boundary effects.

For sparse non-localized input with $N_{P}^{f}$ fields per neuron of population $P$, we first create $N_{P}^{f}$ distorted lattices, each with $N_{P}$ locations. We then assign $N_{P}^{f}$ of the resulting $N_{P}^{f}N_{P}$ locations at random and without replacement to each input neuron (see also Appendix 1).

For dense non-localized input, we convolve Gaussians with white noise and increase the resulting signal to noise ratio by setting the minimum to zero and the mean to 0.5 (Appendix 1). The Gaussian convolution kernels have different standard deviations for different populations. For each input neuron we use a different realization of white noise. This results in arbitrary tuning functions of the same autocorrelation length as the – potentially asymmetric – Gaussian convolution kernel. For grid cell-like input, we place Gaussians of standard deviation $\sigma_{E}$ on the nodes of perfect hexagonal grids whose spacing and orientation is variable. In Figure 5b we draw the grid spacing of each input from a normal distribution of mean $6⁢\sigma_{E}$ and standard deviation $\sigma_{E}/6$. The grid orientation was drawn from a uniform distribution between $-30$ and $30$ degrees.

For input with combined spatial and head direction tuning, we use the Gaussian tuning curves described above for the spatial tuning and von Mises distributions along the head direction dimension (Appendix 1).

For all input tunings, the standard deviation of the firing rate is of the same order of magnitude as the mean firing rate (Appendix 1).

### Initial synaptic weights and global reduction of inhibition

We specify a mean for the initial excitatory and inhibitory weights, respectively, and randomly draw each synaptic weight from the corresponding mean $\pm5%$. The excitatory mean is chosen such that the output neuron would fire above the target rate everywhere in the absence of inhibition; we typically take this mean to be 1 (Table 1 and Appendix 1). The mean inhibitory weight is then determined such that the output neuron would fire close to the target rate, if all the weights were at their mean value (Table 2 and Appendix 1). Choosing the weights this way ensures that initial firing rates are random, but neither zero everywhere, nor inappropriately high. We model a global reduction of inhibition by scaling all inhibitory weights by a constant factor, after the grid has been learned.

### Mathematical analysis of the learning rules

In the following, we derive the spacing of periodic firing patterns as a function of the simulation parameters for the linear track.

We first show that homogeneous weights, chosen such that the output neuron fires at the target rate, are a fixed point for the time evolution of excitatory and inhibitory weights under the assumption of slow learning. We then perturb this fixed point and study the time evolution of the perturbations in Fourier space. The translational invariance of the input overlap leads to decoupling of spatial frequencies and leaves a two-dimensional dynamical system for each spatial frequency. For smoother spatial tuning of inhibitory input than excitatory input, the eigenvalue spectrum of the dynamical system has a unique maximum, which indicates the most unstable spatial frequency. This frequency accurately predicts the grid spacing. We first consider place cell-like input (Gaussians) and then non-localized input (Gaussians convolved with white noise).

At the end of the analysis, you will find a glossary of the notation. Whenever we use P as a sub- or superscript instead of E or I, this implies that the equation holds for neurons of the excitatory and the inhibitory population.

The analysis is written as a detailed and comprehensible walk-through. The reader who is interested only in the result can jump to Equations 78 and 104.

#### Assumption of slow learning

The firing rate of the output neuron is the weighted sum of excitatory and inhibitory input rates:

$$
r^{out}=[w^{E}⋅r^{E}−w^{I}⋅r^{I}]_{+},
$$

where $[…]_{+}$ indicates that negative firing rates are set to zero.

Written as a differential equation, the excitatory learning rule with quadratic multiplicative normalization is given by:

$$
\frac{dw^{E}}{dt}=η_{E}(𝟙−\frac{w^{E}w^{E}^{T}}{‖w^{E}‖^{2}})r^{E}r^{out},
$$

where $𝟙$ is the $N_{E}\timesN_{E}$ identity matrix. The projection operator $\frac{w^{E}w^{E}^{T}}{‖w^{E}‖^{2}}$ ensures that the weights are constrained to remain on the hypersphere whose radius is determined by the initial value of the sum of the squares of all excitatory weights (Miller and MacKay, 1994). The inhibitory learning rule is given by:

$$
\frac{d⁢𝐰^{I}}{d⁢t}=η_{I}⁢𝐫^{I}⁢(r^{out}-ρ_{0}).
$$

We assume that the rat will learn slowly, such that it forages through the environment before significant learning (i.e. weight change) occurs. Therefore we can coarsen the time scale and rewrite Equation 5 and 6 as

$$
\frac{dw^{E}}{dt}=η_{E}⟨(𝟙−\frac{w^{E}w^{E}^{T}}{‖w^{E}‖^{2}})r^{E}r^{out}⟩_{x}
$$

and

$$
\frac{dw^{I}}{dt}=η_{I}⟨r^{I}(r^{out}−ρ_{0})⟩_{x},
$$

respectively, where the spatial average, $⟨…⟩_{x}$, is defined as

$$
⟨(…)⟩_{x}=\frac{1}{L}\int_{−L/2}^{+L/2}(…)dx
$$

and $L$ is the length of the linear track.

#### High density assumption and continuum limit for place cell-like input

We assume a high density of input neurons and formulate the system in continuous variables. More precisely, we assume the distance between two neighboring firing fields to be much smaller than the width of the firing fields, that is, $L/N_{P}≪\sigma_{P}$. Furthermore, we assume that the linear track is very long compared with the width of the firing fields, that is, $\sigma_{P}≪L$.

We replace the neuron index with the continuous variable $\mu$ and denote the weight $w_{\mu}^{P}$ and the tuning function $r^{P}⁢(\mu,x)$ associated with a place field that is centered at $\mu$ in the continuum limit as:

$$
w_{i}^{P}→w^{P}(\mu) and r_{i}^{P}(x)→r^{P}(\mu,x).
$$

The distance between two neighboring place fields is given by $Δ⁢\mu=L/N_{P}$. Thus, for sums over all neurons we get the following integral in the continuum limit:

$$
\sumi=1N_{P}f_{i}=\frac{1}{Δ⁢\mu}⁢\sumi=1N_{P}f_{i}⁢Δ⁢\mu→\frac{N_{P}}{L}⁢\int_{-L/2}^{+L/2}f⁢(\mu)⁢d⁢\mu.
$$

We will switch between the discrete and continuous formulations, using whatever is more convenient.

For place cell-like input we take Gaussian tuning curves:

$$
r_{i}^{P}⁢(x)=\alpha_{P}⁢exp⁡{-\frac{(x-\mu_{i})^{2}}{2⁢\sigma_{P}^{2}}},
$$

with height $\alpha_{P}$ and standard deviation $\sigma_{P}$. Thus, in the continuum limit we get:

$$
r_{i}^{P}(x)→r^{P}(\mu,x)=r^{P}(|x−\mu|)=\alpha_{P}exp⁡{−\frac{(x−\mu)^{2}}{2\sigma_{P}^{2}}}.
$$

Because of the translational invariance of $r^{P}⁢(\mu,x)$, integration over space gives the same result as integration over all center locations and the mean of all inputs is the same:

$$
⟨r_{i}^{P}(x)⟩_{x}=⟨r^{P}(\mu,x)⟩_{x}
$$



$$
=\frac{1}{L}\int_{−L/2}^{+L/2}r^{P}(\mu,x)dx
$$



$$
=\frac{1}{L}\int_{−L/2}^{+L/2}r^{P}(\mu,x)d\mu≈\frac{\alpha_{P}}{L}\sqrt{2\pi\sigma_{P}^{2}}=M_{P}/L
$$

where we introduced $M_{P}:=\alpha_{P}⁢\sqrt{2⁢\pi⁢\sigma_{P}^{2}}$ for the area under the tuning curves. Accordingly, we get a summarized input activity that is independent of location:

$$
\sumi=1N_{P}r_{i}^{P}(x)→\frac{N_{P}}{L}\int_{−L/2}^{+L/2}r^{P}(\mu,x)d\mu≈\frac{N_{P}}{L}M_{P}.
$$

#### Equal weights form a fixed point

In the following, we will show that equal weights $w^{E}⁢(\mu)=w_{0}^{E}$ and $w^{I}⁢(\mu^{′})=w_{0}^{I}$, $∀\mu,\mu^{′}$ form a fixed point if $w_{0}^{I}$ is chosen such that the output neuron fires at the target rate, $ρ_{0}$, throughout the arena. With equal weights we get a constant firing rate $r_{0}^{out}$,

$$
r^{out}⁢(x)=r_{0}^{out}=[w_{0}^{E}⁢\sumir_{i}^{E}⁢(x)-w_{0}^{I}⁢\sumir_{i}^{I}⁢(x)]_{+},
$$

which according to Equation 17 does not depend on $x$. Furthermore, according to Equation 14, $⟨r_{i}^{P}(x)⟩_{x}$ does not depend on the neuron index $i$. Now the stationarity of the excitatory weight evolution follows from Equation 7:

$$
\frac{dw_{i}^{E}}{dt}=η_{E}⟨r^{out}\sumjr_{j}^{E}(\delta_{ij}−\frac{w_{i}^{E}w_{j}^{E}}{\sumkw_{k}^{E}^{2}})⟩_{x}
$$



$$
=η_{E}r_{0}^{out}\sumj[⟨r_{j}^{E}⟩_{x}(\delta_{ij}−\frac{w_{0}^{E}^{2}}{N_{E}w_{0}^{E}^{2}})]
$$



$$
=\frac{r_{0}^{out}η_{E}M_{E}}{L}\sumj=1N_{E}(\delta_{ij}−\frac{1}{N_{E}})=0,
$$

that is, excitatory weights are stationary for all values of $w_{0}^{E}$ and $w_{0}^{I}$ (here $\delta_{i⁢j}$ denotes the Kronecker delta which is 1 if $i=j$ and 0 otherwise). This holds for all input functions for which $⟨r_{j}^{E}(x)⟩_{x}$ is independent of $j$. If $r^{out}=ρ_{0}$, it immediately follows from Equation 6 that $\frac{d⁢w^{I}}{d⁢t}=0$, so the inhibitory weights are stationary if

$$
ρ_{0}=w^{E}⋅r^{E}−w^{I}⋅r^{I}=w_{0}^{E}\sumir_{i}^{E}−w_{0}^{I}\sumjr_{j}^{I},
$$

which is fulfilled if

$$
w_{0}^{I}=\frac{w_{0}^{E}\sumir_{i}^{E}−ρ_{0}}{\sumjr_{j}^{I}}=\frac{w_{0}^{E}N_{E}M_{E}−ρ_{0}}{N_{I}M_{I}}.
$$

#### Linear stability analysis

In the following, we will show that the fixed point of equal weights, the homogeneous steady state, is unstable when the spatial tuning of inhibitory inputs is broader than that of the excitatory inputs. In this case, perturbations of the fixed point will grow and one particular spatial frequency will grow fastest. We will show that this spatial frequency predicts the spacing of the resulting periodic pattern (Figure 1g).

We perturb the fixed point

$$
w^{E}(\mu)=w_{0}^{E}+\deltaw^{E}(\mu),w^{I}(\mu)=w_{0}^{I}+\deltaw^{I}(\mu)
$$

and look at the time evolution of the perturbations $\frac{d⁢\delta⁢w^{E}}{d⁢t}$ and $\frac{d⁢\delta⁢w^{I}}{d⁢t}$ of the excitatory and inhibitory weights around the fixed point.

Close to the fixed point the output neuron fires around the target rate $ρ_{0}$. We thus ignore the rectification in Equation 4, that is, $r^{out}=ρ_{0}+\delta⁢r^{out}$, with $\delta⁢r^{out}=\sum_{k}\delta⁢w_{k}^{E}⁢r_{k}^{E}-\sum_{k^{′}}\delta⁢w_{k^{′}}^{I}⁢r_{k^{′}}^{I}$.

#### Time evolution of perturbations of the inhibitory weights

We start with the time evolution of the inhibitory weight perturbations:

$$
\frac{d\deltaw_{i}^{I}}{dt}=\frac{dw_{i}^{I}}{dt}=η_{I}⟨(r^{out}−ρ_{0})r_{i}^{I}⟩_{x}
$$



$$
=η_{I}⟨(ρ_{0}+\deltar^{out}−ρ_{0})r_{i}^{I}⟩_{x}
$$



$$
=η_{I}⟨r_{i}^{I}\deltar^{out}⟩_{x}
$$



$$
=η_{I}⟨r_{i}^{I}(\sumk\deltaw_{k}^{E}r_{k}^{E}−\sumk^{′}\deltaw_{k^{′}}^{I}r_{k^{′}}^{I})⟩_{x}
$$



$$
=η_{I}(\sumk=1N_{E}⟨r_{i}^{I}r_{k}^{E}⟩\deltaw_{k}^{E}−\sumk^{′}=1N_{I}⟨r_{i}^{I}r_{k^{′}}^{I}⟩\deltaw_{k^{′}}^{I}),
$$

where only the rates $𝐫^{P}$ depend on $x$. Intuitively, the first term in Equation 29 means that the rate of change of the inhibitory weight perturbation of the weight associated with one location depends on the excitatory perturbations of the weights associated with every other location, weighted with the overlap (the cross correlation) of the two associated tuning functions (analogous for inhibitory weight perturbations). In the continuum limit, the sums are:

$$
η^{P}\sumk=1N_{P^{′}}⟨r_{i}^{P}r_{k}^{P^{′}}⟩_{x}\deltaw_{k}^{P^{′}}→η^{P}\frac{N_{P^{′}}}{L}\int_{−L/2}^{+L/2}⟨r^{P}(\mu)r^{P^{′}}(\mu^{′})⟩_{x}\deltaw^{P^{′}}(\mu^{′})d\mu^{′}
$$



$$
=\int_{−L/2}^{+L/2}K^{PP^{′}}(\mu,\mu^{′})\deltaw^{P^{′}}(\mu^{′})d\mu^{′},
$$

where we introduce overlap kernels

$$
K^{PP^{′}}(\mu,\mu^{′}):=η^{P}\frac{N_{P^{′}}}{L}⟨r^{P}(\mu)r^{P^{′}}(\mu^{′})⟩_{x}P,P^{′}\in{E,I}.
$$

The overlap $⟨r^{P}(\mu)r^{P^{′}}(\mu^{′})⟩_{x}$depends only on the distance of the Gaussian fields, that is,

$$
K^{PP^{′}}⁢(\mu,\mu^{′})=K^{PP^{′}}⁢(\mu-\mu^{′}).
$$

Taking $L→∞$, the time evolution of the perturbations of the inhibitory weights can thus be written as convolutions:

$$
\frac{d\deltaw^{I}(\mu)}{dt}=(K^{IE}∗\deltaw^{E})(\mu)−(K^{II}∗\deltaw^{I})(\mu),
$$

where $*$ denotes a convolution.

#### Time evolution of perturbations of the excitatory weights

To derive the time evolution of the excitatory weights, we first show that the weight normalization term in Equation 7 , expressed through the projection operator $P_{i⁢j}=\frac{w_{i}⁢w_{j}}{\sum_{k}w_{k}^{2}}$, leads to a term that balances homogeneous weight perturbations and a term that can be neglected in the continuum limit.

Let $P$ be the projection operator responsible for the normalization of the excitatory weights by projecting a weight update onto a vector that is orthogonal to the hypersphere of constant $\sum_{i=1}^{N_{E}}(w_{i}^{E})^{2}$. We now determine the projection operator around the fixed point (We drop the index ‘E’ in the following, to improve readability):

$$
P_{i⁢j}=\frac{(w_{0}+\delta⁢w_{i})⁢(w_{0}+\delta⁢w_{j})}{\sum_{k}(w_{0}+\delta⁢w_{k})^{2}}≡P_{i⁢j}⁢(𝐰+\delta⁢𝐰).
$$

Using Taylor’s theorem

$$
P_{ij}(w+\deltaw)=P_{ij}(w)+\suml=1N\deltaw_{l}\frac{dP_{ij}(w)}{dw_{l}}+𝒪(\deltaw^{2})
$$

and $w_{l}=w_{0}∀l$, we get

$$
P_{ij}(w)=\frac{w_{i}w_{j}}{\sumkw_{k}^{2}}=1/N,
$$



$$
\frac{dP_{ij}(w)}{dw_{l}}=\frac{\delta_{il}w_{j}}{\sumkw_{k}^{2}}+\frac{\delta_{jl}w_{i}}{\sumkw_{k}^{2}}−\frac{w_{i}w_{j}2w_{l}}{(\sumkw_{k}^{2})^{2}}=\frac{\delta_{il}}{Nw_{0}}+\frac{\delta_{jl}}{Nw_{0}}−\frac{2}{N^{2}w_{0}}.
$$

In summary this gives:

$$
P_{i⁢j}=\frac{1}{N_{E}}⏟≡P_{0}⁣∝𝒪⁢(1)+\frac{1}{N_{E}⁢w_{0}^{E}}⁢(\delta⁢w_{i}^{E}+\delta⁢w_{j}^{E}-\frac{2⁢\sum_{l=1}^{N_{E}}\delta⁢w_{l}^{E}}{N_{E}})⏟≡\delta⁢P_{i⁢j}⁣∝𝒪⁢(\delta⁢𝐰)+𝒪⁢(\delta⁢𝐰^{2}).
$$

Using the perturbed projection operator Equation 39 with Equation 7, we obtain the time evolution of the excitatory weight perturbation to linear order:

$$
\frac{d\deltaw_{i}^{E}}{dt}=\frac{dw_{i}^{E}}{dt}
$$



$$
=η_{E}⟨r^{out}\sumj(\delta_{ij}−P_{ij})r_{j}^{E}⟩_{x}
$$



$$
=η_{E}⟨(ρ_{0}+\deltar^{out})\sumj(\delta_{ij}−P_{0}−\deltaP_{ij})r_{j}^{E}⟩_{x}
$$



$$
=η_{E}⟨ρ_{0}\sumj(\delta_{ij}−P_{0})r_{j}^{E}⟩_{x}⏟=0,cf.Equation19+⟨\deltar^{out}\sumj(\delta_{ij}−P_{0})r_{j}^{E}⟩_{x}−⟨ρ_{0}\sumj\deltaP_{ij}r_{j}^{E}⟩_{x}+𝒪(\deltaw^{2})
$$



$$
=η_{E}(⟨r_{i}^{E}\deltar^{out}⟩_{x}⏟(1)−P_{0}⟨\deltar^{out}\sumjr_{j}^{E}⟩_{x}⏟(2)−ρ_{0}⟨\sumj\deltaP_{ij}r_{j}^{E}⟩_{x}⏟(3))+𝒪(\deltaw^{2})
$$

Term $(1)$ in Equation 44 has a similar structure as in the inhibitory case (Equation 27), and will lead to analogous convolutions. he second term is given by

$$
(2)=\frac{1}{N_{E}}⟨(\sumkr_{k}^{E}\deltaw_{k}^{E}−\sumk^{′}r_{k^{′}}^{I}\deltaw_{k^{′}}^{I})\sumjr_{j}^{E}⟩_{x}
$$



$$
=\frac{M_{E}}{L}⟨\sumkr_{k}^{E}\deltaw_{k}^{E}−\sumk^{′}r_{k^{′}}^{I}\deltaw_{k^{′}}^{I}⟩_{x}
$$



$$
=\frac{M_{E}}{L}(\sumk⟨r_{k}^{E}⟩_{x}\deltaw_{k}^{E}−\sumk^{′}⟨r_{k^{′}}^{I}⟩_{x}\deltaw_{k^{′}}^{I})
$$



$$
=\frac{M_{E}}{L^{2}}(M_{E}\sumk\deltaw_{k}^{E}−M_{I}\sumk^{′}\deltaw_{k^{′}}^{I})
$$



$$
cont. limit→\frac{M_{E}}{L^{3}}(N_{E}M_{E}\int_{−L/2}^{+L/2}\deltaw^{E}(\mu^{′})d\mu^{′}−N_{I}M_{I}\int_{−L/2}^{+L/2}\deltaw^{I}(\mu^{′′})d\mu^{′′})
$$

and the third term by

$$
(3)=\frac{ρ_{0}}{N_{E}w_{0}^{E}}⟨\sumjr_{j}^{E}(\deltaw_{i}^{E}+\deltaw_{j}^{E}−\frac{2}{N_{E}}\suml\deltaw_{l}^{E})⟩_{x}
$$



$$
=\frac{ρ_{0}}{N_{E}w_{0}^{E}}\sumj⟨r_{j}^{E}⟩_{x}(\deltaw_{i}^{E}+\deltaw_{j}^{E}−\frac{2}{N_{E}}\suml\deltaw_{l}^{E})
$$



$$
=\frac{ρ_{0}M_{E}}{N_{E}w_{0}^{E}L}\sumj(\deltaw_{i}^{E}+\deltaw_{j}^{E}−\frac{2}{N_{E}}\suml\deltaw_{l}^{E})
$$



$$
=\frac{ρ_{0}M_{E}}{w_{0}^{E}L}(\deltaw_{i}^{E}+\frac{1}{N_{E}}\sumj\deltaw_{j}^{E}−\frac{2}{N_{E}}\suml\deltaw_{l}^{E})
$$



$$
=\frac{ρ_{0}M_{E}}{w_{0}^{E}L}(\deltaw_{i}^{E}−\frac{1}{N_{E}}\sumj\deltaw_{j}^{E})
$$



$$
cont. limit→\frac{ρ_{0}M_{E}}{w_{0}^{E}L}(\deltaw^{E}(\mu)−\frac{1}{L}\int_{−L/2}^{+L/2}\deltaw^{E}(\mu^{′})d\mu^{′})
$$



$$
=\frac{ρ_{0}M_{E}}{w_{0}^{E}L}\int_{−L/2}^{+L/2}d\mu^{′}\deltaw^{E}(\mu^{′})[\delta(\mu−\mu^{′})−\frac{1}{L}],
$$

where $\delta⁢(\mu-\mu^{′})$ denotes the Dirac delta function. Together, this leads to the time evolution of the excitatory weight perturbations:

$$
\frac{d\deltaw^{E}(\mu)}{dt}=\int_{−L/2}^{+L/2}d\mu^{′}\deltaw^{E}(\mu^{′})[K^{EE}(\mu−\mu^{′})−\frac{η_{E}ρ_{0}M_{E}}{w_{0}^{E}L}\delta(\mu−\mu^{′})
$$



$$
+\frac{η_{E}M_{E}}{L^{2}}(\frac{ρ_{0}}{w_{0}^{E}}−\frac{N_{E}M_{E}}{L})]
$$



$$
−\int_{−L/2}^{+L/2}d\mu^{′′}\deltaw^{I}(\mu^{′′})[K^{EI}(\mu−\mu^{′′})−\frac{η_{E}N_{I}M_{E}M_{I}}{L^{3}}].
$$

We now assume $L≫\sigma_{P}$ and write everything as convolutions, also trivial ones:

$$
\frac{d\deltaw^{E}(\mu)}{dt}=([K^{EE}−\frac{η_{E}ρ_{0}M_{E}}{w_{0}^{E}L}\delta+\frac{η_{E}M_{E}}{L^{2}}(\frac{ρ_{0}}{w_{0}^{E}}−\frac{N_{E}M_{E}}{L})]∗\deltaw^{E})(\mu)−([K^{EI}−\frac{η_{E}N_{I}M_{E}M_{I}}{L^{3}}]∗\deltaw^{I})(\mu).
$$

#### Decoupling of spatial frequencies

The convolutions in Equations 34 and 60 show how the excitatory and inhibitory weight perturbations at one location influence the time evolution of weights at every other location. Transforming the system to frequency space leads to a drastic simplification: The time evolution of a perturbation of a particular spatial frequency depends only on the excitatory and inhibitory perturbation of the same spatial frequency, that is, the Fourier components decouple. We define the Fourier transform $f⁢(k)≡ℱ⁢[f⁢(\mu)]$ with wavevector $k$ of a function $f⁢(\mu)$ of location $\mu$ as:

$$
f⁢(k)≡\int_{-∞}^{+∞}f⁢(\mu)⁢e^{-i⁢k⁢\mu}⁢d⁢\mu
$$

and note that

$$
\int_{-∞}^{+∞}e^{-i⁢k⁢\mu}⁢d⁢\mu=2⁢\pi⁢\delta⁢(k).
$$

Using the Convolution theorem and the linearity of the Fourier transform we get

$$
\frac{d\deltaw^{E}(k)}{dt}=[\frac{η_{E}M_{E}}{L^{2}}(\frac{ρ_{0}}{w_{0}^{E}}−\frac{N_{E}M_{E}}{L})\deltaw^{E}(k)+\frac{η_{E}N_{I}M_{E}M_{I}}{L^{3}}\deltaw^{I}(k)]2\pi\delta(k)−\frac{η_{E}ρ_{0}M_{E}}{w_{0}^{E}L}\deltaw^{E}(k)+[K^{EE}(k)\deltaw^{E}(k)−K^{EI}(k)\deltaw^{I}(k)]
$$

and

$$
\frac{d\deltaw^{I}(k)}{dt}=K^{IE}(k)\deltaw^{E}(k)−K^{II}(k)\deltaw^{I}(k).
$$

The $\delta⁢(k)$ term in Equation 63 balances homogeneous perturbations in such a way that the output neuron would still fire at the target rate, if not for permutations at other frequencies. In the following, we drop this term, because we are not interested in spatially homogeneous perturbations. Moreover, the continuum limit is valid only for high densities: $N_{P}/L→∞$. We can thus drop terms of lower order than $N_{P}/L$, which eliminates the $\frac{η_{E}⁢ρ_{0}⁢M_{E}}{w_{0}^{E}⁢L}$ term. Writing the remaining terms of Equations 63 and 64 as a matrix leads to:

$$
[\deltaw^{E}˙\deltaw^{I}˙](k)=[K^{EE}(k)−K^{EI}(k)K^{IE}(k)−K^{II}(k)][\deltaw^{E}\deltaw^{I}](k),
$$

which no longer contains terms from the weight normalization. The characteristic polynomial of the above matrix is:

$$
\lambda^{2}+\lambda(K^{II}−K^{EE})+K^{EI}K^{IE}−K^{EE}K^{II}=0
$$

The difference, $K^{EI}K^{IE}−K^{EE}K^{II}$, vanishes for Gaussian input, because:

$$
K^{PP^{′}}(\mu,\mu^{′}=0)=\frac{η^{P}N_{P^{′}}}{L}⟨r^{P}(\mu)r^{P^{′}}(0)⟩_{x}
$$



$$
=\frac{\alpha_{P}\alpha_{P^{′}}η^{P}N_{P^{′}}}{L^{2}}\int_{−L/2}^{+L/2}dxexp⁡{−\frac{(x−\mu)^{2}}{2\sigma_{P}^{2}}−\frac{x^{2}}{2\sigma_{P^{′}}^{2}}}
$$



$$
≈\frac{\alpha_{P}\alpha_{P^{′}}η^{P}N_{P^{′}}}{L^{2}}\sqrt{\frac{2\pi}{\frac{1}{\sigma_{P}^{2}}+\frac{1}{\sigma_{P^{′}}^{2}}}}exp⁡{−\frac{\mu^{2}}{2(\sigma_{P}^{2}+\sigma_{P^{′}}^{2})}},
$$

where we completed the square and used $\int_{−∞}^{+∞}e^{−ax^{2}}=\sqrt{\frac{\pi}{a}}$. Taking the Fourier transform and completing the square again gives

$$
K^{PP^{′}}(k)=\frac{η^{P}N_{P^{′}}M_{P} M_{P^{′}}}{L^{2}}exp⁡{−\frac{k^{2}}{2}(\sigma_{P}^{2}+\sigma_{P^{′}}^{2})}.
$$

and thus $K^{EI}K^{IE}−K^{EE}K^{II}=0$.

For $P=P^{′}$, Equation 70 simplifies to:

$$
K^{PP}(k)=\frac{η^{P}N_{P}M_{P}^{2}}{L^{2}}exp⁡{−k^{2}\sigma_{P}^{2}}.
$$

This leads to the eigenvalues:

$$
\lambda_{0}(k)=0
$$



$$
\lambda_{1}(k)=K^{EE}(k)−K^{II}(k)
$$



$$
=\frac{1}{L^{2}}(η_{E}M_{E}^{2}N_{E}exp⁡{−k^{2}\sigma_{E}^{2}}−η_{I}M_{I}^{2}N_{I}exp⁡{−k^{2}\sigma_{I}^{2}}),
$$

which are shown in Figure 8a. Perturbations with spatial frequencies for which $\lambda_{1}⁢(k)$ is positive will grow. Setting $\frac{d⁢\lambda_{1}⁢(k)}{d⁢k}=0$ gives the wavevector $k_{max}$ of the Fourier component that grows fastest:

![Figure 8.](https://cdn.elifesciences.org/articles/34560/elife-34560-fig8-v2.jpg)

**Figure 8.:** (a) The eigenvalue spectrum for the eigenvalues of Equation 72 for an excitatory tuning of width $\sigma_{E}=0.03$. The first eigenvalue $\lambda_{0}$ is always 0. If the inhibitory tuning is more narrow than the excitatory tuning, that is, $\sigma_{I}<\sigma_{E}$, the second eigenvalue $\lambda_{1}$ is negative for every wavevector $k$. For $\sigma_{I}>\sigma_{E}$ the eigenvalue spectrum has a unique positive maximum $k_{max}$, that is, a most unstable spatial frequency. The wavevector $k_{max}$ at which $\lambda_{1}$ is maximal is obtained from Equation 78 and marked with a dashed line. (b) The dependence of the grid spacing on learning rate $η_{I}$, number of input neurons $N_{I}$ and input height $\alpha_{I}$ is accurately predicted by the theory. The gray line shows the grid spacing obtained from Equation 78. We vary the inhibitory learning rate, $η_{I}$ (circles), the number of inhibitory input neurons, $N_{I}$ (squares), or the square of the height of the inhibitory input place fields, $\alpha_{I}^{2}$ (diamonds). The horizontal axis shows the ratio of the product $η_{I}⁢N_{I}⁢\alpha_{I}^{2}$ to the initial value of the product $\gamma_{0}$. We keep $η_{E}=0.3\times10^{-4}$, $N_{E}=800$ and $\alpha_{E}=1$ in each simulation and the $\gamma_{0}$ parameters are: $η_{I}=0.3\times10^{-3}$, $N_{I}=200$, $\alpha_{I}=1$. (c) Distribution of minimal values of GRF input. Histograms show the distribution of the minimal values of 1000 Gaussian random fields for a small linear track, $L=2$, and a large linear track $L=1000$. Red and blue colors correspond to the tuning of excitatory and inhibitory input neurons, respectively. Each dotted line indicates the mean of the histogram of the same color. For larger systems, the distribution of the minimum values gets more narrow and the relative distance between the minima of excitatory and inhibitory neurons decreases.

$$
\frac{2}{L^{2}}(η_{I}M_{I}^{2}N_{I}\sigma_{I}^{2}k_{max}exp⁡{−k_{max}^{2}\sigma_{I}^{2}}−η_{E}M_{E}^{2}N_{E}\sigma_{E}^{2}k_{max}exp⁡{−k_{max}^{2}\sigma_{E}^{2}})=0
$$



$$
⇒ln⁡(η_{I}M_{I}^{2}N_{I}\sigma_{I}^{2})−k_{max}^{2}\sigma_{I}^{2}=ln⁡(η_{E}M_{E}^{2}N_{E}\sigma_{E}^{2})−k_{max}^{2}\sigma_{E}^{2}
$$



$$
⇒k_{max}=\sqrt{\frac{ln⁡(\frac{η_{I}M_{I}^{2}N_{I}\sigma_{I}^{2}}{η_{E}M_{E}^{2}N_{E}\sigma_{E}^{2}})}{\sigma_{I}^{2}−\sigma_{E}^{2}}}.
$$

Assuming that the fastest-growing spatial frequency from the linearized system will prevail, the final spacing of the periodic pattern, $ℓ$, is determined by:

$$
ℓ=2\pi/k_{max}=2\pi\sqrt{\frac{\sigma_{I}^{2}−\sigma_{E}^{2}}{ln⁡(\frac{η_{I}M_{I}^{2}N_{I}\sigma_{I}^{2}}{η_{E}M_{E}^{2}N_{E}\sigma_{E}^{2}})}}=2\pi\sqrt{\frac{\sigma_{I}^{2}−\sigma_{E}^{2}}{ln⁡(\frac{η_{I}N_{I}\alpha_{I}^{2}\sigma_{I}^{4}}{η_{E}N_{E}\alpha_{E}^{2}\sigma_{E}^{4}})}.}
$$

Equation 78 is in exact agreement with the grid spacing obtained in simulations (Figure 1g). Moreover, it indicates the bifurcation point: When excitation is as smooth as inhibition ($\sigma_{E}=\sigma_{I}$), there is no unstable spatial frequency anymore and every perturbation gets balanced (Figure 1g compare Equation 103). The grid spacing also depends on the ratio of the inhibitory and excitatory parameters $η^{P},N_{P},\alpha_{P}$ (logarithmic term in Equation 78). We confirm this dependence with simulations on the linear track where we increase either $η_{I}$ or $N_{I}$ or $\alpha_{I}^{2}$ such that the product $\gamma=η_{I}⁢N_{I}⁢\alpha_{I}^{2}$ increases with respect to the initial product $\gamma_{0}$. We find a good agreement with the theoretical prediction for all three variations (Figure 8b).

Note that the term $η^{P}⁢M_{P}^{2}⁢N_{P}$ in the logarithm in Equation 78 is essentially a factor that determines the rate of weight change of population $P: η^{P}$ is just the scaling factor; $M_{P}$ is the mass under a tuning function (with quadratic influence: once directly through the firing rate of the input, once through the increased firing rate of the output neuron); $N_{P}$ is the number of tuning functions. The remaining $\sigma_{P}^{2}$ originates specifically from the Gaussian shape of the tuning functions.

#### Analysis for non-localized input (Gaussian random fields)

Above, we derived the time evolution of perturbations of excitatory and inhibitory weights for place field-like input, that is, Gaussian tuning curves. In the following we conduct a similar analysis, using non-localized input, that is, random functions with a given spatial autocorrelation length. We show that the grid spacing is predicted by an equation that is equivalent to Equation 78.

The non-localized input $r_{i}^{P}$ for input neuron $i$ of population $P$ was obtained by rescaling a Gaussian random field (GRF) $g_{i}^{P}$ to mean $1/2$ and minimum 0:

$$
r_{i}^{P}(x)=\frac{g_{i}^{P}(x)−minxg_{i}^{P}(x)}{2⟨g_{i}^{P}(x)−minxg_{i}^{P}(x)⟩}_{x},
$$

where $min_{x}$ denotes the minimum over all locations and the GRF $g_{i}^{P}$ is obtained by convolving a Gaussian $𝒢^{P}(x)=exp⁡(−x^{2}/2\sigma_{P}^{2})$ with white noise $ξ_{i}$ from a uniform distribution between $-0.5$ and $0.5$:

$$
g_{i}^{P}(x)=\int𝒢^{P}(x−x^{′})ξ_{i}^{P}(x^{′})dx^{′}.
$$

As the white noise has zero mean, the spatial average of a GRF is also 0 in expectation:

$$
⟨g_{i}^{P}(x)⟩_{x}=\int⟨𝒢^{P}(x−x^{′})⟩_{x}ξ_{i}^{P}(x^{′})dx^{′}
$$



$$
∝\intξ_{i}^{P}(x^{′})dx^{′}=0.
$$

The individual minima $min_{x}⁡g_{i}^{P}⁢(x)$ in Equation 79 would complicate the subsequent analysis. If we again consider infinitely large systems $L→∞$ with infinite density $N_{P}/L→∞$, Equation 79 simplifies. The mean of the distribution of GRF minima over different input neurons scales logarithmically with the number of samples (Bovier, 2005). Here the number of samples corresponds to the number of minima in a GRF, which scales inversely with the width of the convolution kernel that was used to obtain the GRF:

$$
Number of minima in a GRF∝L/\sigma_{P}.
$$

In the continuum limit the variance of the minima distribution over cells decreases and the relative difference between the mean minimum value of excitation and inhibition vanishes (Figure 8c):

$$
\frac{log⁡(L/\sigma_{E})−log⁡(L/\sigma_{I})}{log⁡(L/\sigma_{E})}=\frac{log⁡(\sigma_{I}/\sigma_{E})}{log⁡(L/\sigma_{E})}→0.
$$

NB: For the argument it doesn’t matter if it scales purely logarithmically or with $log^{\gamma}$, where $\gamma$ is any exponent.

Thus, we take the minimum value as a constant m, which does neither depend on the population nor on the input neuron. This leads to a simplified expression of the input tuning functions:

$$
r_{i}^{P}⁢(x)=\frac{1}{2}⁢(1-\frac{g_{i}^{P}⁢(x)}{m}).
$$

As $⟨r_{i}^{P}⟩=0.5$ is independent of $i$, equal excitatory weights are a fixed point for the excitatory learning rule Equation 7 as described in Equation 19. Moreover, the sum over all input neurons does not depend on the location:

$$
\sumi=1N_{P}r_{i}^{P}(x)=\frac{1}{2}(\sumi=1N_{P}1−\sumi=1N_{P}g_{i}^{P}(x))=\frac{N_{P}}{2}−\frac{1}{2}\int𝒢^{P}(x−x^{′})\sumi=1N_{P}ξ_{i}^{P}(x^{′})⏟=0in cont. limitdx^{′}=\frac{N_{P}}{2}.
$$

Therefore, given constant excitatory weights, all inhibitory weights can be set to a value $w_{0}^{I}$ such that the output neuron fires at the target rate, that is, homogeneous weights are a fixed point of the learning rules, as in the scenario with Gaussian input. Moreover, Equation 29 holds also for GRF input. The analysis of the projection operator (see above) of the weight normalization lead to a term of homogeneous weight perturbations and a term that could be neglected in the high density limit. We now omit these terms a priori. The time evolution of excitatory and inhibitory weight perturbations can thus be summarized as (compare Equations 29 and 44):

$$
\frac{d\deltaw_{i}^{P}}{dt}=η^{P}(\sumk=1N_{E}⟨r_{i}^{P}(x)r_{k}^{E}(x)⟩_{x} \deltaw_{k}^{E}−\sumk^{′}=1N_{I}⟨r_{i}^{P}(x)r_{k^{′}}^{I}(x)⟩_{x} \deltaw_{k^{′}}^{I}).
$$

The above equation describes the time evolution of each synaptic weight. For the Gaussian input of the earlier sections, each synaptic weight is associated with one location. In the continuum limit we thus identified the synaptic weight associated with location $\mu$ with $w^{P}⁢(\mu)$. An increase of $w^{E}⁢(\mu)$ corresponded to an increase in firing at location $\mu$ (and in the surrounding, given by the width of the Gaussian of the excitatory tuning). Analogously, an increase of $w^{I}⁢(\mu)$ caused a decrease in firing at location $\mu$ (and in the surrounding, given by the width of the Gaussian of the inhibitory tuning). Because of the non-localized tuning of GRF input, each synaptic weight has an influence on the firing rate at many locations. The influence of neuron $i$ of population $P$ at location $\mu$ is expressed by $ξ_{i}^{P}⁢(\mu)$. If one wanted to increase the firing rate at a specific location $\mu$ – and not just everywhere – one would thus increase all excitatory weights with high $ξ_{i}^{P}⁢(\mu)$ and decrease all excitatory weights with low $ξ_{i}^{P}⁢(\mu)$ (note that $ξ^{P}$ can also be negative). The ‘weight’ that corresponds to location $\mu$ is thus expressed as:

$$
w^{P}(\mu):=\sumi=1N_{P}w_{i}^{P}ξ_{i}^{P}(\mu),
$$

where we weight each synaptic weight with the value of the corresponding white noise at location $\mu$. This corresponds to expressing the weights in a basis that is associated with the location and not with the individual input neurons. Combining Equation 88 and Equation 87 gives the time evolution of the weight perturbations associated with location $\mu$:

$$
\frac{d\deltaw^{P}(\mu)}{dt}=\sumi=1N_{P}ξ_{i}^{P}(\mu)\frac{d\deltaw_{i}^{P}}{dt}
$$



$$
=η^{P}\sumi=1N_{P}ξ_{i}^{P}(\mu)(\sumk=1N_{E}⟨r_{i}^{P}(x)r_{k}^{E}(x)⟩_{x} \deltaw_{k}^{E}−\sumk^{′}=1N_{I}⟨r_{i}^{P}(x)r_{k^{′}}^{I}(x)⟩_{x} \deltaw_{k′}^{I}).
$$

We now look at the first term of the above equation, the second term will be treated analogously:

$$
\sumi=1N_{P}ξ_{i}^{P}(\mu)\sumk=1N_{E}⟨r_{i}^{P}(x)r_{k}^{E}(x)⟩_{x} \deltaw_{k}^{E}=⟨(\sumi=1N_{P}ξ_{i}^{P}(\mu)r_{i}^{P}(x))(\sumk=1N_{E}\deltaw_{k}^{E}r_{k}^{E}(x))⟩_{x}.
$$

The sum containing the white noise can be simplified using the zero mean property and the expression for the variance of uniform white noise:

$$
\sumi=1N_{P}ξ_{i}^{P}(\mu)r_{i}^{P}(x)=\frac{1}{2}(\sumi=1N_{P}ξ_{i}^{P}(\mu)⏟=0−\frac{1}{m}\sumi=1N_{P}ξ_{i}^{P}(\mu)g_{i}^{P}(x))
$$



$$
=−\frac{1}{2m}\sumi=1N_{P}\int𝒢^{P}(x−x^{′})\sumi=1N_{P}ξ_{i}^{P}(\mu)ξ_{i}^{P}(x^{′})⏟=\betaN_{P}\delta(x^{′}−\mu)incont.limitdx^{′}
$$



$$
=−\frac{\betaN_{P}}{2m}𝒢^{P}(x−\mu),
$$

where $\beta$ is a proportionality constant that does not depend on the population type $P$. The Dirac delta $\delta⁢(x^{′}-\mu)$ occurs, because the white noise at different locations is uncorrelated. The sum of the product of weight perturbations and input rates can be rewritten as:

$$
\sumk=1N_{E}\deltaw_{k}^{E}r_{k}^{E}(x)=\frac{1}{2}(\sumk=1N_{E}\deltaw_{k}^{E}⏟homog.pert.−\frac{1}{m}\int𝒢^{E}(x−\mu^{′})\sumk=1N_{E}\deltaw_{k}^{E}ξ_{k}^{E}(\mu^{′})⏟=:\deltaw^{E}(\mu^{′}); Equation 88d\mu^{′}).
$$

The first term is independent of location $x$ and thus will lead only to spatially homogeneous perturbations, which we do not consider in the following. Inserting Equations 94 and 95 and the analogous terms for inhibition in Equation 91 leads to:

$$
\sumi=1N_{P}ξ_{i}^{P}(\mu)\sumk=1N_{E}⟨r_{i}^{P}(x)r_{k}^{E}(x)⟩\deltaw_{k}^{E}=\frac{\betaN_{P}}{4m^{2}}\int⟨𝒢^{P}(x−\mu)𝒢^{E} (x−\mu^{′})⟩_{x} \deltaw^{E}(\mu^{′})d\mu^{′}
$$



$$
=\frac{1}{η^{P}}\intK^^{PE}(\mu−\mu^{′})\deltaw^{E}(\mu^{′})d\mu^{′}
$$



$$
=\frac{1}{η^{P}}(K^^{PE}∗\deltaw^{E})(\mu),
$$

where we introduce kernels for the translation invariant overlap between two Gaussians with different centers (similar to Equation 32):

$$
K^^{PP^{′}}(\mu−\mu^{′}):=\frac{\betaη N_{P}}{4m^{2}}⟨𝒢^{P}(\mu)𝒢^{P}(\mu^{′})⟩_{x}=\frac{\betaη N_{P}}{4m^{2}}⟨𝒢^{P}(0)𝒢^{P^{′}}(|\mu−\mu^{′}|)⟩_{x}
$$

Equation 89 can thus be written as:

$$
\frac{d\deltaw^{P}(\mu)}{dt}=(K^^{PE}∗\deltaw^{E})(\mu)−(K^^{PI}∗\deltaw^{I})(\mu),
$$

which leads to a dynamical system for the Fourier components of the weight perturbations that is equivalent to Equation 65 with eigenvalues:

$$
\lambda_{0}(k)=0
$$



$$
\lambda_{1}(k)=K^^{EE}(k)−K^^{II}(k)
$$



$$
=\frac{\beta}{4m^{2}}(η_{E}M_{E}^{2}N_{E}exp⁡{−k^{2} \sigma^{2}}−η_{I}M_{I}^{2}N_{I}exp⁡{−k^{2}\sigma^{2}}).
$$

Thus, we get the same expression for the grid spacing as in the scenario of Gaussian input (with $\alpha_{E}$ = $\alpha_{I}$ = 1):

$$
ℓ=\sqrt{\frac{\sigma_{I}^{2}−\sigma_{E}^{2}}{ln⁡(\frac{η_{I}\sigma_{I}^{4}N_{I}}{η_{E}\sigma_{E}^{4}N_{E}})}.}
$$

### Glossary

A summary of notation:

$$
The rat^{′}s position at time t:x(t)Spatial dimensions x,y and head direction z:x=(x,y,z)Population label; can be E (excitatory) or I (inhibitory):PStandard deviation of Gaussian tuning of population P:\sigma_{P}Spatial autocorrelation length of input of population P:\sigma_{P,corr}Number of input neurons of population P:N_{P}Number of place fields per input neuron of population P:N_{P}^{f}Firing rate of output neuron:r^{out}(x)Firing rate of input neuron i of population P:r_{i}^{P}(x)Synaptic weight of input neuron i of population P to output neuron:w_{i}^{P}(t)Learning rates of excitation and inhibition:η_{E},η_{I}Target rate of the output neuron:ρ_{0}Length of linear track:LHeight of the Gaussian input fields:\alpha_{E},\alpha_{I}Value of Gaussian with standard deviation \sigma_{P} at location x:𝒢^{P}(x)Von Mises distribution with width \sigma_{P} that is periodic in [−L/2,L/2]:ℳ^{P}(x)
$$
