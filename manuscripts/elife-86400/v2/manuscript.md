# Hydrodynamics and multiscale order in confluent epithelia

## Authors

- Josep-Maria Armengol-Collado<sup>1</sup> ([ORCID: 0000-0003-0740-3040](https://orcid.org/0000-0003-0740-3040))
- Livio Nicola Carenza<sup>1</sup> ([ORCID: 0000-0001-5996-331X](https://orcid.org/0000-0001-5996-331X))
- Luca Giomi<sup>1</sup> ([ORCID: 0000-0001-7740-5960](https://orcid.org/0000-0001-7740-5960)) †

### Affiliations

1. Instituut-Lorentz, Leiden University Leiden Netherlands ([ROR:027bh9e22](https://ror.org/027bh9e22))

† Corresponding author

## Abstract

We formulate a hydrodynamic theory of confluent epithelia: i.e. monolayers of epithelial cells adhering to each other without gaps. Taking advantage of recent progresses toward establishing a general hydrodynamic theory of p-atic liquid crystals, we demonstrate that collectively migrating epithelia feature both nematic (i.e. p = 2) and hexatic (i.e. p = 6) orders, with the former being dominant at large and the latter at small length scales. Such a remarkable multiscale liquid crystal order leaves a distinct signature in the system’s structure factor, which exhibits two different power-law scaling regimes, reflecting both the hexagonal geometry of small cells clusters and the uniaxial structure of the global cellular flow. We support these analytical predictions with two different cell-resolved models of epithelia – i.e. the self-propelled Voronoi model and the multiphase field model – and highlight how momentum dissipation and noise influence the range of fluctuations at small length scales, thereby affecting the degree of cooperativity between cells. Our construction provides a theoretical framework to conceptualize the recent observation of multiscale order in layers of Madin–Darby canine kidney cells and pave the way for further theoretical developments.

## Introduction

Collective cell migration $−$– i.e. the ability of multicellular systems to cooperatively flow, even in the absence of a central control mechanism $−$– has surged, in the past decade, as one of the central questions in cell biology and tissue biophysics (Friedl and Gilmour, 2009). Whether spreading on a synthetic substrate (Serra-Picamal et al., 2012) or invading the extracellular matrix (Haeger et al., 2020), multicellular systems can move coherently within their micro-environment and coordinate the dynamics of their actin cytoskeleton, while retaining cell–cell contacts. This ability lies at the heart of a myriad of processes that are instrumental for life, such as embryonic morphogenesis and wound healing, but also of life-threatening conditions, such as metastatic cancer.

Understanding the physical origin of this behavior inevitably demands reliable theoretical models, aimed at providing a conceptual framework for dissecting and deciphering the wealth of biophysical data stemming from in vitro experiments and in vivo observations. Following the pioneering works by Honda, 1978; Nagai and Honda, 2001; Farhadifar et al., 2007; Bi et al., 2015; Bi et al., 2016, and others (Boromand et al., 2018; Mueller et al., 2019; Loewe et al., 2020; Monfared et al., 2021), cell-resolved models have played so far the leading role in this endeavour. Taking inspiration from the physics of foams (Graner et al., 2008; Marmottant et al., 2008), these models portray a confluent tissue as a collection of adjacent or overlapping polygonal cells (Figure 1a, b), whose dynamics is assumed to be governed by a set of overdamped Langevin equations, expressing the interplay between cells’ autonomous motion and remodeling events, which change the local topology of the cellular networks.

![Figure 1.](https://cdn.elifesciences.org/articles/86400/elife-86400-fig1-v2.jpg)

**Figure 1.:** (a) Example of multiscale hexanematic order in an in vitro layer of Madin–Darby canine kidney (MDCK) cells (b) and its computer-constructed segmentation. Both panels are adapted from Figure 3 of Armengol-Collado et al., 2023. The six-legged stars in the shaded region denote the sixfold orientation of the cells obtained using the approach summarized in Methods. The colored stripes mark the configuration of the nematic director at the length scale of the light-blue disk. (c) Schematic representation of the sixfold symmetric force complexion exerted by cells. The red arrows indicate the structure of the contractile forces acting within the cellular junctions.

Despite their conceptual simplicity, cell-resolved models agree remarkably well with experimental data on confluent monolayers (Park et al., 2015; Atia et al., 2018). In particular they account for a solid-to-liquid transition controlled by the cells velocity and their compliance to deformations (Bi et al., 2015; Bi et al., 2016; Loewe et al., 2020). Furthermore, as demonstrated by Pica Ciamarra and coworkers, the solid and isotropic liquid states of these model-epithelia are separated by an intermediate hexatic phase, in which the system exhibits the typical sixfold rotational symmetry of two-dimensional crystals and yet is able to flow (Li and Ciamarra, 2018; Pasupalak et al., 2020). Shortly after discovery, the same property has been recovered within the framework of the cellular Potts model, thereby strengthening the idea that hexatic order may in fact serve as a guiding principle to unravel the collective dynamics of confluent epithelia (Durand and Heu, 2019). Furthermore, recent in vitro studies of Madin–Darby canine kidney (MDCK) cell layers demonstrated that epithelial layers can in fact feature both nematic and hexatic orders, with the former being dominant at large and the latter at short length scales (see Figure 1a, b and Armengol-Collado et al., 2023; Eckert et al., 2023). This remarkable example of physical organization in biological matter, referred to as multiscale hexanematic order in Armengol-Collado et al., 2023, is believed to complement the complex network or regulatory pathways available to individual cells to achieve multicellular organization and select specific scale-dependent collective migration strategies.

Motivated by these recent discoveries, in this article we propose a continuum theory of confluent epithelia rooted in the hydrodynamics of liquid crystals with generic p-atic rotational symmetry (hereafter p-atic liquid crystals). Previous theories of epithelial hydrodynamics can be schematically grouped in two categories: (1) models based on (isotropic/polar/nematic) active gels (Ranft et al., 2010; Popović et al., 2017; Pérez-González et al., 2019); (2) models built around the so-called shape tensor (Ishihara et al., 2017; Czajkowski et al., 2018; Hernandez and Marchetti, 2021; Grossman and Joanny, 2022), i.e. a rank-2 tensor, similar to the inertia tensor in kinematics, that embodies the geometrical structure of the polygonal cells. Although both classes of models hold great heuristic value and represent a solid foundation for any future development, they suffer from the same limitation: being based on a tensorial order parameter whose rank is two or less, they can account at most for twofold rotational symmetry (i.e. nematic order), while leaving the small-scale hexatic order unresolved. To overcome this limitation, here we exploit recent advances toward extending the classic hydrodynamic theory of hexatic liquid crystals (Zippelius, 1980; Zippelius et al., 1980) to account for arbitrary p-fold rotational symmetry order (Giomi et al., 2022a; Giomi et al., 2022b), with $p=2$ and $p=6$ being the most relevant cases (but possibly not the only) in the context of epithelial dynamics. We demonstrate that multiscale order is inherent to active liquid crystals with coupled order parameters, because of the indissoluble connection between shape and forces characterizing this class of non-equilibrium systems. Using fluctuating hydrodynamics, we explicitly compute the structure factor of epithelial layers and unveil a fascinating interplay between the nature of momentum dissipation (i.e. viscosity or friction) and noise at short length scales, where hexatic order is dominant. Such a mechanism profoundly affects the range of density fluctuations and could be harnessed to control the degree of collectiveness of cellular motion. Finally, by testing predictions against two different microscopic models of epithelia we demonstrate the robustness of multiscale hexanematic order across the rich landscape of models of epithelia.

## Results and discussion

### The model

Two-dimensional p-atic liquid crystals are traditionally described in terms of the orientation field $ψ_{p}=e^{ipϑ}$, with $ϑ$ the local orientation of the p-fold mesogens. A more general approach, proposed in Giomi et al., 2022a; Giomi et al., 2022b and especially suited for hydrodynamics, revolves instead around the rank-p tensor order parameter, $Q_{p}=Q_{i_{1}i_{2}⋯i_{p}}e_{i_{1}}⊗e_{i_{2}}⊗⋯⊗e_{i_{p}}$ with $i_{n}={x,y}$ and $n=1,2…p$, constructed upon averaging the pth tensorial power of the local orientation $ν=cos⁡ϑe_{x}+sin⁡ϑe_{y}$. That is

$$
Q_{p}=\sqrt{2^{p−2}}[[⟨ν^{⊗p}⟩]]=\sqrt{2^{p−2}}|Ψ_{p}|[[n^{⊗p}]],
$$

where $⟨⋯⟩$ denotes the ensemble average and the operator $‖...‖$ has the effect of rendering an arbitrary tensor traceless and symmetric (Hess, 2015). The vector $n=cos⁡\thetae_{x}+sin⁡\thetae_{y}$ is the analog of the director field in standard lexicon of nematic liquid crystals and marks the average cellular direction, which in turn is invariant under rotations of $2\pi/p$. The fields $|Ψ_{p}|$ and $\theta$ represent, respectively, the magnitude and phase of the complex p-atic order parameter $Ψ_{p}=⟨ψ_{p}⟩$, while the normalization factor is chosen so that $|Q_{p}|^{2}=|Ψ_{p}|^{2}/2$ for all $p$ values. For $p=2$, Equation (1) readily gives the standard nematic order parameter tensor: i.e. $Q_{2}=|Ψ_{2}|(n⊗n−1/2)$, with 1 the identity tensor. In practice, if a cell’s planar projection consists of a regular p-sided polygon, the microscopic orientation $ϑ$ equates that of any of the vertices of the polygon. In the more realistic case of an irregular polygon, on the other hand, $ϑ$ is given by the phase of the complex function $\gamma_{p}$, arising form the p-fold generalization of the classic shape tensor (Aubouy et al., 2003). This function was introduced in Armengol-Collado et al., 2023 and is reviewed in Methods for sake of completeness.

The order parameter tensor $Q_{p}$, the mass density $ρ$, and the momentum density $ρv$, with $v$ the local velocity field, comprise the set of hydrodynamic variables describing the dynamics of a generic p-atic fluid, which in turn is governed by the following set of partial differential equations (Giomi et al., 2022a; Giomi et al., 2022b):

$$
\frac{Dρ}{Dt}+ρ∇⋅v=(k_{d}−k_{a})ρ,
$$



$$
ρ\frac{Dv}{Dt}=∇⋅\sigma+f,
$$



$$
\frac{DQ_{p}}{Dt}=Γ_{p}H_{p}+p[[Q_{p}⋅\omega]]+\lambda¯_{p}tr(u)Q_{p}+\lambda_{p}[[∇^{⊗(p−2)}u]]+ν_{p}[[∇^{⊗(pmod2)}u^{⊗⌊p/2⌋}]]
$$

where $D/Dt=∂_{t}+v⋅∇$. Equation (2a) and Equation 2b are the mass and momentum conservation equations, with $k_{d}$ and $k_{a}$ rates of cell division and apoptosis, $\sigma$ the stress tensor and $f$ an arbitrary external force per unit area. In Equation (2c), $Γ_{p}^{−1}$ is a rotational viscosity and $H_{p}=−\deltaF/\deltaQ_{p}$ is the molecular tensor describing the relaxation of the p-atic phase toward the minimum of the free energy $F$ (see Methods). The rank-2 tensors $\omega=[∇v−(∇v)^{⊺}]/2$ and $u=[∇v+(∇v)^{⊺}]/2$, with $⊺$ indicating transposition, are the vorticity and strain rate tensors, respectively, whereas the dot product in the first line of the equation implies a contraction of one index of $Q_{p}$ with one of $\omega$: i.e. $(Q_{p}⋅\omega)_{i_{1}⁢i_{2}⁢⋯⁢i_{p}}=Q_{i_{i}⁢i_{2}⁢⋯⁢j}⁢\omega_{j⁢i_{p}}$. On the second line $(∇^{⊗n})_{i_{1}i_{2}⋯i_{n}}=∂_{i_{1}}∂_{i_{2}}⋯∂_{i_{n}}$, while $⌊…⌋$ denotes the floor function and $pmod2=p−2⌊p/2⌋$ is zero for even $p$ values and one for odd $p$ values. Finally, $\lambda¯_{p}$, $\lambda_{p}$, and $ν_{p}$ are material parameters expressing the strength of the coupling between p-atic order and flow.

Now, in order for Equation 2a to account for the dynamics of epithelial cell layers, we must specify the structure of the external force $f$ in Equation 2b and the stress tensor $\sigma$. As cells collectively crawl on a substrate, at a speed of order 0.1–1 µm/min (Brugués et al., 2014; Angelini et al., 2011), the former can be model as a Stokesian drag: $f=−ςv$, with $ς$ a drag coefficient. A more realistic treatment of the interplay between the cells and the substrate would account for the traction forces exerted by the cells’ cryptic lamellipodium as well as for the compliance of the substrate (Trepat et al., 2009) and will be considered in the future. The stress tensor, on the other hand, is routinely decomposed into a passive and an active component: i.e. $\sigma=\sigma^{(p)}+\sigma^{(a)}$. The passive stress tensor is in turn expressed as $\sigma^{(p)}=−P1+\sigma^{(e)}+\sigma^{(r)}+\sigma^{(v)}$, where $P$ is the pressure, $\sigma^{(e)}$ is the elastic stress, arising in response of a static deformation of a fluid patch, and $\sigma^{(r)}$ and $\sigma^{(v)}$ are, respectively, the reactive (i.e. energy preserving) and viscous (i.e. energy dissipating) stresses originating from the reversible and irreversible couplings between p-atic order and flow. The generic expression of $\sigma^{(p)}$ was derived in Giomi et al., 2022b and is reported in Methods.

The active stress $\sigma^{(a)}$, on the other hand, can be constructed phenomenologically for arbitrary $p$ values in the form

$$
\sigma^{(a)}=\sump(\alpha_{p}∇^{⊗(p−2)}⊙Q_{p}+\beta_{p}[[∇^{⊗2}|Q_{p}|^{2}]]),
$$

where the symbol $⊙$ denotes a contraction of all matching indices of the two operands and yields a tensor whose rank equates the number of unmatched indices: i.e. letting $A_{p}$ and $B_{q}$ be two generic tensors of rank $p<q$, then $(A_{p}⊙B_{q})_{i_{1}i_{2}⋯i_{q−p}}=A_{j_{1}j_{2}⋯j_{p}}B_{j_{1}j_{2}⋯j_{p}i_{1}i_{2}⋯i_{q−p}}$. The sum over $p$, finally, reflects the possibility of having not only one, but multiple types of p-atic order coexisting within the same system, as experiments on in vitro layers of MDCK cells have recently suggested (Armengol-Collado et al., 2023; Eckert et al., 2023).

Before exploring the consequences of the latter assumption, some comment about the physical interpretation of the terms featured in Equation 3 is in order. The first term on the right-hand side of Equation 3 is the stress resulting from the contractile or extensile forces exerted at the length scale of individual cells. To illustrate this concept one can assume each cell to exert a p-fold symmetric force complexion: i.e. $F_{c}=\sumk=1pF_{k}\delta(r−r_{c}−aν_{k})$ with $F_{k}$ the force exerted by a cell at each vertex and originating from the imbalance of the tensions $T_{kl}$, driven by the active contraction of the cellular junctions, converging at the kth vertex: i.e. $F_{k}=\sumlT_{kl}$ (see Figure 1c). The quantities $r_{c}$ and $a$ are the cell’s centroid and circumradius, respectively, while $ν_{k}=cos⁡(ϑ+2\pik/p)e_{x}+sin⁡(ϑ+2\pik/p)e_{y}$. We stress that, while the individual tensions acting along the junctions are exclusively contractile, the resulting vertex forces can be either contractile (i.e. $F_{k}⋅ν_{k}<0$) or extensile ($F_{k}⋅ν_{k}>0$), depending on the overall tension distribution and the geometry of the cellular network. Next, assuming $F_{k}=fν_{k}$ and expanding the delta function about $a=0$ yields $F_{c}=\summ=0∞f_{m}$, where

$$
f_{m}=∇^{⊗m}⊙[\frac{(−a)^{m}f}{m!}(\sumk=1pν_{k}^{⊗(m+1)})\delta(r−r_{c})].
$$

Because of the p-fold symmetry of the force complexion $f_{m}=0$ for all even $m$ values, unless $m=p−1$, whereas odd $m$ values yields, up to symmetrization, $\sumk=1pν_{k}^{⊗(m+1)}∼1^{⊗(m+1)/2}$. Thus, after some algebraic manipulation, one finds $F_{c}≈−apf/2∇[(1+a^{2}/8∇^{2}+⋯)\delta(r−r_{c})]+f_{p−1}$. Finally, taking $⟨\sumcF_{c}⟩=−P^{(a)}1+\sigma^{(a)}$ gives the following expression for contributions to the pressure and the deviatoric stress resulting from the active expansion and contraction of the cells. That is

$$
P^{(a)}=\frac{apf}{2}(n+\frac{a^{2}}{8}∇^{2}n+⋯),
$$



$$
\sigma^{(a)}=\frac{(-a)^{p-1}⁢p⁢n⁢f}{\sqrt{2^{p-2}}⁢(p-1)!}⁢\nabla^{⊗(p-2)}⊙Q_{p},
$$

where $n=⟨\sumc\delta(r−r_{c})⟩$ is the cell number density. From Equation 5b, one finds the following expression for the phenomenological parameter $\alpha_{p}$ in Equation 3: i.e. $\alpha_{p}=(−a)^{p−1}pnf/[\sqrt{2^{p−2}}(p−1)!]$. Notice that both constants $a$ and $f$ involved in Equation 5a are, in general, order dependent. We will come back on this aspect in Conclusion.

The second term in Equation 3, in contrast, expresses the active stress resulting from the spatial variations of the p-atic order parameter and, although similar to other contributions to the passive stress $\sigma^{(p)}$, cannot be derived from equilibrium considerations. Other terms constructed by contracting $Q_{p}$ with $∇^{⊗2}$ can be expressed as linear combinations of this and $\sigma^{(p)}$, thus lead to a mere renormalization of the material parameters. It must be noted that the stress tensor enters in Equation 2b only via its divergence. Thus, possible second-order active terms such as $Q_{k_{1}k_{2}…k_{p}}∂_{i}∂_{j}Q_{k_{1}k_{2}⋯k_{p}}$, $Q_{ijk_{3}⋯k_{p}}∂_{l_{1}}∂_{l_{2}}Q_{l_{1}l_{2}k_{3}⋯k_{p}}$, etc., are mechanically equivalent to the terms $∂_{i}Q_{k_{1}k_{2}⋯k_{p}}∂_{j}Q_{k_{1}k_{2}⋯k_{p}}$ and $Q_{k_{1}k_{2}⋯i}H_{k_{1}k_{2}⋯j}−H_{k_{1}k_{2}⋯i}Q_{k_{1}k_{2}⋯j}$ arising from the passive stresses, as both sets of terms lead to the same body forces.

We observe that Equation 3 already entails a multiscale hydrodynamic behavior even when a single $p$ value is considered. Such a crossover is expected at length scales larger than $ℓ=(\alpha_{p}/\beta_{p})^{1/(p−4)}$, where the second term of the right-hand side of Equation 3 overweights the first term, reflecting the p-fold symmetry of the local active forces. In the presence of multiple types of p-atic order, the p-dependent structure of the active stress renders the multiscale nature of the system enormously more dramatic. To illustrate this crucial point, here we postulate the system to behave as a hexanematic liquid crystal. Formally, such a scenario can be accounted by simultaneously solving two variants of Equation 2c, for $Q_{2}$ and $Q_{6}$. In turn, the interplay between nematic and hexatic order results from a combination of dynamical and energetic effects. The former arise from active flow, which affects the local configuration of both tensor order parameters via the last four terms in Equation 2c. The latter, instead, can be embedded into the free energy $F=\intdA(f_{2}+f_{6}+f_{2,6})$, where

$$
f_{p}=\frac{1}{2}⁢L_{p}⁢|\nabla⁡Q_{p}|^{2}+\frac{1}{2}⁢A_{p}⁢|Q_{p}|^{2}+\frac{1}{4}⁢B_{p}⁢|Q_{p}|^{4},
$$



$$
f_{2,6}=κ_{2,6}⁢|Q_{2}|^{2}⁢|Q_{6}|^{2}+χ_{2,6}⁢Q_{2}^{⊗3}⊙Q_{6}.
$$

Here, $A_{p}$ and $B_{p}$ are constants setting the magnitude of the order parameter at the length scale of the short distance cut-off, here assumed to be of the order of the cell size, and $κ_{2,6}$ determines the extent to which the magnitude of the hexatic order parameter is influenced by that of the nematic order parameter and vice versa. The constant $χ_{2,6}$, on the other hand, is analogous to an inherent susceptibility, expressing the propensity of the nematic and hexatic directors toward mutual alignment. The free energy contribution $f_{2,6}$ can further be augmented with several additional terms of higher differential order: e.g. $(Q_{2}⊙\nabla⁡Q_{2})⋅(Q_{6}⊙\nabla⁡Q_{6})$, $|\nabla⁡(Q_{2}^{⊗3}⊙Q_{6})|^{2}$, $\nabla^{2}⁡(Q_{2}^{⊗3}⊙Q_{6})$, etc. For simplicity, here we ignore these and higher-order couplings and focus on the zeroth order terms included in Equation 6b.

Crucially, Equation 3, Equation 6a entail two length scales, reflecting the distance at which the passive torques originating from the entropic elasticity of the nematic and hexatic phases counterbalance those arising from the active stresses:

$$
ℓ_{2}=\sqrt{\frac{L_{2}}{|\alpha_{2}|}},ℓ_{6}=\sqrt{\frac{|\alpha_{6}|}{L_{6}}}.
$$

The former is the well-known active nematic length scale, dictating both the hydrodynamic stability (Voituriez et al., 2005) and the large-scale structure of spatiotemporal chaos in active nematics (Giomi, 2015) and whose signature in multicellular systems has been identified in both eukaryotes (Blanch-Mercader et al., 2018) and prokaryotes (You et al., 2018). The latter, on the other hand, sets the typical size of hexatic domains at the small length scale. Remarkably, $ℓ_{2}$ and $ℓ_{6}$ inversely depend on the magnitude of cellular forces (see Equation 5a). Thus, increasing activity has the effect of collapsing the multiscale structure of the system toward a single length scale, where $ℓ_{2}≈ℓ_{6}$. Two additional length scales, of purely passive nature, originate from the competition between rotational diffusion and the ordering dynamics driven by either liquid crystalline structure on the other one. These are given by $ℓ_{χ,2}=\sqrt{L_{2}/χ_{2,6}}$ and $ℓ_{χ,6}=\sqrt{L_{6}/χ_{2,6}}$. Their role will be discussed in the following section, in the framework of fluctuating hydrodynamics.

Finally, in the passive limit, when $\alpha_{2}=0$ and $\alpha_{6}=0$, Equations 2 and 6, reduce to those of a two-dimensional liquid crystal with coupled nematic and hexatic order parameter. The latter can be found, e.g., in free-standing liquid hexatic films (Dierker and Pindak, 1987; Sprunt and Litster, 1987), where molecules are either orthogonal to the mid-surface of the film or tilted by a fixed angle. In the latter case, the projection of the average molecular direction on the tangent plane of the mid-surface gives rise to in-plane nematic order, which is coupled to the sixfold bond-orientational order associated with the underlying hexatic phase (see e.g. Bruinsma and Aeppli, 1982; Selinger and Nelson, 1989; Selinger, 1991 for a theoretical account and Drouin-Touchette et al., 2022 for recent developments). As we will detail in the following, activity profoundly alters this scenario by acting as a mechanical bandpass filter, which renders hexatic order dominant at length scales $ℓ≪ℓ_{6}$ and nematic order at length scales $ℓ≫ℓ_{2}$. We stress that by dominant, here we intend able to drive morphological features, dynamical behaviors, and fluctuations reflecting the underlying orientational order. At intermediate length scales, i.e. $ℓ_{6}≪ℓ≪ℓ_{2}$, there is no dominant order and the system’s collective behavior is determined by the complex interplay of competing active and passive effects. To make progress, here we focus on the most dramatic hexatic- and nematic-dominated behaviors and treat intermediate length scales as simply as possible.

### Multiscale order in epithelia

To elucidate the multiscale organization of the system, we next compute the structure factor $S(|q|)$, using the classic framework of fluctuating hydrodynamics (see e.g. Ramaswamy et al., 2003). To this end, we assume both the nematic and the hexatic scalar order parameters to be uniform throughout the system and set $k_{d}=k_{a}$ and $\lambda_{p}=0$ for simplicity. We stress that the validity of this approximation is strictly related with the present comparison between the hydrodynamic theory presented in this article and cell-resolved models. An assessment of the relevance of this and the other material parameters featured in Equation 2a can only be achieved via experimental scrutiny and is likely to depend on the specific cell type and environmental conditions. Furthermore, as the typical Reynolds number of collective epithelial flow is in the range 10−7–10−6, we neglect inertial effects: i.e. $ρDv/Dt=0$. With these simplifications, whose legitimacy will be assessed a posteriori, one can reduce Equation 2b to three coupled differential equations for the density and the phases of the hexatic and nematic order parameter tensors (see Methods). These equations, in turn, can be linearized about the trivial configuration, where all fields are spatially uniform and $v=0$, and augmented with noise terms to give the following exact asymptotic expansion

$$
S(|q|)∼\frac{s_{−2}}{|q|^{2}}+s_{\beta}|q|^{\beta}.
$$

The first term entails the typical giant number density fluctuations associated with the active nematic behavior at the large scale, with $s_{−2}∼\alpha_{2}^{2}$. This effect is overestimated at the linear order, leading to an inverse quadratic dependence on the wave number $|q|$ (Ramaswamy et al., 2003), but is generally renormalized by nonlinearities, so that $lim|q|→0S(|q|)∼|q|^{−\alpha}$, with $1<\alpha<2$ (Shankar et al., 2018; Chaté, 2020).

The second term, on the other hand, reflects the sixfold symmetry characterizing the structure of epithelia at the small length scale, with $s_{\beta}∼\alpha_{6}^{2}$ and the exponent $\beta$ determined by the specific energy dissipation mechanism, as well as by the specific structure of the noise. As detailed in Methods, here we consider four alternative scenarios, obtained upon combining two different momentum dissipation mechanisms (i.e. viscosity and friction) with two different types of noise (i.e. rototranslational and purely rotational). In the presence of viscous dissipation, i.e. a regime referred to as ‘wet‘ in the jargon of active matter, $\beta=4$ irrespective of the nature of noise. Conversely, in the ‘dry‘ limit, when the shear and bulk viscosity vanish and momentum dissipation solely results from the frictional interactions with the substrate, $\beta$ differs depending on whether noise affects both cells’ orientational and translational dynamics, or only the former. Specifically, when only orientational noise is considered, $\beta=6$. In contrast, $\beta=10$ in the presence of conservative rototranslational noise. We again stress that Equation (8) is an exact asymptotic expansion, as one could verify upon comparison with the full analytical solutions plotted in Figure 2, and not a truncated power series.

![Figure 2.](https://cdn.elifesciences.org/articles/86400/elife-86400-fig2-v2.jpg)

**Figure 2.:** Structure factor $S(|q|)$ obtained from the analytical solutions of the linearized hydrodynamic equations in the presence of two different noise fields: purely rotational (blue) and rototranslational (red).The full analytical expression of $S(|q|)$ is given in Methods, together with a derivation of the exact asymptotic expansions of Equation (8). (a) As long as viscous dissipation takes place (i.e. ‘wet’ regime), $S(|q|)∼|q|^{4}$ in the limit $|q|→∞$, irrespective of the type of noise. (b) On the other hand, when friction is the sole momentum dissipation mechanism at play (‘dry’ regime), $S(|q|)∼|q|^{6}$ in case of rotational noise and $S(|q|)∼|q|^{10}$ when noise is both rotational and translational. In both panels, the wave number $|q|$ is rescaled by $q¯=2\pi/ℓ¯$, with $ℓ¯=(ℓ_{2}+ℓ_{6})/2$ and $ℓ_{2}$ and $ℓ_{6}$ as defined in Equation (7).

To test the significance of these predictions and connect the present hydrodynamic theory with the existing literature, in Figure 3a we compare the structure factor obtained from numerical simulations of two different cell-resolved models of epithelia – i.e. the self-propelled Voronoi (SPV) model (Bi et al., 2016) and the multiphase field (MPF) model (Loewe et al., 2020) (see the insets Figure 3b for typical configurations of the two models) – with that resulting from a numerical integration of Equation 2a (Carenza et al., 2019; Carenza et al., 2020), with none of the simplifications behind Equation (8). In both microscopic models, cells are treated as persistent random walkers, self-propelling at constant speed $v_{0}$ and whose direction of motion undergoes rotational diffusion with diffusion coefficient $D_{r}$ (see Methods for details). Noise is therefore expected to affect both the rotational and translational dynamics of the cell monolayer, although in a way that, unlike in our analytical treatment, cannot be trivially decoupled. Consistently with our linear analysis, both data sets exhibit two different power-law scaling regimes at small and large length scales. At small length scales, the structure factor scales like $S(|q|)∼|q|^{\beta}$, with $\beta$ monotonically decreasing from 6 to 4 upon increasing the Péclet number $Pe=ξ_{0}/a$ expressing the ratio between cells’ persistence length $ξ_{0}=v_{0}/D_{r}$ and their typical size $a$ (see Figure 3b).

![Figure 3.](https://cdn.elifesciences.org/articles/86400/elife-86400-fig3-v2.jpg)

**Figure 3.:** (a) Structure factor of model-epithelia calculated from a numerical integration of Equation 2a (black line) and from simulations of two different cell-resolved models: i.e. the self-propelled Voronoi model (SPV, red) and the multiphase field (MPF) model (blue), for a particular choice of parameters. The dashed diagonal lines mark the scaling regimes obtained analytically at the linear order, Equation (8), and the wave number $|q|$ is rescaled by $q_{cell}=2\pi/Δx_{LB}$, where $Δx_{LB}$ is the grid size used by the Lattice Boltzmann integrator (see Methods for details). (b) The exponent $\beta$, as defined in Equation (8), versus the Péclet number $Pe$, reflecting the persistence of directed cellular motion in front of diffusion. Error bars calculated as standard error over $n=250$ configurations for both the SPV and the MPF models. Insets: typical configurations of the SPV (bottom left) and MPF (top right) models.

Conversely, at large length scales, the structure factor scales like an inverse power law, with exponent consistent with the large-scale behavior of active nematics (Chaté, 2020). These observations can be rationalized in the light of the previous fluctuating hydrodynamic analysis. In the limit $Pe→0$, cells do not self-propel, noise is predominantly orientational and momentum propagates only at distances comparable to the average cell size. Under this circumstances, an in silico cell layer, whether modeled via the SPV or the MPF, behaves therefore as a ‘dry’ active system subject to purely rotational noise, for which, consistently with our analysis, $\beta=6$. Increasing $Pe$ has the twofold effect of converting noise from purely rotational to rototranslational and, by stimulating cooperativity in the cellular motion, to increase the range of momentum propagation, thus driving a crossover of the cell layer from ‘dry’ to ‘wet’, hence from $\beta=6$ to $\beta=4$. The simple linear calculation, summarized in Methods, does not allow us to resolve the full crossover, but does provide a precise estimate of the upper and lower bounds. Finally, along the wet–dry crossover, viscosity must emerge from the cells’ lateral interactions. A precise understanding of this process is outside of the scope of the present work, but recent numerical work on the Vertex model has already highlighted the existence of a rich landscape of exotic rheological phenomena, resulting from the interplay between cellular motion, morphology, and adhesion (Tong et al., 2022; Hertaeg et al., 2022). The latter could possibly explain the non-monotonic behavior at small $Pe$ values, as a crossover from a shear-thinning to the shear-thickening behavior (Hertaeg et al., 2022) for additional numerical evidence of this effect.

A different signature of multiscale hexanematic order can be identified in the structure of the cross-correlation function

$$
C_{26}(r)=\frac{⟨ψ_{2}(r)ψ_{6}^{∗}(0)+ψ_{2}^{∗}(r)ψ_{6}(0)⟩}{2}.
$$

At equilibrium, and if deformations are sufficiently gentle to render backflow effects negligible, its behavior can be divided in two regimes, depending on how the distance $|r|$ compares to the length scales $ℓ_{χ,2}$ and $ℓ_{χ,6}$ defined in the previous section and expressing the typical distance at which the mutual alignment rate of the hexatic and nematic orientations overcome that of rotational diffusion. In the simplest possible setting, when $ℓ_{χ,2}=ℓ_{χ,6}=ℓ_{χ}$, fluctuations dominate at short distances and the hexatic and nematic orientations are uncorrelated. Thus, $C_{26}(r)$ is approximatively constant for $|r|≪ℓ_{χ}$. The picture is reversed for $|r|≫ℓ_{χ}$. In this range, the hexatic and nematic orientations are ‘locked’ in a parallel configuration, i.e. $Arg⁡(ψ_{2})/2≈Arg⁡(ψ_{6})/6$, or tilted by $\pi/6$ with respect to each other, depending on the sign of the constant $χ_{2,6}$, and the cross-correlation function exhibits the standard power-law decay characterizing two-dimensional liquid crystals with a single-order parameter: i.e. $C_{26}(r)∼(|r|/ℓ_{χ})^{−η_{26}}$, with $η_{26}$ a specific instance of the generic non-universal exponent $η_{26}=6k_{B}T/(\piK)$, with $K$ the orientational stiffness of both phases (proportional to $L_{2}=L_{6}$). An analytical treatment of this simple case is reported in Methods. In the more generic case, in which $ℓ_{χ,2}\neqℓ_{χ,6}$ and the relaxation rates of the hexatic and nematic phase differ, the cross-correlation function has a less standard functional form, but still features a slow and fast decay regime at short and large distances, respectively. An example of such a scenario, obtained from a numerical integration of Equation 2a with $\alpha_{2}=0$ and $\alpha_{6}=0$, is shown in Figure 4a. The curves in Figure 4b correspond instead to simulated configurations of the cross-correlation function of $C_{26}(r)$ for finite hexatic and nematic activity. In this case, the cross-correlation function exhibits an oscillatory behavior at short distances and vanishes at a length scale that becomes progressively large as the hexatic activity is increased. Consistently with our previous analysis, this latter feature confirms the existence of a hierarchy of orientationally ordered structures nested into each other at different length scales.

![Figure 4.](https://cdn.elifesciences.org/articles/86400/elife-86400-fig4-v2.jpg)

**Figure 4.:** Cross-correlation function $C_{26}(r)$, as defined in Equation 9, obtained from a numerical integration of Equation 2a augmented with rotational noise.(a) In the passive case, when $\alpha_{2}=0$ and $\alpha_{6}=0$, the correlation function decays with $|r|$ at a rate i.e. lower at short distances, where the dynamics of the hexatic and nematic orientations is dominated by fluctuations, and larger at long distances, where the orientations are ‘locked’ in a parallel configuration, or tilted by $\pi/6$ with respect to each other. (b) In the active case, conversely, the cross-correlation function has a damped oscillatory behavior. Consistently with Equation (7) and the related discussion, the range of the oscillations, corresponding to the distance at which these are fully damped, increases with the hexatic activity $\alpha_{6}$, indicating an enhancement of hexatic order at larger length scales. Shaded region corresponding to the standard deviation of $n=500$ configurations. Distance is expressed in terms of the grid size $Δx_{LB}$ used by the Lattice Boltzmann integrator (see Methods for details).

Taken together, our calculations of the structure factor and the cross-correlation function demonstrate that the hydrodynamic theory embodied in Equations 2 and 6 is able to account for the multiscale hexanematic order observed in experiments (Armengol-Collado et al., 2023; Eckert et al., 2023) and harnesses it into a continuum mechanical framework. Whereas the origin of hexanematic order is still a matter of investigation, the current experimental and numerical evidence suggests that, similarly to granular materials (Majmudar and Behringer, 2005), large-scale nematic order could arise from the self-organization of the microscopic force hexapoles into force chains. The possibility of similarity between these two phenomena has also been in relation to the initial phase of Drosophila gastrulation, where linear arrays of cells simultaneously undergo apical constriction in the ventral furrow region (Jason Gao et al., 2016).

### Conclusions

In conclusion, we have introduced a continuum model of collectively migrating layers of epithelial cells, built upon a recent generalization of the hydrodynamic theory of p-atic liquid crystals (Giomi et al., 2022a; Giomi et al., 2022b). This approach allows one to account for arbitrary discrete rotational symmetries, thereby going beyond existing hydrodynamic theories of epithelia (Ranft et al., 2010; Popović et al., 2017; Pérez-González et al., 2019; Ishihara et al., 2017; Czajkowski et al., 2018; Hernandez and Marchetti, 2021; Grossman and Joanny, 2022), where the algebraic structure of the hydrodynamic variables renders impossible to account for liquid crystal order other than isotropic (i.e. $p=0$), polar (i.e. $p=1$), or nematic (i.e. $p=2$). Upon computing the static structure factor and comparing this with the outcome of two different cell-resolved models – i.e. the SPV (Bi et al., 2016) and MPF (Loewe et al., 2020) models – we have shown that, consistently with recent experimental findings (Armengol-Collado et al., 2023; Eckert et al., 2023), epithelial layers may in fact comprise both nematic and hexatic (i.e. $p=6$) order, coexisting at different length scales. Although the consequences of such a remarkable versatility are yet to be explored, we expect hexatic order to be relevant for short-scale remodeling events, where the local nature of hexatic order, combined with the rich dynamics of hexatic defects (Zippelius et al., 1980; Amir and Nelson, 2012), may mediate processes such as cell intercalations and the rearrangement of multicellular rosettes (Blankenship et al., 2006; Rauzi, 2020). Such a local motion, in turn, may be coordianted at the large scale by the underlying nematic order, giving rise to a persistent unidirectional flow, such as that observed during wound healing and cancer progression (Friedl and Gilmour, 2009). Furthermore, the existence of multiscale liquid crystal order echoes the most recent understanding of phenotypic plasticity in tissues, according to which the epithelial (i.e. solid-like) and mesenchymal (i.e. liquid-like) states represent the two ends of a spectrum of intermediate phenotypes (Zhang and Weinberg, 2018). These intermediate states display distinctive cellular characteristics, including adhesion, motility, stemness and, in the case of cancer cells, invasiveness, drug resistance, etc. Can multiscale liquid crystal order help understanding how the biophysical properties of tissues vary along the epithelial–mesenchymal spectrum? This and related questions will be addressed in the near future.

## Methods

### Quantification of p-atic order in epithelial layers

Following Armengol-Collado et al., 2023, we use the shape function$\gamma_{p}$ to quantify the amount of p-fold symmetry of an arbitrary cell. Denoting $r_{v}$ with $v=1,2…V$, the positions of its vertices with respect to the cell’s center of mass, one has

$$
\gamma_{p}=\frac{\sumv=1V|r_{v}|^{p}e^{ipϕ_{v}}}{\sumv=1V|r_{v}|^{p}},
$$

with $ϕ_{v}=Arg⁡(r_{v})$ the angle between $r_{v}$ and the x-axis of a Cartesian frame. A schematic representation of these elements in an arbitrary irregular polygon is shown in Figure 5a. Unlike the complex function $ψ_{p}=e^{ipϑ}$, which has unit magnitude by construction, the magnitude $|\gamma_{p}|$ quantify the resemblance of a generic polygon with a regular p-sided polygon of the same size, while the phase $ϑ=Arg⁡(\gamma_{p})/p$ marks the orientation of the polygon. For regular V-sided polygons, $|\gamma_{p}|=1$ provided $p$ is an integer multiple of $V$ and $|\gamma_{p}|≈0$ otherwise. Furthermore, from $\gamma_{p}$ one can readily compute.

$$
ψ_{p}=\frac{\gamma_{p}}{|\gamma_{p}|}.
$$

![Figure 5.](https://cdn.elifesciences.org/articles/86400/elife-86400-fig5-v2.jpg)

**Figure 5.:** (a) Irregular polygonal cell with a red cross marking its center of mass and $r_{v}$ and $ϕ_{v}$ the radial vector and the angle to one of the six vertices, respectively. (b) and (c) show the same tessellation of the plane with cells of different shapes and the shape analysis using the function in Equation 10 for the nematic ($p=2$) and hexatic ($p=6$) case. Rods and stars are oriented according to the phase of $\gamma_{p}$ and the color corresponds to its magnitude.

Figure 5b, c shows examples of the functions $\gamma_{2}$ and $\gamma_{6}$ for a typical configuration of the SPV. We emphasize that $\gamma_{p}$, which, as shown in Armengol-Collado et al., 2023, arises from a p-fold generalization of the classic shape tensor (Aubouy et al., 2003), is solely determined by the positions of the vertices of an individual polygon and, therefore, does not depend on the spatial organization of the neighboring cells. As a consequence, this approach establishes an orientation purely based on cellular shape, thereby eliminating the arbitrariness involved with associating a network of bonds to a planar tessellation, where the latter is not inherent.

The shape function $\gamma_{p}$ can then be coarse grained at the length scale $ℓ$ to construct the shape parameter:

$$
Γ_{p}(r)=\frac{1}{N_{ℓ}}\sumc=1\gamma_{p}(r_{c})Θ(ℓ−|r−r_{c}|),
$$

where the $r_{c}$ is the position of the cth cell, $Θ$ is the Heaviside step function, such that $Θ(x)=1$ for $x>0$ and 0 otherwise, and $N_{ℓ}=\sumcΘ(ℓ−|r−r_{c}|)$ is the number of cells within a distance $ℓ$ from $r_{c}$. As in the case of $\gamma_{p}$, the magnitude of $Γ_{p}$ reflects the resemblance between a multicelluar cluster and a regular p-sided polygon, while its phase marks the cluster’s global orientation. The outcome of an application of this method to the Voronoi model is illustrated in Figure 6 for $p=2$. The different patches in panel (a) are regions with uniform $\theta=Arg⁡(Γ_{2})/2$, while in panel (b), there are plotted streamlines showing the orientation of the director $n=cos⁡\thetae_{x}+sin⁡\thetae_{y}$.

![Figure 6.](https://cdn.elifesciences.org/articles/86400/elife-86400-fig6-v2.jpg)

**Figure 6.:** (a) Coarse-grained nematic orientation $\theta$ obtained from averaging the local shape of cells over domains of size $30ℓ_{cell}$, with $ℓ_{cell}$ the average size of individual cells. Regions with the same color represent domains of coherent nematic orientation. (b) Part of the system where we use $Γ_{2}$ to characterize the nematic phase. Solid lines represent the nematic director and the color inditicates the magnitude of the nematic shape function. (c) Voronoi cell structure of a region where the nematic field is uniform. Polygons are colored according to $|\gamma_{6}|$ and the stars are oriented according to $Arg⁡(\gamma_{6})/6$.

### Passive stresses

As explained in the main text, the passive contribution to the stress tensor is given by $\sigma^{(p)}=−P1+\sigma^{(e)}+\sigma^{(r)}+\sigma^{(v)}$, where, as demonstrated in Giomi et al., 2022b

$$
\sigma_{i⁢j}^{(e)}=-L_{p}⁢\partial_{i}⁡Q_{p}⊙\partial_{j}⁡Q_{p},
$$



$$
\sigma_{ij}^{(r)}=−\lambda¯_{p}Q_{p}⊙H_{p}\delta_{ij}+(−1)^{p−1}\lambda_{p}∂_{k_{1}k_{2}⋯k_{p−2}}^{p−2}H_{k_{1}k_{2}⋯ij}+\frac{p}{2}(Q_{k_{1}k_{2}⋯i}H_{k_{1}k_{2}⋯j}−H_{k_{1}k_{2}⋯i}Q_{k_{1}k_{2}⋯j}),
$$



$$
\sigma_{ij}^{(v)}=2η[[u_{ij}]]+ζtr(u)\delta_{ij},
$$

where $η$ and $ζ$ are, respectively, the shear and bulk viscosity and the other material parameters are defined in the main text. Under the assumptions of uniform order parameter, i.e. $|Q_{p}|^{2}=|Ψ_{p}|^{2}/2=const$, and taking $\lambda_{p}=0$, Equation 13a reduces to the expression derived in Zippelius, 1980; Zippelius et al., 1980. That is

$$
\sigma^{(e)}+\sigma^{(r)}=−P1+\frac{K_{p}}{2}\epsilon∇^{2}\theta−K_{p}∇\theta⊗∇\theta,
$$

where the first term in Equation 13b has incorporated into the pressure $P$ and $K_{p}$ denotes the orientational stiffness of the p-atic phase, related to the order parameter stiffness by

$$
K_{p}=\frac{p^{2}|Ψ_{p}|^{2}}{2}L_{p}
$$

and $varepsilon$ is the two-dimensional antisymmetric tensor, with $\epsilon_{xy}=−\epsilon_{yx}=1$ and $\epsilon_{xx}=\epsilon_{yy}=0$.

### Linear fluctuating hydrodynamics

To compute the structure factor, we follow Ramaswamy et al., 2003 and augment Equation 2b, Equation 2c with short-ranged correlated noise field. Then calling $ϑ$ and $\phi$ the nematic and hexatic fluctuating orientation fields and linearizing the hydrodynamic equations about the homogeneous and stationary solutions, $ϑ=\phi=0$ and $v=0$, gives

$$
∂_{t}\deltaρ=−ρ_{0}∇⋅\deltav,
$$



$$
∂_{t}\deltaϑ=D_{2}∇^{2}\deltaϑ+\frac{1}{2}e_{z}⋅(∇\times\deltav)+\frac{9}{4}χ_{2}(\deltaϑ−\delta\phi)+ξ^{(ϑ)},
$$



$$
∂_{t}\delta\phi=D_{6}∇^{2}\delta\phi+\frac{1}{2}e_{z}⋅(∇\times\deltav)+\frac{1}{4}χ_{6}(\delta\phi−\deltaϑ)+ξ^{(\phi)},
$$

where $\deltaϑ$, $\delta\phi$, and $\deltav$ indicate a small departure from the homogeneous and stationary configurations of the fields $ϑ$, $\phi$, and $v$, $D_{p}=Γ_{p}L_{p}$, $χ_{p}=Γ_{p}χ_{2,6}$, and $ξ^{(ϑ)}$ and $ξ^{(\phi)}$ are short-ranged correlated noise fields: i.e.

$$
⟨ξ^{(\alpha)}(r,t)ξ^{(\beta)}(r^{′},t^{′})⟩=2(Ξ^{(ϑ)}\delta_{\alphaϑ}\delta_{\betaϑ}+Ξ^{(\phi)}\delta_{\alpha\phi}\delta_{\beta\phi})\delta(r−r^{′})\delta(t−t^{′}).
$$

The velocity field $\deltav$, on the other hand, is found from the Stokes limit of Equation 2b in the main text, which, at the linear order in all fluctuating fields, takes the form

$$
η∇^{2}\deltav+ζ∇(∇⋅\deltav)−ς\deltav+f^{(p)}+f^{(a)}+ξ^{(v)}=0.
$$

where $f^{(p)}=∇⋅\sigma^{(p)}$ and $f^{(a)}=∇⋅\sigma^{(a)}$ are the body forces resulting from the passive and active stresses, respectively. The quantity $ξ^{(v)}$ is a translational noise field. In the absence of external stimuli, it is reasonable to assume that global momentum is neither created nor dissipated by translational fluctuations, but only redistributed across the cell layer. Thus $ξ^{(v)}$ is either conservative or null, from which

$$
⟨ξ_{i}^{(v)}(r,t)ξ_{j}^{(v)}(r^{′},t^{′})⟩=2Ξ^{(v)}\delta_{ij}(−∇^{2})\delta(r−r^{′})\delta(t−t^{′}),
$$

with ${i,j}\in{x,y}$ and the case of noiseless translational dynamics, corresponding to Figure 3 in the main text, is recovered in the limit $Ξ^{(v)}→0$. The pressure $P$, in turn, can be related to the density by a linear equation of state of the form

$$
P=c_{s}^{2}ρ,
$$

with $c_{s}$ the speed of sound. Together with the expression for the active stress given in Equation 3 of the main text, this gives

$$
f^{(p)}=(−c_{s}^{2}∂_{x}\deltaρ+\frac{K_{2}}{2}∂_{y}∇^{2}\deltaϑ+\frac{K_{6}}{2}∂_{y}∇^{2}\delta\phi)e_{x}−(c_{s}^{2}∂_{y}\deltaρ+\frac{K_{2}}{2}∂_{x}∇^{2}\deltaϑ+\frac{K_{6}}{2}∂_{x}∇^{2}\delta\phi)e_{y},
$$



$$
f^{(a)}=[\alpha_{2}∂_{y}\deltaϑ+\frac{3}{2}\alpha_{6}(∂_{y}^{4}−5∂_{x}^{2}∂_{y}^{2}+\frac{5}{2}∂_{x}^{4})∂_{y}\delta\phi]e_{x}+[\alpha_{2}∂_{x}\deltaϑ+\frac{3}{2}\alpha_{6}(∂_{x}^{4}−5∂_{x}^{2}∂_{y}^{2}+\frac{5}{2}∂_{y}^{4})∂_{x}\delta\phi]e_{y}.
$$

Now, in Fourier space Equation 18 can be cast in the form of the following linear algebraic equation

$$
[(η|q|^{2}+ς)1+ζq⊗q]⋅\deltav^=f^^{(p)}+f^^{(a)}+ξ^^{(v)},
$$

where the hat denotes Fourier transformation. Next, using

$$
[(η|q|^{2}+ς)1+ζq⊗q]^{−1}=\frac{[(η+ζ)|q|^{2}+ς]1−ζq⊗q}{(η|q|^{2}+ς)[(η+ζ)|q|^{2}+ς]},
$$

and solving Equation 22 and incorporating the resulting velocity field in Equation 16a gives, after several algebraic manipulation

$$
−i\omega[\deltaρ^\deltaϑ^\delta\phi^]=M^⋅[\deltaρ^\deltaϑ^\delta\phi^]+[η^^{(ρ)}η^^{(ϑ)}η^^{(\phi)}],
$$

where the matrix $M^$ is given by

$$
M^=[−\frac{ρ_{0}c_{s}^{2}|q|^{2}}{(η+ζ)|q|^{2}+ς}\frac{2ρ_{0}\alpha_{2}q_{x}q_{y}}{(η+ζ)|q|^{2}+ς}\frac{3ρ_{0}\alpha_{6}(3q_{x}^{5}q_{y}−10q_{x}^{3}q_{y}^{3}+3q_{x}q_{y}^{5})}{2[(η+ζ)|q|^{2}+ς]}0−D_{2}|q|^{2}−\frac{K_{2}|q|^{4}}{4(η|q|^{2})+ς}+\frac{9}{4}χ_{2}−\frac{\alpha_{2}(q_{x}^{2}−q_{y}^{2})}{(η)|q|^{2}+ς}−\frac{K_{6}|q|^{4}}{4(η)|q|^{2}+ς}−\frac{9}{4}χ_{2}−\frac{3\alpha_{6}(q_{x}^{6}−15q_{x}^{4}q_{y}^{2}+15q_{x}^{2}q_{y}^{4}−q_{y}^{6})}{8(η)|q|^{2}+ς)}0−\frac{K_{2}|q|^{4}}{4(η)|q|^{2}+ς}−\frac{1}{4}χ_{6}−\frac{\alpha_{2}(q_{x}^{2}−q_{y}^{2})}{2(η)|q|^{2}+ς)}−D_{6}|q|^{2}−\frac{K_{6}|q|^{4}}{4(η|q|^{2})+ς}+\frac{1}{4}χ_{6}−\frac{3\alpha_{6}(q_{x}^{6}−15q_{x}^{4}q_{y}^{2}+15q_{x}^{2}q_{y}^{4}−q_{y}^{6})}{8(η)|q|^{2}+ς}]
$$

and the functions $η^{(\alpha)}$, with $\alpha\in{ρ,ϑ,\phi}$, are effective noise fields whose correlation functions are given by

$$
⟨η^^{(\alpha)}(q,\omega)η^^{(\beta)}(q^{′},\omega^{′})⟩=(2\pi)^{3}2H^^{(\alpha)}(q)\delta_{\alpha\beta}\delta(q+q^{′})\delta(\omega+\omega^{′}),
$$

where the functions $H^^{(\alpha)}=H^^{(\alpha)}(q)$ are given by

$$
H^^{(ρ)}=\frac{ρ_{0}^{2}|q|^{4}}{[(η+ζ)|q|^{2}+ς]^{2}}Ξ^{(v)},
$$



$$
H^^{(\alpha)}=Ξ^{(ϑ)}\delta_{\alphaϑ}+Ξ^{(\phi)}\delta_{\alpha\phi}+\frac{|q|^{4}}{4(η|q|^{2}+ς)^{2}}Ξ^{(v)}.
$$

Notice that, while hydrodynamic flow has the effect of coloring the orientational noise embodied in the stochastic fields $ξ^{(ϑ)}$ and $ξ^{(\phi)}$, via the vorticity field on the right-hand side of Equation 16b, Equation 16c, this effect disappears at the small (i.e. $|q|→∞$) and large (i.e. $|q|→0$) scale, as long as both viscous and frictional dissipation are present.

### Structure factor

The static structure factor can be expressed in integral form as

$$
S(q)=\int_{−∞}^{∞}\frac{d\omega}{2\pi}S(q,\omega).
$$

where the dynamic structure factor $S(q,\omega)$, can be calculated from the correlation function

$$
⟨\deltaρ^(q,\omega)\deltaρ^(q^{′},\omega^{′})⟩=(2\pi)^{3}S(q,\omega)\delta(q+q^{′})\delta(\omega+\omega^{′}).
$$

To compute the left-hand side of Equation 29 one can solve Equation 24 with respect to $\deltaρ^$, $\deltaϑ^$, and $\delta\phi^$. This gives

$$
\deltaρ^=\frac{iη^^{(ρ)}}{\omega−iM^_{ρρ}}−\frac{η^^{(ϑ)}[M^_{ρϑ}(\omega−iM^_{\phi\phi})+iM^_{ρ\phi}M^_{\phiϑ}]+η^^{(\phi)}[M^_{ρ\phi}(\omega−iM^_{ϑϑ})+iM^_{ρϑ}M^_{ϑ\phi}]}{(\omega−iM^_{ρρ})[\omega^{2}−i\omega(M^_{ϑϑ}+M^_{\phi\phi})−M^_{ϑϑ}M^_{\phi\phi}+M^_{ϑ\phi}M^_{\phiϑ}]},
$$



$$
\deltaϑ^=\frac{η^^{(ϑ)}(i\omega+M^_{\phi\phi})−η^^{(\phi)}M^_{ϑ\phi}}{[\omega^{2}−i\omega(M^_{ϑϑ}+M^_{\phi\phi})−M^_{ϑϑ}M^_{\phi\phi}+M^_{ϑ\phi}M^_{\phiϑ}]},
$$



$$
\delta\phi^=\frac{η^^{(\phi)}(i\omega+M^_{ϑϑ})−η^^{(ϑ)}M^_{\phiϑ}}{[\omega^{2}−i\omega(M^_{ϑϑ}+M^_{\phi\phi})−M^_{ϑϑ}M^_{\phi\phi}+M^_{ϑ\phi}M^_{\phiϑ}]}.
$$

The static structure factor can then be expressed as

$$
S=S^{(ρ)}+S^{(ϑ)}+S^{(\phi)}.
$$

The first term on the right-hand side can be readily calculated in the form

$$
S^{(ρ)}=\int_{−∞}^{∞}\frac{d\omega}{\pi}\frac{H^^{(ρ)}}{M^_{ρρ}^{2}+\omega^{2}}=\frac{H^^{(ρ)}}{|M^_{ρρ}|}=\frac{ρ_{0}|q|^{2}Ξ^{(v)}}{c_{s}^{2}[(η+ζ)|q|^{2}+ς]},
$$

indicating that, if driven solely by pressure fluctuations, the system would relax toward a structureless homogeneous state with $S→ρ_{0}Ξ^{(ρ)}/(ςc_{s}^{2})$ when $|q|→0$. The effect of the active currents is instead accounted for by the second and third terms on the right-hand side of Equation 31, which can be cast in the general form

$$
S^{(\alpha)}=H^{(\alpha)}\int_{−∞}^{∞}\frac{d\omega}{\pi}\frac{g^{(\alpha)}(\omega)}{|h(\omega)|^{2}},\alpha={ϑ,\phi},
$$

where

$$
g^{(ϑ)}(\omega)=(M^_{ρϑ}\omega)^{2}+(M^_{ρ\phi}M^_{\phiϑ}−M^_{ρϑ}M^_{\phi\phi})^{2},
$$



$$
g^{(\phi)}(\omega)=(M^_{ρ\phi}\omega)^{2}+(M^_{ρϑ}M^_{ϑ\phi}−M^_{ρ\phi}M^_{ϑϑ})^{2},
$$



$$
h(\omega)=(\omega−iM^_{ρρ})[\omega^{2}−i\omega(M^_{ϑϑ}+M^_{\phi\phi})−M^_{ϑϑ}M^_{\phi\phi}+M^_{ϑ\phi}M^_{\phiϑ}].
$$

The integral over $\omega$ can be derived using the residue theorem upon computing the roots of the complex third-order polynomial $h$. To make progress, we express

$$
|h(\omega)|^{2}=(\omega^{2}+\omega_{1}^{2})(\omega^{2}+\omega_{2}^{2})(\omega^{2}+\omega_{3}^{2}),
$$

where $\omega_{1}$, $\omega_{2}$, and $\omega_{3}$ are given by

$$
\omega_{1}=M^_{ρρ},
$$



$$
\omega_{2}=\frac{1}{2}(M^_{ϑϑ}+M^_{\phi\phi}−\sqrt{(M^_{ϑϑ}−M^_{\phi\phi})^{2}+4M^_{ϑ\phi}M^_{\phiϑ}}),
$$



$$
\omega_{3}=\frac{1}{2}(M^_{ϑϑ}+M^_{\phi\phi}+\sqrt{(M^_{ϑϑ}−M^_{\phi\phi})^{2}+4M^_{ϑ\phi}M^_{\phiϑ}.}).
$$

The integrand on the right-hand side of Equation 33 has, therefore, three pairs of purely imaginary poles: i.e. $\pmi|\omega_{1}|$, $\pmi|\omega_{2}|$, and $\pmi|\omega_{3}|$. Next, turning the integration range to an infinite semicircular contour on the complex upper half-plane and summing the associated residues gives, after lengthy algebraic manipulations

$$
S^{(ϑ)}=\frac{H^{(ϑ)}[Ω_{1}M^_{ρϑ}^{2}+Ω_{2}(M^_{ρ\phi}M^_{\phiϑ}−M^_{ρϑ}M^_{\phi\phi})^{2}]}{Ω_{1}Ω_{2}Ω_{3}−Ω_{1}^{2}},
$$



$$
S^{(\phi)}=\frac{H^{(\phi)}[Ω_{1}M^_{ρ\phi}^{2}+Ω_{2}(M^_{ρϑ}M^_{ϑ\phi}−M^_{ρ\phi}M^_{ϑϑ})^{2}]}{Ω_{1}Ω_{2}Ω_{3}−Ω_{1}^{2}},
$$

where we have set

$$
Ω_{1}=|\omega_{1}||\omega_{2}||\omega_{3}|,
$$



$$
Ω_{2}=|\omega_{1}|+|\omega_{2}|+|\omega_{3}|,
$$



$$
Ω_{2}=|\omega_{1}||\omega_{2}|+|\omega_{1}||\omega_{3}|+|\omega_{2}||\omega_{3}|.
$$

Now, although the individual elements of the matrix $M^$ depend on the individual components of the wave vector – i.e. $q_{x}$ and $q_{y}$ – this is an artefact of linearizing the hydrodynamic equations about a specific orientation (i.e. $ϑ=\phi=0$ in this case). Because of the lack of long-ranged order and of specific directions that could affect the spectrum of density fluctuations, the latter is expected to be isotropic, thus $S=S(|q|)$. To remove the fictitious angular dependence, one can either linearize Equation 2a about a generic pair of angles, $ϑ_{0}$ and $\phi_{0}$, and then use these to calculate a circular average – i.e. $S(|q|)=1/(2\pi)^{2}\intdϑ_{0}d\phi_{0}S(q)$ – or, more simply, by orienting $q$ so to cancel the directional dependence. Thus, taking $q_{x}=q_{y}=|q|/\sqrt{2}$ gives a simpler expression of the matrix $M^$. That is

$$
M^=[−\frac{ρ_{0}c_{s}^{2}|q|^{2}}{(η+ζ)|q|^{2}+ς}\frac{ρ_{0}\alpha_{2}|q|^{2}}{(η+ζ)|q|^{2}+ς}−\frac{3ρ_{0}\alpha_{6}|q|^{6}}{4[(η+ζ)|q|^{2}+ς]}0−D_{2}|q|^{2}−\frac{K_{2}|q|^{4}}{4(η|q|^{2}+ς)}+\frac{9}{4}χ_{2}−\frac{K_{6}|q|^{4}}{4(η|q|^{2}+ς)}−\frac{9}{4}χ_{2}0−\frac{K_{2}|q|^{4}}{4(η|q|^{2}+ς)}−\frac{1}{4}χ_{6}−D_{6}|q|^{2}−\frac{K_{6}|q|^{4}}{4(η|q|^{2}+ς)}+\frac{1}{4}χ_{6}].
$$

Using the elements of this matrix in combination with Equations 31; 33, Equations 36a; 38a yields the curves plotted in Figure 3. Finally, asymptotically expanding Equation 31 allows one, after lengthy algebraic manipulations, to calculate the coefficients $s_{−2}$ and $s_{4}$ in Equation 8. That is

$$
s_{−2}=\frac{ρ_{0}\alpha_{2}^{2}[(9χ_{2})^{2}Ξ_{\phi}+χ_{6}^{2}Ξ_{ϑ}]}{c_{s}^{2}(9χ_{2}D_{6}+χ_{6}D_{2})[ρ_{0}c_{s}^{2}(9χ_{2}+χ_{6})+ς(9χ_{2}D_{6}+χ_{6}D_{2})]},
$$



$$
s_{4}=\frac{72ρ_{0}\alpha_{6}^{2}[(K_{2}^{2}+8ηD_{2}K_{2}+8η^{2}D_{2}^{2})Ξ^{(v)}+K_{2}^{2}Ξ_{ϑ}+2η^{2}(K_{2}+4ηD_{2})^{2}Ξ_{\phi}]}{c_{s}^{2}(η+ζ)[K_{2}+K_{6}+4η(D_{2}+D_{6})]^{4}}.
$$

Notice that, while both orientational and translation noise affect the amplitude of density fluctuations at small length scales, where $S(|q|)∼s_{4}|q|^{4}$, translational noise becomes unimportant at the large scale, where $S(|q|)∼s_{−2}/|q|^{2}$. Furthermore, as long as viscous dissipation is at play, switching off translational noise (i.e. $Ξ^{(v)}→0$) does not alter the scaling behavior of the structure factor at neither range of length scales. Taking the dry limit (i.e. $η→0$ and $ζ→0$) leaves the large-scale behavior unaltered, but does affect the scaling of density fluctuations at short length scales, where translational fluctuations are most prominent. Specifically, $S(|q|)∼s_{6}|q|^{6}$ in the case of purely rotational noise and $S(|q|)∼s_{10}|q|^{10}$ in the presence of rototranslational noise. The coefficients $s_{6}$ and $s_{10}$ can be computed as in the viscous case, to give

$$
s_{6}=(\frac{3}{2})^{2}\frac{ρ_{0}^{2}\alpha_{6}^{2}Ξ^{(\phi)}}{ς^{2}(D_{2}+D_{6})^{3}},
$$



$$
s_{10}=(\frac{3}{4})^{2}\frac{ρ_{0}^{2}\alpha_{6}^{2}Ξ^{(\phi)}}{ς^{4}(D_{2}+D_{6})^{3}}.
$$

### Numerical methods

#### The Voronoi model

In the self-propelled Voronoi model (Bi et al., 2016) a confluent cell layer is approximated as a Voronoi tessellation of the plane. Each cell is characterized by the position $r_{c}$ of its center, with $c=1,2…N$, and a velocity $v_{c}=v_{0}(cos⁡\theta_{c}e_{x}+sin⁡\theta_{c}e_{y})$, with $v_{0}$ a constant speed and $\theta_{c}$ an orientation. We stress that, in general, the center of a Voronoi polygon does not correspond to the polygon’s centroid (i.e. center of mass). The dynamics of these variables is governed by the following set of overdamped Langevin equations, expressing the interplay between cells’ autonomous motion and the remodeling events that underlie the tissue’s collective dynamics. That is:

$$
\frac{dr_{c}}{dt}=v_{c}−\mu∇_{r_{c}}E,
$$



$$
\frac{d\theta_{c}}{dt}=η_{c},
$$

where µ is the mobility coefficient and $E=E(r_{1},r_{2}…r_{N})$ is an energy function involving exclusively geometrical quantities, such as the area $A_{c}$ and the perimeter $P_{c}$ of each cell: i.e.

$$
E=\sumc[K_{A}(A_{c}−A_{0})^{2}+K_{P}(P_{c}−P_{0})^{2}],
$$

with $K_{A}$, $K_{P}$, $A_{0}$, and $P_{0}$ constants. The first term in Equation 43 embodies a combination of cells’ volumetric incompressibility and monolayer resistance to thickness fluctuations. The second term results from the cytoskeletal contractility (quadratic in $P_{c}$) and the effective interfacial tension caused by the cell–cell adhesion and the cortical tension (both linear in $P_{c}$) (Farhadifar et al., 2007). The constants $A_{0}$ and $P_{0}$ represent, respectively, the preferred area and perimeter of each cell. The quantity $η_{c}$, on the other hand, is a random number with zero mean and correlation function

$$
⟨η_{c}(t)η_{c^{′}}(t^{′})⟩=2D_{r}\delta_{cc^{′}}\delta(t−t^{′}),
$$

with $D_{r}$ a rotational diffusion coefficient. To make progress, we next introduce the following dimensionless numbers: the shape index $p_{0}=P_{0}/\sqrt{A_{0}}$, which accounts for the spontaneous degree of acircularity of individual cells (Bi et al., 2016), and the Péclet number $Pe=v_{0}/(D_{r}\sqrt{A_{0}})$, which quantifies the persistence of directed cellular motion in front of their diffusivity.

To obtain the plots in Figure 3, we numerically integrate Equation 42a in a domain of size $L_{g}$ with periodic boundary conditions. At $t=0$, the centroids $r_{c}$ are placed in a slightly perturbed hexagonal grid with a random initial velocity. After reaching the non-equilibrium steady state, we perform statistical averages of relevant observables.

In our numerical simulations, we set $p_{0}=3.85$, $\muK_{A}A_{0}/D_{r}=1$, $\muK_{P}/D_{r}=1$, and $D_{r}Δt=5\times10^{−3}$, where $Δt$ is the time-step used for the integration, and the average density of particles $NA_{0}/L_{g}^{2}=1$. We vary the Péclet number in the range $0.1\leqPe\leq2.0$. The results presented in Results are robust to the variation of the system size, as no qualitative difference was observed upon varying the domain size in the range $30\leqL_{g}\leq200$ at constant density. The density structure factor (light green circles) in Figure 3a was obtained, in particular, with $Pe=1.5$.

#### The MPF model

The MPF model is a continuous model where each cell is described by a concentration field $\phi_{c}=\phi_{c}(r)$ with $c=1,2…N$ and $N$ the total number of cells. This model has been used to study the dynamics of confluent cell monolayers (Loewe et al., 2020) and the mechanics of cell extrusion (Monfared et al., 2021). Equilibrium configurations are obtained upon relaxing the free energy $F=\intdAf$, where the free energy density $f$ is given by

$$
f=\frac{\alpha}{4}\sumc\phi_{c}^{2}(\phi_{c}−\phi_{0})^{2}+\frac{k_{\phi}}{2}\sumc(∇\phi_{c})^{2}+ϵ\sumc<c^{′}\phi_{c}^{2}\phi_{c^{′}}^{2}+\sumc\lambda(1−\frac{1}{\piϕ_{0}^{2}R_{\phi}^{2}}\intdA\phi_{c}^{2})^{2}.
$$

Here, $\alpha$ and $k_{ϕ}$ are material parameters which can be used to tune the surface tension $\gamma=(8k_{\phi}\alpha/9)^{1/2}$ and the interfacial thickness $ξ=(2k_{\phi}/\alpha)^{1/2}$ of isolated cells and thermodynamically favor spherical cell shapes. The constant $ϵ$ captures the repulsion between cells. The concentration field is large (i.e. $\phi_{c}≃ϕ_{0}$) inside the cells and zero outside. The contribution proportional to $\lambda$ in the free energy enforces cell incompressibility whose nominal radius is given by $R_{\phi}$. The relaxational dynamics of the field $\phi_{c}$ is governed by the Allen–Cahn equation

$$
∂_{t}\phi_{c}+v_{c}⋅∇\phi_{c}=−M\frac{\deltaF}{\delta\phi_{c}},
$$

where $v_{c}$ has the same meaning as in the SPV model described in the previous section and its dynamics is also governed by Equation 42b. The constant $M$ in Equation 46 is the mobility measuring the relevance of thermodynamic relaxation with respect to non-equlibrium cell migration. The dimensionless parameters of the model are the Péclet number $Pe=v_{0}/(2D_{r}R_{\phi})$ and the cell deformability $d=ϵ/\alpha$.

The system of partial differential equations, Equation 46, is solved with a finite-difference approach through a predictor–corrector finite-difference Euler scheme implementing second-order stencil for space derivatives (Carenza et al., 2019). The C-code implemented for numerical integration is parallelized by means of Message Passage Interface (MPI). We consider systems of $N=361$ cells in a square domain of $L_{g}=380$ grid points. Model parameters in simulation units are as follows: $R_{ϕ}=11$, $\phi_{0}=2.0$, $M\alpha=0.006$, $Mk_{\phi}=0.006$, $Mϵ=0.01$, $M\lambda=600$, $M\gamma=0.008$, $D_{r}Δt=10^{−4}$, being $Δt$ the time-step used to integrate Equation 46. We vary the speed of self-propulsion in the range $0.0\leqv_{0}\leq0.005$. In terms of dimensionless parameters this corresponds to having $d=1.66$ and $Pe$ ranging between 0 and 2.30. The timescale of cell motility with respect to the timescale of elastic relaxation driven by surface tension $v_{0}/(M\gamma)$ ranges between 0 and 0.625. Moreover, the nominal packing fraction is $N(\piR_{\phi}^{2})/L_{g}^{2}=0.95$, while the ratio between the interface thickness and the nominal radius $ξ/R_{\phi}=0.12$. The density structure factor (dark green triangles) in Figure 3a was obtained with $Pe=1.38$.

#### Numerical method for integration of the hydrodynamic equations

Equation 2a has been integrated by means of a hybrid lattice Boltzmann (LB) method, in which Equation (2b) is solved through a predictor–corrector LB algorithm and the remaining equations via a predictor–corrector finite-difference Euler approach, with a first-order upwind scheme and second-order accurate stencils for the computation of spacial derivatives (Carenza et al., 2019). The code has been parallelized by means of MPI, by dividing the computational domain in slices and by implementing the ghost-cell method to compute derivatives on the boundary of the computational subdomains. Runs have been performed using 64 CPUs in two-dimensional geometries, on a computational box of size 2562 and 5122, for at least $1.5\times10^{7}$ LB iterations (corresponding to ∼21 and ∼84 days of CPU-time, respectively, for the smaller and larger computational boxes). Periodic boundary conditions have been imposed. The director fields (for both $p=2$ and $p=6$) have been randomly initialized. The initial density field is assumed to be uniform with $ρ=2.0$ everywhere. The model parameters in simulations units are as follows: $η=ζ=1.66$, $\lambda_{2}=\lambda_{6}=1.1$, $ν_{2}=ν_{6}=0.0$, $Γ_{2}=0.4$, $A_{2}=−B_{2}=−0.04$, $L_{2}=0.04$, $Γ_{6}=0.4$, $A_{6}=−B_{6}=−0.004$, $L_{6}=0.004$, $κ_{2,6}=ξ_{2,6}=−0.004$. Nematic activity $\alpha_{2}$ has been varied in the range $−0.02\leq\alpha_{2}\leq−0.0005$ and hexatic activity $\alpha_{6}$ in the range $−0.050\leq\alpha_{6}\leq0.050$. We set the active parameters $\beta_{2}$ and $\beta_{6}=0$. The density structure factor (continuous black line) in Figure 3a was obtained with $\alpha_{2}=−2\times10^{−3}$ and $\alpha_{6}=2\times10^{−2}$.

The coherence length of the nematic and hexatic liquid crystal can be expressed as the $(L_{p}/A_{p})^{1/2}=Δx_{LB}$ for both $p=2,6$, where $Δx_{LB}$ is the grid spacing of the LB algorithm. The active length scale as defined in the main text is given for the active nematics as $ℓ_{2}$ and ranges between $10Δx_{LB}$ for $\alpha_{2}=−0.0005$ and $1.5Δx_{LB}$ for $\alpha_{2}=−0.02$. Conversely, for hexatics $ℓ_{6}$ and ranges up to $3.5Δx_{LB}$ for $|\alpha_{6}|=0.05$. To compare the results of the hydrodynamics simulations with the discrete models in Figure 3a, we choose $2Δx_{LB}=\sqrt{A_{0}}$ and $2Δx_{LB}=R_{\phi}Δx_{MP}$, with $Δx_{MP}$ the grid spacing used to integrate Equation 46.

### Comparison with passive liquid crystals with coupled order parameters

In this section, we show how multiscale hexanematic order differs from previously reported examples of liquid crystal order with coupled order parameters (Bruinsma and Aeppli, 1982; Selinger and Nelson, 1989; Selinger, 1991). To quantify the interplay between nematic and hexatic order, here we focus on the function $C_{26}(r)$ given in Equation 9, reflecting the amount of cross-correlation in their fluctuations. Here, $ψ_{2}=e^{2iϑ}$ and $ψ_{6}=e^{6i\phi}$, while the fluctuating fields $ϑ$ and $\phi$ represent again the local nematic and hexatic orientations, respectively. Averaging $ψ_{2}$ and $ψ_{6}$ over the scale of a volume element, yields the order complex parameters $Ψ_{2}=⟨e^{2iϑ}⟩=|Ψ_{2}|e^{2i\theta}$ and $Ψ_{6}=⟨e^{6i\phi}⟩=|Ψ_{6}|e^{6iϕ}$, with $\theta$ and $ϕ$ the average orientations. To make progress, we assume that, at the scale of a volume element, both microscopic orientations $ϑ$ and $\phi$ are Gaussianly distributed about their mean values, so that, in general

$$
Ψ_{p}=⟨ψ_{p}⟩≈e^{−\frac{1}{2}var⁡[Arg⁡(ψ_{p})]+i⟨Arg⁡(ψ_{p})⟩},
$$

from which

$$
|Ψ_{p}|≈e^{−\frac{1}{2}var⁡[Arg⁡(ψ_{p})]},Arg⁡(Ψ_{p})=⟨Arg⁡(ψ_{p})⟩.
$$

This approximation holds when the relative fluctuation of the p-atic phase $Arg⁡(ψ_{p})$ is sufficiently small, so that

$$
|Ψ_{p}|≈1−\frac{1}{2}⟨[Arg⁡(ψ_{p})−Arg⁡(Ψ_{p})]^{2}⟩≈⟨cos⁡[Arg⁡(ψ_{p})−Arg⁡(Ψ_{p})]⟩,
$$

consistent with the standard definition of p-atic order parameter. Thus, in particular, $\theta=⟨ϑ⟩$ and $|Ψ_{2}|=⟨cos⁡2(ϑ−\theta)⟩$, whereas $ϕ=⟨\phi⟩$ and $|Ψ_{6}|=⟨cos⁡6(\phi−ϕ)⟩$. This allows to write $C_{26}(r)$, as given by Equation (9), in the form

$$
C_{26}(r)=\frac{Ψ_{2}(r)Ψ_{6}^{∗}(0)+Ψ_{2}^{∗}(r)Ψ_{6}(0)}{2}e^{12[⟨ϑ(r)\phi(0)⟩−⟨ϑ(r)⟩⟨\phi(0)⟩]}.
$$

At equilibrium, both nematic and hexatic order can be approximated as uniform, so that

$$
\frac{Ψ_{2}(r)Ψ_{6}^{∗}(0)+Ψ_{2}^{∗}(r)Ψ_{6}(0)}{2}=|Ψ_{2}||Ψ_{6}|cos⁡(2\theta−6ϕ)≈const,
$$

and the problem reduces to calculating the connected correlation function

$$
C_{ϑ\phi}(r)=⟨ϑ(r)\phi(0)⟩−⟨ϑ(r)⟩⟨\phi(0)⟩.
$$

Notice that Equation (51) is not strictly valid for a quasi long-ranged ordered liquid crystal, where also $\theta$ and $ϕ$ are expected to vary in space. These spatial variations, however, occur on length scales comparable with the system size and, as long as this is much larger than any of the intrinsic length scales entailed in Equation 2a, are negligible for the purpose of this calculation. To compute $C_{ϑ\phi}(r)$, one can take the passive limit of Equation 2c and linearize the resulting equations about the lowest free energy configuration. This, in turn, is determined by the sign of the constant $χ_{2,6}$ in Equation 6b. For $χ_{2,6}<0$, the hexatic and nematic directors are energetically favored to be parallel, so that $ϑ≈\phi$. Conversely, when $χ_{2,6}>0$, the hexatic and nematic directors are preferentially tilted by $\pi/6$, hence $ϑ=\phi\pm\pi/6$. For presentational clarity, here we focus on the former case and, at the end of this section, we show how the same behavior holds for positive $χ_{2,6}$ values. Thus, assuming $χ_{2,6}<0$ and expanding Equation 2c about $ϑ≈\phi$, gives

$$
∂_{t}ϑ=D_{2}∇^{2}ϑ−\frac{9}{4}|χ_{2}|(ϑ−\phi)+ξ^{(ϑ)},
$$



$$
∂_{t}\phi=D_{6}∇^{2}\phi−\frac{1}{4}|χ_{6}|(\phi−ϑ)+ξ^{(\phi)}
$$

where, as in the previous sections, we have set $D_{p}=Γ_{p}L_{p}$ and $χ_{p}=Γ_{p}χ_{2,6}$ and introduced the Gaussian noise fields $ξ^{(ϑ)}$ and $ξ^{(ϑ)}$, having vanishing mean and finite variance. Unlike the active case, however, at equilibrium the latter is related to the environmental temperature by the fluctuation–dissipation theorem. This implies

$$
⟨ξ^{(\alpha)}(r,t)ξ^{(\beta)}(r^{′},t^{′})⟩=2k_{B}T(\frac{\delta_{\alphaϑ}\delta_{\betaϑ}}{\gamma_{2}}+\frac{\delta_{\alpha\phi}\delta_{\beta\phi}}{\gamma_{6}})\delta(r−r^{′})\delta(t−t^{′}),
$$

where $\gamma_{p}=K_{p}/D_{p}$, with $K_{p}$ the orientational stiffness defined in Equation 15, is the rotational viscosity of the associated p-atic phase. Equation 53a can now be decoupled and used to compute the correlation function $C_{ϑ\phi}(r)$. For simplicity, here we set $D_{2}=D_{6}=D$, $\gamma_{2}=\gamma_{6}=\gamma$, and $9χ_{2}=χ_{6}=2χ$. With this choice, taking

$$
\phi_{+}=\frac{1}{2}(\phi+ϑ),
$$



$$
\phi_{−}=\frac{1}{2}(\phi−ϑ),
$$

gives, after simple algebraic manipulations

$$
∂_{t}\phi_{+}=D∇^{2}\phi_{+}+ξ_{+},
$$



$$
∂_{t}\phi_{−}=D∇^{2}\phi_{−}−|χ|\phi_{−}+ξ_{−},
$$

where $ξ_{+}=(ξ^{(\phi)}+ξ^{(ϑ)})/2$ and $ξ_{−}=(ξ^{(\phi)}−ξ^{(ϑ)})/2$. Moreover, using Equation (54), one finds

$$
⟨ξ_{n}(r,t)ξ_{m}(r^{′},t^{′})⟩=\frac{2k_{B}T}{\gamma}\delta_{nm}\delta(r−r^{′})\delta(t−t^{′}),
$$

where ${n,m}={+,−}$. Equation 56a can now be solved in Fourier space and real time to give

$$
\phi^_{n}(q,t)=e^{S_{n}(q,t)}[\phi^_{n}(q,0)+\int_{0}^{t}dt^{′}e^{−S_{n}(q,t^{′})}ξ^_{n}(q,t^{′})],
$$

where the hat indicates Fourier transformation and

$$
S_{n}(q,t)=−Dt(|q|^{2}+m_{n}^{2}),
$$

where $m_{+}=0$ and $m_{−}^{2}=ℓ_{χ}^{−2}=D/|χ|$. The calculation of the cross-correlation function $C_{ϑ\phi}(r)$ is now reduced to calculating the autocorrelation functions of the fields $\phi_{+}$ and $\phi_{−}$. Specifically

$$
C_{ϑ\phi}(r)=C_{++}(r)−C_{−−}(r),
$$

where

$$
C_{nm}(r)=⟨\phi_{n}(r)\phi_{m}(0)⟩−⟨\phi_{n}(r)⟩⟨\phi_{m}(0)⟩,
$$

and we have made use of Equation (54) to demonstrate that $C_{+−}(r)=C_{−+}(r)=0$. The non-vanishing correlation functions, on the other hand, can be expressed as

$$
C_{nn}(r)=limt→∞\int_{0<|q|<Λ}\frac{d^{2}q}{(2\pi)^{2}}e^{iq⋅r}⟨|\phi^_{n}(q,t)|^{2}⟩,
$$

where $Λ=2\pi/a$ is a short-distance cut-off and $⟨|\phi^_{n}(q,t)|^{2}⟩$ is the finite-time orientational structure factor defined from the relation

$$
⟨\phi^_{n}(q,t)\phi^_{n}(q,t^{′})⟩=(2\pi)^{2}⟨|\phi^_{n}(q,t)|^{2}\delta(q+q^{′})\delta(t−t^{′}).
$$

After standard algebraic manipulations one finds

$$
⟨|\phi^_{n}(q)|^{2}⟩=limt→∞⟨|\phi^_{n}(q,t)|^{2}⟩=\frac{k_{B}T}{K}\frac{1}{|q|^{2}+m_{n}^{2}}.
$$

from which Equation (62) can be calculated in the form

$$
C_{nn}(r)=\frac{k_{B}T}{K}\int_{0<|q|<Λ}\frac{d^{2}q}{(2\pi)^{2}}\frac{e^{iq⋅r}}{|q|^{2}+m_{n}^{2}}.
$$

Evidently, Equation (65) is equivalent to that obtained in a purely static setting from the Hamiltonian

$$
H=\frac{1}{2}\intd^{2}r[K|∇\phi_{+}|^{2}+K|∇\phi_{−}|^{2}+m_{−}^{2}\phi_{−}^{2}],
$$

of the non-interacting scalar fields $\phi_{+}$ and $\phi_{−}$. Now, in the case of the ‘massive’ field $\phi_{−}$, the Fourier integral in Equation (65) converges to

$$
C_{−−}(r)=\frac{k_{B}T}{2\piK}K_{0}(\frac{|r|}{ℓ_{χ}}),
$$

in the range $|r|≫a$. Here, $K_{0}$ is a modified Bessel function of the second kind, whose asymptotic expansion at short and long distances is given by

$$
K_{0}(z)≈{−\gamma_{EM}−log⁡\frac{z}{2}0<z≪1,\sqrt{\frac{\pi}{2z}}e^{−z}z≫1,
$$

with $\gamma_{EM}$ the Euler–Mascheroni constant. In the case of the ‘massless‘ field $\phi_{+}$, on the other hand, the Fourier integral diverges in the infrared, but the correlation function $C_{++}(r)$ can still be computed as the Laplacian Green function on an infinite domain punctured by a hole of radius $a$ at the origin. Thus

$$
C_{++}(r)=−\frac{k_{B}T}{2\piK}log⁡\frac{|r|}{a}.
$$

Combining this with Equations (67) and (69) yields the following expression for the correlation function

$$
C_{ϑ\phi}(r)=−\frac{k_{B}T}{2\piK}[log⁡\frac{|r|}{a}+K_{0}(\frac{|r|}{ℓ_{χ}})],
$$

where $|r|≫a$. Finally, using Equation (50) and the asymptotic expansions of Equation (68) gives the following expression for the cross-correlation function

$$
C_{26}(r)∼{const.|r|≪ℓ_{χ}(\frac{|r|}{a})^{−η_{26}}|r|≫ℓ_{χ},
$$

where $η_{26}$ is an instance of the generic non-universal exponent

$$
η_{pp^{′}}=\frac{pp^{′}k_{B}T}{2\piK},
$$

in the specific case $p=2$ and $p^{′}=6$. Lastly, when $χ_{2,6}>0$, the same procedure can be carried out by expanding Equation (2c) about $ϑ=\phi\pm\pi/6$ and taking $\phi_{+}=(\phi+ϑ)/2$ and $\phi_{−}=(\phi−ϑ\pm\pi/6)/2$, from which one finds again Equation 72.
