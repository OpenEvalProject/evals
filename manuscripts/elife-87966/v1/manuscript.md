# Free volume theory explains the unusual behavior of viscosity in a non-confluent tissue during morphogenesis

## Authors

- Rajsekhar Das<sup>1</sup> ([ORCID: 0000-0003-2626-7259](https://orcid.org/0000-0003-2626-7259))
- Sumit Sinha<sup>2</sup> ([ORCID: 0000-0002-8364-5175](https://orcid.org/0000-0002-8364-5175))
- Xin Li<sup>1</sup> ([ORCID: 0000-0002-2510-2236](https://orcid.org/0000-0002-2510-2236))
- TR Kirkpatrick<sup>3</sup>
- D Thirumalai<sup>1</sup> ([ORCID: 0000-0003-1801-5924](https://orcid.org/0000-0003-1801-5924)) †

### Affiliations

1. Department of Chemistry, University of Texas at Austin Austin United States ([ROR:00hj54h04](https://ror.org/00hj54h04))
2. Department of Physics, University of Texas at Austin Austin United States ([ROR:00hj54h04](https://ror.org/00hj54h04))
3. Institute for Physical Science and Technology, University of Maryland College Park United States ([ROR:047s2c258](https://ror.org/047s2c258))

† Corresponding author

## Abstract

A recent experiment on zebrafish blastoderm morphogenesis showed that the viscosity (η) of a non-confluent embryonic tissue grows sharply until a critical cell packing fraction (ϕS). The increase in η up to ϕS is similar to the behavior observed in several glass-forming materials, which suggests that the cell dynamics is sluggish or glass-like. Surprisingly, η is a constant above ϕS. To determine the mechanism of this unusual dependence of η on ϕ, we performed extensive simulations using an agent-based model of a dense non-confluent two-dimensional tissue. We show that polydispersity in the cell size, and the propensity of the cells to deform, results in the saturation of the available free area per cell beyond a critical packing fraction. Saturation in the free space not only explains the viscosity plateau above ϕS but also provides a relationship between equilibrium geometrical packing to the dramatic increase in the relaxation dynamics.

## Introduction

There is great interest in characterizing the mechanical and dynamical properties of embryonic tissues because they regulate embryo development (Kimmel et al., 1995; Keller et al., 2008; Petridou and Heisenberg, 2019; Hannezo and Heisenberg, 2019; Autorino and Petridou, 2022). Measurements of bulk properties, such as viscosity and elastic modulus, and the dynamics of individual cells through imaging techniques, have been interpreted by adapting concepts developed to describe phase transitions (PTs), glass transition, and active matter (Shaebani et al., 2020; Marchetti et al., 2013; Kirkpatrick and Thirumalai, 2015; Bär et al., 2020).

Several experiments have shown that during embryo morphogenesis, material properties of the tissues change dramatically (Morita et al., 2017; Mongera et al., 2018; Barriga et al., 2018; Petridou et al., 2019; Petridou et al., 2021). Of relevance to our study is a remarkable finding that provided evidence that a PT occurs during zebrafish blastoderm morphogenesis, which was analyzed using rigidity percolation theory (Petridou et al., 2021; Jacobs and Thorpe, 1995; Jacobs and Thorpe, 1996; Jacobs and Hendrickson, 1997). The authors also estimated the viscosity ($η$) of the blastoderm tissue using the micropipette aspiration technique (Guevorkian et al., 2010; Petridou et al., 2019). It was found that change in $η$ is correlated with cell connectivity ($⟨C⟩$), rising sharply over a narrow range of $⟨C⟩$. Surprisingly, a single geometrical quantity, the cell–cell contact topology controls both the rigidity PT and changes in $η$ in this non-confluent tissue, thus linking equilibrium and transport properties.

Here, we focus on two pertinent questions that arise from the experiments on zebrafish blastoderm. First, experiments (Sinha and Thirumalai, 2021) showed that $η$ increases as a function of the cell packing fraction ($ϕ$) till $ϕ\leq0.87$. The dependence of $η$ on $ϕ$ follows the well-known Vogel–Fulcher–Tammann (VFT) law (Sinha and Thirumalai, 2021), which predicts that $η$ grows monotonically with $ϕ$. The VFT law, which is commonly used to analyze the viscosity of a class of glass-forming materials (Angell, 1991), is given by $η∼exp⁡[\frac{1}{ϕ_{0}/ϕ−1}]$, where $ϕ_{0}$ is a constant. Surprisingly, for packing fractions, $ϕ\geqϕ_{S}≈0.90$, $η$ deviates from the VFT law and is independent of $ϕ$, which cannot be explained using conventional theories for glasses (Berthier and Biroli, 2011; Kirkpatrick and Thirumalai, 2015). Second, the experimental data (Petridou et al., 2021) was interpreted using equilibrium rigidity percolation theory (Jacobs and Thorpe, 1995; Jacobs and Thorpe, 1996; Jacobs and Hendrickson, 1997) for an embryonic tissue in which cells undergo random cell divisions. A priori it is unclear why equilibrium concepts should hold in zebrafish morphogenesis, which one would expect is controlled by non-equilibrium processes such as self-propulsion, growth, and cell division.

We show that the two conundrums (saturation of $η$ at high packing fractions and the use of equilibrium statistical mechanics in a growing system to explain PT) may be rationalized by (i) assuming that the interactions between the cells are soft, and (ii) the cell sizes are highly heterogeneous (polydisperse), which is the case in zebrafish blastoderm. Using an agent-based (particle) simulation model of a two-dimensional (2D) non-confluent tissue, we explore the consequences of varying $ϕ$ (see ‘Materials and methods’ for the definition) of interacting self-propelled polydisperse soft cells, on $η$. The central results of our study are (i) the calculated effective viscosity $η¯$ (for details see, Appendix 6, ‘Dynamical changes in local packing fraction cause jammed cells to move’), for the polydisperse cell system, shows that for $ϕ\leqϕ_{S}≈0.90$ the increase in viscosity follows the VFT law. Just as in experiments, $η$ is essentially independent of $ϕ$ at high ($\geqϕ_{S}$) packing fractions. (ii) The unusual dependence of $η$ at $ϕ\geqϕ_{S}$ is quantitatively explained using the notion of available free area fraction ($ϕ_{free}$), which is the net void space that can be explored by the cells when they are jammed. At high densities, a given cell requires free space in order to move. The free area is created by movement of the neighboring cells into the available void space. One would intuitively expect that the $ϕ_{free}$ should decrease with increasing packing fractions due to cell jamming, which should slow down the overall dynamics. Indeed, we find that $ϕ_{free}$ decreases with increasing packing fraction ($ϕ$) until $ϕ_{S}$. The simulations show that when $ϕ$ exceeds $ϕ_{S}$, the free area $ϕ_{free}$ saturates because the soft cells (characterized by ‘soft deformable disks’) can overlap with each other, resulting in the collective dynamics of cells becoming independent of $ϕ$ for $ϕ\geqϕ_{S}$. As a consequence, $η$ saturates at high $ϕ$. (iii) Cells whose sizes are comparable to the available free area move almost like a particle in a liquid. The motility of small-sized cells facilitates adjacent cells to move through multi-cell rearrangement even in a highly jammed environment. The facilitation mechanism, invoked in glassy systems (Biroli and Garrahan, 2013), allows large cells to move with low mobility. A cascade of such facilitation processes enable all the cells to remain dynamic even above the onset packing fraction of the PT. (iv) We find that the relaxation time does not depend on the waiting time for measurements even in the regime where viscosity saturates. In other words, there is no evidence of aging even in the regime where viscosity saturates. Strikingly, the tissue exhibits ergodic (Thirumalai et al., 1989) behavior at all densities. The cell-based simulations, which reproduce the salient experimental features, may be described using equilibrium statistical mechanics, thus providing credence to the use of cell contact mechanics to describe both rigidity PT and dynamics in an evolving non-confluent tissue (Petridou et al., 2021).

## Results

### Experimental results

We first describe the experimental observations, which serve as the basis for carrying out the agent-based simulations. Figure 1A shows the bright-field images of distinct stages during zebrafish morphogenesis. A 2D section of zebrafish blastoderm (Figure 1B) shows that there is considerable dispersion in cell sizes. The statistical properties of the cell sizes are shown in Appendix 1—figure 1D. Figure 1C shows that $η$ increases sharply over a narrow $ϕ$ range and saturates when $ϕ$ exceeds $ϕ_{S}≈0.90$.

![Figure 1.](https://cdn.elifesciences.org/articles/87966/elife-87966-fig1-v1.jpg)

**Figure 1.:** (A) Bright-field single-plane images of an exemplary embryo of zebrafish before ($t=−60$ min), at the onset ($t=0$ min), and after blastoderm spreading ($t=60$ min). (B) Snapshot of 2D confocal sections at the 1st–2nd deep-cell layer of the blastoderm at $t=60$ min. (A) and (B) are taken from Petridou et al., 2021. (C) Viscosity $η$ of zebrafish blastoderm as a function of $ϕ$ in a log-linear scale using the data from Petridou et al., 2021. The dashed line is the fit to Vogel–Fulcher–Tammann (VFT) equation. Note that $η$ does not change significantly beyond $ϕ\geq0.87$. (D) A typical snapshot taken from cell-based simulations for $ϕ=0.93$. Cells are colored according to their radii (in µm) (color bar shown on the right). (E) The pair correlation function, $g(r)$, as a function of $r$ for $ϕ=0.93$. The vertical dashed line is the position of the first peak ($r_{max}=17.0\mum$). The pair correlation function does not exhibit signs of long-range order. Scale bars in (A) is 100 µm and (B) is 50 µm.

To account for the results in Figure 1C, we first simulated a mono-disperse system in which all the cells have identical radius ($R=8.5\mum$). Because the system crystallizes (Appendix 1—figure 1A and B), we concluded that the dynamics observed in experiments cannot be explained using this model. A 1:1 binary mixture of cells with different radii gives glass-like behavior for all $ϕ$, with the relaxation time $\tau_{\alpha}$ as well as the effective viscosity $η¯$ (defined in Equation 1) following the VFT behavior (see Appendix 2).

### Polydispersity and cell–cell interactions

In typical cell tissues, and zebrafish in particular, there is a great dispersion in the cell sizes, which vary in a single tissue by a factor of ∼5–6 (Petridou et al., 2021; Figure 1B, Appendix 1—figure 1D). In addition, the elastic forces characterizing cell–cell interactions are soft, which implies that the cells can overlap, with $r_{ij}−(R_{i}+R_{j})<0$ when they are jammed (Figure 1B, D). Thus, both polydispersity (PD) and soft interactions between the cells must control the relaxation dynamics. To test this proposition, we simulated a highly polydisperse system (PDs) in which the cell sizes vary by a factor of ∼8 (Figure 1D , Appendix 1—figure 1E).

A simulation snapshot (Figure 1D) for $ϕ=0.93$ shows that different sized cells are well mixed. In other words, the cells do not phase separate. The structure of the tissue can be described using the pair correlation function, $g(r)=\frac{1}{ρ}⟨\frac{1}{N}\sumiN\sumj\neqiN\delta(r−|r→_{i}−r→_{j}|)⟩$, where $ρ=\frac{N}{L^{2}}$ is the number density, $\delta$ is the Dirac delta function, $r→_{i}$ is the position of the ith cell, and the angular bracket $⟨⟩$ denotes an average over different ensembles. The $g(r)$ function (Figure 1E) has a peak around $r∼17\mum$, which is approximately the average diameter of the cells. The absence of peaks in $g(r)$ beyond the second one suggests there is no long-range order. Thus, the polydisperse cell system exhibits liquid-like structure even at the high $ϕ$.

### Effective shear viscosity(η¯) as a function of ϕ

A fit of the experimental data for $η$ using the VFT (Tammann and Hesse, 1926; Fulcher, 1925) relation in the range $ϕ\leq0.87$ (Figure 1C) yields $ϕ_{0}≈0.95$ and $D≈0.51$ (Sinha and Thirumalai, 2021). The VFT equation for cells, which is related to the Doolittle equation (White and Lipson, 2016) for fluidity ($\frac{1}{η}$) that is based on free space available for motion in an amorphous system (Doolittle and Doolittle, 1957; Cohen and Turnbull, 1959), is $η=η_{0}exp⁡[\frac{D}{ϕ_{0}/ϕ−1}]$, where $D$ is the apparent activation energy. In order to compare with experiments, we calculated an effective shear viscosity ($η¯$) for the polydisperse system using a Green–Kubo-type relation (Hansen and McDonald, 2013)

$$
η¯=\int_{0}^{∞}dt\sum(\muν)⟨P_{\muν}(t)P_{\muν}(0)⟩.
$$

The stress tensor $P_{\muν}(t)$ in the above equation is

$$
P_{\muν}(t)=\frac{1}{A}(\sumi=1N\sumj>iNr→_{ij,\mu}f→_{ij,ν}),
$$

where $\mu,ν\in(x,y)$ are the Cartesian components of coordinates, $r→_{ij}=r→_{i}−r→_{j}$, $f→_{ij}$ is the force between ith and jth cells, and $A$ is the area of the simulation box. Note that $η¯$ should be viewed as a proxy for shear viscosity because it does not contain the kinetic term and the factor $\frac{A}{k_{B}T}$ is not included in Equation (1) because temperature is not a relevant variable in the highly over-damped model for cells considered here.

Plot of $η¯$ as a function of $ϕ$ in Figure 2A shows qualitatively the same behavior as the estimate of viscosity (using dimensional arguments) made in experiments. Two features about Figures 1C and 2A are worth noting. (i) Both simulations and experiments show that up to $ϕ≈0.90$, $η¯(ϕ)$ follows the VFT relation with $ϕ_{0}∼0.94$ and $D∼0.5$. More importantly, $η¯$ is independent of $ϕ$ when $ϕ>0.90$. (ii) The values of $ϕ_{0}$ and $D$ obtained by fitting the experimental estimate of $η$ to the VFT equation and simulation results are almost identical. Moreover, the onset of the plateau packing fraction in simulations and experiments occurs at the same value ($ϕ_{S}∼0.90$). The overall agreement with experiments is remarkable given that the model was not created to mimic the zebrafish tissue.

![Figure 2.](https://cdn.elifesciences.org/articles/87966/elife-87966-fig2-v1.jpg)

**Figure 2.:** (A) Effective viscosity $η¯$ as a function of $ϕ$, with the solid line being the fit to Vogel–Fulcher–Tammann (VFT) equation. The inset shows $η¯$ at high $ϕ$. The dashed line in the inset is the expected behavior assuming that the VFT relation holds at all $ϕ$. (B) The self-intermediate scattering function $F_{s}(q,t)$ as a function of $t$ for $0.70\leqϕ\leq0.905$. The dashed line corresponds to $F_{s}(q,t)=\frac{1}{e}$. (C) A similar plot for $ϕ>0.905$. (D) The logarithm of the relaxation time $\tau_{\alpha}(s)$ as a function of $ϕ$. The VFT fit is given by the dashed line. The inset shows a zoomed-in view for $ϕ\geqϕ_{S}$. The error bars in (D) are calculated using the standard deviation of $\tau_{\alpha}$ for 24 independent simulations.

To provide additional insights into the dynamics, we calculated the isotropic self-intermediate scattering function, $F_{s}(q,t)$,

$$
F_{s}(q,t)=\frac{1}{N}⟨\sumj=1Nexp⁡[−iq→⋅(r→_{j}(t)−r→_{j}(0))]⟩,
$$

where $q→$ is the wave vector, and $r→_{j}(t)$ is the position of a cell at time $t$. The degree of dynamic correlation between two cells can be inferred from the decay of $F_{s}(q,t)$. The angle bracket $⟨...⟩$ is an average over different time origins and different trajectories. We chose $q=\frac{2\pi}{r_{max}}$, where $r_{max}$ is the position of the first peak in $g(r)$ between all cells (see Figure 1E). The relaxation time $\tau_{\alpha}$ is calculated using $F_{s}(q,t=\tau_{\alpha})=\frac{1}{e}$.

From Figure 2B and C, which show $F_{s}(q,t)$ as a function of $t$ for various $ϕ$, it is clear that the dynamics become sluggish as $ϕ$ increases. The relaxation profiles exhibit a two-step decay with a plateau in the intermediate time scales. The dynamics continues to slow down dramatically until $ϕ\leq0.90$. Surprisingly, the increase in the duration of the plateau in $F_{s}(q,t)$ ceases when $ϕ$ exceeds $≈0.90$ (Figure 2C), a puzzling finding that is also reflected in the dependence of $\tau_{\alpha}$ on $ϕ$ in Figure 2D. The relaxation time increases dramatically, following the VFT relation, till $ϕ≈0.90$, and subsequently reaches a plateau (see the inset in Figure 2D).

If the VFT relation continued to hold for all $ϕ$, as in glasses or in binary mixture of 2D cells (see Appendix 2), then the fit yields $ϕ_{0}≈0.95$ and $D≈0.50$. However, the simulations show that $\tau_{\alpha}$ is nearly a constant when $ϕ$ exceeds $0.90$. We should note that the behavior in Figure 2D differs from the dependence of $\tau_{\alpha}$ on $ϕ$ for 2D monodisperse polymer rings, used as a model for soft colloids. Simulations (Gnan and Zaccarelli, 2019) showed $\tau_{\alpha}$ increases till a critical $ϕ_{S}$ but it decreases substantially beyond $ϕ_{S}$ with no saturation.

### Relaxation dynamics of individual cells

Plot of $\tau_{\alpha}$ as a function of the radius of cells $R_{i}$ (Figure 3A) shows nearly eight orders of magnitude change. The size dependence of $\tau_{\alpha}$ on $ϕ$ is striking. That $\tau_{\alpha}$ should increase for large-sized cells (see the data beyond the vertical dashed line in Figure 3A) is not unexpected. However, even when cell sizes increase beyond $R_{i}=4.25\mum$, the dispersion in $\tau_{\alpha}$ is substantial, especially when $ϕ$ exceeds $ϕ_{S}$. The relaxation times for cells with $R_{i}<4.25\mum$ are relatively short even though the system as a whole is jammed. For $ϕ\geq0.90$, $\tau_{\alpha}$ for small-sized cells have a weak dependence on $ϕ$. Although $\tau_{\alpha}$ for cells with radius <4 µm is short, it is clear that for a given $ϕ$ (e.g., $ϕ=0.93$) the variations in $\tau_{\alpha}$ are substantial. In contrast, $\tau_{\alpha}s$ for larger cells ($R\geq7\mum$) are substantially large, possibly exceeding the typical cell division time in experiments. In what follows, we interpret these results in terms of available free area $⟨A_{free}⟩$ for cells. The smaller-sized cells have the largest $⟨A_{free}⟩≈50\mum^{2}≈\piR_{S}^{2}(R_{S}≈4\mum)$ ($R_{S}$ is the radius of the small cell).

![Figure 3.](https://cdn.elifesciences.org/articles/87966/elife-87966-fig3-v1.jpg)

**Figure 3.:** (A) Scatter plot of relaxation times $\tau_{\alpha}(s)$ as a function of cell radius. From top to bottom, the plot corresponds to decreasing $ϕ$. The vertical dashed line is for $R_{i}=4.25\mum$, beyond which the $\tau_{\alpha}$ changes sharply at high packing fractions. (B) Histogram $P(ln⁡(\tau_{\alpha}))$ as a function of $ln⁡(\tau_{\alpha})$. Beyond $ϕ=0.90$ ($ϕ_{S}$), the histogram peaks do not shift substantially towards a high $\tau_{\alpha}$ values. (C) For $ϕ\leqϕ_{S}P(ln⁡(\tau_{\alpha}))$ (scaled by $P^{max}(ln⁡(\tau_{\alpha}))$) falls on a master curve, as described in the main text. (D) Same as (C) except the results are for $ϕ>0.90$. The data deviates from the Gaussian fit, shown by the dashed line.

The effect of jamming on the dramatic increase in $\tau_{\alpha}$ occurs near $R_{i}≈4.5\mum$, which is comparable to the length scale of short-range interactions. For $ϕ\leq0.90$, $\tau_{\alpha}$ increases as the cell size increases. However, at higher packing fractions, even cells of similar sizes show substantial variations in $\tau_{\alpha}$, which change by almost 3–4 orders of magnitude (see the data around the vertical dashed line for $ϕ\geq0.915$ in Figure 3A).

This is a consequence of large variations in the local density (Appendix 6—figure 1). Some of the similar-sized cells are trapped in the jammed environment, whereas others are in less crowded regions (see Appendix 6—figure 1). The spread in $\tau_{\alpha}$ increases dramatically for $ϕ>ϕ_{S}$ ($≈0.90$) and effectively overlap with each other. This is vividly illustrated in the histogram, $P(log⁡(\tau_{\alpha}))$, shown in Figure 3B. For $ϕ<ϕ_{s}$, the peak in $P(log⁡(\tau_{\alpha}))$ monotonically shifts to higher $log⁡(\tau_{\alpha})$ values. In contrast, when $ϕ$ exceeds $ϕ_{S}$ there is overlap in $P(log⁡(\tau_{\alpha}))$, which is reflected in the saturation of $η¯$ and $\tau_{\alpha}$.

There are cells (typically with small sizes) that move faster even in a highly jammed environment (see Appendix 5—figures 1C and 2). The motions of the fast-moving cells change the local environment, which effectively facilitates the bigger cells to move in a crowded environment (see Appendix 5—figures 1D and 2, Video 1 ($ϕ=0.92>ϕ_{S}$) and Video 2 ($ϕ=0.90=ϕ_{S}$)). In contrast, for $ϕ=0.85<ϕ_{S}$, small- and large-sized cells move without hindrance because of adequate availability of free area (Video 3). The videos vividly illustrate the large-scale facilitated rearrangements that enable the large-sized cells to move.

![Video 1.](https://cdn.elifesciences.org/articles/87966/elife-87966-video1.mp4.jpg)

**Video 1.:** Shows multiple rearrangements of smaller sized cells (blue and green cells) causes the big cells (yellow cells) to move in a highly jammed environment ($ϕ=0.92>ϕ_{S}$).Bright colors show the cell-cell overlap. Note that the overlap values are higher than those in lower area fractions. Free spaces (black background) are changing dynamically around a cell.

![Video 2.](https://cdn.elifesciences.org/articles/87966/elife-87966-video2.mp4.jpg)

**Video 2.:** Shows how a big cell (yellow) moves in the crowded environment $(ϕ=0.90(ϕ_{S}))$.Note that the smaller-sized cells (colored as deep blue) always move faster. Again, the multiple rearrangement causes the bigger cell to move substantially. The amount of overlap is smaller than that at $ϕ=0.92$.

![Video 3.](https://cdn.elifesciences.org/articles/87966/elife-87966-video3.mp4.jpg)

**Video 3.:** Shows the movements of cells at a low area fraction ($ϕ=0.85$).Note that the smaller and bigger-sized cells are almost equally faster at lower area fractions ($phi=0.85$) because of the huge available free areas.

The dependence of $\tau_{\alpha}$ on $ϕ$ for $ϕ\leqϕ_{S}$ (Figure 2D) implies that the polydisperse cell systems behave as a soft glass in this regime. On theoretical grounds, it was predicted that $P(ln⁡(\tau_{\alpha}))∼exp⁡[−c(ln⁡(\frac{\tau_{\alpha}}{\tau_{0}}))^{2}]$ in glass-forming systems (Kirkpatrick and Thirumalai, 2015). Remarkably, we found that this prediction is valid in the polydisperse cell system (Figure 3C). However, above $ϕ_{S}$ the predicted relation is not satisfied (see Figure 3D).

### Available free area explains viscosity saturation at high ϕ

We explain the saturation in the viscosity by calculating the available free area per cell, as $ϕ$ increases. In a hard disk system, one would expect that the free area would decrease monotonically with $ϕ$ until it is fully jammed at the close packing fraction (∼0.84; Drocco et al., 2005; Reichhardt and Reichhardt, 2014). Because the cells are modeled as soft deformable disks, they could overlap with each other even when fully jammed. Therefore, the region where cells overlap creates free area in the immediate neighborhood.

The extent of overlap ($h_{ij}$) is reflected in distribution $P(h_{ij})$. The width in $P(h_{ij})$ increases with $ϕ$, and the peak shifts to higher values of $h_{ij}$ (Figure 4A). The mean, $⟨h_{ij}⟩$, increases with $ϕ$ (Figure 4B). Thus, even if the cells are highly jammed at $ϕ≈ϕ_{S}$, free area is available because of an increase in the overlap between cells (see Figure 5).

![Figure 4.](https://cdn.elifesciences.org/articles/87966/elife-87966-fig4-v1.jpg)

**Figure 4.:** (A) Probability of overlap ($h_{ij}$) between two cells, $P(h_{ij})$, for various $ϕ$ values.The peak in the distribution function shifts to higher values as $ϕ$ increases. (B) Mean $⟨h_{ij}⟩=\intdh_{ij}P(h_{ij})$ as a function of $ϕ$. Inset shows a pictorial illustration of $h_{12}$ between two cells with radii $R_{1}$ and $R_{2}$ at a distance $r_{12}$.

![Figure 5.](https://cdn.elifesciences.org/articles/87966/elife-87966-fig5-v1.jpg)

**Figure 5.:** Changes in free area fraction with $ϕ$.(A) Voronoi tessellation of cells for $ϕ=0.93$ for a single realization. The orange circles represent actual cell sizes. The blue polygons show the Voronoi cell size. (B) Distribution of Voronoi cell size $A$ as a function of $ϕ$. (C) Mean Voronoi cell size $⟨A⟩$ as a function of $ϕ$. A zoomed-in view for $ϕ>0.860$ is shown in the inset. (D) Distribution of free area $P(A_{free})$ for all $ϕ$. The vertical blue dashed line shows that the maximum in the distribution is at $A_{free}∼50\mum^{2}$. (E) Free area fraction $ϕ_{free}$ as a function of $ϕ$. Note that $ϕ_{free}$ saturates beyond $ϕ=0.90$. An expanded view of the saturated region is shown in the right panel of (E). The error bars in (C) and (D) are the standard deviation in $⟨A⟩$ and $ϕ_{free}$, respectively, for 24 independent simulations.

When $ϕ$ exceeds $ϕ_{S}$, the mobility of small-sized cells facilitates the larger cells to move, as is assumed in the free volume theory of polymer glasses (Cohen and Turnbull, 1959; Turnbull and Cohen, 1961; Turnbull and Cohen, 1970; Falk et al., 2020). As a result of the motion of small cells, a void is temporarily created, which allows other (possibly large) cells to move. In addition to the release of space, the cells can also interpenetrate (Figure 4A and B). If $h_{ij}$ increases, as is the case when the extent of compression increases (Figure 4A), the available space for nearby cells would also increase. This effect is expected to occur with high probability at $ϕ_{S}$ and beyond, resulting in high overlap between the cells. These arguments suggest that the combined effect of PD and cell–cell overlap creates, via the self-propulsion of cells, additional free area that drives larger cells to move even under jammed conditions.

In order to quantify the physical picture given above, we calculated an effective area for each cell by first calculating Voronoi cell area $A$. A plot for Voronoi tessellation is presented in Figure 5A for $ϕ=0.93$, and the histogram of $A$ is shown in Figure 5B. As $ϕ$ increases, the distribution shifts toward lower Voronoi cell size $⟨A⟩$. The mean Voronoi cell size $⟨A⟩$ as a function of $ϕ$ in Figure 5C shows $⟨A⟩$ decreases as $ϕ$ is increased. As cells interpenetrate, the Voronoi cell size will be smaller than the actual cell size ($\piR_{i}^{2}$) in many instances (Figure 5A). To demonstrate this quantitatively, we calculated $A_{free,i}=A_{i}−\piR_{i}^{2}$. The value of $A_{free}$ could be negative if the overlap between neighboring cells is substantial; $A_{free}$ is positive only when the Voronoi cell size is greater than the actual cell size. Positive $A_{free}$ is an estimate of the available free area. The histograms of $A_{free}$ for all the packing fractions in Figure 5D show that the distributions saturate beyond $ϕ=0.90$. All the distributions have a substantial region in which $A_{free}$ is negative. The negative value of $A_{free}$ increases with increasing $ϕ$, which implies that the amount of interpenetration between cells increases.

Because of the overlap between the cells, the available free area fraction $ϕ_{free}$ is higher than the expected free area fraction ($1.0−ϕ$) for all $ϕ$. We define an effective free area fraction $ϕ_{free}$ as

$$
ϕ_{free}=\frac{\sumj=1N_{t}\sumi=1N_{p}A_{free_{+,i}}^{j}}{N_{t}A_{box}},
$$

where $N_{p}$ is the number of positive free area in jth snapshots, $N_{t}$ is the total number of snapshots, $A_{box}$ is the simulation box area, and $A_{free_{+,i}}^{j}$ is the positive free area of ith cell in jth snapshot.

The calculated $ϕ_{free}$, plotted as a function of $ϕ$ in Figure 5E, shows that $ϕ_{free}$ decreases with $ϕ$ until $ϕ=0.90$, and then it saturates near a value $ϕ_{free}≈0.22$ (see the right panel in Figure 5E). Thus, the saturation in $η¯$ as a function of $ϕ$ is explained by the free area picture, which arises due to combined effect of the size variations and the ability of cells to overlap.

### Aging does not explain viscosity saturation

Our main result, which we explain by adopting the free volume theory developed in the context of glasses (Cohen and Turnbull, 1959; Turnbull and Cohen, 1961; Turnbull and Cohen, 1970; Falk et al., 2020), is that above a critical packing fraction $ϕ_{S}∼0.90$ the viscosity saturates. Relaxation time, $\tau_{\alpha}$, measured using dynamic light scattering, in nearly monodisperse microgel poly(N- isopropylacrylamide) (PNiPAM) (Philippe et al., 2018) was found to depend only weakly on the volume fraction (3D), if $ϕ_{V}$ exceeds a critical value. It was suggested that the near saturation of $\tau_{\alpha}$ at high $ϕ_{V}$ is due to aging, which is a non-equilibrium effect. If saturation in viscosity and relaxation time in the embryonic tissue at high $ϕ$ is due to aging, then $\tau_{\alpha}$ should increase sharply as the waiting time, $\tau_{\omega}$, is lengthened. We wondered if aging could explain the observed saturation of $η$ in the embryonic tissue above $ϕ_{S}$. If aging causes the plateau in the tissue dynamics, then $η$ or $\tau_{\alpha}$ should be an increasing function of the waiting time, $\tau_{\omega}$. To test the effect of $\tau_{\omega}$ on $\tau_{\alpha}$, we calculated the self-intermediate scattering function $F_{s}(q,t+\tau_{\omega})$ as a function of $t$ by varying $\tau_{\omega}$ over three orders of magnitude at $ϕ=0.92$ (Figure 6A). There is literally no change in $F_{s}(q,t+\tau_{\omega})$ over the entire range of $\tau_{\omega}$. We conclude that, $\tau_{\alpha}$, extracted from $F_{s}(q,t+\tau_{\omega})$ is independent of $\tau_{\omega}$. The variations in $\tau_{\alpha}$ (Figure 6B), with respect to $\tau_{\omega}$, are significantly smaller than the errors in the simulation. Thus, the saturation in $η$ or $\tau_{\alpha}$ when $ϕ>ϕ_{S}$ is not a consequence of aging.

![Figure 6.](https://cdn.elifesciences.org/articles/87966/elife-87966-fig6-v1.jpg)

**Figure 6.:** (A) $F_{s}(q,t)$ for $ϕ=0.92$ at different waiting times ($\tau_{\omega}=10^{6}(s))$. Regardless of the value of $\tau_{\omega}$, all the $F_{s}(q,t)$ curves collapse onto a master curve. (B) Relaxation time, $ln⁡(\tau_{\alpha})$, as a function of $\tau_{\omega}$. Over a three orders of magnitude change in $t_{\omega}$, the variation in relaxation times is less than the sample-to-sample fluctuations, as shown by the error bar. The error bars in (B) are the standard deviation in $\tau_{\alpha}$ for 24 independent simulations.

There are two implications related to the absence of aging in the dynamics of the non-confluent embryonic tissues. (i) Although active forces drive the dynamics of the cells, as they presumably do in reality, the cell collectives can be treated as being near equilibrium, justifying the use of Green–Kubo relation to calculate $η$. (ii) Parenthetically, we note that the absence of significant non-equilibrium effects, even though zebrafish is a living system, further justifies the use of equilibrium rigidity percolation theory to analyze the experimental data (Petridou et al., 2021).

## Discussion

Extensive computer simulations of a 2D dense tissue using a particle-based model of soft deformable cells with active self-propulsion have successfully reproduced the dynamical behavior observed in the blastoderm tissue of zebrafish.

The dependence of viscosity ($η$) and relaxation time ($\tau_{\alpha}$) (before the saturation) is well fit by the VFT equation. The value of $ϕ_{0}$ obtained from simulations, $ϕ_{0}∼0.95$, is close to $ϕ_{0}∼0.94$ extracted by fitting the experimental data to the VFT equation. Thus, the dynamics for $ϕ\leqϕ_{S}$ resembles the behavior expected for glass-forming systems. Remarkably, the dependence of $η$ on $ϕ$ over the entire range (VFT regime followed by a plateau) may be understood using available free area picture with essentially a single parameter, an idea that was proposed nearly 70 y ago. We discovered that PD as well as the ease of deformation of the cells that creates free area under high jamming conditions is the mechanism that explains viscosity saturation at high cell densities. The mechanism suggested here is an important step that links equilibrium PT to dynamics during zebrafish development (Hannezo and Heisenberg, 2022).

One could legitimately wonder if the extent of PD used in the soft discs simulations, which seems substantial, is needed to recapitulate the observed dependence of $η$ on $ϕ$. Furthermore, such large values of PD may not represent biological tissues. Although the choice of PD was made in part by the 2D projection of area reported in experiments (Petridou et al., 2021), it is expected that PD values have to be less in three dimensions. We performed preliminary simulations in three dimensions with considerably reduced PD and calculated the dependence of relaxation time ($\tau_{\alpha}$) as a function of $ϕ$. The results show that $\tau_{\alpha}$ does indeed saturate at high-volume fractions.

The proposed model neglects adhesive interactions between cells, which of course is not unimportant. It is crucial to wonder if the proposed mechanism would change if cell–cell adhesion is taken into account. We wanted to create the simplest model to explain the experimental data. We do think that realistic values of adhesion strength would not significantly alter the forces between cells (Malmi-Kakkada et al., 2018). Thus, we expect a similar mechanism. Furthermore, the physics of the dynamics in glass-forming materials does not change in systems with and without attractive forces (Kirkpatrick and Thirumalai, 2015). Universal behavior, such as VFT relation, is valid for a broad class of unrelated materials (see Figure 1 in Angell, 1991). Needless to say, non-universal quantities such as glass transition temperature $T_{g}$ or effective free energy barriers for relaxation will change. In our case, we expect that changing the adhesion strength, within a reasonable range, would change $ϕ_{S}$ without qualitatively altering the dependence of $η$ on $ϕ$. For these reasons, in the first pass we neglected adhesion, whose effects have to be investigated in the future.

In the physical considerations leading to Equation (6), the random activity term (µ) plays an important role. Is it possible to create a passive model by maintaining the system at a finite temperature using stochastic noise with µ = 0, which would show the observed viscosity behavior? First, in such a system of stochastic equations, the coefficient of noise (a diffusion constant) would be related to $\gamma_{i}$ in Equation (6) through fluctuation dissipation theorem (FDT). Thus, only $\gamma_{i}$ can be varied. In contrast, in Equation (6) the two parameters ($\gamma_{i}$ and µ) maybe independently changed, which implies that the two sets of stochastic equations of motion are not equivalent. Second, the passive system describes particles that interact by soft Hertz potential. In analogy with systems in which the particles interact with harmonic potential (Ikeda et al., 2012), we expect that the passive model would form a glass in which the viscosity would follow the VFT law.

We find it surprising that the calculation of viscosity using linear response theory (valid for systems close to equilibrium) and the link to free area quantitatively explain the simulation results and by implication the experimental data for a living and growing tissue. The calculation of free area of the cells is based on the geometrical effects of packing, which in turn is determined by cell-to-cell contact topology. These considerations, which are firmly established here, explain why equilibrium PTs are related to a steep increase in viscosity (Kirkpatrick and Thirumalai, 2015) as the packing fraction changes over a narrow range. The absence of aging suggests that, although a large number of cell divisions occur, they must be essentially independent, thus allowing the cells to reach local equilibrium.

## Materials and methods

### Two-dimensional cell model

Following our earlier studies (Malmi-Kakkada et al., 2018; Sinha et al., 2020), we simulated a 2D version of a particle-based cell model. We did not explicitly include cell division in the simulations. This is physically reasonable because in the experiments (Petridou et al., 2021) the time scales over which cell division induced local stresses relax are short compared to cell division time. Thus, local equilibrium is established in between random cell division events. We performed simulations in 2D because experiments reported the dependence of viscosity as a function of area fraction.

In our model, cells are modeled as soft deformable disks (Matoz-Fernandez et al., 2017; Drasdo and Höhme, 2005; Schaller and Meyer-Hermann, 2005; Malmi-Kakkada et al., 2018) interacting via short-ranged forces. The elastic (repulsive) force between two cells with radii $R_{i}$ and $R_{j}$ is Hertzian, which is given by

$$
F_{ij}^{el}=\frac{h_{ij}^{3/2}}{\frac{3}{2}(\frac{1−ν^{2}}{E})\sqrt{\frac{1}{R_{i}}+\frac{1}{R_{j}}}},
$$

where $h_{ij}=max[0,R_{i}+R_{j}−|r→_{i}−r→_{j}|]$. The repulsive force acts along the unit vector $n→_{ij}$, which points from the center of the jth cell to the center of the ith cell. The total force on the ith cell is

$$
F_{i}→=\sumj\inN⁢N⁢(i)(F_{i⁢j}^{e⁢l})⁢n→_{i⁢j},
$$

where $NN(i)$ is the number of near-neighbor cells that are in contact with the ith cell. The jth cell is the nearest neighbor of the ith cell, if $h_{ij}>0$. The near-neighbor condition ensures that the cells interpenetrate each other to some extent, thus mimicking the cell softness. For simplicity, we assume that the elastic moduli ($E$) and the Poisson ratios ($ν$) for all the cells are identical. PD in the cell sizes is important in recovering the plateau in the viscosity as a function of packing fraction. Thus, the distribution of cell areas ($A_{i}=\piR_{i}^{2}$) is assumed to have a distribution that mimics the broad area distribution discovered in experiments.

### Self-propulsion and equations of motion

In addition to the repulsive Hertz force, we include an active force arising from self-propulsion mobility (µ), which is a proxy for the intrinsically generated forces within a cell. For illustration purposes, we take µ to independent of the cells, although this can be relaxed readily. We assume that the dynamics of each cell obeys the phenomenological equation

$$
r→˙_{i}=\frac{F→_{i}}{\gamma_{i}}+\muW→_{i}(t),
$$

where $\gamma_{i}$ is the friction coefficient of ith cell, and $W_{i}(t)$ is a noise term. The friction coefficient $\gamma_{i}$ is taken to be $\gamma_{0}R_{i}$ (Sinha et al., 2022). By scaling $t$ by the characteristic time scale, $\tau=\frac{⟨R⟩^{2}}{\mu^{2}}$ in Equation (6), one can show that the results should be insensitive to the exact value of µ. The noise term $W_{i}(t)$ is chosen such that $⟨W_{i}(t)⟩=0$ and $⟨W_{i}^{\alpha}(t)W_{j}^{\beta}(t^{′})⟩=\delta(t−t^{′})\delta_{i,j}\delta^{\alpha,\beta}$. In our model, there is no dynamics with only systematic forces because the temperature is zero. The observed dynamics arises solely due to the self-propulsion (Equation 6).

We place $N$ cells in a square box that is periodically replicated. The size of the box is $L$ so that the packing fraction (in our 2D system it is the area fraction) is $ϕ=\frac{\sumi=1N\piR_{i}^{2}}{L^{2}}$. We performed extensive simulations by varying $ϕ$ in the range $0.700\leqϕ\leq0.950$. The results reported in main text are obtained with $N=500$. Finite size effects are discussed in Appendix 7.

To mimic the variations in the area of cells in a tissue (Petridou et al., 2021), we use a broad distribution of cell radii (see Appendix 1 for details). The parameters for the model are given in Table 1. In this study, we do not consider the growth and division of cells. Thus, our simulations describe steady-state dynamics of the tissue. For each $ϕ$, we performed simulations for at least (5–10)$\tau_{\alpha}$ before storing the data. For each $ϕ$, we performed 24 independent simulations. The calculation of viscosity was performed by averaging over 40 independent simulations at each $ϕ$.

**Table 1.**
 Parameters used in the simulation.


<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Values</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Timestep (Δt)</td>
      <td>10s</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>Self-propulsion (µ)</td>
      <td>0.045μm/s</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>Friction coefficient (γo)</td>
      <td>0.1kg/(μm s)</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>Mean cell elastic modulus (Ei)</td>
      <td>10−3MPa</td>
      <td>Galle et al., 2005; Malmi-Kakkada et al., 2018</td>
    </tr>
    <tr>
      <td>Mean cell Poisson ratio (νi)</td>
      <td>0.5</td>
      <td>Schaller and Meyer-Hermann, 2005; Malmi-Kakkada et al., 2018</td>
    </tr>
  </tbody>
</table>

### Calculation of viscosity

We calculated the effective viscosity ($η¯$) for various values of $ϕ$ by integrating the off-diagonal part of the stress–stress correlation function $⟨P_{\muν}(t)P_{\muν}(0)⟩$ using the Green–Kubo relation (Hansen and McDonald, 2013) (without the pre-factor $\frac{A}{k_{B}T}$)

$$
η¯=\int_{0}^{∞}dt\sum(\muν)⟨P_{\muν}(t)P_{\muν}(0)⟩,
$$

where µ and $ν$ denote Cartesian components ($x$ and $y$) of the stress tensor $P_{\muν}(t)$ (see main text for the definition of $P_{\muν}(t)$). The definition of $η¯$, which relates the decay of stresses as a function of times in the non-confluent tissue, is akin to the methods used to calculate viscosity in simple fluids (Equation 7). The time dependence of $⟨P_{\muν}(t)P_{\muν}(0)⟩$, normalized by $⟨P_{\muν}(0)^{2}⟩$, for different values of $ϕ$ (Figure 7A and B) shows that the stress relaxation is clearly non-exponential, decaying to zero in two steps. After an initial rapid decay followed by a plateau at intermediate times (clearly visible for $ϕ\geq0.91$), the normalized $⟨P_{\muν}(t)P_{\muν}(0)⟩$ decays to zero as a stretched exponential. The black dashed lines in Figure 7C show that a stretched exponential function, $C_{s}exp⁡[−(\frac{t}{\tau_{η}})^{\beta}]$, where $\tau_{η}$ is the characteristic time in which stress relax and $\beta$ is the stretching exponent, provides an excellent fit to the long time decay of $⟨P_{\muν}(t)P_{\muν}(0)⟩$ (from the plateau region to zero) as a function of $t$. Therefore, we utilized the fit function, $C_{s}exp⁡[−(\frac{t}{\tau_{η}})^{\beta}]$, to replace the noisy long time part of $⟨P_{\muν}(t)P_{\muν}(0)⟩$ by a smooth fit data before evaluating the integral in Equation (7). The details of the procedure to compute $η¯$ are described below.

![Figure 7.](https://cdn.elifesciences.org/articles/87966/elife-87966-fig7-v1.jpg)

**Figure 7.:** (A) The stress–stress correlation function $⟨P_{\muν}(t)P_{\muν}(0)⟩$ divided by the value at $t=0⟨P_{\muν}(0)^{2}⟩$ as a function of $t$ for $ϕ\in(0.75−0.87)$. (B) Similar plot for $ϕ\in(0.89−0.93)$. (C) The long time decay of $⟨P_{\muν}(t)P_{\muν}(0)⟩$ is fit to $C_{s}exp⁡[−(\frac{t}{\tau_{η}})^{\beta}]$, as shown by the dashed lines. The inset shows the dependence of $\beta$ on $ϕ$. (D) The data that is fit using the stretched exponential function (black dashed line) is combined with the short time data (blue solid line), which is fit using the cubic spline function. The resulting fits produces a smooth curve $⟨P_{\muν}(t)P_{\muν}(0)⟩_{combined}$, as shown in the inset.

We divided $⟨P_{\muν}(t)P_{\muν}(0)⟩$ in two parts. (i) The short time part ($⟨P_{\muν}(t)P_{\muν}(0)⟩_{short}$) – the smooth initial rapid decay until the plateau is reached (e.g., see the blue circles in Figure 7D for $ϕ=0.93$). For the $n$ data points at short times, $(t_{1},⟨P_{\muν}(t_{1})P_{\muν}(0)⟩_{% short})$,…, $(t_{n},⟨P_{\muν}(t_{n})P_{\muν}(0)⟩_{% short})$, we constructed a spline $S(t)$ using a set of cubic polynomials:

$$
S_{1}(t)= ⟨P_{\muν}(t_{1})P_{\muν}(0)⟩_{short}+b_{1}(t−t_{1})+c_{1}(t−t_{1})^{2}+d_{1}(t−t_{1})^{3}S_{2}(t)= ⟨P_{\muν}(t_{2})P_{\muν}(0)⟩_{short}+b_{2}(t−t_{2})+c_{2}(t−t_{2})^{2}+d_{2}(t−t_{2})^{3}S_{n−1}(t)= ⟨P_{\muν}(t_{n−1})P_{\muν}(0)⟩_{short}+b_{n−1}(t−t_{n−1})+c_{n−1}(t−t_{n−1})^{2}+d_{n−1}(t−t_{n−1})^{3}.
$$

The polynomials satisfy the following properties. (a) $S_{i}(t_{i})=⟨P_{\muν}(t_{i})P_{\muν}(0)⟩_{% short}$ and $S_{i}(t_{i+1})=⟨P_{\muν}(t_{i+1})P_{\muν}(0)⟩_{short}$ for $i=1,...,n−1$ which guarantees that the spline function $S(t)$ interpolates between the data points. (b) $S_{i−1}^{′}(t)=S_{i}^{′}(t)$ for $i=2,...,n−1$ so that $S^{′}(t)$ is continuous in the interval $[t_{1},t_{n}]$. (c) $S_{i−1}^{′′}(t)=S_{i}^{′′}(t)$ for $i=2,...,n−1$ so that $S^{′′}(t)$ is continuous in the interval $[t_{1},t_{n}]$. By solving for the unknown parameters, $b_{i},c_{i}$, and $d_{i}$, using the above-mentioned properties, we constructed the function S(t). We used $S(t)$ to fit $⟨P_{\muν}(t)P_{\muν}(0)⟩_{short}$ to get an evenly spaced ($\deltat=10s$) smooth data (solid blue line in Figure 7D). The fitting was done using the software ‘Xmgrace’.

(ii) The long time part ($⟨P_{\muν}(t)P_{\muν}(0)⟩_{long}$) – from the plateau until it decays to zero – is shown by the red circles in Figure 7D. The long time part was fit using the analytical function $C_{s}exp⁡[−(\frac{t}{\tau_{η}})^{\beta}]$ (black dashed line in Figure 7D). We refer to the fit data ($\deltat=10s$) as $⟨P_{\muν}(t)P_{\muν}(0)⟩_{long}^{fit}$.

We then combined $⟨P_{\muν}(t)P_{\muν}(0)⟩_{short}$ and $⟨P_{\muν}(t)P_{\muν}(0)⟩_{long}^{% fitted}$ to obtain $⟨P_{\muν}(t)P_{\muν}(0)⟩_{combined}$ (see inset of Figure 7D). Finally, we calculated $η¯$ using the equation,

$$
η¯=lim\deltat→0\sumi=0T\deltat\sum(\muν)⟨P_{\muν}(i\deltat)P_{\muν}(0)⟩_{combined}=lim\deltat→0\sumi=0t_{1}\deltat\sum(\muν)⟨P_{\muν}(i\deltat)P_{\muν}(0)⟩_{ short}+lim\deltat→0\sumi=t_{1}T\deltat\sum(\muν)⟨P_{\muν}(i\deltat)P_{\muν}(0)⟩_{ long}^{fit},
$$

where $t_{1}\deltat$ is the end point of $⟨P_{\muν}(t)P_{\muν}(0)⟩_{short}$ and $T\deltat$ is the end point of $⟨P_{\muν}(i\deltat)P_{\muν}(0)⟩_{combined}$.
