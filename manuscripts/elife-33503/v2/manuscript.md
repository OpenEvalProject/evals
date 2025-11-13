# Inferring circuit mechanisms from sparse neural recording and global perturbation in grid cells

## Authors

- John Widloski<sup>1</sup> ([ORCID: 0000-0003-4236-8957](https://orcid.org/0000-0003-4236-8957)) †
- Michael P Marder<sup>2</sup>
- Ila R Fiete<sup>2</sup> ([ORCID: 0000-0003-4738-2539](https://orcid.org/0000-0003-4738-2539)) †

### Affiliations

1. Department of Psychology The University of California Berkeley United States
2. Department of Physics The University of Texas Austin United States
3. Center for Learning and Memory The University of Texas Austin United States

† Corresponding author

## Abstract

A goal of systems neuroscience is to discover the circuit mechanisms underlying brain function. Despite experimental advances that enable circuit-wide neural recording, the problem remains open in part because solving the ‘inverse problem’ of inferring circuity and mechanism by merely observing activity is hard. In the grid cell system, we show through modeling that a technique based on global circuit perturbation and examination of a novel theoretical object called the distribution of relative phase shifts (DRPS) could reveal the mechanisms of a cortical circuit at unprecedented detail using extremely sparse neural recordings. We establish feasibility, showing that the method can discriminate between recurrent versus feedforward mechanisms and amongst various recurrent mechanisms using recordings from a handful of cells. The proposed strategy demonstrates that sparse recording coupled with simple perturbation can reveal more about circuit mechanism than can full knowledge of network activity or the synaptic connectivity matrix.

## Introduction

In systems neuroscience we seek to discover how neural responses and complex functionality can emerge from the dynamical interactions of neurons in circuits. For instance, the circuit mechanisms that give rise to orientation tuning in primary visual cortex have been closely studied for the better part of a century (Hubel and Wiesel, 1959). Despite these efforts, arbitrating between between different candidate mechanisms has been difficult. Our experimental tools are typically observational: Neurons are recorded, often during a behavior, in increasing numbers today (Dombeck et al., 2010; Ahrens et al., 2012; Ziv et al., 2013; Dunn et al., 2016). Our theoretical models usually run in the ‘forward’ direction: We build hypothesized circuits to reproduce the observed activity data. Because there often is a many-to-one mapping from plausible models to neural activity, it is difficult to know which model more accurately describes the underlying system. For this reason, it remains unsettled whether – to return to a familiar example – orientation tuning arises mostly from selective feedforward summation of inputs or lateral interactions (Rivlin-Etzion et al., 2012; Kim et al., 2014; Takemura et al., 2013; Ferster and Miller, 2000; Sompolinsky and Shapley, 1997).

Here, we show that grid cells (Hafting et al., 2005) provide a unique opportunity to understand cortical circuit mechanism, when coupled with a novel approach for doing so. The promise of our approach lies in the fact that (1) it is not merely observational but rather relies on perturbation, and (2) it provides a novel theoretical measure (the ‘distribution of relative phase shifts’ or DRPS) along which several competing feedforward and recurrent grid cell models can be distinguished with the perturbative experiments.

The structure of grid cell responses – with their periodic tuning to 2D space – makes the system particularly amenable to dissection, as we will see below. Grid cells have already yielded insight into their underpinnings: All cells with a common spatial tuning period remain confined to a single 2D manifold in activity space, and this manifold is invariant over time even when grid cell tuning curves deform as the animals are moved between novel and familiar environments (Yoon et al., 2013; Fyhn et al., 2007), as well as during REM and non-REM sleep (Gardner et al., 2017; Trettel et al., 2017). These findings imply the existence of a 2D continuous attractor dynamics within or feeding into the grid cell circuit.

Many models reproduce the spatially periodic responses of individual grid cells or groups of cells (Fuhs and Touretzky, 2006; Burak and Fiete, 2006; McNaughton et al., 2006; Hasselmo et al., 2007; Burgess et al., 2007; Kropff and Treves, 2008; Guanella et al., 2007; Burak and Fiete, 2009; Welday et al., 2011; Dordek et al., 2016). These include models in which the mechanism of grid tuning is a selective feedforward summation of spatially tuned responses (Kropff and Treves, 2008; Dordek et al., 2016; Stachenfeld et al., 2017), recurrent network architectures that lead to the stabilization of certain population patterns (Fuhs and Touretzky, 2006; Burak and Fiete, 2006; Guanella et al., 2007; Burak and Fiete, 2009; Pastoll et al., 2013; Brecht et al., 2014; Widloski and Fiete, 2014), the interference of temporally periodic signals in single cells (Hasselmo et al., 2007; Burgess et al., 2007), or a combination of some of these mechanisms (Welday et al., 2011; Bush and Burgess, 2014). They employ varying levels of mechanistic detail and make different assumptions about the inputs to the circuit. Because exclusively single-cell models lack the low-dimensional network-level dynamical constraints observed in grid cell modules (Yoon et al., 2013), and are further challenged by constraints from biophysical considerations (Welinder et al., 2008; Remme et al., 2010) and intracellular responses (Domnisoru et al., 2013; Schmidt-Hieber and Häusser, 2013), we do not further consider them here. The various recurrent network models (Fuhs and Touretzky, 2006; Burak and Fiete, 2006; McNaughton et al., 2006; Guanella et al., 2007; Burak and Fiete, 2009; Brecht et al., 2014) produce single neuron responses consistent with data and further predict the long-term, across-environment, and across-behavioral state cell–cell relationships found in the data (Yoon et al., 2013; Fyhn et al., 2007; Gardner et al., 2017; Trettel et al., 2017), but are indistinguishable on the basis of existing data and analyses. Here we examine ways to distinguish between a subset of grid cell models, specifically between the recurrent and feedforward models, and also between various recurrent network models. We call this subset of models our candidate models. Our goal is not to provide new models of grid cell activity, but rather to show, through theory and modeling, how the candidate models could be feasibly distinguished through experiment.

The candidate models form a diverse set, with differences that carry important implications for mechanism and for how the network could have developed from plasticity mechanisms. The candidates first broadly partition into recurrent and feedforward models, depending on whether the dynamics that originate spatial tuning and velocity integration are within (recurrent) or upstream (feedforward) of the grid cell layer. Recurrent models further partition on the basis of two key features: topology (periodic or not) and locality of connectivity (from local to global).

Among recurrent models, the first candidate models are aperiodic networks (Figure 1a) (Burak and Fiete, 2009; Widloski and Fiete, 2014): Network connectivity has no periodicity (flat, hole-free topology) and it is purely local (with respect to an appropriate or ‘topographic’ rearrangement of neurons only nearby neurons connect to each other). Despite the aperiodic and local structure of the network, activity in the cortical sheet is periodically patterned (under the same topographic arrangement). In this model, co-active cells in different activity bumps in the cortical sheet are not connected, implying that periodic activity is not mirrored by any periodicity in connectivity. Interestingly, this aperiodic network can generate spatially periodic tuning in single cells because, as the animal runs, the population pattern can flow in a corresponding direction and as existing bumps flow off the sheet, new bumps form at the network edges, their locations dictated by inhibitory influences from active neurons in other bumps (Figure 1e). From a developmental perspective, associative learning rules can create an aperiodic network (Widloski and Fiete, 2014), but only with the addition of a second constraint: Either that associative learning is halted as soon as the periodic pattern emerges, so that strongly correlated neurons in different activity neurons do not end up coupled to each other, or that the lateral coupling in the network is physically local, so that grid cells in the same network cannot become strongly coupled through associative learning even if they are highly correlated, because they are physically separated. In the latter case, the network would have to be topographically organized, a strong prediction.

![Figure 1.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig1-v2.jpg)

**Figure 1.:** (a–d) Recurrent pattern-forming models. Gray bumps: population activity profiles. Blue: Profile of synaptic weights from a representative grid cell (green) to the rest of the network. Bottom of each panel: 2D network; Top: equivalent 1D toy network. Matching arrows along a pair of straight network edges signify that those edges are glued together. (a) Aperiodic network: (Burak and Fiete, 2009; Widloski and Fiete, 2014): local connectivity without periodic network boundaries. (b) Partially periodic network (Burak and Fiete, 2009): local connectivity in a network with periodic boundaries. (c) Bottom left and top: Fully periodic network (Guanella et al., 2007; Burak and Fiete, 2006; Fuhs and Touretzky, 2006; Pastoll et al., 2013; Brecht et al., 2014; Widloski and Fiete, 2014), with global connectivity and periodic boundaries. Bottom right: multi-bump network with local-looking connectivity but long-range connections between co-active cells in different bumps. This model is mathematically equivalent to a fully periodic model (see Figure 1—figure supplement 1). (d) A network with a single activity bump and without periodic boundaries cannot properly retain phase information as the bump moves around: it will not be a good integrator of animal velocity and is not a candidate mechanism. (e) Movement of the animal (left) causes a flow of the population pattern in proportion to animal velocity (four snapshots over time in center panels) for the models in (a–c). Red line: Electrode whose tip marks the location of a recorded cell. The recorded cell’s response is spatially periodic (right; spikes in black), like grid cells. (f) Feedforward model: A grid cell (green) receives and combines inputs that are spatially tuned with uniform resolution across open spaces (implying these inputs reflect path integration-baed location estimates). These inputs may arise from recurrent ring attractor networks (Mhatre et al., 2012; Blair et al., 2008) (top) and exhibit stripe-like spatial tuning either in their firing rates (Mhatre et al., 2012) (bottom left) or firing phase with respect to the theta-band LFP oscillation (Welday et al., 2011; Bush and Burgess, 2014) (not shown). Or, they could arise from place cells assumed to path integrate (Kropff and Treves, 2008; Dordek et al., 2016). Selective feedforward summation followed by a nonlinearity produces grid-like responses (bottom right).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) The population pattern period in an aperiodic network expands continuously with increasing inhibition strength ($\gamma_{i⁢n⁢h}$) over a range. The ordinate shows the stretch-factor $\alpha$, which quantifies the deviation of the period post-perturbation from that pre-perturbation, normalized by the pre-perturbation period (see Materials and methods). Altering the network’s connectivity to even slightly take into account the periodic activity pattern by adding weak connections between neurons in adjacent activity bumps (as in [b]) transforms the network into one that will not stretch at all (cyan curve). This network with coupled activity bumps, despite the weakness of the connectivity, is in principle mathematically analogous to the fully periodic network. Indeed, the population period in the network with cyan connectivity can no longer gradually vary with inhibition strength (cyan curve, (a)). Simulation details: The network connectivity is a hybrid of the aperiodic network in Burak and Fiete, 2009 with the fully periodic network of Fuhs and Touretzky, 2006 (note that, while the model of Fuhs and Touretzky, 2006 does not have explicit periodic boundary conditions, the multimodality of the synaptic weights couples adjacent activity bumps so that the network acts as a single-bump, fully periodic network). The dynamics are LNP-based (see Materials and methods) and driven with inputs simulating animal motion at constant speed (v = 0.3 m/s) for 10 s. There are only two populations (call them R and L), distinct in their directional preferences ($e^^{P}=$ (0,1), (0,–1) for the R and L populations, respectively) and output synaptic asymmetries (see below). The shifted output weight profiles are sinusoids with gaussian envelopes, the latter which constrain the non-locality of the projections. For a narrow gaussian envelope, the weights resemble the purely local, center-surround profiles of Burak and Fiete, 2009, whereas for wide gaussian envelopes, the weights resemble the non-local, multimodal projections of Fuhs and Touretzky, 2006. The weights going from population $P^{′}$ to $P$ and from cells i and j, are given by $W_{i⁢j}^{P⁢P^{′}}=\frac{η}{C}⁢exp⁡(\frac{-x^{2}}{2⁢\sigma^{2}})⁢(cos⁡(a⁢x)-1)$, where $x=i-j+Δ$ ($Δ=\pm1$ for $P^{′}=R⁢(+)$ and $P^{′}=L⁢(+)$), $η$ is a scaling factor that modulates the amplitude of the weights, $C=\sqrt{2⁢\pi⁢\sigma^{2}}⁢(exp⁡(\frac{-\sigma^{2}⁢a^{2}}{2})-1)$ is a normalization factor, $\sigma$ determines the width of the gaussian envelope, and $a$ determines the period of the underlying sinusoid. Parameters. $N_{R}=N_{L}=$ 200 neurons; CV = 0.5; $d⁢t=$0.5 ms; $\tau_{s⁢y⁢n}=$30 ms; $G^{0}=$ 50; $G^{0^{′}}=$ 0; $\beta^{v⁢e⁢l}=$ 1; $A_{i}^{P}=A_{i}^{P,aper}$; $a=2\pi/20$; $η$ = 200; $\sigma=$ 4$→$12.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Population activity in the cortical sheet (yellow-black blobs), with schematic of connectivity (green). Note that in the bulk of the sheet, connectivity is local and not determined by the periodic activity in the sheet. However, the imposition of periodic boundary conditions requires that some neurons connect with others on the far edge of the sheet. Even if neurons are not topographically organized, the connectivity requires that a planar cortical sheet is somehow intrinsically connected as a torus. Activity-dependent weight changes that are based on the expression of periodic activity patterns could produce a torus-like connectivity, but then if the sheet is not topographically ordered it is likely that neurons in various bumps will connect to each other, producing a fully periodic rather than partially periodic network.

Second are fully periodic networks (Figure 1c) (Guanella et al., 2007; Fuhs and Touretzky, 2006; Pastoll et al., 2013; Brecht et al., 2014). The network is topologically a torus with periodic boundary conditions between the pairs of opposite edges, and connectivity is global: There is no neural rearrangement under which network connectivity will be local. It is mathematically equivalent to view this network as having a single activity bump (Burak and Fiete, 2006; Guanella et al., 2007) or having multiple periodically arranged bumps with inter-bump connections (Burak and Fiete, 2009). In this network, periodic connectivity underlies periodic activity. Developmentally, a fully periodic network would naturally arise if associative plasticity continued post-pattern formation, so that the topology of activity and connectivity would come to mirror each other (Widloski and Fiete, 2014).

Third are partially periodic networks (Burak and Fiete, 2009) (Figure 1b) with periodic boundary conditions (torus topology) but only local connectivity on the torus after appropriate rearrangement of neurons. In this model, neural activity on the cortical sheet is multi-peaked and periodic (under appropriate rearrangement). Conceptually and developmentally, these networks are the strangest: None of the connectivity in the bulk of the network reflects the periodic nature of activity within it, except for the connectivity necessary to connect together neurons across the edges of an initially aperiodic sheet of cells. The wiring of this ‘edge’ subset of neurons must, unlike the rest of the cells, depend on details of the periodic activity pattern to make sure that opposite edge bumps are ‘aligned’ before joining (Figure 1—figure supplement 2). It is unclear how activity-dependent plasticity rules, which could wire together faraway edge neurons based on activity, would refrain from doing the same for the rest, to maintain otherwise local connectivity.

The fourth potential combination of topology and locality is not permitted: it is not possible to obtain grid-like activity from neurons with global connectivity (and single-bump activity) but aperiodic boundaries (topologically flat hole-free networks), Figure 1d.

Feedforward models of grid cell activity form a robust and growing set. In these models, grid cells merely sum and transform with a pointwise nonlinearity inputs that are already spatially tuned with roughly uniform coverage and resolution across the environment (Figure 1f) (Kropff and Treves, 2008; Welday et al., 2011; Mhatre et al., 2012; Bush and Burgess, 2014; Hasselmo and Brandon, 2012; Dordek et al., 2016; Stachenfeld et al., 2017); thus, it is implicitly assumed that the upstream inputs to grid cells have already performed path integration. These feedforward models, which we propose could be distinguished from recurrent models with the proposed perturbative approach, themselves segment into two major varieties. One type (Welday et al., 2011; Mhatre et al., 2012; Bush and Burgess, 2014; Hasselmo and Brandon, 2012) generates low-dimensional grid cell population activity across environments (e.g., in Welday et al., 2011, three upstream circuits, each a 1D continuous attractor network, integrate one component of animal velocity aligned to each of the three primary directions of a triangular lattice; the combined response is 2-dimensional, and preserved across environments; other models of this type differ in details but are similar in this regard), as predicted also by the recurrent models and found in the data (Yoon et al., 2013). In the second type (Kropff and Treves, 2008; Dordek et al., 2016; Stachenfeld et al., 2017), the grid cell pattern for an environment depends on the place cell pattern for that environment. Thus, when the place cell representations remap across environments, the model grid cells will not preserve their spatial relationships.

Our candidate models are the set of recurrent and feedforward models described and cited above. They are architecturally and mechanistically distinct in ways both large and subtle: they differ in whether grid cells or their upstream inputs are performing velocity-to-location integration, in whether spatial patterning originates wholly or only partly within grid cells, and in the structure of their recurrent circuitry. As already noted, some of the subtle-seeming structural differences have important implications for circuit development: different connectivity profiles and topologies require distinct models of plasticity and experience during circuit formation (Widloski and Fiete, 2014). Nevertheless, candidate recurrent and feedforward models that exhibit approximate 2D continuous attractor dynamics are difficult to distinguish on the basis of existing data.

As we discuss at the end, neither complete single neuron-resolution activity records nor complete single synapse-resolution weight matrices (connectomes) will fully suffice to distinguish between the candidate models because they are observational or correlative techniques: they do not probe the causal origin of the observed responses.

We show how it is nevertheless possible to gain surprisingly detailed information about the grid cell circuit from a feasible perturbation-based experimental strategy, enough to discriminate between the candidate models.

## Results

### A perturbation-based probe of circuit architecture

The question of mechanism is focused on a pre-specified set of neurons or local circuit: Is the observed low-dimensional grid cell activity primarily based on recurrent interactions within the set, and how, or is it inherited from feedforward drive originating outside this set? We refer to a perturbation as simple, low-dimensional and global in this context if it affects most cells within this set without regard to their individual functional identities, and does not affect those outside. In what follows, we consider the set to consist of all grid cells and conjunctive cells in one (or more) grid modules (Stensola et al., 2012), as well as the interneurons that surround them; toward the end we discuss the effects of perturbing subpopulations or bigger sets.

The central idea is as follows: Globally perturbing either the time-constant of neurons or the gain of recurrent inhibition is predicted to affect cell–cell spatial tuning relationships in candidate models in a specific way that can be robustly observed and characterized from ultra-sparse sampling of neurons in the network, and the predicted effects differ across candidate mechanisms.

To present the idea, we consider a thought experiment on the aperiodic recurrent network models. We will retake the larger perspective, of discriminating between the various model categories, immediately afterward. In aperiodic models, perturbing the gain of recurrent inhibition or the time-constant of neurons will induce a shift in the period of the internal population pattern (Figure 2—figure supplement 1). Let us quantify the change in period by the population period stretch factor, $\alpha=|\frac{\lambda_{p⁢o⁢p,p⁢o⁢s⁢t}}{\lambda_{p⁢o⁢p,p⁢r⁢e}}-1|$ (where $\lambda_{p⁢o⁢p,p⁢r⁢e}$ is the pre-perturbation population period). Without loss of generality, suppose that the focus of pattern expansion is at the left edge, Figure 2a (blue: original pattern, red: expanded pattern). Each neuron can be assigned a population phase with respect to the period of the population pattern: If the phase at the left edge is called 0 (again without loss of generality), neurons lying at integer multiples of the original period also originally had a phase of 0 (Figure 2b). However post-expansion, the population phase of a neuron originally one period away from the left edge is no longer zero (Figure 2a,b). Let us call the shift in the population phase of this neuron one ‘quantum’ (Figure 2b), and denote it by $Δ$. The quantum of shift must be $Δ=|1-\frac{\lambda_{p⁢o⁢p,p⁢r⁢e}}{\lambda_{p⁢o⁢p,p⁢o⁢s⁢t}}|=\frac{\alpha}{1+\alpha}$ ($≈\alpha$ for small perturbations). A neuron $K$ periods away will shift in phase by $K$ quanta, Figure 2b. If there are $M$ bumps in the population pattern, the largest shift will be $M$ quanta, or $M⁢Δ$ (modulo 1). If we construct a distribution of shifts in population phase pre- to post-expansion for cells across the network, the distribution will be quantal, with $2⁢M$ peaks (assuming the biggest phase shift, $M⁢Δ$, is less than $1/2$, because phase is a periodic variable that we parameterize as running between $-1/2$ to $1/2$; this condition can be met by keeping the perturbation small, such that $Δ<1/(2⁢M)$), Figure 2—figure supplement 2 and Figure 2c. In other words, for small perturbations, the number of peaks in this distribution is predicted to be twice the number of bumps in the original population pattern. We will call this distribution of relative phase shifts the DRPS.

![Figure 2.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig2-v2.jpg)

**Figure 2.:** (a) Schematic of population activity before (blue) and after (red) a 10% period expansion ($\alpha=0.1$; the center of expansion is shown at left, but results are independent of this choice) in an aperiodic network. Circle, square, triangle: three sample cells with the same pre-expansion population phase. (b) The population phase $ϕ_{p⁢o⁢p}^{i}$ of the $i$th neuron is defined as $ϕ_{p⁢o⁢p}^{i}=((i-1)/\lambda_{p⁢o⁢p})mod1$ where $\lambda_{p⁢o⁢p}$ is the population pattern period. Plotted: population phase magnitudes pre- (blue) and post- (red) expansion (phase magnitude is given by the Lee distance, $|ϕ|=min⁡(||ϕ||,1-||ϕ||)$, where $||⋅||$ denotes absolute value). (c) Histogram of quantal shifts in the pre-to post-expansion population phases for all (n = 100) cells in the network. Gray line: raw histogram (200 bins). Black line: smoothed histogram (convolution with 2-bin Gaussian). Negative (positive) phase shifts arise from gray-shaded (horizontally-striped) areas in (b). (d–e) Quantal shifts in the population phase (experimentally inaccessible) are mirrored in shifts in the pairwise relative phase of spatial tuning between cells (experimentally observable). (d) Schematic of spatial tuning curves of three cells (circle, square, triangle) from (a). Pre-expansion the tuning curves have the same phase (top), thus their relative spatial tuning phases are zero. The tuning curves become offset post-expansion (bottom), because the shift in the population pattern forces them to stop being coactive. (e) Distribution of relative phase shifts (DRPS; gray). Relative phase between cells $i,j$ ($d^{i⁢j}$ is the offset of the central peak in the cross-correlation of their spatial tuning curves; $\lambda$ is their shared spatial tuning period). A relative phase shift is the difference in relative phase between a pair of cells pre- to post-perturbation. Black: smoothed version. There are (100 choose 2)=4950 pairwise relative phase samples. (f) Population activity pattern and pattern phase pre- and post-expansion in a 2D grid network (as in (a–b)). Dotted lines: principal axes of the population pattern (left). An arrow marks each cell’s population phase (right). (g) DRPS for the two components of 2D relative phase (as in (e); see Materials and methods). Samples: (3200 choose 2).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Change in population pattern period as the the time-constant (a) and inhibition strength (b) are increased in a 1D aperiodic network (see Materials and methods). In all trials (black circles), the network is driven by a constant velocity input (v = 0.3 m/s) for 10 s. Red line: average (n = 50 for each parameter value). In (c), same as in (a), except that velocity input into each neuron is additive instead of multiplicative (see Materials and methods).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Top: Schematic of the phase in a population pattern, pre- (blue) and post- (red) perturbation, for a large 1D network with many bumps with population period stretch factor $\alpha$=0.1, with phase shift quanta indicated by black vertical bars for cells lying at integer multiples of the pre-perturbation wavelength. Bottom: Black curve: Difference in the pre- and post-perturbation phases of cells. At left, the DRPS is aligned vertically with the y-axis of the phase shift plot, so that the origin of the DRPS peaks is more readily apparent. For the neuron lying one wavelength away from the center of expansion, we define its phase shift as one ‘quantum’, $Δ$. $Δ$ is related to the stretch factor via $Δ=\frac{\alpha}{1+\alpha}$. The peak locations in the DRPS at bottom left correspond roughly to all half integer multiples of $Δ$. After moving five bumps away from the center of expansion, the phase shift has reached its maximum at 0.5. At this point, there can be no additional (farther out) quantal peaks in the DRPS, meaning that only patterns of up $M^=5$ bumps can be discriminated. Thus, the number of DRPS peaks equals twice the number of bumps, $M$, in the pattern only when $M⁢Δ<M^⁢Δ=0.5$; when $M>M^$, the number of peaks in the DRPS will systematically underestimate the number of bumps in the pattern.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (a) 1D population activity, pre- (blue) and post-perturbation, for a $%16$ increase the wavelength of the pattern ($\alpha=0.16;\lambda_{p⁢o⁢p,p⁢r⁢e}=250$ neurons), with pattern expansion is centered at the left network edge. Circle, square, and triangle: locations of cells that are separated by integer numbers of wavelengths. (b) Population phase, pre- (blue) and post- (red) perturbation (see Materials and methods subsection ‘Alternative formulation of the DRPS’ for definitions and transformations in this context). (c) Post-perturbation phase vs. pre-perturbation phase, with projection of data onto orthogonal axis shown at upper right (see Materials and methods). (d) Distribution of shifts in population phase (n = 1000) (see Materials and methods). (e–f) Shift distributions for population phase (experimentally inaccessible) carry over to shift distributions for spatial tuning phase (experimentally observable). (e) The circle, square, and triangle cells, which original have identical spatial tuning (blue curves), now exhibit shifted spatial tuning curves (red curves). The shift in spatial phase for a pair is proportional to the number of activity bumps between them in the original population activity pattern. (f) Distribution of relative phase shifts (DRPS) ($n=$ (1000 choose 2) relative phase samples because relative phase is computed pairwise) (see Materials and methods).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Results from a 1D aperiodic recurrent network grid cell model with CHH neurons. In all simulations, the network is driven by a constant velocity of 0.3 m/s and the run is a 10 s trajectory. (a–d) The change in population period as parameters are varied to simulate thermal and neuromodulatory effects (see Materials and methods). (a) Population period increases gradually with the strength of inhibition. Each point is the population period averaged over 10 trials (error bars reflect the SEM). (b) Effect of temperature on period through ionic conductances: Only the ionic parameters (and not the synaptic parameters) are varied according to their $Q_{10}$ factors (see Materials and methods). The population period shrinks with decreasing temperature. (c) Effect of temperature on period through synaptic parameters: Temperature perturbation of only the synaptic parameters (and not the ionic parameters) causes the population period to expand with decreasing temperature. (d) Total effect of temperature on period through all ionic and synaptic parameters: All synaptic and ionic parameters are varied according to their $Q_{10}$ factors (see Materials and methods) as temperature is stepped down from $36^{∘}$C to $26^{∘}$C. The combined effect is an increase in population period with decreasing temperature. Thus, we may predict that the effect of cooling the experimental system should be an expansion of the population period. We conclude from (b–d) that synaptic parameter changes trump the opposing effects of ionic versus synaptic temperature-dependent changes on population period. We also conclude that, because synaptic effects dominate over cellular effects, we may reasonably mimic the effects of temperature in network simulations with simpler neurons by using the synaptic model of the CHH simulations together with the prescribed temperature-dependent modification of synaptic parameters, while neglecting how temperature might affect neural parameters and equations (e) Dissecting synaptic temperature effects: Temperature modulation of only the synaptic time constant, leaving synaptic conductances unchanged. (f) Dissecting synaptic temperature effects: Temperature modulation of only the synaptic conductances, leaving the synaptic time constants unchanged (solid line). The effect on period of conductance modulation is weaker than the effect of time constant modulation. (This difference can be traced to the larger $Q_{10}$ modulation of the time-constant: If the $Q_{10}$ factor for synaptic conductances is set to be that of the time constant (dotted line), the effects on population period become comparable; compare with (e)). Summarizing (b–f), ionic and synaptic temperature modulations have opposing effects on period, but synaptic effects dominate leading to an increase in period with decreasing period. Within synaptic parameters, time constant effects on period dominate over conductance effects. Thus, in simpler neuron models of grid cells, the effect of temperature can be roughly approximated by scaling $\tau_{s⁢y⁢n}$ without a rescaling of the other parameters. (g–j) How temperature changes single-cell and synaptic properties in CHH models when all synaptic and ionic parameters are changed according to their respective $Q_{10}$ factors. (g) Firing rate as a function of input current, (h) action potential shape, and (i) impulse response (i.e., subthreshold response of membrane potential to current pulse), with log-log plot in inset. (j) The net EPSP shape as a function of temperature. There is a slight decrease in the overall amplitude of the EPSP with temperature (as shown by the log-log plot of the same data in the inset), but this change is small compared to the effect on the EPSP time constant, consistent with (e–f).

Practically, however, the grid cell network might not be topographically well-ordered on a sufficiently fine scale (Heys et al., 2014), and one cannot simply image the population response and expect to read off pattern phases for each cell as in Figure 2a,b.

Fortunately, the distribution of shifts in the difficult-to-observe population phases of cells, based on instantaneous and topographically ordered population activity snapshots, is mirrored in the distribution of shifts in the relative phase of the straightforward-to-observe and time-averaged spatial tuning curves of cells (Figure 2d). Consider a pair of cells one population period apart pre-perturbation, so they have the same population phase (circle, square or square, triangle in Figure 2a). These cells are co-active and have the same spatial tuning curves, and thus a relative spatial tuning phase of 0 (circle, square or square, triangle in Figure 2d, top). Post-perturbation, their spatial tuning curves will be shifted relative to each other by the same amount as the shift in their individual population phases (circle, square or square, triangle in Figure 2d, bottom). In other words, cells one bump apart in the original population pattern will exhibit one quantum of shift in their relative spatial tuning. The relative phase of spatial tuning for a pair originally separated by $K$ periods will shift by $K$ quanta post-perturbation (e.g., circle, triangle in Figure 2d, bottom: spatial tuning curves shift by two quanta in phase because these cells were two periods apart in the original population pattern).

This series of theoretical observations leads us to construct a predicted distribution of relative phase shifts (DRPS) from all pairs of neurons, Figure 2e. The DRPS is quantal and has the same number of peaks as the distribution of shifts in population phase (Figure 2c). Indeed, multiplying the number of peaks in the multimodal DRPS by $1/2$ gives the number of bumps in the original population pattern, if the quantal shift size is sufficiently small. The DRPS is a property of patterning in an abstract space, independent of how neurons are actually arranged in the cortical sheet. It can be obtained from the spatial tuning curves of cells recorded simultaneously through either conventional electrophysiology or imaging. As we show later, a robust estimate of the full DRPS can be obtained from only a handful of cells.

In 2D, relative phase is a vector. The two components are each computed simply as in 1D, along each of the two principal axes of the spatial tuning grid. For an aperiodic network, for small enough perturbations, the total number of bumps in the population pattern can be inferred to be a quarter of the product of the number of peaks in the two relative phase shift distributions from the two components of the relative phase (Figure 2f–h).

### Experimental knobs to modulate the population pattern

To generate the DRPS in experiment and use it to distinguish between grid cell models requires an experimental knob that can be turned to change the period of the population activity pattern. Temperature is one potential knob: Cooling a biological system reduces reaction rates and increases time-constants through the Arrhenius effect (Katz and Miledi, 1965; Thompson et al., 1985; Moser and Andersen, 1994; Long and Fee, 2008). However, existing models of grid cells are based on simplified rate-based or linear-nonlinear Poisson (LNP) spiking units, and it is unclear which parameters to modify to correctly predict the effects of cooling the neural circuit: Varying a ‘neural’ time-constant parameter in a recurrent network of simple units may or may not change the population pattern period, depending on whether PSP height is scaled together with the time-constant change (Widloski and Fiete, 2014; Beed et al., 2013) or not. To better predict the effects of cooling on grid cell period, we constructed more detailed grid cell models using cortical Hodgkin-Huxley model neurons (Pospischil et al., 2008) whose parameters accommodate thermal effects (Hodgkin et al., 1952; Katz and Miledi, 1965).

The population period in aperiodic grid cell models built from Hodgkin-Huxley neurons is pulled in opposing directions by temperature modulations in ion-channel biophysics and synaptic signalling (Figure 2—figure supplement 4). However, the dominant influence on network response comes from the growth in the PSP time-constant with cooling and results in an overall expansion of the population period (Figure 2—figure supplement 4).

This result allows us to conclude that the net effect of cooling the biological circuit should be an expansion in the period, if the circuit is recurrently connected and aperiodic. It also allows us to continue using simple rate-based and LNP spiking models because we can now interpret how to scale parameters as a function of temperature: It is most appropriate to scale the time-constant inversely with temperature, while essentially keeping the PSP height fixed (Figure 2—figure supplement 4).

The strength of recurrent inhibition is another experimental knob. Unlike temperature, manipulating the gain of inhibitory synaptic conductances has a relatively unambiguous interpretation in grid cell models. Experimentally, the strength of inhibition might be modulated by locally infusing allosteric modulators that increase inhibitory channel conductances (e.g. benzodiazipines; Rudolph and Möhler, 2004 and personal communication with C. Barry). In both cortical Hodgkin-Huxley based models grid cell models (Figure 2—figure supplement 4) and rate-based models, a gain change in inhibitory conductances predicts a change in the period of the population pattern (Figure 2—figure supplement 4 and Moser et al., 2014, Widloski and Fiete, 2014).

To summarize, thermal perturbation (cortical cooling) and biochemical perturbation (drug infusions to alter the gain of recurrent inhibition) are two experimental manipulations that could, according to the models, alter the period of a recurrently formed population pattern and thus may act as appropriate knobs to enable the construction of the DRPS.

### Discriminating among recurrent architectures

In dynamical simulations of the various plausible candidates (Materials and methods), the same global perturbations have different effects, resulting in distinct predicted DRPS’s. To generate maximally robust and easy-to-interpret predictions, we focus on how the candidate models differ with respect to one simple property of the DRPS: the overall width of its envelope.

In aperiodic networks (Figure 1a) with smooth boundaries for accurate integration (Burak and Fiete, 2009), an incremental increase in the strength of global perturbation results in incremental expansion of the population activity pattern (Figure 3a, red, and Figure 2—figure supplement 1) (see Widloski, 2015 for an analysis of boundary conditions and permitted number of peaks). Thus, the peaks in the DRPS will incrementally spread out, producing a DRPS envelope that gradually and smoothly widens with perturbation strength (Figure 3b–c, red). In addition, because the change in period is incremental when the perturbation strength is gradually increased, it may be possible to estimate the number of bumps in the population pattern by counting peaks in the DRPS.

![Figure 3.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig3-v2.jpg)

**Figure 3.:** (a) Simulations of aperiodic (column 1), partially periodic (column 2), and fully periodic (column 3) networks show changes in the population pattern pre-perturbation (first row; $\gamma_{i⁢n⁢h}=1$) to post-perturbation (second row; $\gamma_{i⁢n⁢h}=1.33$). Solid vertical lines: pre-perturbation bump locations. (Simulation details in Materials and methods.) (b) Perturbation-induced DRPS in the various networks for two perturbation strengths ($\gamma_{i⁢n⁢h}=1.33$: solid line and filled gray area; $\gamma_{i⁢n⁢h}=1.66$: dotted line), both relative to the unperturbed case. (c) DRPS width ($\sigma_{D⁢R⁢P⁢S}$, defined as the standard deviation of the DRPS) as a function of perturbation strength for the different networks. Dashed green line: feedforward networks (predicted, not from simulation). The step-like shape for the partially periodic network is generic; however, the point at which the step occurs may vary from trial to trial. (d–e) Change in spatial tuning period (d) and amplitude (e) as a function of the perturbation strength (see Materials and methods). Change is defined as $|\frac{X_{p⁢o⁢s⁢t}}{X_{p⁢r⁢e}}-1|$, where $X$ is the spatial tuning period or amplitude.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Change in spatial tuning period (a), population pattern period (b), and the velocity response (c) for the different network architectures (see Materials and methods for definitions of measures). Change is defined for quantity $X$ as $|X_{p⁢o⁢s⁢t}/X_{p⁢r⁢e}-1|$, where $X_{p⁢r⁢e}$ refers to that quantity measured in the unperturbed ($\gamma_{i⁢n⁢h}=1$) case, and $X_{p⁢o⁢s⁢t}$ refers to that quantity as measured in the perturbed ($\gamma_{i⁢n⁢h}$=1.33, 1.66, 2) cases. It is clear that the spatial tuning period (a) is more strongly influenced by the velocity response (c) than by the population period (b).

Partially periodic networks (Figure 1c), unlike aperiodic networks, must because of their symmetry accommodate an integer number of complete activity bumps in a way that is perfectly periodic (Widloski, 2015). The bumps and spacings within a partially periodic network are identical and the population pattern (if the geometry of the 2D pattern is fixed) is characterized simply by the number of bumps, which is constrained to be an integer. Incrementally increasing the perturbation strength is thus predicted to first result in no change, followed by a sudden change when the network can accommodate an entire additional bump, Figure 3a (purple) (or an additional row of bumps in 2D, assuming the pattern does not rotate as a result of the perturbation; see Discussion). As soon as a new bump has been inserted into the population pattern, the phase shifts will be large even for cells in adjacent bumps, and the DRPS will be wide. To summarize, for partially periodic networks, incremental changes in perturbation strength are therefore predicted to result in a stepwise (stepping to maximal width) change in the DRPS (Figure 3b–d, purple).

Counting peaks to estimate the number of bumps in the underlying population pattern after a stepwise change in the DRPS will likely result in substantial underestimation: because the phases shift by a large step when a change occurs, if a shift of $M$ quanta already exceeds one cycle, the DRPS will not distinguish between an $M$-bump and a $K$-bump network ($K>M$; Figure 2—figure supplement 2 and e.g., Figure 3b: compare peaks in the solid and dashed lines for small and large perturbations, respectively).

Finally, in the fully periodic network (Figure 1b) the globally periodic connectivity completely determines the population period of the pattern, and changes in the neural time-constants or network inhibition strength do not alter it (Figure 3a, blue). Thus, the same global perturbations that effected changes in the population period in the other recurrent models (Figure 3a, red and purple) have no effect in the fully periodic network. The DRPS is consequently predicted to remain narrow, unimodal, and peaked at zero (Figure 3b–c, blue).

### Discriminating feedforward from recurrent architectures

If low-dimensional dynamics and spatially tuned responses first originate upstream of the perturbed set, then the perturbations will leave unchanged the spatial tuning phases of grid cells, preserving grid cell–grid cell relationships. This prediction holds even if grid cells play a role in constructing their particular patterns of spatial tuning, for instance by combining elements that are already spatially tuned as when stripe-tuned inputs are combined to generate 2D lattice responses (Mhatre et al., 2012; Welday et al., 2011; Bush and Burgess, 2014) (Figure 1f). Thus, for feedforward models, as for fully periodic (recurrent) networks, the DRPS is predicted to remain narrowly peaked at zero across a range of perturbation strengths (Figure 3c, dashed green line).

Further, perturbing grid cells but not their spatially patterned feedforward inputs will not affect their spatial tuning. By contrast, in all recurrent models (Figure 1a–c), perturbing the grid cell network induces a change in the efficacy with which feedforward velocity inputs drive the population phase over time, thus the spatial tuning period of cells is predicted to change even if the population period does not (as in fully periodic networks – see Figure 3—figure supplement 1), Figure 3d. This expansion in spatial tuning period with global perturbation strength is predicted to hold for all three recurrent network classes, and distinguishes fully periodic recurrent networks from feedforward ones.

Finally, in both feedforward and recurrent neural network models, the amplitude of the grid cell response will change in response to perturbation (Figure 3e). This universal prediction of amplitude change with perturbation can be used as an assay of whether the attempted global perturbation is in effect.

### Data limitations and robustness

We consider two key data limitations. First, it is not yet experimentally feasible to record from all or even a large fraction of cells in a grid module. Interestingly, the proposed method is tolerant to extreme sub-sampling of the population: a tiny random fraction grid cells from the population (10 out of e.g. 1600 cells, or 0.6%) can capture the essential structure of the full DRPS, Figure 4a, including its overall width and the detailed locations of its multiple peaks. This robustness to subsampling is dramatically better than in statistical inference methods, where even ‘sparse’ methods can require $∼2$ orders of magnitude denser data (Soudry et al., 2015).

![Figure 4.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig4-v2.jpg)

**Figure 4.:** (a) Left: The quantal structure of the DRPS (along first principal axis of the 2D phase) is apparent even in small samples of the population (black: full population; red: n = 10 cells out of 1600; stretch factor $\alpha=0.1$). Right: The L2-norm difference between the full and sampled DRPS as a function of number of sampled cells. Inset: log-log scale. (b) First and second rows: DRPS for population patterns with different numbers of bumps (gray line: raw; black line: smoothed with 2-bin Gaussian). Column 1: zero error or noise in estimating relative phase. Column 2: same DRPS’ as in column 1, but with phase estimation errors (i.i.d. additive Gaussian noise with zero mean and standard deviation 0.02 for each component of the relative phase vector, $\delta→^{i⁢j}$). Column 3: Increasing the stretch factor ($\alpha=0.2$) renders the peaks in the DRPS more discernible at a fixed level of phase noise. For the 5-bump pattern (second row), $M⁢Δ≈M⁢\alpha=5\times0.2>1/2$ and thus the number of peaks in the DRPS times 1/2 at this larger stretch factor will underestimate the number of bumps in the underlying population pattern. (c) In grid cell recordings (data from Hafting et al., 2005), the uncertainty in measuring relative phase, as estimated by bootstrap sampling from the full dataset (see Materials and methods), declines with the length of the data record according to $T^{-\frac{1}{2}}$ (dotted line). Parameters: $\lambda_{p⁢o⁢p,p⁢r⁢e}=40/3≈13.3$ neurons (a) =20 neurons (b, top row),=8 neurons (b, bottom row); $\alpha$ = 0.1; $e^_{1}=[1,0]$; network size: $40\times40$ neurons.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) Copied from Figure 4b. First and second columns: DRPS (200 bins; gray line: raw; black line: smoothed with 2-bin Gaussian) for different numbers of population pattern bumps along the first principal axis of the pattern and for different amounts of phase noise (noise is sampled i.i.d. from a gaussian distribution, $𝒩⁢(0,\sigma_{p⁢h⁢a⁢s⁢e}^{2})$, and added to each component of the relative phase vector, $\delta→^{i⁢j}$; ‘phase noise’ is the same as $\sigma_{p⁢h⁢a⁢s⁢e}$). Third column: Same as the second column, except for a larger stretch factor, $\alpha=0.2$. Note that the peak separation has increased so that the individual peaks are discernible. However, for the five bump network in the second row, inferring the number of bumps in the underlying population pattern would lead to an underestimate, since $M⁢Δ≈M⁢\alpha=5\times0.2>1/2$. (b) Solid lines: Periodicity score (a measure of how well separated and equidistant are the peaks in the DRPS, and ranges between 0 and 1; see Materials and methods) as a function of phase noise for 2-bump network in (a), for different values of the stretch factor, $\alpha$ (solid lines). Periodicity is measured for the DRPS along the first principal axis. Dashed lines: Same as solid lines, except computed by randomly shuffling the phase vectors post-perturbation. (c) Stretch factor, $\alpha$, as a function of threshold phase noise (defined as the phase noise where the DRPS is indistinguishable from the DRPS when the phase vectors in the post-perturbation condition are reassigned randomly, i.e., the value of the phase noise when the colored curves in (b) cross the respective colored dashed lines).

The second limitation arises from the limited accuracy with which spatial tuning and relative phase can be estimated from finite data. In tests that depend only on the width of the DRPS (e.g. Figure 3), this phase uncertainty is not a serious limitation.

Resolving the relative phase accurately becomes important when counting DRPS peaks to estimate how many bumps are in the underlying population pattern of a recurrent network. The spacing between DRPS peaks determines the required tolerance in relative phase (Figure 4—figure supplement 1). DRPS peak spacing (in the aperiodic network) increases with the stretch factor at small stretch factors (Figure 4b and Figure 4—figure supplement 1), but the stretch factor must still obey $\alpha≈Δ<1/(2⁢M)$ (where $M$ equals the larger of the number of bumps along the two dimensions of the population pattern; Figure 4b) to avoid underestimating the number of bumps in the population pattern.

Fortunately, it is possible to gain progressively better estimates of relative phase over time even if there is substantial drift in the spatial responses of cells, because relative phases remain stable in a fixed network (Yoon et al., 2013) (here ‘fixed’ means that a given perturbation strength is stably maintained). Many estimates of relative phase may be made from short pieces of the trajectory, and these estimates averaged together (similar to the methods used in Yoon et al., 2013 and Bonnevie et al., 2013).

To distinguish $M=5$ bumps per dimension based on structure within the DRPS requires a stretch factor $\alpha≈Δ<1/(2⁢M)=0.1$, and a phase noise of 0.02 or smaller (Figure 4—figure supplement 1), which would require an approximately 8 min recording (estimated from grid cell and trajectory data, http://www.ntnu.edu/kavli/research.grid-cell-data), Figure 4c. Distinguishing seven bumps would require $\alpha\leq0.07$, phase noise less than $0.01$, and a 35 min recording.

In summary, the proposed method has high tolerance to subsampling and more limited tolerance to phase uncertainty, which can be reduced by averaging estimates over time.

### A decision tree for experimental design

We lay out a decision tree with an experimental workflow for discriminating between disparate feedforward and recurrent grid cell mechanisms, all of which exhibit approximate 2D continuous attractor dynamics at the population level (Figure 5).

![Figure 5.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig5-v2.jpg)

**Figure 5.:** The ‘specific’ approach involves a specific perturbation to either the gain of inhibition or the neural time-constants. Under the assumption of this kind of perturbation, the period, the amplitude, and the relative phases of the spatial tuning curves of neurons are measured pre-perturbation and then for each of three increasingly strong perturbations. A change in spatial tuning amplitude means that the attempted perturbation is in effect. Recurrent mechanisms can be discriminated from feedforward ones based on whether the perturbation changes the spatial tuning period (first open triangle). Different recurrent networks can be discriminated from each other based on the change in DRPS width or peak separation with perturbation strength (second open triangle). Finally, the number of bumps in the multi-bump population patterns can be inferred by counting the peaks in the DRPS (third open triangle), but for the partially periodic network only a lower bound on the number of bumps can be established (dotted line). Inset: ‘Nonspecific’ approach: After a perturbation of any type, the relative phases are measured. If the DRPS exhibits multiple peaks, then the underlying population pattern is multi-bump; otherwise, the test is inconclusive.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a) Population period as a function of a fractional perturbation of the network for aperiodic (top row), partially periodic (middle row), and fully periodic (bottom row) networks. Black circles indicate individual trials (n = 50, for each perturbation value) in which some fixed fraction of the network is randomly selected for perturbation (unperturbed neurons: $\tau_{s⁢y⁢n}=30⁢m⁢s$; perturbed neurons: $\tau_{s⁢y⁢n}=90⁢m⁢s$). For each trial, the network is driven with inputs simulating animal motion at constant speed (v = 0.3 m/s) for 10 s (see Materials and methods for definition of population period). Red line is the mean. Right: Histogram of population periods shown at left. (b–c) Same as in (a), except that the perturbation is applied to the E population (b) and I population (c) separately.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (a) Left: Population period as a function of a global perturbation of the synaptic time constants ($\tau_{s⁢y⁢n}=\beta⁢\tau_{s⁢y⁢n}^{*}$, where $\tau_{s⁢y⁢n}^{*}=30$ ms and $\beta$ is the perturbation parameter scale factor), for aperiodic (top row), partially periodic (middle row), and fully periodic (bottom row) networks. Black circles indicate individual trials ($n=50$, for each perturbation value) in which the network is driven with inputs simulating animal motion at constant speed ($v=0.3$ m/s) for 10 s (see Materials and methods for definition of population period). Red line is the mean. Right: Histogram of population periods shown at left. (b–c) Same as in (a), except that the perturbation is applied to the E population (b) and I population (c) separately.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (a) Left: Population period as a function of a global perturbation of the firing rates (the perturbation scale factor $\beta$ is applied multiplicatively to both $G^{0}$ and $G^{0^{′}}$, see Materials and methods), for aperiodic (top row), partially periodic (middle row), and fully periodic (bottom row) networks. Black circles indicate individual trials (n = 50, for each perturbation value) in which the network is driven with inputs simulating animal motion at constant speed (v = 0.3 m/s) for 10 s (see Materials and methods for definition of population period). Red line is the mean. Right: Histogram of population periods shown at left. (b–c) Same as in (a), except that the firing rate perturbation is applied to the E (b) and I (c) populations separately.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (a) Left: Snapshot of the I (black), E$^{R}$ (red), and E$^{L}$ (blue) population activities, for the case when EE connections are added (i.e., E$^{L}$-E$^{L}$, E$^{R}$-E$^{R}$, E$^{L}$-E$^{R}$, E$^{R}$-E$^{L}$ - see Materials and methods for details; network very similar to that shown in the SI of Widloski and Fiete, 2014) and weights adjusted so that there is patterning in the E populations but not in the I population. Right: Sample single neuron spatial responses of cells in the I (black) and E$^{R}$ (red) populations (dotted vertical line in left panel indicates relative locations of cells in the population), in the case in which the network is driven with inputs simulating a 10 s sinusoidal, back-and-forth motion of the animal across the environment. (b) Left: Population period as a function of a global perturbation of the synaptic time constants ($\tau_{s⁢y⁢n}=\beta⁢\tau_{s⁢y⁢n}^{*}$, where $\tau_{s⁢y⁢n}^{*}=30$ ms and $\beta$ is the perturbation parameter scale factor), for aperiodic (top row), partially periodic (middle row), and fully periodic (bottom row) networks with additional EE connections. Black circles indicate individual trials ($n=50$, for each perturbation value) in which the network is driven with inputs simulating animal motion at constant speed ($v=0.3$ m/s) for 10 s (see Materials and methods for definition of population period). Red line is the mean. Right: Histogram of population periods shown at left. Because of the recurrent excitation in the network, perturbations can lead to very large firing rates. Therefore, we include a cap on the maximum allowable mean firing rates, which is the reason for the limited range of perturbation values in (b) and (c) for which there is data, as compared to Figure 5—figure supplement 2. (c–d) Same as in (b), except that the perturbation is applied to the E population (b) and I population (c) separately. Results: If the time-constants of all cells in this model are perturbed, the predicted effects in (b) are qualitatively the same as in Figure 5—figure supplement 2. If only E cells are affected by the perturbation, the qualitative effect in (c) is also the same as in Figure 5—figure supplement 2. If only I cells are affected, this model predicts a weak change in the opposite direction with respect to the period of the pattern relative to Figure 5—figure supplement 2: increasing perturbation in the I population leads to a decrease in the period. However, the DRPS will change in qualitatively the same way because it depends on the magnitude of change, not the sign.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/33503/elife-33503-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** (a) Top row: Firing field of a single place cell (cell 67) learned in two familiar environments (first and second column) based on associating this field with the co-active grid cells (see Materials and methods for details; simulation based on Sreenivasan and Fiete, 2011), and the (untrained) response of this cell in a novel environment (last column). The solid vertical lines in the two familiar environments indicate the cell’s place preference. The dashed horizontal lines indicate the spiking threshold. Bottom rows: Strength of spatial inputs from grid cells of different modules (different rows) onto a single place cell (cell 67). Each colored line represents a different grid cell’s activation, multiplied by the synaptic weight from that grid cell onto place cell 67. The periodicity of the $i$th module is $0.2⁢(\sqrt{2})^{i-1}$ (fractions of the unit-sized enclosure). In the two familiar environments, the grid cell inputs are selected by plasticity to align such that the firing field of the place cell is unimodal and above threshold at the chosen locations; in the novel environment, starting from a random arrangement of grid phases, the place cell drive does not exceed the firing threshold. Thus, it cannot reset grid cell phases to take on values from the familiar environments. (b) Sub-threshold and super-threshold (spiking) fields of entire population of place cells. Top row: Same as top row in (a), except for an entire population of place cell with learned fields, ordered according to learned location preference (in the novel environment, cells are ordered as in familiar environment 1). Bottom row: Superthreshold responses generated from the subthreshold fields in the top row by applying the spiking threshold (dashed horizontal line in (a)).

We start with the ‘specific’ approach, which, according to our model, has more discriminatory power than the ‘nonspecific approach’ described later. The experimental demands of this approach are to be able to stably induce a global perturbation in at least one grid module, and to do so at 2–3 different strengths. Critically, the perturbation must be one of the two specific types discussed above: a perturbation of the strength (gain) of inhibition in the network, or of the network time constants. The data to be collected are simultaneous recordings from several grid cells as the animal explores novel enclosures with no proximal spatial cues, over a $\geq20$ minute trajectory.

First, before applying a perturbation, characterize spatial tuning (periods) and cell–cell relationships (relative spatial phases). Next, apply a series of 2–3 global perturbations of increasing strength. At each perturbation strength, characterize the spatial tuning of cells and cell-cell relationships.

A change in the amplitude of the grid cells’ response across the different perturbations should signal that the perturbation is having an effect, regardless of underlying mechanism (Figure 5, first triangle on left).

If the different perturbation strengths do not cause a change in the spatial tuning periods of single cells (but the response amplitudes do change), it follows that velocity integration and spatial patterning are originating elsewhere, consistent with some feedforward mechanism (Figure 5, green). To confirm, verify that cell–cell relationships remain unchanged across perturbations, as also predicted for feedforward networks.

If there is a change in the spatial tuning period, characterize the cell–cell relationships in each perturbation condition. Plot the DRPS from each perturbed condition relative to the pre-perturbation condition, and quantify its width and if possible the separation between its peaks. If the DRPS width or peak separation increases steadily and smoothly with perturbation strength, that implies an aperiodic recurrent architecture (Figure 5, red). If the DRPS peak separation or width exhibits a step-like change, it is consistent with a partially periodic recurrent network (Figure 5, purple). Together with a change in the spatial tuning period, a DRPS that remains narrowly peaked at zero, with no change in width with perturbation strength, is consistent with a fully periodic network (Figure 5, blue).

Finally, if the network is either an aperiodic or partially periodic recurrent network, the number of peaks in the DRPS for each relative phase dimension is a lower bound on the quantity $2⁢M$, where $M$ is the number of bumps in the population pattern along that dimension. If the stretch factor $\alpha$ times the number of bumps is smaller than 1/2 and the DRPS is multiply peaked the number of DRPS peaks should equal twice the number of population activity bumps along the corresponding dimension (Figure 5, final triangle and gray oval).

The ‘specific’ approach above should provide insight into the underlying dynamics of the system with respect to the candidate models, regardless of outcome. By contrast, a ‘nonspecific’ approach (Figure 5, dashed box) could do the same, but only for certain outcomes. Suppose that after a number of any type of perturbations to the system, with known or unknown underlying mechanisms and at a local or systemic scale, one measures the DRPS. If the DRPS does not exhibit multiple peaks then, because this outcome is consistent with many possibilities and the nature of the perturbation is not precisely known or controlled to change the inhibitory gain or neural time-constant (the specific perturbations that provide higher discriminatory power), one cannot conclude anything about circuit architecture. On the other hand, if the DRPS after nonspecific perturbation does exhibit multiple, equi-spaced peaks, one can conclude with high confidence that the brain generates an underlying multi-bump population pattern through recurrent mechanisms with partially periodic or aperiodic structure. This is because a multi-peaked DRPS is a highly specific outcome of recurrent pattern-formation dynamics.

### Questions about experimental contingencies

## Discussion

It is interesting to compare the potential of the present approach for discovering mechanism with other approaches. A high-quality, full-circuit connectome (Seung, 2009; Briggman et al., 2011) can specify the topology and locality of the network architecture. In other words, with appropriate analysis of the obtained data it should be possible to learn whether the connectivity matrix is ‘local’ (Widloski and Fiete, 2014) (Figure 1a), partially periodic (Figure 1b), or fully periodic (Figure 1c).

Network topology is, however, but one ingredient in circuit mechanism: Determining whether the observed connectivity actually accounts for the activity still requires inference (for instance, given a set of connections and weights, it is unknown whether they are strong enough to drive pattern formation in neural activity; determining this involves writing down a model of neural dynamics with the observed coupling). Even with further inference steps, whether the network originates certain functions like velocity-to-position integration and spatial tuning de novo (as in Figure 1a–c) or only amplifies or alters spatial tuning inherited from elsewhere (as in Figure 1f) cannot be answered by connectomics data. Despite their functional differences, feedforward and recurrent network models may exhibit similar lateral connectivity between grid cells. By contrast, the perturbative approach outlined here has the potential to reveal whether the function of path integration and spatial tuning originates in the perturbed set. The same approach can be sequentially applied to candidate areas progressively upstream of the grid cells.

Next, full-circuit activity data at single-neuron resolution can reveal much about the dynamics and dimensionality of the population response in the circuit. But without perturbation, inferring mechanism from activity alone is problematic: Materials and methods to estimate connectivity from activity (Pillow et al., 2008; Roudi et al., 2009; Honey et al., 2009) yield only effective couplings that reflect collective and externally driven correlations in addition to the true couplings. In other words, activity data alone without perturbation does not indicate where the observed activity arises or its mechanisms.

In summary, while connectomics and large-scale recording will provide vast amounts of valuable information, they are by themselves fundamentally correlative and thus not sufficient for discriminating between the candidate models discussed here. As we have shown, they may also not be immediately necessary: a low-dimensional or ‘global’ perturbative approach which does not require targeting specific individual neurons according to their responses can yield rich information about mechanism, and can do so with a far sparser dataset.

Interestingly, cooling and similar perturbation experiments have been performed in V1 (Michalski et al., 1993; Ferster and Miller, 2000) but were not as revealing about underlying mechanism as they promise to be in grid cells. Why is this? Unfortunately, the candidate models of orientation tuning in V1 are ring networks (fully periodic, single-bump) or a feedforward mechanism, and as we have seen, these two models do not differ in their predictions for the DRPS (Figure 3). The multi-bump spatial tuning of grid cells derived from velocity integration at some stage offers a way to distinguish feedforward from recurrent models because perturbation at the integration stage is predicted produce a change in the spatial tuning curve period, an opportunity that does not exist in in V1. Thus, grid cells offer a unique opportunity to uncover the circuit mechanisms that support tuning curves and computation in the cortex, and our modeling work shows how to do so.

### Assumptions

We have assumed that the population pattern is stable against rotations (but the spatial tuning curves of cells are permitted to rotate) because a rotation would induce large changes in the DRPS and obscure the predicted effects of pattern expansion. Our assumption is supported by the observation that cell–cell phase relationships between grid cells are conserved across time and environments (Yoon et al., 2013), which can only hold if the underlying population pattern does not rotate.

The simplification that relative phases in the population pattern can be obtained from relative spatial tuning phases is valid if the intrinsically determined relative spatial phases of cells are not overridden by external spatial inputs. For instance, if an external cue (landmark or boundary) is associated with a specific configuration of grid cell phases, with the association acquired pre-perturbation, then the cue could activate the same configuration of grid cells post-perturbation, which can interfere with the perturbation-induced shifts in the intrinsic relative phases between these cells. To avoid this possibility it is important, post-perturbation, to assess spatial tuning relationships between cells only in novel environments, where there are no previously learned associations between external cues and the grid cell circuit. Ideally, these novel environments will be relatively free of spatial cues that resemble previously encountered cues and boundaries. Thus, the best environments for post-perturbation testing would be circular 2D arenas, differently colored, patterned, and scented, and with minimal distal cues beyond a global orienting cue; or virtual environments with visually textured but landmark-free walls (Yoon et al., 2016).

Even in novel environments, intrinsic error correcting mechanisms hypothesized in Sreenivasan and Fiete, 2011 might trigger pre-perturbation grid cell configurations: a configuration of grid cells, after it is associated with a specific place field, can be triggered simply by activation of that place cell by another but similar grid cell configuration in the novel environment. We explore this possibility in a model and show that even after constructing associations of grid configurations with place fields at every location in two familiar environments, grid cell activations in a novel environment do not trigger activation of the learned place fields and their associated grid configurations from the familiar environments Figure 5—figure supplement 5. Based on this result, we believe that post-perturbation relative phases in grid cells may be relatively unaffected by intrinsic error-correction mechanisms in relatively featureless novel environments.

An interesting corollary to the possibility that previously learned reset or corrective inputs may co-activate cells that are out-of-phase cells post-perturbation (as is possible for partially periodic and aperiodic recurrent mechanisms) in familiar environments is that such resets should degrade rather than improve the quality of grid cell spatial tuning post-perturbation in previously learned environments.

Finally, it is important to note that if, in feedforward models, one were to include strong, continuous (rather than punctate, landmark-based) feedback from the grid cell layer to the spatially tuned inputs (as in Bush and Burgess, 2014), the network would effectively become a recurrent circuit that we have not included as a candidate. Similarly, we have excluded from our analysis recurrent network models of the spatial circuit with heterogeneous tuning and connectivity (Cueva and Wei, 2018; Banino et al., 2018; Kanitscheider and Fiete, 2016); these models do not yet capture the modular dynamics of the grid cell system, in which cells cluster in spatial period and those with similar period have the same orientation without the help of external aligning cues. When these models are refined, and if the result is a distinct mechanism for modular grid cell dynamics than the candidate models considered here, it will be interesting to perform our proposed perturbations in them to obtain their predictions for experiment.

## Materials and methods

Figure 1 and Figure 1—figure supplement 1 are schematic. In Figure 2, Figure 4a–b, Figure 2—figure supplement 2 and Figure 4—figure supplement 1, relative phase is computed from the population phases using idealized (hand-drawn) periodic population patterns that expand ($\delta^{i⁢j}=ϕ_{p⁢o⁢p}^{i}-ϕ_{p⁢o⁢p}^{j}$), without the use of neural network simulations. Figure 3, Figure 1—figure supplement 1, Figure 2—figure supplement 1, Figure 3—figure supplement 1, Figure 2—figure supplement 4, Figure 5—figure supplement 1, Figure 5—figure supplement 2, Figure 5—figure supplement 3, and Figure 5—figure supplement 4, which distinguish between different recurrent architectures, are obtained by simulating the grid cell system in a neural network. Briefly, the network consists of excitatory and inhibitory neurons (except in Figure 1—figure supplement 1 – see figure caption for details) with linear-nonlinear Poisson (LNP) spiking dynamics (Burak and Fiete, 2009; Widloski and Fiete, 2014) (except for Figure 2—figure supplement 4, where we use Hodgkin-Huxley dynamics). Structured lateral interactions between neurons pattern the neural population responses. Relative spatial tuning phases are computed from the tuning curves of different neurons, obtained by simulating the network response over 1 min long simulated quasi-random trajectories. The analysis of relative phase shifts, tuning amplitude and period in a network includes all cells with sufficiently good spatial tuning profiles: this set includes all cells in the fully and partially periodic networks and $3/4$ of the cells in aperiodic networks (from the central part of the network). Since the inhibitory and excitatory populations share similar population patterning and spatial tuning in these simulations (except in Figure 5—figure supplement 4), we arbitrarily display results from the inhibitory population.

### Neural network simulations

We use two different neuron models in our network simulations: LNP and Hodgkin-Huxley neurons, described below. Roman subscripts (e.g. $i,j$) refer to individual cells within population $P$. The population index $P$ can take the values ${$I, E$^{R}$, E$}L$, designating inhibitory cells or excitatory cells that receive rightward or leftward velocity input, respectively. Integration is by the Euler method with time-step $d⁢t$.

#### Linear-nonlinear-poisson (LNP) neurons

The time-varying firing rate $r_{i}^{P}⁢(t)=f⁢(G_{i}^{P}⁢(t))$ of the $(P,i)$th cell is an instantaneous function of its time-varying summed input $G_{i}^{P}⁢(t)$ with threshold-linear transfer function $f$:

$$
f⁢(x)={xx>00x\leq0.
$$

Neurons emit spikes according to an inhomogeneous point process with rate $r_{i}^{P}⁢(t)$ and coefficient of variance of CV = 0.5 (see Burak and Fiete, 2009 and Widloski and Fiete, 2014 for details on generating a sub-Poisson point process). LNP dynamics were used in all simulations except for Figure 2—figure supplement 4.

#### Cortical Hodgkin-Huxley (CHH) neurons

The membrane potential of the $(P,i)$th neuron is given by:

$$
C_{m}⁢\frac{d⁢V_{i}^{P}}{d⁢t}=-I_{i}^{i⁢o⁢n,P}⁢(V_{i}^{P})-I_{i}^{s⁢y⁢n,P}
$$

where $C_{m}$ is the capacitance of the membrane, $I^{i⁢o⁢n}⁢(V)$ is the sum of the cell’s intrinsic ionic currents, and $I^{s⁢y⁢n}⁢(V)$ is the current from recurrent and feedforward synaptic inputs to the cell. The ionic current is modeled as (Pospischil et al., 2008):

$$
I^{i⁢o⁢n}⁢(V)=g¯_{L}⁢(V-V¯_{L})+g¯_{K}⁢n^{4}⁢(V-V¯_{K})+g¯_{M}⁢q⁢(V-V¯_{K})+g¯_{N⁢a}⁢m^{3}⁢h⁢(V-V¯_{N⁢a}),
$$

where the $g¯$’s represent maximal conductance values and the $V¯$’s are the reversal potentials of the leak conductance (L), the fast (K) and slow (M) potassium conductances, and the sodium conductance (Na). The dynamics and parameter settings of $n,m,q,h$ are as in Pospischil et al., 2008 (we have replaced the ‘p’ gating variable in Pospischil et al., 2008 with the notation ‘q’). For CHH neurons, the time of a spike is defined as the time-step when the voltage crosses 0 mV from below. CHH dynamics were used in Figure 2—figure supplement 4.

#### Synaptic activation

For both LNP and CHH neurons, spikes by the $(P,i)$th neuron activate all its outgoing synapses according to:

$$
\frac{d⁢s_{i}^{P}}{d⁢t}+\frac{s_{i}^{P}}{\tau_{s⁢y⁢n}}=\sumb\delta⁢(t-t_{i,b}^{P}),
$$

where $t_{i,b}^{P}$ is the time of the $b$th spike and $\delta⁢(t)$ is the Dirac delta function. The sum is over all spikes of the cell.

#### Network inputs and interactions

We based our grid cell network models on the connectivity and weights that emerge from plasticity rules over a plausible developmental process, given in Widloski and Fiete, 2014, and thus might better represent the grid cell system than a model fully wired by hand. Moreover, the network contains both inhibitory and excitatory units (with the number of inhibitory units equalling 1/5 the number of excitatory units, like in cortex).

##### Synaptic input to LNP cells

The total synaptic input $G_{i}^{s⁢y⁢n,P}⁢(t)$ into the $(P,i)$th LNP cell is given by

$$
G_{i}^{s⁢y⁢n,P}=[\alpha^{v⁢e⁢l,P}⁢(G_{i}^{r⁢e⁢c,P}+G^{0})+G^{0^{′},P}]⁢A_{i}^{P},
$$

where $\alpha^{v⁢e⁢l,P}$ is the velocity input (described below), in multiplicative form; $G_{i}^{r⁢e⁢c,P}=\sum_{P^{′}}\sum_{j=1}^{N^{P^{′}}}W_{i⁢j}^{P⁢P^{′}}⁢s_{j}^{P^{′}}$ is the recurrent network input; $G^{0},G^{0^{′},P}$ are (small, positive) constant bias terms ($G^{0}=50,G^{0^{′},I}=0,G^{0^{′},E^{L}}=G^{0^{′},E^{R}}=15$); and $A_{i}^{P}$ is a smooth envelope that modulates neural activity magnitudes across the network (described below).

To model additive velocity input, as in Figure 2—figure supplement 1c, we replace Equation 5 with the following:

$$
G_{i}^{s⁢y⁢n,P}=[G^{v⁢e⁢l,P}+G_{i}^{r⁢e⁢c,P}+G^{0}+G^{0^{′},P}]⁢A_{i}^{P},
$$

where $G^{v⁢e⁢l,P}=W^{v⁢e⁢l}⁢\alpha^{v⁢e⁢l,P}$ and $W^{v⁢e⁢l}=200$ ($\alpha^{v⁢e⁢l,P}$ described below).

##### Synaptic input to CHH cells

The total synaptic current $I_{i}^{s⁢y⁢n,P}$ into the $(P,i)$th CHH neuron is given by

$$
I_{i}^{s⁢y⁢n,P}=\alpha^{v⁢e⁢l,P}⁢[\sumP^{′}g_{i}^{r⁢e⁢c,P}⁢(V_{i}^{P}-V¯^{P^{′}})+I^{0}]⁢A_{i}^{P}
$$

where $V¯^{P^{′}}$ is the reversal potential for synaptic inputs from population $P^{′}$ ($V¯^{E}=0$ mV and $V¯^{I}=-80$ mV), $g_{i}^{r⁢e⁢c,P}=\sum_{j}^{N^{P^{′}}}W_{i⁢j}^{P⁢P^{′}}⁢s_{j}^{P^{′}}$ is the recurrent network input, $I^{0}$ is a constant bias and $\alpha^{v⁢e⁢l,P},A_{i}^{P}$ are the same velocity and envelope terms mentioned above.

##### Velocity input

The cells in the $P$th population receive a common motion-related input proportional to animal velocity along preferred direction $e^^{P}$:

$$
\alpha^{v⁢e⁢l,P}=1+\beta^{v⁢e⁢l}⁢v→⋅e^^{P},
$$

where $v→$ is the instantaneous velocity of the animal and $\beta^{v⁢e⁢l}$ is a scalar gain parameter. $e^^{P}=$ (0,0), (0,1), (0,–1) for the I, E$^{R}$ and E$^{L}$ populations, respectively. Unless otherwise noted, the velocity input is derived from a 1 min quasi-random trajectory (Widloski and Fiete, 2014).

##### Recurrent weights

We based the recurrent weights $W_{i⁢j}^{P⁢P^{′}}$ from cell $j$ in population $P^{′}$ to $i$ in $P$ on those from the mature network of Widloski and Fiete, 2014.

We first describe weights in their periodic form. Let $x_{i⁢j}=i-\gamma⁢j$, where $\gamma=\frac{N_{P}}{N_{P^{′}}}$ ($N_{P}$ is the number of neurons in population $P$). We also define the norm, $||x||_{N_{P}}≡min⁡(N_{P}-|x|,|x|)$. The E$→$I weights (i.e., $P=I$ and $P^{′}=E^{L},E^{R}$) are written as

$$
W_{i⁢j}=\frac{η}{ρ}⁢exp⁡(\frac{-||x_{i⁢j}-ρ⁢Δ||_{N_{I}}^{2}}{2⁢(\sigma⁢ρ)^{2}}),
$$

where $η$ controls the overall weight strength, $Δ$ and $\sigma$ control the shift and width, respectively, of the Gaussian profile, and $ρ$ is a scale factor that is used to shift from partially periodic ($ρ=1$) to fully periodic ($ρ=11$). The parameter $ρ$ takes the same values for the I-E and I-I weights (which are described below). The parameters are set as follows:

<table>
  <thead>
    <tr>
      <th>Weight</th>
      <th>η</th>
      <th>Δ</th>
      <th>σ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>E→L I</td>
      <td>11.5</td>
      <td>-2</td>
      <td>4</td>
    </tr>
    <tr>
      <td>E→R I</td>
      <td>11.5</td>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

The I$→$E weights are written as

$$
W_{i⁢j}=\frac{η}{ρ}⁢exp⁡(\frac{-||x_{i⁢j}-ρ⁢Δ||_{N_{E}}^{2}}{2⁢(\sigma⁢ρ)^{2}})⁢Θ⁢(||x_{i⁢j}||_{N_{E}}-ρ⁢\delta)⁢[Θ⁢(-\mu⁢x_{i⁢j})⁢Θ⁢(\mu⁢x_{i⁢j}+N_{E}/2)+Θ⁢(\mu⁢x_{i⁢j}-N_{E}/2)],
$$

where $Θ$ is the Heaviside function ($Θ⁢(x)=1$ for $x\geq0$ and 0 otherwise). The first Heaviside function cuts out weights along the diagonal (the width of which is controlled by the parameter $\delta$), while the second, third, and fourth Heaviside functions together act as a windowing function to set to zero portions of the matrix to make the weights qualitatively resemble the developmental weights from Widloski and Fiete, 2014. The parameters are set as follows:

<table>
  <thead>
    <tr>
      <th>Weight</th>
      <th>η</th>
      <th>Δ</th>
      <th>σ</th>
      <th>μ</th>
      <th>δ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4</td>
      <td>8</td>
      <td>10</td>
      <td>-1</td>
      <td>3</td>
      <td>I → EL</td>
    </tr>
    <tr>
      <td>4</td>
      <td>-8</td>
      <td>10</td>
      <td>1</td>
      <td>3</td>
      <td>I → ER</td>
    </tr>
  </tbody>
</table>

Finally, the I$→$I weights are written as

$$
W_{i⁢j}=\frac{η}{ρ}⁢[exp⁡(\frac{-||x_{i⁢j}-ρ⁢Δ||_{N_{I}}^{2}}{2⁢(\sigma⁢ρ)^{2}})+exp⁡(\frac{-||x_{i⁢j}+ρ⁢Δ||_{N_{I}}^{2}}{2⁢(\sigma⁢ρ)^{2}})]⁢Θ⁢(||x_{i⁢j}||_{N_{I}}-ρ⁢\delta),
$$

which is essentially a sum-of-Gaussians with the central portion removed (the width of which is controlled by $\delta$). The parameters are set as follows:

<table>
  <thead>
    <tr>
      <th>Weight</th>
      <th>η</th>
      <th>Δ</th>
      <th>σ</th>
      <th>δ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>12</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
      <td>I → I</td>
    </tr>
  </tbody>
</table>

For the aperiodic network, the weights have the same form and parameter values as above (with $ρ=1$), except with the following replacements:

$$
|x|←||x||_{N}
$$



$$
A_{i⁢j}^{P⁢P^{′}}⁢W_{i⁢j}^{P⁢P^{′}}←W_{i⁢j}^{P⁢P^{′}}.
$$

where $|.|$ is the absolute value and $A_{i⁢j}^{P⁢P^{′}}=A_{i}^{P}⁢A_{j}^{P^{′}}$ is an envelope function used to enforce a tapered profile on the weights, similar to Burak and Fiete, 2009:

$$
A_{i}^{P}={1r_{i}^{P}<κ⁢N_{P}exp⁡[-a_{0}⁢(\frac{r_{i}^{P}-κ⁢N_{P}}{(1-κ)⁢N_{P}})^{2}]otherwise,
$$

where $r_{i}^{P}=|i-\frac{N_{P}}{2}|$, and$κ=0.3$ determines the range of the taper while $a_{0}=30$ controls its steepness.

##### Changing pattern period by varying the ‘neural’ time-constant and the gain of recurrent inhibition in a network of LNP neurons

The period of the population pattern can be varied by rescaling the synaptic activation time constant, $\tau_{s⁢y⁢n}$. It can also be varied by changing a gain parameter $\gamma_{i⁢n⁢h}$ that controls the strength of synaptic weights from the inhibitory neurons: we set $W^{P⁢I}→\gamma_{i⁢n⁢h}⁢W^{P⁢I}$, and allow $\gamma_{i⁢n⁢h}$ to be varied away from unity.

The effect of time-constant on period in the different networks is quite non-trivial: It cannot be derived from a linear stability analysis on the network equations since it depends strongly on nonlinear interactions within the network bulk and with the network boundaries (Widloski, 2015). Instead, we study the effect though simulation of the nonlinear dynamics of the networks.

As noted in the main manuscript, neuromodulators can drive the requisite gain changes in recurrent weights. We show, through the more detailed Hodgkin-Huxley neuron simulations described below, that temperature may be used in experiments to cause similar changes in period as can be affected by changing recurrent weight strength, and that the effects of temperature change resemble the effects of changing the time-constant in the LNP model.

We study Hodgkin-Huxley (HH) dynamics to predict, with the help of more biophysically detailed neuron models and the documented variation of their parameters with temperature, the effects of cooling on population activity in grid cells. Specifically, we use a ‘regular spiking’ HH model of cortical neurons (Pospischil et al., 2008), which we supplement with models that describe temperature-induced changes in the parameters (Hodgkin et al., 1952; Katz and Miledi, 1965).

##### Effects of temperature and neuromodulation on HH dynamics

Some HH models include modifications that capture the effects of temperature variation (Hodgkin et al., 1952; Katz and Miledi, 1965). These temperature effects are modeled by $Q_{10}$ factors that multiply the time-constants ($Q_{10}^{\tau}=$ 3) and amplitudes ($Q_{10}^{a}=$ 1.3) of the ionic conductances. At temperature $T$ (in $^{∘}$C), the conductance amplitudes $g¯⁢(T)$ and time constants $\tau⁢(T)$ have the following form:

$$
g¯⁢(T)←g¯⁢(T_{0})⁢(Q_{10}^{a})^{\frac{T-T_{0}}{10}}
$$



$$
\tau⁢(T)←\tau⁢(T_{0})/(Q_{10}^{\tau})^{\frac{T-T_{0}}{10}}.
$$

where $T_{0}$ is 36$^{∘}$. We applied the $Q_{10}$ factor for $g¯$ to the ionic conductance amplitudes $g¯_{L},g¯_{K},g¯_{M},g¯_{N⁢a}$ as well as to the synaptic conductance amplitudes $W_{i⁢j}^{P⁢P^{′}}$. We also simultaneously applied the $Q_{10}$ factor for $\tau$ to the conductance and synaptic time-constants $\tau_{n},\tau_{q},\tau_{m},\tau_{h}$ and $\tau_{s⁢y⁢n}$. (For gating variable $x$, the time constant $\tau_{x}$ is defined as $\tau_{x}=1/(\alpha_{x}+\beta_{x})$, where $\alpha_{x}$ and $\beta_{x}$ are the rate constants governing the gating variable’s dynamics (Pospischil et al., 2008).)

Finally, to isolate which parameters drove the strongest thermal effects on population patterning and the direction of these effects (so that we could extract lessons for how to vary parameters in grid cell models with simpler neuron dynamics) we applied thermal changes to the ionic conductances only (changing $g¯_{L},g¯_{K},g¯_{M},g¯_{N⁢a},\tau_{n},\tau_{q},\tau_{m},\tau_{h}$ according to the $Q_{10}$ factors while holding $W_{i⁢j}^{P⁢P^{′}}$ and $\tau_{s⁢y⁢n}$ constant), or to the synaptic conductances only (changing $W_{i⁢j}^{P⁢P^{′}}$ and $\tau_{s⁢y⁢n}$ according to the $Q_{10}$ factors while holding the ionic conductance parameters fixed).

To simulate the effects of a neuromodulatory gain change in inhibitory synapses, we set $W^{P⁢I}$ to $\gamma_{i⁢n⁢h}⁢W^{P⁢I}$, where $\gamma_{i⁢n⁢h}$ is the prefactor modulating the strength of inhibition.

#### Simulation parameters

##### LNP dynamics

$N_{E_{L}}=N_{E_{R}}=$ 400 neurons; $N_{I}=$ 160 neurons; CV = 0.5; $d⁢t=$0.5 ms; $\tau_{s⁢y⁢n}=$30 ms*; $\beta^{v⁢e⁢l}=$ 1; $\gamma_{i⁢n⁢h}$ = 1*. (*: Indicates that parameters can change through perturbation.)

##### Aperiodic network with CHH dynamics

All ionic conductance parameters are identical to those described in Pospischil et al., 2008 for the RS model; as noted there, the parameters are set to values corresponding to a temperature of $T_{0}=36^{∘}⁢C$. Synaptic weight definitions and parameter values same as LNP dynamics for aperiodic network (above), except that all $η$ values are scaled by the factor $0.0015$ 400 neurons; $N_{I}=$ 160 neurons; $d⁢t=$0.025 ms; $\tau_{s⁢y⁢n}=$15 ms*; $\beta^{v⁢e⁢l}=$ 0.8; $C_{m}$ = 1 $\mu$ F/cm$^{2}$; $g¯_{L}=$0.1 ms/cm$^{2}$*; $g¯_{K}=$5 ms/cm$^{2}$*; $g¯_{M}=$0.07 ms/cm$^{2}$*; $g¯_{N⁢a}=$50 ms/cm$^{2}$*; $V¯_{L}=$−70 mV; $V¯_{K}=$−90 mV; $V¯_{N⁢a}=$50 mV; $I^{0}=$ 3 $\mu$A/cm$^{2}$; $ρ=$1. $\gamma_{i⁢n⁢h}$ = 1*. (*: Indicates that parameters can change through perturbation).

##### LNP dynamics with E-E connections

All network parameters and synaptic weight definitions same as for LNP network (see above) with the addition of E-E connections (see below), except that the weight parameters have the following changes:

<table>
  <thead>
    <tr>
      <th>Weight</th>
      <th>η</th>
      <th>Δ</th>
      <th>σ</th>
      <th>μ</th>
      <th>δ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>E→L I</td>
      <td>3</td>
      <td>-2</td>
      <td>8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E→R I</td>
      <td>3</td>
      <td>2</td>
      <td>8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>I → EL</td>
      <td>3.25</td>
      <td>8</td>
      <td>8</td>
      <td>-1</td>
      <td>3</td>
    </tr>
    <tr>
      <td>I → ER</td>
      <td>3.25</td>
      <td>-8</td>
      <td>8</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <td>I → I</td>
      <td>4</td>
      <td>4</td>
      <td>6</td>
      <td></td>
      <td>3</td>
    </tr>
  </tbody>
</table>

The E-E weights for the periodic networks are written similar to the E-I weights as

$$
W_{i⁢j}=\frac{η}{ρ}⁢exp⁡(\frac{-||x_{i⁢j}-ρ⁢Δ||_{N_{E}}^{2}}{2⁢(\sigma⁢ρ)^{2}}),
$$

and have the following parameters:

<table>
  <thead>
    <tr>
      <th>Weight</th>
      <th>η</th>
      <th>Δ</th>
      <th>σ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>E→L EL</td>
      <td>5.5</td>
      <td>-4</td>
      <td>4</td>
    </tr>
    <tr>
      <td>E→R ER</td>
      <td>5.5</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td>E→L ER</td>
      <td>5.5</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <td>E→R EL</td>
      <td>5.5</td>
      <td>0</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

As in the LNP case, to get the aperiodic version of the E-E weights, replace

$$
|x|←||x||_{N_{E}}
$$



$$
A_{i⁢j}^{E⁢E}⁢W_{i⁢j}^{E⁢E}←W_{i⁢j}^{E⁢E}.
$$

where the envelope function $A_{i⁢j}$ is described above.

#### Alternative formulation of the DRPS

As before, the $i$th cell’s firing phase within the periodic population activity pattern, defined as the cell’s population phase, is $ϕ_{p⁢o⁢p}^{i}=((i-1)mod\lambda_{p⁢o⁢p})/\lambda_{p⁢o⁢p}$ (with the arbitrary choice, made without loss of generality, that neuron 1 has phase 0) (Figure 2—figure supplement 3b, blue curve). For each cell in the population, plotting the pre-perturbation phase against the post-perturbation phase (red vs. blue curves in Figure 2—figure supplement 3b) shows that the data is quantized and lies on a series of parallel manifolds, Figure 2—figure supplement 3c. This quantization is captured via the following transformation to the phase shifts:

$$
Δϕ_{pop}^{i}={ϕ_{pop,pre}^{i}−(1+\alpha)(ϕ_{pop,post}^{i}−1),if ϕ_{pop,pre}^{i}<(1+\alpha)ϕ_{pop,post}^{i}ϕ_{pop,pre}^{i}−(1+\alpha)ϕ_{pop,post}^{i},otherwise,
$$

(we have assumed that the true stretch factor, $\alpha$, is known – later, we will show how $\alpha$ can be inferred from the data) followed by a modulo operation

$$
Δ⁢ϕ_{p⁢o⁢p}^{i}=Δ⁢ϕ_{p⁢o⁢p}^{i}mod1,
$$

and then reflecting about the midpoint of the interval

$$
Δ⁢ϕ_{p⁢o⁢p}^{i}=min⁡{Δ⁢ϕ_{p⁢o⁢p}^{i},1-Δ⁢ϕ_{p⁢o⁢p}^{i}}.
$$

The distribution of these phase shift values, Figure 2—figure supplement 3d, has three special properties: (1) The distribution is quantized, due to the fact that population activity pattern itself is quantized. (2) The number of peaks in the distribution is exactly equal to the number of bumps in the population activity pattern (this holds only for sufficiently small perturbations, such that $Δ⁢M<0.5$, where $M$ is the number of bumps in the pre-perturbation population activity pattern – see Figure 2—figure supplement 2 for explanation). (3) The peak separation in the distribution is exactly equal to the stretch factor, $\alpha$. The transformations described in Equations 20-22 require knowledge of the stretch factor, $\alpha$, a quantity that is not directly observable. However, it can be inferred from the data, because the desired $\alpha$ value is the one that makes the distribution the most peak-y. This is equivalent to projecting the data onto its orthogonal axis, Figure 2—figure supplement 3c. Peaky-ness is quantified as the Pearson’s correlation coefficient between the DRPS and a comb-like function defined over the same interval. The comb function is a series of delta-functions laid out with a spacing equal to $\alpha$. The desired $\alpha$ stretch factor is the one that maximizes this correlation (not shown).

### Correction of grid cell phases by grid cell-driven place cells

The model described below is based on work in Sreenivasan and Fiete, 2011. We assume $M$ modules, each with $N$ grid cells. The $i$th grid cell from the $m^{t⁢h}$ module in the $k^{t⁢h}$ environment has the following simplified tuning curve response:

$$
f_{i,m,k}^{G⁢C}⁢(x)∝sin⁡(\frac{2⁢\pi⁢x}{\lambda_{m}}+ϕ_{i}+ϕ~_{m,k}),
$$

where $\lambda_{m}$ is the spatial period of the $m^{t⁢h}$ module, $ϕ_{i}=2⁢\pi⁢i/N$ is the cell’s phase relative to others within the module (fixed across environments), and $ϕ~_{m,k}$ is a random module-wide phase shift that is specific to each module and each environment, Figure 5—figure supplement 5a. The synaptic projections from grid cells to place cells are set as follows: Assume a population of $P$ place cells. For the $i$th place cell in the $k^{t⁢h}$ familiar environment, assign a random place preference, $x_{i,k}^{P⁢C}$. The synaptic weight from the $(j,m)^{t⁢h}$ grid cell onto the $(i)^{t⁢h}$ place cell is incremented based on experience in environment $k$. The increment is Hebbian, given by the amplitude of the grid cell tuning curve at that place cell’s preferred location:

$$
Δ⁢W_{i,j,m}^{k}=f_{j,m,k}^{G⁢C}⁢(x_{i,k}^{P⁢C}).
$$

The total weight from grid cell $(j,m)$ to place cell $i$ is given by the sum of increments over all $L$ familiar environments:

$$
W_{i,j,m}=\sumk=1LΔ⁢W_{i,j,m}^{k}=\sumk=1Lf_{j,m,k}^{G⁢C}⁢(x_{i,k}^{P⁢C}).
$$

Given these weights, the $i^{t⁢h}$ place cell’s full sub-threshold activity in environment $k$ is simply a weighted sum over the activities of the grid cells across modules, based on its weights:

$$
f_{i,k}^{P⁢C}⁢(x)=\summM\sumjNW_{i,j,m}⁢f_{j,m,k}^{G⁢C}⁢(x),
$$

This description of place cell subthreshold activations holds for both familiar and novel environments; the only difference between familiar and novel environments is that in the latter there has been no increment of the grid cell-place cell weights based on coincident grid cell-place cell activity, Figure 5—figure supplement 5a–b. In the current implementation, we allowed every cell to have a field in every familiar environment. We see that even in this case, the subthreshold activations of PCs in the novel environment are far lower than at place fields in familiar environment; in other words, they will not be activated and drive correction or resetting of the grid cell phases in the novel environment. Including the measured degrees of sparseness in PCs should lead to even less interference than seen in simulated novel environment conditions.

### Measures used in main text

#### DRPS in 1D

The relative phase of cell $i$ and $j$ is defined as $\delta^{i⁢j}=d^{i⁢j}mod\lambda/\lambda$, where $d^{i⁢j}$ is the offset in the central peak of the cross-correlation in their spatial tuning curves, and $\lambda$ is their common spatial period (in the main text, for Figures 2, 4a-b, Figure 2—figure supplement 2, and Figure 4—figure supplement 1, the relative phase is computed directly from the population phases, that is, $\delta^{i⁢j}=ϕ_{p⁢o⁢p}^{i}-ϕ_{p⁢o⁢p}^{j}$. The relative phase magnitude is given by $|\delta|=min⁡(||\delta||,1-||\delta||)$, where $||⋅||$ is the absolute value norm. The DRPS is computed by making a distribution of phase magnitude shifts, $|\delta_{p⁢r⁢e}|-|\delta_{p⁢o⁢s⁢t}|$, where $\delta_{p⁢r⁢e}$ and $\delta_{p⁢o⁢s⁢t}$ are the relative phases measured pre- and post-perturbation.

#### 2D relative phase

For two cells $i$ and $j$, let $d→$ be the displacement vector which measures the 2D offset in the central peak of the cross-correlation in their spatial tuning curves. The displacement vector is converted into a 2D phase $\delta→$ according to $\delta→=(\delta_{1},\delta_{2})=f⁢(d_{1}^{p⁢r⁢o⁢j}/\lambda_{1}mod1,d_{2}^{p⁢r⁢o⁢j}/\lambda_{2}mod1)$, where $d→^{p⁢r⁢o⁢j}=(d_{1}^{p⁢r⁢o⁢j},d_{2}^{p⁢r⁢o⁢j})$ is the oblique projection of $d→$ onto the principal vectors $\lambda_{1}⁢e^_{1}$ and $\lambda_{2}⁢e^_{2}$, and

$$
f(x→)={(x_{1}−1,x_{2}−1)if x_{1}\geq0.5 and x_{2}\geq0.5(x_{1}−1,x_{2})if x_{1}\geq0.5 and x_{2}<0.5(x_{1},x_{2}−1)if x_{1}<0.5 and x_{2}\geq0.5(x_{1},x_{2})if x_{1}<0.5 and x_{2}<0.5.
$$

#### DRPS in 2D

The DRPS in 2D is computed separately for the two components of the 2D relative phase. That is, given the relative phase vector $\delta→=(\delta_{1},\delta_{2})$, the DRPS is computed by making a distribution of phase magnitude shifts for each component: $|\delta_{1,p⁢r⁢e}|-|\delta_{1,p⁢o⁢s⁢t}|$ and $|\delta_{2,p⁢r⁢e}|-|\delta_{2,p⁢o⁢s⁢t}|$, where the magnitude is defined as the absolute value norm: $|⋅|=||⋅||.$

#### Bootstrap resampling and phase uncertainty

Given an original spike map of $M$ total spikes (with locations) from one cell, we created a new spike map of $N$ ($N<M$) total spikes, by picking spikes (with their corresponding location coordinates) from the original map one at a time, at random, and with replacement. The same was done for a second, simultaneously recorded cell. From these sampled spike trains for a pair of cells, we estimated relative phase (by computing the location of the peak closest to the origin in the cross-correlation of the spatial maps of the two cells, as in Yoon et al., 2013). The procedure was performed 100 times, generating 100 bootstrapped relative phase estimates per cell pair. Phase uncertainty was measured as the peak location of the Rayleigh distribution that best fit the distribution of magnitudes of the bootstrapped relative phase estimates.

#### Spatial tuning curves

For a given cell and trajectory, we build a histogram of spike counts at each location (bin size = 1 cm), then normalize the count in each bin by the amount of time spent in it. The normalized histogram is smoothed by convolution with a boxcar filter (width = 5 bins) to yield a spatial tuning curve.

#### Spatial tuning period and amplitude

The spatial tuning period is measured as the inverse of the spatial frequency with the highest peak in the power spectrum of the spatial tuning curve (excluding the peak at 0 frequency). Likewise, the spatial tuning amplitude is measured as the mean spike rate density across the bins of the spatial tuning curve. The quantities reported in Figure 3 and Figure 3—figure supplement 1 are averaged over all cells in the population.

#### Population activity period and gridness

The population activity gridness is taken to be the power of the largest frequency component of the power spectrum measured from a normalized snapshot (frame) of the population activity (normalized = mean subtracted, followed by division by standard deviation). The power spectrum is rescaled by the factor 2/L$^{2}$, where L is the number of bins in the population activity vector from which the power spectrum was computed. The population activity vector is shortened to include only the middle one-half of the population, so that for the E$^{L}$ population, L is 100. From the power spectrum, the population activity period is taken to be the wavelength at which the power spectrum has the largest peak. Throughout the paper, both the reported population period and gridness are averaged over the last 10000 snapshots of the population activity pattern from a given trial.

#### Velocity response

Velocity response is measured as the translation speed (neurons/sec) of the network pattern to fixed input velocity, computed by tracking the displacement of the pattern for 10 s, smoothing the resulting trajectory with an 4 s moving average filter, and then measuring the average speed of the middle-half of the trajectory.

#### Periodicity score for the DRPS

We smooth the histogram of relative phase shifts (by convolution with a 2-bin Gaussian kernel) and normalize it (by mean subtraction and division by the standard deviation). Next, we compute the power spectrum, rescaling the result by $2/L^{2}$, where $L$ is the number of bins in the histogram ($L=200$). The periodicity score is set to be the power of the largest- amplitude non-zero frequency component in the scaled power spectrum. This score returns 1 if the DRPS is a pure sinusoid. It returns 0 if the DRPS is flat and returns an average value of $<0.2$ if the DRPS were constructed bin by bin by taking independent, identically distributed (iid) samples from a uniform distribution on the unit interval.
