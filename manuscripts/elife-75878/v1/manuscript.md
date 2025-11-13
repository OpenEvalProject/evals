# Active morphogenesis of patterned epithelial shells

## Authors

- Diana Khoromskaia<sup>1</sup> ([ORCID: 0000-0003-2597-6336](https://orcid.org/0000-0003-2597-6336))
- Guillaume Salbreux<sup>1</sup> ([ORCID: 0000-0001-7041-1292](https://orcid.org/0000-0001-7041-1292)) †

### Affiliations

1. The Francis Crick Institute London United Kingdom ([ROR:04tnbqb63](https://ror.org/04tnbqb63))
2. University of Geneva Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))

† Corresponding author

## Abstract

Shape transformations of epithelial tissues in three dimensions, which are crucial for embryonic development or in vitro organoid growth, can result from active forces generated within the cytoskeleton of the epithelial cells. How the interplay of local differential tensions with tissue geometry and with external forces results in tissue-scale morphogenesis remains an open question. Here, we describe epithelial sheets as active viscoelastic surfaces and study their deformation under patterned internal tensions and bending moments. In addition to isotropic effects, we take into account nematic alignment in the plane of the tissue, which gives rise to shape-dependent, anisotropic active tensions and bending moments. We present phase diagrams of the mechanical equilibrium shapes of pre-patterned closed shells and explore their dynamical deformations. Our results show that a combination of nematic alignment and gradients in internal tensions and bending moments is sufficient to reproduce basic building blocks of epithelial morphogenesis, including fold formation, budding, neck formation, flattening, and tubulation.

## Introduction

Morphogenesis of embryos and the establishment of body shape rely on the three-dimensional deformation of epithelial sheets which undergo repeated events of expansion, contraction, convergence-extension, invagination, evagination, tubulation, and branching (Gilbert and Barresi, 2020). Tissue folding, for instance, is involved at different steps of embryogenesis (Kominami and Takata, 2004; Sui et al., 2018), organ (Sumigray et al., 2018), or entire organism development (Livshits et al., 2017; Braun and Keren, 2018). Recently, the growth of in vitro organoids, organ-like structures derived from stem cells capable of self-renewal and self-organisation, has revealed the intrinsic ability of biological systems to self-organise into complex structures from simple building blocks (Huch et al., 2017; Kamm et al., 2018; Rossi et al., 2018). Early steps in organoid self-organisation often start through the formation of a hollow, fluid-filled unpatterned sphere, undergoing spontaneous symmetry breaking (Ishihara and Tanaka, 2018) for example, in neural tube (Meinhardt et al., 2014) or intestinal (Serra et al., 2019; Yang et al., 2021) organoids. How this repertoire of shape changes and complex organisation emerges physically is a fundamental question.

Continuum theories of active materials, treating the epithelium as an active liquid crystal, have proven highly successful to achieve an understanding of the mechanics and flows of cellular collective motion. Epithelia cultured in vitro exhibit patterns of orientational order and spontaneous flows which are consistent with predictions from hydrodynamic theories of active matter (Duclos et al., 2017; Duclos et al., 2018; Blanch-Mercader et al., 2021a). Constitutive equations involving a shear decomposition of tissue area and anisotropic elongation into cell shape changes, cell division, and cellular topological transitions can reproduce basic features of the developing Drosophila pupal wing (Etournay et al., 2015; Popović et al., 2017). Recently, several studies established a link between topological defects in tissue order, provided by cell elongation or internal anisotropic cellular structure, and morphogenetic events (Kawaguchi et al., 2017; Saw et al., 2017; Mueller et al., 2019; Maroudas-Sacks et al., 2021).

Here, we propose a description of three-dimensional deformations of a patterned epithelial spheroid, considered as a shell of active liquid crystal. We consider an active elastic shell theory which takes into account in-plane tensions and internal bending moments (Lomholt, 2006; Maitra et al., 2014; Sahu et al., 2017; Salbreux and Jülicher, 2017). Internal bending moments arise from an inhomogeneous distribution of stress across the tissue. Such inhomogeneities can arise from, for example, changes in cytoskeletal organisation along the epithelium apico-basal axis, or from apposed epithelial tissues with different mechanical properties (Braun and Keren, 2018; Maroudas-Sacks et al., 2021). Apico-basal gradients of contractility, for instance, play a key role in morphogenetic processes (Martin and Goldstein, 2014; Sui et al., 2018) and are effectively taken into account here by active bending moments.

We consider an initially spherically symmetric tissue subjected to spatially modulated internal forces. Our rationale is to consider a situation where chemical and mechanical processes are uncoupled, such that cell–cell communication mechanisms ensure symmetry-breaking of the sphere, which is then converted into a pattern of mechanical forces (Ishihara and Tanaka, 2018). We consider a particularly simple pattern where the spherical tissue is decomposed into two regions, subjected to different active forces, and explore shape changes that result from this pattern (Figure 1a). We compare the situation where internal tensions and bending moments are isotropic to a situation where a nematic field, provided by cellular anisotropic structures, orients the internal tensions and bending moments.

![Figure 1.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig1-v1.jpg)

**Figure 1.:** (a) Schematic of an epithelial tissue with a cellular state pattern. (b) Parametrisation of the axially symmetric shell and its deformation with the flow $v$, and components of the tension and torque tensors. We note that $m^{ϕ⁢s}=m¯^{ϕ⁢ϕ}⁢x$ and $m^{s⁢ϕ}=-m¯^{s⁢s}/x$. (c) Stresses integrated across the thickness of the sheet result in tensions $t_{i⁢j}$ and bending moments $m_{i⁢j}$ acting on the midsurface. Anisotropic and possibly different tensions (dark-blue arrow crosses) on the apical and basal sides of the epithelium result in anisotropies in $t_{i⁢j}$ and $m¯_{i⁢j}$, which can be captured by a nematic order parameter $Q_{i⁢j}$ (e.g. blue rods on the top surface).

## Model

### Viscoelastic nematic active surface model for epithelial mechanics

We first discuss our mechanical description of the deforming tissue. We represent an epithelium as an active surface flowing with velocity $v$ (Salbreux and Jülicher, 2017). The surface is taken to be elastic with respect to area changes, and fluid with respect to pure shear in the plane of the surface. Indeed, cellular rearrangements can fluidify in-plane epithelial flows by allowing cell elongation and cellular elastic stresses to relax on long time scales (Popović et al., 2017). Here, we consider such long enough time scales of hours to days which are relevant to organoid and developmental morphogenesis (Gilbert and Barresi, 2020). We also assume here that cell division and apoptosis or delamination are not occurring, such that elastic isotropic stresses do not relax (Ranft et al., 2010). Implicitly, we assume that cells have a preferred cell area.

Epithelia typically have a non-negligible thickness compared to characteristic transverse dimensions, and the apical and basal surfaces have different structures and are regulated differently. Notably, the basal surface is in contact with the basal lamina, a layer of extracellular matrix (Khalilgharibi and Mao, 2021). Therefore, a purely two-dimensional representation of epithelial stresses would miss essential aspects of their mechanics. We therefore introduce here the tension tensor $t^{i⁢j}$, but also the bending moment tensor $m^{i⁢j}$ which captures internal torques arising from differential stresses acting along the surface cross section (Figure 1b and c). We assume that the surface possesses a bending rigidity, captured by a bending modulus $κ$. When the curvature deviates from a flat layer, a bending moment results from the surface curvature (Equation 6). In addition, active bending moments can arise in the surface (Salbreux and Jülicher, 2017), for instance, due to actomyosin-generated differential active stresses along the apicobasal axis (Messal et al., 2019; Fouchard et al., 2020).

Cellular force generating elements are not necessarily isotropic; for instance, because cytoskeletal structures exhibit a preferred orientation (Martin, 2020) or inhomogeneous distribution across cellular interfaces (Bertet et al., 2004), or because the epithelial cells themselves exhibit an elongation axis (Duclos et al., 2017). Therefore, we introduce a coarse-grained surface nematic order parameter $Q$ which quantifies the average level of orientational order in the tissue. We assume that the nematic order parameter is tangent to the active surface.

#### Force balance

On a curved surface we define the rotated bending moment tensor $m¯^{i⁢j}=-m^{i⁢k}ϵ_{k}^{j}$, which we adopt for convenience. The local force balance projected on the tangential and normal directions reads (Salbreux and Jülicher, 2017)

$$
∇_{i}t^{ij}+C_{i}^{j}t_{n}^{i}=−f^{ext,j}
$$



$$
∇_{i}t_{n}^{i}−C_{ij}t^{ij}=−f_{n}^{ext}−P,
$$

where notations of differential geometry are introduced in Appendix 1; briefly $C_{i⁢j}$ is the curvature tensor, $g_{i⁢j}$ denotes the metric tensor, and $ϵ_{i⁢j}$ the antisymmetric Levi-Civita tensor, $n$ the vector normal to the surface, $t^{i⁢j}$ is the tangential contribution of the tension tensor and $t_{n}^{i}$ its normal contribution, and $\nabla_{i}$ denotes the covariant derivative on the surface. The tangential and normal torque balance provide the transverse tension and antisymmetric part of the tangent tension tensor:

$$
t_{n}^{i}=∇_{k}m¯^{ki},
$$



$$
ϵ_{ij}t^{ij}=C_{ij}m^{ij}.
$$

We assume an external force density $f^{ext}=f_{n}^{ext}n+f^{ext,j}e_{j}$ acting on the surface in addition to a difference of hydrostatic (uniform) pressure $P=P_{i⁢n}-P_{o⁢u⁢t}$, but no external torques (Figure 1). Here, we consider situations at low Reynolds number, where inertial forces may be neglected, and where additional external forces are negligible, such that the surface as a whole is force-free, $∮_{S}dSf^{ext}=0$. Dissipative couplings to the external fluid are ignored here as the characteristic viscosity of a biological tissue ($∼10^{5}$ Pa s; Marmottant et al., 2009; Guevorkian et al., 2010) is several orders of magnitude larger than that of water ($10^{-3}$ Pa s).

#### Constitutive equations

In line with our hypothesis describing the material properties of an epithelium, we use the following constitutive equations:

$$
t_{s}^{ij}=(2Ku+ζ+(η_{b}−η)v_{k}^{k})g^{ij}+2ηv^{ij}+ζ_{n}Q^{ij},
$$



$$
m¯^{ij}=(2κC_{k}^{k}+ζ_{c}+η_{cb}\frac{D}{Dt}C_{k}^{k})g^{ij}+ζ_{cn}Q^{ij}.
$$

where $t_{s}^{i⁢j}$ is the symmetric part of the tension tensor and, on a curved surface, the strain rate tensor $v^{i⁢j}$ and the corotational time derivative of the curvature tensor $\frac{D}{Dt}⁢C^{i⁢j}$ are given by (Salbreux and Jülicher, 2017)

$$
v^{ij}=\frac{1}{2}(∇^{i}v^{j}+∇^{j}v^{i})+C^{ij}v_{n},
$$



$$
\frac{D}{Dt}C^{ij}=−∇^{i}(∂^{j}v_{n})−v_{n}C^{i}_{k}C^{kj}+v_{k}∇^{k}C^{ij}+\omega_{n}(ϵ^{ik}C_{k}^{j}+ϵ^{jk}C_{k}^{i}),
$$

with $\omega_{n}=\frac{1}{2}⁢ϵ^{i⁢j}⁢\nabla_{i}⁡v_{j}$ the normal component of the vorticity. $u$ is the area strain, measuring local changes of area relative to a reference value; a precise definition is introduced in Equation 14. $Q^{i⁢j}$ is a traceless, symmetric tensor characterising nematic orientational order on the surface.

We now discuss these constitutive equations. The surface elastic response is determined by the area elastic modulus $K$ and the bending modulus $κ$. The dynamical deformations of the surface are characterised by the two-dimensional shear and bulk viscosities $η$ and $η_{b}$ and the bulk bending viscosity $η_{c⁢b}$. While the shear and bulk viscosities penalise in-plane isotropic and anisotropic deformation rates, the bending viscosity penalises the rate of change of total surface curvature $C_{k}^{k}$. The bending viscosity dampens normal deformations and prevents bending modes, which would otherwise have no dissipative cost and could result in numerical instabilities.

The remaining contributions to Equations 5; 6 proportional to $ζ$, $ζ_{n}$, $ζ_{c}$, $ζ_{c⁢n}$ correspond to active tensions and bending moments. $ζ$ is an isotropic active surface tension, $ζ_{n}$ is the in-plane nematic active stress, with $ζ_{n}>0$ usually referred to as the ‘contractile’ active stress and $ζ_{n}<0$ as the ‘extensile’ active stress (Marchetti et al., 2013). $ζ_{c}$ is the isotropic bending moment, which locally favours a spontaneous curvature $C_{k}^{k}=−ζ_{c}/(2κ)$. If the active surface corresponds simply to two parallel layers under surface tension $\gamma_{a}$, $\gamma_{b}$ (such as an epithelium with apical surface tension $\gamma_{a}$ and basal surface tension $\gamma_{b}$), and separated by a distance $h$, an active isotropic bending moment $ζ_{c}∼h⁢(\gamma_{a}-\gamma_{b})/2$ emerges in the surface to lowest order in the curvature tensor. The term in $ζ_{c⁢n}$ corresponds to an anisotropic active bending moment. In the bilayer picture, where the active surface corresponds to two layers $a$ and $b$, it could generally arise from differences between the two layers in the level of order $Q_{ij}^{a}$ and $Q_{ij}^{b}$ or in the level of nematic active stress $ζ_{n}^{a}$ and $ζ_{n}^{b}$. For example, such differences could stem from two contractile (respectively extensile) layers with perpendicular nematic orientations $+Q_{i⁢j}$ and $-Q_{i⁢j}$ (Figure 1c), or from two layers with parallel nematic order, but one subjected to contractile active stresses and the other to extensile active stresses.

In the absence of external forces, deformations of the epithelial shell are driven by distributions of active tensions and bending moments, which are prescribed on it through the isotropic profiles $ζ⁢(s)$ and $ζ_{c}⁢(s)$, the anisotropic components proportional to $ζ_{n}⁢(s)$ and $ζ_{c⁢n}⁢(s)$, and the shape-dependent nematic order parameter.

We note that Equations 5 and 6 can be seen as generic constitutive equations for a nematic active surface with broken up-down symmetry but no broken chiral or planar-chiral symmetry, arising from an expansion in the curvature tensor and in the nematic order parameter $Q_{i⁢j}$ of the tensor $t_{s}^{i⁢j}$ and $m¯_{i⁢j}$ (Salbreux and Jülicher, 2017; Salbreux et al., 2022). For simplicity some allowed additional couplings entering the generic constitutive equations have not been taken into account here, notably active contributions to the tension tensor (Equation 5) and bending moment tensor (Equation 6) proportional to the curvature tensor $C_{i⁢j}$. Salbreux et al., 2022 provide a more general list of possible couplings for active fluid nematic surfaces.

#### Nematic order parameter

For simplicity here we assume that the nematic order parameter minimises an effective free energy, thus ignoring potential active effects on the ordering (Salbreux et al., 2022). We consider the following effective free energy of the nematic on a curved surface (De Gennes and Prost, 1995; Jiang et al., 2007; Kralj et al., 2011; Pearce et al., 2019):

$$
F=\intdS(\frac{k}{2}(∇_{i}Q^{jk})(∇^{i}Q_{jk})−\frac{a}{4}Q_{ij}Q^{ij}+\frac{a}{16}(Q_{ij}Q^{ij})^{2}),
$$

with the Frank elastic constant $k$, which is assumed to be equal for all distortions. The Landau–de Gennes contribution is chosen such that for $k=0$ the aligned state with $Q_{ij}Q^{ij}=2$ is a minimiser for $a>0$. Additional coupling terms between the nematic and curvature tensor are not considered here for simplicity (Napoli and Vergori, 2012).

### Deformations of a polarised active sphere

We now turn to describe axisymmetric deformations of a closed nematic active surface.

#### Geometric setup

The epithelium is represented by a thin spherical shell undergoing axisymmetric deformations (Figure 1b). Its two-dimensional midsurface $X⁢(ϕ,s)\inℝ^{3}$ is parametrised by the arc length coordinate $s\in[0,L]$ and the angle of rotation $ϕ\in[0,2⁢\pi]$ as

$$
X(ϕ,s)=(x(s)cos⁡ϕ,x(s)sin⁡ϕ,z(s)).
$$

The local tangent basis is given by ${e_{ϕ},e_{s}}$, and $n$ is the outward-pointing surface normal. The geometry of axisymmetric surfaces is described further in Appendix 1. We require that the metric component $g_{s⁢s}=1$, which implies relations between the tangent angle $ψ⁢(s)\in[0,\pi]$ and the shape functions $x⁢(s)$ and $z⁢(s)$

$$
∂_{s}x=cos⁡ψ,
$$



$$
∂_{s}z=sin⁡ψ,
$$

which, together with the meridional principal curvature

$$
C_{s}^{s}=∂_{s}ψ,
$$

are sufficient to reconstruct the surface shape from the curvature $C_{s}^{s}$. In this axisymmetric setup, the velocity field reads $v=v^{s}e_{s}+v_{n}n$, with $v^{s}$ the tangential and $v_{n}$ the normal velocities.

The undeformed initial surface is a sphere $S_{0}$ with radius $R_{0}$, and all quantities defined on it are denoted with a subscript ‘0’. We define the area strain on a point of the surface as

$$
u=\frac{dS−dS_{0}}{dS_{0}},
$$

where $dS$ is the surface area element at the point considered on the surface, and $dS_{0}$ is the surface area element of the same material point on the sphere. With this definition, $u=0$ on the initial sphere. We denote $s_{0}⁢(s)$ the arc length position on the undeformed sphere $S_{0}$ of a material point at arc length position $s$ on the deformed sphere. One then has $u=f_{ϕ}⁢f_{s}-1$ with $f_{s}=\frac{d⁢s}{d⁢s_{0}}$ the meridional stretch and $f_{ϕ}=\frac{x}{x_{0}}$ the circumferential stretch. Integrating $f_{s}^{−1}=f_{ϕ}/(u+1)$ yields the arc length reparametrisation $s_{0}⁢(s)$ between the initial and the deformed surface. The Lagrangian time derivative of the area strain (Equation 14) is related to the flow through

$$
\frac{D}{Dt}u=(1+u)v_{k}^{k}.
$$

#### Nematic order

Here, with axial symmetry, the nematic tensor $Q_{i⁢j}$ has the non-zero component $q=Q_{ϕ}^{ϕ}=-Q_{s}^{s}$. On the closed shell, the nematic director (Appendix 3), which represents the alignment, will have two +1 topological defects at the poles (Figure 3a) as a consequence of the Poincaré–Hopf theorem (Hopf, 1927). The order parameter $q$ vanishes there, creating defect cores of size $l_{c}=\sqrt{k/a}$, which is the characteristic nematic length. In this geometry the Euler–Lagrange equation resulting from the free energy (Equation 9) is

$$
∂_{s}^{2}q=\frac{1}{2l_{c}^{2}}q(q^{2}−1)+\frac{cos⁡ψ}{x}(4\frac{cos⁡ψ}{x}q−∂_{s}q).
$$

An example solution of Equation 16 on the sphere is shown in Figure 3b. From the two possible states with $q=\pm1$ in the bulk, respectively, we choose $q=1$ for reference. This corresponds to circumferential alignment of the nematic order (Figure 3a, right). The sign of the tensions and bending moments is then only controlled by the $ζ$-prefactors. For example, a nematic tension with $ζ_{n}>0$ corresponds to circumferential active contraction, resulting in an elongated shape. For nematic bending moments, if one chooses $Q_{i⁢j}$ to represent the order parameter on the outer side of the shell, the sign convention is such that $ζ_{cn}>0$, $q>0$ results in circumferential contraction on the outer side and contraction along the meridians on the inner side of the shell. We note that the shape is only influenced by the order parameter via the active tension $ζ_{n}⁢Q^{i⁢j}$ and the active moment $ζ_{c⁢n}⁢Q^{i⁢j}$, but is otherwise insensitive to the nematic elastic energy (Equation 9). Minimisation of the Frank free energy by deformations of passive nematic surfaces has been previously discussed (Jiang et al., 2007).

#### Active profiles

We consider initially spherical epithelial shells containing an active region that drives the deformation. For the steady-state analysis, this region is a circular patch of size $l_{a}\leqL_{0}$ (Figure 1b), such that the active terms are given on $S_{0}$ by step-like profiles, for example

$$
ζ_{c}(s_{0})={ζ_{c}^{0}+\deltaζ_{c},if s_{0}\in[0,l_{a}]ζ_{c}^{0},otherwise
$$

and similarly for $ζ⁢(s_{0})$, $ζ_{n}⁢(s_{0})$, and $ζ_{c⁢n}⁢(s_{0})$. The circular patch deforms with the material points, which reflects that the active properties are associated with a predefined group of cells. If not stated otherwise, the values outside the active region are $ζ^{0}=ζ_{c}^{0}=ζ_{n}^{0}=ζ_{c⁢n}^{0}=0$. This passive part of the surface is governed by the constitutive equations 5 and 6, but with vanishing active terms.

In dynamical simulations, active tension and bending moment profiles are defined on the spherical surface at time $t=0$ using sigmoid functions $f⁢(x,\mu,\sigma)$ of the form

$$
f(x,\mu,\sigma)=1−(1+e^{−\frac{x−\mu}{\sigma}})^{−1},
$$

for their space and time dependence. For instance, the active bending moment profile is defined on $S_{0}$ as

$$
ζ_{c}(s_{0},t=0)=(1−f(t=0,\mu_{t},\sigma_{t}))(ζ_{c}^{0}+\deltaζ_{c}f(s_{0},l_{a},\sigma_{s}))
$$

as a smooth version of the step-profile Equation 17, and $ζ$, $ζ_{n}$, and $ζ_{c⁢n}$ are defined analogously. The profile is then advected with the material points (Figure 1b), while its intensity increases through the time-dependent sigmoid (e.g. Figure 2d).

![Figure 2.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig2-v1.jpg)

**Figure 2.:** (a, e) Shape diagram. (b, f) Details of shape diagram illustrating different behaviours of solution branches. The ideal neck line (green) represents the bending moment difference required to create budded shapes consisting of two spheres with $u=0$, as given by Equation 24. (c) Examples of solution branches in the $(\delta⁢ζ_{c},V)$-plane corresponding to four different regions in (b). (g) Examples of solution branches in the $(\delta⁢ζ_{c},P)$-plane chosen from three different regions in (e). (d, h) Dynamic simulations of shape changes, for parameter values indicated in the shape diagrams (a, e). (i) Neck radius and curvatures at the neck as functions of $\delta⁢ζ_{c}$ for the example $l_{a}/L_{0}=0.04$ in (g). Other parameters: $K~=10^{3},η~_{c⁢b}=10^{-2}$, $η~_{V}=10^{-4}$.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Details of the steady-state solutions with nearly closed necks formed by isotropic bending moments for free volume (a) and conserved volume (b), and $l_{a}/L_{0}=0.9$.The location of the neck, taken as the point where $C_{ϕ}^{ϕ}$ is maximal, is marked by a grey line in the plots. (a) The shape is characterised by $t_{s}^{s}=t_{n}^{s}=u=0$ and constant.$m¯_{s}^{s}$. (b) Here, $t_{s}^{s}$ changes sign and $m¯_{s}^{s}$ is continuous across the neck.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Maximal relative surface area of the steady-state shapes measured along a solution branch for each $l_{a}/L_{0}$ in the case of conserved volume, corresponding to shapes shown in Figure 2e–g.

#### Volume

We consider two possibilities for the volume enclosed by the epithelium. In one limit the tissue is assumed to be impermeable and the enclosed volume is treated as an incompressible fluid exerting hydrostatic pressure on the tissue. The volume is conserved when the shell deforms:

$$
V=V_{0},
$$

with the pressure $P$ acting as the Lagrange multiplier.

In the other limit the tissue is fully permeable. At steady state, in this limit the volume can change freely and no pressure acts on the tissue, $P=0$. In dynamical simulations, we introduce a volume viscosity $η_{V}$ such that the pressure is coupled to the volume change via

$$
P=−η_{V}∂_{t}V
$$

where $η_{V}$ is a parameter chosen to be small enough that the internal pressure is small compared to other forces.

#### Stationary shapes

For given profiles of active tensions and bending moments, steady-state shapes are obtained as solutions of the mechanical equilibrium equations. Those are a system of non-linear ode’s containing the force and torque balances Equations 1–4, the geometric Equations 11–13, the constitutive relations Equations 5–8 and Equation 14 with vanishing velocities $v^{s}=v_{n}=0$, and, if applicable, the nematic equilibrium Equation 16.

#### Dynamical deformations

In the dynamical version of the model a given active profile generates a velocity $v(ϕ,s,t)$, whose normal part deforms the surface (Figure 1b). The components ${v^{s},v_{n}}$ of this instantaneous velocity are obtained by solving the force and torque balance Equations 1–4 (derived for the axisymmetric surface in Equations 63–65), together with the constitutive Equations 5–8, on the shape $X⁢(ϕ,s,t)$. Since $u⁢(s,t)$ and $Q_{i⁢j}⁢(s,t)$ are also given, these constitute a linear system of ode’s. The shape is evolved in time in a Lagrangian approach, in which material points move according to the full-velocity vector $v$,

$$
∂_{t}X=v.
$$

Surface quantities, such as the active profiles and the area strain, are advected accordingly. The nematic order parameter evolves in time quasi-statically, where we assume that it relaxes instantaneously to the solution of Equation 16 written on the deformed surface at time $t$.

#### Dimensionless variables

The equations are made dimensionless (marked by tilde) by rescaling tensions by $κ/R_{0}^{2}$, bending moment densities by $κ/R_{0}$, lengths by $R_{0}$, force densities by $κ/R_{0}^{3}$, viscosities by the two-dimensional shear viscosity $η$ of the epithelium, times by the characteristic time scale $\tau_{a}=η⁢R_{0}^{2}/κ$ , and velocities by $R_{0}/\tau_{a}$. This leaves the dimensionless parameters $K~=K⁢R_{0}^{2}/κ$, $l~_{c}=l_{c}/R_{0}$, $η~_{b}=η_{b}/η$, $η~_{c⁢b}=η_{c⁢b}⁢R_{0}^{2}/η$ and $η~_{V}=η_{V}⁢R_{0}^{4}/η$ to be fixed. We choose to set $η~=η~_{b}=1$, $η~_{V}=10^{-4}$ for fast relaxation of the volume, and the nematic length scale is set to $l~_{c}=0.1$. Working under the assumptions of linear shell theory for a homogeneous thin shell (Reddy, 2006), one can relate the elastic moduli to each other via the thickness $h$ of the cell layer, and express $K~=12⁢(R_{0}/h)^{2}$. In simulations we use $K~=1000$, corresponding to $h/R_{0}≈0.1$, which covers a range of systems from gastrulating embryos (e.g. sea urchin Davidson et al., 1995) to organoids (Serra et al., 2019). Similarly, for the bulk bending viscosity we have $η~_{c⁢b}∼(h/R_{0})^{2}=10^{-2}$.

### Numerical methods

For both the steady-state computation and the dynamics, the resulting sets of ode’s are integrated numerically with the boundary-value-problem solver bvp4c of MATLAB, which implements a fourth-order collocation method on an adaptive spatial grid (Kierzenka and Shampine, 2001). The equations are solved on the full interval $[0,L]$, and geometrical singularities at the poles are handled using analytical limits at $s=0,L$ (Appendix 6). Any integral constraint, such as volume conservation, is rewritten as a boundary value problem and added to the system of ode’s to be solved.

The dynamics simulations start with a sphere at time $t~=0$. We study each of the four active effects separately. The corresponding active profile is switched on smoothly via a sigmoid function in time, such that it reaches its target intensity at $t~≈0.02$. The time integration according to Equation 22 is done with an explicit Euler method with adaptive step size via

$$
X^{′}(ϕ,s,t+\deltat)=X(ϕ,s,t)+\deltatv(ϕ,s,t).
$$

In order to keep the force and torque balance equations in the form given by Equations 63–65, the updated surface is reparametrised as $X^{′}⁢(ϕ,s^{′},t+\delta⁢t)$ in a new arc length $s^{′}⁢(s)$ which is calculated from the condition $g_{s^{′}⁢s^{′}}=1$. The profiles and surface quantities are passed between time steps as spline interpolants.

To produce the diagrams of steady-state shapes, $l_{a}$ is fixed and the control parameter is the difference of the active profile value between the passive and the active regions of the shell, for example, for the profile given in Equation 17 it is $\delta⁢ζ_{c}$. A solution branch is found by starting from the spherical solution at zero difference of active profile, and calculating a sequence of steady-state shapes, progressively increasing the magnitude of the difference in activity. Two different methods are used to construct the solution branch for a sequence of control parameter values. For small values, starting from zero, the solution branch is obtained by making small increments in the control parameter. For larger values we switch to an implicit stepping method, which we developed based on a parametric representation of the solution branch (see Appendix 6 section ‘Construction of solution branches’). This second method allows us to continue the solution branches into regions where the steady-state shapes become non-unique in the control parameter.

Details of the numerical methods can be found in Appendices 6 and 7 for the steady state and the dynamics simulations, respectively.

## Results

### Epithelia as active membranes: Isotropic active tensions

We first consider deformations of an epithelial shell due to patterns of isotropic active tensions and bending moments. A spatially varying isotropic tension represents a change in the preferred area of the epithelium due to either changes in sheet thickness or cell number (Popović et al., 2017). However, one can show that a step-profile of positive (contractile) tension $ζ>0$ does not lead, at steady state, to a three-dimensional deformation of the shell away from a spherical shape, which is a consequence of the absence of shear elasticity in our model (Appendix 8). Instead, the epithelium remains spherical and regions with higher tension contract. This leads to a rescaling of the relative active region size $l_{a}/L_{0}$ and, if the volume is free to change, also to a decrease in shell radius (Appendix 8). If the tension becomes negative, a buckling of the surface may occur (Salbreux and Jülicher, 2017). Here, we focus on positive tensions; therefore, if only isotropic active effects are considered, active internal bending moments are required to drive deformations away from the spherical shape.

### Epithelia as active shells: Isotropic active bending moments

We now turn to deformations induced by an increasing active bending moment in a spherical cap. In Figure 2a and e, we plot a phase diagram of steady-state shapes as a function of the increased active bending moment $\delta⁢ζ_{c}$ and the size of the active region $l_{a}$. The steady-state deformed shapes are plotted with the active region shown in red and the ‘passive’ region, where $ζ_{c}=0$, shown in blue. We can contrast the situation where fluid is free to exchange across the surface and at steady state the difference of pressure across the surface vanishes, $P=0$ (Figure 2a–d), to the case where the volume enclosed by the surface is constrained to a fixed value (Figure 2e–i).

An isotropic active bending moment (term in $ζ_{c}$ in Equation 6) induces a preferred curvature $(C^{0})_{k}^{k}=-\frac{ζ_{c}}{2⁢κ}$, such that regions of a spherical shell with $ζ_{c}>0$ can be expected to flatten or bend inwards. Specifically, a difference of $\delta⁢ζ_{c}$ applied at the boundary of the active cap induces a jump in meridional curvature $C_{s}^{s}$ and a local folding of the sheet. Due to the spherical topology, the shape of the whole shell is affected by this fold, as can be seen from the sequences of stationary shapes obtained by increasing $\delta⁢ζ_{c}$ for intermediate values of $l_{a}/L_{0}$ (Figure 2a). In particular, for the same value of $\delta⁢ζ_{c}$ the active region may bend inward or keep a positive curvature, depending on its size.

When $l_{a}/L_{0}$ is small or close to 1, the resulting shape is characterised by the formation of a bud which form either inwards ($l_{a}≪L_{0}$) or outwards $(L_{0}-l_{a}≪L_{0})$. In these cases, for sufficiently large values of $\delta⁢ζ_{c}$ the steady-state solution is lost through the formation of a constricting neck. In our simulations the constricting neck is numerically resolved up to values of $∼10^{-3}⁢R_{0}$; extrapolation indicates full constriction at a finite $\delta⁢ζ_{c}$ (Figure 2i). As the neck radius decreases the principal curvatures at the neck diverge as $C_{s}^{s},C_{ϕ}^{ϕ}→\pm∞$, such that $C_{k}^{k}$ remains finite (Figure 2i) and therefore the limiting, budded shape is a true steady-state solution. Such a transition is reminiscent of models of lipid membrane vesicles, which can be induced to form a budded shape consisting of two spheres connected by an infinitesimal region called the ideal neck (Seifert et al., 1991; Jülicher and Lipowsky, 1993; Fourcade et al., 1994; Jülicher and Lipowsky, 1996; Seifert, 1997). For lipid membranes the ideal neck condition gives the difference in spontaneous curvature between the two domains at which a vesicle will form two spheres, $1/R_{1}+1/R_{2}=C_{0}$ with $R_{1}$ and $R_{2}$ the radius of the two spheres and $C_{0}$ the spontaneous curvature (Seifert, 1997). Here the choice of constitutive Equations 5 and 6 does not correspond to the Helfrich model, and we find alternative matching conditions for the two regions connected by the infinitesimal neck: we find that $t_{s}^{s}$ changes sign across the neck, while $m¯_{s}^{s}$ is continuous. This result can be derived by a scaling analysis around the neck (Appendix 2). In the free volume case, these conditions are satisfied when the active and passive regions are separated by the neck, and have the shapes of spheres with vanishing strain ($u=0$) and radii $R_{a}$, $R_{p}$, related by the condition:

$$
\frac{1}{R_{a}}−\frac{1}{R_{p}}=−\frac{\deltaζ_{c}}{4κ},−\frac{1}{R_{a}}−\frac{1}{R_{p}}=−\frac{\deltaζ_{c}}{4κ},
$$

where the change of sign in the second line arises because the active region deforms inward and form a sphere with a negative mean curvature. The additional condition of vanishing strain $u=0$ gives an additional relation for $R_{1}$ and $R_{2}$ as a function of $l_{a}/L_{0}$. Combining these conditions determine a curve in the parameter space $\delta⁢ζ_{c}⁢R_{0}/κ$, $l_{a}/L_{0}$, which matches with the numerically determined curve of neck constriction (Figure 2b). In the fixed volume case, the matching conditions do not result in such a simple shape solution; however, using the same condition as for the free volume case appears to still provide a good approximation of the constriction point for small ($l_{a}≪L_{0}$) and close to $L_{0}$ $(L_{0}-l_{a}≪L_{0})$ values of $l_{a}$ (Figure 2f). We conclude that infinitesimal neck formation can arise outside of the Helfrich model and that the ideal neck condition which is satisfied there does not generally extend to other models of surface mechanics.

At sufficiently large increase in the active bending moment difference $\delta⁢ζ_{c}$ and for intermediate values of $l_{a}/L_{0}$, a fold in the solution branch in the $(\delta⁢ζ_{c},V)$-plane appears (Figure 2c). For most values of $l_{a}/L_{0}$, this fold is associated to the loss of a continuously attainable solution with increasing $\delta⁢ζ_{c}$, and a shape transition (Figure 2b and c). We expect shapes obtained by following the continuous branch of shapes beyond the fold to be unstable (Appendix 9). The (potentially unstable) physical branch eventually stops either through a self-intersection of the sheet at the poles (Figure 2c, $l_{a}/L_{0}=0.35$) or through the constriction of a small neck that develops near the boundary of the passive and active regions and separates the shell into two smaller, approximately spherical compartments (Figure 2c, $l_{a}/L_{0}=0.31,0.7$). Alternatively the solution branch continues in a sequence of loops and the active region elongates (Figure 2c, $l_{a}/L_{0}=0.5$), forming an increasing number of bubble-like compartments.

Since we follow continuous trajectories of steady-state shapes in parameter space, we cannot directly obtain alternative steady-state solution branches after the shape transition. Therefore, we turn to dynamic simulations where we explicitly calculate flow fields, starting from the reference spherical shape, and evolve the surface shape (Figure 2d) with parameters chosen to be away from the transition in parameter space (Figure 2a). This also allows to resolve the sequence of shapes and velocity fields leading to a given steady-state deformed shape (Figure 2h, $l_{a}/L_{0}=0.1,\delta⁢ζ_{c}=40⁢κ/R_{0}$). For parameters beyond the shape transition, we find that a small neck can form, separating roughly the active and passive regions, whose radius decreases to 0 over time (Figure 2d). Alternatively, the surface ends up self-intersecting (Figure 2d, $l_{a}/L_{0}=0.35,\delta⁢ζ_{c}=12.5⁢κ/R_{0}$). We do not find therefore alternative solution branches beyond the shape instability. Since intersection of the surface with itself is described by different physical interactions than considered here, our framework does not answer what would happen beyond the self-intersection line. However, assuming that self-intersection results in fusion and rupture of the apposed two surfaces, active isotropic bending moment difference could in principle drive a change in tissue topology, from one sphere to two ($l_{a}/L_{0}=0.85,\delta⁢ζ_{c}=15⁢κ/R_{0}$), or from a sphere to a torus via self-intersection ($l_{a}/L_{0}=0.35,\delta⁢ζ_{c}=12.5⁢κ/R_{0}$).

When volume is conserved, deformations are broadly similar but tend to be more localised to the fold at the active boundary (Figure 2e–i). For intermediate values of $l_{a}/L_{0}$, the shell deforms into locally folded shapes, which eventually self-intersect at large bending moment difference (Figure 2g, $l_{a}/L_{0}=0.3,0.7$, Figure 2h).

### Nematic active tensions

We now introduce the nematic order parameter $Q_{i⁢j}$ and consider shape changes driven by contractile or extensile active stress in the active region (Figure 3). As expected, solving for the nematic order parameter profile on the undeformed sphere results in maximal order at the equator and two defects at the poles where the nematic order parameter vanishes, $q=0$ (Figure 3). Two solutions with $q<0$ and $q>0$ can exist; in the following we take the convention that $Q_{ϕ}^{ϕ}=q>0$, $Q_{s}^{s}=−q<0$, corresponding to circumferential alignment of the order parameter, such that a contractile active stress $(ζ_{n}>0)$ results in a positive circumferential tension, $t_{ϕ}^{ϕ}>0$. Due to invariance of the constitutive equation by exchange $Q_{i⁢j}→-Q_{i⁢j}$, $ζ_{n}→-ζ_{n}$, the same shape deformations occur when considering meridional alignment of the order parameter ($q<0$) and exchanging contractile $(ζ_{n}>0)$ and extensile $(ζ_{n}<0)$ active stresses.

![Figure 3.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig3-v1.jpg)

**Figure 3.:** (a) Two possible configurations for the nematic order parameter $Q_{i⁢j}$ on a sphere with a + 1 topological defect at each pole: meridional (left) or circumferential (right) alignment. The order parameter minimises an effective energy (Equation 9 with $l_{c}=0.1⁢R_{0}$). (b) Order parameter $q⁢(s)=Q_{ϕ}^{ϕ}⁢(s)$ as a solution of the Euler–Lagrange Equation 16 on a sphere with $R_{0}=1$ and $l_{c}=0.1R_{0};q=1$ at the equator and $q=0$ at the locations of the defects (poles). For uniform $ζ_{n}$, $ζ_{n}⁢\nabla_{i}⁡Q^{i⁢s}$ is the active nematic contribution to the tangential force balance (Equation 63) and, close to the equator, results in the elongation of the surface along the axis of symmetry for $ζ_{n}>0$, and its contraction for $ζ_{n}<0$.

As before, we study the cases of vanishing pressure difference across the shell (Figure 4a–e) and constrained volume inside the shell (Figure 4f–i). With a nematic tension profile on the surface, a deformation away from the spherical shape occurs even for homogeneous active nematic tension, $l_{a}/L_{0}=1$ (Figure 4a–e).

![Figure 4.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig4-v1.jpg)

**Figure 4.:** (a, e) Shape diagrams. (b, g) Details of shape diagram illustrating the behaviour of solution branches. (d) Curvature at the south pole for extensile stress. (c, e, h, i) Dynamic simulations of shell shape changes, for parameter values indicated in the phase diagrams (a, f). Other parameters: $K~=10^{3},η~_{c⁢b}=10^{-2}$, $η~_{V}=10^{-4}$, $l~_{c}=0.1$.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Surface quantities are shown for the last plotted time step in Figure 4. The location of the neck, taken as the point where $C_{ϕ}^{ϕ}$ is maximal, is marked by a grey line in the plots. In (a, b) the radius at the equator, the volume, and the pole–pole distance are shown as functions of time. In (c) the smooth sigmoidal pattern of $ζ_{n}⁢(s)$ is visualised as two discrete regions (colour coded as red and blue) for simplicity. The parameter values correspond to the examples in Figure 4c, e and h in the main text.

In the extensile case $ζ_{n}<0$ (or in the contractile case $ζ_{n}>0$ if $q<0$), and no pressure difference across the shell, the surface progressively flattens into a flat, double-layered disc (Figure 4b, $l_{a}/L_{0}=1$, $ζ_{n}<0$). There is no shape transition occurring; instead, we find that the shape converges to a limit shape as $|ζ_{n}|→∞$ (Appendix 4). The limit shape corresponds to two parallel flat discs of radius $R_{d}$, separated by a distance $2⁢h$, connected by a narrow curved region. An asymptotic analysis (Appendix 4) shows that the radius of the disc and the separating distance obey the scaling relations, in the limit $κ≪K⁢l_{c}^{2}$:

$$
R_{d}∼l_{c},h∼(\frac{κl_{c}}{K})^{\frac{1}{3}}
$$

The first relation shows that the limit shape has the size of the characteristic nematic length $l_{c}$. Physically, for $l_{c}≪L_{0}$, the nematic active tension results in a contraction of the shape, until the shape is sufficiently close to the defect core for the nematic order to ‘dissolve,’ thus limiting further increase in the active tension.

In the contractile case ($ζ_{n}>0$), the shape elongates until a shape transition is reached, characterised by a fold in the solution branch (Figure 4b, $l_{a}/L_{0}=1$, $ζ_{n}>0$). Following the solution branch after the fold eventually gives rise to a sequence of presumably unstable shapes with the formation of a central constricting neck. Intrigued by this result, we performed dynamical simulations for contractile active tensions above the shape transition (Figure 4c and e; Figure 4—figure supplement 1). Dynamic simulations show separation of the shape into two or more compartments via dynamical neck constrictions, with the neck radius vanishing over time (Figure 4—figure supplement 1a). Within the neck, $q→0$ as a result of the diverging principal curvatures (as can be seen from the presence of a term $(\frac{cos⁡(ψ)}{x}⁢q)^{2}$ term in the nematic free energy, Equation 102). In particular, for values close to the branch fold (Figure 4c) the dynamics is reminiscent of cell division; however, in contrast to existing models of cell division (Salbreux et al., 2009; Turlier et al., 2014), the constriction appearing here does not require a narrow peak of active stress around the equator to occur. At larger contractile stress (Figure 4e), a narrow, elongated tube forms around the equator. This tube thins out over time, and two symmetric necks emerge and constrict, suggesting that the shape would eventually separate into three topologically separated surfaces (Figure 4—figure supplement 1b).

For $0<l_{a}/L_{0}<1$ and extensile stress in the active region $\deltaζ_{n}<0$, the active region tends to flatten more and more strongly as $|\delta⁢ζ_{n}|$ is increased, and the total curvature vanishes at the south pole ($C_{k}^{k}→0$, Figure 4d). For $0<l_{a}/L_{0}<1$ and contractile stress $\deltaζ_{n}>0$, a fold in the solution branch appears at large value of $\delta⁢ζ_{n}$ (Figure 4b and d). Following the solution branch beyond the fold results in a complex trajectory in parameter space, corresponding to successive additions of new bubbles to a linear chain of bubbles within the active region. This bubble chain is observed both with free or constrained volume (Figure 4b and g). Here, we cannot conclude however whether these shapes are unstable. Instead, we consider the shape dynamics for $\delta⁢ζ_{n}$ values larger than the shape transition, here at fixed internal volume (Figure 4h and i). Here, a neck forms within the active region and its constriction leads to the separation of a smaller bubble. For small enough $l_{a}$ the smaller bubble appears nematic-free and spherical (Figure 4h, Figure 4—figure supplement 1b). This is consistent with restoration of isotropic state stability which can occur on a sphere whose size becomes smaller or comparable to $l_{c}$ (Appendix 3 section ‘Stability of the isotropic state on a sphere’).

### Active nematic bending moments

We now turn to shape deformations resulting from active bending moments oriented along the nematic order $Q_{i⁢j}$. As for nematic tension, we adopt the convention of nematic alignment along the circumference, $Q_{ϕ}^{ϕ}=q>0$; alignment along the meridians can be studied simply by changing the sign of the active coefficient $ζ_{c⁢n}$.

We first discuss the case where the nematic active bending moment is homogeneous ($l_{a}/L_{0}=1$), where there is no difference of pressure across the surface, and where $ζ_{cn}=\deltaζ_{cn}<0$ (Figure 5a–c and g). We find that the sphere deforms into a shape with a central cylindrical part (Figure 5a and b). The length of the cylindrical part increases with increasing value of $|ζ_{c⁢n}|$. To characterise this, we note that the corresponding steady-state shape solutions have vanishing tensions $t_{s}^{s}=0$ and $t_{n}^{s}=0$ everywhere (Figure 5—figure supplement 1) and the force balances Equations 63 and 64 are trivially satisfied. The torque balance Equation 65 reads

$$
2κ∂_{s}C_{k}^{k}−ζ_{cn}∂_{s}q=2ζ_{cn}\frac{cos⁡ψ}{x}q.
$$

Combining Equations 26 and 48 one obtains that $L[C_{s}^{s}−C_{ϕ}^{ϕ}−ζ_{cn}q/(2κ)]=0$, with the operator $ℒ=\partial_{s}+2⁢\frac{cos⁡ψ}{x}$. Solutions to $ℒ⁢[f]=0$ have the form $f=A/x^{2}$ with A a constant. The boundary condition that the function $f$ should be finite at the poles requires $A=0$, such that

$$
C_{s}^{s}−C_{ϕ}^{ϕ}=\frac{qζ_{cn}}{2κ} .
$$

As a result, if the shape has a cylindrical part, in which $C_{s}^{s}=0$ and $q=1$, then the cylinder radius $R_{c}$ is given by

$$
\frac{1}{R_{c}}=−\frac{ζ_{cn}}{2κ},
$$

and since such solutions are area-preserving, with $u=0$, the length of the cylindrical part scales as $L_{c}∼1/R_{c}$. These relations are in excellent agreement with simulation results for large enough $|ζ_{c⁢n}|$ (Figure 5g).

![Figure 5.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig5-v1.jpg)

**Figure 5.:** (a, d) Shape diagrams. (b, e) Details of shape diagram illustrating the behaviour of solution branches. (c, f) Dynamic simulations of shell shape changes, for parameter values indicated in the phase diagrams (a, d). In both cases in (f) the dynamics results in self-intersection. (g) Comparison of curvature and length of the cylindrical tubes for $l_{a}/L_{0}=1,0.7,0.3$, $\deltaζ_{cn}<0$ with analytical predictions. The tube length is measured on the steady-state shape as the arc length of the deformed active region, $s_{t⁢u⁢b⁢e}=s⁢(s_{0}=l_{a})$, and the tube curvature as $C_{ϕ}^{ϕ}(s_{tube}/2)$. Other parameters: $K~=1000,η~_{c⁢b}=10^{-2}$, $η~_{V}=10^{-4}$, $l~_{c}=0.1$. In (c), (f), for $\deltaζ_{cn},ζ_{cn}<0$ the orientation of the director field drawn on the surface (black lines) is set by $-Q_{i⁢j}$.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Details of steady-state shapes resulting from nematic bending moments with $ζ_{cn}<0$ and free volume.(a) Closed cylinder; (b) shape with cylindrical appendage. Such solutions are characterised by $t_{s}^{s}=t_{n}^{s}=u=0$ everywhere, and a cylindrical part where $C_{s}^{s}=0$ and $m¯_{s}^{s}$ is constant.

When $l_{a}<L_{0}$, the active region forms an outward cylindrical protrusion (Figure 5a, b and g) whose radius is still well described by Equation 28, replacing $ζ_{c⁢n}$ by $\delta⁢ζ_{c⁢n}$, the value of the active nematic bending moment in the active region (Figure 5g). Using that within the cylindrical protrusion $u=0$ so that the cylindrical protrusion has the same area as the original active domain and the relation Equation 85 for the size of the active domain, we find that the length of the active protrusion is now given by

$$
L_{c}≃\frac{R_{0}^{2}}{R_{c}}(1−cos⁡\frac{l_{a}}{R_{0}})=−\frac{\deltaζ_{cn}R_{0}^{2}}{2κ}(1−cos⁡\frac{l_{a}}{R_{0}}),
$$

which is again in excellent agreement with numerical simulation for large $|\delta⁢ζ_{c⁢n}|$ and for different values of $l_{a}/L_{0}$ (Figure 5g).

For $ζ_{cn}>0$ and $l_{a}/L_{0}=1$ we find erythrocyte-like shapes, where the indentations at the poles become stronger with $ζ_{c⁢n}$ until the two poles touch (Figure 5b). This behaviour remains for $l_{a}<L_{0}$, resulting in a self-intersection line in the phase diagram (Figure 5a). Here, the shape can take the form of an inner tube entering the spherical shell (Figure 5b), reminiscent of epithelial shape changes observed during sea urchin gastrulation (Ettensohn, 1984).

Interestingly, when $l_{a}/L_{0}<1$ and the volume is free to change, both signs of $\delta⁢ζ_{c⁢n}$ result in a cylindrical appendage forming from the active region. The sign of $\delta⁢ζ_{c⁢n}$ determines whether the cylinder forms outside or inside of the remaining, roughly spherical shape. Dynamics simulations confirm that the shapes described above are stable solutions (Figure 5c). At the tip of the emerging cylinder lies the +1 topological defect. For $\deltaζ_{cn}<0$, when the protrusion grows towards the outside, such a situation is reminiscent of the observation of nematic defects in Hydra, where a set of topological defects, with +1 defects at the tip, have been observed in growing tentacles (Maroudas-Sacks et al., 2021). There, actin layers are perpendicular to each other, with circumferential alignment in the inner cell layer and longitudinal in the outer layer, which would indeed result in $\deltaζ_{cn}<0$ with our sign convention if the layers are contractile.

We now describe surfaces with fixed volume (Figure 5d–f). Here, we do not observe cylindrical shapes or protrusions as in the case of free volume. When $ζ_{cn}<0$ and $l_{a}=L_{0}$ the surface becomes spindle-like, narrowing at the poles with increasing $|ζ_{c⁢n}|$. As in the free volume case, when $ζ_{cn}>0$ the two opposite poles come in contact with each other (Figure 5e); such that subsequent fusion of the poles would lead to an overall toroidal shape of the shell. The shapes become more complex for $l_{a}<L_{0}$. Shape transitions occur at large $|\delta⁢ζ_{c⁢n}|$, for both $\deltaζ_{cn}<0$ and $\deltaζ_{cn}>0$ (Figure 5e). In the case $\deltaζ_{cn}<0$, for increasing magnitude of the active bending moment, the shape becomes increasingly curved at the boundary between the passive and active regions, until the solution is lost. In the case $\deltaζ_{cn}>0$, the shell indents within the active region and the solution branch has a fold. To the right of the fold line in the shape diagram, the steady-state solutions are eventually lost through the formation of a small neck that separates off a smaller, internalised compartment. In contrast to the case of isotropic bending moments, here the sign of $\delta⁢ζ_{cn}$ determines whether the active region folds inwards or outwards, independent of the initial size $l_{a}/L_{0}$. As before, we use dynamics simulations to study the deformations for large $|\delta⁢ζ_{cn}|$ (Figure 5f). For both signs of $\delta⁢ζ_{cn}$, these result in shapes that are self-intersecting either along a circle ($l_{a}/L_{0}=0.3,\delta⁢ζ_{cn}=-150⁢κ/R_{0}$) or at the poles ($l_{a}/L_{0}=0.5,\delta⁢ζ_{cn}=50⁢κ/R_{0}$).

## Discussion

In this study of deformations of patterned nematic active surfaces, we have found a diverse zoology of possible shape changes (Figure 6), characterised by budding and neck constrictions, transition of sphere to cylinder, tubulation, and flattening. We find that introduction of a nematic field on the surface greatly increases the space of possible shapes. Overall our work contributes to the characterisation of the ‘morphospace’ which biological systems can explore.

![Figure 6.](https://cdn.elifesciences.org/articles/75878/elife-75878-fig6-v1.jpg)

**Figure 6.:** Active tensions and bending moments are present only in the red region of the surface. For $ζ_{cn}<0$ the director field orientation (black lines) is set by $-Q_{i⁢j}$.

Some of our findings recapitulate epithelial deformations observed in biological systems. The flattening observed for an extensile homogeneous nematic surface (Figure 4b, $l_{a}/L_{0}=1$) could in principle lead to merging of the two apposed surfaces into a double-layer for large $|ζ_{n}|$. Such a process of tissue planarisation appears to occur as an intermediate step in skin organoid formation, where epithelial cysts fuse and merge to form transient bilaterally symmetric structures (Lei et al., 2017). The formation of tubular appendages from nematic bending moments appears to recapitulate growth/regeneration of elongated bodies and tentacles in Hydra (Maroudas-Sacks et al., 2021) and, with an opposite sign, of epithelial invagination during sea urchin embryo gastrulation (Ettensohn, 1984).

The axisymmetric structure we have considered here naturally gives rise to two +1 nematic defects at the poles (Figure 3a). These defects then structure the nematic field and, as a result, the shape changes driven by nematic active tension or bending moments. Such an interplay between topological defect and shape changes is a recurring theme that may play a key role in morphogenesis (Frank and Kardar, 2008; Metselaar et al., 2019; Hoffmann et al., 2021; Blanch-Mercader et al., 2021a; Blanch-Mercader et al., 2021b). In practice +1 nematic defects are unstable to separation into two +1/2 defects; however, it is conceivable that a polar or additional weakly polar field stabilises the +1 defects (Amiri et al., 2022). Extension of the present work beyond axisymmetric structures will allow to distinguish more clearly the purely nematic and polar cases.

Continuum theories for curved surfaces, such as the Helfrich theory, have been extremely successful to describe shape transformations of passive vesicles, including homogeneous or phase-separated vesicles with coexisting domains (Seifert et al., 1991; MacKintosh and Lubensky, 1991; Jülicher and Lipowsky, 1993; Seifert, 1997; Allain et al., 2004; Sens and Turner, 2004; Bassereau et al., 2014). The effect of broken symmetry variables on passive surfaces, arising, for instance, from molecular tilt giving rise to polar order on a lipid membrane, has been considered theoretically (MacKintosh and Lubensky, 1991; Lubensky and Prost, 1992; Park et al., 1992). Continuum theories of active surfaces can similarly allow to study epithelial deformations (Salbreux and Jülicher, 2017; Morris and Rao, 2019; Messal et al., 2019). We note some important differences between the active surface model described here and passive membranes. (i) Our constitutive equations for tensions and bending moments Equations 5 and 6 do not in general derive from a free energy (Salbreux and Jülicher, 2017) and describe a system out-of-equilibrium; (ii) while lipid membranes are nearly incompressible and are usually treated as surfaces with constant area, cells within epithelial tissues can change their area significantly (Latorre et al., 2018), which prompted us to consider a finite area modulus $K$: for example, simulations with constant volume have relative area changes of up to 20% (Figure 2—figure supplement 2); (iii) patterns of active tensions and bending moments imposed here also do not derive from an energy and are thought to respond to spatiotemporal chemical cues: in contrast, phase-separated domains in passive lipid vesicles obey equilibrium thermodynamics and their size is controlled, for instance, by line tension at the domain boundary (Jülicher and Lipowsky, 1993). In some cases, however, a similarity appears between shape transformations obtained in the active model we study here and the passive Helfrich model. For instance, budding occurring in lipid membranes due to phase separation of domains with different spontaneous curvature (Jülicher and Lipowsky, 1993) is similar to the budding we observe here for different regions with different active isotropic bending moments.

We find here that nematically oriented active bending moments can give rise to spontaneous cylindrical tubes, without external force application (Figure 5). Spontaneous formation of hollow cylindrical vesicles with polar order due to molecular tilt has been discussed Lubensky and Prost, 1992; there the cylindrical shapes are considered to be open and the gain in defect energy allows the open cylinder to be more stable than the spherical shape. In contrast, we find here active surfaces which spontaneously form tubes, but stay closed and keep their topological charge. It has also been reported that a supported bilayer membrane under compression can spontaneously form tubes under negative tension (Staykova et al., 2013). In this work we have chosen to consider only positive isotropic tension; negative isotropic tension could give rise to further buckling instabilities. Models for chiral lipid bilayers in a tilted fluid phase have also predicted tubular shapes (Helfrich and Prost, 1988; Selinger and Schnur, 1993; Selinger et al., 1996; Tu and Seifert, 2007). Here, we have not considered chiral effects. These effects could be introduced by generalising the constitutive Equations 5 and 6, including terms which appear for surfaces with broken planar-chiral or chiral symmetry (Salbreux and Jülicher, 2017).

In contrast to purely elastic models of morphogenesis (Höhn et al., 2015; Haas et al., 2018), we have considered here morphogenetic events occurring on time scales long enough for shear elastic stresses to be relaxed by cell topological rearrangements, such that the tissue exhibits fluid behaviour (Popović et al., 2017). Whether a tissue behaves as an elastic or fluid material on time scales relevant to morphogenesis can in principle be probed experimentally (Mongera et al., 2018).

While we have focused the interpretation of our results to epithelial mechanics, the constitutive Equations 5 and 6 we have considered here are generic and may also describe the large-scale behaviour of active nematics formed with cytoskeletal filaments and motors on a deformable surface (Keber et al., 2014). We considered here, however, a situation where the two-dimensional fluid has area elasticity, whereas cytoskeletal networks can in principle be fluid with respect to both shear and bulk shear due to the turnover of components.

In this study, we have considered chemical and mechanical processes to be uncoupled, except for the profile of active tension or torque being advected with the surface flow. Introducing additional couplings explicitly in this framework will extend the repertoire of shapes considered here. A natural choice is to consider the effect of a chemical undergoing reaction-diffusion on the surface and advected by the fluid, regulating active forces on the surface (Mietke et al., 2019a; Mietke et al., 2019b). Here, we assumed that orientational order relaxes quickly compared to other dynamical processes; in future work, this assumption could be lifted and one could study in particular how chemical regulation could influence the dynamics of orientational order in the tissue. Cells could also be sensing their own curvature and actively adapt their behaviour accordingly (Chen et al., 2019), which could lead to a dependency of the active coupling coefficients $ζ$, $ζ_{n}$, $ζ_{c}$ or $ζ_{c⁢n}$ on the trace or determinant of the curvature tensor $C_{i⁢j}$. It would be interesting to explore shapes arising from such a feedback. Volume conservation at cellular level could also be included explicitly, for instance, by introducing a tissue height field (Morris and Rao, 2019). Finally, we have considered here a tissue with a fixed preferred area, implicitly assuming that the epithelium is not growing. Tissue growth is a key aspect of biological development (Gokhale and Shingleton, 2015; Eder et al., 2017), and cell division and death can fluidify elastic stresses in an epithelium (Ranft et al., 2010); adding regulated growth in the model will be a step forward in our understanding of active morphogenesis of biological tissues.
