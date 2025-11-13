# Cells use molecular working memory to navigate in changing chemoattractant fields

## Authors

- Akhilesh Nandan<sup>1</sup>
- Abhishek Das<sup>1</sup>
- Robert Lott<sup>1</sup>
- Aneta Koseska<sup>1</sup> ([ORCID: 0000-0003-4263-2340](https://orcid.org/0000-0003-4263-2340)) †

### Affiliations

1. Department of Systemic Cell Biology, Max Planck Institute of Molecular Physiology Dortmund Germany ([ROR:03vpj4s62](https://ror.org/03vpj4s62))

† Corresponding author

## Abstract

In order to migrate over large distances, cells within tissues and organisms rely on sensing local gradient cues which are irregular, conflicting, and changing over time and space. The mechanism how they generate persistent directional migration when signals are disrupted, while still remaining adaptive to signal’s localization changes remain unknown. Here, we find that single cells utilize a molecular mechanism akin to a working memory to satisfy these two opposing demands. We derive theoretically that this is characteristic for receptor networks maintained away from steady states. Time-resolved live-cell imaging of Epidermal growth factor receptor (EGFR) phosphorylation dynamics shows that cells transiently memorize position of encountered signals via slow-escaping remnant of the polarized signaling state, a dynamical ‘ghost’, driving memory-guided persistent directional migration. The metastability of this state further enables migrational adaptation when encountering new signals. We thus identify basic mechanism of real-time computations underlying cellular navigation in changing chemoattractant fields.

## Introduction

Directed chemotactic behavior relies on generating polarized signaling activity at the plasma membrane of the cell that is translated to an elongated cell shape, and subsequent persistent migration in the direction of the signal. Experimental observations have shown that cells as diverse as social amoeba, neutrophils, leukocytes, fibroblasts, and nerve cells maintain the acquired orientation even when signals are disrupted or noisy (Parent and Devreotes, 1999; Foxman et al., 1999; Ridley et al., 2003). However, not only do they respond robustly to dynamic gradients, they can also adapt the migrational direction by integrating and resolving competing spatial signals, or prioritizing newly encountering attractants (Jilkine and Edelstein-Keshet, 2011; Skoge et al., 2014; Albrecht and Petty, 1998). This suggests that cells likely memorize their recent environment. Numerous models based on positive feedbacks, incoherent feed-forward, excitable or Turing-like networks have been proposed to describe how polarized signaling activity of cell-surface receptors and/or downstream signaling component such as members of the Rho GTPase family can arise (Levchenko and Iglesias, 2002; Levine et al., 2002; Mori et al., 2008; Goryachev and Pokhilko, 2008; Beta et al., 2008; Xiong et al., 2010; Trong et al., 2014; Halatek and Frey, 2018). This polarized activity in turn controls actin and myosin dynamics, and thereby cell migration. Conceptually, the underlying dynamical principles of the proposed models are similar, and can be understood as switching from the stable state of basal- to the stable polarized-signaling steady state in presence of guiding external cues. However, they can account either for sensing and adaptation to non-stationary stimuli or for long-term maintenance of polarized signaling activity, but not both. Thus, how cells process the information from a changing chemoattractant field in real time for long-range navigation remains unknown.

We propose a shift in the conceptual framework, describing theoretically that efficient navigation can be achieved when the polarized signaling state of the receptor network is transiently stable. This is fulfilled in the presence of dynamical ‘ghosts’ at a unique dynamical transition, which we demonstrate in the EGFR signaling network dynamics using a mathematical model, as well as quantitative live-cell imaging of polarized EGFR signaling. We show with a physical model of the cell and migration experiments using microfluidics, that cells generate memory of encountered signals through the ‘ghost’ state, translating it to memory in polarized shape changes and directional migration. Due to the metastability of the ‘ghost’ state, cells can also easily adapt their migration direction depending on the changes in signal localization. We therefore describe a basic mechanism of real-time cellular navigation in complex chemoattractant fields.

## Results

### Dynamical mechanism of navigation in non-stationary environments

We conjectured that only dynamically metastable receptor signaling states can enable both transient stability of polarized signaling as necessary for robust, memory-guided migration in noisy fields, as well as rapid adaptation of its direction when signals vary in space and time. Our hypothesis is that this can be achieved if biochemical systems are maintained outside, but in the vicinity of the polarization steady state. We therefore approached the problem using the abstract language of dynamical systems theory, where the characteristics of any process directly follow from the type of dynamical transitions, called bifurcations, through which they emerge (Strogatz, 2018).

Directed migration relies on a polarized representation of the directional signal, requiring a reliable mechanism for signal-induced transition from a non-polarized symmetric, to a polarized receptor signaling state, and subsequently polarized cell shape. This transition is thus a symmetry-breaking transition, and we propose that a pitchfork bifurcation ($P⁢B$, Koseska et al., 2013; Strogatz, 2018) satisfies the necessary dynamical conditions (Figure 1A, Figure 1—figure supplement 1A). Transient memory on the other hand is a unique characteristic of another bifurcation, a saddle-node ($S⁢N$) bifurcation, that characterizes a transition between stable and unstable steady states. When the $S⁢N$ and thereby a stable steady-state is lost, for example upon signal removal, a remnant or a dynamical ‘ghost’ of the stable state emerges (Strogatz, 2018). These ‘ghost’ states are dynamically metastable and transiently maintain the system in the vicinity of the steady state (Figure 1A, Figure 1—figure supplement 1A). Necessary for manifestation of the ‘ghost’ state is organization at criticality, before the $S⁢N$. We have previously examined both theoretically and experimentally, the response of receptor networks under uniform growth factor stimulation and determined that the concentration of receptors on the cell membrane regulate the organization of the system at criticality (Stanoev et al., 2018; Stanoev et al., 2020). The features of both bifurcations, cell polarization under spatial cues and a transient memory of this polarization in absence of the cue, will be unified for a sub-critical $P⁢B$, as it is stabilized via  $S⁢N_{P⁢B}$ s. We thus propose that organization at criticality - in the vicinity of a $S⁢N_{P⁢B}$ (gray shaded area in Figure 1—figure supplement 1A; details discussed in Materials and methods), renders a minimal mechanism for cellular responsiveness in changing environments.

![Figure 1.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig1-v2.jpg)

**Figure 1.:** (A) Dynamical mechanism: sub-critical pitchfork bifurcation ($P⁢B$) determines stimulus-induced transition (arrow) between basal unpolarized and polarized receptor signaling state, whereas the associated saddle-node through which the $P⁢B$ is stabilized ($S⁢N_{P⁢B}$) gives rise to a ‘ghost’ memory state upon signal removal for organization at criticality (before the $S⁢N_{P⁢B}$). See Figure 1—figure supplement 1A and Methods for detailed description of these transitions. (B) Scheme of the EGFR-PTP interaction network. Ligandless EGFR ($E_{p}$) interacts with PTPRG ($P_{R⁢G}$) and PTPN2 ($P_{N⁢2}$). Liganded EGFR ($E-E_{p}$) promotes autocatalysis of $E_{p}$. Causal links - solid black lines; curved arrow lines - diffusion, PM - plasma membrane, ER- endoplasmic reticulum. See also Figure 1—figure supplement 1B. (C) Signal-induced shape-changes during cell polarization. Arrows: local edge velocity direction. Zoom: Viscoelastic model of the cell - parallel connection of an elastic and a viscous element. $P_{total}$: total pressure; v: local membrane velocity; l: viscoelastic state. Bold letters: vectors. Cell membrane contour: $[0,2⁢\pi]$. (D) Top: In silico evolution of spatial EGF distribution. Bottom: Kymograph of $E_{p}$ for organization at criticality from reaction-diffusion simulations of the network in (B). Triangle - gradient duration. (E) Corresponding exemplary cell shapes with color coded $E_{p}$, obtained with the model in (C). (F) Top: Temporal profiles $E_{p}$ (black) and $E-E_{p}$ (gray). Green shaded area: EGF gradient presence. Bottom: State-space trajectory of the system with denoted trapping state-space areas (colored) and respective time-scales. See also Figure 1—video 1. Thick/thin line: signal presence/absence. (G) Quantification of in silico cell morphological changes from the example in (E). Triangle - gradient duration. (H) Left: same as in (G), only when stimulated with two consecutive dynamic gradients (triangles) from same direction. Second gradient within the memory phase of the first. See also Figure 1—figure supplement 1D. Right: the second gradient (orange triangle) has opposite direction. See also Figure 1—figure supplement 1E. Dashed line: curve from (G). Mean ± s.d. from n=3 is shown. Parameters: Materials and methods. In (D-H), green(orange)/red lines: stimulus presence/absence.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Dynamical mechanism of signal-induced polarization and subsequent memory. Top, left: critical organization before sub-critical pitchfork bifurcation ($P⁢B$, grey shaded area). $S⁢N_{P⁢B}$: saddle-node bifurcation through which $P⁢B$ is stabilized. Top, right: Stimulus induces unfolding of the $P⁢B$. For the same organization (gray shaded area) the system is now in the stable polarized state (inhomogeneous steady state, IHSS). Bottom: After stimulus removal and disappearance of the $S⁢N_{P⁢B}$, the systems is transiently trapped in the ‘ghost’ of this bifurcation, causing memory of the polarized state. Stable/unstable steady states (solid/dashed lines): basal (homogeneous, black) and polarized (inhomogeneous, magenta) receptor activity; stimulus-induced transitions between states: arrow lines; circles: schematic representation of cell; color bar: receptor activity. (B) Spatial representation of the EGFR sensing network shown in Figure 1B. $E_{p}$ - phosphorylated EGFRR, $P_{R⁢G}$ - PTPRG; $P_{N⁢2}$ - PTPN2, solid lines: causal interactions, curved lines: diffusion. (C) Bifurcation diagram of the EGFR sensing network. Notations and line description as in (A). $E_{t}$: total EGFR on the plasma membrane. Parameters in Materials and methods. (D) Top: Position of two subsequent dynamic EGF gradients in the numerical simulation. Bottom: Representative in silico kymograph of EGFR phosphorylation ($E_{p}$) for organization of the system at criticality. Shape changes depicted in Figure 1H, left. (E) Same as in (D), only when the second gradient ( orange) is from the opposite direction. Corresponding shape changes depicted in Figure 1H, right. (F) Position of dynamic EGF signals(s) in the numerical simulation (top) and respective kymographs of EGFR activity changes (bottom) for organization of the system in the stable inhomogeneous state (magenta attractor in (C)). Left: Single dynamic gradient; Middle: a temporally disrupted gradient represented by two subsequent dynamic gradients from the same direction; Right: Second gradient (orange) from the opposite direction. (G) Same as in (E), only for organization in the homogeneous steady state representing symmetric basal EGFR phosphorylation (lower solid black line in C). (H) Same as in (E), only for organization in the homogeneous steady state representing uniform high EGFR phosphorylation (upper solid black line in C). For (C-H) parameters in Methods. Vertical green(orange)/red lines: stimulus presence/absence.

We described this conjecture mathematically for a general reaction-diffusion model representing the signaling activity on the plasma membrane of a cell, $\frac{\partial⁡U⁢(x,t)}{\partial⁡t}=F⁢(U)+D⁢\nabla^{2}⁡U⁢(x,t)$, with $U$ being the vector of local densities of active signaling components, $D$ - diffusion constants and $F$ accounting for all chemical reactions. Our theoretical analysis shows that a $P⁢B$ exists if, for a spatial perturbation of the symmetric steady state ($U_{s}$) of the form $U⁢(x,t)=U_{s}+\delta⁢U⁢(x)⁢e^{\lambda⁢t}$, the conditions $\delta⁢U⁢(-x)=-\delta⁢U⁢(x)$ and the limit $lim_{\lambda→0}⁡F_{\lambda}=d⁢e⁢t⁢(J)=0$ are simultaneously fulfilled (Materials and methods). This implies that the linearized system has zero-crossing eigenvalues ($\lambda$) associated with the odd mode of the perturbation (Paquin-Lefebvre et al., 2020). To probe the sub-critical transition and therefore the necessary organization at criticality, a reduced description in terms of an asymptotic expansion of the amplitude of the polarized state ($ϕ$) must yield the Landau equation $\frac{d⁢ϕ}{d⁢t}=c_{1}⁢ϕ+c_{2}⁢ϕ^{3}-c_{3}⁢ϕ^{5}$, guaranteeing the existence of $S⁢N_{P⁢B}$ (see Materials and methods for derivation).

These abstract dynamical transitions can be realized in receptor signaling networks with different topologies and are best analyzed using computational models, whose predictions are then tested in quantitative experiments on living cells. To exemplify the above-mentioned principle, we use the well-characterized Epidermal growth factor receptor (EGFR) sensing network (Reynolds et al., 2003; Baumdick et al., 2015; Stanoev et al., 2018). It constitutes of double negative and negative feedback interactions of the receptor, EGFR ($E_{p}$) with two enzymes, the phosphatases PTPRG ($P_{R⁢G}$) and PTPN2 ($P_{N⁢2}$, Figure 1B, Figure 1—figure supplement 1B), respectively. $E_{p}$ and $P_{R⁢G}$ laterally diffuse on the membrane and inhibit each-other’s activities (see Materials and methods for the molecular details of the network). The bidirectional molecular interactions between EGFR and the phosphatases can be mathematically represented using mass action kinetics, giving a system of partial differential equations (PDE) that describes how the dynamics of the constituents evolves in time and space (Equation 14 in Materials and methods). Applying a weakly nonlinear stability analysis (Becherer et al., 2009) to this system of equations shows that the EGFR phosphorylation dynamics undergoes a symmetry-breaking transition ($P⁢B$) as outlined above (proof in Materials and methods, Figure 1—figure supplement 1C). The $P⁢B$ generates a polarized state that is represented as a inhomogeneous steady state (IHSS) - a combination of a high receptor phosphorylation at the cell front and low in the back of the cell (schematically shown in Figure 1A, Figure 1—figure supplement 1A). This is contrary to a bistable system, where the polarized signaling state would be manifested by two steady states, high and low protein phosphorylation in the front and back of the cell, respectively (Beta et al., 2008). This profiles $P⁢B$ as a robust mechanism of cell polarization. Polarized EGFR signaling on the other hand, will lead to reorganization of the cortical actomyosin cytoskeleton by regulating members of the Rho GTPase family, thereby inducing signal-dependent cell shape changes and subsequent migration (Chiasson-MacKenzie and McClatchey, 2018; Ridley and Hall, 1992). In order to link signaling activity with morphodynamics, we modeled the cell as a viscoelastic cortex surrounding a viscous core (Yang et al., 2008) (Materials and methods), where EGFR signaling dynamics affects cell shape changes through the protrusion/retraction stress and the viscoelastic nature of the cell membrane (Figure 1C).

We first fixed the total EGFR concentration on the cell membrane to a value that corresponds to organization at criticality, and investigated the response of the in silico cell to gradient stimulus. In the absence of stimulus, basal EGFR phosphorylation is uniformly distributed along the cell membrane rendering a symmetrical cell shape (Figure 1D and E). Introducing dynamic gradient stimulus in the simulation (slope changes from steep to shallow over time, Figure 1D, top) led to rapid polarization of EGFR phosphorylation in the direction of the maximal chemoattractant concentration, generating a cell shape with a clear front and back. The polarized signaling state was maintained for a transient period of time after removal of the gradient, corresponding to manifestation of memory of the localization of the previously encountered signal (Figure 1D and E; temporal profile Figure 1F, top). The prolonged polarized state does not result from remnant ligand-bound receptors ($E-E_{p}$) on the plasma membrane, as they exponentially decline after signal removal (Figure 1F, top). The memory in polarized signaling was also reflected on the level of the cell morphology, as shown by the difference of normalized cell protrusion area in the front and the back of the cell over time (Figure 1G). Plotting the trajectory that describes the change of the state of the system over time (state-space trajectory, Figure 1F bottom) shows that the temporal memory in EGFR phosphorylation polarization is established due to transient trapping of the signaling state trajectory in state-space, a property of the metastable ‘ghost’ state (Stanoev et al., 2020; Strogatz, 2018) through which the system is maintained away from the steady state. The simulations show that there are two characteristic time-scales present in the system: slow evolution of the system’s dynamics in the ‘ghost’ state due to the trapping, and fast transitions between the steady states (Figure 1—video 1). This emergence of the slow time-scale is another hallmark of systems organized at criticality. What is crucial here however, is that the trapping in the dynamically metastable memory state does not hinder sensing of, and adapting to subsequent signals. The cell polarity is sustained even when the EGF signal is briefly disrupted (Figure 1H left, Figure 1—figure supplement 1D), but also, the cell is able to rapidly reverse direction of polarization when the signal direction is inverted (Figure 1H right, Figure 1—figure supplement 1E).

We next chose in the simulations a higher EGFR concentration on the membrane, such that the system moves from criticality to organization in the stable polarization state (magenta lines, Figure 1—figure supplement 1C). In this scenario, even a transient signal induces switching to the polarized state that is permanently maintained, generating a long-term memory of the direction on the initial signal. Thus, the cell is insensitive to subsequent stimuli from the same direction, whereas consecutive gradients from opposite directions generate conflicting information that cannot be resolved (Figure 1—figure supplement 1F). Organization in the homogeneous, symmetric steady states on the other hand renders cells insensitive to the extracellular signals (Figure 1—figure supplement 1G,H). These response features for organization in the stable steady state regimes resemble the finding of the previously published models: such models cannot simultaneously capture memory in polarization along with continuous adaptation to novel signals, or require fine-tuning of kinetic parameters to explain the experimentally observed cell behavior (Levchenko and Iglesias, 2002; Levine et al., 2002; Mori et al., 2008; Goryachev and Pokhilko, 2008; Beta et al., 2008; Xiong et al., 2010; Trong et al., 2014). This demonstrates that organization at criticality, in a vicinity of a $S⁢N_{P⁢B}$, is a unique mechanism for processing changing signals.

### Cells display temporal memory in polarized receptor phosphorylation resulting from a dynamical ‘ghost’

To test experimentally whether cells maintain memory of the direction of previously encountered signals through prolonged EGFR phosphorylation polarization, and what is the duration of this effect, epithelial breast cancer-derived MCF7 cells were subjected for 1 hr to a stable gradient of fluorescently tagged EGF-Alexa647 (EGF647) with a maximal amplitude of 10 ng/ml applied from the top of the chamber in a computer-programmable microfluidic device (Figure 2A and B). EGFR phosphorylation at the plasma membrane was quantified during and for 3 hr after gradient wash-out (gradient wash-out established in 4–5 min) by determining the rapid translocation of mCherry-tagged phosphotyrosine-binding domain (PTBmCherry) to phosphorylated tyrosines 1086/1148 of ectopically expressed EGFR-mCitrine (EGFRmCitrine) using ratiometric imaging (Offterdinger et al., 2004; Materials and methods). Due to the low endogenous EGFR levels in MCF7 cells, the expression range of EGFRmCitrine was set to mimic the endogenous receptor range in the related MCF10A cell line, such that both cell lines have equivalent signaling properties of downstream effector molecules (Stanoev et al., 2018), and were therefore used in a complementary way in this study.

![Figure 2.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig2-v2.jpg)

**Figure 2.:** Molecular memory in polarized $EGFR^{mCitrine}$ phosphorylation resulting from dynamical state-space trapping is translated to memory in polarized cell shape.(A) Scheme of microfluidic EGF647-gradient experiment; Zoom: single-cell measurables. Cell membrane contour $[0,2⁢\pi]$ (20 segments). $P⁢T⁢B$ - phosphotyrosine binding domain, $F⁢P$/star symbol - fluorescent protein, $E⁢G⁢F⁢R_{p}$- phosphorylated $EGFR^{mCitrine}$. Remaining symbols as in Figure 1B. (B) Quantification of EGF647 gradient profile (at $60⁢m⁢i⁢n$, green) and after gradient wash-out (at $65⁢m⁢i⁢n$, red). Mean ± s.d., N=4. (C) Exemplary quantification of, Top: Spatial projection of EGF647 around the cell perimeter. Gaussian fit of the spatial projection is shown. Middle: single-cell $E⁢G⁢F⁢R_{p}$ kymograph. Data was acquired at 1 min intervals in live $MCF7−EGFR^{mCitrine}$ cells subjected for $60⁢m⁢i⁢n$ to an EGF647 gradient. Other examples in Figure 2—figure supplement 1D. Bottom: respective spatial projection of $E⁢G⁢F⁢R_{p}$. Gaussian fit of the spatial projection is shown. Mean ± s.d. from n=20 cells, N=7 experiments in Figure 2—figure supplement 1C. (D) Average fraction of polarized plasma membrane area (mean ± s.d.). Single cell profiles in Figure 2—figure supplement 1G. (E) Quantification of memory duration in single cells (median±C.I.). In (D) and (E), n=20, N=7. (F) Top: Exemplary temporal profiles of phosphorylated $E⁢G⁢F⁢R^{m⁢C⁢i⁢t⁢r⁢i⁢n⁢e}$ (black) and $E⁢G⁢F^{647}-E⁢G⁢F⁢R^{m⁢C⁢i⁢t⁢r⁢i⁢n⁢e}$ (gray) corresponding to (C). Bottom: Corresponding reconstructed state-space trajectory (Figure 2—video 1) with denoted trapping state-space areas (colored). Thick/thin line: signal presence/absence. d - embedding time delay. (G) Equivalent as in (F), only in live MCF7-EGFR $SN_{PB}$ cell subjected to 1 hr EGF647 gradient (green shading), and 3 hr after wash-out with 1 µM Lapatinib. Corresponding kymograph shown in Figure 2—figure supplement 2A. Mean ± s.d. temporal profile from n=9, N=2 in Figure 2—figure supplement 2B. Bottom: Corresponding reconstructed state-space trajectory with state-space trapping (colored) (Methods, Figure 2—video 2). (H) Averaged single-cell morphological changes (solidity, mean ± s.d. from n=20, N=7). Average identified memory duration (blue arrow): $40⁢m⁢i⁢n$. Top insets: representative cell masks at distinct time points. (I) Average solidity in $MCF7−EGFR^{mCitrine}$ cells subjected to experimental conditions as in (G). Mean ± s.d. from n=9, N=2. Top insets: representative cell masks at distinct time points. In (F-I) green shaded area: EGF647 gradient duration; green/red lines: stimulus presence/absence. Brown line: Lapatinib stimulation. See also Figure 2—figure supplements 1 and 2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Quantification of $EGFR^{mCitrine}$ phosphorylation polarization.(A) Representative images / overlay of $EGFR^{mCitrine}$ (cyan) and $PTB^{mCherry}$ (magenta) prior to ($0⁢m⁢i⁢n$), during ($30⁢m⁢i⁢n$) and after ($200⁢m⁢i⁢n$) $MCF7−EGFR^{mCitrine}$ cells were subjected to $60⁢m⁢i⁢n$ EGF647 gradient. Columns: non-activated (blue), transiently polarized (green) and uniformly pre-activated (yellow). Scale bar: $15⁢\mu⁢m$. (B) Distribution of single-cell responses corresponding to (A) from $N=7$ experiments. (C) Average profile of the spatial projection of the fraction of phosphorylated $EGFR^{mCitrine}$ from single-cell kymographs. For each cell, temporal average per spatial bin is calculated, and the final spatial profile was estimated as an average of a moving window of 7 points. Peaks of the single-cell distributions were shifted to $\pi$ before averaging. Mean ± s.d. from n=20 cells, N=7 experiments is shown. (D) Additional exemplary single-cell kymographs depicting polarized $EGFR^{mCitrine}$ phosphorylation. Data acquisition and quantification as in Figure 2C. Triangle: gradient duration. (E) Same as in (D), only for non-activated (basal, left) and uniformly pre-acivated (right) $EGFR^{mCitrine}$ phosphorylation. Triangle: gradient duration. (F) Quantification of direction of polarization of $EGFR^{mCitrine}$ phosphorylation. Top: exemplary kymographs of $E⁢G⁢F⁢R_{p}$ (left) and EGF647 outside the cells (right) during the gradient stimulation (60 min). Data corresponds to Figure 2C. Middle: respective spatial projection of $E⁢G⁢F⁢R_{p}$ and EGF647. Average using a moving window of 7 bins is shown. Bottom: Schematic representation of identifying direction of polarization. Left: angle ($\alpha$) between $E⁢G⁢F⁢R_{p}$ and EGF647 is estimated as the angle between the maxima of the spatial projections (shown in middle plots). Right: distribution of $\alpha$ calculate from n=20 cells, N=7 experiments. (G) Temporal profiles of the estimated fraction of polarized area for single cells. Green shaded area: EGF647 gradient duration. The mean ± s.d. shown in Figure 2D.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Memory in polarized $E⁢G⁢F⁢R_{p}$ results from a dynamical ‘ghost’.(A) Exemplary single-cell kymograph depicting phosphorylated $EGFR^{mCitrine}$ for data acquired at 1 min intervals in live $MCF7−EGFR^{mCitrine}$ cell subjected for 1 hr to EGF647 gradient, and 3 hr during gradient wash-out with  1 µM Lapatinib. (B) Average temporal profiles of plasma membrane $EGFR^{mCitrine}$ phosphorylation of live $MCF7−EGFR^{mCitrine}$ cells subjected for 1 hr to EGF647 gradient, and 3 hr during gradient wash-out with  1 µM Lapatinib. Related to Figure 2G. Mean ± s.d. from n=9, N=2 is shown. Green shaded area: EGF647 gradient. (C) In silico temporal profiles of $E_{p}$ (black) and $E-E_{p}$ (gray), when the kinase activity of the receptor is inhibited after gradient removal by decreasing the autocatalytic rate constant ($\alpha_{2}=0.25$). Green shaded area: EGF gradient presence. (D) State-space trajectory corresponding to the example in (C), with denoted trapping state-space areas (colored). Thick/thin line: signal presence/absence. See also Figure 2—video 3. (E) Exemplary profiles of $E⁢G⁢F⁢R_{p}$ (black) and corresponding fit with an inverse sigmoid function after gradient removal (magenta) of $MCF7−EGFR^{mCitirine}$ cell subjected for 1 hr to an EGF647 gradient, and 3 hr wash-out with 1 µM Lapatinib. (F), Same as in (E), but for cells without Lapatinib treatment. (G) Left: Hill coefficient estimated from single-cell fits with inverse sigmoid function as in (E, F). Right: Corresponding half-life estimates. n=23, N=5, (without Lapatinib) and n=12, N=5 (with Lapatinib). Error bars: median±95%C.I (H) Exemplary quantification of morphological changes using directed cell protrusion area for the cell shown in Figure 2C. Estimated memory duration: 43 min (blue arrow).

Kymograph analysis of $EGFR^{mCitrine}$ phosphorylation at the plasma membrane of single cells showed polarization in a shallow gradient of EGF647 (as shallow as 10% between front and back of the cell; Figure 2C, Figure 2—figure supplement 1A-D). The direction of $EGFR^{mCitrine}$ phosphorylation polarization coincided with the direction of maximal EGF647 concentration around each cell ($\pi/4$ on average, Figure 2—figure supplement 1F). Only few cells manifested basal or symmetric $EGFR^{mCitrine}$ phosphorylation distribution upon gradient stimulation (Figure 2—figure supplement 1A, B, E). Plotting the fraction of plasma membrane area with polarized $EGFR^{mCitrine}$ phosphorylation showed cell-to-cell variability in the polarization kinetics, as well as the maximal amplitude of polarized $EGFR^{mCitrine}$ phosphorylation (Figure 2—figure supplement 1G), in contrast to the rapid EGFR polarization in the numerical simulations (Figure 1D). These differences likely results from the variable positioning of the cells along the gradient in the microfluidic chamber, as well as the variability of total EGFR concentrations in single cells. However, quantification of the polarization duration revealed that, similarly to the numerical predictions, the polarization persisted ~ 40 min on average after gradient removal ([4–159 min], Figure 2D and E).

The memory in $EGFR^{mCitirne}$ phosphorylation was also reflected in the respective single-cell temporal profiles (exemplary profile shown in Figure 2F, top). Reconstructing the state-space trajectory from this temporal profile using Takens’s delay embedding theorem (Takens, 1980) (Materials and methods) showed that before the fast transition to the basal state, the trajectory of the system was trapped in the vicinity of the polarized state (Figure 2F bottom, Figure 2—video 1). Despite the biological and technical noise that affect the measurement of the temporal $EGFR^{mCitrine}$ phosphorylation profile, and thereby the reconstruction of the state-space trajectory, both qualitatively resemble the equivalent numerical profiles (compare Figures 1F and 2F). In contrast, when cells were subjected to an ATP analog EGFR inhibitor (Björkelund et al., 2013) during gradient wash-out, the  $EGFR^{mCitrine}$ phosphorylation response exponentially decayed, resulting in a clear absence of transient memory and respective state-space trapping (Figure 2G, Figure 2—figure supplement 2A, B, Figure 2—video 2). Since Lapatinib inhibits the kinase activity of the receptor, the dynamics of the system in this case is mainly guided by the dephosphorylating activity of the phosphatases. Implementing an equivalent of the Lapatinib inhibition in the numerical simulations by decreasing the autocatalytic EGFR activation rate constant after gradient removal verifies that the presence of memory in EGFR phosphorylation cannot be explained only by a dephosphorylation process (Figure 2—figure supplement 2C). This is also evident from the respective state-space trajectory, where the system directly transits from the polarized to the basal state, without intermediate state-space trapping (Figure 2—figure supplement 2D, Figure 2—video 3).

Fitting the experimentally measured single-cell temporal $EGFR^{mCitrine}$ phosphorylation profiles after gradient wash-out using an inverse sigmoid function (Methods) further corroborated that under Lapatinib treatment, phosphorylated $EGFR^{mCitrine}$ exponentially relaxed from the polarized to the basal state (Hill coefficient ≈ 1.28), with a half-life of approx. 10 min (Figure 2—figure supplement 2E, G). Under normal conditions however, the half-life was 30 min on average, reflecting that the phosphorylated $EGFR^{mCitrine}$ is transiently maintained in the metastable signaling state after gradient removal, before rapidly switching to the basal state (Hill coefficient ≈2.88, Figure 2—figure supplement 2F, G). Taken together, this analysis suggests that the memory in polarized $EGFR^{mCitrine}$ phosphorylation results from a dynamically metastable ‘ghost’ state, and not a slow dephosphorylation process.

In order to identify whether the memory in polarized $EGFR^{mCitrine}$ phosphorylation also enables maintaining memory of polarized cell morphology after gradient removal, we quantified the cellular morphological changes using solidity, which is the ratio between the cell’s area and the area of the convex hull. The average single-cell solidity profile over time showed that epithelial cells maintained the polarized cell shape for ~ 40 min after signal removal (Figure 2H, Materials and methods), which directly corresponds to the average memory duration in polarized $EGFR^{mCitrine}$ phosphorylation (Figure 2E). The exemplary quantification of the temporal evolution of the cell protrusion area in direction of the gradient showed equivalent results (Figure 2—figure supplement 2H corresponding to the profile in Figure 2C; memory duration ~ 43 min). In contrast, the absence of memory in $EGFR^{mCitrine}$ phosphorylation under Lapatinib treatment also resulted in absence of transient memory in polarized morphology after stimulus removal (Figure 2I). This establishes a direct link between memory in polarized receptor activity and memory in polarized cell shape.

### Transient memory in cell polarization is translated to transient memory in directional migration

To test the phenotypic implications of the transient memory in cell polarization, we analyzed the motility features of the engineered $MCF7−EGFR^{mCitrine}$, as well as of MCF10A cells at physiological EGF concentrations. Cells were subjected to a 5 hr dynamic EGF647 gradient that was linearly distributed within the chamber, with EGF647 ranging between 25-0 ng/ml, allowing for optimal cell migration (Figure 3—figure supplement 1A, B). The gradient steepness was progressively decreased in a controlled manner, rendering an evolution towards a ∼50% shallower gradient over time (Figure 3—figure supplement 1B). Automated tracking of single-cell’s motility trajectories was performed for 14 hr in total. $MCF7−EGFR^{mCitrine}$, as well as MCF10A cells migrated in a directional manner toward the EGF647 source (Figure 3A- and Figure 3—figure supplement 1C, D - left, green trajectory parts). This directed migration persisted for transient period of time after the gradient wash-out (Figure 3A- and Figure 3—figure supplement 1C, D - left, red trajectory parts, Figure 3—video 1), indicating that cells maintain memory of the location of previously encountered source. After the memory phase, the cells transitioned to a migration pattern equivalent to that in the absence of a stimulus (Figure 3A right, Figure 3—figure supplement 1C, D middle). Uniform stimulation with 20 ng/ml EGF647 did not induce directed migration in either of the cell lines, although the overall migration distance was increased in accordance with previous findings (Brüggemann et al., 2021; Figure 3—figure supplement 1C, D, right). Quantification of the directionality of single cells’ motion, that is defined as the displacement over travelled distance, showed that for MCF10A cells, it was significantly higher during the gradient stimulation (5 hr) as compared to no- or uniform-stimulation case (Figure 3B). Moreover, the directionality estimated in the 9 hr time-frame after the gradient removal was greater than the one in continuous stimulus absence, corroborating that cells transiently maintain memory of the previous direction of migration.

![Figure 3.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig3-v2.jpg)

**Figure 3.:** (A) Left: representative MCF10A single-cell trajectories. Green - 5 hr during and red line - 9 hr after dynamic EGF647 gradient (shaded). Exemplary cell in Figure 3—video 1. Right: Same as in (A), only 14 hr in continuous EGF647 absence. Black dots: end of tracks. (B) Directionality (displacement/distance) in MCF10A single-cell migration during 14 hr absence (0 ng/ml; n=245, N=3) or uniform 20 ng/ml EGF647 stimulation (n=297, N=3); 5 hr dynamic EGF647 gradient (green) and 9 hr during wash-out (red; n=23, N=5). p-values: ***p≤ 0.001, two-sided Welch’s t-test. Error bars: median±95%C.I. (C) Top: Projection of the cells’ relative displacement angles (mean ± s.d.; n=23, N=5) during (green shaded) and after 5 hr dynamic EGF647 gradient. Green/red lines: stimulus presence/absence. Bottom: Kolmogorov-Smirnov (KS) test p-values depicting end of memory in directional migration (blue arrow, $t=350⁢m⁢i⁢n$). KS-test estimated using 5 time points window. For (A-C), data sets in Figure 3—figure supplements 1D and 2A. (D) Representative in silico single-cell trajectories. Left: PB(t)RW: Persistent biased random walk, bias is a function of time (green/blue trajectory part - bias on). Right: RW: random walk. (E) Corresponding directionality estimates from n=50 realizations, data in Figure 3—figure supplement 2D. PRW: persistent random walk. p-values: ***p≤ 0.001, two-sided Welch’s t-test. Error bars: median±95%C.I. (F) Same as in (C), top, only from the synthetic PB(t)RW trajectories. (G) MCF10A single-cell trajectories quantified 5 hr during (green) and 9 hr after (brown) dynamic EGF647 gradient (shading) wash-out with 3 µM Lapatinib. n=12, N=5. See also Figure 3—video 2. (H) Directionality in single-cell MCF10A migration after gradient wash-out with (brown, n=12, N=5) and without Lapatinib (red, n=23, N=5). p-values: **p≤ 0.01, KS-test. Error bars: median±95%C.I. (I) Same as in (C), only for the cells in (G). See also Figure 3—figure supplement 2H.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Characterization of $MCF7−EGFR^{mCitrine}$ and MCF10A single-cell migration.(A) Identification of optimal EGF647 dose range for single-cell gradient migration assay for $MCF7−EGFR^{mCitrine}$ (top) and MCF10A (bottom). Percentage of cells having motility greater than a displacement threshold ((Number of cell tracks with track length greater than threshold/Total number of cells)*100) is shown. (B) Top: Quantification of 5 hr dynamic EGF647 gradient at distinct time-points. Bottom: Corresponding quantification of the temporal evolution of the gradient slope. Percentage of gradient steepness: $((E⁢G⁢F_{(0)}^{647}-E⁢G⁢F_{(L)}^{647})/E⁢G⁢F_{(0)}^{647})*100$ where $L$ is the length across the chamber. Mean ± s.d. from N=4 is shown. (C) Divergence plots depicting MCF7-EGFRmCitrine single-cell trajectories quantified, left: 5 hr during (green) and for 9 hr after (red) dynamic EGF647 gradient duration (n=26, N=7); middle: 14 hr of 0 ng/ml EGF647 (subset of n=207 from n=426 is shown, N=2); and right: 14 hr of uniform 20 ng/ml EGF647 stimulation (subset of n=200 from n=456 is shown, N=2). (D) Same as in (C), only for MCF10A cells. Left: n=23, N=5; middle: n=245, N=3; right: n=297, N=3. Related to Figure 3A–C. Black dots: end of tracks.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Scheme of single-cell relative displacement angle estimation ($cos⁡\theta$). (B) Average $cos⁡\theta$ from single MCF10A cell trajectories (mean ± s.d.), estimated over a 2 min interval upon, left: 0 ng/ml EGF647 (n=245, N=3); right: 20 ng/ml uniform EGF647 stimulation (n=297, N=3). Related to Figure 3A–C. (C) Kernel density estimates (KDE) of the distributions in (B) and Figure 3C top, in continuous EGF647 absence (gray), during 5 hr dynamic EGF647 gradient (green), after gradient wash-out: $t\in[300⁢m⁢i⁢n,350⁢m⁢i⁢n]$ (blue) and $t\in[350⁢m⁢i⁢n,840⁢m⁢i⁢n]$ (red). p-values: ***p≤ 0.001, ns: not significant, KS-test. (D) Synthetic single-cell trajectories (Equation 7, Materials and methods). Left: Persistent biased random walk PB(t)RW; middle: random walk (RW); right: Persistent random walk (PRW). Parameters: for PB(t)RW, $\tau=38.143$, $b⁢(t)=0.134$, $D=2.207$ for $t\in[0⁢m⁢i⁢n,350⁢m⁢i⁢n]$ (green,blue), $\tau=11.105$, $b⁢(t)=0$, $D=0.425$ for $t\in[350⁢m⁢i⁢n,840⁢m⁢i⁢n]$ (red); for RW, $\tau=11.105$, $b⁢(t)=0$, $D=0.425$; for PRW, $\tau=38.143$ and $D=2.207$. (E) Same as in (B), only from the synthetic trajectories. Left: PB(t)RW with $\tau=38.143$, $D=2.207$, $b⁢(t)=0.134$ for $t\in[0⁢m⁢i⁢n,300⁢m⁢i⁢n]$ (green shading), $\tau=11.105$, $D=0.425$, $b⁢(t)=0$ for $t\in[300⁢m⁢i⁢n,840⁢m⁢i⁢n]$, middle: RW; right: PRW. (F) Same as in (C), only from the synthetic trajectories. p-values: ***p≤ 0.001, ns: not significant, KS-test. (G) Synthetic single cell trajectories generated when PBRW is considered only in the time frame during gradient duration to mimic the experimental data in Figure 3G. Parameters as in (E, left). (H) Same as in (C), only for MCF10A cells stimulated for 5 hr with EGF647 gradient and 9 hr after wash-out with 3µM Lapatinib. Related to Figure 3I. p-values: ***p≤ 0.001, ns: not significant, KS-test.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Quantifying duration of memory in directional migration from single-cell $cos⁡\theta$ profiles.(A) Duration of memory in directional migration of MCF10A cells treated with a 5 hr dynamic EGF647 gradient (n=23, N=5; single cell tracks in Figure 3—figure supplement 1D), and MCF10A cells treated with a 5 hr dynamic EGF647 gradient, followed by 9 hr 3 µM Lapatinib during gradient wash-out (n=12, N=5, single cell tracks in Figure 3G). p-values: ***p≤0.001, two-sided Welch’s t-test. Error bars: median±95%C.I. Values estimated from single-cell $cos⁡\theta$ plots. (B) Exemplary $cos⁡\theta$ plots estimated from MCF10A cell motility trajectories. Cells were treated with a 5 hr dynamic EGF647 gradient, followed by 9 hr 3 µM Lapatinib during gradient wash-out. Green shaded area denotes EGF647 gradient interval, blue shaded area - time interval of identified memory in directional migration (Materials and methods). (C) Same as in (B), only without Lapatinib treatment. (D) Divergence plots of the cells shown in (B). Green part of the tracks denotes migration during gradient, blue - migration during identified memory phase after gradient removal, brown - random migration after gradient removal. Green shaded triangle: gradient direction. Black dots: end of tracks. (E) Divergence plots of the cells in (C). Color coding as in (D). Red: random migration after gradient wash-out.

This was also reflected in the projection of the cell’s relative displacement angles ($cos⁡\theta$) estimated along the gradient direction ($\pi$) at each time point (Figure 3—figure supplement 2A), representing the angular alignment of the cells to the source direction. The cellular migration trajectories aligned with the source direction ($cos⁡\theta$ approached 1) during, and maintained this temporally after gradient removal, before returning to a migration pattern characteristic for stimulus absence or during uniform stimulation ($cos⁡\theta≈$ ~ 0, Figure 3C top, Figure 3—figure supplement 2B). Calculating the similarity between the kernel density distribution estimate (KDE) of the angular alignment distributions at each point in the gradient series with that in continuous stimulus absence, showed that the distributions approach each other only ~ 50 min after the gradient removal (Figure 3C, bottom; Figure 3—figure supplement 2C). Additionally, the calculated similarity between the KDE distributions during the gradient (5 hr) and the $50⁢m⁢i⁢n$ memory period further corroborated this finding (Figure 3—figure supplement 2C). The average memory phase in directional motility thus corresponds to the time-frame in which the memory in polarized $EGFR^{mCitrine}$ phosphorylation and cell shape is maintained (Figures 2E and 3C), indicating that the metastable signaling state is translated to a stable prolonged directed migration response after gradient removal.

To investigate whether the motility patterns during the gradient and the memory phase have equivalent characteristics, we fitted the motility data using a modified Ornstein-Uhlenbeck process (Uhlenbeck and Ornstein, 1930; Svensson et al., 2017) and used the extracted migration parameters to generate synthetic single-cell trajectories (Materials and methods). In absence of stimulus, the cellular motion resembled a random walk process (RW: Figure 3D right, Figure 3—figure supplement 2D, E middle), persistent random walk (PRW) was characteristic for the uniform stimulation case (Figure 3—figure supplement 2D, E right), whereas biased PRW described the migration in gradient presence (PBRW, Figure 3D- and Figure 3—figure supplement 2D, left, green trajectory part). Extending the bias duration during the interval of the experimentally observed memory phase (PB(t)RW) was necessary to reproduce the transient persistent motion after gradient removal (Figure 3D- and Figure 3—figure supplement 2D, left, blue trajectory part; Figure 3E and F; Figure 3—figure supplement 2F).

To corroborate the link between memory in polarized receptor activity, memory in polarized cell shape and memory in directional migration, we also quantified the directional migration of MCF10A cells when subjected to Lapatinib during gradient wash-out (Figure 3G). The directionality after gradient removal was significantly lower than in the case without Lapatinib (Figure 3H), suggesting that cells rapidly switch to a RW migration pattern upon gradient wash-out due to the absence of memory in polarized $EGFR^{mCitrine}$ phosphorylation (Figure 2G,I). Thus, single-cell motility trajectories that closely resembled the experimentally observed ones could be mimicked with the PB(t)RW simulation, where the bias duration corresponded to the duration of the gradient (Figure 3—figure supplement 2E left, 2G). Quantification of the average cells’ relative displacement angles showed as well that $cos⁡\theta$ approaches 0 exponentially after gradient removal (Figure 3I, Figure 3—figure supplement 2G), suggesting that majority of cells display absence of memory in directional migration under Lapatinib treatment.

In order to dissect better the cell-to-cell variability in this case, we also calculated memory duration from single cell $cos⁡\theta$ profiles. For this, single-cell trajectories were first smoothed using Kalman filter (Materials and methods). The quantification showed that majority of the cells displayed absence of or shorter memory in directional migration, with a mean value of ∼25 min (Figure 3—figure supplement 3A, B, D). Since under Lapatinib treatment, EGFR phosphorylation rapidly decays (Figure 2G), this residual memory in some cells likely results from memory in cytoskeletal asymmetries, as previously suggested (Prentice-Mott et al., 2016). Without Lapatinib treatment however, the duration of memory estimated from single-cell $cos⁡\theta$ profiles was of the order of 90 min (Figure 3—figure supplement 3A, C, E). If we therefore account in this case also the contribution of cytoskeletal memory, then the memory in directional migration which results from memory in polarized EGFR phosphorylation is on average ∼50 min, similar to the deduced values from the single-cell kymograph quantification (Figure 2E).

### Molecular working memory enables cells to navigate in dynamic chemoattractant fields

To test whether the identified memory enables cellular navigation in environments where signals are disrupted but also change over time and space, we subjected cells in the simulations and experiments to a changing growth factor field. The field was generated by a sequence of signals, starting with a dynamic gradient whose steepness changed over time, and was temporary disrupted for a time interval shorter than the interval of memory in cell polarization. This was followed by a second static gradient in the same direction, that after an equivalent disruption period was followed by a third dynamic gradient in the opposite direction (Figure 4A). The in silico migration simulations showed that the cell can sense the initial dynamic gradient and polarizes in the direction of maximal attractant concentration, resulting in directed migration (Figure 4B, Figure 4—figure supplement 1A, Figure 4—video 1). The simulations also predicted that the memory of the previously encountered signal localization enables maintaining robust directional migration even when the signal was disrupted, while still remaining sensitive to the newly emerging signal from the opposite direction. The in silico cell rapidly adapted the orientation when encountering the third signal, demonstrating that the proposed mechanism can also account for prioritizing newly encountered signals. Such a dynamic memory which enables information of previous signals to be temporally maintained while retaining responsiveness to upcoming signals, and thereby manipulate the stored information, in neuronal networks is described as a working memory (Atkinson and Shiffrin, 1968).

![Figure 4.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig4-v2.jpg)

**Figure 4.:** (A) Scheme of dynamic spatial-temporal growth factor field implemented in the simulations and experiments. Green(orange)/red: gradient presence/absence. (B) In silico cellular response to the sequence of gradients as depicted in (A), showing changes in EGFR activity, cellular morphology and respective motility trajectory over time. Trajectory color coding corresponding to that in (A), cell contour color coding with respective $E_{p}$ values as in Figure 1E. Cell size is magnified for better visibility. See also Figure 4—figure supplement 1A, Figure 4—video 1. (C) Representative MCF10A single-cell trajectory and cellular morphologies at distinct time-points, when subjected to dynamic EGF647 gradient field as in (A) (gradient quantification in Figure 4—figure supplement 1E). Trajectory color coding corresponding to that in (A). See also Figure 4—video 4. Full data set in Figure 4—figure supplement 1F. (D) Projection of cells’ relative displacement angles ($cos⁡\theta$) depicting their orientation towards the respective localized signals. Mean ± s.d. from n=12, N=5 is shown. (E) Corresponding kernel density estimates (intervals and color coding in legend). p-values: ***, p≤0.001, ns: not significant, KS-test.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) In silico obtained $E_{p}$ kymograph corresponding to Figure 4B. Parameters in Materials and methods. (B) In silico cellular response to a sequence of gradients as depicted on top, showing changes in EGFR phosphorylation, cellular morphology and respective motility trajectory over time. Trajectory color coding corresponding to scheme on top, cell contour color coding with respective $E_{p}$ values as in Figure 1E. Cell size is magnified for better visibility. See also Figure 4—video 2. (C) $E_{p}$ kymograph obtained for organization in the stable polarized state, when a cell is subjected to the gradient filed in Figure 4A. (D) Corresponding changes in cellular morphology and respective motility trajectory over time. Trajectory and $E_{p}$ color coding as in (B). Cell size is magnified for better visibility. See also Figure 4—video 3. (E) Quantification of a 15 hr dynamic fluorescein gradient at distinct time-points. Mean ± s.d. from N=3 is shown. (F) Divergence plots depicting MCF10A single-cell trajectories quantified during migration in dynamic EGF647 gradient field shown in (E). n=12, N=5. Trajectory color-coding corresponding to the scheme in Figure 4A. (G) Zoomed exemplary single-cell trajectories from (F).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/76825/elife-76825-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Top: Position of two simultaneous EGF gradients with different amplitudes in the numerical simulation. Bottom: Representative in silico kymograph of EGFR phosphorylation ($E_{p}$) for organization of the system at criticality. (B) Corresponding changes in cellular morphology and motility trajectory over time. Trajectory and $E_{p}$ color coding as in (A). Cell size is magnified for better visibility. See also Figure 4—video 5. (C) Same as in (A), only for organization in the stable polarized state. (D) Same as in (B), only for organization in the stable polarized state (corresponding to C). See also Figure 4—video 6.

If the signal disruption is however longer than the duration of the working memory, the simulations demonstrated that cells cannot integrate the signals. In turn, cells respond to each signal individually, as the directional migration after the memory is lost, resulting in a shorter range migration trajectory (Figure 4—figure supplement 1B, Figure 4—video 2). On the other hand, if the system has a long-term memory, as resulting from organization in the stable polarized regime, the simulations showed that cellular adaptation to a changing gradient field is hindered (Figure 4—figure supplement 1C,D Figure 4—video 3). The initial dynamic gradient shifted the system to the stable polarization steady state where it was maintained on a long-term, such that sensitivity to upcoming signals from the same direction was hindered. Even more, the cell could not resolve the conflicting information from a subsequent gradient from the opposite direction, as the signals induced high receptor activity on the opposed cell sides, resulting in halted migration. These results therefore highlight the importance of working memory for generating memory-guided migration over long trajectories.

We next tested these predictions experimentally by establishing an equivalent dynamic EGF647 spatial-temporal field in a controlled manner in the microfluidic chamber, and quantified the migratory profile of MCF10A cells (Figure 4—figure supplement 1E). The MCF10A cells sensed the initial dynamic gradient field and migrated in the direction of increasing chemoattractant concentration, maintaining the directionality even when the signal was temporary disrupted. Despite the memory in cell polarization, cells remained responsive and adapted the duration of directional migration when presented with a second static gradient from the same direction, and subsequently prioritized the third, newly encountered signal with opposed orientation (exemplary trajectory in Figure 4C, Figure 4—video 4, Figure 4—figure supplement 1F,G). Thus, the predictions derived by the numerical simulations quantitatively captured that the proposed mechanism of navigation enables integration of, and adaptation to changes in signal localization. The distinction between the simulations and the experiments (Figure 4B and C) is only in the details of the migration pattern, since the PBRW migration mode was not included in the physical model of the cell for simplicity. The temporal memory in directional migration as well as the continuous adaptation of MCF10A cells to novel cues was also reflected in the projection of the cell’s relative displacement angles (Figure 4D). The thereby derived KDE distributions during the first and second gradient (5–245 min; 275–335 min, respectively), as well as the corresponding intervals in which the gradient has been disrupted (245–275 min; 335–365 min, respectively) were statistically similar to each other, demonstrating that cells maintain the direction of migration in the intermittent intervals when the gradient was interrupted (Figure 4E). Moreover, these distributions statistically differed from the one characterizing cellular migration in continuous EGF647 absence (w/o EGF647, distribution symmetrically distributed around $cos⁡\theta=0$). The presence of the third gradient from the opposite direction (365–605 min) on the other hand, induced a shift in the respective KDE distribution to negative $cos⁡\theta$ values, reflecting that cells revert the direction of migration (established in ∼10 min). Furthermore, the reverse migration was maintained for approximately 20 min after wash-out of the third gradient (KDE 605–625 min). The statistical similarity between these two distributions demonstrates that cells also establish transient memory of the last detected signal, before reverting to a random walk migration mode (KDE 625–900 min similar to KDE w/o EGF647). These results therefore demonstrate that cells utilize molecular working memory to navigate in changing gradient fields.

Navigation in non-stationary fields, however, also necessitates integration of information, requiring active comparison during migration task execution. We therefore tested next numerically whether the identified organization at criticality enables resolving simultaneous gradients with different amplitudes from opposite sides, that temporally vary in time. In the simulations, the cell sensed the presence of both signals, as reflected in the respective increase in EGFR phosphorylation. However, the net polarization towards the higher amplitude gradient was dominant, resulting in a clear directional migration toward this signal (Figure 4—figure supplement 2A, B). After the gradient removal, the EGFR phosphorylation and the cell shape remained transiently polarized, manifesting memory of the recently encountered stronger signal that was translated to memory in directional migration, before the cell reverted to a random walk migration (Figure 4—video 5). In contrast, if the system has a long-term memory as resulting from organization in the stable polarized state, the simulations showed that EGFR phosphorylation increased almost equivalently with respect to both signals, despite the difference in signal amplitudes. This hindered the responsiveness of the cell such that migration could not be effectively exhibited (Figure 4—figure supplement 1C, D; Figure 4—video 6). These simulations therefore suggest that critical organization of receptor networks is in general crucial for performing complex cellular behavior that goes beyond simple stimulus-response associations.

## Discussion

Our data establishes that mammalian cells use a mechanism of working memory to navigate in complex environments where the chemical signals are disrupted or vary over time and space. Previous observations of memory in directed migration have been explained through the presence of bistable dynamics, where the transition from the basal to the polarized steady state and vice versa (after a memory phase) is regulated by two finely tuned thresholds. The authors however did not identify potential molecular elements that store this information, or regulate the thresholds (Skoge et al., 2014). Similarly, the remaining proposed models of polarization also rely on steady-state description of the basal and polarized states (Levine et al., 2002; Mori et al., 2008; Goryachev and Pokhilko, 2008; Beta et al., 2008; Trong et al., 2014), and thereby cannot account for the rapid adaptation to changes in signal localization.

The mechanism of transient memory we report here is realized on a molecular level by a prolonged polarized phosphorylation state of a receptor tyrosine kinase. Dynamically, this state emerges for organization at criticality, where a slow-escaping remnant from the polarized state or a dynamically metastable ‘ghost’ state is generated, and endows cells with robust transient maintenance of directional migration after signal removal. Although the observed memory in directional migration is in part supported by the memory in cytoskletal asymmetries as previously suggested (Prentice-Mott et al., 2016), the memory in receptor signaling we identify here provides a crucial bridge between the rapid receptor phosphorylation/dephosphorylation events and the long-range cellular migration. In particular, the organization at criticality endows the system with a slow time-scale through which the prolonged receptor phosphorylation state can be maintained on average for ∼40–50 min after signal removal, which in turn maintains the polarized cell shape, and thereby directional migration in absence of a signal. Moreover, we have demonstrated that this memory arising from a metastable state uniquely ensures the ability of cells to quickly adapt to changes in the external environment.

Thus, our results suggest that in order to balance between a robust response and adaptation to novel signals, cell utilize an optimal receptor amount at the plasma membrane that corresponds to organization at criticality. The theoretical analysis suggest that the closeness of the receptor amount to the one corresponding to the critical transition is reflected in the memory duration. It can be therefore suggested that the observed variability in the experimentally identified memory length likely results from cell-to-cell variability in receptor concentration at the plasma membrane. Moreover, these results also suggest that a higher number of sensory units at the plasma membrane does not necessarily imply improved sensitivity of cells, but rather counterintuitively , leads to permanent memory of the initially encountered signal. This in turn will limit the cellular responsiveness to upcoming signal changes. It would be therefore of interest to study whether receptor networks are self-organized at criticality through an active sensing mechanism, or this feature has been fine-tuned through evolution, as a means for optimizing sensing and computational capabilities of cells.

Our work furthermore suggest that this general mechanism of a system poised at criticality can explain a wide range of biologically relevant scenarios, from the integration of temporally and spatially varying signals, to how extracellular information is transformed into guidance cues for memory-directed migration. Such memory-guided navigation is advantageous when migration must be realized over long and complex trajectories through dense tissues where the chemical cues are disrupted or only locally organized (Lämmermann et al., 2013). We have demonstrated here that the molecular working memory in cell polarization and therefore the capabilities of cells to navigate in a complex environment are an emergent feature of receptor networks.

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
      <td>Cell line (Homo sapiens)</td>
      <td>MCF-7</td>
      <td>ECACC</td>
      <td>Cat.No.86012803</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>MCF10A</td>
      <td>ATCC</td>
      <td>CRL-10317</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>EGFR-mCitrine</td>
      <td>Baumdick et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PTB-mCherry</td>
      <td>Fueller et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>cCbl-BFP</td>
      <td>Fueller et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Fibronectin</td>
      <td>Sigma-Aldrich</td>
      <td>F0895-1MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Collagen</td>
      <td>Sigma-Aldrich</td>
      <td>C9791-50MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lapatinib</td>
      <td>Cayman chemicals</td>
      <td>Cay11493-10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hoechst 33,342</td>
      <td>Thermo Fisher Sc.</td>
      <td>62,249</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM)</td>
      <td>PAN Biotech</td>
      <td>Cat. # P04-01500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MEM Amino Acids Solution (50 x)</td>
      <td>PAN Biotech</td>
      <td>Cat. # P08 32,100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Penicillin- Streptomycin</td>
      <td>PAN Biotech</td>
      <td>Cat. # P06 07100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fetal Bovine Serum</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. # F7524</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EGF</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. # E9644</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrocortisone</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #H-0888</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cholera toxin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #C-8052</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Insulin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #I-1882</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Horse Serum</td>
      <td>Invitrogen</td>
      <td>26050088</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FuGENE6</td>
      <td>Promega</td>
      <td>E2691</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python</td>
      <td>Python software foundation</td>
      <td>RRID:SCR_008394</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>MathWorks</td>
      <td>RRID:SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XPPAUT</td>
      <td>http://www.math.pitt.edu/~bard/xpp/xpp.html</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Trackmate</td>
      <td>https://doi.org/10.1016/j.ymeth.2016.09.016</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji, ImageJ</td>
      <td>https://doi.org/10.1038/nmeth.2019</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>EGF-Alexa647</td>
      <td>Sonntag et al., 2014</td>
      <td>Prof. Luc Brunsveld, University of Technology, Eindhoven</td>
      <td>Methods</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Cellasic ONIX plates</td>
      <td>Merck Chemicals</td>
      <td>M04G-02-5PK</td>
      <td>Methods</td>
    </tr>
  </tbody>
</table>

### Cell culture

MCF7 cells (sex: female, ECACC, Cat. No. 86012803) were grown at 37 °C and 5% CO2 in Dulbecco’s Eagle’s medium (DMEM) (PAN-Biotech, Germany), supplemented with 10% inactivated Fetal Calf Serum (FCS) (Sigma-Aldrich), 100 ng ml–1 L-Glutamine, 0.5 mg ml–1 non-essential amino acids, 100 µg ml-1 penicillin and 100 µg ml-1 streptomycin (PAN-Biotech, Germany). Serum starvation was performed by culturing the cells in DMEM supplemented with 0.5% FCS, 100 µg ml-1 penicillin and 100 µg ml-1 streptomycin (PAN-Biotech, Germany). MCF10A cells (sex: female, ATCC-CRL 10317) were grown at 37 °C and 5% CO2 in Mammary Epithelial Cell Growth Basal medium (MEBM from Lonza Pharma & Biotech), supplemented with 5% Horse Serum (HS) (Invitrogen), 20 ng ml–1 EGF (Sigma-Aldrich), 0.5 mg ml–1 hydrocortisone (Sigma-Aldrich), 100 ng ml–1 cholera toxin (Sigma-Aldrich), 10 µg ml-1insulin (Sigma-Aldrich), 100 µg ml-1 penicillin and 100 µg ml-1 streptomycin. Serum starvation was performed by culturing the cells in the DMEM supplemented with 0.5% HS, 0.5 mg ml–1 hydrocortisone (Sigma-Aldrich), 100 ng ml–1 cholera toxin (Sigma-Aldrich), 100 µg ml-1 penicillin and 100 µg ml-1 streptomycin. MCF7 and MCF10A cells were authenticated by Short Tandem Repeat (STR) analysis and did not contain DNA sequences from mouse, rat and hamster (Leibniz-Institut DSMZ). Cells were regularly tested for mycoplasma contamination using MycoAlert Mycoplasma detection kit (Lonza).

### Transfection and cell seeding

For $EGFR^{mCitrine}$ polarization experiments, 2.5 × 105 MCF7 cells were seeded per well in a six-well Lab-Tek chamber (Nunc) until 80% confluence was reached. After 9–10 hr of seeding, transient transfection was performed with a total of 1 µg of plasmids ($E⁢G⁢F⁢R^{m⁢C⁢i⁢t⁢r⁢i⁢n⁢e}$, $P⁢T⁢B^{m⁢C⁢h⁢e⁢r⁢r⁢y}$ and $c⁢C⁢b⁢l^{B⁢F⁢P}$ at ratio 4:3:4 by mass) using FUGENE6 (Roche Diagnostics) transfection reagent and Opti-MEM (Gibco - Thermo Fisher Scientific) according to manufacturer’s procedure. All plasmids were generously provided by Prof. P. Bastiaens, MPI of Molecular Physiology, Dortmund. Cells were incubated for 7–8 hr to allow the expression of the transfected proteins prior to experiments. To detach the cells, the growth media was discarded and cells were washed once with DPBS (PAN Biotech) before adding 100 µl Accutase (Sigma-Aldrich). After $10min$ incubation period at 37 °C and 5% CO2, fresh growth media was added, and the cell density and viability was measured using cell counter (Vi-CELL XR Cell Viability Analyzer System). After spinning down, the cells were diluted to 10 × 106 cells/ml. The M04-G02 microfluidic gradient plates (Merck Chemicals) were primed for usage by flowing cell culture growth media through the cell chamber for $5min$ and cells were subsequently seeded according to manufacturer’s instructions.

For migration experiments with uniform $E⁢G⁢F^{647}$ stimulation, 6-well Lab-Tek plates were coated with Collagen (Sigma-Aldrich) in 0.1 M Acetic acid (Sigma-Aldrich) for MCF7 (100 µg cm-2), and Fibronectin (Sigma-Aldrich) in Phosphate-Buffered Saline (DPBS) (PAN-Biotech) for MCF10A cells (2 µg ml-1), and stored in incubator at 37 °C overnight for evaporation. Excessive media was removed and the wells were washed with DPBS before seeding cells. MCF7 cells were seeded and transfected as described above. In the case of MCF10A cells, 1 × 105 cells per well were used for seeding. For migration experiments with gradient EGF647 stimulation, MCF7 cells were transferred to the coated M04-G02 microfluidic gradient plates as described above. Before seeding, MCF10A cells were detached from 6 well Lab-Teks by discarding the growth media and washing once with DPBS (PAN Biotech) before adding 100 µl Accutase (Sigma-Aldrich). After 20–30 min incubation period at 37 °C and 5% CO2, fresh cell growth media was added, and the cell density and viability were measured using a cell counter (Vi-CELL XR Cell Viability Analyzer System). After spinning down, the cells were diluted to 2 × 106 cells/ml, and subsequently seeded in the microfluidic plates according to manufacturer’s instructions.

### Reagents

For gradient quantification, Fluorescein (Sigma Aldrich) was dissolved in Dulbecco’s modified Eagle’s medium (with 25 mM HEPES, without Phenol Red) (PAN Biotech). Imaging media: DMEM without Phenol Red was mixed with $25m⁢M$ HEPES. For nuclear staining, 20 mM Hoechst 33342 (Thermo Fisher Scientific) was mixed with DPBS and diluted to 2 µM working concentration. EGFR inhibitor Lapatinib (Cayman Chemical, Ann Arbor, MI) was solubilized in DMSO (Thermo Fisher Scientific) to a stock concentration of 5 mM and stored at –20 °C.

### Confocal and wide-field microscopy

Confocal images were recorded using a Leica TCS SP8i confocal microscope (Leica Microsystems) with an environment-controlled chamber (Life Imaging Services) maintained at 37 °C and HC PL APO 63 x/1.2 N.A / motCORR CS2 water objective (Leica Microsystems) or a HC PL FLUOTAR 10 x/0.3 N.A. dry objective (Leica Microsystems). mCitrine, mCherry and Alexa647 were excited with a 470nm–670nm pulsed white light laser (Kit WLL2, NKT Photonics) at 514 min, 561 nm, and 633 nm, respectively. BFP and Hoechst 33342 (Thermo Fisher Scientific) were excited with a $405nm$ diode laser. The detection of fluorescence emission was restricted with an Acousto-Optical Beam Splitter (AOBS): BFP (425nm–448nm), Hoechst 33342 (425nm–500nm), mCitrine (525nm–551nm), mCherry (580nm–620nm), and Alexa647 (655nm–720nm). Transmission images were recorded at a 150–200% gain. To suppress laser reflection, Notch filter 488/561/633 was used whenever applicable. When using the dry objective for migration experiments, the pinhole was set to 3.14 airy units and 12-bit images of 512 × 512 pixels were acquired in frame sequential mode with 1 x frame averaging. When using the water objective for polarization experiments, the pinhole was fixed (1.7 airy units) for all channels. The Leica Application Suite X (LAS X) software was used.

Wide field images were acquired using an Olympus IX81 inverted microscope (Olympus Life Science) equipped with a MT20 illumination system and a temperature controlled C02 incubation chamber at 37 °C and 5% CO2. Fluorescence and transmission images were collected via a 10 x/0.16 NA air objective and an Orca CCD camera (Hamamatsu Photonics). Hoechst 33342 fluorescence emission was detected between 420nm–460nm via DAPI filter, mCitrine fluorescence emission between 495nm–540nm via YFP filter and Alexa647 fluorescence emission between 705nm–745nm via Cy5 filter. The xCellence (Olympus) software was used.

### Gradient establishment for polarization and migration experiments

The CellAsic Onix Microfluidic Platform (EMD Millipore) was used for gradient cell migration and $EGFR^{mCitrine}$ phosphorylation polarization experiments. For $EGFR^{mCitrine}$ phosphorylation polarization experiments, 1 hr gradient stimulation was established using CellASIC ONIX2 software as follows. (i) Pre-stimulus: Imaging media was flowed from well groups 3 and 4 (CellAsic Onix Manual - https://www.merckmillipore.com/) at low pressure (2.5 kPa) for 5 min. (ii) Gradient establishment: After closing well group 3, pre-loaded EGF647 (10 ng mL–1) was flowed through well group 2 and imaging media from well group 4 at high pressure (15 kPa) for 15 min (iii) Gradient maintenance: The pressure was reduced to 10 kPa for 45 min. (iv) Washout: After closing well groups 2 and 4, imaging media was flowed from well groups 3 and 5 at high pressure (15 kPa) for 15 min and maintained at low pressure (7 kPa) for 165 min. For single gradient migration experiments, this protocol was modified as follows: in step (iii), gradient maintenance was done for 285 min. In step (iv), maintenance was at low pressure for 585 min. 30 ng mL–1 EGF647 was used. For polarization experiments with inhibitor, the same protocol as for polarization experiments was used, except well group 3 and 5 were filled with 1 µM Lapatinib solution and in step (i) well group 3 was kept closed. For single cell gradient migration experiment with inhibitor, 3 µM Lapatinib was used.

For migration experiments under subsequent gradient stimuli / gradient quantification, the following changes in the steps were used: (ii) well group 2 with 30 ng mL–1 EGF647/ 2.5 µM Fluorescein was used. (iii) The gradient maintenance was done for 225 min. (iv) Washout: imaging media was flowed from well groups 3 and 4 at high pressure (15 kPa) for 15 min and maintained at low pressure (7 kPa) for 15 min. (v) Second gradient establishment: After closing well group 3, EGF647 (30 ng ml-1)/ 2.5 µM Fluorescein was flowed from well group 2 and imaging media from well group 4 at high pressure (15 kPa) for 15 min. (vi) The second gradient formed was maintained by reducing the pressure to 10 kPa for 45 min. (vii) Washout: imaging media was flowed from well groups 3 and 4 at high pressure (15 kPa) for 15 min and maintained at low pressure (7 kPa) for 15 min. (viii) Third gradient establishment: After closing well group 4, EGF647 (30 ng mL–1) / 2.5 µM Fluorescein was flowed from well group 5 and imaging media from well group 3 at high pressure (15 kPa) for 15 min. (ix) The third reversed gradient was maintained by reducing the pressure to 10 kPa for 225 min. (x) Washout: imaging media was flowed from well groups 3 and 4 at high pressure (15 kPa) for 15 min and maintained at low pressure (7 kPa) for $285min$.

### Imaging E⁢G⁢F⁢Rm⁢C⁢i⁢t⁢r⁢i⁢n⁢e phosphorylation polarization and single cell migration

Transfected $MCF7−EGFR^{mCitrine}$ cells transferred to M04G-02 gradient plates as described above were incubated for at least 3 hr, followed by serum starvation for at least 6 hr before imaging. Existing cell media was substituted right before imaging with imaging media. Confocal imaging for multiple positions at $1min$ time interval using adaptive auto-focus system and the water objective was performed concurrently during the duration of the experiment using the Leica TCS SP8i.

For migration experiments under uniform EGF647 stimulation, confocal laser scanning microscopy / transmission imaging of live $MCF7−EGFR^{mCitrine}$ / MCF10A cells was done on a Leica TCS SP8i or Olympus IX81 for multiple positions at 3 min and 2 min time interval respectively, using the 10 × dry objective for 14 hr.

### EGF647 / Fluorescein gradient quantification

hEGF647 was generated in the lab of Prof. P. Bastiaens, MPI of molecular Physiology, Dortmund, using the His-CBD-Intein-(Cys)-hEGF-(Cys) plasmid (Sonntag et al., 2014), kindly provided by Prof. Luc Brunsveld, University of Technology, Eindhoven. Human EGF was purified from E. coli BL21 (DE3), N-terminally labeled with Alexa647-maleimide as described previously (Sonntag et al., 2014) and stored in PBS at –20 °C. To quantify the spatial extent of the EGF647 /Fluorescein gradient, gradients were generated following the protocol described in sub-section 5.6 in plates without cells or matrix coating. Confocal images of Alexa647 /GFP channel were acquired at $1min$ interval. A rectangular region of interest (including the perfusion channels and the culture chamber) was used to obtain an averaged pixel intensity profile using FIJI at each time point. This spatial profile was averaged across multiple experiments and then scaled with the mean intensity value in the perfusion channel, which corresponds to the applied EGF647 /Fluorescein concentration.

### Quantifying EGFRmCitrine phosphorylation in single cells

To quantify plasma membrane $EGFR^{mCitrine}$ phosphorylation in live $MCF7−EGFR^{mCitrine}$ cells, single-cell masks were obtained from the $EGFR^{mCitrine}$ channel at each time-point using FIJI (https://imagej.net/Fiji). All pixels within the obtained boundary were radially divided into two segments of equal areas (Stanoev et al., 2018), and the outer segment was taken to represent the plasma membrane. For the kymograph analysis, at each time point, the plasma membrane segment was divided into 4 quadrants in anti-clockwise direction, and each was divided into 5 spatial bins (Figure 2A). The fraction of phosphorylated $EGFR^{mCitrine}$ in each bin, $i$ was estimated as:

$$
E⁢G⁢F⁢R_{p}^{i}⁢(t)=\frac{P⁢T⁢B_{P⁢M}^{i}⁢(t)/(P⁢T⁢B_{T}⁢(t)-P⁢T⁢B_{e⁢n⁢d⁢o}⁢(t))}{E⁢G⁢F⁢R_{P⁢M}^{i}⁢(t)/E⁢G⁢F⁢R_{T}⁢(t)}
$$

where $P⁢T⁢B_{P⁢M}^{i}⁢(t)$ and $E⁢G⁢F⁢R_{P⁢M}^{i}⁢(t)$ are respectively the $PTB^{mCherry}$ and $E⁢G⁢F⁢R^{m⁢C⁢i⁢t⁢r⁢i⁢n⁢e}$ fluorescence at $i^{t⁢h}$ plasma membrane bin, $P⁢T⁢B_{T}⁢(t)$ and $E⁢G⁢F⁢R_{T}⁢(t)$ - respective total fluorescence in the whole cell, $P⁢T⁢B_{e⁢n⁢d⁢o}⁢(t)$ – the $PTB^{mCherry}$ fluorescence on vesicular structures in the cytoplasm. Endosomal structures were identified from the cytosol by intensity thresholding (1.5 s.d. percentile) and $PTB^{mCherry}$ fluorescence from these structures was subtracted from the $P⁢T⁢B_{T}⁢(t)$, to correct for the $PTB^{mCherry}$ fraction bound to the phosphorylated $EGFR^{mCitrine}$ on endosomes.

Temporal profile of the fraction of phosphorylated $EGFR^{mCitrine}$ on the plasma membrane was obtained using:

$$
E⁢G⁢F⁢R_{p}⁢(t)=\frac{\frac{\sum_{i=1}^{20}P⁢T⁢B_{P⁢M}^{i}⁢(t)}{(P⁢T⁢B_{T}⁢(t)-P⁢T⁢B_{e⁢n⁢d⁢o}⁢(t))}}{\frac{\sum_{i=1}^{20}E⁢G⁢F⁢R_{P⁢M}^{i}⁢(t)}{(E⁢G⁢F⁢R_{T}⁢(t))}}
$$

and then normalized as:

$$
EGFR_{p}(t)=\frac{EGFR_{p}(t)−<EGFR_{p}>_{t\in[0,5min]}}{max_{t}(EGFR_{p}(t))−<EGFR_{p}>_{t\in[0,5min]}}
$$

with <> being the temporal average in the pre-stimulation interval $t\in[0,5⁢m⁢i⁢n]$. The fraction of liganded receptor was calculated using:

$$
E⁢G⁢F-E⁢G⁢F⁢R⁢(t)=\frac{E⁢G⁢F_{P⁢M}}{E⁢G⁢F⁢R_{P⁢M}}⁢(t)
$$

To classify single cells into non-activated, activated (polarized $EGFR^{mCitrine}$ phosphorylation) and pre-activated (uniformly distributed $EGFR^{mCitrine}$ phosphorylation) upon gradient EGF647 stimulation (Figure 2—figure supplement 2A, B), the following method was applied. To identify pre-activated cells, a Gaussian Mixture Model (GMM) was fitted to the histogram of $(E⁢G⁢F⁢R_{p}^{i})_{t\in[0,5⁢m⁢i⁢n]}$ values from all the analysed cells, and the intersection point between the two normal distributions was identified. If more than 30% of the $(E⁢G⁢F⁢R_{p}^{i})_{t\in[0,5⁢m⁢i⁢n]}$ pixel intensity values for any cell lie above the intersection point, the cell is classified as pre-activated. To distinguish between the non-activated and activated cells in the remaining population, average $EGFR^{mCitrine}$ phosphorylation value ($E⁢G⁢F⁢R_{p}$) per cell was estimated during the pre-stimulation ($t\in[0,5⁢m⁢i⁢n]$) and the stimulation period ($t\in[5⁢m⁢i⁢n,65⁢m⁢i⁢n]$) ($<EGFR_{p}>_{t\in[0,65]}$) from the temporal $EGFR^{mCitrine}$ phosphorylation profiles. Histogram of the respective $E⁢G⁢F⁢R_{p}$ values was again fitted with a GMM model. All cells with an average $<EGFR_{p}>_{t\in[0,65]}$ value lying below the intersection point were considered to be non-activated, whereas those above - activated.

The average of the spatial projection of the fraction of phosphorylated $EGFR^{mCitrine}$ from single-cell kymographs (Figure 2—figure supplement 1C) was generated from the 20 cells that were polarized in the direction of the EGF647 gradient. For each cell, a temporal average of $E⁢G⁢F⁢R_{p}$ per bin was calculated for the duration of the gradient ($t\in[5⁢m⁢i⁢n,65⁢m⁢i⁢n]$) and the bin with the maximal $E⁢G⁢F⁢R_{p}$ value was translated to $\pi$. The profiles were then smoothened using a rolling average with a window of 7 bins. The resulting profiles were then averaged over all cells and mean ± s.d. is shown.

The local spatial EGF647 distribution around single cells (Figure 2—figure supplement 1F) was estimated as follows: the cell mask obtained using the $EGFR^{mCitrine}$ images were dilated outwards by 8 pixels to account for possible ruffles, and then by additional 15 pixels. The secondary rim of 15 pixels around the cell mask was used to calculate the spatial distribution of EGF647 outside single cells. This outer contour was divided in 20 bins as for the kymographs, and EGF647 intensity was quantified in each bin. The angle between the direction of EGF647 and the direction of EGFR phosphorylation was calculated as the amount of radial bins between the maxima in the spatial projections. This bin-distance was then translated into an angle under the assumption of a circular perimeter.

In order to identify the characteristic features of the $EGFR^{mCitrine}$ phosphorylation profile during the transition from polarized to unpolarized state, the single-cell $E⁢G⁢F⁢R_{p}⁢(t)$ profiles with and without Lapatinib treatment after gradient wash-out were fitted to an inverse sigmoid function given by,

$$
f⁢(t)=\frac{a_{0}}{a^{n}+t^{n}}
$$

were a0, $a$ are constants and $n$ is the Hill-coefficient (examples in Figure 2—figure supplement 2E, F). Non-linear least square method (python package curve fit) was used to perform the fitting. Under normal conditions (w/o Lapatinib), $a∼10$, $a_{0}∼10^{3}$ and $n∼2.88$ fitted well the data ($R^{2}∼0.79$). The same function however could not describe the EGFRp profiles in the Lapatinib treatment experiment (median $R^{2}∼0.33$). The Lapatinib treatment profiles were therefore fitted by fixing $a=10$, and leaving a0 and $n$ as free parameters, as they determine the upper plateau and the steepness of the drop to the basal level. In this case, $a_{0}∼19$ and $n∼1.28$ were identified from the fitting (median $R^{2}∼0.84$, Figure 2—figure supplement 2E, G). From the fitted profiles in both cases, half-life was estimated to be the time frame in which 50% of $EGFR^{mCitrine}$ phosphorylation is lost after EGF647 removal.

### Estimating memory duration in EGFRmCitrine phosphorylation polarization

The duration of memory in $EGFR^{mCitrine}$ phosphorylation polarization in single cells was estimated from the temporal profile of the fraction of plasma membrane area with high $EGFR^{mCitrine}$ phosphorylation during and after gradient removal (Figure 2D and E). For this, the single-cell kymographs were normalized to a maximal value of 1 using

$$
EGFR_{p}^{i}(t)=\frac{EGFR_{p}^{i}(t)−<EGFR_{p}>_{t\in[0,5min]}}{max_{t}(EGFR_{p}(t))−<EGFR_{p}>_{t\in[0,5min]}}
$$

yielding the value of phosphorylated $EGFR^{mCitrine}$ per bin $i$ per time point $t$. Using the mean of $E⁢G⁢F⁢R_{p}+s.d.$ over the whole experiment duration as a threshold, all $E⁢G⁢F⁢R_{p}^{i}⁢(t)$ lying above the threshold were taken to constitute the area of polarized $EGFR^{mCitrine}$ phosphorylation. To account for different bin sizes, at each timepoint, the area of all bins with $E⁢G⁢F⁢R_{p}$ above the threshold was summed and divided by the respective total cell area, yielding the temporal evolution of the fraction of polarized cell area (FPA) (Figure 2D). The end of the memory duration per cell was identified as the time point at which $FPA_{per−cell}<(FPA_{average}−s.d.)$ in 3 consecutive time points (Figure 2E).

### Quantifying morphological changes in response to EGF647 in experiments and simulations

Morphological changes of polarized cells were quantified using the solidity (Figure 2H1) of each cell at each time point and the directed protrusive area towards and away from the gradient (Figure 1G and H; Figure 2—figure supplement 2H). The solidity $\sigma$ is the ratio between the cell’s area $A_{c⁢e⁢l⁢l}$ and the area of the convex hull $A_{c⁢o⁢n⁢v⁢e⁢x}$ ($\sigma=\frac{A_{c⁢e⁢l⁢l}}{A_{c⁢o⁢n⁢v⁢e⁢x}}$). The memory duration in cell morphology was calculated from the single-cell solidity profiles, and corresponds to the time-point at which the solidity is below mean-s.d. estimated during gradient presence. The directed cell protrusion area was estimated by comparing single cell masks at two consecutive time points. To reduce noise effects, the masks were first subjected to a 2D Gaussian filtering using the $f⁢i⁢l⁢t⁢e⁢r⁢s.g⁢a⁢u⁢s⁢s⁢i⁢a⁢n$ function from the $s⁢c⁢i⁢p⁢y$ python package. Protrusions were considered if the area change was greater than 10 pixels or 1.2 µm2 per time point. The front and the back of the cells were determined by identifying an axis that runs perpendicular to the gradient and through the cell nucleus of the initial time point. The directed cell protrusion area was then obtained using $\frac{A_{p⁢r⁢o⁢t,f⁢r⁢o⁢n⁢t}}{A_{f⁢r⁢o⁢n⁢t}}-\frac{A_{p⁢r⁢o⁢t,b⁢a⁢c⁢k}}{A_{b⁢a⁢c⁢k}}$. The final profiles of directed protrusive area were smoothed using 1D Gaussian filtering with the $f⁢i⁢l⁢t⁢e⁢r⁢s.g⁢a⁢u⁢s⁢s⁢i⁢a⁢n⁢_⁢f⁢i⁢l⁢t⁢e⁢r⁢1⁢d$ function from the $s⁢c⁢i⁢p⁢y$ python package. For the equivalent quantification from the simulations, the same procedures were applied without an area threshold. The memory duration was estimated as the time point at which the directed protrusive area crosses zero after the gradient removal.

### Quantification of single-cell migration and duration of memory in directed cell migration

Single cell migration trajectories were extracted using Trackmate (Tinevez et al., 2017) in Fiji (Schindelin et al., 2012) using Hoechst 33342/transmission channel. From the positional information (x and y coordinates) of individual cell tracks, quantities such as Motility, Directionality and $cos⁡\theta$ were extracted using custom made Python code (Python Software Foundation, versions 3.7.3, https://www.python.org/). Directionality was calculated as displacement over total distance and statistical significance was tested using two-sided Welch’s t-test. To quantify the memory duration in directed single-cell migration, the Kernel Density Estimate (KDE) from $cos⁡\theta$ quantification in the continuous absence of EGF647 (uniform case, between 250–300 min) was compared with a moving window KDE (size of 5 time points) from the gradient migration profile, using two sided Kolmogorov-Smirnov test. To verify the absence of memory when cells were treated with Lapatinib during gradient wash-out, a moving window KDE (5 time points) from $cos⁡\theta$ obtained in this case was compared to the KDE in continuous absence of EGF647 (uniform case Figure 3—figure supplement 2B, between 250–300 min) using two sided Kolmogorov-Smirnov test (Figure 3I). Furthermore, the KDE between 300–350 min and 350–840 min (after gradient removal) was statistically equivalent to the KDE in continuous absence of EGF647, confirming the rapid switch from directed to random-walk migration in the Lapatinib case (Figure 3—figure supplement 2H). To estimate the time required for complete reversal of cell migration direction when the cells were subjected to a gradient from opposite direction, KDE distributions were compared between the following time windows: 275–335 min (second gradient), 335–365 min, 365–385 min, 375–385 min, and 365–605 min (third gradient).

To quantify the motility patterns of MCF10A cells in absence, uniform or gradient $E⁢G⁢F^{647}$ stimulation, we fitted the experimentally obtained single cell migration trajectories using modified Ornstein-Uhlenbeck process (mOU) (Uhlenbeck and Ornstein, 1930) that is defined by the Langevin equation for the velocity vector $ν$:

$$
\frac{d⁢ν⁢(t)}{d⁢t}=-\frac{1}{\tau}⋅ν⁢(t)+\frac{\sqrt{2⁢D}}{\tau}⋅(ξ⁢(t)+b⁢(t))
$$

where $ξ⁢(t)$ represents a white noise component, D is a diffusion coefficient characteristic of a Brownian motion, $\tau$ is the persistence time and $b⁢(t)$ models the contribution of the time-dependent bias. The experimental data was fitted to obtain values of D and $\tau$. In order to estimate D, Mean Square Displacement (MSD) was calculated from the single cell tracks using $MSD(t)=<|x_{i}(t)−x_{i}(0)|^{2}>$, where $x_{i}⁢(t)$ is the tracked position of i-th cell in the 2D plane, <> is the average across all single cell tracks, and $|.|$ is the Euclidean distance (Selmeczi et al., 2005). To estimate D, the obtained MSD profile was fitted with a linear function ($=4⁢D⁢t$). Goodness of Fit for the different experimental conditions: 0 ng/ml EGF647, $R^{2}=0.975$; for uniform 20 ng/ml EGF647 stimulation, $R^{2}=0.995$. In order to estimate $\tau$, Velocity Auto-Correlation Function $VACF(t)=<ν_{i}(t)⋅ν_{i}(0)>$, where $ν_{i}⁢(t)$ is the measured velocity of $i$-th cell at time t, was fitted with a mono exponential function ($=ϕ_{0}⋅e^{\frac{-t}{\tau}}$). Goodness of Fit: for 0 ng/ml EGF647 case - Standard Error of Estimate $S⁢E⁢O⁢E=0.0261$; for uniform 20 ng/ml EGF647 stimulation case, $S⁢E⁢O⁢E=0.0570$. Fitted values: for 0 ng/ml EGF647 case, $\tau=11.105$, $D=0.425$; for uniform 20 ng/ml EGF647 stimulation case, $\tau=38.143$, $D=2.207$; bias $b⁢(t)=0.134$.

To compute the duration of memory in directional migration after gradient removal for individual cells (Figure 3—figure supplement 3), single cell migration tracks were first smoothened using a Kalman-filter (python package filterpy.kalman) by predicting the cell position and velocity. The cell’s displacement angles relative to the gradient direction ($cos⁡\theta$) were calculated for each cell at each timepoint, rendering single-cell $cos⁡\theta$ plots (Figure 3—figure supplement 3B,C). The memory duration was then calculated as the point where three consecutive timepoints in the $cos⁡\theta$ profiles fall below a threshold $cos⁡\theta$ value of 0.75.

### Reconstructing state-space trajectories from temporal EGFRmCitrine phosphorylation profiles

The state-space reconstruction in Figure 2F and G was performed using the method of time-delay. For a time series of a scalar variable, a vector $x⁢(t_{i})$, $i=1,...N$ in state-space in time ti can be constructed as following

$$
X⁢(t_{i})=[x(t_{i}),x(t_{i}+d),..,x(t_{i}+(m-1)d)]
$$

where $i=1$ to $N−(m−1)d$, d is the embedding delay, $m$ - is a dimension of reconstructed space (embedding dimension). Following the embedding theorems by Takens (Takens, 1980; Sauer et al., 1991), if the sequence $X⁢(t_{i})$ consists of scalar measurements of the state of a dynamical system, then under certain genericity assumptions, the time delay embedding provides a one-to-one image of the original set, provided $m$ is large enough. The embedding delay was identified using the timeLag function (based on autocorrelation), the embedding dimension using the estimateEmbeddingDims function (based on the nearest-neighbours method), and the state-space reconstruction using the buildTakens function, all from the nonlinearTseries package in R (https://cran.r-project.org/web/packages/nonlinearTseries/index.html). Before state-space reconstructions, time series were smoothened using the Savitzky-Golay filter function in Python. For Figure 2F, $d=26$, $d_{e}=3$; for Figure 2G, $d=50$, $d_{e}=3$.

### Theoretical consideration of the navigation mechanism in a generalized reaction-diffusion signaling model

We consider a generalized form of a (mass-conserved) reaction-diffusion (RD) model of an $M$ ($U\inR^{M}$) component system in $N$ ($x\inR^{N}$) dimensional space

$$
\frac{∂U(x,t)}{∂t}=F(U(x,t))+D⋅∇^{2}U(x,t)
$$

where $F\inR^{M}$ is the reaction term, $D$ is a $M\timesM$ diagonal matrix of diffusion constants $D_{j},j=1,…,M$, and $\nabla^{2}$ is the Laplacian operator. Standard analysis of such models relies on linear stability analysis to find the conditions for a Turing-type instability (Turing, 1952), such that the symmetric steady state becomes unstable and an asymmetric polarized state is stabilized. By its nature, the linear stability analysis makes no prediction about the transition process itself, and thereby the type of bifurcation that underlies it. To provide quantitative description of the symmetry breaking transition in reaction-diffusion models, local perturbation analysis can be applied (Holmes et al., 2015). However, this analysis is mainly restricted to models characterized with large diffusion discrepancy between the signaling components. The conditions for a pitchfork bifurcation ($P⁢B$)-induced transition in a generic RD model therefore have to be formally defined. Let $U_{s}=(u_{i⁢s})$ for $i=1,...,M$, be the stable homogeneous symmetric steady state of the RD system. Consider a linear perturbation of the form

$$
U(x,t)=U_{s}+\deltaU(x)e^{(\lambdat)},     \deltaU(x)\inR^{M}
$$

where $\delta⁢U⁢(x)$ is the spatial and $e^{(\lambda⁢t)}$ is the temporal part of the perturbation. Substituting Equation 10 in Equation 9 yields a linearized eigenvalue equation whose solution can be determined by solving the characteristic equation, $F_{\lambda}=det(\lambdaI_{M\timesM}−J_{M\timesM})=0$. J is the Jacobian matrix of the system defined by $J_{i⁢j}=\frac{\partial⁡F_{i}⁢(U⁢(x,t))}{\partial⁡U_{j}},i=1,….,M,j=1,…..,M$.

The system exhibits a $P⁢B$ if, an odd eigenfunction $\delta⁢U⁢(x)$ such that $\delta⁢U⁢(-x)=-\delta⁢U⁢(x)$, taken in the limit $\lambda→0$, fulfills the following condition (Paquin-Lefebvre et al., 2020):

$$
lim\lambda→0⁡F_{\lambda}=d⁢e⁢t⁢(J)=0.
$$

When this conditions is satisfied, the symmetric, homogeneous steady state of the system undergoes a pitchfork bifurcation and an inhomogeneous steady state (IHSS) with two branches of asymmetric steady states emerges. In terms of polarization, these branches correspond to front-back-polarized states, where the orientation depends on the direction of the external signal (Figure 1A, Figure 1—figure supplement 1A).

To identify whether the PB is of sub-critical type, and thereby identify the presence of an $S⁢N_{P⁢B}$, a weakly nonlinear analysis of Equation 9 must be performed to obtain description of the amplitude dynamics of the inhomogeneous state. This can be achieved using an approximate analytical description of the perturbation dynamics based on the Galerkin method (Becherer et al., 2009; Rubinstein et al., 2012; Bozzini et al., 2015). For simplicity, we outline the steps for a one-dimensional system ($N=1$). As we are interested in the description of a structure of finite spatial size (i.e. finite wavelength $k$), the final solution of the PDE is expanded around the fastest growing mode, km into a superposition of spatially periodic waves. That means that $u⁢(x,t)\inU$ can be written as:

$$
u⁢(x,t)≈\sumn=-∞+∞(u_{n}⁢(t)⁢e^{n⁢i⁢k_{m}⁢x}+u_{n}^{*}⁢(t)⁢e^{-n⁢i⁢k_{m}⁢x})
$$

where $u_{n}⁢(t)$ is the complex amplitude of the $n^{t⁢h}$ harmonics. Let the amplitude corresponding to the leading harmonics $(n=1)$ is $ϕ⁢(t)$. After assuming that the amplitude of every other harmonics can be written as a power series of $ϕ⁢(t)$, substituting Equation 12 into Equation 9 allows to write an equation that describes the evolution of $ϕ⁢(t)$. In the case when the resulting equation is of Stuart-Landau type:

$$
\frac{d⁢ϕ}{d⁢t}=c_{1}⁢ϕ+c_{2}⁢ϕ^{3}-c_{3}⁢ϕ^{5}
$$

with $c_{1},c_{2},c_{3}>0$, this corresponds to the normal form of a sub-critical pitchfork bifurcation (Strogatz, 2018). Together with the condition given by Equation 11, the existence of a sub-critical PB for the full system (Equation 9) is guaranteed. A numerical or analytical analysis of Equation 13 enables the identification of the position of the $S⁢N_{P⁢B}$.

### Modeling EGFR phosphorylation polarization dynamics

The dynamics of the experimentally identified spatially distributed EGFR sensing network (Figure 1B, Figure 1—figure supplement 1B) is described using the following one-dimensional system of partial differential equations (PDEs):

$$
\frac{∂[E_{p}]}{∂t}= f_{1}([E_{p}],[E−E_{p}],[RG_{a}],[N2_{a}],[EGF_{t}])+D_{E_{p}}\frac{∂^{2}[E_{p}]}{∂x^{2}}\frac{∂[E−E_{p}]}{∂t}= f_{2}([E_{p}],[E−E_{p}],[EGF_{t}])+D_{E−E_{p}}\frac{∂^{2}[E−E_{p}]}{∂x^{2}}\frac{∂[RG_{a}]}{∂t}= f_{3}([E_{p}],[E−E_{p}],[RG_{a}])+D_{RG_{a}}\frac{∂^{2}[RG_{a}]}{∂x^{2}}\frac{∂[N2_{a}]}{∂t}= f_{4}([E_{p}],[E−E_{p}],[N2_{a}])
$$

with

$$
 f_{1}=([E_{t}]−[E_{p}]−[E−E_{p}])(\alpha_{1}([E_{t}]−[E_{p}]−[E−E_{p}])+\alpha_{2}[E_{p}]+\alpha_{3}[E−E_{p}])−\gamma_{1}[RG_{a}][E_{p}]−\gamma_{2}[N2_{a}][E_{p}]−k_{on}([EGF_{t}]−[E−E_{p}])[E_{p}]^{2}+1/2k_{off}[EE_{p}];f_{2}=k_{on}([EGF_{t}]−[E−E_{p}])([E_{p}]^{2}+([E_{t}]−[E_{p}]−[E−E_{p}])^{2})−k_{off}[E−E_{p}];f_{3}=k_{1}([RG_{t}]−[RG_{a}])−k_{2}[RG_{a}]−\beta_{1}[RG_{a}]([E_{p}]+[E−E_{p}]);
$$

and

$$
f_{4}=ϵ⁢(k_{1}⁢([N⁢2_{t}]-[N⁢2_{a}])-k_{2}⁢[N⁢2_{a}]+\beta_{2}⁢([E_{p}]+[E-E_{p}])⁢([N⁢2_{t}]-[N⁢2_{a}])).
$$

The reaction terms are described in details in Stanoev et al., 2018. In brief, $[E-E_{p}]$ is the phosphorylated ligand-bound dimeric EGFR, $[E_{p}]$ - ligandless phosphorylated EGFR, $[E_{t}]$ - total amount of EGFR, $[R⁢G_{a}],[R⁢G_{t}]$ and $[N⁢2_{a}],[N⁢2_{t}]$ - the active and total amount of the membrane localized PTPRG and the ER-bound PTPN2, respectively. Both, the receptor and the deactivating enzymes have active and inactive states, and the model equations describe their state transition rates. Therefore, mass is conserved in the system and the total protein concentrations of the three species ($[E_{t}]$, $[R⁢G_{t}]$ and $[N⁢2_{t}]$) are constant parameters. Autonomous, autocatalytic and ligand-bound-induced activation of ligandless EGFR ensue from bimolecular interactions with distinct rate constants $\alpha_{1-3}$, respectively. Other parameters are as follows: $k_{1}/k_{2}$ — activation/inactivation rate constants of the phosphatases, $\beta_{1}/\beta_{2}$ - receptor-induced regulation rate constants of $P⁢T⁢P⁢R⁢G/P⁢T⁢P⁢N⁢2$, $\gamma_{1}/\gamma_{2}$ - specific reactivity of the enzymes ($P⁢T⁢P⁢R⁢G/P⁢T⁢P⁢N⁢2$) towards the receptor. The EGFR-PTPN2 negative feedback is on a time scale ($ϵ$) approximately two orders of magnitude slower than the phosphorylation-dephosphorylation reaction, as estimated from the ~ 4 min recycling time of $E⁢G⁢F⁢R_{p}$ (Stanoev et al., 2018). This enables, when necessary, to consider a quasi-steady state approximation for the dynamics of PTPN2 for simplicity:

$$
[N⁢2_{a}]_{q⁢s⁢s}=[N⁢2_{t}]⋅\frac{(k_{1}+\beta_{2}⋅([E_{p}]+[E-E_{p}]))}{k_{1}+k_{2}+\beta_{2}⋅([E_{p}]+[E-E_{p}])}
$$

$[E⁢G⁢F_{t}]$ denotes the total ligand concentration. Assuming that at low, physiologically relevant EGF doses, the ligand will be depleted from the solution due to binding to EGFR (Lauffenburger and Linderman, 1996), ligand-binding unbinding was explicitly modeled ($k_{o⁢n}$, $k_{o⁢f⁢f}$) in Equation 14, with values corresponding to the experimentally identified ones.

The diffusion terms model the lateral diffusion of the EGFR and PTPRG molecules on the plasma membrane, whereas PTPN2 is ER-bound and does not diffuse. Single particle tracking studies have demonstrated that EGFR molecules on the plasma membrane occupy three distinct mobility states, free, confined and immobile, with the occupations of the free and immobile states decreasing and increasing significantly after EGF stimulation, respectively (2 min after EGF stimulation, corresponding with the time-scale of EGF binding) (Ibach et al., 2015). In the reaction-diffusion (RD) simulations therefore for simplicity, it is assumed that $D_{E-E_{p}}≈0$, whereas diffusion constants of same order are assumed for the ligandless EGFR and PTPRG ($D_{E_{p}}∼D_{R⁢G_{a}}$).

### Analytical consideration for an S⁢NP⁢B existence in the EGFR network

To identify analytically the existence of a $S⁢N_{P⁢B}$ in the EGFR receptor network, we performed a weakly nonlinear analysis as described in the general consideration (Section. Theoretical consideration of the navigation mechanism in a generalized reaction-diffusion signaling model). For this, we considered the system Equation 14, where the dynamics of PTPN2 is at quasi-steady state (Equation 15), $[E-E_{p}]=0$, and rest of the dependent and independent variables were scaled to have a dimensionless form. Let $[E_{p}~]=[E_{p}]/E_{0}$, $[R⁢G_{a}~]=[R⁢G_{a}]/R⁢G_{0}$, $x~=x/x_{0}$, $\tau=t/t_{0}$, such that $t_{0}=1/(k_{1}+k_{2})$, $E_{0}=k_{1}/\beta_{2}$, $R⁢G_{0}=(k_{1}+k_{2})/\gamma_{1}$ and $t_{0}/x_{0}^{2}=1/D_{E_{p}}$. Substituting these into Equation 14 yields the system of dimensionless equations:

$$
\frac{\partial⁡[E_{p}~]}{\partial⁡\tau}=q_{1}+q_{2}⁢[E_{p}~]+q_{3}⁢[E_{p}~]^{2}-[R⁢G_{a}~]⁢[E_{p}~]-\frac{q_{4}⁢(1+[E_{p}~])⁢[E_{p}~]}{(1+k+[E_{p}~])}+\frac{\partial^{2}⁡[E_{p}~]}{\partial⁡x~^{2}}\frac{\partial⁡[R⁢G_{a}~]}{\partial⁡\tau}=r_{1}-[R⁢G_{a}~]-r_{2}⁢[R⁢G_{a}~]⁢[E_{p}~]+D⁢\frac{\partial^{2}⁡[R⁢G_{a}~]}{\partial⁡x~^{2}}
$$

with $q_{1}=\frac{\alpha_{1}⋅[E_{t}]^{2}}{(k_{1}+k_{2})⋅\beta_{2}}$, $q_{2}=\frac{(\alpha_{2}−2⋅\alpha_{1})⋅[E_{t}]}{k_{1}+k_{2}}$, $q_{3}=\frac{(\alpha_{1}−\alpha_{2})⋅k_{t}}{(k_{1}+k_{2})⋅\beta_{2}}$, $q_{4}=\frac{\gamma_{2}⋅[N2_{t}]}{k_{1}+k_{2}}$, $k=k_{2}/k_{1}$, $r_{1}=\frac{k_{1}⋅[RG_{t}]⋅\gamma_{1}}{(k_{1}+k_{2})^{2}}$, $r_{2}=\frac{\beta_{1}⋅k_{1}}{(k_{1}+k_{2})⋅\beta_{2}}$ and $D=\frac{D_{RG_{\alpha}}}{D_{E_{p}}}$.

We further simplify the system Equation 16 by taking the Talyor series expansion of the quasi-steady state approximation of $[N⁢2_{a}]$ around $E_{s}$, the steady state of $[E_{p}]~$

$$
\frac{q_{4}(1+[E_{p}~])[E_{p}~]}{1+k+[E_{p}~]}= q_{7}+q_{8}[E_{p}~]+q_{9}[E_{p}~]^{2}+o([E_{p}~]^{2})
$$

with $q_{7}=\frac{E_{s}q_{4}}{1+k+E_{s}}−\frac{E_{s}q_{4}(1+k)}{(1+k+E_{s})^{2}}$, $q_{8}=\frac{E_{s}q_{4}}{1+k+E_{s}}+\frac{q_{4}(1+k)}{(1+k+E_{s})^{2}}(1−E_{s})$, and $q_{9}=\frac{q_{4}(1+k)}{(1+k+E_{s})^{2}}$, thus yielding:

$$
\frac{∂[E~_{p}]}{∂_{\tau}}=q_{9}+q_{10}[E~_{p}]+q_{11}[E~_{p}]^{2}−[RG~_{a}][E~_{p}]+\frac{∂^{2}[E~_{p}]}{∂x~^{2}}\frac{∂[RG~_{a}]}{∂_{\tau}}=r_{1}−[RG~_{a}]−r_{2}[RG~_{a}][E~_{p}]+D\frac{∂^{2}[RG~_{a}]}{∂x~^{2}}
$$

with $q_{9}=q_{1}−q_{7},q_{10}=q_{2}−q_{8}$ and $q_{11}=q_{3}−q_{9}$.

To avoid long expression in the further analysis, we re-name the dependent variables as $u_{1}=[E_{p}~]$ and $u_{2}=[R⁢G_{a}~]$, and the independent variables as $x~=x$, $\tau=t$. The system Equation 16 therefore obtains the generic form:

$$
\frac{\partial⁡u_{1}}{\partial⁡t}=F_{1}⁢(u_{1},u_{2})+\frac{\partial^{2}⁡u_{1}}{\partial⁡x^{2}}\frac{\partial⁡u_{2}}{\partial⁡t}=F_{2}⁢(u_{1},u_{2})+D⁢\frac{\partial^{2}⁡u_{2}}{\partial⁡x^{2}}.
$$

In order to perform linear stability analysis, a one-dimensional projection of Equation 19 is considered,

$$
\frac{d⁢u_{1⁢f}}{d⁢t}=F_{1}⁢(u_{1⁢f},u_{2⁢f})-(u_{1⁢f}-u_{1⁢b})=G_{1}⁢(u_{1⁢f},u_{2⁢f},u_{1⁢b})\frac{d⁢u_{2⁢f}}{d⁢t}=F_{2}⁢(u_{1⁢f},u_{2⁢f})-D⁢(u_{2⁢f}-u_{2⁢b})=G_{2}⁢(u_{1⁢f},u_{2⁢f},u_{2⁢b})\frac{d⁢u_{1⁢b}}{d⁢t}=F_{1}⁢(u_{1⁢b},u_{2⁢b})-(u_{1⁢b}-u_{1⁢f})=G_{3}⁢(u_{1⁢b},u_{2⁢b},u_{1⁢f})\frac{d⁢u_{2⁢b}}{d⁢t}=F_{2}⁢(u_{1⁢b},u_{2⁢b})-D⁢(u_{2⁢b}-u_{2⁢f})=G_{4}⁢(u_{1⁢b},u_{2⁢b},u_{2⁢f})
$$

The simplified one-dimensional geometry assumes a model composed of two compartments (front and back), resembling a projection of the membrane along the main diagonal of the cell. The standard approach of modeling the diffusion along the membrane in this case is simple exchange of the diffusing components. The one-dimensional projection, as demonstrated below, preserves all of the main features of the PDE model.

Let, $U_{s}=(u_{1⁢f⁢s}u_{2⁢f⁢s}u_{1⁢b⁢s}u_{2⁢b⁢s})$ be the stable symmetric steady state of the system ($u_{1⁢f⁢s}=u_{1⁢b⁢s}$, $u_{2⁢f⁢s}=u_{2⁢b⁢s}$). A small amplitude perturbation on this symmetric steady state of the form,

$$
(u_{1⁢f}⁢(t)u_{2⁢f}⁢(t)u_{1⁢b}⁢(t)u_{2⁢b}⁢(t))=(u_{1⁢f⁢s}u_{2⁢f⁢s}u_{1⁢b⁢s}u_{2⁢b⁢s})+(\delta⁢u_{1⁢f}\delta⁢u_{2⁢f}\delta⁢u_{1⁢b}\delta⁢u_{2⁢b})⋅e^{\lambda⁢t}
$$

yields a linearized equation,

$$
\lambda⁢(\frac{d⁢\delta⁢u_{1⁢f}}{d⁢t}\frac{d⁢\delta⁢u_{2⁢f}}{d⁢t}\frac{d⁢\delta⁢u_{1⁢b}}{d⁢t}\frac{d⁢\delta⁢u_{2⁢b}}{d⁢t})=J⁢(\delta⁢u_{1⁢f}\delta⁢u_{2⁢f}\delta⁢u_{1⁢b}\delta⁢u_{2⁢b})
$$

where

$$
J=(\frac{∂G_{1}}{∂u_{1f}}\frac{∂G_{1}}{∂u_{2f}}\frac{∂G_{1}}{∂u_{1b}}0\frac{∂G_{2}}{∂u_{1f}}\frac{∂G_{2}}{∂u_{2f}}0\frac{∂G_{2}}{∂u_{2b}}\frac{∂G_{3}}{∂u_{1f}}0\frac{∂G_{3}}{∂u_{1b}}\frac{∂G_{3}}{∂u_{2b}}0\frac{∂G_{4}}{∂u_{2f}}\frac{∂G_{4}}{∂u_{1b}}\frac{∂G_{4}}{∂u_{2b}})
$$

is the Jacobian of the system evaluated at the symmetric steady state. In order to identify existence of $P⁢B$ in the system, the condition given in Equation 11 should be satisfied for an odd mode of the perturbation. For the one-dimensional projection (Equation 20), the odd mode of the perturbation $(\deltaU(−x)=−\deltaU(x))$ must yield: $\delta⁢u_{1⁢f}=-\delta⁢u_{1⁢b}$ and $\delta⁢u_{2⁢f}=-\delta⁢u_{2⁢b}$. Substituting this into Equation 22 to obtain $F_{-}⁢(\lambda)$, in the limit $\lambda→0$ renders:

$$
lim\lambda→0F_{−}(\lambda)=det((\frac{∂G_{1}}{∂u_{1f}}+\frac{∂G_{3}}{∂u_{1b}})−(\frac{∂G_{1}}{∂u_{1b}}+\frac{∂G_{3}}{∂u_{1f}})(\frac{∂G_{1}}{∂u_{2f}}+\frac{∂G_{2}}{∂u_{2b}})(\frac{∂G_{2}}{∂u_{1f}}+\frac{∂G_{4}}{∂u_{1b}})(\frac{∂G_{2}}{∂u_{2f}}+\frac{∂G_{4}}{∂u_{2b}})−(\frac{∂G_{2}}{∂u_{2b}}+\frac{∂G_{4}}{∂u_{2f}}))=0
$$

Thus, there exists parameter set for which existence of PB in the system Equation 20 is guaranteed.

To identify whether the PB is sub-critical and thereby identify existence of a $S⁢N_{P⁢B}$, the solution of the system Equation 19 is approximated as in Equation 12:

$$
u⁢(x,t)=ϕ⁢(t)⁢e^{i⁢k_{m}⁢x}+ϕ^{*}⁢(t)⁢e^{-i⁢k_{m}⁢x}+u_{0}⁢(t)+\sumn=23(u_{n}⁢(t)⁢e^{n⁢i⁢k_{m}⁢x}+u_{n}^{*}⁢(t)⁢e^{-n⁢i⁢k_{m}⁢x})v⁢(x,t)=ϕ⁢(t)⁢e^{i⁢k_{m}⁢x}+ϕ^{*}⁢(t)⁢e^{-i⁢k_{m}⁢x}+v_{0}⁢(t)+\sumn=23(v_{n}⁢(t)⁢e^{n⁢i⁢k_{m}⁢x}+v_{n}^{*}⁢(t)⁢e^{-n⁢i⁢k_{m}⁢x})
$$

The expansion is taken to $n=3^{r⁢d}$ order, rendering an amplitude equation of $5^{t⁢h}$ order. As described in Becherer et al., 2009, the complex coefficients of the $n=0^{t⁢h},n=2^{n⁢d}$ and $n=3^{r⁢d}$ harmonics can be approximated as power series of $ϕ⁢(t)$. Substituting into Equation 19 allows to derive these coefficients. This yields a system of coupled ODEs representing the time evolution of the complex amplitudes, in this case, for $ϕ⁢(t)$, $u_{0}⁢(t)$, $v_{0}⁢(t)$, $u_{1}⁢(t)$, $v_{1}⁢(t)$, $u_{2}⁢(t)$, $v_{2}⁢(t)$, $u_{3}⁢(t)$ and $v_{3}⁢(t)$. Assuming that the dynamics of the higher order harmonics reaches their steady state much faster than the leading perturbation does, the derivatives of their amplitudes can be set to zero. This allows to obtain expressions of the amplitudes purely as functions $ϕ$ and the parameters of the system as:

$$
u_{0}⁢(ϕ)=(\frac{1}{q_{10}}⁢(2⁢(1-q_{11})-\frac{q_{9}}{|ϕ|^{2}}))⁢|ϕ|^{2}v_{0}⁢(ϕ)=(\frac{r_{1}}{|ϕ|^{2}}-2⁢r_{2})⁢|ϕ|^{2}u_{2}⁢(ϕ)=u_{2}^{(2)}⁢ϕ^{2}v_{2}⁢(ϕ)=v_{2}^{(2)}⁢ϕ^{2}u_{3}⁢(ϕ)=u_{3}^{(3)}⁢ϕ^{3}v_{3}⁢(ϕ)=v_{3}^{(3)}⁢ϕ^{3}
$$

where $u_{2}^{(2)}=\frac{1-q_{11}}{q_{10}-4⁢k_{m}^{2}}$, $v_{2}^{(2)}=\frac{-r_{2}}{1+4⁢D⁢k_{m}^{2}}$, $u_{3}^{(3)}=\frac{u_{2}^{(2)}+v_{2}^{(2)}-2⁢q_{11}⁢u_{2}^{(2)}}{q_{10}-9⁢k_{m}^{2}}$ and $v_{3}^{(3)}=\frac{-r_{2}⁢(u_{2}^{(2)}+v_{2}^{(2)})}{1+9⁢D⁢k_{m}^{2}}$. The dynamics of the leading harmonics $(n=1)$ can be written as:

$$
\frac{d⁢ϕ}{d⁢t}=c_{1}⁢ϕ+c_{2}⁢ϕ^{3}-c_{3}⁢ϕ^{5}
$$

where $c_{1}=q_{10}-k_{m}^{2}-r_{1}+\frac{q_{9}⁢(1-2⁢q_{11})}{q_{10}}$, $c_{2}=(1-q_{11})⁢(2⁢q_{11}-1)⁢(\frac{2}{q_{10}}-\frac{1}{q_{10}-4⁢k_{m}^{2}})+r_{2}⁢(2+\frac{1}{1+4⁢D⁢k_{m}^{2}})$ and $c_{3}=2⁢q_{11}⁢u_{2}^{(2)}⁢u_{3}^{(3)}-u_{2}^{(2)}⁢v_{3}^{(3)}$. Equation 26 is of Stuart-Landau type and represents a normal form of a sub-critical pitchfork bifurcation. This shows the existence of $S⁢N_{P⁢B}$ in the EGFR network.

To corroborate this, we also performed numerical bifurcation analysis on one-dimensional projection (Equation 20) where the reaction terms have the form as defined in Equation 14, including the full form for $[N⁢2_{a}]$, when $[E-E_{p}]=0$. The bifurcation analysis (Figure 1—figure supplement 1C) was obtained using the Xppaut software package (Ermentrout, 2016). The parameters in the model Equation 14 have been described in Stanoev et al., 2018, where they were calibrated with experimental data: $\alpha_{1}=0.001$, $\alpha_{2}=0.3$, $\alpha_{3}=0.7$, $\beta_{1}=11$, $\beta_{2}=1.1$, $k_{1}=0.5$, $k_{2}=0.5$, $g_{1}=1.9$, $g_{2}=0.1$, $k_{o⁢n}=0.05$, $k_{o⁢f⁢f}=0.28$, $ϵ=0.01$, $R⁢G_{t}=1$, $N⁢2_{t}=1$; and the diffusion-like terms have been scaled from the values derived in Orr et al., 2005: $D_{E_{p}}~=0.02$, $D_{R⁢G_{a}}~=0.02$ (see also Supplementary file 1).

The bifurcation analysis is performed with respect to total EGFR concentration at the plasma membrane in order to reveal all possible dynamical regimes of the system. This analysis demonstrates that for the spatially distributed EGFR network, the homogeneous steady state (HSS, gray solid line, Figure 1—figure supplement 1C) representing basal non-polarized state losses stability via a symmetry-breaking pitchfork bifurcation ($P⁢B$), which gives rise to a polarized state represented via an inhomogeneous steady states (IHSS). The polarized state is stabilised via saddle-node bifurcations ($S⁢N_{P⁢B}$) (Figure 1—figure supplement 1C, magenta branched lines). There is a coexistence between the HSS and the IHSS before the $P⁢B$, rendering it sub-critical. The IHSS (Koseska et al., 2013) that gives rise to the stable polarized state is a single attractor that describes a heterogeneous state with two branches corresponding to orientation of the front-back-polarized state. The IHSS solution is therefore fundamentally distinct from a bistable system where the high and the low phosphorylation states correspond to two different homogeneous steady states. As the IHSS is a single attractor, the high and low phopshorylation state are interdependent, rendering the $P⁢B$ a unique mechanism for generating robust front-back polarization.

We next describe the dynamical basis of the polarization and memory of polarization in details. We assume that the steady state EGFR concentration at the plasma membrane corresponds to organization at criticality, before the $S⁢N_{P⁢B}$. For this receptor concentration, only the basal unpolarized state (HSS) is stable (Figure 1—figure supplement 1A, top left, schematic representation). In the presence of a spatially inhomogeneous EGF signal however, the system undergoes a series of complex transitions through which the topology of the phase space changes. In particular, the inhomogeneity introduced by the localized signal leads to unfolding of the pitchfork bifurcation, such that for the same organization (the given EGFR concentration), only the polarized state (the IHSS) is stable (Figure 1—figure supplement 1A, top right). This unfolding of the $P⁢B$ therefore enables robust transition from basal to polarized state. When the EGF signal is removed, the system undergoes again topological phase space changes. However, in this transition, the system does not revert back to the unpolarized state immediately, but rather it is transiently maintained in the ”ghost” of the $S⁢N_{P⁢B}$ that is lost in this transition (Figure 1—figure supplement 1A, low). This is manifested as a transient memory of the polarized state, after which the system rapidly reverts to the basal state.

The reaction diffusion simulations were performed by assuming PTPN2 at quasi-steady state. The cell boundary was represented with a 1D circular domain of length $L=2⁢\pi⁢R$ (where $R=2⁢\mu⁢m$) which was then divided into 20 equal bins. The diffusion terms were approximated by central difference method, enabling for conversion of the PDE system to a system of ordinary differential equations (ODEs). Stochastic simulations with additive white noise were implemented by adding $\sigma⋅d⁢W_{t}$ ($\sigma=0.02$, $d⁢W_{t}$ is sampled from a normal distribution with mean 0 and variance 0.01) in the equation for $[E_{p}]$. The stochastic sdeint Python package was used. Parameters: $D_{E_{p}}=D_{RG_{a}}=0.008\mum^{2}/min$. DEp was taken from Orr et al., 2005 and scaled to correspond to a cell with perimeter $L$ in the simulations. For organization in the homogenous symmetric steady states (the basal and pre-activated states), organization at criticality or in the stable polarized state (IHSS), $E_{t}\in{1.1,1.85,1.26,1.35}$ respectively, time step was set to 0.01 min, other parameters as above. Periodic boundary conditions were used. To mimic the dynamic nature of $E⁢G⁢F^{647}$ gradient, a Gaussian function on a periodic window with varying amplitude and standard deviation was used (shape shown in Figure 1D, top). To represent the state-space trajectory (Figure 1F, bottom), stochastic realization of the one-dimensional projection of the full system (as for the bifurcation analysis) was used.

### Physical model of single-cell chemotaxis

To describe signal-induced cell shape changes and subsequent cell migration, we combined the dynamical description of the gradient sensing capability of the EGFR network (Equation 14, Figure 1B) together with a physical model for cellular migration, thereby implicitly modeling the signal-induced cell shape changes (Figure 1C). In order to couple a mechanical model of the cell with the biochemical EGFR signaling model as a means to simulate large cellular deformations, we utilized the Level Set Method (LSM) (Osher and Sethian, 1988) as described in Yang et al., 2008. Briefly, the cell boundary at time $t$ is described on a two-dimensional Cartesian grid by the closed-contour $Γ⁢(t)={x|Ψ⁢(x,t)=0}$, that represent the zero-level set of the potential function $Ψ⁢(x,t)$, taken to have an initial form:

$$
Ψ(x,0)={−d(x,Γ),if x\inSd(x,Γ),if x∉S0,if x\inΓ
$$

where $S$ identifies the area occupied by the cell and $d(x,Γ)$ is the distance of position $x$ to the curve $Γ$. Thus, the cell membrane is represented implicitly through the potential function which is defined on the fixed Cartesian grid, eliminating the need to parameterize the boundary, and thereby enabling to handle complex cell boundary geometries.

The shape of the cell ($Γ⁢(x,t)$) evolves according to the Hamilton-Jacobi equation:

$$
\frac{∂Ψ(x,t)}{∂t}+v(x,t)⋅∇Ψ(x,t)=0
$$

The vector $v⁢(x,t)$ is the velocity of the level set moving in the outward direction, thereby intrinsically describing the cell’s membrane protrusion and retraction velocities that are driven by internally generated mechanical forces (e.g. actin polymerization or myosin-II retraction, Bray, 2000). To determine how these forces translate to membrane velocity, a mechanical model that describes the viscoelastic behavior of the cell represented as a viscoelastic cortex surrounding a viscous core, is implemented. Following Yang et al., 2008, the cortex connecting the cell membrane and the cytoplasm is represented by a Voigt model parallel connection of an elastic element kc and a viscous element $\tau_{c}$, whereas the cytoplasm is modeled as a purely viscous element, $\tau_{a}$, which is placed in series with the Voigt model.

Let $l⁢(x,t)$, $x\inΓ⁢(t)$ be the viscoelastic state of the cell at time $t$ and at a position $x$ on the membrane, such that $|l|$ represents the length of the numerous parallel unconnected spring-damper systems. The viscoelastic state of the cell then evolves according to:

$$
\frac{-k_{c}}{\tau_{c}}⁢l⁢(t)+\frac{1}{\tau_{c}}⁢P_{total}⁢(t)=\nabla⁡l⋅v⁢(t)+\frac{\partial⁡l⁢(t)}{\partial⁡t}
$$

where ∇ is the gradient operator, the pressure $P_{total}⁢(t)=P_{prot}⁢(t)+P_{retr}⁢(t)+P_{area}⁢(t)-P_{ten}⁢(t)$ is sum of the protrusion, retraction, area conservation, and cortical tension pressures, respectively. The EGFR signaling state ($[E_{p}]$) directly determines the protrusion/retraction pressure, since high/low signaling activity triggers actin polymerization / myosin-II retraction following: $P_{prot}(t)=$ $K_{prot}(([E_{p}](t)−<[E_{p}](t)>)$$/([E_{p}]_{max}(t)−<[E_{P}](t)>))n$ and $P_{ret}(t)=$ $−K_{retr}((<[E_{p}]>−[E_{p}])$$/(<[E_{P}]>−[E_{p}]_{max}))n$, where <.> denotes mean at the membrane, $K_{p⁢r⁢o⁢t}$, $K_{r⁢e⁢t⁢r}$ - proportionality constants. The cell is assumed to be flat with uniform thickness, such that the 2D area ($A⁢(t)$) of the cell is conserved ($P_{area}⁢(t)=K_{a⁢r⁢e⁢a}⁢(A⁢(0)-A⁢(t))⁢n$), $K_{a⁢r⁢e⁢a}$ - proportionality constant. The pressure generated by the cortical tension therefore depends only on the 2D local surface curvature and the 2D equilibrium pressure, rendering the rounding pressure due to cortical tension to be $P_{ten}⁢(t)=K_{t⁢e⁢n}⁢(κ⁢(Γ)-1/R)⁢n$, with $κ⁢(x)$ being the local membrane curvature, R - initial cell radius, was set to 2 $\mu⁢m$, and $K_{t⁢e⁢n}$ - proportionality constant. The local membrane velocity $v⁢(x)$, $x\inΓ⁢(t)$ depends both on the viscoelastic nature of the cell and on the effective pressure profile ($P_{total}⁢(t)$) and is given by,

$$
v=\frac{−k_{c}}{\tau_{c}}l+(\frac{1}{\tau_{c}}+\frac{1}{\tau_{a}})P_{total}
$$

For the simulations in Figures 1 and 4 and Figure 4—figure supplements 1 and 2 first the stochastic PDEs (Equation 14) are solved and the kymographs of the signalling ($[E_{p}]$) activity are generated. The viscoelastic state is initialized with zero value on the membrane, $l⁢(x,0)=0$. At each time point, $P_{total}$ is estimated, as well as the local membrane velocity using Equation 30. This velocity is then used to evolve both the viscoelastic state (Equation 29) and the potential function (Equation 27).

The spatial discretization of these advection equations (Equations 28 and 29) was performed using the upwindENO2 scheme, as described in the Level Set Toolbox (Mitchell, 2007) and was integrated with first-order forward Euler method. The time step was set to $0.01⁢m⁢i⁢n$ and the potential function was solved on a 2D Cartesian grid with spatial discretization of 5 points per µm. All the codes were custom implemented in Python. Parameters: $k_{c}=0.1nN/\mum^{3}$, $\tau_{c}=0.08nNmin/\mum^{3}$, $\tau_{a}=0.1nNmin/\mum^{3}$, $K_{prot}=0.08nN/\mum^{2}$, $K_{retr}=0.05nN/\mum^{2}$, $K_{area}=0.02nN/\mum^{4}$, $K_{ten}=0.1nN/\mum$. $K_{ten}$ was taken from the literature, corresponding to an experimentally measured range of cell cortical tension values (Cartagena-Rivera et al., 2016). The rest of the parameters were selected to match the cell migration speed during gradient and memory phase, estimated from the experiments (Figure 3A, $v=0.49\pm0.173⁢\mu⁢m/m⁢i⁢n$).
