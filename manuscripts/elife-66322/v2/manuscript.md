# Ciliary chemosensitivity is enhanced by cilium geometry and motility

## Authors

- David Hickey<sup>1</sup> ([ORCID: 0000-0003-0149-712X](https://orcid.org/0000-0003-0149-712X))
- Andrej Vilfan<sup>1</sup> ([ORCID: 0000-0001-8985-6072](https://orcid.org/0000-0001-8985-6072)) †
- Ramin Golestanian<sup>1</sup> ([ORCID: 0000-0002-3149-4002](https://orcid.org/0000-0002-3149-4002)) †

### Affiliations

1. Max Planck Institute for Dynamics and Self-Organization (MPIDS) Göttingen Germany
2. J. Stefan Institute Ljubljana Slovenia
3. Rudolf Peierls Centre for Theoretical Physics, University of Oxford Oxford United Kingdom

† Corresponding author

## Abstract

Cilia are hairlike organelles involved in both sensory functions and motility. We discuss the question of whether the location of chemical receptors on cilia provides an advantage in terms of sensitivity and whether motile sensory cilia have a further advantage. Using a simple advection-diffusion model, we compute the capture rates of diffusive molecules on a cilium. Because of its geometry, a non-motile cilium in a quiescent fluid has a capture rate equivalent to a circular absorbing region with ∼4× its surface area. When the cilium is exposed to an external shear flow, the equivalent surface area increases to ∼6×. Alternatively, if the cilium beats in a non-reciprocal way in an otherwise quiescent fluid, its capture rate increases with the beating frequency to the power of 1/3. Altogether, our results show that the protruding geometry of a cilium could be one of the reasons why so many receptors are located on cilia. They also point to the advantage of combining motility with chemical reception.

## Introduction

Cilia are small hairlike organelles with a microtubule-based core structure that protrude from the cell surface. They are found on most eukaryotic cells (Nachury and Mick, 2019) and can be broadly classified into two categories: primary and motile. Primary cilia, of which there is only one on each cell, have primarily sensory functions (as receptors for chemical, mechanical, or other signals) (Zimmermann, 1898; Berbari et al., 2009; Hilgendorf et al., 2016; Spasic and Jacobs, 2017; Ferreira et al., 2019). Due to their shape and their role in signalling, they are often referred to as ‘the cell’s antenna’ (Marshall and Nonaka, 2006; Malicki and Johnson, 2017). Motile cilia, typically appearing in larger numbers (Brooks and Wallingford, 2014; Spassky and Meunier, 2017), move the surrounding fluid by beating in an asymmetric fashion (Golestanian et al., 2011; Gilpin et al., 2020), and often with some degree of coordination (Uchida and Golestanian, 2010; Elgeti and Gompper, 2013). They play a key role in a number of processes, including the swimming and feeding of microorganisms (Guasto et al., 2012; Lisicki et al., 2019), mucus clearance in airways (Bustamante-Marin and Ostrowski, 2017), fluid transport in brain ventricles (Faubel et al., 2016), and egg transport in Fallopian tubes. However, there are exceptions to this classification. Primary cilia in the vertebrate left-right organiser are motile and drive a lateral fluid flow that triggers, through a mechanism that is not yet fully understood, a distinct signalling cascade determining the body laterality (Essner et al., 2002). There is also mounting evidence that motile cilia can have various sensory roles (Bloodgood, 2010), including chemical reception (Shah et al., 2009). Adversely, receptors localised on motile cilia, such as ACE2, can also act as entry points for viruses including SARS-CoV-2 (Lee et al., 2020). Some chemosensory systems, including vomeronasal (Leinders-Zufall et al., 2000) and olfactory neurons (Bhandawat et al., 2010) and marine sperm cells (Kaupp et al., 2003), are known to achieve a sensitivity high enough to detect a small number of molecules.

The sensitivity of a chemoreceptor is characterised by its binding affinity for the ligand, as well as its association/dissociation kinetics. If the time-scale of ligand dissociation is longer than the time-scale of the changes in ligand concentration, or if the ligands bind irreversibly, the sensitivity is determined by the binding rate alone. It has been shown that the theoretical limit of sensing accuracy is achieved when the receptors detect the frequency of binding events and when re-binding is excluded (Bialek and Setayeshgar, 2005; Endres and Wingreen, 2009) Because diffusion is fast on very short length scales, only 1% of the surface area of a cell or cilium needs to be covered in high-affinity receptors to obtain near-perfect adsorption (Berg and Purcell, 1977). Even if this condition is not satisfied, the membrane itself could non-specifically bind the ligands with near-perfect efficacy, which then reach the receptors in a two-stage process. In either of these cases, as long as there is no advection, the binding rates can be estimated using the theory of diffusion-limited reactions (Adam and Delbruck, 1968). This binding rate is known as the diffusion limit, and it has already been shown that flagella-driven swimming microorganisms can break the diffusion limit in order to increase their access to nutrients (Short et al., 2006).

The increasingly overlapping functions of sensory and motile cilia lead to the natural question about the advantage of placing receptors on a cilium, or in particular on a motile cilium. Because of its small volume, a cilium forms a compartment that facilitates efficient accumulation of second messengers (Marshall and Nonaka, 2006; Hilgendorf et al., 2016). Placing receptors on a protrusion, away from the flat surface, could have other advantages, like avoiding the effect of surface charges or the glycocalycx. It has also been suggested that the location of chemoreceptors on cilia exposes them to fluid that is better mixed (Marshall and Nonaka, 2006). A recent study suggests that the hydrodynamic interaction between motile and sensory cilia can enhance the sensitivity of the latter (Reiten et al., 2017). However, the question of how the geometry and motility of cilia affect their ability to capture and detect ligands has still remained largely unexplored.

In this paper, we investigate the theoretical limits on association rates of ligands on passive and motile cilia. In particular, we address the question of whether the elongated shape of a cilium and its motility can improve its chemosensory effectiveness. By using analytical arguments and numerical simulations, we show that the capture rate of a cilium is significantly higher than that of a receptor located on a flat epithelial surface. Motile cilia can further improve their chemosensitivity. Finally, we show that a cilium within an immotile bundle has a lower capture rate than an isolated cilium, but a higher one when the cilia are sufficiently motile.

## Results

In this study, we calculate the second-order rate constant for diffusive particle capture on a cilium. We discuss scenarios where the fluid and the cilium are at rest, where the fluid exhibits a shear flow, where the cilium is actively beating, and where a bundle of hydrodynamically interacting cilia absorbs particles.

We consider a perfectly absorbing cilium protruding from a non-absorbing surface, in a fluid containing some chemical species with a concentration field $c$. Far from the cilium, the unperturbed concentration has a constant value $c_{0}$. The rate constant $k$ is defined such that

$$
I=c_{0}⁢k,
$$

where $I$ is the capture rate, defined as the number of captured particles per unit time.

Since the aforementioned cilium is perfectly absorbing, we define an absorbing boundary condition such that the concentration of the chemical species is zero at every point on the cilium’s surface. We assume that the flat membrane surrounding the cilium does not absorb particles and it is therefore described with a reflecting boundary condition at $z=0$. The geometry and boundary conditions are illustrated in Figure 1.

![Figure 1.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig1-v2.jpg)

**Figure 1.:** The cilium satisfies an absorbing boundary condition, and there is a constant concentration an infinite distance from the cilium. The coloured overlay shows the concentration field in the absence of any fluid flow.

### Cilium in quiescent fluid

We consider a cilium (modelled as a cylinder next to a boundary at $z=0$) in a quiescent fluid, with the goal of determining its capture rate constant in the absence of advection. In the case where there is a steady state with no advection, the advection-diffusion equation reduces to

$$
D⁢\nabla^{2}⁡c=0,
$$

where $D$ is the diffusion constant. The rate constant is determined by the integral of the current density $𝐉$ over the surface, which follows from Fick’s law:

$$
k=-\frac{1}{c_{0}}⁢\intd𝐒⋅𝐉=\frac{1}{c_{0}}⁢\intd𝐒⋅(D⁢\nabla⁡c).
$$

As we show in Appendix 1, the rate constant can be evaluated using an analogy between particle diffusion and electrostatics (Berg and Purcell, 1977). Up to a prefactor, the capture rate is determined by the self-capacitance $C$ of a conducting body of the same shape as $k=D⁢C/\epsilon_{0}$.

To determine the capture rate of a cilium embedded in a non-absorbing surface, we first eliminate the reflective boundary condition at the surface by symmetrically extending the problem to a cylinder of length $2⁢L$ in open space and considering $1/2$ of its capacitance. There is no closed-form expression for the capacitance of a cylinder, so we loosely approximate this cylinder as a prolate spheroid with semi-major axis $L$ and semi-minor axis $a$. Using its self-capacitance in the limit $L≫a$ (Snow, 1954), we find the rate constant:

$$
k_{cilium}=2⁢\pi⁢D⁢\frac{L}{ln⁡(2⁢L/a)}.
$$

This value agrees well with simulations: the ratio of the simulated to this analytical rate constant is 1.02.

The finding that the capture rate scales almost linearly with the length of the cilium can be compared to experimental data obtained on olfactory cilia from the nasal cavity of mouse, whose lengths in different regions vary from a few micrometers to tens of micrometers. Challis et al., 2015 have used patch-clamp recordings on olfactory sensory neurons and measured the response to pulses of an odorant (eugenol or a mixture of 10 odorants), lasting $5-400⁢ms$. Regions with different lengths show very different sensitivity thresholds, differing by an order of magnitude. The results are qualitatively consistent with the predicted length dependence of the capture rate.

To quantify the advantage of localising the receptors on a cilium, we compare it with a case where the receptors form a circular patch on a flat surface (Figure 2a). Again, we assume that the receptor patch has a perfectly absorbing surface, while the surface surrounding it is reflective. We determine the size of the patch needed to attain the same rate constant as the cilium. The rate constant for a circular patch on the reflective boundary can be found by applying the electrostatic analogy to the well-known result for the self-capacitance of a thin conducting disc of radius $R$ (Berg and Purcell, 1977):

$$
k_{patch}≈4⁢D⁢R.
$$

![Figure 2.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig2-v2.jpg)

**Figure 2.:** All diagrams use $L/a=80$, indicated on the graphs by a red dot. (a) In a quiescent fluid, the cilium has the same capture rate as a surface patch with 3.8 times the surface area. (b) The area ratio $A_{patch}/A_{cilium}$ as a function of the cilium aspect ratio $L/a$ in a quiescent fluid, given by Equation (6). (c) In a shear flow at a high Péclet number, the capture rate of the cilium reaches that of a surface patch with 6.0 times the surface area. (d) The area ratio as a function of the aspect ratio in the high Péclet number limit (Equation 14).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The lines show the capture rates for cilia that absorb particles only on a fraction of their length, starting from the tip. The schematics indicate the absorbing part of the cilium in blue and the non-absorbing part in black.

We find that the patch has a much larger surface area than the cilium with the same rate constant. We can calculate this area ratio:

$$
\frac{A_{patch}}{A_{cilium}}≈\frac{\pi^{2}}{8}⋅\frac{L}{a}\frac{1}{ln^{2}⁡(2L/a)}.
$$

The area ratio as a function of the aspect ratio $L/a$ is shown in Figure 2b. For a typical cilium aspect ratio of $L/a=80$ (with $L=10\mum$, and $a=125nm$), this area ratio is 3.8, implying that the cilium is much more effective per unit area than a receptor on the surface of the cell. Olfactory cilia have a great variation of lengths, ranging from $2.5⁢\mu⁢m$ to $100⁢\mu⁢m$ (Challis et al., 2015; Williams et al., 2014). If we neglect the fact that long cilia are not straight, the calculated area ratio ranges from 2.7 to 18. Using an exact numerical result for the capacitance of a cylinder (Paffuti, 2018), the ratio becomes 4.5 for $L/a=80$. With the dimensions given above, the radius of the circular patch with the same capture rate is $R=3.4\mum$.

### Cilium in shear flow

At the scale of cilia, the flow is characterised by a low Reynolds number, meaning that viscous forces dominate over inertia. The fluid motion is well-described by the Stokes equation, together with the incompressibility condition:

$$
η∇^{2}u−∇p=0
$$



$$
∇⋅u=0
$$

in which $𝐮$ is the fluid velocity, η is the dynamic viscosity, and $p$ is the pressure. The concentration field of some chemical species suspended within this fluid is governed by the advection-diffusion equation:

$$
\frac{∂c}{∂t}+u⋅∇c=D∇^{2}c
$$

where $c$ is a function of both position and time.

The ratio of advection to diffusion is described by the dimensionless Péclet number. This is usually written as some characteristic flow speed multiplied by some characteristic length scale, all divided by the diffusion constant.

Because the cilium grows from a flat surface with a no-slip boundary condition, the flow can be described as a uniform shear flow with the shear rate $\gamma˙$. To estimate the capture rate constant of a cilium in a shear flow, we make use of the fact that the radius of the cylinder is much smaller than the length scale over which the shear flow varies. We therefore approximate the local rate density at any point on the cilium with that of an infinitely long cylinder in a uniform flow with velocity $v⁢(z)=\gamma˙⁢z$. The capture rate per unit length is

$$
\frac{dk_{cilium}}{dz}=\betaD⋅(A\frac{av}{D})^{1/3},
$$

where $\beta=2.50$ is a numerical constant (see Appendix 2 for derivation).

Now the total rate constant is obtained by integration over the cilium length

$$
k_{cilium}=\int_{0}^{L}dz⁢\beta⁢D⋅(\frac{a⁢\gamma˙⁢z}{D})^{1/3}=\frac{3}{4}⁢\beta⁢D⁢L⋅(\frac{L}{a})^{-1/3}⁢Pe_{cilium}^{1/3}.
$$

We take the characteristic velocity to be the speed of the cilium’s tip relative to the surrounding fluid, and hence the Péclet number for the extended cilium is

$$
Pe_{cilium}=\frac{\gamma˙⁢L^{2}}{D}.
$$

This expression for the rate once again shows a strong positive relationship between cilium length and sensitivity, as is known to be the case in real biological systems (Challis et al., 2015). The characteristic Péclet number for the cross-over between the diffusive and the convective capture is of the order $∼L/a≈80$.

Once again we determine the size of a circular surface patch offering an equivalent effectiveness to the cilium in a flow with the same shear rate (Figure 2c). The high-Pe rate constant for a patch in a shear flow is (Stone, 1989):

$$
k_{patch}≈D⁢R⁢[ζ⋅Pe_{patch}^{1/3}+O⁢(Pe_{patch}^{-1/6})],
$$

where $Pe_{patch}≡\gamma˙⁢R^{2}/D$ and $ζ=2.157$ is a purely numerical constant. We can calculate the ratio of the area of the equivalent patch to the area of the cilium for these high-Pe asymptotic results:

$$
\frac{A_{patch}}{A_{cilium}}≈\frac{1}{2}⁢(\frac{3⁢\beta}{4⁢ζ})^{6/5}⋅(\frac{L}{a})^{3/5}≈0.42⁢(\frac{L}{a})^{3/5}.
$$

The area ratio is shown in Figure 2d and compared with the results in a quiescent fluid. For a typical cilium aspect ratio $L/a=80$ (with $L=10\mum$, and $a=125nm$), this area ratio is 6.0 – much larger than the area ratio in a quiescent fluid, which was 3.8. This means that a cilium is better per area than a patch at both low and high Péclet numbers, but the cilium excels when the Péclet number is large.

We additionally investigated the question how robust the results are if the receptors are localised to only one segment of the cilium. In a model, we assumed that of the total length $L$, the distal part $ν⁢L$ is absorbing, while the proximal $(1-ν)⁢L$ is reflective. At high Péclet numbers, we can modify the integration limits in Equation (11) and obtain a theoretical capture rate $k_{cilium}(ν)=k_{cilium}⋅(1−(1−ν)^{4/3})$. The result is compared to simulations in Figure 2—figure supplement 1. A cilium with receptors over the distal 50% of its length therefore achieves 60% of the maximal capture rate.

### Active pumping

A mounting collection of evidence suggests that both primary and motile cilia have sensory roles (Bloodgood, 2010). We are interested in the extent to which cilium motility can increase their ability to detect particles. To this end, we numerically simulate various different possible types of ciliary motion in otherwise quiescent fluids.

Because of the complex flow patterns and time-dependent boundary conditions, the absorption by a beating cilium is not analytically tractable. Instead, we use numerical simulations to determine the rate constants. We consider four different active pumping scenarios: a purely reciprocally moving cilium, a cilium tracing out a cone around an axis perpendicular to the surface, a cilium tracing out a tilted cone, and a cilium with a trajectory that includes bending, to raise the pumping efficiency (all shown in their respective order in Figure 3a–d).

![Figure 3.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig3-v2.jpg)

**Figure 3.:** (a) The cilium is undergoing reciprocal motion, which is not generating any net flow. (b) The cilium moves along a cone with its axis perpendicular to the surface, such that it produces a rotational flow, but no long-range fluid transport. (c) The cilium moves along a tilted cone, which generates a long-range volume flow. (d) The cilium follows a realistic trajectory, beginning with a recovery stroke along the no-slip surface in 1, then performing an overhead power-stroke from 2 to 3 before returning to one in another recovery stroke. (e) The capture rate constants $k$ of a beating cilium as a function of the Péclet number. The rates are determined using stochastic simulations. The error bars denote 95% confidence intervals and the dashed line shows a fit function that interpolates between the high and low-Péclet limits. All rates are normalised to the rate constant for a diffusion-limited capture with a cylindrical cilium with the same length and width.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** These results were obtained from numerical simulations. The lines show the capture rates for cilia that absorb particles only on a fraction of their length, starting from the tip. The schematics indicate the absorbing part of the cilium in blue and the non-absorbing part in black.

The rate constants in these scenarios, relative to that of a non-moving cilium, are plotted in Figure 3e. Analogously to the cilium in a shear flow, we define the Péclet number using the maximum tip velocity during the cycle:

$$
Pe=\frac{v_{tip}^{max}⁢L}{D}.
$$

The reciprocally moving cilium (Figure 3a) displays almost no improvement over several orders of magnitude of the Péclet number. This is expected, because Purcell’s scallop theorem (Purcell, 1977) states that purely reciprocal motion does not create any net flow, so the particle intake is largely diffusive in nature. A minor increase of the rate constant with the Péclet number is caused by the local shear flow that facilitates absorption on the surface.

The cilium moving around a vertical cone (Figure 3b) induces a net rotational flow, but no inflow or outflow (by symmetry, the time-averaged flow can only have a rotational component [Vilfan, 2012]). Nevertheless, the constant motion of the cilium through the fluid leads to a higher local capture efficiency. The rate constant therefore shows more improvement; over a few orders of magnitude of the Péclet number, the rate constant increases by a factor of two.

The tilted cone (Figure 3c) shows a much higher capture rate, which is unsurprising. When the cilium is near to the plane, the no-slip boundary screens the flow, whereas when it is far from the plane, its pumping is unimpeded. This results in the cilium inducing a long range flow in one direction, characterised by a finite volume flow rate (Smith et al., 2008). The long range flow causes a constant intake that replenishes the depleted particles. At high Péclet numbers, the capture rate scales $k∼Pe^{1/3}$, which is the same dependence as in an external shear-flow, although with a prefactor that is lower by a factor of ∼2. Locally, the relative flow around the cilium is the same whether a cilium is pivoting or resting in a shear flow. The pumping effect of the tilted cilium, on the other hand, provides sufficient inflow that the concentration around a cilium sees only a small depletion effect.

We finally simulated the capture process on a cilium exerting a realistic beating pattern, consisting of a stretched working stroke and a bent, sweeping recovery stroke (Figure 3d). The capture rate is close to that of the tilted cone, but surpasses it at very high Péclet numbers.

### Collective active pumping

We consider seven cilia on a hexagonal centred lattice with lattice constant $0.95⁢L$, with a view to understand how the presence of multiple cilia affects performance. We quantify the performance gain using a quantity $Q$, which we define as

$$
Q=\frac{k_{multiple}}{k_{cilium}⁢(Pe)⋅N_{cilia}},
$$

which represents the fractional per-cilium improvement in rate constant compared to a single isolated cilium at the same Péclet number.

Using numerical simulations, we find that at zero Péclet number (Figure 4a–b), $Q≈0.5$, which means that the cilia locally deplete the concentration field, harming the per-cilium effectiveness; in a quiescent fluid, it is most efficient for cilia to stand far away from their neighbours.

![Figure 4.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig4-v2.jpg)

**Figure 4.:** Comparison between the capture rate constant of a single cilium (a, c) and a bundle of $N_{cilia}\in{4,7,19}$ cilia (b, d–g).In the insets, the height of each red cylinder indicates the rate constant per cilium at $Pe≈10000$, and the number of cylinders represents the number of cilia. For immotile cilia (a, b), a bundle has a lower per-cilium capture rate than an isolated cilium, although the the total rate constant of the bundle is higher. The reduced capture rate per cilium is caused by the depletion of ligands close to the bundle. For motile cilia (d–g), the situation is reversed and the capture rate per cilium in a bundle (d–g) can be significantly higher than for an isolated cilium (c). The increase can be explained by the collective flow generation, which helps the capture on all cilia. In (d) the cilia all beat with the same frequency corresponding to $Pe≈10000$ but with identical phases. In (e–g) all cilia beat with the same frequency corresponding to $Pe≈10000$, but their phases are chosen randomly. It can be seen that the random phases give a higher rate constant than the uniform phases. (h) shows how the performance gain $Q$ varies with the Péclet number for different configurations. The rates shown at each point are the average of 30 random phase configurations like the one shown in (e). The dashed line is the $Q$-value for $Pe=0$ for each configuration.

However, when the cilia actively move (with each tracing out a tilted cone with a different randomly-chosen phase lag compared to its neighbours, as in Figure 4e) the trend is reversed: we find that at $Pe≈10000$, $Q≈1.53$, meaning that per cilium, the capture rate is around 50% higher in the collective when compared to an isolated cilium with the same Péclet number. We find that over the range of Péclet numbers simulated, the $Q$ increases monotonically with the Péclet number (Figure 4h).

When comparing these randomly chosen phases to a patch of cilia which beat in uniform, we find that cilia which beat in phase (Figure 4d) see an improvement over the stationary case with $Q≈1.16$, but are much less effective than the cilia patch that beats with random phases. The random phases give a higher volume flow, and complex hydrodynamic interactions between the randomly-phased cilia result in a slightly higher capture chance for any given particle. Similar levels of improvement are also seen for other arrangements of cilia forming a bundle, that is, $N_{cilia}=19$ on a hexagon (Figure 4f) or $N_{cilia}=4$ on a square (Figure 4g). Furthermore, an improvement of randomly beating over uniformly-beating cilia has been observed in previous work with finite-sized particles (Ding and Kanso, 2015; Nawroth et al., 2017). The results suggest that mutual enhancement of capture rates is a robust phenomenon and does not depend on a specific geometry.

## Discussion

Our results address a simple question: does the location of so many chemical receptors on cilia bring them an advantage in sensitivity? Besides the well-known advantages of compartmentalisation, which facilitates the downstream signal processing, we show that the elongated shape of a cilium provides an advantage for the capture rate of molecules in the surrounding fluid. The advantages can be summarised as follows:

Our results are based on a few assumptions. We assumed that the particles get absorbed and detected upon their first encounter of the cilia surface – an assumption that is justified if the receptors are covering the surface at a sufficient density (Berg and Purcell, 1977), or if the particles bind non-specifically to the membrane of the cilium first. We also treat the particles as point-like (their size only has an influence on their diffusivity), which is accurate for molecules up to the sizes of a protein and we do not expect a significant error even for small vesicles. The Rotne-Prager tensor approximation used to determine the flow fields does not exactly satisfy the no-slip boundary condition on the surface of the cilium, especially at high Péclet numbers.

With the typical dimensions of a cilium ($L=10⁢\mu⁢m$, $a=0.125⁢\mu⁢m$) and a diffusion constant of a small molecule $D=10^{−9}m^{2}s^{−1}$, we obtain $k_{cilium}=7⁢pM^{-1}⁢s^{-1}$. A chemosensory cilium working at the physical limit is therefore capable of detecting picomolar ligand concentrations on a timescale of seconds. Sensitivity thresholds in the sub-picomolar range have been measured in some olfactory neurons (Frings and Lindemann, 1990; Zhang et al., 2013), indicating that some olfactory cilia work close to the theoretical sensitivity limit. If the cilia are embedded in mucus with a viscosity at least 3 orders of magnitude higher than water (Lai et al., 2009) (we disregard its viscoelastic nature here) and the molecule has a Stokes radius of a few nanometres, the diffusion-limited capture rate reduces to around $k_{cilium}=1⁢nM^{-1}⁢s^{-1}$.

In a shear flow with a typical shear rate of $\gamma˙=10s^{−1}$, the Péclet number of a small molecule in water is of the order of $Pe≈1$, where the capture rate still corresponds to the stationary case. However, with larger molecules and higher viscosities, the Péclet numbers can exceed 104, leading to a significant enhancement of the capture rate.

When the same cilium is beating with a frequency of $25Hz$, the Péclet number is of the order ∼10, which is too small to have an effect on the capture rate. With larger molecules and higher viscosities, the Péclet numbers can be significantly higher. With a medium viscosity of $0.2Pa⋅s$ (200 times the water viscosity) and a Stokes radius of $10nm$, it reaches 105, meaning that the motility accelerates the capture rate by one order of magnitude. For example, according to one hypothesis, motile cilia in the zebrafish left-right organizer (Kupffer’s vesicle) both generate flow and detect signalling particles, possibly extracellular vesicles (Ferreira et al., 2017; Ferreira et al., 2019) similar to the proposed ‘nodal vesicular parcels’ (Tanaka et al., 2005). With a cilium length of $L=6⁢\mu⁢m$ and a particle radius of $a=100⁢nm$, we obtain $Pe=1300$, showing that the capture rates can be several times higher than in a passive cilium. Figure 5 shows how the molecular Stokes radius affects the fluid viscosity required to break the diffusion limit for a few different scenarios. However, when the particle size becomes comparable to the cilium diameter, the approximation that treats them as point particles loses validity. Indeed, it has been shown that particle size can have a direct steric effect on the capture rate (Ding and Kanso, 2015). Furthermore, the capture process of large particles can depend on a competition between hydrodynamic and adhesive forces (Tripathi et al., 2013). Steric effects can even lead to particle enrichment in flow compartments (Nawroth et al., 2017).

![Figure 5.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig5-v2.jpg)

**Figure 5.:** The blue, orange, and green lines show the results for a passive cilium in a shear flow (Figure 2c), the red line for an actively beatig cilium (Figure 3c) and the magenta line for a bundle of 7 cilia (Figure 4e). For all lines, the cilium dimensions are $L=10\mum$ and $a=250nm$.

We have thus proven that for individual isolated cilia the geometry of a cilium always means an advantage in chemical sensitivity over receptors covering the same area on a flat surface (assuming they act as perfect absorbers), whether in a quiescent or moving fluid. At high Péclet numbers, which are achieved in viscous fluids, with very large particles or in very strong flows, the advantage of a cilium increases further and even confers an advantage in chemosensitivity to cilium bundles over individual cilia. These advantages can work in concert with others, such as avoiding charged surfaces and glycocalix and the provision of a closed compartment on the inside. Further work might examine the extent to which motility benefits cilia in a fluid with bulk flow, or investigate the effect of metachronal waves on ciliary chemosensitivity. Finally, our results shed light on possible engineering applications for microfluidic sensing devices based on these ideas, for example using magnetic actuation (Vilfan et al., 2010; Meng et al., 2019; Matsunaga et al., 2019).

## Materials and methods

Numerically simulated point particles are injected into a finite system containing a motile cilium, and move around due to advection (resulting from the motion of the cilium) and diffusion, until they either escape from the system or are absorbed by the cilium. The proportion of particles which are captured is used to compute a rate constant.

### Flow calculation

The hydrodynamics are computed using a modified Rotne-Prager mobility tensor $𝐌$ that accounts for the no-slip boundary. If there are $N$ spheres of equal radius $R$ in the simulation, each having a prescribed trajectory $𝐫_{i}⁢(t)$ and each acted upon by a force $𝐅_{i}⁢(t)$, then these forces must satisfy (Vilfan et al., 2010)

$$
r˙_{i}(t)=\sumj=1NM[r_{i}(t),r_{j}(t);R,R]⋅F_{j}(t)
$$

for every $i\in[1,N]$. Since every term except the forces is known, the forces can be determined numerically at a given $t$ by solving this set of simultaneous equations. Then the fluid velocity at any point $𝐱$ can be determined by

$$
𝐮⁢(𝐱,t)=\sumi=1N𝐌⁢[𝐱,𝐫_{i}⁢(t);0,R]⋅𝐅_{i}⁢(t).
$$

In the simulations we used $N=20$ spheres, corresponding to an aspect ratio $L/a=40$. A somewhat lower value than in the analytical calculations was chosen to save computational time and also to compensate for the fact that a cylinder is replaced with a chain of spheres.

### Injection

We require a particle injection procedure that satisfies the concentration boundary condition $c→c_{0}$ far from the absorbing cilium. We achieve this by introducing two bounding boxes in the simulation: an inner and an outer box, separated by a thin distance $d$ (Figure 6). The particles are injected at the boundary of the inner box and absorbed at the outer box. The injection rate is calculated such that it corresponds to the advective-diffusive flux through the layer between the boxes if the concentration at the inner box is $c_{0}$. Because the flux through the boundary layer is much larger than the flux of particles absorbed inside the inner box, the method is suited to ensure a constant concentration boundary condition. The method is similar to a recent algorithm using a single boundary (Ramírez-Piscina, 2018), but uses a simpler injection function.

![Figure 6.](https://cdn.elifesciences.org/articles/66322/elife-66322-fig6-v2.jpg)

**Figure 6.:** Since the fraction in incident particles absorbed by the cilium is small compared to the fraction absorbed by the outer surface, the concentration at the inner boundary is very close to c0. The coloured overlay shows the concentration as recorded in an example numerical simulation of a cilium in a shear flow with $Pe=50$.

To calculate the injection current density, we solve the one-dimensional steady-state advection-diffusion equation

$$
0=D⁢\frac{d^{2}⁢c}{d⁢x^{2}}-v⁢\frac{d⁢c}{d⁢x},
$$

with the boundary conditions $c⁢(0)=0$ and $c⁢(d)=c_{0}$. The solution is 

$$
c⁢(x)=c_{0}⁢\frac{e^{vx/D}-1}{e^{vd/D}-1}.
$$

By the application of Fick’s law, this leads to an expression for the current density through the inner box:

$$
j⁢(x)=v⁢c_{0}⁢\frac{1}{1-e^{-vd/D}}.
$$

We assume that a test particle will take take much longer to reach the cilium than the characteristic time required for the flow to change, and hence we take $v=⟨u(x,t)⋅n^⟩_{t}$, where $n^$ is the inward pointing surface normal of the inner box. This function can then be used to probabilistically weight where particles are injected on the inner box.

### Numerical integration

The test particle position is updated using an Adams-Bashforth-Milstein multistep numerical integration method in the presence of noise (Tocino and Senosiain, 2015):

$$
𝐱_{i+1}=𝐱_{i}+Δ⁢t⁢[\frac{3}{2}⁢𝐮⁢(𝐱_{i},t)-\frac{1}{2}⁢𝐮⁢(𝐱_{i-1},t-Δ⁢t)]+ξ_{i}.
$$

Because the computation of the flow field $𝐮$ (see Equation 18) is the most demanding step, it is advantageous over methods that require additional function evaluations per step. $ξ_{i}$ is a vector where each element is pseudorandomly generated Gaussian noise with standard deviation $\sqrt{2⁢D⁢Δ⁢t}$ and mean of zero.

### Rate evaluation

We finish each simulation run when the particle position reaches the cilium (capture), or the outer box (escape). At the end, the rate constant is determined as

$$
k=\frac{I}{c_{0}}⁢\frac{n_{capture}}{n_{capture}+n_{escape}},
$$

where $I$ is the calculated total particle flux, obtained by integrating the flux density over the inner box, $I=\intjdS$.

### Numerical parameters

For all numerical simulations, we use a cilium consisting of 20 beads (thus giving a length to radius ratio $L/a=40$). For the conical and reciprocal motion (Figure 3a–c), we use an opening angle (between the cone axis and surface) of 30°, and for the titled conical motion (Figure 3c) the axis of the cone is tilted relative to the vertical by an angle of 55°.

In the collective regime, the parameters are the same, with the addition of a hexagon lattice constant of $0.95⁢L$. The cones are tilted such that their axes are perpendicular to one chosen side of the hexagon (left to right in Figure 4d-f).
