# From plasmodesma geometry to effective symplasmic permeability through biophysical modelling

## Authors

- Eva E Deinum<sup>1</sup> ([ORCID: 0000-0001-8564-200X](https://orcid.org/0000-0001-8564-200X)) †
- Bela M Mulder<sup>2</sup> ([ORCID: 0000-0002-8620-5749](https://orcid.org/0000-0002-8620-5749))
- Yoselin Benitez-Alfonso<sup>4</sup> ([ORCID: 0000-0001-9779-0413](https://orcid.org/0000-0001-9779-0413))

### Affiliations

1. Mathematical and statistical methods (Biometris) Wageningen University Wageningen Netherlands
2. Living Matter Department Institute AMOLF Amsterdam Netherlands
3. Laboratory of Cell Biology Wageningen University Wageningen Netherlands
4. Centre for Plant Science University of Leeds Leeds United Kingdom

† Corresponding author

## Abstract

Regulation of molecular transport via intercellular channels called plasmodesmata (PDs) is important for both coordinating developmental and environmental responses among neighbouring cells, and isolating (groups of) cells to execute distinct programs. Cell-to-cell mobility of fluorescent molecules and PD dimensions (measured from electron micrographs) are both used as methods to predict PD transport capacity (i.e., effective symplasmic permeability), but often yield very different values. Here, we build a theoretical bridge between both experimental approaches by calculating the effective symplasmic permeability from a geometrical description of individual PDs and considering the flow towards them. We find that a dilated central region has the strongest impact in thick cell walls and that clustering of PDs into pit fields strongly reduces predicted permeabilities. Moreover, our open source multi-level model allows to predict PD dimensions matching measured permeabilities and add a functional interpretation to structural differences observed between PDs in different cell walls.

## Introduction

The formation of spatial patterns in plants requires the transport and interaction of molecular signals. This sharing of information coordinates cell fate decisions over multiple cells and the isolation of cell fate determinants within a cell or group of cells on the same developmental path. Small molecules such as sugars, peptides, hormones and RNAs move long and short distances to coordinate cell/organ development (Otero et al., 2016). Cell-to-cell transport of proteins, such as transcription factors, is also important in the regulation and/or developmental reprogramming of local cellular domains (Gallagher et al., 2014). A well studied example is SHORT-ROOT (SHR), an Arabidopsis thaliana GRAS family transcription factor, that moves from the stele to cortical-endodermal tissue layers to specify cell fate and root patterning (Nakajima et al., 2001; Spiegelman et al., 2018; Wu and Gallagher, 2013; Wu and Gallagher, 2014). Other mobile factors with developmental importance include TARGET OF MONOPTEROS 7, PEAR transcription factors and miRNAs (Lu et al., 2018; Miyashima et al., 2019; Skopelitis et al., 2018).

Plant cells are connected by channels named plasmodesmata (PDs) that facilitate the transport of these molecules. PD are narrow membrane lined structures embedded in cell walls to allow for symplasmic (cytoplasm-to-cytoplasm) molecular flux (Figure 1). The ER forms a tubular structure called desmotubule (DT) that traverses the PD, leaving a discrete cytosolic sleeve (also called ‘cytoplasmic sleeve’ in the literature) where molecular transport occurs (Nicolas et al., 2017a; Sager and Lee, 2018). In the region closest to the PD entrances, the cytosolic sleeve appears constricted (neck) in most tissue types, although there are recent observations of ’straight’ PDs in meristematic root sections (Nicolas et al., 2017b). Cell walls at PD locations play a key role in regulating its dimensions. The accumulation of callose, a cell wall beta-1,3 glucan polysaccharide synthesized by callose synthases and degraded by β−1,3-glucanases (Zavaliev et al., 2011; Amsbury et al., 2017), is the best understood mechanism for the control of PD dimensions and symplasmic transport capacity (i.e. effective symplasmic permeability). Other factors such as membrane composition, shape and number of PDs change during development and between cell types adding extra dimensions to PD regulation (Nicolas et al., 2017a). Mutants blocked in PD form and function are embryo or seedling lethal, highlighting the importance of these structures for normal plant development (Kim et al., 2002; Benitez-Alfonso et al., 2009; Xu et al., 2012).

![Figure 1.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig1-v3.jpg)

**Figure 1.:** (A) Electron microscopy image showing one PD, constricted at the neck regions (arrows), from Arabidopsis thaliana root tissue. The image was extracted from a reconstructed tomograph. Scale bar: 50 nm. The image was kindly provided by the Bayer lab. (B) Cartoon showing PD geometry and structural features. (C-F) The model to determine effective symplasmic permeability considers that connectivity within a cell file (C) is affected by the distribution of PDs in the cell wall (D) (modelled as a function of the cytoplasmic column belonging to a single PD (E)) as well as by the structural features of individual PDs (F).

Small molecules can move via PD by diffusion (non-targeted transport). This is considered to be predominantly symmetrical (Schönknecht et al., 2008; Maule, 2008), while in certain tissues, such as secreting trichomes (Waigmann and Zambryski, 1995; Gunning and Hughes, 1976) and the phloem (Ross-Elliott et al., 2017; Comtet et al., 2017), hydrodynamic flow may create directionality. The maximum size of molecules that can move by this generic ‘passive’ pathway is often referred to as the ‘size exclusion limit’ (SEL), which obviously depends on PD properties and structural features (Dashevskaya et al., 2008). Large molecules can move through PD via an 'active’ or ‘targeted’ pathway overriding the defined SEL. This may involve additional factors that temporarily modify these substrates, target them to the PDs, or induce transient modifications of the PDs to allow for the passage of larger molecules in a highly substrate dependent fashion (Zambryski and Crawford, 2000; Maule et al., 2011).

Computational modelling approaches have been applied to model PD transport but, so far, these have mainly focused on hydrodynamic flow and the specific tissues where that matters (Blake, 1978; Bret-Harte and Silk, 1994; Jensen et al., 2012; Ross-Elliott et al., 2017; Comtet et al., 2017; Foster and Miklavcic, 2017; Couvreur et al., 2018). The few existing studies on diffusive transport do not consider neck constrictions or the approach to PDs from the cytoplasmic bulk. Most models consider PDs as straight channels, with advective/diffusive transport through an unobstructed cytosolic sleeve and typically, but not always, account for reduced diffusivity inside these narrow channels compared to the cytosol (Bret-Harte and Silk, 1994; Liesche and Schulz, 2013; Dölger et al., 2014; Ross-Elliott et al., 2017; Couvreur et al., 2018). Only the oldest of this set, (Blake, 1978), uses a dilated central region in its calculations, but is entirely focused on hydrodynamics. In specific contexts, also a few other geometries are considered. (Ross-Elliott et al., 2017) also consider ‘funnel’ shaped PDs, which are observed in the phloem unloading zone, but ignore the DT in their diffusion model, as they only calculate a best case scenario for diffusive transport. In the context of size selectivity for small (sugar) molecules in phloem loading, also the so-called ‘sub-nano channel model’ of PD geometry has been considered (Liesche and Schulz, 2013; Comtet et al., 2017). In this model, symplasmic transport is modelled to be confined to nine cylindrical channels spanning the PD. This was based on a 9-fold rotational symmetry in enhanced 'top view’ electron micrographs but never validated experimentally in longitudinal sections. Instead, sparsely spaced axial spoke structures have been reported (Ding et al., 1992; Nicolas et al., 2017b).

Experimental measurement of the parameters that determine effective symplasmic permeability is difficult and many examples exist of misleading and/or conflicting results. Generally speaking two main approaches are used, providing results at different scales that are hard to reconcile. On the one hand, ultrastructural observations using transmission electron microscopy (EM) can provide useful data on PD dimensions and structural features but, despite recent advances, sample preparation affects the integrity and dimensions of PDs to an unknown extent potentially yielding an underestimation of relevant parameters (Nicolas et al., 2017b). On the other hand, tissue level measurement of symplasmic fluxes is achieved using symplasmic molecular reporters, but this is either invasive or limited to few molecular sizes, mostly fluorescein and its chemical relatives (hydrodynamic radii of about 0.4 to 0.6 nm) and GFP derived fluorescent proteins (such as DRONPA-s (28 kDa), Dendra2 (26 kDa), (photoactive and non-photoactive) single GFP (27 kDa, hydrodynamic radius 2.45–2.82 nm) and its multiples [Calvert et al., 2007; Terry et al., 1995; Chudakov et al., 2007; Gerlitz et al., 2018; Kim et al., 2005; Rutschow et al., 2011]). In all cases, the tissue geometry and varying degrees of vacuoloarization can severely complicate the interpretation of the measurements in terms of effective wall permeability for symplasmic transport. Old data on symplasmic permeability use either microinjection or particle bombardment, which allow for a much wider size range of dyes/molecular reporters, but these techniques can produce cellular stress, which affects PD function (Liesche and Schulz, 2012). Even when using the same dye/fluorescent molecule and the same tissue, these approaches deliver much lower permeabilities than less invasive techniques, demonstrating that they are unreliable for estimating permeabilities in unperturbed plants (e.g. see Haywood et al., 2002, or compare Rutschow et al., 2011 and Goodwin et al., 1990). Less invasive methods involve transgenic lines expressing fluorescent proteins under cell-specific promoters (Roberts et al., 2001; Stadler et al., 2005a), which are very time consuming to generate, or photoactivation and photobleaching techniques (Rutschow et al., 2011; Gerlitz et al., 2018). These approaches have yielded valuable insights, but again, both are limited to few proteins/molecular sizes.

In summary, despite recent advances in the development of probes and techniques, effective symplasmic permeability is difficult to assess directly. The fast response of plants to wounding and other stresses, may render part of the ultrastructurally derived parameters less reliable than others, explaining the frequent observation of apparently incompatible results when modelling diffusive symplasmic transport from ultrastructural measurements. In a multi-species analysis correlating photobleaching and electron microscopy results, (Liesche et al., 2019) were unable to find a universal model for matching measurements at the ultrastructural and tissue levels for different interfaces along the phloem loading pathway, illustrating the need for better models. Ideally, we would be able to integrate the results of the experimental approaches at both levels in a model that considers their limitations in order to get more accurate estimates of effective symplasmic permeability and the underlying structural parameters. This brings us to our central question: what do we need to assume about PD size, number, structure, etc. to be able to reproduce tissue level measurements? Moreover, PD geometry changes during development (Roberts et al., 2001; Fitzgibbon et al., 2013), inspiring our second main question: how do distinct features of PD geometry influence transport properties?

Here, we describe the biophysical properties of diffusive symplasmic transport considering detailed PD structural features (such as the DT and the neck region) and the approach from the cytoplasmic molecular bulk towards PDs that are either evenly distributed or clustered into pit fields (Faulkner et al., 2008) (Figure 1). Inside our model PDs, the entire cytosolic sleeve is available for particle diffusion (‘unobstructed cytosolic sleeve model’). We investigate how neck/central region, wall thickness, the presence of a DT and PD clustering into pit fields affect transport characteristics for different particle sizes, adding a functional context to some puzzling recent experimental observations. We also apply our framework to compute effective permeabilities for carboxyfluorescein (CF), a fluorescent dye used routinely to measure changes in symplasmic permeability. Comparing calculated and experimentally measured values, we demonstrate that the relatively high effective CF permeabilities observed by Rutschow et al. (2011) can be explained by our model of diffusive non-targeted symplasmic transport and reveal the potential source of conflicts with ultrastructural measurements. We found that, in this context, our model performed better than the ‘sub-nano channel model’ (Liesche and Schulz, 2013) referred to above. Our calculations demonstrate that multi-scale modelling approaches can integrate results from PD structural dimensions and molecular fluxes and reveal conflicts on these determinations. We, therefore, recommend these should be applied systematically when defining effective symplasmic permeability for a particular tissue/molecule and/or biological context. To facilitate this, we share a python program for computing effective permeabilities from PD geometries as a community resource.

## Results

### Outline of the model

Our aim is to describe the symplasmic transport properties of a cell wall as an effective wall permeability, that is a single number that could be plugged into tissue/organ level models. For this, we split the transport into two parts: the movement through an individual channel representing a PD and the approach to this channel from the cytoplasmic bulk (Figure 1). This implicitly assumes a homogeneous cytosol. The basic geometrical terminology that we considered in our calculations is introduced in the cartoon PD shown in Figure 1B. An overview of all mathematical symbols is given in Appendix 1.

Obtaining good EM data of PD dimensions is notoriously hard. We therefore opted for a simple geometrical description that allows us to study the effects of PD neck, central region and desmotubule dimensions with as few parameters as possible (see Materials and methods). We modelled a single PD as a 3-part cylindrical channel (Figure 2A), with total length $l$, which would typically equal the local wall thickness. The ends of the channel were modelled by narrow cylinders representing the plasmodesmal ‘neck’ constriction. These have length $l_{n}$ and radius $R_{n}$. The central region has radius $R_{c}$. Over the whole length, the center of the channel is occupied by a ‘desmotubule’ (DT) modelled as a cylinder of radius $R_{d⁢t}$. The part available for diffusive transport, the cytosolic sleeve, is the space between the outer cylinder wall and the DT.

![Figure 2.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig2-v3.jpg)

**Figure 2.:** (A) Individual PDs are modelled using multiple cylinders with a total length $l$, neck (inner) radius $R_{n}$ and neck length $l_{n}$, central region (inner) radius $R_{c}$ and desmotubule (outer) radius $R_{d⁢t}$. B,C: Illustration of the impact of steric hindrance and rescaled parameters. The gray areas of the longitudinal (B) and transverse (C) sections cannot be reached by the center of the particle with radius $\alpha$ (steric hindrance). For a concise description of the available volume and cross section area, we use the rescaled lengths $l~_{n}=l_{n}+\alpha$, $R~_{c}=R_{c}-\alpha$, $R~_{d⁢t}=R_{d⁢t}+\alpha$ and $R~_{n}=R_{n}-\alpha$. (C) The cross section area available for diffusion on a transverse section was named $A~$, which depends on the particle radius ($\alpha$). $A~$ is the area of the white ring in each cross section. The maximum particle size $\alpha¯$ is illustrated with a dashed circle. For a particle of size $\alpha=\alpha¯$, $A~=0$. (D) In practice, particles spend less time diffusing close to the wall than farther away from it (hydrodynamic hindrance). Consequently, the area close to wall contributes less to diffusive transport, as illustrated with purple gradients. These additional hindrance effects are accounted for in $A~~$.

We made the arguably simplest choice of modelling particles as (non-additive, i.e. not interacting among themselves) hard spheres with radius $\alpha$. This is partially supported by previous research showing that the hydrodynamic radius is the main determinant of PD transport characteristics, leaving behind, among others, particle charge (Dashevskaya et al., 2008; Terry and Robards, 1987). We also assumed that PD walls are rigid, and hence are unable to deform to accommodate larger particles. These assumptions imply a boundary condition: the center of a particle cannot come closer to the wall than the particle’s radius $\alpha$ (Figure 2B,C). This so-called steric hindrance reduces the volume that is available for diffusion of the particle’s center in a size dependent manner. Moreover, the maximum particle radius that can pass the PD, $\alpha¯$, is always well defined. In practice, a precise definition of the SEL in terms of molecule size/shape is hard to give, however, we can use $\alpha¯$ to operationalize the SEL concept in a straightforward manner. To avoid confusion, however, we will consistently write $\alpha¯$ when referring to our model.

We introduced rescaled geometrical parameters to account for the reduced available volume in a compact way: $l~_{n}=l_{n}+\alpha$, $R~_{c}=R_{c}-\alpha$, $R~_{d⁢t}=R_{d⁢t}+\alpha$ and $R~_{n}=R_{n}-\alpha$. With these, the available surface area (Figure 2C) is

$$
A~_{x}(\alpha)=\pi(R~_{x}^{2}-R~_{d⁢t}^{2}),(2\alpha<R_{x}-R_{d⁢t}),
$$

with $x=n$ for the neck and $x=c$ for the central region. In the typical situation that the neck is the narrowest part of the channel, the maximum particle radius that can pass is: $\alpha¯=(R_{n}-R_{d⁢t})/2$.

Considering pure diffusion without particle turnover inside the PD, particle flux through the channel is described by $\frac{\partial⁡C_{x⁢y⁢z}}{\partial⁡t}=D⁢\nabla^{2}⁡C_{x⁢y⁢z}$, or in steady state: $D⁢\nabla^{2}⁡C_{x⁢y⁢z}=0$, with $C_{x⁢y⁢z}$ the position dependent particle concentration and $D$ the particle’s diffusion constant inside the PD. Note that $D$ strongly depends on particle size. Assuming a homogeneous distribution of particle flux over (the available part of) each channel cross section, we can treat diffusion through the channel as a simple 1D problem along the channel axis (for the impact of this assumption, see Appendix 2). Particle mass conservation, as dictated by the steady state diffusion equation, then gives that the local concentration gradient at position $x$, $\nabla⁡C_{x}$, is inversely proportional to the available surface area $A_{x}$, so $\nabla⁡C_{c}=A~_{n}/A~_{c}⁢\nabla⁡C_{n}$. The total concentration difference over the PD, $Δ⁢C=C_{l}-C_{0}$ is accordingly distributed over the channel: $Δ⁢C=2⁢l_{n}~⁢\nabla⁡C_{n}+(l-2⁢l_{n}~)⁢\nabla⁡C_{c}$. The steady state molar flow rate $Q⁢(\alpha)$ through each channel is proportional to the entrance cross section: $Q⁢(\alpha)=-D⁢A~_{n}⁢\nabla⁡C_{n}$. Solving these equations for $\nabla⁡C_{n}$ leads to:

$$
Q⁢(\alpha)=-\frac{D⁢A~_{n}⁢A~_{c}}{2⁢l~_{n}⁢A~_{c}+(l-2⁢l~_{n})⁢A~_{n}}⁢Δ⁢C.
$$

This result can be improved further by incorporating hydrodynamic interactions between particles and walls (Figure 2D). To that end we followed (Liesche and Schulz, 2013) in employing the so-called hindrance factors $0\leqH⁢(\lambda)<1$, which are based on proper cross sectional averaging of particle positions over time, as described by Dechadilok and Deen (2006). Based on geometrical considerations, we used the factors for a slit-pore geometry (see Materials and methods). These factors depend on the relative particle size $\lambda$. In our case, $\lambda=2⁢\alpha/(R_{x}-R_{d⁢t})$. In the neck region, $\lambda=\alpha/\alpha¯$. For the full expression and behaviour of $H⁢(\lambda)$, see Materials and methods.

As $H⁢(\lambda)$ already includes the effect of steric hindrance between wall and particle, we can adjust Equation 2 by replacing every instance of $A_{x}~$ with

$$
A~~_{x}=H⁢(\frac{2⁢\alpha}{R_{x}-R_{d⁢t}})⁢A_{x}.
$$

For completeness, we note that the simplification of a uniform particle flux along the channel axis is violated near the neck-central region transitions, resulting in an error of a few percent (see Materials and methods for further discussion). We now define the permeation constant of a single PD, $Π⁢(\alpha)$, through the rule rule steady-state flow rate = permeation constant × concentration difference, yielding

$$
Π⁢(\alpha)≡\frac{Q⁢(\alpha)}{Δ⁢C}=\frac{D⁢A~~_{n}⁢A~~_{c}}{2⁢l~_{n}⁢A~~_{c}+(l-2⁢l~_{n})⁢A~~_{n}}.
$$

We also defined $\tau$ as the corresponding estimate for the mean residence time (MRT) in the channel. Using a steady state mass balance argument this can be calculated as the number of particles in the channel divided by the number leaving (or entering) per unit of time (see Materials and methods for further description).

$$
\tau(\alpha)=\int_{0}^{l}C_{x}A~~_{x}dx/Q(\alpha)
$$

Having defined the permeation constant of a single channel, the effective symplasmic permeability of the wall as a whole ($P⁢(\alpha)$, the quantity that can be estimated using tissue level measurements) follows from the definition $J=P⁢Δ⁢C$ ($steady state flux=permeability\timesdensity jump$):

$$
P⁢(\alpha)=f_{i⁢h}⁢ρ⁢Π⁢(\alpha),
$$

with $ρ$, the density of PDs per unit wall area (number/ μm2) and $f_{i⁢h}$, a (density dependent) correction factor for the inhomogeneity of the wall ($0<f_{i⁢h}<1$). The latter takes into account that the wall is, in fact, only permeable at discrete spots. To calculate $f_{i⁢h}$, we considered a linear chain of cells of length $L$ that are symplasmically connected over their transverse walls (Figure 1C) and computed mean first passage times (MFPT) through a straight PD and a column of cytoplasm surrounding the PD. The column was determined by assigning every bit of cytoplasm to the PD closest to it. For a regular triangular PD distribution, this results in a hexagonal column from the middle of one cell to the middle of the next, with a PD in its centre (Figure 1D). We then converted the MFPT to an effective wall permeability and compared the result with the uncorrected effective permeability computed as $ρ⁢Π⁢(\alpha)$ (as described in the Materials and methods).

As expected, $P⁢(\alpha)$ depends on particle size. Two factors underlie this size dependence, which both affect $Π⁢(\alpha)$: hindrance effects, which reduce the space available for particle diffusion, and the fact that the diffusion constant is inversely proportional to particle size: $D=d_{1}/\alpha$. Figure 3A and (Figure 3—figure supplement 1) show that hindrance effects have the strongest impact for particle sizes close to the maximum $\alpha¯$, whereas the particle diffusion constant always has a large impact Figure 3B. For example, at $R_{n}=R_{c}$, the 50+ fold difference between α = 0.1 nm and α = 2 nm is reduced to a 3-fold difference when ignoring the particle size dependence of the diffusion constant.

![Figure 3.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig3-v3.jpg)

**Figure 3.:** Impact of particle size (radius = $\alpha$) on single pore effective permeability $Π⁢(\alpha)$.(A) Dependence of $Π⁢(\alpha)$ on neck radius ($R_{n}$) and $\alpha$ (different line colours, see legend). The diffusion constant $D$ is inversely proportional to particle size ($D=d_{1}/\alpha$). Dashed lines show $Π⁢(\alpha)$ considering only steric hindrance, solid lines include all hindrance effects. B: Using the same diffusion constant for all particle sizes instead shows that, once particles can pass easily, the particle size dependence of $Π⁢(\alpha)$ is largely due to the relation between particle size and diffusion constant. Parameters for calculations: $l$ = 200 nm, $l_{n}$ = 25nm, $R_{dt}$ = 8 nm, $R_{c}$ = 17.5 nm. For simplicity we use $d_{1}$= 1 nm3/s in this figure. Therefore, only the relative values of the unit permeabilities have meaning (consequently expressed in arbitrary units [a.u.]).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Impact of hindrance effects on $Π⁢(\alpha)$.(A) Impact of hindrance on $Π⁢(\alpha)$ decays with decreasing relative particle size. (B) Steric hindrance alone particularly overestimates $Π⁢(\alpha)$ for large relative particle sizes. Parameters: $l$ = 200 nm, $l_{n}$ = 25nm, $R_{dt}$ = 8 nm, $R_{c}$ = 17.5 nm.

Using the model presented here, we computed the effects of different PD structural features and changes in PD density and distribution on effective symplasmic permeability and its dependence on particle size as described below.

### A dilated central region increases molecular flux in thicker cell walls

Electron microscopy suggests that PDs often have a neck region of reduced radius in comparison to the central region. We investigated how a constricted neck region, or, similarly, a dilated central region, affects PD transport. For this, we compared transport properties while conserving the size selectivity (constant $\alpha¯$). We investigated how both the transport volume (using Equation 2) and transport time ($\tau$ as above) change when the central region is dilated. To compare channels with neck and dilated central region (12 nm $=R_{n}\leqR_{c}$) with narrow straight channels ($R_{n}=R_{c}=$ 12 nm), we define a relative molar flow rate as $Q_{r⁢e⁢l}=Q_{d⁢i⁢l⁢a⁢t⁢e⁢d}/Q_{n⁢a⁢r⁢r⁢o⁢w}$ and similarly relative $\tau_{r⁢e⁢l}$ (Figure 4). For a more detailed discussion of $\tau_{r⁢e⁢l}$ and its computation, see Materials and methods and Appendix 2.

![Figure 4.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig4-v3.jpg)

**Figure 4.:** Impact of central region dilation on molar flow rate ($Q$) and mean residence time ($\tau$).The same legend shown in C applies to all panels. Narrow channels have $R_{n}=R_{c}=$ 12 nm, whereas for necked/dilated channels, $R_{n}$ = 12 nm but $R_{c}$ varies. (A-C) Red curves show the relation between molar flow rate in dilated PD vs narrow PD $Q_{r⁢e⁢l}=Q_{d⁢i⁢l⁢a⁢t⁢e⁢d}⁢(R_{n},R_{c})/Q_{n⁢a⁢r⁢r⁢o⁢w}⁢(R_{n})$ whereas cyan curves show the relation between mean residence time in dilated PD vs narrow PD: $\tau_{r⁢e⁢l}=\tau_{d⁢i⁢l⁢a⁢t⁢e⁢d}⁢(R_{n},R_{c})/\tau_{n⁢a⁢r⁢r⁢o⁢w}⁢(R_{n})$. Both quantities are computed for different particle sizes (solid: $\alpha≈0$, dashed: $\alpha$ = 0.5 nm, sparse dashed: $\alpha$ = 1 nm, dash-dotted: $\alpha$ = 1.5 nm). (A, B) $Q_{r⁢e⁢l}$ and $\tau_{r⁢e⁢l}$ are shown as a function of the radius in the central region $R_{c}$ for different PD lengths (cell wall thickness) (A) $l$ = 100 nm, (B) $l$ = 200 nm. (C) Values calculated for $R_{c}$ = 17.5 nm ($R_{c}^{*}$ in A,B) as a function of PD length. (D) Ratios of curves calculated for $R_{c}$ = 17.5 nm (C) and $R_{c}$ = 26.4 nm (Figure 4—figure supplement 1B) represented for varying PD lengths. Other parameters used for modelling are: $l_{n}$ = 25 nm, $R_{n}$ = 12 nm, $R_{dt}$ = 8 nm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Additional panels: $l$ = 500 nm (similar to A, B), $R_{c}$ = 26.4 nm (similar to C).Additional panels for Figure 4: Impact of central region dilation on molar flow rate ($Q$) and mean residence time ($\tau$). (A) $R_{c}$ variable, $l$ = 500 nm, compare to Figure 4A,B. (B) $R_{c}$ = 26.4 nm, $l$ variable, compare to Figure 4C.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Impact of neck length $l_{n}$ on $Π⁢(\alpha)$, $Q_{r⁢e⁢l}$ and $\tau_{r⁢e⁢l}$.(A, B) Dependence of $Π⁢(\alpha)$ on $l_{n}$ for different PD length (indicated by line colour) for $\alpha$ = 0.5 nm (A) and $\alpha$ = 1 nm (B). Dotted lines indicate that neck length is unrealistically short ($l_{n}<$ 15 nm), or the central region is too short for computations to be considered valid (conservatively estimated as $l-2⁢l_{n}<2⁢R_{c}$). (C) Dependence of $Q_{r⁢e⁢l}$ on $l_{n}$ for different PD length (line colours as in A). (D) Dependence of $\tau_{r⁢e⁢l}$ on $l_{n}$ for different PD length (line colours as in A). (C, D) Except for the scaling of the y-axis, curves for different particle sizes are highly similar. Default parameters: $R_{n}$ = 12 nm, $R_{c}$ = 17.5 nm, $R_{dt}$ = 8 nm.

We then investigated how both $Q_{r⁢e⁢l}$ and $\tau_{r⁢e⁢l}$ change with increasing central region radius $R_{c}$ and how this depends on particle radius $\alpha$ and PD length $l$ (Figure 4). The panels A and B show that molar flow rate increases with the central radius but quickly saturates, whereas mean resident time increases without upper bound. Moreover, both quantities increase faster for larger particle sizes ($\alpha$, dashed lines). In fact, from studying the limiting behaviour of the underlying formulas, we found that $Q_{r⁢e⁢l}$ is always less than its theoretical maximum $\frac{l}{2⁢l~_{n}}$, whereas $\tau_{r⁢e⁢l}$ ultimately scales quadratically with $R_{c}$, and, equivalently, linearly with the surface ratio $A~~_{c}/A~~_{n}$ (see Appendix 3 and Appendix 3—figure 1). In simpler terms: the benefits of increased transport volume with increasing $R_{c}$ saturate, and instead the costs in transport time increases ever faster with further dilation of the central region. This defines a trade-off between transport volume and transport time with increasing $R_{c}$ when we analyze a single PD with a given entrance area.

Our computations also show that with increasing PD length $l$, the balance between both factors shift, because a much larger increase of $Q_{r⁢e⁢l}$ is possible (Figure 4A–C). Similarly, for any given combination of $R_{n}$ and $R_{c}$, $Q_{r⁢e⁢l}$ decreases with increasing $l_{n}$ and decreases faster for shorter $l$, whereas $\tau_{r⁢e⁢l}$ has its maximum at $l~_{n}=l/2$ (Figure 4—figure supplement 2). Together, these computations suggests that dilation of the central region is more favourable in thicker cell walls. Interestingly, this theoretical observation correlates well with a recent EM study in Arabidopsis root tips (Nicolas et al., 2017b). The authors observed that PDs with a distinct dilated central region and neck region occurred mostly in thicker cell walls (average 200 nm), whereas in thin cell walls (average 100 nm), they found mostly straight PDs.

Additionally, (Nicolas et al., 2017b) observed a smaller and less variable radius in channels where the central region was occupied by spokes compared to channels without them ($R_{c}$ = 17.6 nm vs. 26.4 nm on average). To analyze the effects of these changes on molar flow rate and MRT, we redrew the curves to compute relative values for $R_{c}$ = 26.4 nm and $R_{c}$ = 17.5 nm as a function of PD length (cell wall thickness) and for various particle sizes. As an example, panel C shows the variations observed when considering $R_{c}$ = 17.5 nm ($R_{c}^{*}$ in A,B). We found that the molar flow rate $Q_{r⁢e⁢l}$ increases less than the MRT $\tau_{r⁢e⁢l}$ when increasing $R_{c}$ from 17.5 nm to 26.4 nm, except for the smallest particle sizes in combination with large $l$ (Figure 4D). These data suggest that in cell walls of moderate thickness, restricting the radius of the central region (which can be achieved by adding spokes) improves overall performance.

In summary, transport time and transport volume scale differently with the radius of the central region thus producing PDs with a dilated central region becomes more favourable when cell wall thickness increases. However, if the radius of the central region becomes too wide (as exemplified here for $R_{c}$ = 26.4 nm) the increase in transport volume does not compensate for the delay in transport time. Interpretation of this result might explain why mostly straight PDs are found in recently divided cells (with thin cell walls) and why spokes (potentially limiting the radius of the central region) are often observed in mature PDs.

### For the same given maximum particle size a PD with desmotubule can transport more than a PD without

A conserved feature of PDs –at least in embryophytes– is the presence of the DT, so we asked how this structure affects the transport capacity for particles of various sizes. In our model, the DT and the neck radius jointly define the maximum particle radius $\alpha¯$. Assuming that control over maximum particle size $\alpha¯$ is important and a high net flux often is desirable, we estimated the number of cylindrical channels required to match a single PD with DT. Using that $P⁢(\alpha)$ is proportional to orifice area ($≈A_{n}$), we first computed $n_{c}⁢(\alpha¯)$, the number of circular channels that would offer the same $A_{n}$ as a single channel with a DT of radius $R_{dt}$ = 8 nm and the same $\alpha¯$:

$$
n_{c}⁢(\alpha¯)=\frac{(R_{d⁢t}+2⁢\alpha¯)^{2}-R_{d⁢t}^{2}}{\alpha¯^{2}}=4⁢\frac{R_{d⁢t}+\alpha¯}{\alpha¯}.
$$

Figure 5A displays the $n_{c}⁢(\alpha¯)$ as a function of the maximum particle size. As an example, when $\alpha¯$ = 2 nm, 20 cylindrical channels without DT would be needed to match the orifice surface area of a single channel with DT (with $R_{dt}$ = 8 nm). This number decreases for larger $\alpha¯$. We then considered that not all of this surface area is available for transport because of hindrance effects (Figure 2B–D). We found that even if the total surface area is the same, the channel with DT has a larger available surface area than the equivalent number of cylindrical channels. This is because in cylinders a larger fraction of the surface is close to the wall and, hence, hindrance effects are much more severe (Figure 5B, Figure 5—figure supplement 1). The difference increases with increasing relative particle size ($\alpha/\alpha¯$). Steric hindrance, that is the center of a hard particle cannot come closer to the wall than its own radius, plays only a minor part in this effect (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig5-v3.jpg)

**Figure 5.:** DT increases the cross section surface area available for transport per channel given a maximum particle radius $\alpha¯$.(A) The number of cylindrical channels ($n_{c}$) that is required to match the total entrance surface of a single channel with $R_{dt}$ = 8 nm and the same maximum particle radius $\alpha¯$. (B) Shows the relative area available for transport ($A_{n}$) in relation to relative particle size ($\alpha/\alpha¯$) when comparing channels with DT and the equivalent number of cylindrical channels. Total surface area is the same. Solid lines include all hindrance effects ($A~~_{n}/,dtA~~_{n}_{,circle}$; cf. Figure 2D). Dashed lines includes steric effects only ($A~_{n,d⁢t}/A~_{n,c⁢i⁢r⁢c⁢l⁢e}$; cf. Figure 2C).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** Hindrance factors for slit (‘with DT’) and cylinder (‘no DT’) compared.

### Clustering of PDs in pit fields reduces effective symplasmic permeability

The cell wall is only permeable for symplasmic transport where the PDs are. In this scenario, particles have to diffuse longer distances (on average) to reach a spot to cross the wall compared to a wall that is permeable everywhere. To account for this, we have introduced a correction factor, or ‘inhomogeneity factor’, $f_{i⁢h}$ in Equation 6 for the effective symplasmic permeability. Here, we explore how $f_{i⁢h}$ depends on all model parameters. To calculate $f_{i⁢h}$, we treated the cytoplasm as a homogeneous medium. This simplifying assumption is necessitated by the lack of detailed information on the cytoplasm structure and how it differs among cells. Effectively, we assumed that the obstructing effects of ER, vacuoles, etc. are similar throughout the whole cell volume and thus can be captured in a single reduced cytoplasmic diffusion constant.

First, we calculated $f_{i⁢h}$ for isolated PDs positioned on a triangular grid in the cell wall (Figure 6A), as described in the Materials and methods. In Figure 6 we presented $f_{i⁢h}$ as a function of $R_{n}$ and explored its dependence on particle size $\alpha$ (Figure 6—figure supplement 1A), presence/absence of DT (Figure 6—figure supplement 1A), cell length $L$ (Figure 6—figure supplement 1B), density of PD $ρ$ (B), wall thickness $l$ (C) and PD distribution in the wall (D). We found that, provided that $R_{n}$ is large enough for particles to enter (as indicated by vertical cyan lines in Figure 6—figure supplement 1A), $f_{i⁢h}$ is independent of cell length $L$ and particle size $\alpha$ (Figure 6—figure supplement 1A,B) and is not affected by the DT. We also adjusted the computation for different regular trap distributions (Berezhkovskii et al., 2006) to find that $f_{i⁢h}$ also hardly depends on the precise layout of PDs (Figure 6D). Although variations in $f_{i⁢h}$ appear larger at low PD densities, for typical $R_{n}$ values (for example, 12 nm as in Figure 4) density only has a minor impact (Figure 6B). Finally, we found an increase of $f_{i⁢h}$ with increasing PD length $l$, saturating to its theoretical maximum of $f_{i⁢h}=1$ in thick cell walls ($l$ > 500 nm) (Figure 6C). This result reflects the increasing time required for passing the PD itself with increasing PD length and, hence, a decreasing relative importance of the cytoplasmic diffusion.

![Figure 6.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig6-v3.jpg)

**Figure 6.:** Correction factor $f_{i⁢h}$ for inhomogeneous wall permeability depends on PD distribution, cell wall thickness and neck radius.(A) The cartoon shows the geometrical considerations and parameters used to model the diffusion towards PDs. Cell wall inhomogeneity is incorporated as a correction factor $f_{i⁢h}$, $0<f_{i⁢h}\leq1$, which measures the relative impact of cytoplasmic diffusion towards the locations of the PDs in the cell wall compared to reaching a wall that is weakly but homogeneously permeable (i.e., with $f_{i⁢h}=1$). The cytoplasm is considered homogeneous. Each bit of cytoplasm can be assigned to the PD closest to it. With PDs on a regular triangular grid, the cytoplasm belonging to a single PD, with an outer (neck) radius $R_{n}$, is a hexagonal column with cross section area $A⁢w$ and 1/2 of the cell length $L$ on either side of the wall. (B-D) $f_{i⁢h}$ is represented as a function of $R_{n}$. The presence/absence of DT does not affect the values of $f_{i⁢h}$ (Figure 6—figure supplement 1A). In all cases, solid lines correspond to: $l$ = 100 nm, $L$ = 10 μm, $\alpha$ = 0.5 nm, a PD density of $ρ$= 10 PD/μm2, and PDs distributed on a triangular grid. Broken lines show the effects of changes in PD density $ρ$ (B), PD length $l$ (C) and PD distribution (D).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** $f_{i⁢h}$ is not affected by particle size $\alpha$, presence of DT, or cell length $L$.$f_{i⁢h}$ is represented as a function of $R_{n}$, calculated for PDs with (cyan; A only) and without (red) DT. In all cases, solid lines correspond to: $l$ = 100 nm, $L$ = 10 μm, $\alpha$ = 0.5 nm, a PD density of $ρ$ = 10 PD/μm2, and PDs distributed on a triangular grid. Broken lines show the effects of changes in particle size $\alpha$ (A) or cell length $L$ (B). Vertical cyan lines in A indicate the $R_{n}$ in which $f_{i⁢h}$ is start to be measurable as determined by $\alpha<\alpha¯$.

Second, we investigated the effect of PDs grouped in small clusters resembling pit fields (see Materials and methods). The average centre-to-centre distance between PDs in pit fields considerably varies across species, with reported/calculated distances between 60 and 180 nm (Terauchi et al., 2015; Schmitz and Kühn, 1982; Danila et al., 2016; Faulkner et al., 2008). The lowest values, however, are from brown algae, which have a different PD structure from higher plants (Terauchi et al., 2012). As a default, we used $d$ = 120 nm, which also coincides with measurements on electron micrographs of tobacco trichomes presented in Faulkner et al. (2008). In Figure 7A we calculated $f_{i⁢h}$ as a function of total PDs (‘entrances’) per area of cell wall for different numbers of PDs $p$ clustered in a single pit field. We found that $f_{i⁢h}$ decreases with increasing number of PDs in a pit (and constant total PD density $ρ$). Different from isolated PDs, Figure 7A also reveals that, when grouped in pit fields, there is a strong dependence of $f_{i⁢h}$ on total PD density (number of PD entrances per area of cell wall). This could be predicted from extrapolating Figure 6B for isolated PDs, where density dependence also increases with increasing PD radius, because cluster radii $R_{p⁢i⁢t}$ are much larger than the largest $R_{n}$ used in Figure 6B. Figure 7B shows that clustering (in this case 7 PDs) increases the dependence of $f_{i⁢h}$ on PD length (compare solid and dashed lines of the same colour). Increasing the distance between PDs within the cluster (Figure 7C), also increases the dependence of $f_{i⁢h}$ on PD density. Also the arrangement of PDs in small model clusters affects the degree of dependence $f_{i⁢h}$ on $ρ$. In both cases, we observe the steepest dependency of $f_{i⁢h}$ on $ρ$ for the clusters with the lowest within cluster PD density (pit fields with $p$ = 5, 6 and 19: indicated with blue lines in Figure 7A; see also Table 1).

![Figure 7.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig7-v3.jpg)

**Figure 7.:** PD organization within pits is indicated with small cartoons in each graph. Pits themselves are distributed on a regular triangular grid. Within pit fields, the nearest neighbour distance between PDs $d$ (120 nm by default) is independent of the number of PDs per pit field. (A-C) $f_{i⁢h}$ is represented as a function of total PD density $ρ$ (the total number of PD entrances per unit of cell wall area) for: a varying number of PDs per cluster $p$ (as indicated by line type, (A), for different PD length $l$ (B, solid lines: isolated PDs, dash-dotted lines: 7 PDs per cluster, red colour indicates $l$: 100 nm, cyan for 200 nm, blue for 500 nm) and for different PD spacing within clusters (C, shown for clusters of 7 PDs with centre-to-centre distance $d$ as indicated by line type and colour). Cluster sizes 5, 6, and 19 are indicated with blue lines for readability (A,D). For comparison, $f_{i⁢h}$ for non-clustered but randomly distributed PDs is also indicated. (D) The impact of increasing the number of PDs per cluster $p$ on $P⁢(\alpha)$ as a function of cluster density $ρ_{p⁢i⁢t⁢s}$ (the number of pit fields per unit of cell wall area). Lines show the fold increase of $P⁢(\alpha)$ when increasing the number of PDs per cluster from one to the number indicated by the line type (same as in A). Lines are terminated where $f_{i⁢h}$ of clusters meets $f_{i⁢h}$ of isolated PDs at the same total PD density. Beyond that, calculation results are no longer reliable because clusters get too close and the impact of clustering on $f_{i⁢h}$ could be considered negligible. (A-D) Default parameters: $l$ = 100 nm, $d$ = 120 nm, $R_{n}$ = 12 nm.

**Table 1.**
 Pit radius ($R_{p⁢i⁢t}$) as a function of number of PDs per pit.The third and fourth column show numerical values for $d$ = 120 nm and $R_{n}$ = 12.


<table>
  <thead>
    <tr>
      <th>PDs/pit</th>
      <th>Rp⁢i⁢t</th>
      <th>AP⁢D/Ap⁢i⁢t</th>
      <th>Rp⁢i⁢t</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>12</td>
      <td>Rn</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.056</td>
      <td>72</td>
      <td>Rn+12⁢d</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.065</td>
      <td>81.3</td>
      <td>Rn+13⁢3⁢d</td>
    </tr>
    <tr>
      <td>4*</td>
      <td>0.061</td>
      <td>96.9</td>
      <td>Rn+12⁢2⁢d</td>
    </tr>
    <tr>
      <td>5*</td>
      <td>0.041</td>
      <td>132</td>
      <td>Rn+d</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0.038</td>
      <td>150.6</td>
      <td>Rn+23⁢3⁢d</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0.058</td>
      <td>132</td>
      <td>Rn+d</td>
    </tr>
    <tr>
      <td>12</td>
      <td>0.071</td>
      <td>156.2</td>
      <td>Rn+13⁢13⁢d</td>
    </tr>
    <tr>
      <td>19</td>
      <td>0.043</td>
      <td>252</td>
      <td>Rn+2⁢d</td>
    </tr>
  </tbody>
</table>

_*: All entries are based on PDs on a triangular grid within each pit, except for 4 and 5, where the PDs inside a pit are arranged on a square grid. Clusters (pitfields) are always arranged on a triangular grid._

It is hypothesized that PD clustering arises or increases in the process of increasing PD number post cytokinesis, possibly through (repeated) ‘twinning’ of existing PDs (Faulkner et al., 2008). We, therefore, also investigated the effect of increasing the number of PDs per cluster ($p$), starting from 1 PD per cluster (Figure 7D). As expected, $P⁢(\alpha)$ always increased with the increase in cluster size/PD number (Figure 7D), despite the decrease in $f_{i⁢h}$ compared to homogeneously distributed PDs. This increase was larger for larger pit densities (number of pit fields per cell wall area).

In summary, for isolated and roughly evenly distributed PDs, the correction factor $f_{i⁢h}$ for inhomogeneous wall permeability has only a minor role on $P⁢(\alpha)$. For realistic PD dimensions ($R_{n}$ < 20–25 nm), the additional effect of $f_{i⁢h}$ with parameter changes would be too small to be observed experimentally, with the possible exception of PD length $l$. However, when considering clusters of PDs, as is common in pit fields, $f_{i⁢h}$ is markedly reduced, and PD length and density have a much larger impact on $f_{i⁢h}$. We observed the biggest difference between isolated PDs and pairs, that is when going from single to twinned PDs (Figure 7A).

### Application of the model to compute effective permeability for fluorescein derivatives

In a system where non-targeted symplasmic transport is fully driven by diffusion (so no (significant) active transport or hydrodynamic flow), our calculations using reasonable PD dimensions and densities should yield values close to the ones measured experimentally. As a resource to test this hypothesis, we have build a Python program, PDinsight, that computes effective permeabilities from parameter measurements extracted from EM. As some of these parameters might be more reliable than others, we also created a mode in the program to predict what are the minimum requirements in terms of parameter (combination of parameters) values to obtain experimentally measured symplasmic permeability. Exploring these requirements is equivalent to testing hypotheses like: ‘What if PD aperture is larger than observed with EM? or if the molecular radius is smaller than predicted?”. Predictions made with the program can be used to explain experimental results, highlight areas/parameters that need more investigation and can help with the design of new strategies to change effective symplasmic permeability in vivo. For a full description of the program and its possibilities, see Appendix 6.

As a test case, we used the model to explain the permeability measurements in Arabidopsis thaliana roots reported for carboxyfluorescein (CF) diacetate: a membrane permeable non-fluorescent dye that once converted inside cells into a fluorescent version of fluorescein can only move from cell to cell via the PDs (Rutschow et al., 2011). Using a technique named fluorescence recovery after photobleaching (FRAP), CF effective permeability was estimated for transverse walls in the root meristem zone (measured ≈ 200 μm from the quiescent centre). The authors present two experimental setups: a ‘tissue level’ experiment in which a whole ≈ 50 μm longitudinal section of the root was bleached (estimated effective permeability 6–8.5 μm/s) and a single cell experiment in which a single epidermal cell was bleached (estimated effective permeability 3.3 ± 0.8 μm/s).

PD densities in transverse walls of Arabidopsis thaliana roots were reported by Zhu et al. (1998): vascular: 9.92 ± 0.58, inner cortex: 12.28 ± 0.67, outer cortex: 9.08 ± 0.50 and epidermis 5.42 ± 0.42 PDs/μm2. Based on these numbers we assume a PD density of 10–13 PDs/μm2 for the tissue level experiment and 5 PDs/μm2 for the single cell experiment. Fluorescein has a Stokes radius of approximately 0.5 nm (Champion et al., 1995; Corti et al., 2008) and a cytoplasmic diffusion constant of $D$ = 162 μm2/s (one third of its water value) (Rutschow et al., 2011). Feeding these numbers to the model, and considering that PDs appear as straight channels in these walls (Nicolas et al., 2017b), we are able to reproduce the measured permeability values for observed PD densities (Zhu et al., 1998) only if we assume a relatively wide open neck ($R_{n}$ > 15 nm) (Figure 8A,B, Table 2). Notably, the required neck radius for the single cell experiment fits within the range of the tissue level experiment when considering the respectively measured densities. This prediction is plausible if we consider that, in the same tissues, GFP (a protein with a reported hydrodynamic radius of 2.45 nm [Calvert et al., 2007] to 2.82 nm [Terry et al., 1995]) moves intercellularly (Stadler et al., 2005b). Using our default $R_{d⁢t}$, $R_{n}$ should be distinctly wider than 13–14 nm for GFP to move. We also explored the possibility that PD densities are higher than determined by Zhu et al. (1998). We found that to obtain the required effective permeabilities for CF with our default $R_{n}$ = 12 nm, we would need PD densities of 33–47 PDs μm-2 for the tissue level experiment and 19 (14 - 23) PDs μm-2 for the single cell experiment (Table 2). The ratio of these required densities is in line with the observed ratio of relevant densities (Zhu et al., 1998).

![Figure 8.](https://cdn.elifesciences.org/articles/49000/elife-49000-fig8-v3.jpg)

**Figure 8.:** Calculated effective permeabilities for carboxyfluorescein (CF) as a function of PD aperture at the neck $R_{n}$.(A, B) Shows the graphs for straight channels. (A) Effective permeabilities are calculated for different PD densities (different colour curves). The horizontal gray band in A and C indicates the cortical values observed by Rutschow et al. (2011). (B) Shows the PD density required to obtain measured values of $P⁢(C⁢F)$ (different colour curves) as a function of $R_{n}$. Horizontal broken lines are introduced to aid readability. (C, D) Shows that effective permeability increases with dilation of the central region ($R_{c}>R_{n}$). As a reference, values for straight channels are indicated in black. Dashed curves show values calculated for channels without DT. (D) Shows the same calculations as C but for longer PDs $l$ = 200 nm. Default parameters: $\alpha$ = 0.5 nm, $D$ = 162 μm2/s, $l_{n}$ = 25 nm, $l$ = 100 nm, $R_{dt}$ = 8 nm, $ρ$ = 10 PD/μm2, PDs are spaced on a triangular grid, without clustering.

**Table 2.**
 Parameter requirements for reproducing measured $P⁢(C⁢F)$ values (Rutschow et al., 2011) with the default model.This table was generated using PDinsight. A: Required density ($ρ$) for a given $\alpha¯$ and neck radius ($R_{n}$). B: Required $\alpha¯$ and corresponding $R_{n}$ for a given $ρ$. C: values required to reproduce $P(CF)$ = 25 μm/s. Values computed for a 2x, 3x and 4x increase of $ρ$ are also shown. This is done both for a uniform increase of the density ($p=1$) and for (repeated) twinning ($p>1$) from a uniform starting density (indicated in bold). $p$ is the number of PDs per pit.


<table>
  <tbody>
    <tr>
      <td>A P⁢(C⁢F)(μm/s)</td>
      <td colspan="2">α¯ (nm)</td>
      <td>Rn (nm)</td>
      <td>ρ (PD/μm2)</td>
    </tr>
    <tr>
      <td>3.3*</td>
      <td colspan="2">2.0</td>
      <td>12</td>
      <td>18.6</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">2.5</td>
      <td>13</td>
      <td>12.6</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.0</td>
      <td>14</td>
      <td>9.3</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.4</td>
      <td>14.8</td>
      <td>7.6</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.5</td>
      <td>15</td>
      <td>7.3</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">4.0</td>
      <td>16</td>
      <td>5.9</td>
    </tr>
    <tr>
      <td>6</td>
      <td colspan="2">2.0</td>
      <td>12</td>
      <td>33.5</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">2.5</td>
      <td>13</td>
      <td>22.7</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.0</td>
      <td>14</td>
      <td>16.8</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.4</td>
      <td>14.8</td>
      <td>13.8</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.5</td>
      <td>15</td>
      <td>13.2</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">4.0</td>
      <td>16</td>
      <td>10.7</td>
    </tr>
    <tr>
      <td>8.5</td>
      <td colspan="2">2.0</td>
      <td>12</td>
      <td>47.2</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">2.5</td>
      <td>13</td>
      <td>32.0</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.0</td>
      <td>14</td>
      <td>23.7</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.4</td>
      <td>14.8</td>
      <td>19.4</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">3.5</td>
      <td>15</td>
      <td>18.5</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">4.0</td>
      <td>16</td>
      <td>15.0</td>
    </tr>
    <tr>
      <td>B P⁢(C⁢F)(μm/s)</td>
      <td colspan="2">ρ</td>
      <td>α¯</td>
      <td>Rn (nm)</td>
    </tr>
    <tr>
      <td>3.3*</td>
      <td colspan="2">5</td>
      <td>4.5</td>
      <td>16.9</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td>4.2</td>
      <td>16.5</td>
      <td></td>
    </tr>
    <tr>
      <td>6</td>
      <td colspan="2">10</td>
      <td>4.2</td>
      <td>16.3</td>
    </tr>
    <tr>
      <td colspan="2">13</td>
      <td>3.5</td>
      <td>15.1</td>
      <td></td>
    </tr>
    <tr>
      <td>8.5</td>
      <td colspan="2">10</td>
      <td>5.2</td>
      <td>18.4</td>
    </tr>
    <tr>
      <td colspan="2">13</td>
      <td>4.4</td>
      <td>16.8</td>
      <td></td>
    </tr>
    <tr>
      <td>1</td>
      <td colspan="2">10</td>
      <td>1.5</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td colspan="2">13</td>
      <td>1.3</td>
      <td>10.6</td>
      <td></td>
    </tr>
    <tr>
      <td>C P⁢(C⁢F)(μm/s)</td>
      <td>ρ</td>
      <td>p</td>
      <td>α¯</td>
      <td>Rn (nm)</td>
    </tr>
    <tr>
      <td>25</td>
      <td>10</td>
      <td>1</td>
      <td>10.5</td>
      <td>28.9</td>
    </tr>
    <tr>
      <td></td>
      <td>20</td>
      <td>1</td>
      <td>6.6</td>
      <td>21.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2</td>
      <td>7.2</td>
      <td>22.5</td>
    </tr>
    <tr>
      <td></td>
      <td>30</td>
      <td>1</td>
      <td>5.1</td>
      <td>18.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3</td>
      <td>5.6</td>
      <td>19.2</td>
    </tr>
    <tr>
      <td></td>
      <td>40</td>
      <td>1</td>
      <td>4.2</td>
      <td>16.4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4</td>
      <td>4.6</td>
      <td>17.2</td>
    </tr>
    <tr>
      <td></td>
      <td>13</td>
      <td>1</td>
      <td>8.8</td>
      <td>25.6</td>
    </tr>
    <tr>
      <td></td>
      <td>26</td>
      <td>1</td>
      <td>5.6</td>
      <td>19.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2</td>
      <td>6.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <td></td>
      <td>39</td>
      <td>1</td>
      <td>4.3</td>
      <td>16.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3</td>
      <td>4.6</td>
      <td>17.2</td>
    </tr>
    <tr>
      <td></td>
      <td>52</td>
      <td>1</td>
      <td>3.6</td>
      <td>15.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4</td>
      <td>3.8</td>
      <td>15.5</td>
    </tr>
  </tbody>
</table>

_*: Single cell experiment. All other data relates to tissue level experiments._

Using the model, we also explored the effect of ‘necked’/‘dilated’ PDs by adding a wider central region to PDs. For a central radius $R_{c}$ = 17.6 nm, the required $R_{n}$ to reproduce the tissue level CF permeability values would decrease by perhaps 1 nm or at most 3 nm (for $R_{c}$ = 26.4 nm) considering a PD density in the order of $ρ$ = 10 μm–2 (Figure 8C, $R_{c}$ values from Nicolas et al., 2017b). In thicker cell walls (Figure 8D), the calculated effective permeabilities increased relatively more, but remained too low, suggesting that increasing cavity radius is never sufficient for reproducing the Rutschow et al. (2011) values (see also Figure 4).

Using the tissue level setup, Rutschow et al. also reported drastic changes in effective permeability after H2O2 treatment. They found a strong decrease in symplasmic permeability to ≈ 1μm/s after treatment with a ‘high’ H2O2 concentration, which was explained by rapid PD closure through callose deposition. Using our program we found that, for this reduction of $P⁢(C⁢F)$, callose must reduce $R_{n}$ to 11 nm ($ρ$ = 10 μm–2) or 10.6 nm ($ρ$ = 13 μm–2), resulting in $\alpha¯$ = 1.5 nm or 1.3 nm, respectively. The authors also found a strong increase in permeability to ≈ 25 μm/s after treatment with a ‘low’ H2O2 concentration. Reproducing this increase requires a large change at the PD level. At the extremes, an increase of $R_{n}$ to approximately 29 nm for $ρ$ = 10 μm–2 (Figure 8A,B, Table 2B), or a slightly more than four fold increase in PD density would be required to reproduce this high effective permeability (Table 2C). Alternatively, both $R_{n}$ and $ρ$ would have to increase substantially (Figure 8B). As an extreme hypothesis, we also calculated the effects of complete DT removal. The increases in $P⁢(\alpha)$ that could be obtained this way were by far insufficient to explain the reported effect of mild H2O2 treatment (Figure 8C,D), making DT modification or removal a highly unlikely explanation for this change.

Taken together, these calculations indicate that our model for diffusive symplasmic transport can indeed explain experimentally observed measurements of effective symplasmic permeability, but only with somewhat wider PDs/neck regions than expected yet in line with the observed permeability for GFP and within the range of PD diameters measured in thick cell walls. Alternatively, similar changes in symplasmic permeability can be achieved with several fold higher densities than typically measured. These predictions provide a framework for experimental validation. We also compared the results obtained with our unobstructed sleeve model and the sub-nano channel architecture. Using the sub-nanochannel architecture, much larger PD densities would be required to achieve the same $P⁢(C⁢F)$: roughly twice as large for $\alpha¯$ = 3.5–4 nm and even larger for smaller $\alpha¯$ (see Appendix 5 and Appendix 5—table 1). These results favour unobstructed sleeve models for offering more plausible hypotheses to explain the experimental results for CF and the impact of H2O2 treatment on effective permeability.

## Discussion

In this manuscript, we presented a method for calculating effective wall permeabilities for non-targeted, diffusive symplasmic transport based on the dimensions and distribution of PDs and on the size of the mobile particles. For individual PDs, we used a minimal geometrical description that allowed us to extensively investigate the effects of dilation of the central PD region and the implications of a DT at the PD axis on transport properties. Because PDs are narrow, our calculated effective symplasmic permeabilities were heavily affected by molecular hindrance effects. For the effects of PD distribution, we introduced an ‘inhomogeneity factor’ $f_{i⁢h}$ between 0 and 1, which accounts for the reduction in overall permeability due to spatial arrangement of PDs. We found that the degree of PD clustering had a strong impact on this factor, whereas the exact spatial distribution of either isolated PDs or clusters had little impact.

Our model uses an unobstructed cytosolic sleeve for symplasmic transport. In such models, the DT gives the PD an annular cross section, which strongly increases transport capacity compared to cylindrical channels with the same $\alpha¯$ and total cross section area at the entrance, particularly for relatively large molecules. Having a DT offers an additional flexibility in regulating size selectivity through the possibility of a dilated state of the PD by displacement or temporal removal of the DT (Zambryski and Crawford, 2000; Crawford and Zambryski, 2000). This feature, however, can be exploited for the spreading of viruses (Benitez-Alfonso et al., 2010) and other intracellular parasites such as the fungus Magnaporthe oryzae (Kankanala et al., 2007). Functional PDs without DT (and inner diameter of 10–20 nm) have been reported for the brown algae species Dictyota dichotoma (Terauchi et al., 2012). Due to their very high membrane curvature, DT formation requires curvature-inducing proteins (such as reticulons) and a special lipid composition (Tilsner et al., 2011; Grison et al., 2015; Knox et al., 2015). It is likely that performance benefits of the DT offset these costs and disadvantages and it is therefore under evolutionary selection. Additionally, the connection between DT and ER could result in variable degrees of PD occlusion and hence a potential control mechanism for PD accessibility. Park et al. (2019) have started to explore this concept in the context of pressure regulated PD occlusion.

We have also calculated the performance costs (transport rate) and benefits (transport volume per PD) of having distinct central and neck regions. Whereas the transport time scales quadratically with the radius of the central region ($R_{c}$), the relative transport volume has a strong upper bound that increases with channel length. These results suggest that straight PDs perform better in thin (average 100 nm) cell walls and necked/dilated PDs in thick (average 200 nm or more) cell walls, which correlates with recent observations (Nicolas et al., 2017b). This is not, however, the only way to explain these observations. Necked/dilated PDs might appear because (1) size selectivity is more efficiently controlled by restricting callose deposition to a 20–30 nm long neck region, (2) the formation of ‘spokes’ in the central region leads to this narrow-wide-narrow structure, and/or (3) the material properties of cellulosic cell walls and PD cell membranes only allow for a distinctly wider central region if the channel is long enough.

In our model, we naturally define the SEL as $\alpha¯$, the maximum particle radius that could fit through the model PD, but experimental determination of this value is difficult and often relies on the transport of detectable, typically fluorescent, molecules such as CF. The limited set of suitable molecules, particularly for non-invasive techniques, introduces a large uncertainty in SEL measurements and hence $\alpha¯$. Also other biological factors could lead to an underestimation as well as an overestimation of $\alpha¯$. For example, in so-called active symplasmic phloem loaders, such as the cucurbits, sucrose moves symplasmically from bundle sheet cells (BSC) to intermediary cells (IC), where it is polymerized into the larger oligomers raffinose and stachyose, that do not diffuse back in detectable amounts (Haritatos et al., 1996; Liesche and Patrick, 2017). Two explanations have been suggested: (1) a discriminating PD SEL at this interface, which prevents the back transport of raffinose and stachyose (Liesche and Schulz, 2013), or (2) open PDs combined with a directional flow which could be sustained by the xylem flow (Comtet et al., 2017). Only the latter could explain the observed amount of sucrose transport (Liesche and Schulz, 2013; Comtet et al., 2017). This example illustrates that the consideration of a symplasmic flow could largely affect calculated permeabilities and fluxes.

An overestimation of $\alpha¯$ could occur for non-spherical molecules or temporal variations in PD properties. Although a molecule’s hydrodynamic radius is a better predictor of its symplasmic transport efficiency than its molecular weight (Terry and Robards, 1987; Dashevskaya et al., 2008), it conceptually assumes a static replacement sphere. Molecules may be more flexible and/or have a shortest dimension than what is captured by its diffusive behaviour in bulk. PDs might also accommodate molecules that are larger than expected, either through interactions with specific PD proteins (Benitez-Alfonso et al., 2010) or because membranes and/or cell wall domains around PDs allow for reversible transient modifications in $\alpha¯$ (Abou-Saleh et al., 2018). Additionally, molecules could pass in the wake of larger proteins/complexes/structures that modify PDs (e.g., tubule-forming viruses; Amari et al., 2010). Assessing the extent and time scales of temporal variations in PD boundaries and their implications remains an open topic for future investigation.

The framework we have developed for so-called ‘simple’ PDs also provides an intuition for the functional implications of complex geometries such as ‘twinned’, ‘branched’ or ‘funnel’ PDs (Ehlers and Kollmann, 2001; Ehlers and van Bel, 2010; Faulkner et al., 2008; Ross-Elliott et al., 2017). All else remaining equal, ‘twinned’ PDs have twice the entrance surface area, which would result in doubling the effective permeability $P⁢(\alpha)$. This increase, however, will be reduced because of the less uniform PD spacing in a density dependent manner (Figure 7A). ‘Branched’ or ‘complex’ PDs contain multiple sub-channels (branches) on at least one side with typically a single shared central cavity connecting all branches (Oparka et al., 1999; Roberts et al., 2001; Fitzgibbon et al., 2013). In the leaf sink/source transition, massive branching is observed and, coincidentally, the number of PDs is reduced (Roberts et al., 2001). The formation of many channels per PD could help to maintain sufficient transport capacity for smaller molecules. If so, the increase in the number of typically narrower channels should be much larger than the decrease in total (simple or complex) PD number. Our computations of $f_{i⁢h}$ after twinning suggest that minimizing the distance between sub-channels could be favourable at low to moderate PD densities (Figure 7C). ‘Funnel’ PDs are reported in tissues surrounding the phloem at the root unloading zone (Ross-Elliott et al., 2017) and show a wide opening on the PSE (protophloem sieve element) side and a narrow opening on the PPP (phloem pole pericycle) side. (Ross-Elliott et al., 2017) model these as a triangular funnel that reaches its narrowest diameter only at the (PPP) bottom. There appears to be, however, a longer neck-like region at the narrow end of variable length. As hindrance is by far the highest in the narrowest section, the length of this narrow part would be a vital parameter in correctly estimating the transport permeabilities of these PDs.

We have applied our model to calculate the effective permeability for fluorescein in transverse walls of Arabidopsis root tip cells (Rutschow et al., 2011). Assuming purely diffusive transport and parameters based on various ultrastructural measurements, we were able to reproduce the observed effective permeabilities for CF and to assess the plausibility of different hypotheses aimed at resolving the conundrum of apparently incompatible measurements at different scales. For resolving this conundrum, we assumed that not all PD dimensions are reliably measured with EM. We could reproduce the measured values with somewhat wider PDs/neck regions or several fold higher PD densities than usually measured by EM. Of these, the increased radius seems the more plausible scenario, in line with the requirements for efficient GFP transport reported to occur among root meristem cells (Benitez-Alfonso et al., 2009; Benitez-Alfonso et al., 2013; Nicolas et al., 2017b), and similar to $R_{c}$ values reported in thicker cell walls (Zhu et al., 1998; Grison et al., 2015; Nicolas et al., 2017b). Remarkably, our model predicts very similar PD aperture in the transverse walls of the epidermis and the more interior root layers when considering the ≈ 2-fold difference in PD density (Zhu et al., 1998). The obvious next step would be testing more data sets of different interfaces/plant species where purely diffusive symplasmic transport is expected. First of all, it would be ideal to test if a near or complete match between tissue level and ultrastructural measurements can be produced if all measurements are performed on the same system with the same growth/treatment conditions. Additionally, more testing could yield a better understanding of potential systematic side-effects of modern EM preparation techniques and/or uncertainties in the tissue level measurements, which would show as systematic vs random required adjustments of the model parameters. A very exciting outcome would be the discovery of distinct clusters in required parameter adjustments that could be related to cell wall properties, PD or interface type, etc. Additional model testing would become easier if the results of tissue level experiments are reported in the form of effective symplasmic wall permeabilities (in μm/s), or clearly provide all information required to transform into such units.

We also used our model to predict the PD changes after treatment with high and low concentrations of H2O2 in Rutschow et al. (2011). The reduced permeability after high H2O2 treatment could easily be explained by a redox induced stress response and corresponding reduction of PD aperture (e.g., at a density of 10 PD/μm2, a reduction from $\alpha¯$ = 4.2–5.2 nm to $\alpha¯$ = 1.5 nm would be required, see Table 2B). The strongly increased permeability after low H2O2 treatment, however, is harder to explain. With a single parameter change, the model predicts either a very wide PD aperture of $\alpha¯$ = 8.8–10.5 nm, or a ±4-fold increase in PD density (possibly through 2 rounds of twinning/duplication), or less extreme changes if both parameters increase simultaneously (see Table 2C). The required increase in PD density should occur relatively fast, that is within the applied incubation period of 2 hr, and is so large that it should be readily detectable with EM.

The fact is that to reproduce experimentally measured CF effective permeabilities with our model, we had to deviate from ultrastructural based values for at least one parameter. Potential sources for these variations are: (1) ultrastructural studies might underestimate $R_{n}$ because plants could respond to pre-EM manipulation by closing PDs, like they do in response to microinjection or particle bombardment (Haywood et al., 2002; Liesche and Schulz, 2012), (2) PD integrity could be affected during processing for TEM leading to an underestimation of PD densities, (3) the mechanical properties of cell walls and membranes provide a flexibility in the channel that could to some degree accommodate molecules larger than the apparent $R_{n}$ (Abou-Saleh et al., 2018; Yan et al., 2019; Amsbury and Benitez-Alfonso, 2019). For a passive transport mechanism, the elastic energy required for these reversible deformations would have to be in the order of a few $k_{B}⁢T$ or less. A model with flexible PD lining would be required to investigate the physical limits of this ‘flexibility hypothesis’, which is quite an increase in model complexity compared to the hard walls used in all current models, including ours. Finally, technical issues limit the accuracy of the CF effective permeability measurements themselves, for example, the speed of confocal microscopy bounds the spatial and temporal resolution at which CF concentrations can be monitored during and after bleaching/photoactivation (Rutschow et al., 2011; Liesche and Schulz, 2012).

To assess the impact on effective symplasmic permeability of various PD distributions, including clustering into pit fields, we introduced the inhomogeneity factor $f_{i⁢h}$ that accounts for the fact that the wall is only permeable at certain spots (i.e., where the PDs are located). Clustering into pit fields had by far the largest impact on this factor, particularly for lower PD densities. This means that not only total PD density, but also the degree of clustering is important information for calculating effective wall permeability from experimental data. The above inhomogeneity factor and the possibility of a dilated central region set our model apart from other models based on the unobstructed sleeve architecture (Bret-Harte and Silk, 1994; Liesche and Schulz, 2013; Dölger et al., 2014; Ross-Elliott et al., 2017). Using typical PD dimensions and no clustering, inhomogeneity factor $f_{i⁢h}$ would reduce the effective symplasmic permeability by about 15%, meaning that our model would require slightly wider or more PDs to explain the same tissue level experiments with straight channels compared to the above models.

A dilated central region is also considered in Blake (1978), who investigates hydrodynamic flow only. There is, however, an interesting similarity between both conditions: in both cases the driving gradient is steepest in the (narrowest part of) the neck region, be it the concentration gradient (Appendix 2—figure 2A) or the pressure gradient (Blake, 1978). When it comes to describing the PD geometry, (Blake, 1978), makes the opposite choice compared to us. He glues together sin2 functions with a straight middle part, resulting in a mathematically nice (i.e., continuous differentiable) function, but consequently, neck shape cannot be controlled, and neck length and the length of the widening region are linked. We, on the other hand, use an instantaneous increase in PD radius, which introduces a mild systematic error in our estimates of effective symplasmic permeability $P⁢(\alpha)$ (Appendix 2), but results in parameters that are directly measurable on EM images.

Comparing the unobstructed sleeve architecture to the sub-nano channel architecture, we found that the latter requires roughly twice as high PD densities to produce the same permeability values $P⁢(C⁢F)$ in the (Rutschow et al., 2011) experiments. This difference is due to the increased hindrance effects in cylindrical channels vs annular channels with the same cross sectional area. In the future, sleeve models could be refined with the consideration of central spokes (Ding et al., 1992; Nicolas et al., 2017b) and variability of PD dimensions within a single cell wall (Nicolas et al., 2017b; Yan et al., 2019). Simple considerations of the available volume suggest that the addition of spokes will increase hindrance effects, but most likely to a lesser extend than the sub-nano channel structure. Detailed molecular simulations could be a valuable tool to assess this effect.

Other future applications could be the coupling of our detailed PD level calculations of effective symplasmic permeability with tissue level models, which would allow for investigating the impact of microscopic changes on developmental and physiological processes (for example see Foster and Miklavcic, 2017; Couvreur et al., 2018). Depending on the context, it would then be useful or even required to also implement hydrodynamic flow through the PDs. Many ingredients are available for doing this while maintaining the distinguishing features of our mode, including hindrance factors (Dechadilok and Deen, 2006), but as far as we know, the theoretical and numerical results that we use for calculating $f_{i⁢h}$ are only available for diffusion processes, and not yet for advection. Additionally, one may need to replace the abrupt change in PD radius by a more gradual function. The importance of this final change could be estimated using numerical simulations.

Technological advances have started to be applied for more refined determinations on ultrastructural parameters. New fixation and sectioning techniques and new technologies such as electron-tomography (ET) and Correlative Fluorescence Electron Microscopy (CFEM) are now part of the systematic study of PD connections in different plant cells, tissues and organs. In parallel, new information on structural features characterizing PDs in different plant species/developmental stages as well as on the factors controlling PD structure and function (and thereby the effective permeability of specific molecules in different developmental or environmental conditions) are emerging. Combined with this significant experimental progress, our calculations provide a functional interpretation to characteristic PD morphological features and provide a framework to investigate how transport properties depend on these ultrastructural features and particle size in the context of simple and complex PD geometries. Another level of predictive power could be unlocked by integrating our framework into larger models at the tissue to whole organism level. This opens new avenues for exploring how developmental regulation of symplasmic transport interacts with various other pathways for long and short range intercellular communication.

## Materials and methods

### Diffusive flux through a single PD

Similar to Smith (1986), we assumed the flux is distributed homogeneously within each cross section along the axis of the channel. This results in a simple mapping to a 1D channel, that is that the average local flux (per unit area of cross section) ∼ 1/available cross section surface. This assumption does not hold close to the transition between neck and central region, that is a sharp transition between narrow and wide cylinders. Numerical simulations showed, however, that the error introduced by the assumption of homogeneous flux turned out to less than 4 percent for $l$ = 200 nm, the shortest $l$ with experimentally observed neck region in Nicolas et al. (2017b) (Appendix 2—figure 1) and will be less for longer channels. This error can be considered irrelevant given the quality of available data on PD dimensions and the many molecular aspects of PD functioning that are necessarily neglected in a simple model.

### Hindrance factors

Hindrance factors $H⁢(\lambda)$ including both steric and hydrodynamic effects are modelled using the numerical approximations in Dechadilok and Deen (2006). They present functions for cylindrical and slit pores. For PDs with a desmotubule, we use the function calculated for straight slits.

$$
H(\lambda)=1+\frac{9}{16}\lambdaln⁡(\lambda)−1.19358\lambda+0.4285\lambda^{3}−0.3192\lambda^{4}+0.08428\lambda^{5}.
$$

This choice is supported by the steric hindrance prefactor that is included in $H⁢(\lambda)$ (Dechadilok and Deen, 2006). This $Φ⁢(\lambda)=1-\lambda$ is the same as the ratio of available to full surface area $A~_{x}⁢(\alpha)/A_{x}$. For cylindrical channels, that is reference channels in Figure 5 and the regular PDs after DT removal, we use

$$
H_{c}(\lambda)=1+\frac{9}{8}\lambdalog⁡(\lambda)−1.56034\lambda+0.528155\lambda^{2}+1.91521\lambda^{3}−2.81903\lambda^{4}+0.270788\lambda^{5}+1.10115\lambda^{6}−0.435933\lambda^{7}
$$

for $\lambda<0.95$ and the asymptotic approximation by Mavrovouniotis and Brenner (1988),

$$
H_{c}(\lambda)=(1-\lambda)^{2}⋅(0.984(\frac{1-\lambda}{\lambda})^{\frac{5}{2}}
$$

otherwise, as suggested by Dechadilok and Deen (2006).

### Relative molar flow rate and MRT

For assessing the impact of the neck constriction on PD transport, we defined two relative quantities: $Q_{r⁢e⁢l}=Q_{d⁢i⁢l⁢a⁢t⁢e⁢d}/Q_{n⁢a⁢r⁢r⁢o⁢w}$ and $\tau_{r⁢e⁢l}=\tau_{d⁢i⁢l⁢a⁢t⁢e⁢d}/\tau_{n⁢a⁢r⁢r⁢o⁢w}$ (Figure 4, Appendix 3—figure 1). Using Equation 2 for $Q⁢(\alpha)$, $Q_{r⁢e⁢l}$ is well defined:

$$
Q_{rel}(\alpha,R_{c})=\frac{lA~~_{c}}{2(l~_{n})A~~_{c}+(l−2l~_{n})A~~_{n}}
$$



$$
limR_{c}→∞Q_{rel}(\alpha,R_{c})=\frac{l}{2l~_{n}}
$$

For $\tau_{r⁢e⁢l}$ we first needed an expression for $\tau$ itself. Ideally, this would be a MFPT, which could calculated in a way similar to $\tau_{∥}$ in the calculation of $f_{i⁢h}$, using a narrow-wide-narrow setup. These calculations, however, critically depend on trapping rates at the narrow-wide transitions. We do not have an expression for these, because the DT takes up the central space of the channel, which, contrary to the case of $f_{i⁢h}$, substantially alters the problem and the circular trap based calculations would result in an underestimation of the MFPT. Instead, we stuck to the homogeneous flux assumption also used for $Q⁢(\alpha)$ and defined $\tau$ as the corresponding estimate for the mean residence time (MRT) in the channel (see Equation 5). Elaborating Equation 5:

$$
(13)\tau(\alpha)=\frac{C_{l}+C_{0}}{2DΔC}\frac{(2l~_{n}A~~_{n}+(l−2l~_{n})A~~_{c})(2l~_{n}A~~_{c}+(l−2l~_{n})A~~_{n})}{A~~_{n}A~~_{c}}(14)=\frac{C_{l}+C_{0}}{2DΔC}(4l~_{n}^{2}+(l−2l~_{n})^{2}+2l~_{n}(l−2l~_{n})(\frac{A~~_{c}}{A~~_{n}}+\frac{A~~_{n}}{A~~_{c}})).
$$

Unfortunately, this depends on the concentration difference over the channel. We are interested, however, in how the MRT changes with increasing $R_{c}$. In our definition of $\tau_{r⁢e⁢l}$, the concentration difference cancels from the equation, solving the problem:

$$
\tau_{rel}(\alpha,R_{c})=\frac{1}{l^{2}}(4l~_{n}^{2}+(l−2l~_{n})^{2}+2l~_{n}(l−2l~_{n})(\frac{A~~_{c}}{A~~_{n}}+\frac{A~~_{n}}{A~~_{c}})).
$$

This method of computing $\tau_{r⁢e⁢l}$ again depends on the homogeneous flux assumption. For an estimate of the error introduced by this approach, see Appendix 2.

### Flow towards PDs: correction for inhomogeneity of the wall permeability

To compute $f_{i⁢h}$, we consider a linear chain of cells that are symplasmically connected over their transverse walls (Figure 1). We first compute mean first passage time (MFPT) $\tau_{∥}$ through a simplified PD and a column of cytoplasm surrounding it. We then convert $\tau_{∥}$ to an effective wall permeability and compare the result with the uncorrected effected permeability computed using Equation 6 for the simplified PD geometry and $f_{i⁢h}=1$.

As a simplified PD, we use a narrow cylindrical channel of length $l$ and radius $R_{n}$, that is initially without DT. We assume that PDs are regularly spaced on a triangular grid. Consequently, the domain of cytoplasm belonging to each PD is a hexagonal column of length $L$, the length of the cell (Figure 6). We adjust the results reported by Makhnovskii et al. (2010) for cylindrical tubes with alternating diameter by changing the wide cylinder of radius $R_{w}$ with a hexagonal column with cross section area $A_{w}=1/ρ$ and considering hindrance effects. Makhnovskii et al. use a setup with an absorbing plane in the middle of a wide section and a reflecting plane, where also the initial source is located, in the middle of the next wide section. Assuming equal diffusion constants in both sections, they report the following MFPT from plane to plane:

$$
\tau_{∥}=\frac{1}{2⁢D}⁢[L^{2}+l^{2}+2⁢D⁢(\frac{l}{κ_{n}}+\frac{L}{κ_{w}})+l⁢L⁢(\frac{κ_{w}}{κ_{n}}+\frac{κ_{n}}{κ_{w}})],
$$

where

$$
κ_{w}=\frac{4⁢D⁢R_{n}⁢f⁢(\frac{R_{n}^{2}}{R_{w}^{2}})}{\pi⁢R_{w}^{2}}
$$

is a trapping rate to map the 3D setup onto a 1D diffusion problem. In this,

$$
f⁢(\sigma)=\frac{1+A⁢\sqrt{\sigma}-B⁢\sigma^{2}}{(1-\sigma)^{2}}
$$

is a function that monotonically increases from 0 to infinity as $\sigma$, the fraction of the wall occupied by the circular PDs, increases from 0 to 1. $f⁢(\sigma)$ is the result of a computer assisted boundary homogenization procedure with the values of $A$ and $B$ depending on the arrangement of trapping patches (Berezhkovskii et al., 2006). To maintain detailed balance, the corresponding trapping rate $κ_{n}$ must satisfy $A_{w}⁢κ_{w}=A_{n}⁢κ_{n}$, with $A_{x}$ the respective cross section areas of both tubes.

As PDs are very narrow, we must take into account that only part of the cross section surface inside the PD is available to a particle of size $\alpha$. Additionally, a subtle problem lies in the determination of $R_{w}$, as it is impossible to create a space filling packing with cylinders. To solve both issues, we rewrite Equation 16 to explicitly contain cross section surfaces. We then replace $A_{n}$ with $A~~_{n}$ to accommodate hindrance effects and we replace $A_{w}$ by $1/ρ$. We also ajust PD length: $l~=l+2⁢\alpha$ and $L=L-2⁢\alpha$. At the same time, we adjust $f⁢(\sigma)$ to match a triangular distribution of the simplified PDs by using $A=1.62$ and $B=1.36$ (Berezhkovskii et al., 2006), which produces the hexagonal cytoplasmic column shape. This yields:

$$
\tau_{∥}=\frac{1}{2⁢D}⁢[L~^{2}+l~^{2}+2⁢D⁢(\frac{l~}{κ_{n}}+\frac{L~}{κ_{w}})+l~⁢L~⁢(A~~_{n}⁢ρ+\frac{1}{A~~_{n}⁢ρ})].
$$

We similarly adjust $κ_{w}$:

$$
κ_{w}=4⁢ρ⁢D⁢H_{c}⁢(\alpha/R_{n})⁢R_{n}⁢f⁢(ρ⁢A~_{n}),
$$

where $H_{c}⁢(\lambda)$ is the hindrance factor for cylindrical pores (see Materials and methods). In the same fashion, we also adjust $κ_{n}$.

We then invert the relation $\tau_{∥}=\frac{L^{2}}{2⁢D}+\frac{L}{2⁢P_{e⁢f⁢f}}$, where we write $P_{e⁢f⁢f}$ for the effective wall permeability (Makhnovskii et al., 2009), to obtain $P_{e⁢f⁢f}=\frac{L}{2⁢\tau_{∥}-L^{2}/D}$. With this, we can compute $f_{i⁢h}=P_{e⁢f⁢f}/(ρ⁢Π⁢(\alpha))$, where $Π⁢(\alpha)$ is calculated using the same PD geometry. To validate the choice of boundary placement underlying the calculations above, we also calculated the MFPT over two PD passages, that is by shifting the reflecting boundary to the middle of one cell further. This resulted in a 4-fold increase of $\tau_{∥}$ and $L^{2}$ and hence in exactly the same $P_{e⁢f⁢f}$.

To assess whether the desmotubule has a large impact on $f_{i⁢h}$, we further adapt Equation 19 by replacing $A~~_{n}$ by our desmotubule corrected $A~~_{n}$, except in $f⁢(\sigma)$. Additionally, we multiply $f⁢(\sigma)$ by $ξ=(R~_{n}^{2}-R~_{d⁢t}^{2})/R~_{n}^{2}$. Numerical calculations in a simple trapping setup confirm the validity of reducing $f⁢(\sigma)$ proportional to the area occupied by the desmotubule whilst calculating $\sigma$ based on the outer radius alone (Appendix 4—figure 1 and Appendix 4). This is in agreement with results for diffusion towards clusters of traps in 3D (Makhnovskii et al., 2000). By the same reasoning, we introduced a hindrance factor in $κ_{w}$. Finally, we adjust the hindrance factors to a slit geometry as before. This results in:

$$
\tau_{∥}=\frac{1}{2⁢D}⁢[L~^{2}+l~^{2}+\frac{L~/ρ+l~⁢A~~_{n}}{2⁢R_{n}⁢H⁢(2⁢\alpha/(R_{n}-R_{d⁢t}))⁢ξ⁢f⁢(ρ⁢A~_{n})}+l~⁢L~⁢(A~~_{n}⁢ρ+\frac{1}{A~~_{n}⁢ρ})].
$$

To investigate the effect of different PD distributions, we used all relevant pairs of $A$ and $B$ in $f⁢(\sigma)$ for different regular trap distributions as given in Berezhkovskii et al. (2006). As $A_{w}$ is calculated implicitly from $1/ρ$, no other adjustments were necessary.

### Correction factor fi⁢h for pit fields

For computing $f_{i⁢h}$ in pit fields, we used a two step approach similar to computing $f_{i⁢h}$ including DT as described above. A similar approach is also followed for the sub-nano channel model. In this calculation, a single pit field is modelled as a number of PDs on a triangular (or square) grid with a centre-to-centre distance $d$ between nearest neighbours. We then calculate the pit radius, $R_{p⁢i⁢t}$ as the radius of the circle that fits the outer edges of the PD entrances. In the trivial case of one PD per ‘pit’, $R_{p⁢i⁢t}=R_{n}$. For larger numbers of PDs per pit, see Table 1. For this calculation, individual PDs are modelled as straight cylindrical PDs with radius $R_{n}$. We calculate a $\tau_{∥}$ based on circular traps with radius $R_{p⁢i⁢t}$ and a reduced efficiency based on the fraction of the pit that is occupied by the circular PDs. We accordingly adjust $κ_{w,p⁢i⁢t}$ and $\tau_{∥,pit}$:

$$
κ_{w,p⁢i⁢t}=4⁢ρ⁢D⁢H_{c}⁢(\alpha/R_{p⁢i⁢t})⁢R_{p⁢i⁢t}⁢ξ⁢f⁢(ρ⁢\pi⁢R~_{p⁢i⁢t}^{2}),
$$

where $p$ is the number of PDs per pit and $ξ=p⁢R~_{n}^{2}/R~_{p⁢i⁢t}^{2}$ is the fraction of available pit area that is occupied by available PD area, and

$$
\tau_{∥}=\frac{1}{2⁢D}⁢[L~^{2}+l~^{2}+\frac{L~/ρ+l~⁢p⁢A~~_{n}}{2⁢R_{p⁢i⁢t}⁢H⁢(\alpha/R_{p⁢i⁢t})⁢ξ⁢f⁢(ρ⁢A~_{p⁢i⁢t})}+l~⁢L~⁢(p⁢A~~_{n}⁢ρ+\frac{1}{p⁢A~~_{n}⁢ρ})].
$$

In these equations, $ρ$ is the total PD density. In our graphs, we either keep $ρ$ constant while increasing $p$ to investigate the effect of clustering, resulting in a pit density $ρ_{p⁢i⁢t⁢s}$ of $ρ/p$, or keep $ρ_{p⁢i⁢t⁢s}$ constant to investigate the effect of (repeated) PD twinning. As a default, we used $d$ = 120 nm based on distances measured from pictures in Faulkner et al. (2008) of basal cell walls of Nicotinia tabacum leaf trichomes. To verify our calculations, we compared them with a single step calculation with large circles only, that is with radius $R_{p⁢i⁢t}$ and density $ρ/p$. As results in 3D suggest that for strongly absorbing clusters, the outer radius and cluster density dominate the diffusion (survival time) process (Makhnovskii et al., 2000), this should produce a lower bound to $f_{i⁢h}$. In terms of PDs, this regime applies if a particle that reaches a pit field also has a high probability of entering in it. Indeed, the values calculated with the two step method above were similar and somewhat larger than with the simple large patch method, showing that our computation method is reasonable.

Only a relatively small fraction of the pits is occupied by the PD entrances (5–10% when modelled as circles with $R_{n}$ = 14 nm and 3–7% with $R_{n}$ = 12 nm.). Consequently, this approach may become inaccurate when $R_{p⁢i⁢t}$ gets too large. We indeed found instances where $f_{i⁢h,p⁢i⁢t⁢s}$ was larger than $f_{i⁢h,s⁢i⁢n⁢g⁢l⁢e⁢P⁢D⁢s}$. In those cases, $R_{p⁢i⁢t}$ was in the order of $d_{p⁢i⁢t}/4$ or larger. We assume that in those cases, the clusters are so close, that the clustering has only minor impact on $f_{i⁢h}$, and $f_{i⁢h}$ is better estimated by the calculation for single PDs.

### Computing required densities or α¯ with default model

Numbers in Table 2 are computed based on forward computation of $P⁢(\alpha)$ given $ρ$, $\alpha¯$, corresponding $R_{n}$ and other parameters with increments of 0.1 PD/μm2 ($ρ$) or 0.01 nm ($\alpha¯$ etc.) and linear interpolation between the two values that closest match the target $P⁢(\alpha)$. This yields an error of less than 0.0001 μm/s on $P⁢(\alpha)$. We use $\alpha$ = 0.5 nm for CF. The method for computing $P⁢(C⁢F)$ using the unobstructed sleeve (default) model is described throughout the main text. PDinsight, the python program used for computing all values in Table 2, Appendix 5—table 1, Figure 8B and Table 1 is available as supporting material.
