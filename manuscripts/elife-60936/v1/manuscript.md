# Data-driven reduction of dendritic morphologies with preserved dendro-somatic responses

## Authors

- Willem AM Wybo<sup>1</sup> ([ORCID: 0000-0003-1385-4980](https://orcid.org/0000-0003-1385-4980)) †
- Jakob Jordan<sup>1</sup> ([ORCID: 0000-0003-3438-5001](https://orcid.org/0000-0003-3438-5001))
- Benjamin Ellenberger<sup>1</sup>
- Ulisses Marti Mengual<sup>1</sup>
- Thomas Nevian<sup>1</sup> ([ORCID: 0000-0001-9804-608X](https://orcid.org/0000-0001-9804-608X))
- Walter Senn<sup>1</sup> ([ORCID: 0000-0003-3622-0497](https://orcid.org/0000-0003-3622-0497))

### Affiliations

1. Department of Physiology, University of Bern Bern Switzerland

† Corresponding author

## Abstract

Dendrites shape information flow in neurons. Yet, there is little consensus on the level of spatial complexity at which they operate. Through carefully chosen parameter fits, solvable in the least-squares sense, we obtain accurate reduced compartmental models at any level of complexity. We show that (back-propagating) action potentials, Ca2+ spikes, and N-methyl-D-aspartate spikes can all be reproduced with few compartments. We also investigate whether afferent spatial connectivity motifs admit simplification by ablating targeted branches and grouping affected synapses onto the next proximal dendrite. We find that voltage in the remaining branches is reproduced if temporal conductance fluctuations stay below a limit that depends on the average difference in input resistance between the ablated branches and the next proximal dendrite. Furthermore, our methodology fits reduced models directly from experimental data, without requiring morphological reconstructions. We provide software that automatizes the simplification, eliminating a common hurdle toward including dendritic computations in network models.

## Introduction

Morphological neuron models have been instrumental in neuroscience (Segev and London, 2000). Major experimental discoveries, for instance that N-methyl-D-aspartate (NMDA) channels (MacDonald and Wojtowicz, 1982) produce local dendritic all or none responses (Schiller et al., 2000; Major et al., 2008), or that dendritic Ca2+ spikes mediate coincidence detection between distal inputs and somatic action potentials (APs) (Larkum et al., 1999), have been combined in morphological models to arrive at a consistent picture of dendritic integration: the dendrite is an intricate system of semi-independent subunits (Mel, 1993; Poirazi et al., 2003b; Poirazi et al., 2003a), amenable to dynamic regulation (Poleg-Polsky et al., 2018; Wybo et al., 2019), and able to distinguish specific input patterns (Branco and Häusser, 2010; Laudanski et al., 2014).

Nevertheless, morphological models are not without shortcomings. They are highly complex and consist of thousands of coupled compartments, each receiving multiple non-linear currents. The parameters of the models, typically fitted with evolutionary algorithms to electro-physiological recordings (Hay et al., 2011; Almog and Korngreen, 2014; Van Geit et al., 2016), number in the tens of thousands. Since recordings can only be obtained at a few dendritic sites, these fits are under-constrained, and thus susceptible to over-fitting. Accordingly, the single-neuron fitting challenge, where model performance was measured on unseen spike trains, was not won by a biophysical model, but by an abstract spiking model (Gerstner and Naud, 2009; DiLorenzo and Victor, 2013). Finally, many network-level observations can be explained without morphological models (Gerstner et al., 2012).

These shortcomings underline the need to find the essential computational repertoire of a neuron: the set of computations needed to understand brain functions such as learning and memory. Model simplification is crucial in this endeavor, as it elucidates the lowest level of complexity at which computational features are preserved. Conceptually, the simplification thus extracts the essential elements required for the computation from the underlying biophysics. Simulation-wise, the reduced model requires few resources and can thus be integrated in large-scale networks. Experimentally, the reduced model likely leads to a well-constrained fit.

Past simplification efforts can be grouped in two categories: approaches that use traditional compartments, but with adapted parameters (Pinsky and Rinzel, 1994; Destexhe, 2001; Tobin et al., 2006; Bahl et al., 2012; Marasco et al., 2013; Amsalem et al., 2020), and approaches that rely on more advanced mathematical techniques (Kellems et al., 2009; Kellems et al., 2010; Wybo et al., 2013; Wybo et al., 2015). Many authors apply ad hoc morphological simplifications and then adjust model parameters to conserve geometrical quantities, such as surface area (Davison et al., 2000; Hendrickson et al., 2011; Marasco et al., 2013), or electrical quantities, such as attenuation (Destexhe, 2001) and transfer impedance (Amsalem et al., 2020). Other authors propose two-compartment models whose parameters are adjusted to reproduce certain response properties (Pinsky and Rinzel, 1994; Naud et al., 2014). Nevertheless, these approaches often lack the flexibility to be adapted to a wide range of dendritic computations. Furthermore, particular afferent spatial connectivity motifs might be lost, so that essential computations are not captured by such a reduction. Hence, in a network model, the computational relevance of these motifs might unknowingly be ignored. Advanced mathematical techniques on the other hand are very flexible, as they can incorporate the response properties of the morphology implicitly. (Wybo et al., 2013 and Wybo et al., 2015 propose a system of convolutions whose kernels capture the passive properties of the compartmental model, whereas Kellems et al., 2009 and Kellems et al., 2010 linearly transform the compartmental model into a low-dimensional basis.) However, these techniques are not supported by standard simulation software, such as NEURON (Carnevale and Hines, 2004), a considerable hurdle toward their integration in the canonical neuroscience toolset.

Here, we introduce a simplification method with the flexibility of advanced mathematical techniques, but using traditional compartments. The approach accommodates any morphological model in public repositories (McDougal et al., 2017) and commonly used ion channels (Podlaski et al., 2017). The reduced models represent the optimal approximation to the dendritic resistance matrix, evaluated at any spatial resolution of choice. We fit ion channels by approximating the quasi-active resistance matrices (Koch and Poggio, 1985). All our fits are uniquely solvable linear least-squares problems. The obtained models extrapolate well to non-linear dynamics, and reproduce back-propagating APs (bAPs), Ca2+ spikes (Larkum et al., 1999), and NMDA spikes (Schiller et al., 2000; Major et al., 2008) with few compartments. Additionally, we investigate whether a dendritic tree with given afferent spatial connectivity motifs can be simplified by ablating subtrees or branches and grouping synapses in the next proximal compartment. We find that effective weight-rescale factors for synapses can be computed if temporal conductance fluctuations stay below a limit that depends on the difference in input resistance between the ablated branch and the next proximal dendrite. Under application of these factors, voltage responses in the simplified tree are preserved. Finally, we demonstrate that our approach can fit reduced models to experimental recordings, without the need to reconstruct full morphologies. We have created a Python toolbox (NEural Analysis Toolbox – NEAT – https://github.com/unibe-cns/NEAT) (copy archived at swh:1:rev:1cb15f36aa0a764105348541d046c85ef38e21ee) that implements this method together with an extension to NEURON to simulate the obtained models.

## Results

### A systematic simplification of complex neuron morphologies

Our simplification strategy fits compartments with voltage-gated channels to a reduced set of dendritic locations of interest (Figure 1A, left-middle). The locations, together with the morphology, provide a tree structure for the reduced model (Figure 1A, middle-right) where each node corresponds to a traditional compartment and each edge to a coupling conductance. The fit requires that the reduced model responds similarly to perturbative current steps as the full neuron, at the set of chosen locations (Figure 1B). We consider perturbations around any spatially uniform holding potential $v_{h}$. Experimentally, $v_{h}$ may be reached by injecting a constant current $i_{h}$, and thus $v_{h}$ is the effective equilibrium potential under this current injection. In models, we do not need to know $i_{h}$; we simply assume that $v_{h}$ is the equilibrium potential around which to linearize the model. Note that if $i_{h}=0$, $v_{h}$ is the resting membrane potential.

![Figure 1.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig1-v1.jpg)

**Figure 1.:** (A) For any set of locations on a given morphology (left, here an L2/3 pyramidal cell [Branco and Häusser, 2010]), a reduced compartmental model can be derived (middle), with an associated schematic representation (right). (B) Steps of our approach: (1) choice of locations at which the reduced model should reproduce the full model’s voltage, (2) coupling, leak and channel conductances are fitted to resistance matrices derived from the full model at different holding potentials, and (3) capacitances are fitted to mimic the largest eigenmode of the full model. (C) The resistance matrix of the passive full model (top) restricted to the five locations in A is approximated accurately by the inverse of the conductance matrix of the passive reduced model (bottom). Labels correspond to locations in A. (D) Example components of the quasi-active resistance matrix of the full model, equipped with a Na+-channel, as a function of the holding potential $v_{h}$. Red lines show the four holding potentials at which our methodology evaluates the resistance matrix. Singularities correspond to holding potentials where the linearization is invalid and should be avoided in the fit. Labels correspond to locations in A. (E) Temporal shape of exemplar input impedance kernels of the full model (gray) and their reduced counterparts (blue, dashed). (F) Same as in E, but for transfer impedance kernels.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Error of the reduced model’s resistance matrix compared to the full model’s resistance matrix, for reductions of the passive L2/3 pyramid with 2, 5, 10, 20, and 50 compartments. Five random sets of fit locations were chosen for each compartment number; mean (marker) and standard deviation (error bars) are shown. (B) Same as A, but for the impedance kernels. (C) The bifurcations between compartment sites need to be added, as shown in the red forked dendrite (left). Soma $S$ and two compartment sites 1, 2 (top) were augmented with a site $B$ on the main trunk (but not at a bifurcation, middle) or a site $B$ at the bifurcation (bottom). Reductions were derived for all three configurations, but only the last configuration can accurately approximate all resistances (right). (D) Resistance matrices for the soma S and location five in Figure 1A, with Na+-channels at the soma. The resistance matrix $Z$ (first column) depends on $v_{h}$. The inverse of the matrix $G$ (second column) is fitted by adjusting the maximal Na+ conductance parameter so that $ZG=I$ at the four holding potentials. $G^{-1}$ matches $Z$ closely, as the difference between both matrices is close to zero (third column). (E) Behavior of the input and transfer resistances between a compartment site $c$ (green square) and a synapse site $s$ located more distally on the same subtree (only a single branch is shown for clarity, marked in green). Transfer resistance between $c$ and $s$ remains close to the input resistance at $c$, while input resistance at $s$ increases markedly with distance. This principle holds in the apical (top) as well as basal (bottom) dendrites.

Suppose we have chosen $N$ locations. Let $\delta⁢𝐢$ be a vector describing perturbative input currents to each of those $N$ locations. The linearized voltage response of the full neuron, at those locations, is given in the Fourier domain for an input of a particular frequency $\omega$ by

$$
\delta⁢𝐯⁢(\omega)=Z_{v_{h}}⁢(\omega)⁢\delta⁢𝐢⁢(\omega),
$$

with $Z_{v_{h}}$ the quasi-active (Koch and Poggio, 1985) $N\timesN$ impedance matrix. In experiments, $Z_{v_{h}}$ is extracted from $\delta⁢𝐯$ measured in response to $\delta⁢𝐢$. In models, $Z_{v_{h}}$ is algorithmically computed based on the full morphology, the parameters of the passive currents, and the dynamics of the voltage-gated ion channels (Koch and Poggio, 1985). For our reduction method, we consider perturbative current steps, so that after an equilibration period, we obtain a steady-state voltage response $\delta⁢𝐯$. Note that this corresponds to evaluating (Equation 1) at zero frequency, and that the corresponding matrix $Z_{v_{h}}(\omega=0)$ contains the input and transfer resistances. Throughout the manuscript, we maintain the notation that $z$ without argument signifies $z(\omega=0)$, representing an individual input or transfer resistance, and that $Z$ signifies $Z(\omega=0)$, representing the resistance matrix.

Linearizing the reduced compartmental model around a holding potential (see Materials and methods — The conductance matrix) yields an $N\timesN$ conductance matrix $G_{v_{h}}$, with on its diagonal

$$
g_{L⁢i}+\sumn\in𝒩_{i}g_{C,i⁢n}+\sumd\inℐ_{i}g¯_{d⁢i}⁢l_{d}⁢(v_{h}),
$$

where $g_{L⁢i}$ is the unknown leak conductance of the $i$-th compartment, $𝒩_{i}$ the set of nearest neighbor compartments, and $g_{C,i⁢n}$ the unknown coupling conductance between compartment $i$ and compartment $n\in𝒩_{i}$. The second sum runs over the set $ℐ_{i}$ of all linearized currents of ion channels present in compartment $i$, where $g¯_{d⁢i}$ is the unknown maximal conductance of ion channel $d$ and $l_{d}⁢(v_{h})$ is a factor that follows from linearizing the dynamics of channel $d$ around the holding potential $v_{h}$ (see Materials and methods – Quasi-active channels). Thus, the unknowns $g_{L⁢i}$, $g_{C,i⁢n}$ for $n\in𝒩_{i}$, and $g¯_{d⁢i}$ for $d\inℐ_{i}$ are to be fitted for each compartment, and the factors $l_{d}⁢(v_{h})$ are known and determined by the ion-channel dynamics. The $i⁢j$’th off-diagonal element of $G_{v_{h}}$ is $-g_{C,i⁢j}$ – the negative of the coupling conductance between compartments $i$ and $j$ – if $i$ and $j$ are nearest neighbor compartments on the reduced tree structure, and zero otherwise. The conductance matrix relates the reduced model’s voltage response to the perturbative input current steps

$$
G_{v_{h}}⁢\delta⁢𝐯=\delta⁢𝐢.
$$

The full neuron and reduced model will behave similarly for all possible perturbative input steps $\delta⁢𝐢$ if their responses $\delta⁢𝐯$ match. From (Equation 1) and (Equation 3), it follows that $Z_{v_{h}}$ should be the inverse of $G_{v_{h}}$. Consequently, we require that multiplying the known $Z_{v_{h}}$ (measured or calculated) by the parametric $G_{v_{h}}$ yields the identity

$$
Z_{v_{h}}G_{v_{h}}≈I.
$$

From (Equation 2), it can be seen that (Equation 4) is linear in the parameters that have to be fitted (leak, coupling, and maximal ion-channel conductances of the reduced compartments). By consequence, (Equation 4) can be cast into a least-squares problem and solved accurately (Figure 1C, Figure 1—figure supplement 1A).

Since the linearized ion channel activation $l_{d}⁢(v_{h})$ depends on the holding potential, $Z_{v_{h}}$ changes with $v_{h}$ (Figure 1D). The fit must disentangle the changes in $Z_{v_{h}}$ induced by the various channels. In models, we first block all voltage-gated ion channels in the full and reduced models and fit $G_{pas}$ to $Z_{pas}$ according to (Equation 4), and thus obtain leak and coupling conductances for each compartment. Then, we unblock one ion channel at a time and decompose the conductance matrix into $G_{v_{h}}=G_{pas}+G_{v_{h},chan}$, with $G_{v_{h},chan}$ a diagonal matrix containing the conductances of the unblocked channel, linearized around $v_{h}$, at each compartment. Thus $G_{v_{h},chan}$ depends linearly on the unknown maximal ion channel conductance parameters. With $Z_{v_{h}}$ and $G_{pas}$ known, we optimize these maximal conductances, so that the left-hand side of

$$
Z_{v_{h}}G_{v_{h},chan}≈I−Z_{v_{h}}G_{pas}.
$$

matches the right-hand side, and that it does so for multiple holding potentials (we chose $v_{h}=-75,-55,-35$, and $−15$ mV, Figure 1D, Figure 1—figure supplement 1D). Thus, we obtain an overdetermined system of equations in the unknown maximal channel conductances at each compartment and compute its solution in the least mean squares sense.

Having fixed the steady-state behavior of the reduced model, we are left with the capacitance of each compartment of the reduced model to match the temporal dynamics of the full model as closely as possible. In our reductions, the capacitance of each compartment is thus a parameter to be fitted. To do so, we found it sufficient to consider passive membrane dynamics. Blocking all voltage-gated ion channels in the reduced model ($G_{v_{h},chan}=0$), temporal voltage responses follow

$$
diag⁢(𝐜)⁢𝐯˙=-G_{pas}⁢𝐯+𝐢,
$$

with $𝐜$ a vector containing the unknown capacitance of each compartment. We require that voltage-decay back to rest, as described by (Equation 6), matches voltage decay in the full neuron with all active channels blocked, at the $N$ chosen locations. According to linear dynamical systems theory (Strogatz, 2000), this decay can be decomposed as a sum of exponentially decaying eigenmodes, each with an associated eigenvalue $\alpha_{k}$ and eigenvector $ϕ_{k}$. The former gives the exponential time scale $\tau_{k}=1/\alpha_{k}$ of the decay and the latter the spatial profile of the mode. The most prominent of these modes has the largest time scale $\tau_{0}=1/\alpha_{0}$, and primarily models the voltage decay back to rest through trans-membrane currents (Holmes et al., 1992). In experiments, we extract this mode by fitting an exponential to the voltage decay. In full models, we compute the eigenvalue $\alpha_{0}$ and eigenvector $ϕ_{0}$ – restricted to the $N$ chosen locations – with the separation-of-variables method (Major et al., 1993). In the reduced model, eigenmodes are found as the eigenvalues and eigenvectors of the matrix $S=-diag⁢(𝐜)^{-1}⁢G_{pas}$. To fit the capacitances, we require that $S$ has $\alpha_{0}$ as eigenvalue and $ϕ_{0}$ as corresponding eigenvector:

$$
S⁢ϕ_{0}=\alpha_{0}⁢ϕ_{0}.
$$

This system of equations is linear in the reciprocals of the capacitances entering in $S$ and can thus be solved efficiently.

To accurately reproduce the spatio-temporal voltage responses of the full model, the reduced model must approximate the ‘impedance kernels’ $z⁢(t)$ (Wybo et al., 2015), the inverse Fourier transforms of the frequency-dependent elements of the impedance matrix. Despite only fitting the largest time scale $1/\alpha_{0}$, we accurately reproduce kernels at all times (Figure 1E,F, Figure 1—figure supplement 1B).

Unless a large number of closely spaced compartment sites is retained on the morphology, our reductions replace the true axial currents flowing along the dendritic tree, which are shaped by the distribution of ion channels in the dendritic membrane, with a strong abstraction: a single coupling conductance between compartments that may be far apart. Hence, it is not guaranteed that the resting voltage of reduced model will be equal to the resting voltage of the full model, at the $N$ chosen locations. We ensure that this will be the case by fitting the leak reversals for each compartment. The product of leak conductance and reversal represents a constant current for each compartment, and thus does not influence model dynamics beyond fixing it’s resting voltage. To fit the leak reversals, we evaluate all ion-channel currents in the reduced model at the full model’s resting voltage and require that temporal voltage derivatives are zero. The obtained equations are linear in the reduced model’s leak reversals, and hence can be solved efficiently. Note that our methodology does not guarantee that the obtained reversals are within physiological limits. Thus, they should purely be seen as fit parameters that determine the resting membrane potential.

### Reduced models match the voltage response of their full counterparts

We demonstrated the reduction on two computations that require accurate spatio-temporal interaction. We reproduced sequence discrimination in an L2/3 pyramidal cell model (Branco and Häusser, 2010), where a neuron responds more strongly to a centripetal sequence of inputs than to a centrifugal one, by only retaining compartments on a single branch (Figure 2A). We also reproduced input-order detection (Torben-Nielsen and Stiefel, 2009), where a neuron responds more strongly when one input arrives before the other, by only retaining compartments at the soma and the two input sites (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig2-v1.jpg)

**Figure 2.:** (A) Reduction of full model (right) to a single branch (middle) reproduces sequence discrimination (right), full model in gray, and reduced model colored for different time-steps between inputs, centripetal (dashed), and centrifugal (dash-dotted). (B) Full model (left) and three-compartment reduction (middle, bottom) discriminate temporal order of inputs, where the response to inputs (middle, top) ordered $1→2$ is stronger than $2→1$. Voltage responses (right) in full model (gray) and reduced model (colored). (C, D) Reductions of resp. L5 pyramidal and Purkinje cells with active ion channels at the soma, and excitatory (AMPA+NMDA) and inhibitory (GABA) synapses at dendritic compartment sites. From left to right: full model with compartment sites (soma S and a selected dendrite site D are labeled), reduced model, somatic voltage with zoom on a single AP (full model in gray and reduced model in purple, input spikes at the bottom), dendritic voltage at D (full model in gray and reduced model in green, input spikes at the bottom), and the relative root mean square voltage errors at each compartment (root mean squared error normalized by the standard deviation $R⁢R⁢M⁢S⁢E⁢(v)=\sqrt{Avg⁢(v_{full}-v_{reduced})^{2}}/\sigma_{v_{full}}$). Spike coincidence factor $Γ$ is also shown.

We then tested our approach with non-linear currents concentrated at discrete points (hot-spots) along the morphology. In two biophysical models – an L5 neocortical pyramid (Hay et al., 2011; Figure 2C) and a Purkinje cell (Chen et al., 2013; Miyasho et al., 2001; Figure 2D) – we removed active dendritic channels, but added their total conductance at rest to the passive leak (we term this the 'passified’ model), while retaining all active channels at the soma. The soma, with its AP-generating channels, naturally forms such a non-linear hot-spot. We implemented dendritic hot-spots by clustering sets of excitatory (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid [AMPA] + NMDA) and inhibitory (γ-aminobutyric acid [GABA]) synapses at randomly selected points on the morphology. Both the reduced pyramidal cell model and the reduced Purkinje cell model accurately reproduced the somatic and dendritic membrane voltage traces of their full counterparts (Figure 2C,D, middle panels). Furthermore, 97% and 89% of APs coincided within a 6 ms window, respectively (Jolivet et al., 2008; Figure 2C,D, right panels).

Models with passive dendritic membranes but non-linear synapse clusters can already reproduce much of the canonical computational repertoire of dendrites. Clusters of AMPA+NMDA synapses at the distal tips of basal dendrites can make neurons function as two-layer networks (Mel, 1993; Poirazi et al., 2003b; Poirazi et al., 2003a). Such reduced models also exhibit the same robustness to input noise as the full models (Poleg-Polsky, 2019), and can include modulation of the co-operativity between AMPA+NMDA clusters through compartments with shunting conductances (Wybo et al., 2019). Furthermore, because our reduced models reproduce dendritic input impedance properties, long time-scale NMDA currents activate strongly in distal compartments as high distal input impedance helps to overcome their voltage-dependent Mg2+ block (Jahr and Stevens, 1990a; Jahr and Stevens, 1990b), whereas short time-scale AMPA currents dominate in more proximal compartments. Thus passive models with non-linear synapse clusters also capture the shift in computational strategy from a proximal temporal code to a distal rate code (Branco and Häusser, 2011).

What level of spatial complexity reproduces characteristic responses generated by somatic and dendritic ion channels? These responses arise through the interplay of integrative properties of the morphology – captured in the impedance kernels $z⁢(t)$ – and channel dynamics. If a full model (here the L2/3 pyramid) is reduced to a single somatic compartment (Figure 3A), the impedance kernel has only one time scale – the membrane time-scale (Figure 3B, top – purple). The kernel of the full model contains additional shorter time scales (Figure 3B, top – gray), leading to a faster AP onset than in the reduced model (Figure 3B, bottom). This effect is thus a fundamental limitation of the single-compartment reduction. Extending the compartmental model with four nearby dendritic sites (Figure 3A) adds fast components to the somatic impedance kernel (Figure 3B, top – green) that model the spread of charge to the other compartments. These components increase AP amplitude and decrease AP delay (Figure 3C), leading to a better match with the full model.

![Figure 3.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig3-v1.jpg)

**Figure 3.:** (A–C) Effect of compartment distribution on AP dynamics in reduced models. (A) One- and five-compartment reductions of the L2/3 pyramid, equipped with somatic and dendritic ion channels. (B) Differences in short time-scale behavior in somatic input impedance kernels (top) between full model (gray) and one- (purple) and five-compartment (green) reductions result in different AP delays (bottom). (C) AP amplitude (top) and AP delay (bottom) for the three models (colors as in B). (D–F) Effect of compartment distribution on AP back-propagation in basal dendrites. (D) Four- and two-compartment reductions of a basal branch. (E) APs at soma (top) and most distal compartment site (bottom) for four models (full in gray, four compartments in blue, two compartments in orange, and full but with a passive dendrite in green). (F) Amplitude (top) and delay (bottom) for bAPs at different distances from soma (if compartment is present in model), averaged over all basal branches longer than 150 μm (error bars indicate standard deviation). (G–I) AP back-propagation in the apical dendrite of the L5 pyramid. (G) Reductions of the apical dendrite with increasing inter-compartment spacing. (H) Voltage waveform at soma (top, full in gray, $Δ⁢x=100$ μm in blue, $Δ⁢x=200$ μm in orange) and two dendritic sites (middle, bottom). (I) Waveform amplitude as a function of distance to soma for various inter-compartment spacings. (J, K) Ca2+-spike-mediated coincidence detection. (J) Reduction of the L5-pyramid’s apical dendrite to 11 compartments. (K) Response to a somatic current pulse (top, left), a dendritic synaptic current waveform (top, right), and the coincident arrival of both inputs (bottom).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) The compartment sites on the morphology. (B) Ca2+ mediated coincidence detection between somatic and dendritic inputs does not result in an AP burst. Response to a somatic current pulse (top, left), a dendritic synaptic current waveform (top, right), and the coincident arrival of both inputs (bottom). Stimulus parameters where identical to Figure 3, except the amplitude of the dendritic input current, which was increased to 0.75 nA. (C) Somatic input impedance kernel (top), input impedance kernel at most proximal dendritic location (middle, marked with D in A) and transfer impedance kernel between soma and dendritic location. Full model (gray), reduction with trunk (blue, configuration as in Figure 3J), and reduction without trunk (orange, configuration as in A).

Dendritic ion channels support the back-propagation of APs (Stuart et al., 1997). For each basal branch of at least 150 μm in the L2/3 pyramid, we derived reduced models with three compartments (at 50, 100, and 150 μm from the soma) and with one compartment. We compared bAP amplitudes and delays relative to the somatic AP (Figure 3E) and found that even models with a single distal compartment support active back-propagation (Figure 3E,F). In the apical dendrite of the L5 pyramid (Figure 3G), we found that a distance step of 100 μm between compartments was required to support bAPs to the same degree as in the full model (Figure 3H,I).

Finally, we considered the pairing of a somatic current pulse with a dendritic post-synaptic potential waveform. We found that an 11-compartment reduction (Figure 3J) – with compartments spaced at 100 μm through the apical trunk to support bAPs until the Ca2+ hot-zone – reproduced the Ca2+-mediated coincidence detection mechanism (Larkum et al., 1999; Pérez-Garci et al., 2013).

### Conditions under which afferent spatial connectivity motifs can be simplified

Our method allows us to reduce morphological complexity by removing any branch or subtree without affecting the integrative properties of other branches or subtrees. Up until now, we have only considered reductions where the to-be removed branch or subtree does not receive direct synaptic input. However, if this branch or subtree does receive synaptic input, the morphological reduction also simplifies the afferent spatial connectivity motifs targeting it, as synapses have to be grouped at the nearest proximal intact compartment. We assess whether the computational repertoire of the neuron remains intact under such a simplification, or which elements of the repertoire might be lost. We study two proxies for this repertoire: the voltage difference between full and reduced models at the intact compartments – in order to assess whether the output of local computations in the ablated branch or subtree can be recovered, and the difference between full and reduced models in NMDA-spike threshold at the nearest proximal intact compartment (quantified as the smallest number of AMPA+NMDA synapses with a weight of 1 nS that need to be activated simultaneously to elicit an NMDA spike) – in order to assess whether local integrative properties at the intact compartments can also be retained under the shift of synapses. We allow ourselves the liberty of rescaling the weights of the shifted synapses by a temporally constant factor $\beta$ (Figure 4A). Which spatial synapse distributions admit simplification in this sense, and under which input conditions?

![Figure 4.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig4-v1.jpg)

**Figure 4.:** (A) Removal of a branch with a synapse (red triangle) is considered possible if the correct voltages at the compartment sites (here, dendritic – green square and somatic – purple square) can be obtained by shifting the synapse to the compartment site and rescaling its weight with a fixed factor $\beta$ for the all input conditions under consideration. (B) Comparison between weight-rescale factors for current-based (left) and conductance-based (right) input. Voltage trace for dendritic compartment without rescaling (gray) and with the current-based scale factor $\beta_{c⁢u⁢r⁢r}$ compensating for attenuation (blue). Bottom right panel shows voltage trace with conductance-based scale factor $\beta_{c⁢o⁢n⁢d}$. (C) Current- and conductance-based scale factors in the green dendritic branch, for a shift of a synapse at a given distance from the soma to the dendritic compartment site (green square). (D) Spatial peak voltage without (left, blue) and with (right, orange) application of $\beta_{c⁢o⁢n⁢d}$. (E) For a cluster of AMPA+NMDA synapses in isolation, scale factors for physiological constants can be obtained (see Materials and methods — Synaptic weight-rescale factors) that reproduce the correct voltage waveform. Colors as in D. (F) Maximal amplitude of NMDA-spike waveform upon activation of increasing numbers of synapses – NMDA-spike thresholds indicated with vertical lines. Colors as in D. (G–H) Removing a whole subtree and shifting multiple synapses (red triangles) to the next proximal compartment site (green square). NMDA-spike generation (gray voltage trace) at the compartment site through burst inputs to local AMPA+NMDA synapses (green inputs), with AMPA (blue) and GABA (red) background inputs spread throughout the subtree. Reductions shown without rescaling (blue, dash-dotted), with the analytical single-site rescaling rule (red, full) and the numerical multi-site rule (orange, dashed). (I) Error in NMDA-spike threshold for the three cases in H. (J) Dependence of the error in NMDA-spike threshold on the factor $Δ⁢z⁢g$, with $Δ⁢z$ the average input resistance difference between synapse sites and the compartment and $g$ the average synaptic conductance.

For a single, current-based synapse, shifted from its original location on the ablated branch to the next proximal compartment, we analytically compute the weight-rescale factor and find $\beta_{curr}=z_{c⁢s}/z_{c⁢c}$, with $z_{c⁢s}$ the transfer resistance from synapse site $s$ to compartment site $c$ and $z_{c⁢c}$ the input resistance at $c$. Since $z_{c⁢s}<z_{c⁢c}$ (Koch, 1998), the weight-rescale factor weakens the shifted synapse, so that it matches the attenuation of its distal counterpart. Nevertheless, when $s$ is located more distally on the same branch or subtree as $c$, the transfer resistance $z_{c⁢s}$ is often close to the input resistance $z_{c⁢c}$ (Figure 1—figure supplement 1E). Thus, $\beta_{curr}$ is often close to one, and hence negligible (Figure 4B,C). For a conductance-based synapse, rescaling weights by $\beta_{curr}$ does not accurately fit the full model (Figure 4B). We decompose the synaptic conductance $g⁢(t)$ as $g+\delta⁢g⁢(t)$, with $g$ the temporal average and $\delta⁢g⁢(t)$ the fluctuations around $g$. We then analytically compute (see Materials and methods — Synaptic weight-rescale factors) that the weight-rescale factor for a conductance-based synapse

$$
\beta_{cond}=\frac{1}{1+Δ⁢z⁢g}
$$

recovers the full model’s voltage if

$$
Δ⁢z⁢\delta⁢g⁢(t)≪1+Δ⁢z⁢g,
$$

where $Δ⁢z=z_{s⁢s}-z_{c⁢c}$ is the difference between input resistance $z_{s⁢s}$ at the original synapse site $s$ and input resistance $z_{c⁢c}$ at the nearest proximal compartment site $c$. Multiplying the synaptic weights by $\beta_{cond}$ weakens the synapse so that it matches the shunt effect of its distal counterpart, and so that the voltage at all compartments more proximal than $c$ and in their respective side branches is reproduced (Figure 4D).

If $s$ and $c$ are close, $Δz$ is small and (Equation 9) is satisfied for plausible conductance fluctuations. Thus, shifting the synapse to the next proximal compartment keeps the voltage response intact. If the separation between $s$ and $c$ increases, $Δz$ increases accordingly, and the magnitude of tolerated conductance fluctuations shrinks (Equation 9). Thus, for a given magnitude of $\delta⁢g⁢(t)$, it is possible that a thick branch can be removed, but not a thin branch, as the input resistance increase in the former is much more gradual than in the latter. Nevertheless, (Equation 9) suggests that even for large $Δz$ the full model’s voltage can be recovered by downscaling synaptic weight by $\beta_{cond}$, but only if $\delta⁢g⁢(t)≪g$. A tonic level of AMPA and/or GABA activation, as in the high-conductance state (Destexhe et al., 2003), can implement this input condition. For NMDA synapses, this input condition does not hold, as NMDA spikes arise through a strong, transient conductance increase. However, when a cluster of such synapses – to be moved to a proximal site – is considered in isolation, a workaround can be found by applying constant rescale factors not just to synaptic weight, but also to threshold and width of the Mg2+ block, as well as to the reversal (see Materials and methods — Synaptic weight-rescale factors). These factors recover NMDA-spike shape (Figure 4E) and threshold (Figure 4F) when the cluster is moved to from $s$ to $c$.

Our analytical weight-rescale factor $\beta_{cond}$ treated reductions where a single site $s$ was moved to $c$. We consider now the ablation of a whole subtree and the shift of all its synapses to $c$ (Figure 4G). In our simulations, we distributed 100 AMPA and 100 GABA synapses on the to be ablated subtree, and activated them with a Poisson process with fixed rate. We studied how the reduction influenced the local integrative properties at the intact compartment $c$. As a proxy for those integrative properties, we checked the shape of the waveform elicited by activating AMPA+NMDA synapses at $c$ in a short burst (Figure 4H), and we quantified the threshold for NMDA-spike generation. We found that neither shape nor threshold were preserved by the analytical weight-rescale factors $\beta_{cond}$, derived for the case where only a single input site is present on the subtree. We numerically extend the derivation of the weight-rescale factors to multi-site inputs (see Materials and methods – Synaptic weight-rescale factors). These extended weight-rescale factors $\beta_{cond}^{ext}$ reproduced local voltage (Figure 4H) and NMDA-spike threshold (Figure 4I). We also investigate whether $\beta_{cond}^{ext}$ can still be conceptualized as depending on $Δ⁢z_{avg}⁢g_{avg}$ – the product between (1) a difference in average input resistance between synapses on the to be ablated subtree and the compartment site and (2) the average conductance load exerted by those synapses. To do so, we activated the 100 AMPA and 100 GABA synapses on the to be ablated subtree at a wide range of input conditions (see Materials and methods – Simulation-specific parameters), and measured the error in threshold for NMDA-spike generation at $c$. We found that this error depended strongly on $Δ⁢z_{avg}⁢g_{avg}$ and remained small for $Δ⁢z_{avg}⁢g_{avg}≪1$ (Figure 4J).

In conclusion, we can now assess whether given spatial synapse motifs on branches or subtrees admit simplification by shifting the synapses to the nearest proximal compartment site and ablating the branch or subtree. We find that reduction in this sense is possible for any motif if fluctuations are small, so that $\delta⁢g⁢(t)≪g$, by applying temporally constant weight-rescale factors. Otherwise, the synapses must be located sufficiently closely to the compartment site, so that $Δz$ is small and that $Δ⁢z⁢\delta⁢g$ remains below $1+Δ⁢z⁢g$ for all relevant activation levels.

### Active and passive reduced dendrites under synaptic bombardment

We next investigated how many compartments are needed to reproduce somatic and dendritic responses under a synaptic bombardment and quantified the contribution of active dendritic Na+, Ca2+, and K+ channels. We mimicked the in vivo state in the basal dendrites of the L2/3 pyramid by distributing 200 AMPA and 200 GABA synapses receiving Poisson inputs and 20 clusters of AMPA+NMDA synapses receiving bursts of inputs (Figure 5A). We sampled 10 different sets of meta-parameters governing synaptic activation (Poisson and burst rates and synaptic weights, see Materials and methods — Simulation-specific parameters), resulting in output spike rates between 0 and 8 Hz (Figure 5B). We derived reduced models, once based on the full model with all active channels (‘active reduced dendrite’ in Figure 5C) and once based on the passified full model (‘passive reduced dendrite’ in Figure 5C). We distributed increasing numbers of compartment sites on the basal branches and measured somatic and dendritic voltage responses for the active full model and for the reduced models with active and passive dendrites (Figure 5C, Figure 5—figure supplement 1 for dendritic traces). Spike coincidence (Figure 5D), subthreshold somatic voltage error (Figure 5E), and dendritic voltage error (Figure 5F) showed a significant improvement when compartment numbers increased from 0 (point-neuron – top row in Figure 5C) to 2 per 100 μm. In the presence of active channels, the error decreases until up to three compartments per 100 μm (Figure 5E,F). Spike coincidence factors were consistently ∼10% higher than in the passive case (Figure 5D).

![Figure 5.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig5-v1.jpg)

**Figure 5.:** (A) AMPA and GABA synapses, and AMPA+NMDA synapse clusters are spread randomly throughout the basal dendrites of the L2/3 pyramid (inset). AMPA and GABA synapses receive Poisson inputs and AMPA+NMDA synapses receive bursting input (right). (B) Output spike rates of the full model for 10 different input configurations. (C) Reductions with increasing numbers of compartment sites along the basal dendrites (left). Somatic voltage traces and spike times for the full model (gray), for a reduction with passive dendrites (middle, blue) and a reduction with active dendrites (right, orange). (D–F) Spike coincidence factors (D), relative somatic voltage errors (E) and relative dendritic voltage errors (F) for reductions with increasing numbers of compartments, and with passive (blue) and active dendrites (orange), averaged over all 10 input configurations. Relative voltage errors are computed as in Figure 2C,D.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Voltage in the full model (gray) at a dendritic site (red hexagon on the left), together with the voltage in the closest compartment of the reduced model with passive dendrite (middle, blue) and of the reduced model with active dendrites (left, orange) for the same simulations as in Figure 5.

### Fitting reduced models directly to experimental data

Traditionally, creating a morphological neuron model involves a reconstruction of the morphology and an evolutionary fit of the electrical parameters (Hay et al., 2011; Almog and Korngreen, 2014; Van Geit et al., 2016). Our method allows skipping these resource-intensive steps (Figure 6A). We adapt our method to a common experimental paradigm where hyper- and depolarizing current steps are injected under applications of various ion-channel blockers (Marti Mengual et al., 2020). We extract resistance matrices and holding potentials from voltage step amplitudes (Figure 6B), and the time scale of the largest eigenmode from the average voltage decay back to rest (Figure 6C). If the modeling goal is a reduced model, the traditional reconstruction and subsequent reduction both introduce errors (Figure 6D). Thus, we find that while our reduction of the full model is faithful within an expected accuracy margin (Figure 6E), fitting a reduced model directly to the experimental traces is more accurate (Figure 6F).

![Figure 6.](https://cdn.elifesciences.org/articles/60936/elife-60936-fig6-v1.jpg)

**Figure 6.:** (A) Comparison between the traditional neuron model creation paradigm (morphological reconstruction and evolutionary fit, possibly followed by a reduction), and the proposed direct experiment to reduced dendrite model paradigm. (B) Resistance matrices and holding potentials are extracted from the response amplitude to hyper- and depolarizing current step inputs, here measured once under application of an h-channel antagonist and once under control conditions. (C) Time scale of largest eigenmode is extracted from average decay back to the resting membrane potential. (D) Combined root mean square voltage error $R⁢M⁢S⁢E⁢(v)=\sqrt{Avg⁢(v_{full}-v_{reduced})^{2}}$ of full model (gray) – fitted to current step data through an evolutionary algorithm, of the reduction of the full model (red), and of the direct fit of the reduced model to the data (brown). (E) Experimentally recorded traces (gray), traces from the full reconstruction (black), and its reduction (green and purple, dashed). (F) Experimentally recorded traces (gray) and traces from the directly fitted reduced model (green and purple, dashed).

## Discussion

We have presented a flexible yet accurate method to construct reduced neuron models from experimental data and morphological reconstructions. The method consists of linear parameter fits at holding potentials that are informative for the full non-linear dynamics. First, we derive leak and coupling conductances from the passified version of the full model. Second, we fit the maximal conductances of the active ion-channels, so that the reduced model, at various holding potentials, responds similarly to input perturbations as the full model. Third, we fit the capacitances to reproduce spatio-temporal integrative properties. Finally, we ensure that resting membrane potentials in the full and reduced models match. The resulting method can be adapted to a wide variety of use cases.

A fundamental use case is deriving reduced models that retain specific elements of the dendritic computational repertoire, to explore how those dendritic computations may improve network function. To that purpose, one can apply our method to compartments placed at input sites needed for the computation of interest. For instance, if a computation requires independent computational subunits (Poirazi et al., 2003b; Kastellakis et al., 2016), one would place compartments at the dendritic tips. If one wants to modulate co-operativity of excitatory inputs at distal sites, one would place compartments with shunting conductances at the bifurcations between the distal sites (Wybo et al., 2019). Detecting input sequences (Branco and Häusser, 2010) or implementing a dendritic integration gradient (Branco and Häusser, 2011) would require placing two or more compartments along the branches of interest. For many of these computations, a passive morphology with non-linear (NMDA) synapses suffices. Furthermore, our method can be combined with abstract models of AP generation (Pozzorini et al., 2013; Pozzorini et al., 2015).

A second use case is constructing models directly from electro-physiological recordings. Our method avoids the labor-intensive detour of reconstructing the morphology and optimizing model parameters with an evolutionary algorithm (Marti Mengual et al., 2020). In combination with advances in voltage-sensitive dye imaging, our method may thus form the basis of a high-throughput experiment-to-model paradigm.

A third use case is elucidating the effective complexity of a given dendritic tree. We assessed whether afferent spatial input motifs could be simplified by removing a branch or subtree and grouping the affected synapses at the next proximal compartment. We found that such simplification is possible when the input resistance of the affected synapse sites is close to the input resistance of the compartment site. If this condition does not hold, the simplification can still proceed if conductance fluctuations are small compared to the average conductance magnitude, but not otherwise. What is the simplest model for a given dendritic tree that captures its full computational repertoire? We find that spike coincidence and subthreshold voltage metrics reach satisfying accuracy at, but do not improve much beyond ∼3 compartments per 100 μm. Further research is required to tease apart mere numerical errors from potentially missed computational features.

The process of simplifying complex dynamical systems, such as morphological neuron models, is inherently approximate. Due to the vast variety of morphologies, voltage-gated ion-channel configurations and input patterns, it is beyond the scope of any single paper to give an exhaustive overview of possible inaccuracies. Rather, we propose three lines of inquiry if a reduction fails to reproduce a particular response pattern. First, we suggest checking the discrepancy between the impedance kernels $z⁢(t)$ of the full and reduced models. Often, response mismatches arise from slight inaccuracies in how ion-channel dynamics are integrated by the passive system (Figure 3A–C). Second, we suggest assessing to what degree afferent spatial input motifs, present in the full model, are simplified, and whether that simplification still admits a sufficient accuracy in reproducing local voltage-dependent responses, such as NMDA spikes (Figure 4). Finally, we suggest checking whether the distribution of compartments on the morphology admits ion channel dynamics that are sufficiently rich to reproduce the response characteristic in question. To illustrate these lines of inquiry, we have further simplified the L5 pyramid to five compartments, by omitting the compartments in the apical trunk (Figure 3—figure supplement 1A vs Figure 3J). This reduction results a change in AP shape, and in a failure to elicit AP bursts through the pairing of a somatic and a dendritic input, even though a Ca2+ spike can still be elicited (Figure 3—figure supplement 1B). Likely, the change in AP shape can be traced back to the difference in the somatic input impedance kernels (Figure 3—figure supplement 1C), while the failure to elicit an AP burst may be due to insufficient Na+-driven cross-talk between soma and apical tuft.

Computational tools have played a key role in neuroscience. Take NEURON (Carnevale and Hines, 2004), which accelerated our understanding of morphological neurons, or NEST (Gewaltig and Diesmann, 2007), which enabled simulation of large-scale spiking point-neuron networks. We have implemented a Python toolbox that automatizes the simplification process (NEural Analysis Toolkit – NEAT – https://github.com/unibe-cns/NEAT; copy archived at swh:1:rev:1cb15f36aa0a764105348541d046c85ef38e21ee). The toolbox reads any morphology in the standard ‘.swc’ format (Ascoli, 2006) and returns the parameters of the reduced models, while also providing tools to export the models to NEURON (Carnevale and Hines, 2004).

Our method and toolbox fill a void in between the extremes of modeling large-scale networks with abstract models and modeling single cells in all their detail. By enabling the efficient systematic derivation of simplified neurons, amenable to simulation at the network level, our work bridges the gap between two branches of neuroscience that historically have remained separate.

## Materials and methods

### Morpohologies

Three exemplar cell models were used for the analysis: a cortical L2/3 pyramidal cell (Branco and Häusser, 2010; Figure 2D), a cortical L5 pyramidal cell (Hay et al., 2011; Figure 2E), and a cerebellar Purkinje cell (Figure 2F). The latter morphology was retrieved from the NeuroMorpho.org repository (Ascoli, 2006) and the two others from the ModelDB repository (McDougal et al., 2017).

### Physiological parameters

In our passive models, physiological parameters were set according to Major et al., 2008: the equilibrium potential was $-75⁢mV$, the membrane conductance $100⁢\mu⁢S/cm^{2}$, the capacitance $0.8⁢\mu⁢F/cm^{2}$, and the intracellular resistivity $100⁢Ω⋅cm$. For the active models, we took ion channels and parameters according to Branco and Häusser, 2010 for the L2/3 pyramid, Hay et al., 2011 for the L5 pyramid, and Miyasho et al., 2001 for the Purkinje cell.

AMPA and GABA synaptic input currents were implemented as the product of a conductance profile, here a double exponential (Rotter and Diesmann, 1999), with a driving force:

$$
i_{syn}=g⁢(e_{r}-v).
$$

AMPA rise resp. decay times were $\tau_{r}=0.2⁢ms$, $\tau_{d}=3⁢ms$ and AMPA reversal potential was $e=0⁢mV$. For GABA, we used $\tau_{r}=0.2⁢ms$, $\tau_{d}=10⁢ms$, and $e=-80⁢mV$. NMDA currents (Jahr and Stevens, 1990a) had the form:

$$
i_{syn}=g⁢\sigma⁢(v)⁢(e-v)
$$

with rise resp. decay time $\tau_{r}=0.2⁢ms$, $\tau_{d}=43⁢ms$, and $e=0⁢mV$, while $\sigma⁢(v)$, modeling the channel’s magnesium block, had the form (Behabadi and Mel, 2014):

$$
\sigma⁢(v)=\frac{1}{1+0.3⁢e^{-0.1⁢v}}.
$$

The ‘conductance’ of an AMPA or GABA synapse signifies the maximum value of its conductance window. For an AMPA+NMDA synapse, the conductance is the maximal value of the AMPA conductance window, and the conductance of the NMDA component is determined by multiplying the AMPA conductance value with an NMDA ratio $R_{NMDA}$, set to be either 2 or 3.

### Biophysical models

We used the NEURON simulator (Carnevale and Hines, 2004) to implement biophysical and reduced models. For the biophysical models, the distance step was set according the lambda rule (Carnevale and Hines, 2004) or smaller.

### Quasi-active channels

A voltage-dependent ion channel described by the Hodgkin–Huxley formalism can in general be written as follows:

$$
i=g¯⁢f⁢(y_{1},…,y_{K})⁢(v-e),y˙_{k}=g_{k}⁢(y_{k},v)⁢for ⁢k=1,…,K,
$$

where $g¯$ is the channel’s maximal conductance, $e$ its reversal potential, $y_{1},…,y_{K}$ its state variables, $f(_{◼})$ a function that depends on the channel type (e.g. for a typical sodium channel $f⁢(m,h)=m^{3}⁢h$), and $g_{k}⁢(y_{k},v)$ ($k=1,…,K$) the functions governing state-variable activation ($g_{k}⁢(y_{k},v)$ can usually be written as $(y_{∞⁢k}⁢(v)-y_{k})/\tau_{k}⁢(v)$ with $y_{∞⁢k}⁢(v)$ the state-variable’s activation and $\tau_{k}⁢(v)$ its time scale). To obtain the channel’s quasi-active approximation (Mauro et al., 1970; Koch and Poggio, 1985) around a holding potential $v_{h}$ and a state variable expansion point $y_{1}^{0},…,y_{K}^{0}$, we linearize (Equation 13):

$$
i_{lin}=g¯[\sumk=1K\frac{∂f}{∂y_{k}}(y_{1}^{0},…,y_{K}^{0})(v_{h}−e)(y_{k}−y_{k}^{0})+f(y_{1}^{0},…,y_{K}^{0})(v−v_{h})],y˙_{k}=\frac{∂g_{k}}{∂y_{k}}(y_{k}^{0},v_{h})(y_{k}−y_{k}^{0})+\frac{∂g_{k}}{∂v}(y_{k}^{0},v_{h})(v−v_{h})for k=1,…,K.
$$

To obtain the zero-frequency contribution of (Equation 14) to the resistance and conductance matrices, we set $y˙_{k}=0$, solve the linearized state-variable equations for $(y_{k}-y_{k}^{0})$, and substitute the result in $i_{lin}$:

$$
i_{lin}=g¯⁢[-\sumk=1K\frac{\frac{\partial⁡f}{\partial⁡y_{k}}⁢\frac{\partial⁡g_{k}}{\partial⁡v}}{\frac{\partial⁡g_{k}}{\partial⁡y_{k}}}⁢(v_{h}-e)+f⁢(y_{1}^{0},…,y_{K}^{0})]⁢(v-v_{h}).
$$

Introducing a shorthand for the factor in square brackets

$$
l⁢(v_{h})=-\sumk=1K\frac{\frac{\partial⁡f}{\partial⁡y_{k}}⁢\frac{\partial⁡g_{k}}{\partial⁡v}}{\frac{\partial⁡g_{k}}{\partial⁡y_{k}}}⁢(v_{h}-e)+f⁢(y_{1}^{0},…,y_{K}^{0})
$$

results in the linearized ion-channel current as described in (Equation 2).

### The impedance matrix

The voltage response $\delta⁢v_{x}⁢(t)$ at a location $x$ along the neuron to an input current perturbation $\delta⁢i_{x^{′}}⁢(t)$ at location $x^{′}$ can be computed as the convolution of an impedance kernel with $\delta⁢i_{x^{′}}⁢(t)$:

$$
\delta⁢v_{x}⁢(t)=z_{x⁢x^{′}}⁢(t)∗\delta⁢i_{x^{′}}⁢(t).
$$

The impedance kernel itself can be computed in the frequency domain from the quasi-active cable equation using Koch’s algorithm (Koch and Poggio, 1985). We may assume any a priori arbitrary set of holding potentials and ion-channel state variables to compute the quasi-active expansion (with Koch’s algorithm, the only constraint is that their distribution is uniform for each cylindrical segment). For our purpose, spatially uniform holding potentials and state-variable expansion points suffice. For a steady-state current $\delta⁢i_{x^{′}}$, (Equation 17) simplifies to:

$$
\delta⁢v_{x}=z_{x⁢x^{′}}⁢\delta⁢i_{x^{′}},
$$

where we term $z_{x⁢x^{′}}=\int_{0}^{∞}dt⁢z_{x⁢x^{′}}⁢(t)$ the ‘resistance’ ($z_{x⁢x^{′}}$ is also known as the input resistance if $x=x^{′}$ or the transfer resistance if $x\neqx^{′}$). For passive membranes, impedance kernels can also be computed as a sum of exponentials (Holmes et al., 1992; Major et al., 1993):

$$
z_{x⁢x^{′}}⁢(t)=\suml=0∞ϕ_{l}⁢(x)⁢ϕ_{l}⁢(x^{′})⁢e^{-\frac{t}{\tau_{l}}},
$$

where we adopt the ordering $\tau_{0}\geq\tau_{1}\geq\tau_{2}\geq…$ Essentially, this infinite sum can be thought of as the generalization of the eigenmodes for linear dynamical systems (Strogatz, 2000) to partial differential equations.

When a current perturbation is applied at multiple sites along the neuron (we write $\delta⁢𝐢⁢(t)=(\delta⁢i_{1}⁢(t),…,\delta⁢i_{n}⁢(t))$), we obtain the voltage response $\delta⁢𝐯⁢(t)=(\delta⁢v_{1}⁢(t),…,\delta⁢v_{n}⁢(t))$ at those sites from:

$$
\delta⁢𝐯⁢(t)=Z⁢(t)∗\delta⁢𝐢⁢(t),
$$

with $Z⁢(t)$ the matrix of impedance kernels (the $i⁢j$’th elements of this matrix is the impedance kernel between sites $i$ and $j$). In the steady-state case, we call $Z$ the resistance matrix.

### Compartmental models

The voltage $v_{i}$ in a compartment $i$, connected to a set $𝒩_{i}$ of nearest neighbor compartments, and with a set of ion channels $ℐ_{i}$, is given by

$$
c_{i}⁢v˙_{i}+g_{L⁢i}⁢(v_{i}-e_{L⁢i})+\sumn\in𝒩_{i}g_{C,i⁢n}⁢(v_{i}-v_{n})+\sumd\inℐ_{i}i_{d⁢i}=i_{i},
$$

where $c_{i}$ is the capacitance of compartment $i$, $g_{L⁢i}$ resp. $e_{L⁢i}$ its leak conductance resp. reversal, $g_{C⁢i⁢n}$ its coupling conductance to the neighboring compartment $n$, $i_{d⁢i}$ the ion channel current (Equation 13) of channel $d$ in compartment $i$ and $i_{i}$ an arbitrary input current to compartment $i$.

### The conductance matrix

To obtain the conductance matrix of the compartmental model for steady-state inputs, (Equation 21) is linearized around a certain holding potential $v_{h}$ and we assume that $v˙_{i}=0$. After absorbing all constant terms into $i_{i}$, we obtain

$$
g_{L⁢i}⁢\delta⁢v_{i}+\sumn\in𝒩_{i}g_{C,i⁢n}⁢(\delta⁢v_{i}-\delta⁢v_{n})+\sumd\inℐ_{i}g¯_{d⁢i}⁢l_{d}⁢(v_{h})⁢\delta⁢v_{i}=i_{i},
$$

where $\delta⁢v_{i}=v_{i}-v_{h}$, where $g¯_{d⁢i}⁢l_{d}⁢(v_{h})$ is the linearized ion-channel current (Equation 15), and where we used the notation (Equation 16). Summarizing the voltage responses for each compartment in a vector $\delta⁢𝐯=(\delta⁢v_{1},…,\delta⁢v_{N})$, (Equation 22) for each compartment $i=1,…,N$ can be recast as a matrix equation, yielding (Equation 3).

### Simplification method details

For any given set of $M$ sites on the morphology, we construct a simplified compartmental model whose connection structure follows a tree graph defined by the original morphology (Figure 1A). We do not allow triplet connections (e.g. sites 1–2, sites 2–3, and sites 3–1 all mutually connected) in our reduced models. Hence, to obtain accurate results, it is necessary to extend the original set of $M$ sites with the $B$ bifurcation points that lie in between (Figure 1—figure supplement 1C). With these $N=M+B$ sites, we thus define a tree graph that provides the scaffold for our fit (and our reduced model).

The fitting process proceeds in four steps: (1) fit the passive leak and coupling conductances, (2) fit the capacitances, (3) fit the maximal conductances of the ion channels, and (4) fit the reversal potentials to obtain the same resting membrane potentials as in the biophysical model. The order of steps 2 and 3 is interchangeable, but not of the other steps. We describe these steps in detail below:

### Synaptic weight-rescale factors

To be able to analytically compute the weight-rescale factor when a synapse with temporal conductance $g⁢(t)$ is moved from its original site $s$ to a compartment site $c$ on a dendritic tree, we use the steady-state approximation (Equation 18). Because we implicitly convolve the rescaled synaptic current with the temporal input impedance kernel $z_{c⁢c}⁢(t)$ at the compartment site when we simulate the reduced model, the weight-rescale factor still yields accurate temporal voltage responses (Figure 4B,E,H). In the original configuration, we have

$$
⟮v_{c}v_{s}⟯=⟮z_{cc}z_{cs}z_{sc}z_{ss}⟯⟮i_{c}g(t)(e−v_{s})⟯,
$$

with $i_{c}$ an arbitrary current at the compartment site and $g$ resp. $e$ the synaptic conductance resp. reversal. Eliminating $v_{s}$ from this yields

$$
v_{c}=\frac{(z_{c⁢c}+(z_{c⁢c}⁢z_{s⁢s}-z_{c⁢s}⁢z_{s⁢c})⁢g⁢(t))⁢i_{c}+z_{c⁢s}⁢g⁢(t)⁢e}{1+z_{s⁢s}⁢g⁢(t)}.
$$

In the reduced configuration we have:

$$
v_{c}^{′}=z_{c⁢c}⁢(i_{c}+\beta⁢g⁢(t)⁢(e-v_{c}^{′})).
$$

From requiring that $v_{c}=v_{c}^{′}$, $\beta$ is found as follows:

$$
\beta=\frac{z_{c⁢s}}{z_{c⁢c}}⁢\frac{z_{c⁢s}⁢i_{c}-e}{[1+(z_{s⁢s}-\frac{z_{c⁢s}^{2}}{z_{c⁢c}})⁢g⁢(t)]⁢z_{c⁢c}⁢i_{c}-[1+(z_{s⁢s}-z_{c⁢s})⁢g⁢(t)]⁢e}.
$$

When $z_{c⁢c}≈z_{c⁢s}$, which is true in basal dendrites and a reasonable approximation in many apical dendrites if $c$ is on the direct path from $s$ to the soma, (Equation 31) reduces to

$$
\beta=\frac{1}{1+(z_{s⁢s}-z_{c⁢c})⁢g⁢(t)}.
$$

The weight-rescale factor hence depends on time. Decomposing the time-varying $g⁢(t)$ into $g+\delta⁢g⁢(t)$, with $g$ the temporal average and $\delta⁢g⁢(t)$ the fluctuations around $g$, we find (Equation 8) and (Equation 9) from requiring that the denominator of (Equation 32) be constant in time:

$$
\beta=\frac{1}{1+Δzg+Δz\deltag(t)}=\frac{1}{(1+Δzg)(1+\frac{Δz\deltag(t)}{1+Δzg})}≈\frac{1}{1+Δzg}if\frac{Δz\deltag(t)}{1+Δzg}≪1
$$

where $Δ⁢z=z_{s⁢s}-z_{c⁢c}$.

In the case of an NMDA synapse, the conductance depends sigmoidally on the local voltage. Using scale factor (Equation 8), we obtain for the rescaled synaptic current at the compartment site:

$$
i_{s}^{′}=\frac{g⁢\sigma⁢(v_{s};v_{T},Δ_{v})}{1+(z_{s⁢s}-z_{c⁢c})⁢g⁢\sigma⁢(v_{s};v_{T},Δ_{v})}⁢(e-v_{c}).
$$

This current still depends on the voltage at the synaptic site $v_{s}$ in the sigmoid. A current at the compartment site that causes a voltage $v_{c}$ there would have caused a voltage

$$
v_{s}=v_{e⁢q}+\frac{z_{s⁢s}}{z_{c⁢c}}⁢(v_{c}-v_{e⁢q})
$$

if it was placed at the synapse site. Hence, to retain the same activation level of the NMDA synapse, we substitute (Equation 35) in the sigmoid. This amounts to a change in threshold and width of the sigmoid:

$$
\sigma⁢(v_{s};v_{T},Δ_{v})⟶\sigma⁢(v_{e⁢q}+\frac{z_{s⁢s}}{z_{c⁢c}}⁢(v_{c}-v_{e⁢q});v_{T},Δ_{v})=\sigma⁢(v_{c};\frac{z_{c⁢c}}{z_{s⁢s}}⁢(v_{T}+v_{e⁢q})-v_{e⁢q},\frac{z_{c⁢c}}{z_{s⁢s}}⁢Δ_{v}).
$$

We will denote this modified sigmoid as $\sigma^{′}⁢(v)$. We have not yet succeeded in reformulating (Equation 34) by only rescaling its parameters with constant rescale factors, since $1/(1+(z_{s⁢s}-z_{c⁢c})⁢g⁢\sigma^{′}⁢(v_{c}))$ still depends on time through its dependence on $v_{c}$. To obtain constant rescale factors, we substitute the (Equation 34) in (Equation 17):

$$
v_{c}-v_{e⁢q}=z_{c⁢c}⁢(t)∗[\frac{g⁢\sigma^{′}⁢(v_{c})}{1+(z_{s⁢s}-z_{c⁢c})⁢g⁢\sigma^{′}⁢(v_{c})}⁢(e-v_{c})].
$$

Here, the current in square brackets is the synaptic current. The convolution to obtain $v_{c}$ is implemented implicitly by the compartmental model. We then approximately eliminate the denominator: 

$$
v_{c}-v_{e⁢q}≈z_{c⁢c}⁢(t)∗[g⁢\sigma^{′}⁢(v_{c})⁢(e-v_{c})-\frac{z_{s⁢s}-z_{c⁢c}}{z_{c⁢c}}⁢g⁢\sigma^{′}⁢(v_{c})⁢(v_{c}-v_{e⁢q})]
$$

to obtain for the synaptic current: 

$$
i_{s}^{′}=\frac{z_{s⁢s}}{z_{c⁢c}}⁢g⁢\sigma^{′}⁢(v_{c})⁢(\frac{z_{c⁢c}}{z_{s⁢s}}⁢(e-v_{e⁢q})+v_{e⁢q}-v_{c}).
$$

We thus find that the synaptic weight is rescaled by a constant factor $\frac{z_{s⁢s}}{z_{c⁢c}}$ and the reversal potential is shifted to $\frac{z_{c⁢c}}{z_{s⁢s}}⁢(e-v_{e⁢q})+v_{e⁢q}$. Note however that this reduction relies on two key assumptions: that there are no other inputs to the dendritic tree and that there are no fluctuations in $v_{c}$ generated by input currents not at site $s$, as this could lead to spurious activation or suppression of $\sigma^{′}⁢(v_{c})$.

Suppose now we shift $M$ conductance synapses to $N$ compartments. Let $𝐯=(v_{1},…,v_{N},v_{N+1},…,v_{N+M})$ be the vector with $K=N+M$ components containing the voltages at the $N$ compartment sites and at the $M$ synapse sites. Similarly $𝐠=(0,…,0,g_{1},…,g_{M})$ is a vector of $K$ components containing $N$ zeros and the $M$ synaptic conductances, while $𝐞=(0,…,0,e_{1},…,e_{M})$ contains the synaptic reversals. In matrix form, (Equation 18) for this system becomes:

$$
𝐯=Z⁢diag⁢(𝐠)⁢(𝐞-𝐯),
$$

and its solution:

$$
𝐯=Γ⁢𝐞,
$$

with $Γ$ a matrix given by:

$$
Γ=(I+Zdiag(g))^{−1}Zdiag(g).
$$

In the reduced setting, we assign each synapse to one compartment site (a reasonable choice could be the closest site). We introduce an $N\timesM$ compartment assignment matrix $C$ where an element $c_{n⁢m}$ is 1 if synapse $m$ is assigned to compartment $n$ and zero otherwise. We further introduce a vector of reduced compartment voltages $𝐯^{′}=(v_{1}^{′},…,v_{N}^{′})$, a vector of rescaled synaptic conductances $𝐠_{\beta}^{′}=(\beta_{1}⁢g_{1},…,\beta_{M}⁢g_{M})$ and a vector of synaptic reversals $𝐞^{′}=(e_{1},…,e_{M})$. In the reduced model, voltages are obtained from:

$$
𝐯^{′}=Z⁢C⁢diag⁢(𝐠_{\beta}^{′})⁢(𝐞^{′}-C^{T}⁢𝐯^{′}).
$$

We then require that $𝐯_{N}=𝐯^{′}$, with $𝐯_{N}$ a vector containing the first $N$ components of $𝐯$. We denote by $Γ_{N⁢M}$ the matrix containing the first $N$ rows and last $M$ columns of $Γ$, and note that we can write (Equation 41) as $𝐯_{N}=Γ_{N⁢M}⁢𝐞^{′}$. Substituting this in (Equation 43) yields:

$$
Γ_{N⁢M}⁢𝐞^{′}=Z⁢C⁢diag⁢(𝐠_{\beta}^{′})⁢(𝐞^{′}-C^{T}⁢Γ_{N⁢M}⁢𝐞^{′}).
$$

We then fit the parameters $\beta_{1},…,\beta_{M}$ (here absorbed in $𝐠_{\beta}^{′}$) in the least-square sense from:

$$
Γ_{NM}=ZCdiag(g_{\beta}^{′})(I−C^{T}Γ_{NM}),
$$

which again is a linear fit.

### Experimental recordings

Coronal slices (300 μm thick) containing the anterior cingulate cortex (ACC) were prepared from 10 to 12 week old C57BL/6 mice using a vibratome on a block angled at 15 degree to the horizontal in ice-cold oxygenated artificial cerebral spinal fluid (ACSF) and then maintained in the same solution at 37°C for 15–120 min. Normal ACSF contained (in mM) NaCl, 125; NaHCO3, 25; KCl, 2.5; NaH2PO4, 1.25; MgCl2, 1; glucose, 25; CaCl2, 2; pH 7.4. Individual neurons were visualized with a Nikon Eclipse E600FN fit with a combination of oblique infrared illumination optics and epifluorescence, the switch between optical configurations was software-triggered (Sieber et al., 2013). Pyramidal neurons were selected on the clearly visible, proximal apical dendrite. This selection criterion resulted in a homogeneous population of pyramidal neurons based on their firing properties and shape of the AP (i.e. all cells possessed a prominent after-hyperpolarization and a significant sag ratio at the soma). Dual somatic and dendritic whole-cell patch-clamp recordings were performed from identified L5 pyramidal neurons in the rostroventral ACC (1.1–1.4 mm below the pial surface, 1.1–0.2 mm rostral to the Bregma) using two Dagan BVC-700. During the experiments, the external recording solution (normal ACSF) was supplemented with 0.5 mM CNQX and 0.5 mM AP-5 to block excitatory glutamatergic synaptic transmission. Experiments were performed at physiological temperatures between 34–37°C. Whole-cell recording pipettes (somatic, 4 to 8 MΩ; dendritic, 12 to 32 MΩ), were pulled from borosilicate glass. The internal pipette solution consisted of (in mM) potassium gluconate, 135; KCl, 7; Hepes, 10; Na2-phosphocreatine, 10; Mg-ATP, 4; GTP, 0.3; 0.2% biocytin; pH 7.2 (with KOH); 291–293 mosmol l−1. For somatic recordings, 10–20 μm Alexa 594 was added to the intracellular solution: first, the soma was patched (whole-cell configuration by negative pressure); after 5 min of intracellular perfusion, the fluorescent signal allowed for the clear identification of the apical dendritic tree, then the dendritic region of interest was patched with a smaller pipette. Compensation was performed in current clamp mode by recovering the fast, initial square voltage response to a hyperpolarizing current injection (−100 pA, 50 ms). First the pipette capacitance was compensated to the level that the voltage response showed an immediate voltage drop due to the series resistance of the pipette that was adjusted subsequently. Compensation of dendritic series resistance yielded values between 30 and 60 MΩ for pipettes with a resistance between 17 and 21 MΩ. On average, series resistance was 2.3 times larger than the pipette resistance. Series resistance of both somatic and dendritic recording electrodes was monitored frequently, and experiments were terminated when proper compensation was not possible anymore (i.e. reached values of more than four times the pipette resistance). All cells were filled with biocytin, and PFA-fixed slices were developed with the avidin–biotin-peroxidase method for Neurolucida reconstructions (Egger et al., 2008). Data analysis was performed using Igor software (Wavemetrics) and Excel (Microsoft).

### Simulation-specific parameters

#### Parameters Figure 2

For the sequence detection (Figure 1f), the synapse model is as in Branco and Häusser, 2010. The maximal conductance of the AMPA component is $g¯_{AMPA}=0.5$ nS and its conductance window shape given by an alpha function (Rotter and Diesmann, 1999) with a time scale of 2 ms. The NMDA component is given by a kinetic model (Destexhe et al., 1998) with $g¯_{NMDA}=8$ nS and external magnesium concentration of 1 mM, and receives an exponentially decaying ($\tau=.5$ ms) neurotransmitter concentration with amplitude of 5 mM. For the input-order detection (Figure 1G), AMPA synapses 1 and 2 use the standard parameters and have respective maximal conductances of 10 and 5 nS. For the simulation with the L5 pyramidal cell, excitatory synapses have AMPA+NMDA components with $R_{NMDA}=2$ and $g¯=3$ nS. For inhibitory synapses, $g¯=2$ nS. In the Purkinje cell, excitatory synapses only have AMPA components with $g¯=10$ nS, while for inhibitory synapses, $g¯=5$ nS. For the L2/3 pyramid, L5 pyramid, resp. Purkinje cell, excitatory Poisson rates are 2, five resp. 6 Hz and inhibitory firing rates are 4, one resp. 2 Hz. Simulation were run for 10,000 ms.

#### Parameters Figure 3

APs are evoked with a DC current pulse. For panels A–C, pulse amplitude is $i_{amp}=0.5$ nA and pulse duration is $t_{dur}=5$ ms. For panels D–F, we have $i_{amp}=3$ nA and $t_{dur}=1$ ms. For panels G–I, $i_{amp}=1.5$ nA and $t_{dur}=5$ ms. For panels J–K, the somatic current pulse had $i_{amp}=1.9$ nA and $t_{dur}=5$ ms, while the dendritic current injection had a double exponential waveform, with $\tau_{r}=0.5$ ms and $\tau_{d}=5$ ms and amplitude $i_{amp}=0.5$ nA. Onset of the somatic current pulse precedes onset of the dendritic current injection by 5 ms.

#### Parameters Figure 4

In panel B, we inject Ornstein–Uhlenbeck (OU) processes for current (mean $\mu=0.08$ nA and standard deviation $\sigma=0.025$ nA) and conductance ($\mu=0.005$ μS, $\sigma=0.0025$ μS). Reversal was 0 mV for the excitatory conductance and −80 mV for the inhibitory conductance. All OU processes had a time scale of 30 ms. In panels D–F, we use AMPA+NMDA synapses with $g¯=0.5$ nS and $R_{NMDA}=3$. Burst firing is mimicked by drawing synapse activation times from a Gaussian distribution with as mean the burst time and a standard deviation of 2 ms.

In panels G–J, AMPA+NMDA synapses at the compartment site (green square) have $g¯=1$ nS and $R_{NMDA}=2$. To determine the NMDA-spike threshold, we activate between 0 and 200 synapses in a burst. The burst is again modeled by drawing spike times from a Gaussian distribution with a 2 ms standard deviation. We then multiply the amplitude of the resulting waveform with its half-width, and average this quantity over five trials for each number of activated synapses. The number of synapses at which this quantity increases most is taken to be the NMDA-spike threshold.

We aim to test the synaptic weight-rescale factors for the AMPA and GABA synapses $\beta_{cond}^{ext}$ under a wide range of input conditions. To do so, we conduct simulations with different total time-averaged conductance loads $g_{avg}$, exerted by the AMPA and a GABA synapse on the subtree that is to be reduced. These synapses are activated with spike times drawn from a homogeneous Poisson process. We also also change the size of the conductance fluctuations, by conducting simulations with different firing rates for the homogeneous Poisson processes (since the total conductance load for a simulation is fixed, a small firing rate means that individual synaptic weights have to be increased to reach the desired total conductance load, hence resulting in larger conductance fluctuations). We furthermore change the number of locations on the subtree $n_{loc}$ over which the conductance load is distributed. Note that by consequence, the conductance load at each location is $g_{avg}/n_{loc}$. We also adapt these locations to a specified average difference in input resistance $Δ⁢z_{avg}$ between the compartment site and the location. Finally, we change the average voltage level achieved by the combined AMPA and GABA input by changing the ‘nudging potential’ $e_{n}$ (Urbanczik and Senn, 2014)

$$
e_{n}=\frac{g_{AMPA}⁢e_{AMPA}+g_{GABA}⁢e_{GABA}}{g_{AMPA}+g_{GABA}},
$$

where $g_{AMPA}$ resp. $g_{GABA}$ are the time-average conductances of individual AMPA resp. GABA synapses, and $g_{AMPA}=0$ mV resp. $g_{GABA}=-80$ mV their respective reversal potentials.

We thus draw five meta-parameters for each simulation: $g_{avg}$, $r_{avg}$, $n_{loc}$, $Δ⁢z_{avg}$ and $e_{n}$. The time-averaged conductance at each location is given by 

$$
g_{avg}/n_{loc}=g_{AMPA}+g_{GABA}.
$$

Together with (Equation 46), this fixes the time-averaged conductance of each individual AMPA synapse and GABA synapse. Since the temporal conductance profile of a synapse (e.g. the AMPA synapse) following the arrival of a single input AP is modeled as the product of a weight factor $w_{AMPA}$ and a unitary conductance window $g_{u⁢AMPA}⁢(t)$, the time-averaged conductance of that synapses activated by a homogeneous Poisson process input is 

$$
g_{AMPA}=w_{AMPA}r_{avg}\int_{0}^{∞}dtg_{uAMPA}(t).
$$

Thus, given $r_{avg}$ and $g_{AMPA}$, the synaptic weight $w_{AMPA}$ can be extracted (and similarly for the GABA synapse).

To perform simulations across a wide range of input conditions, we draw 200 samples of these five meta-parameters from the intervals: $e_{n}\in[-80⁢mV,-50⁢mV]$, $g_{avg}\in[0.01⁢nS,300⁢nS]$, $r_{avg}\in[1⁢Hz,100⁢Hz]$, $n_{loc}\in[1,20]$, and $Δ⁢z_{avg}\in[0⁢M⁢Ω,1023.2⁢M⁢Ω]$ following the Latin hypercube (LH) method (Press et al., 2007). $g_{avg}$ and $r_{avg}$ are sampled on a log scale, whereas for all other parameters, we use a linear scale.

#### Parameters Figure 5

To obtain compartment sites, we divide the longest branch in each basal subtree in $n$ parts of equal length, thus giving us $n$ distances from the soma, where we increase $n$ from 0 (point-neuron) to 10. In each subtree, we distribute compartments at all sites at these distances, and also add all bifurcation sites in between compartment sites. In this way, we obtain 11 reductions that we quantify according to ‘no. of compartments per 100 μm of dendrite’. We implement 400 ‘background’ synapses; 200 AMPA and 200 GABA synapses with an average conductance of $g_{AMPA}$ resp. $g_{GABA}=4⁢g_{AMPA}$ and firing rate $r_{AMPA}=r_{avg}$ resp. $r_{GABA}=r_{avg}$. We implement 20 synapse clusters, consisting of AMPA+NMDA synapses with maximal conductance $g¯_{A+N}$ and $R_{NMDA}=2$. These clusters are activated with a Poissonian burst rate $r_{burst}$, the number of spikes per burst is drawn from a Poisson distribution with parameter $n_{avg}$, and spike times are drawn for each burst time according to a Gaussian distribution with standard deviation of 5 ms. For each of the parameters not given previously, 10 LH samples were drawn from $g_{AMPA}\in[0.4nS,0.8nS]$, $r_{avg}\in[1.5Hz,3.0Hz]$, $g¯_{A+N}\in[0.5nS,1.5nS]$, $n_{avg}\in[10,30]$, and $r_{burst}\in[0.25Hz,0.6Hz]$, resulting in 10 different output spike rates shown in B. For each parameter set, a simulation was run for 10,000 ms.

#### Parameters Figure 6

Hyper- resp. depolarizing current steps have $i_{amp}=-.3$ nA resp. $i_{amp}=.1$ nA and $t_{dur}=500$ ms. The full model was optimized with an evolutionary algorithm using the BluePyOpt library (Van Geit et al., 2016), where we ran 100 iterations with and offspring size of 100. Goodness of fit was evaluated in a multi-objective manner as the root mean square error of the resting voltage (average voltage 100 ms before each current step), the final step voltage amplitudes after sag (average voltage during the last 100 ms of the DC current injection), and the voltage root mean square error of the full trace. We optimized the specific membrane capacitance and the conductance densities for passive leak and h, $K_{i⁢r}$ and $K_{m}$ channels. The membrane currents followed an exponential distribution $g⁢(x)=g_{0}⁢e^{x/d_{x}}$, with $x$ the distance from the soma, and as parameters $g_{0}$ – the conductance at the soma – and $d_{x}$ – the length constant of the distribution.

### Data and software availability

NEAT (NEural Analysis Toolbox), our open-source Python toolbox to obtain reduced models, is available on https://github.com/unibe-cns/NEAT  (copy archived at swh:1:rev:1cb15f36aa0a764105348541d046c85ef38e21ee).
