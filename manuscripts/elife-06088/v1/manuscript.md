# Cortical microtubule nucleation can organise the cytoskeleton of Drosophila oocytes to define the anteroposterior axis

## Authors

- Philipp Khuc Trong<sup>1</sup>
- Hélène Doerflinger<sup>3</sup>
- Jörn Dunkel<sup>1</sup>
- Daniel St Johnston<sup>3</sup>
- Raymond E Goldstein<sup>1</sup> †

### Affiliations

1. Department of Applied Mathematics and Theoretical Physics University of Cambridge Cambridge United Kingdom
2. Department of Physics University of Cambridge Cambridge United Kingdom
3. Wellcome Trust/Cancer Research UK Gurdon Institute, Henry Wellcome Building of Cancer and Developmental Biology University of Cambridge Cambridge United Kingdom
4. Department of Mathematics Massachusetts Institute of Technology Cambridge United States

† Corresponding author

## Abstract

Many cells contain non-centrosomal arrays of microtubules (MTs), but the assembly, organisation and function of these arrays are poorly understood. We present the first theoretical model for the non-centrosomal MT cytoskeleton in Drosophila oocytes, in which bicoid and oskar mRNAs become localised to establish the anterior-posterior body axis. Constrained by experimental measurements, the model shows that a simple gradient of cortical MT nucleation is sufficient to reproduce the observed MT distribution, cytoplasmic flow patterns and localisation of oskar and naive bicoid mRNAs. Our simulations exclude a major role for cytoplasmic flows in localisation and reveal an organisation of the MT cytoskeleton that is more ordered than previously thought. Furthermore, modulating cortical MT nucleation induces a bifurcation in cytoskeletal organisation that accounts for the phenotypes of polarity mutants. Thus, our three-dimensional model explains many features of the MT network and highlights the importance of differential cortical MT nucleation for axis formation.

## Introduction

Microtubules (MTs) are polar cytoskeletal filaments that can adopt different global network organisations to fulfil different functions. The vast majority of studies have focussed on understanding the architecture and function of MT arrays organised by centrosomes, such as radial arrays or the mitotic spindle. In contrast, much less is known about the organisation, assembly and function of non-centrosomal MT arrays despite their ubiquity in differentiated cell types, such as neurons, epithelia, fission yeast and plants (Bartolini and Gundersen, 2006; Carazo-Salas and Nurse, 2006). In a variety of cell-types, non-centrosomal MT arrays play an essential role in directing the subcellular localisation of mRNAs to spatio-temporally control gene expression. In neuronal dendrites, for example, MTs form bidirectional arrays with MT plus-ends both pointing away and towards the cell body (Conde and Caceres, 2009; Kapitein and Hoogenraad, 2011). MTs and associated motor proteins were implicated in the transport of mRNAs along dendrites (Bramham and Wells, 2007), where their activity-dependent translation contributes to long term changes in synaptic function, neuronal circuitry and memory (Miller et al., 2002; Sutton and Schuman, 2006; Holt and Schuman, 2013). Similar overlapping, bidirectional MT arrays in the Xenopus oocyte have been proposed to mediate the transport of Vg1 mRNA to the vegetal cortex, where it orchestrates germ layer patterning (Messitt et al., 2008; Gagnon et al., 2013). The Drosophila oocyte is probably the best-studied example of mRNA transport along non-centrosomal MTs. In this system, a diffuse gradient of MTs of mixed polarity is required for the localisation of bicoid and oskar mRNAs to opposite ends of the cell (Becalska and Gavis, 2009). Despite the large amount of work, however, the organisation of the non-centrosomal MT cytoskeleton underlying this mRNA localisation is controversial (MacDougall et al., 2003; Januschke et al., 2006; Zimyanin et al., 2008), and its assembly and function are not understood. In stage 9 oocytes, MTs grow from most parts of the cell cortex into the volume (Theurkauf et al., 1992; Parton et al., 2011) thereby giving rise to a complex, three-dimensional MT network without pronounced polarity along the anterior-posterior (AP) axis (Theurkauf et al., 1992; Cha et al., 2001). In contrast to this apparent disordered organisation, bicoid and oskar mRNAs become reliably localised by Dynein and Kinesin to the anterior corners and to the posterior pole of the oocyte, respectively, thereby defining the AP axis (Brendza et al., 2000; Duncan and Warrior, 2002; Januschke et al., 2002; Weil et al., 2006; Zimyanin et al., 2008).

The most pronounced feature of the MT cytoskeleton at stage 9 is a gradient of cortical MTs from the anterior to the posterior pole, where MT nucleation is suppressed by the polarity protein PAR-1 (Doerflinger et al., 2006; Roth and Lynch, 2009). Live imaging of oskar mRNAs and direct measurements of growing MTs showed that the MT network is mostly disordered with only a weak statistical bias of about 8% more plus ends pointing towards the posterior pole (Zimyanin et al., 2008). This bias vanishes in absence of PAR-1 when MTs nucleate from all over the cortex (Parton et al., 2011). While these findings established a directionality of the MT meshwork for the first time, several questions remain unanswered. For example, mRNA transport and localisation is highly reproducible, raising doubts about whether the underlying cytoskeletal organisation can be mostly disordered. Moreover, Dynein-dependent transport to MT minus ends localises injected, so-called naive bicoid mRNA to the cortex closest to the injection site (Cha et al., 2001), which is difficult to reconcile with a cytoskeleton that is simply biased towards the posterior everywhere. Similarly, the different behaviour of so-called conditioned bicoid mRNA, which localises specifically to the anterior cortex irrespective of the injection site (Cha et al., 2001), has remained unexplained. Finally, motor-driven cytoskeletal transport is not the only transport mechanism in oocytes. Kinesin moves only 13% of oskar mRNA at any given time, and the remaining 87% is subject to diffusion and slow cytoplasmic flows that are driven indirectly by Kinesin activity on the MT network (Zimyanin et al., 2008). This raises the question if cytoskeletal transport alone is sufficient to account for mRNA localisation (Glotzer et al., 1997; Forrest and Gavis, 2003) and highlights the importance of distinguishing its contribution to localisation from the contribution of flows and diffusion (Serbus et al., 2005).

Here, we present the first theoretical model for stage 9 Drosophila oocytes. Based on the distribution of MT nucleation sites around the cortex, this model accurately reproduces the observed distribution of MTs and cytoplasmic flows in the oocyte. It reveals that the MT cytoskeleton is compartmentalised and more ordered than previously thought. By modelling the movement of mRNAs on this network, we also show that this MT organisation is sufficient to explain the localisation of oskar and naive bicoid mRNA. Finally, we show that modulation of MT nucleation gradients causes a bifurcation in cytoskeletal organisation that explains mutant phenotypes. Thus, our results explain many features of the assembly, organisation and function of the non-centrosomal MT array in Drosophila oocytes and highlight the key role of differential MT nucleation or anchoring at the cortex (Lüders and Stearns, 2007).

## Results

MTs in the oocyte are nucleated or anchored at the cortex (Theurkauf et al., 1992; Parton et al., 2011) and grow from the membrane into the volume. The cortical MT density follows a steep gradient along the posterior-lateral cortex from high density at the anterior corners to low densities at the posterior pole (Figure 1D, ‘Materials and methods’ MT nucleation probability). In our model, we emulated these features by selecting seeding points for MTs at random positions along the oocyte cortex, comprised of two parabolic, rotationally symmetric caps that capture the typical shape of a stage 9 Drosophila oocyte (Figure 1A, ‘Materials and methods’ Coordinates and oocyte geometries). The density of seeding points decreases steeply along the posterior-lateral cortex to zero at the posterior pole, and decreases weakly along the anterior cortex towards the anterior centre (Figure 1A,B, ‘Materials and methods’ MT nucleation probability). Each seeding point nucleates a MT polymer that grows until it either hits a boundary or reaches a target length imposed by the aging of MTs before catastrophe (Gardner et al., 2011) (‘Materials and methods’ MT growth). In total, we computed more than 55,000 MTs for each realisation of a 3D wild-type cytoskeleton.

![Figure 1.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig1-v1.jpg)

**Figure 1.:** (A) 3D geometry of a stage 9 Drosophila oocyte (grey, anterior to the left, posterior to the right) containing more than 55,000 MT seeding points. From the corners to the centre, MT seeding density decreases weakly along the anterior (kA = 1000 μm, $h_{0}^{A}=0.8$) and strongly along the posterior-lateral cortex (kP = 150 μm, $h_{0}^{P}=0$, see ‘Materials and methods’ MT nucleation probability). Nucleated MT polymers are stiff random walks, initially pointing in a random direction. Only MT segments in a cross section are shown (green) to emulate confocal images. MT target lengths are chosen from a probability distribution that accounts for the MT aging process. The mean target length is set to a fraction ϵ of the anterior-posterior (AP) axis length, here ϵ = 0.5 (‘Material and methods’ MT growth). The inset shows the 3D angular distribution of 0.5% of all MT segments with 3D statistical bias. (B) Cross section through the MT cytoskeleton shown in A with 2D directional bias (top right). The inset shows 2D posterior bias (in percent) as function of depth (bottom right). (C) Local vector sum of MT segments from the cross section in panel B on a coarse-grained grid shown as streamlines that visualize local directionality. (D) Staining of α-tubulin (green) shows MT density distribution in a fixed stage 9 oocyte. Nuclei in blue (DAPI), scale bar is 30 μm. (E) Schematic detailing the work flow in the model and comparisons to experiments. (F) Local directionality of MT cross section as in panel C for an average over 50 independent realizations of the cytoskeleton. (G) Local directionality computed from the rod model with the same parameters as in panels A, B but shortened MT lengths (‘Material and methods’ Motor velocity field). Orange arrows show the separatrices between subcompartments. (H) MT density distribution computed from 50 realizations of the polymer model.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Alternative geometry for a stage 9 oocyte comprised of a posterior parabolic cap and an anterior disc. MT segments intersecting a cross section in one realization of the polymer model with nondimensional seeding density parameters kP = 150 μm, $h_{0}^{P}=0,k_{A}=1000 μm$, $h_{0}^{A}=0.8$ and MT length parameter ϵ = 0.5 from more than 55,000 seeding points are shown in green. Inset shows directionality of 0.5% of all MT segments with posterior bias. (B) Cross section through 3D MT cytoskeleton shown in panel A with 2D directional bias (top right). Inset shows 2D posterior bias (in percent) as function of depth (bottom right). (C) Local vectorial sum of MT segments visualized as a streamplot. One individual realization of the MT cytoskeleton shows poor spatial order. (D) α-tubulin staining of an early stage 9 oocyte. Scale bar is 25 μm. (E) Schematic of the work flow in our model. (F) Streamplot of the local vectorial sum of 50 realizations of the polymer MT cytoskeleton with parameters as in A, B. (G) Local net orientation of straight rod MTs in the rod model with parameters as in A, B but reduced mean MT target length ϵ = 0.28, showing the same compartmentalization of the oocyte as the average in the polymer model. (H) MT density distribution in the ensemble of 50 realization of the polymer MT cytoskeleton.

A cross section through the computed MT meshwork (Figure 1A,B) bears a striking resemblance to confocal images of Tau- (Micklem et al., 1997; Ganguly et al., 2012) and EB-1- (Parton et al., 2011) tagged MTs, correctly showing the pronounced AP gradient of MT density. Taking into account the orientations of all MT segments in the 3D volume, it also reproduces the experimentally measured directional bias (Parton et al., 2011) with 8.5% more MT segments pointing posteriorly than anteriorly (Figure 1A, inset). The directional bias in a 2D slice varies depending on the depth of the slice in the oocyte, ranging from 50.7% of posteriorly oriented MT segments at the cortex to 60.6% in the mid plane (Figure 1B, inset). This demonstrates that measurements in 2D confocal slices poorly characterise the fully extended 3D system.

Central to understanding mRNA localisation is the question of MT orientations. Calculating the local vectorial sum of MT segments on a coarse-grained grid gives the local MT orientations in the computed cytoskeleton. Local orientations of an individual realisation of the cytoskeleton (Figure 1A,B) show poor global network order (Figure 1C). However, cargo localisation in the oocyte does not involve only a single cytoskeletal realisation. MTs disappear after 5–10 min in the presence of Colchicine (Theurkauf et al., 1992; Zhao et al., 2012) (V Trovisco, personal communication), a drug that blocks MT growth and destabilizes dynamic MTs, indicating that the whole network turns over within minutes. Thus, the oocyte samples many tens to a hundred of independent MT organisations over the 6–9 hr of stage 9. Summation of local orientations over an ensemble of 50 independent realisations of the computed MT network reveals a striking spatial partitioning of the cytoskeleton into several subcompartments (Figure 1F). At the anterior, the mean orientation points posteriorly, while MTs at the lateral sides on average point inwards toward the AP-axis. Counting the number of MT segments that contribute to each grid box in the ensemble also shows the distribution of MT density (Figure 1H). In agreement with experiments (Figure 1D), the MT density exhibits a pronounced AP gradient with highest values in the anterior corners, even when MT seeding is uniform on the anterior surface.

In the limit of a large ensemble, the MT polymers sample all possible initial directions and possible lengths at every point along the cortex. In this limit, we can test the predicted compartmentalised MT organisation by constructing a second model in which MTs are represented as straight rods. The net orientation of the cytoskeleton at a given point inside the oocyte is then computed as weighted sum of MT contributions from each point along the boundary (‘Materials and methods’ Model setup).

With a shorter MT target length to compensate for the effectively longer length of straight rods compared to curved polymers, computation of net MT orientations in the rod model shows a topology (Figure 1G) that confirms the mean topology in the polymer model (Figure 1F). The three compartments of a posterior-pointing anterior section and two inwards-pointing lateral sections are effectively bounded by separatrices (Figure 1G, orange arrows). Cargo molecules that are transported on MTs to their plus ends move along the arrows and converge at the separatrices, eventually leading to the posterior pole as the sole point of attraction in the entire oocyte volume (the attractor). By contrast, cargo that is transported to MT minus ends moves opposite to the arrows and diverges away from the separatrices.

This mean topology of the MT cytoskeleton is insensitive to the exact choice of the MT nucleation probability and to the choice of the MT length distribution (‘Materials and methods’ MT nucleation probability, MT growth). It also remains unchanged in a differently shaped oocyte geometry in both the polymer model and the rod model (Figure 1—figure supplement 1). In summary, both models show that even disordered non-centrosomal MT arrays can feature well-defined mean organisations, and that the MT cytoskeleton in oocytes is organised in a compartmental fashion.

The suitably scaled local vectorial sum of MT segments (Figure 1C) for an individual realisation of the polymer model (Figure 1A,B) is a vector field vm which represents active Kinesin-driven transport on the cytoskeleton (‘Materials and methods’ Motor velocity field). In vivo during stage 9, the oocyte cytoplasm undergoes slow cytoplasmic flows that are abolished in kinesin heavy chain mutants. This indicates that flows are driven by kinesin-dependent transport of an unknown cargo through the viscous cytoplasm (Palacios and St Johnston, 2002; Serbus et al., 2005), thus making cytoplasmic flows a secondary read-out of cytoskeletal organisation (Khuc Trong et al., 2012). Therefore, we next tested if our computed polymer MT cytoskeleton can produce flows that are consistent with observed cytoplasmic streaming.

Measurements of speeds of autofluorescent yolk granules in live stage 9 oocytes showed that mean flow velocities are slow (Figure 2F). The physics of slow incompressible fluid flows u driven by forces f is described by the Stokes equations(1)0=−∇p+μ∇2u+f , ∇⋅u=0 .

![Figure 2.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig2-v1.jpg)

**Figure 2.:** (A) Streamlines (light blue lines) visualize the 3D cytoplasmic flow field computed from the realization of the cytoskeleton shown in Figure 1A. The horizontal plane shows a 2D cross-section through the 3D field. Anterior to the left, posterior to the right. (B) Cross-section through the 3D field shown in panel A with arrows indicating flow directions and colouring indicating flow speeds. (C) Confocal image of a live stage 9 oocyte. Arrows show the flow field computed from particle image velocimetry (PIV) of streaming yolk granules and averaged over ≈5 min. Scale bar is 25 μm. (D) Same as A, but showing the mean flow organization for an average of 100 individual 3D flow fields, analogous to the mean organization of the MT cytoskeleton in Figure 1F. (E) Same as B for the average in panel D. (F) Mean fluid flow speeds were obtained by PIV (red, 13.7 ± 0.8 nm/s, mean ± sem) and automatic particle tracking (orange, 15.3 ± 0.7 nm/s, mean ± sem) from 48 oocytes. Experimentally measured flow speeds were used to calibrate the forces f in the Stokes Equation 2 such that the computed mean speeds in 3D (blue, mean: 14.5 nm/s) or in 2D cross sections (green, mean: 14.8 nm/s) match the measured values. The larger spread in experimental flow speeds may reflect greater variability of motor activity, cytoplasmic composition, geometry or age in vivo.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Streamlines visualizing the flow field computed in the 3D oocyte geometry with additional no-slip boundary condition on a sphere representing the nucleus. Same forces as in Figure 2A,B, main text. The nucleus occupies 2.2% of the oocyte volume. Horizontal plane shows a cut through the flow field. (B) Young stage 9 oocyte stained with DAPI (blue), phalloidin (red) and showing oskar MS2 GFP (green) in the process of reaching the posterior pole. Scale bar is 25 μm. (C) Extracted and rotated shape of the oocyte in panel B (red), and symmetrized geometry resulting from averaging the shape above and below the AP-axis (blue). Black circle indicates the nucleus. (D) Ratio of nucleus volume to oocyte volume computed for Ne = 9 early (red) and Nm = 7 mid stage 9 oocytes (blue). Arrowhead marks the oocyte shown in panel B. (E, F) Cross sections through the 3D flow fields for the same forces as in panel A with (F) and without (E) nucleus. (G, H) Same as E and F, but vertical cross section that does not contain the nucleus.

We make the simplest possible assumption that the forces f are proportional to the motor-velocity field, and use experimentally measured flow speeds to calibrate the scalar factor of proportionality. By solving the Stokes equations, we then computed the full 3D fluid flow field (Figure 2A) corresponding to an individual realisation of the MT cytoskeleton (Figure 1A), and 2D cross sections through the 3D field (Figure 2B) were compared to in vivo flow patterns visualised by particle image velocimetry (PIV, Figure 2C).

Despite large variability, both computed and in vivo flows show very similar patterns, generally being strongest in the anterior half of the oocyte, and weaker in the posterior half (Figure 2B,C). Computed flows occasionally reach further into the posterior half than typically seen in PIV flow fields, thereby slightly overestimating the range of flows. However, except in rare cases, computed flows do not reach the posterior pole. This result is largely independent of the presence of the oocyte nucleus which occupies less than 2.5% of the oocyte volume, even for small oocytes at the beginning of stage 9 (Figure 2—figure supplement 1, ‘Materials and methods’ Nucleus to oocyte volume ratio, Impact on flow field). Thus, computed flows appear consistent with observed slow cytoplasmic streaming.

We tested next if our computed cytoskeleton in combination with the derived cytoplasmic flows and diffusion can account for dynamic mRNA transport and localisation. We described the mRNA distributions as continuous concentration fields. oskar mRNA is assumed to reside in either one of two states: the Kinesin-bound state with concentration cb, in which cargo is transported actively on the cytoskeleton-derived motor-velocity field vm (Figure 1C), or the unbound state with concentration cu, in which cargo is transported by the cytoplasmic flows u (Figure 2A) and diffuses with diffusion constant D. Cargo can exchange between both states by chemical reactions, thereby resulting in the reaction-advection-diffusion equations:

$$
\partial_{t} c_{b}+\nabla⋅(v_{m} c_{b})=k_{b} c_{u}−k_{u} c_{b},
$$



$$
\partial_{t} c_{u}+\nabla⋅(u c_{u})=−k_{b} c_{u}+k_{u} c_{b}+D\nabla^{2}c_{u}.
$$

Parameter values were constrained with experimentally measured values (‘Materials and methods’ Parameter values). Furthermore, throughout the simulation we cycled through the pairs of fluid flow u and motor-velocity fields vm (Figure 3) to account for the dynamic nature of the MT network (Parton et al., 2011) and flow patterns, which change over time scales of minutes compared to the 6–9 hr during which oskar mRNA is localised (‘Materials and methods’ Autocorrelation function).

![Figure 3.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig3-v1.jpg)

**Figure 3.:** (A–C) Shown are fixed oocytes with oskar MS2 GFP (green) and stained with DAPI (blue) and Phalloidin (red). oskar mRNA forms a central cloud at late stage 8 (A), a collimated channel while moving to the posterior (B), and a posterior crescent at stage 9 (C). Scale bars are 25 μm. (D) 3D oocyte showing the initial oskar mRNA cargo distribution. (E, F) Cross sections through a simulation of oskar mRNA transport with diffusion, motor-transport and flows showing the distribution of total cargo cb + cu at the indicated time points. No posterior anchor is present. Simulations of three 6 hr cycles through 50 (vm,u)-pairs in random order once (twice, see Figure 4). For simulations of 1.5 hr, 25 (vm,u)-pairs were chosen at random. Compare to experimental observations in panels B and C. (G) Same simulation as in D–F, but without cytoplasmic flows, showing largely identical localisation as in F. (H) Simulation of bicoid mRNA transport shows the mRNA quickly accumulating at the nearest cortex (arrowheads) when injected in the posterior (inset), corresponding to the behavior of naive bicoid. (I) Same as in H, corresponding to naive bicoid mRNA injection at the anterior-dorsal region (inset). (J) Same as in H for injection at the anterior middle (inset), showing that over long times simulated bicoid mRNA localises to the anterior corners (arrowheads). Localization to the anterior depends on sufficient proximity of the injection site as observed for injections of naive bicoid mRNA. (K) Same simulation for oskar mRNA as in D–F, but with a posterior anchor (arrowhead) and without active motor-driven transport. Compare to panels F and G.

Starting from an initial diffuse cloud of oskar mRNA in the centre of the oocyte (Figure 3A,D,E), simulations show that the mRNA quickly concentrates in the centre before forming a channel from the centre of the oocyte towards the posterior pole (Figure 3E). Formation of this channel reflects the locally inwards orientation of MTs in the posterior half of the oocyte (Figure 1E,F). This transient state closely resembles transient patterns of fluorescently-tagged oskar mRNA during the transition between stages 8 and 9 (Figure 3B), thereby supporting the notion that our computed MT cytoskeleton correctly captures key aspects of the in vivo MT network.

Upon reaching the posterior cortex, oskar mRNA is translated to produce Long Osk (Vanzo and Ephrussi, 2002), which is involved in anchoring oskar mRNA. However, oskar mRNA localises normally at stage 9 when anchoring is disrupted (Micklem et al., 2000; Vanzo and Ephrussi, 2002). Anchoring is therefore not necessary at stage 9, and we did not include it in our model at this point. Despite the lack of any anchoring, oskar mRNA forms a posterior crescent after 1.5 hr and becomes highly concentrated by the end of the simulation (Figure 3F), correctly capturing observations of in vivo localisation (Figure 3C). A 4 μm thick slice at the posterior pole contains 12.5% of total cargo in the oocyte (Figure 3F), showing that continual transport combined with slow diffusion is sufficient to reach and maintain high concentrations of mRNA.

In our description of transport (Equation 2), cargo acts as an unspecific passive tracer. Passive tracers merely follow the transport fields vm and u, and these two fields must contain all information about the localisation sites. We therefore asked which field contains most information about localisation. We first tested localisation in the absence of cytoplasmic flows by setting the fluid flow field identical to zero u ≡ 0. This situation is similar to but more severe than in slow Kinesin mutants (Serbus et al., 2005). Starting from the central oskar mRNA cloud (Figure 3D), we found that oskar mRNA still localises to and forms a concentrated crescent at the posterior pole (Figure 3G). A 4 μm thick slice off the posterior pole contains 11.3% of total available oskar mRNA cargo, only marginally less than localisation with cytoplasmic flows present. This suggests that the cytoskeletal transport alone localises the majority of mRNA. Cargo localisation in the absence of cytoskeletal transport can be tested by either setting the motor-velocity field identical to zero vm ≡ 0, or by setting the binding constant kb to zero. In either case, cargo disperses throughout the oocyte without forming a central channel and completely fails to produce any posterior crescent. We further asked whether the flow could localise cargo to wild-type levels if an anchor captured cargo at the posterior. To this end, we replaced the bound state in the model by an anchored state to which cargo can bind only at the very posterior boundary. Binding to the anchor occurs with a reaction rate constant that is 10 times larger than the reaction rate constant kb used for oskar mRNA binding to the MT cytoskeleton (‘Materials and methods’ Parameter values). Moreover, anchored cargo cannot be released, thus making this anchor a perfect sink with stronger trapping properties than any realistic anchor. Under these idealised conditions, oskar mRNA accumulates slightly at the anchor (Figure 3K). However, a 4 μm thick posterior slice contains only 2.7% of total cargo in the oocyte, about 78% less cargo than in the wild-type simulations, and only 25% more cargo compared to the purely diffusive case, which localises 2.2% of cargo. Thus, even under the most favourable conditions, the cytoplasmic flows cannot localise mRNA to wild-type levels, arguing against a mixing and entrapment mechanism for oskar mRNA localisation at stage 9. Despite the small fraction of actively transported cargo (13%), motor-driven mRNA transport is both necessary and sufficient to account for oskar localisation.

In contrast to oskar mRNA, bicoid mRNA is believed to be transported by Dynein (Duncan and Warrior, 2002; Januschke et al., 2002; Weil et al., 2006), but other parameters such as the fraction of bound cargo and the active transport speeds are similar to oskar mRNA (Belaya, 2008) (V Trovisco, personal communication). To test whether the proposed cytoskeletal organisation also captures transport and localisation of injected bicoid mRNA, we inverted the directions of the motor-velocity fields (Figure 1C) to account for the minus end directed transport by Dynein instead of the plus end directed transport by Kinesin. Other parameters including cytoplasmic flow fields remained unchanged.

Simulations show that bicoid mRNA accumulates at both posterior-lateral sides (Figure 3H) when initially placed in the posterior half of the oocyte (Figure 3H, inset). This is in very good agreement with experimental observations when naive bicoid mRNA is injected into this posterior region (Cha et al., 2001). When bicoid mRNA is placed initially in the anterior-ventral region (Figure 3I, inset), it accumulates at the anterior and lateral cortex (Figure 3I), again in concordance with the experimental observations (Cha et al., 2001). This simulated localisation of bicoid mRNA remains virtually identical in the absence of cytoplasmic streaming. Thus, splitting of a bulk amount of injected bicoid mRNA occurs when the RNA is placed on the border (separatrices) between two diverging subcompartments of the MT cytoskeleton, each one transporting part of the cloud towards the adjacent cortex. The agreement between simulations and experiments therefore further supports an on average compartmentalised MT cytoskeleton, and naive bicoid mRNA, like oskar mRNA, unspecifically traces out the MT cytoskeleton.

In contrast to naive bicoid mRNA, endogenous bicoid mRNA is transported into the oocyte after being transcribed in neighbouring nurse cells where it also becomes modified in presence of the protein Exuperantia. Endogenous bicoid mRNA can be approximated by so-called conditioned bicoid mRNA that is first injected into the nurse cells, then sucked out and injected into the oocyte. Conditioned bicoid mRNA localises specifically to the anterior surface within 30 min, even if this surface is not closest to the injection site (Cha et al., 2001). In the model, starting from an initial distribution at the anterior surface where endogenous bicoid mRNA enters the oocyte, cargo quickly moves to the anterior cortex before concentrating in the anterior corners after several hours of simulated time (Figure 3J). This resembles the anterior ring-like localisation of bicoid mRNA in wild-type stage 9 oocytes (St Johnston et al., 1989; Weil et al., 2006), and occurs independently of cytoplasmic flows. However, the model does not reproduce transport specifically to the anterior surface when injection is further away from the anterior. This suggests that Exuperantia activity somehow either enables bicoid mRNA to move along an unidentified population of MTs (Cha et al., 2001; MacDougall et al., 2003) that are not included in the computed cytoskeleton, or that it allows localisation of the mRNA by an unknown MT-independent mechanism.

We have shown so far that cortical gradients of MT nucleation are sufficient to assemble a functional, compartmentalised MT cytoskeleton that successfully localises oskar mRNA and naive bicoid mRNA. Next, we asked if cortical MT nucleation can also produce cytoskeletal organisations that explain mutants with partial or complete polarity defects. Mutations interfering with the posterior follicle cells that surround the oocyte, for example, can disrupt the proper positioning of mRNAs (Gonzalez-Reyes et al., 1995; Roth et al., 1995). Specifically, follicle cell clones (rasΔC40b) that are adjacent to only one side of the oocyte posterior repel cargo from that side of the cortex (termed clone adjacent mislocalisation [Poulton and Deng, 2006]), likely due to an altered MT organisation. To mimic this phenotype, we used an ensemble of wild-type cytoskeletons and artificially added MT nucleation sites to a patch on one side of the posterior pole. Simulations of cargo transport with diffusion, motor transport and flows show that oskar mRNA is repelled from this patch and localises to the adjacent posterior boundary, in agreement with experiments (Figure 4—figure supplement 2).

Mislocalisation of mRNAs also occurs in mutants of the polarity protein PAR-1, which acts to suppress MT nucleation at the posterior pole of the oocyte (Shulman et al., 2000; Doerflinger et al., 2010). In strong par-1 hypomorphs with strongly reduced PAR-1 expression, MT minus ends occupy the whole cortex including the posterior pole (Parton et al., 2011), thereby causing oskar mRNA to mislocalise to a dot in the centre of almost 90% of mutant oocytes (Doerflinger et al., 2006). To test this phenotype in the model we distributed MT seeding points uniformly on the posterior surface (Figure 4G, inset) while keeping the seeding density on the anterior surface constant. The AP gradient of MT density then vanishes and the directional bias of MT segments evens out (Figure 4G, ensemble-averaged 3D-bias: 50.1%:49.9%). The ensemble-averaged local orientations of MTs show that MTs point towards a single focal point in the centre of the oocyte (Figure 4G) that acts as a stable fixed point of the system. Computation of 3D flow fields for each realisation in the new ensemble (3D mean: 13.5 nm/s; 2D mean: 14.5 nm/s, N = 50) and simulations of transport with and without cytoplasmic flows show oskar mRNA concentrating in a cloud in the centre of the oocyte (Figure 4C). oskar mRNA accumulation to a central dot also remains unchanged if the posterior MT seeding density is decreased slightly (Figure 4H, inset) as might be expected for hypomorphs that do not abolish PAR-1 expression completely.

![Figure 4.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig4-v1.jpg)

**Figure 4.:** (A–E) Simulations of oskar (A–C) and bicoid (D) mRNA transport with diffusion, cytoskeletal transport and flow for the cytoskeletal architectures shown in panels E–H, and their corresponding flow fields. For oskar mRNA, simulations reproduce wild-type localisation (A, same as Figure 3F), and partial (B) or complete mislocalisation (C). Initial condition as in Figure 3D. Simulation times were occasionally increased to 6 hr (B) to rule out transient concentration patterns. For bicoid mRNA, simulations capture mislocalisation to both anterior and posterior as in gurken/torpedo/cornichon mutants and in strong par-1 hypomorphs (D, arrowheads). Time points as indicated. The inset in D shows initial condition. (E–H) Average local MT orientations in ensembles of 50 realizations of the polymer model for varying MT seeding densities along arclength s (see panel E) of the posterior-lateral cortex (insets). A MT seeding density that increases from a wild-type gradient (E, $h_{0}^{P}=0,k_{P}=150 μm$) laterally towards the posterior (F, $h_{0}^{P}=0,k_{P}=17.5 μm$) to a near-uniform distribution (G, $h_{0}^{P}=0,k_{P}=1 μm$) shows a saddle-node bifurcation by creating a pair of stable (green) and unstable (red) fixed points. (H) A MT seeding density that is slightly lower at the posterior pole ($h_{0}^{P}=0.7,k_{P}=40 μm$) produces mean MT orientations virtually indistinguishable from uniform seeding density (compare to G). (I–K) Vector field of the mathematical normal form of the 2D saddle-node bifurcation (‘Materials and methods’ Bifurcation normal form). Values of the bifurcation parameter λ as indicated. Fixed points are located at positions $x=\pm\sqrt{\lambda}$. (L) Fluorescence in-situ hybridization to bicoid mRNA in a strong par-1 hypomorph. The mRNA (red) localises around the cortex, with most accumulation at the anterior corners and at the posterior pole (compare to panel D, arrowheads). Scale bar is 25 μm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A–J) Each panel shows the mean local MT orientations for an ensemble of 50 realizations of the polymer MT cytoskeleton under variations of the seeding density parameter kP and MT length parameter ϵ as indicated. Approximate location of the stable fixed point is shown in green, with region of attraction in blue, and domain of attraction of the posterior pole in red. The point on the AP-axis between red and blue arrow region marks the unstable fixed point. Percentages indicate the ensemble-averaged 3D directional bias. Experimentally, the directional bias was measured as 57.97%:42.03% (Parton et al., 2011). Cytoskeleton in panel I was used as wild-type cytoskeleton (Figure 1F, main text). Anterior seeding density is unchanged in all panels kA = 1000 μm, $h_{0}^{A}=0.8$. (K–O) Same as panels A–J but for ensembles with 100 realizations of the cytoskeleton to ensure reliable visualization of vector field even when fewer MTs reaching the oocyte center. (P–T) Vector fields computed from a saddle-node bifurcation normal form. The critical bifurcation point is λ = 0, and for λ < 0, fixed points are located at $x_{\pm}=\pm\sqrt{−\lambda}$.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A–D) Addition of lateral MTs reproduces the clone-adjacent-mislocalisation phenotype. (A) Cross section through one realization of the wild-type MT cytoskeleton in the polymer model ($h_{0}^{A}=0.8,k_{A}=1000 μm$, $h_{0}^{P}=0,k_{P}=150 μm$). Additional MTs have been added dorsal to the posterior pole (black arrow) to mimick posterior follicle cell clones (RASΔC40b MARCM) that overexpress dystroglycan (Poulton and Deng, 2006). (B) Density of MTs for 50 realizations of the cytoskeleton shows enrichment on one side of the posterior pole (white arrow). (C) Streamplot showing the local vectorial orientation averaged over 50 realizations of the cytoskeleton. Note the upwards tilt away from the central posterior pole. (D) Simulations of oskar mRNA transport by diffusion, cytoskeletal transport and corresponding cytoplasmic flows show that cargo is repelled from the site of additional MT nucleation on one side of the posterior pole, thereby capturing the CAM phenotype (Poulton and Deng, 2006).

Interestingly, bicoid mRNA simulated either with slightly decreased (Figure 4H) or with uniform (Figure 4G) posterior MT nucleation not only localises to the anterior corners as in wild-type but also enriches at the posterior pole (Figure 4D, arrowheads), despite injection close to the anterior (Figure 4D, inset). This matches experiments showing bicoid mRNA mislocalisation to both anterior and posterior in gurken, torpedo and cornichon mutants (EGFR mutants) in which posterior follicle cells fail to signal a MT reorganisation in the oocyte (Gonzalez-Reyes et al., 1995; Roth et al., 1995).

Failure of the external signal to the oocyte is thought to have the same effect as par-1 hypomorphs, but previous experiments with bicoid mRNA in par-1 hypomorphs resulted in ambiguous localisations (Shulman et al., 2000; Benton et al., 2002). Here, using confocal fluorescence in situ hybridisation, our experiments show that bicoid mRNA localises primarily to the anterior corners and to the posterior pole in strong par-1 hypomorphs (Figure 4L), thereby mirroring EGFR mutants and agreeing with the model predictions. Thus, (near-)uniform MT nucleation along the posterior and lateral cortex is sufficient to explain the polarity phenotypes observed for oskar and bicoid mRNAs in gurken, torpedo and cornichon mutants and in strong par-1 hypomorphs.

In 10% of strong par-1 hypomorphs and 30% of weak par-1 hypomorphs with weakly reduced PAR-1 expression, oskar mRNA is only partially mislocalised, combining a wild-type-like posterior crescent with a centrally mislocalised dot (Doerflinger et al., 2006). We therefore modulated the MT nucleation along the posterior-lateral cortex to test if this is sufficient to produce intermediate cytoskeletal organisations between wild-type (Figure 4F) and strong par-1 hypomorphs (Figure 4H).

Increasing MT nucleation laterally towards the posterior pole (Figure 4G, inset) again creates a stable focus in the centre of the oocyte. However, its domain of attraction does not cover the entire oocyte. Instead, a small basin of attraction towards the posterior pole persists (Figure 4G, red), separated from the basin of attraction of the stable focus by an unstable saddle-node point. Further increasing the seeding density towards the posterior pole shows that the pair of stable and unstable fixed points move further apart (Figure 4—figure supplement 1) until the unstable point no longer resides inside the oocyte geometry, thereby giving rise to the strong par-1 hypomorph topology (Figure 4H,I,J). Cargo simulated on cytoskeletons with stable and unstable fixed points and their corresponding flow fields can split into two separate accumulations, first at the posterior pole and second in a dot along the AP-axis (Figure 4B). This agreement with experimental results suggests that intermediate levels of PAR-1 at the posterior lead to a cytoskeleton with a potential barrier between the oocyte centre and its posterior pole. It also shows that modulation of MT nucleation along the posterior-lateral cortex alone is sufficient to capture this. Because the potential barrier only affects the bound state, diffusion and flows can aid posterior localisation in this context by pushing unbound cargo across the unstable point and increasing the amount of oskar mRNA that reaches the posterior pole. In summary, variations of MT nucleation along the cortex not only explain mRNA localisations in wild-type but can also account for the mislocalisations of bicoid and oskar mRNAs in polarity mutants.

The creation of stable and unstable fixed points in the transition from wild-type to strong par-1 hypomorph topology constitutes a classical saddle-node bifurcation (Figure 4K–M, ‘Materials and methods’ Bifurcation normal form) with the cortical MT seeding density as the bifurcation parameter. Interestingly, in both the polymer model and the rod model, the mean length of MTs acts as a second bifurcation parameter. For example, for sufficiently short MT filaments (Figure 4K), few MTs from the anterior can reach and contribute to orientations in the posterior half of the oocyte. In the posterior half, MTs from the lateral side either point towards the anterior, thereby combining with anterior MTs to create a stable node, or towards the posterior, to form a domain of attraction at the posterior pole. Therefore, for sufficiently weak contributions from anterior MTs, MTs from the lateral sides create the unstable tipping-point.

To understand more generally how the MT lengths and the posterior-lateral distribution of seeding points together influence the three different cytoskeletal topologies (Figure 4E–G) we computed the parameter space of the straight rod model (Figure 5). If MTs are absent at the posterior pole, the wild-type topology (Figure 5Di,vi) covers a large fraction of parameter space (Figure 5A, red) for sufficiently long MTs (large ϵ) and cortical MT nucleation gradient (large kP). The creation of two fixed points splits the oocyte into different domains of attraction (Figure 5A, blue, Figure 5Di,ii) for either shorter MTs (Figure 5A, vertical dashed arrow; Figure 4—figure supplement 1I,N) or for increasingly uniform MT nucleation (Figure 5A, horizontal dashed arrow; Figure 4—figure supplement 1I,H). For almost uniform nucleation along the entire posterior-lateral cortex, the unstable fixed point exits the geometry, leaving behind only a single stable focus (Figure 5A, green, arrowhead, Figure 5Diii,iv). If some MT nucleation is allowed at the posterior pole this region of strong par-1 hypomorph topology expands substantially (Figure 5B,C, green). Interestingly, if MTs are sufficiently long, MTs from the lateral and anterior cortex can reach and overpower those from the posterior pole, thus restoring wild-type-like cytoskeletal topology that allows oskar mRNA localisation. Therefore, a low level of posterior nucleation of MTs does not necessarily lead to mislocalisation of oskar mRNA. Instead, and in addition to the distribution of cortical MT nucleation, the length of MT filaments emerges as another key regulator for polarisation and function of the non-centrosomal network.

![Figure 5.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig5-v1.jpg)

**Figure 5.:** (A) The regions corresponding to wild-type (red), weak par-1 hypomorph (blue) and strong par-1 hypomorph topologies (green, arrowhead at far left) are shown as a function of the mean MT length ϵ and extent of the posterior seeding density kP. The bifurcation line between wild-type and weak par-1 hypomorph topologies can be crossed by either changing the seeding density laterally (horizontal dashed arrow), or by shortening the MTs (vertical dashed arrow). (B, C) Parameter spaces as in A for increasing MT nucleation at the posterior pole (B: $h_{0}^{P}=0.03,C:h_{0}^{P}=0.1$). Inset in panel C shows a magnification of the triple point at which small changes in parameters can convert each cytoskeletal architecture into any other. (D) Local net orientations of MT rods for parameter values indicated in the inset of panel C (yellow circles). In all panels, parameter values for anterior MT nucleation were kept constant ($h_{0}^{A}=0.8,k_{A}=1000 μm$).

## Discussion

Non-centrosomal MT networks represent a large, yet poorly understood class of MT arrangements that often fulfil specialised functions (Keating and Borisy, 1999). Non-centrosomal MTs are frequently aligned in parallel, thereby forming linear arrays as in epithelia or neurons (Bartolini and Gundersen, 2006; Conde and Caceres, 2009; Kapitein and Hoogenraad, 2011). The non-centrosomal MT cytoskeleton in Drosophila oocytes was also first hypothesised to form a highly polarised linear array with MTs growing from the anterior surface towards the posterior pole (Clark et al., 1994; Brendza et al., 2000). Instead, the MT cytoskeleton is a complex network without a visibly discernible polarity along the AP axis (Theurkauf et al., 1992; Cha et al., 2001, 2002), and its organisation remained ambiguous (MacDougall et al., 2003; Januschke et al., 2006; Zimyanin et al., 2008; Parton et al., 2011).

We showed that in two different theoretical models, in which MTs grow from the oocyte cortex into the volume, the cytoskeleton features an on average compartmental organisation and is therefore more ordered than previously thought. In combination with cytoplasmic flows and diffusion, this cytoskeletal organisation successfully reproduces localisations of oskar and naive bicoid mRNAs in wild-type oocytes. Such a spatially varying, compartmental organisation suggests that a single statistical measure of polarity, derived by averaging data from the entire oocyte (Zimyanin et al., 2008; Parton et al., 2011), may not be a sufficient metric to characterise mRNA localisation.

Cytoplasmic flows may generally contribute to mRNA transport. Flows at later stages of oogenesis are fast and well-ordered, and occur concurrently with a late-phase enhancement of oskar mRNA accumulation (Sinsimer et al., 2011). This is consistent with a contribution of flows to mRNA localisation (Glotzer et al., 1997; Forrest and Gavis, 2003). At stage 9 of oocyte development, which is the focus of the work presented here, flows are slow and chaotic. At this stage, mutants with reduced flows showed oskar mRNA localising normally (Serbus et al., 2005), thus suggesting that slow and chaotic flows may not play the same role as in late oogenesis. However, flows in these mutants were merely reduced rather than abolished completely, and the measurements underestimated flow speeds (Serbus et al., 2005), hence leaving the interpretation of flows unclear. We here find that the effects of slow cytoplasmic flows on mRNA transport are negligible, and that cytoskeletal transport alone is sufficient for localisations of oskar and naive bicoid mRNAs. In this view, slow cytoplasmic flows arise primarily as inevitable physical byproduct of active motor-driven transport on the cytoskeleton rather than as an evolutionarily selected trait. This appears to mirror findings in the Caenorhabditis elegans zygote in which P-granules segregate by dissolution and condensation rather than via transport by cytoplasmic flows (Brangwynne et al., 2009).

Interestingly, neither MT-based transport alone nor combined with cytoplasmic flows and diffusion is sufficient to reproduce the anterior localisation of nurse cell conditioned bicoid mRNA irrespective of the position of injection into the oocyte (Cha et al., 2001). This Exuperantia-dependent mechanism may rely either on an unobserved population of MTs in the oocyte that can be specifically recognised by conditioned bicoid mRNA (Cha et al., 2001; MacDougall et al., 2003), or on an unknown MT-independent mechanism.

The central finding of our work is that gradients of cortical MT nucleation are sufficient for the assembly of a functional compartmentalised MT cytoskeleton in wild-type oocytes. While many non-centrosomal MT arrays are linear and emphasise questions about establishment and maintenance of parallel filament orientations (Ehrhardt, 2008; Lindeboom et al., 2013), our result stresses the need to understand gradients in MT nucleation as an alternative strategy for the assembly of functional non-centrosomal arrays. Whether MTs in Drosophila oocytes are differentially nucleated along the cortex itself or created elsewhere and then differentially anchored at the cortex remains an interesting open question, but both scenarios are compatible with our model. Understanding how this gradient is established will therefore depend on discovering how PAR-1 regulates MT interactions with the cortex.

Cortical MT gradients cannot only account for the wild-type cytoskeletal configuration but also for the phenotypes observed in a hierarchy of par-1 hypomorphs. Modulation of MT gradients along the posterior-lateral cortex alone are sufficient to explain the splitting of oskar mRNA between the centre and the posterior pole of the oocyte (Doerflinger et al., 2006) via a saddle-node bifurcation, suggesting that the anterior and posterior-lateral surfaces of the oocyte are functionally decoupled. Generally, bifurcations in temporal behaviour govern important qualitative transitions in many biological systems, such as the lactose network in Escherichia coli (Ozbudak et al., 2004), cell cycle in yeast (Charvin et al., 2010), and collapses of bacterial populations (Dai et al., 2012). In Drosophila, one important qualitative change is the temporal transition between stages 7/8 and 9. During this transition the MT cytoskeleton reorganises from uniform nucleation around the cortex and oskar mRNA in the centre to the AP MT nucleation gradient with oskar mRNA at the posterior. It is therefore tempting to speculate that the sequence of PAR-1 mutants and the underlying bifurcation represent static snapshots of this dynamic developmental transition in wild-type.

In conclusion, the present work provides a model that describes the assembly, organisation and function of the non-centrosomal MT array in Drosophila oocytes and directs future attention to the molecular mechanisms that enable differential MT nucleation or anchoring at the cortex.

## Materials and methods

### Coordinates and oocyte geometries

For calculation of the MT cytoskeleton, the AP axis is aligned with the z-axis of a cartesian coordinate system, and results are later shifted and rotated to align with the x-axis for visualization, for subsequent computations of cytoplasmic flows and simulations of cargo transport. Dimensional coordinates cover the ranges x ∈ [−L, L], y ∈ [−L, L] and z ∈ [0, z0 L] with length scale L = 50 μm. After nondimensionalization with scale L, coordinates are ranged as x′ ∈ [−1, 1], y′ ∈ [−1, 1] and z′ ∈ [0, z0]. Similarly, nondimensionalization of the shape parameter kP in the MT seeding density leads to $k_{P}^{′}=k_{P}/L$, and all primes will be dropped subsequently. Methods figures are shown in nondimensional spatial coordinates, and reported parameter values are nondimensional unless noted otherwise.

The 3D geometry of a typical stage 9 Drosophila oocyte is defined as two parabolic, rotationally-symmetric caps (Figure 1). Anterior (i = A) and posterior (i = P) parabolic caps are parameterized in cylindrical coordinates ρ=x2+y2∈[0,1] and ϕ ∈ [0, 2π) as(3)σi(ρ,ϕ)=ρ e^ρ+z0i(1−ρ2)e^z ,where e^ρ=(cos(ϕ),sin(ϕ),0) and e^z=(0,0,1) are the unit vectors in radial and z-direction, respectively. The line element along the parabola is calculated asdsi=‖∂σi∂ρ‖dρ=1+(2z0i ρ)2dρ,with arclength(4)si(ρ)=ρ21+(2z0i ρ)2+14z0isinh−1(2z0i ρ),defined such that si(ρ = 0) = 0 denotes the tip of the parabolic cap while si(ρ=1)=s0i denotes the distance from the tip to the anterior corners (Figure 6A,G), and hence 0≤si(ρ)≤s0i. The surface element for parabolic caps (in units of L) is given by(5)dΣi=‖∂σi∂ρ×∂σi∂ϕ‖=ρ 1+(2z0iρ)2dρ dϕ ,with total surface area(6)Σi=π6(z0i)2([1+(2z0i)2]3/2−1) .

![Figure 6.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig6-v1.jpg)

**Figure 6.:** Shown are N randomly drawn seeding points on the posterior cap of the standard oocyte geometry, according to Equation 15 distributed either (near-)uniformly on the cap (A, G) or in a parabolic gradient from the posterior pole to the anterior corners (F, L). Between uniform and parabolic distribution, the seeding density can vary either by laterally reducing the density (B, C–E, parameter kP), or by reducing the density at the posterior pole (H, I–K, parameter $h_{0}^{P}$). Total number of points is calculated with a fixed number of anterior points NA = 4000 (Equation 20). For actual computations of wild-type cytoskeletons ($k_{P}=3,h_{0}^{P}=0,k_{A}=20,h_{0}^{A}=0.8$, see main text for dimensional parameters), more than 55,000 seeding points are used.

The inward pointing normals for posterior and anterior caps are given by

$$
n^_{P}(ρ,ϕ)=−\frac{2z_{0}^{P} ρ e^_{ρ}+e^_{z}}{\sqrt{1+(2z_{0}^{P}ρ)^{2}}},
$$



$$
n^_{A}(ρ,ϕ)=\frac{2z_{0}^{A} ρ e^_{ρ}+e^_{z}}{\sqrt{1+(2z_{0}^{A}ρ)^{2}}}.
$$

A special case arises for $z_{0}^{A}=0$ when the anterior parabolic cap becomes a flat disc. In this case, the arclength (Equation 4) reduces to sA(ρ) = ρ, and the surface area (Equation 6) simplifies to ΣA = π. The inwards pointing normals for this case are given by $n^_{P}$ (Equation 7) for the posterior cap and $n^_{A}=e^_{z}$ for the anterior disc, respectively.

To investigate the robustness with respect to changes in oocyte shape, we test our model for the cytoskeleton, cytoplasmic flows and mRNA transport in two different geometries for a stage 9 Drosophila oocyte. Geometry-1 is used as standard geometry, and is comprised of two parabolic caps (Equation 3) with $z_{0}^{P}=1.48$ for the posterior cap and $z_{0}^{A}=0.2$ for the anterior cap (see Figure 1). This results in a length of the AP axis of $z_{0}^{P}−z_{0}^{A}=1.28$ with an aspect ratio of 1.56 that qualitatively resembles a typical stage 9 oocyte. Geometry-2 is tested as alternative geometry, and consists of a posterior parabolic cap with $z_{0}^{P}=1$, and an anterior flat disc with $z_{0}^{A}=0$ (Figure 1—figure supplement 1), giving an AP-axis length of 1 and aspect ratio of 2. We find that results are robust with respect to this change in geometry.

### Polymer model for MT cytoskeleton

#### MT nucleation probability

The first step in the computation of the MT cytoskeleton is the generation of MT seeding points that are randomly positioned along the oocyte membrane. We define the following probability density along the arclength si(ρ) of the anterior and posterior parabolic caps

$$
p_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i})=\frac{1}{A} p˜_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i}) ,
$$

with normalization over the oocyte surface

$$
A=\int_{Σ_{A}}dΣ_{A} p˜_{Σ}(s_{A}(ρ)|h_{0}^{A},k_{A})+\int_{Σ_{P}}dΣ_{P} p˜_{Σ}(s_{P}(ρ)|h_{0}^{P},k_{P} ),
$$

where the surface elements were specified in Equation 5 and the arclength was given in Equation 4. For the functional form of $p˜_{Σ}(s(ρ)|h_{0},k)$ we use the expression

$$
p˜_{Σ}(s(ρ)|h_{0},k)=h_{0}+(1−h_{0})[1+(\frac{k}{s_{0}})^{2}]\frac{s(ρ)^{2}}{k^{2}+s(ρ)^{2}} ,
$$

wherein the index i was dropped for simplicity. Note that for the maximum arclength s = s0 it holds that $p˜_{Σ}(s=s_{0}|h_{0},k)=1$.

h0 ∈ [0, 1] and k ∈ (0, ∞) represent two parameters governing the shape of the probability density. For small values k ≪ s0 the nucleation density approaches a Hill function with Hill coefficient n = 2 and depth h0

$$
limk≪s_{0}p˜_{Σ}(s(ρ),|h_{0},k)=h_{0}+(1−h_{0})\frac{s(ρ)^{2}}{k^{2}+s(ρ)^{2}} .
$$

In the opposite limit k ≫ s0, the probability density approaches a parabola with depth h0 (Figure 6B,H, red curve)

$$
limk≫s_{0}p˜_{Σ}(s(ρ),|h_{0},k)=h_{0}+(1−h_{0})(\frac{s(ρ)}{s_{0}})^{2} ,
$$

thus creating a pronounced gradient of MT nucleation from the pole (s = 0) to the corners (s = s0).

MT nucleation along the arclength can increase from the gradient to a homogeneous nucleation along the arclength in two different ways: (i) either by increasing nucleation from the corners laterally towards the posterior pole, or (ii) by increasing nucleation uniformly at the posterior pole. Each shape parameter h0 and k accounts for one of these possibilities. Increasing the parameter h0 leads to shallower gradients by increasing the probability for nucleation at the pole from 0 for h0 = 0 to the value for homogeneous nucleation for h0 = 1 (Figure 6H). Contrary, decreasing the parameter k leads to narrower regions of low nucleation probability by decreasing its width laterally (Figure 6B).

To compare to experimental data, we stained α-tubulin in fixed stage 9 wild-type Drosophila oocytes and extracted fluorescence intensity profiles along the cortex from the posterior pole to the anterior corners (Figure 7A,B). An ensemble of smoothed fluorescence profiles shows steep increases in cortical MT density from posterior to anterior, albeit with high variability. Still, a quadratic fit of the ensemble shows that a parabolic function is a plausible representation of the increasing MT density (Figure 7C). Several oocytes show fluorescent profiles that exhibit a local maximum at the posterior. This likely stems from out of plane fluorescence due to the geometric shape of the oocyte pole, and we neglect this minor effect here. At the anterior surface, MT density tends to be more homogeneous with only shallow increases in cortical MT density towards the corners. In summary, for the posterior cap we choose a probability density with parabolic shape that reaches zero at the posterior pole h0P=0,kP=20 (Figure 7D, bottom), whereas for the anterior cap we chose a density with parabolic shape but only shallow depth h0A=0.8,kP=20 (Figure 7D, top).

![Figure 7.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig7-v1.jpg)

**Figure 7.:** (A) α-tubulin staining of a stage 9 oocyte (green) with DAPI staining of DNA (blue). Arrows indicate arclengths sP from the posterior pole to the anterior corners and analogously sA at the anterior. (B) Fluorescence intensity profile (green) with moving average (red) extracted from a 10 pixel wide line along sP indicated in panel A. Arclength was normalized to one, and the minimum intensity of the moving average was subtracted from both fluorescence profiles. (C) Average intensity profiles (red) of cortical MT density as in panel B from N = 15 oocytes. The minimum intensity value across all profiles was subtracted from each. Blue line shows a parabolic fit. (D) Probability densities for the distribution of MT seeding points along anterior arclength (top) and posterior arclength (bottom) used for the wild-type cytoskeleton (blue lines). Black dashed line in bottom panel shows exact parabola. Arclengths are nondimensional lengths with scale L = 50 μm.

#### Generation of seeding points

Discrete seeding points that are randomly positioned along the oocyte membrane according to the probability density $p_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i})$ (Equation 8) can be achieved by inverse transform sampling. To this end, the cumulative distribution function on the anterior (i = A) or posterior (i = P) cap can be computed as

$$
C(ρ′|h_{0}^{i},k_{i})=\int^{​}_{0}^{2\pi}\int^{​}_{0}^{ρ′}dΣ_{i} p_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i}) .
$$

Note that $C(ρ′=1|h_{0}^{i},k_{i})\neq1$ due to normalization across the total oocyte surface rather than across each individual cap. Therefore, random seeding points on each cap can be drawn by applying the inverted cumulative distribution function to a random sample that is uniformly distributed over the interval $[0,C(ρ′=1|h_{0}^{i},k_{i})]$. In this formulation, the total number of seeding points is N = NA + NP (see Figure 6). The ratio of anterior (NA) and posterior (NP) seeding points to be drawn must equal the ratio of total probability for a point to fall on the anterior and posterior caps, respectively. For a fixed value NA, this results in

$$
N_{P}=N_{A} \frac{\int^{​}dΣ_{P} p_{Σ}(s_{P}(ρ)|h_{0}^{P},k_{P})}{\int^{​}dΣ_{A} p_{Σ}(s_{A}(ρ)|h_{0}^{A},k_{A})} .
$$

Here, we generated seeding points in an equivalent way by renormalizing the probability density (Equation 8) on each cap individually as

$$
P_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i})=\frac{1}{A} p˜_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i}) ,
$$

wherein the new normalization factor $A$ is obtained by integration over only one parabolic cap

$$
A(h_{0}^{i},k_{i})=\int^{​}dΣ_{i} p˜_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i}) .
$$

Hence, the corresponding cumulative distribution function

$$
C(ρ′|h_{0}^{i},k_{i})=\int^{​}_{0}^{2\pi}\int^{​}_{0}^{ρ′}dΣ_{i} P_{Σ}(s_{i}(ρ)|h_{0}^{i},k_{i}),
$$

covers the range [0, 1] and seeding points are obtained as $C^{−1}(u)$ for a random sample u with uniform distribution u ∈ [0, 1].

For parabolic caps, the normalization (Equation 16) can not be calculated analytically. Therefore, the probability density (Equation 15) and its cumulative distribution function (Equation 17) were evaluated and inverted numerically. For the special case of a flat anterior (i = A) disc in the alternative geometry-2, the normalization can be solved in closed form as

$$
A(h_{0}^{A},k_{A})=\int^{​}_{0}^{2\pi}dϕ\int^{​}_{0}^{1}dρ ρ p˜_{Σ}(ρ,h_{0}^{A},k_{A})=\pi[(1−h_{0}^{A})k_{A}^{2}+1−(1−h_{0}^{A})k_{A}^{2}(k_{A}^{2}+1)ln(1+1/k_{A}^{2})] .
$$

The corresponding cumulative distributions function evaluates to

$$
C(ρ′)=\int^{​}_{0}^{2\pi}dϕ\int^{​}_{0}^{ρ′}dρ ρ P_{Σ}(ρ,h_{0}^{A},k_{A})=\frac{ρ^{2}[(1−h_{0}^{A})k_{A}^{2}+1]−(1−h_{0}^{A})k_{A}^{2}(k_{A}^{2}+1)ln[1+(ρ/k_{A})^{2}]}{(1−h_{0}^{A})k_{A}^{2}+1−(1−h_{0}^{A})k_{A}^{2}(k_{A}^{2}+1)ln[1+(1/k_{A})^{2}]} ,
$$

which was numerically inverted to generate randomly positioned seeding points on the anterior disc.

Due to the new individual normalization, the values of anterior and posterior probability densities differ at the contact line between anterior and posterior caps. Consider two rings with areas dAi along the contact line ($s=s_{0}^{i}$) on the anterior (i = A) and posterior (i = P) cap which contain $dN_{i}=N_{i} P_{Σ}(s=s_{0}^{i}|h_{0}^{i},k_{i}) dA_{i}$ seeding points. Setting the number of anterior points fixed, and enforcing the point densities to be equal in the corner rings dNA/dAA = dNP/dAP for equal ring areas dAA = dAP allows to compute the number of posterior seeding points as

$$
N_{P}=N_{A}\frac{P_{Σ}(s=s_{0}^{A}|h_{0}^{A},k_{A})}{P_{Σ}(s=s_{0}^{P}|h_{0}^{P},k_{P})},
$$



$$
=N_{A}\frac{A(h_{0}^{P},k_{P})}{A(h_{0}^{A},k_{A})} ,
$$

where the second line follows because $p˜_{Σ}(s_{i}=s_{0}^{i}|h_{0}^{i},k_{i})=1$. Inserting the expression for $A(h_{0}^{i},k_{i})$ (Equation 16) shows that forcing seeding point densities on the anterior and posterior caps to be equal at the anterior corners (Equation 20) is identical to chosing points according to the ratio of total probabilities on the anterior and posterior caps (Equation 14). Thus, chosing points from pΣ normalized over the entire surface (Equation 8) or from $P_{Σ}$ normalized over each cap (Equation 15) is equivalent.

##### Alternative seeding densities

Our model is not sensitive to the exact choice of the probability density for MT seeding points, and here we define alternative seeding densities that are mathematically tractable. Specifically, as randomly positioned seeding points are generated by operating the inverse CDF on a uniformly distributed sample u ∈ [0, 1] and ϕ ∈ [0, 2π), it is convenient to chose the seeding probability such that the CDF can be inverted analytically.

We first note that writing out explicitly the CDF for a rotationally-symmetric probability density function p(si(ρ)) along the arclength (Equation 13) leads to

$$
C(ρ′)=\int^{​}_{0}^{2\pi}dϕ\int^{​}_{0}^{ρ′}dρ p(s_{i}(ρ)) ρ \sqrt{1+(2z_{0}^{i}ρ)^{2}}.
$$

For the case of a gradient of MT seeding points along the arclength of a parabolic cap we can define the density to be

$$
p(s_{i}(ρ))≡p_{n}(ρ|n,z_{0}^{i})=\frac{(n+1) ρ^{n−1}}{2\pi \sqrt{1+(2z_{0}^{i}ρ)^{2}}} .
$$

From Equation 21 this results in a CDF $u≡C_{n}(ρ′)=ρ′^{n+1}$ which can be analytically inverted as $ρ′=C_{n}^{−1}(u)=u^{1/(n+1)}$.

For the case of a uniform distribution of seeding points along the arclength, the probability density is constant and given by the inverse surface area of the parabolic caps (Equation 6)

$$
p(s_{i}(ρ))≡p_{u}(ρ|z_{0}^{i})=\frac{1}{Σ_{i}}.
$$

For $p_{u}(ρ|z_{0}^{i})$ we find the CDF

$$
u≡C_{u}(ρ′)=\frac{(1+(2z_{0}^{i}ρ′)^{2})^{3/2}−1}{(1+(2z_{0}^{i})^{2})^{3/2}−1} ,
$$

which can again be inverted analytically to give

$$
C_{u}^{−1}(u)=\frac{1}{2z_{0}^{i}}\sqrt{(u[(1+(2z_{0}^{i})^{2})^{3/2}−1]+1)^{2/3}−1} .
$$

For the special case of a flat disc, the uniform distribution of seeding points simplifies the CDF to

$$
u≡C_{u}=\int^{​}_{0}^{2\pi}dϕ\int^{​}_{0}^{ρ}dρ \frac{1}{\pi} ρ=ρ^{2},
$$

with inverse $ρ=C_{u}^{−1}(u)=\sqrt{u}$.

For a wild-type cytoskeleton, we impose a uniform MT density $p_{u}(ρ|z_{0}^{i})$ along the anterior cap and a gradient of MTs $p_{n}(ρ|n,z_{0}^{i})$ along the posterior cap. At the contact line between anterior and posterior caps, the seeding densities need to be matched by adjusting the total number of posterior seeding points NP. A ring on the anterior cap at the anterior corners contains dNA = (NA/ΣA)dAA seeding points, while a ring on the posterior cap at the anterior corners contains $dN_{P}=N_{P} p_{n}(ρ=1|n,z_{0}^{P}) dA_{P}$ points. Using Equation 22 and Equation 6 and forcing densities to be equal dNA/dAA = dNP/dAP results in

$$
N_{P}=\frac{N_{A}}{Σ_{A} p_{n}(ρ=1)}
$$



$$
=\frac{3(2z_{0}^{A})^{2}N_{A}}{n+1} \frac{\sqrt{1+(2z_{0}^{P})^{2}}}{(1+(2z_{0}^{A})^{2})^{3/2}−1} .
$$

For the alternative geometry-2 comprised of a posterior parabolic cap and flat anterior disc, matching of seeding densities results in

$$
N_{P}=\frac{2 N_{A}}{n+1} \sqrt{1+(2z_{0}^{P})^{2}} .
$$

Using these alternative seeding densities does not qualitatively change the behavior of the model.

#### MT growth

We describe MTs as persistent random walks, that is, a chain of straight segments of constant length λ that show some flexibility in their relative orientations. The orientation $\mu^_{i}$ of the i-th segment is drawn from a von Mises-Fisher probability distribution on a 2D sphere

$$
f(\mu^_{i}|\mu^_{i−1},κ)=\frac{κ}{4\pi sinh(κ)} e^{κ \mu^_{i}⋅\mu^_{i−1}} ,
$$

where κ is the concentration parameter around the orientation $\mu^_{i−1}$ of the previous segment (see ‘Motor velocity field’ for parameter values). The first orientation $\mu^_{1}$ is drawn from the uniform angular distribution on a 2D sphere (κ = 0) where orientations are rejected if pointing locally outwards of the geometry $n^_{A,P}(ρ,ϕ)⋅\mu^_{1}<0$.

Polymers stop growing if they either encounter a boundary, or if they reach a pre-defined target length l drawn from a probability distribution. The probability density is based on the experimental finding that MTs in vitro undergo a three-step aging process leading to catastrophe, resulting in catastrophe lengths (lc) that follow a Gamma distribution (Gardner et al., 2011). From this catastrophe length distribution, the length distribution observed in an ensemble of growing MTs without shrinkage was calculated as

$$
ϕ_{Γ}(l|n,Λ)=\frac{Γ(n,l/Λ)}{n Λ Γ(n)} ,
$$

where Γ(n, l) is the incomplete Gamma function, Γ(n) is the Gamma distribution, n = 3 is the number of steps to reach catastrophe and Λ is the step length (equivalent to a transition time per step for constant growth velocity, see Gardner et al. (2011)). We set the expectation value $E[ϕ_{Γ}(l|n=3,Λ)]=2 Λ≡N_{Γ}^{−1}$ as fraction ϵ of the AP axis length, hence $Λ=ϵ(z_{0}^{P}−z_{0}^{A})/2$.

Pseudo-random numbers distributed according to this probability density (Equation 30) were generated by inverse transform sampling of the cumulative distribution function

$$
Φ_{Γ}(l|n=3,Λ)=1−\frac{6 Λ^{2}+4 l Λ+l^{2}}{6 Λ^{2}} e^{−l/Λ} .
$$

Similar to the MT seeding densities, the model is not sensitive to the exact choice of the MT length distribution. For example, using the one-parameter exponential distribution

$$
ϕ_{e}(l|Λ)=\frac{1}{Λ} e^{−l/Λ},
$$

as an alternative length distribution and again regulating the expectation value $E[ϕ_{e}(l|Λ)]=Λ=ϵ(z_{0}^{P}−z_{0}^{A})$ of MT lengths via a parameter ϵ does not qualitatively change our results.

#### MT persistence length

The stiffness of a polymer is commonly characterized by its persistence length P, which is defined as the decay length of tangent–tangent correlations. To calculate the persistence length of MT random walks, we first define the end-to-end vector for a polymer with Ns segments of length λ and given initial orientation $\mu^_{1}$ as

$$
R(N_{s}|\mu^_{1})=\lambda\sumi=1N_{s}\mu^_{i}.
$$

Orientations are drawn from a von Mises-Fisher distribution (Equation 29) with mean

$$
〈x^|\mu^〉=\int^{​}x^ f(x^|\mu^,κ)dx^=(\frac{1}{tanh(κ)}−\frac{1}{κ})\mu^≡\sigma \mu^ .
$$

In order to calculate the persistence length of these polymers, we first consider the mean orientations of the second and third MT segments

$$
〈\mu^_{2}|\mu^_{1}〉=\int^{​}\mu^_{2} f(\mu^_{2}|\mu^_{1},κ)d\mu^_{2}=\sigma \mu^_{1} ,
$$



$$
〈\mu^_{3}|\mu^_{1}〉=\int^{​}\mu^_{3}\prodi=23f(\mu^_{i}|\mu^_{i−1},κ)d\mu^_{i}=\sigma^{2} \mu^_{1} ,
$$

and we find in general the relation

$$
〈\mu^_{N_{s}}|\mu^_{1}〉=\int^{​}\mu^_{N_{s}}\prodi=2N_{s}f(\mu^_{i}|\mu^_{i−1},κ)d\mu^_{i}=\sigma^{N_{s}−1} \mu^_{1} .
$$

Hence, using Equation 35 and shifting indices, the expectation value of the end-to-end vector $〈R(N_{s}|\mu^_{1})〉$ is given by

$$
\lambda\sumi=1N_{s}〈\mu^_{i}|\mu^_{1}〉=\lambda\sumn=0N_{s}−1\sigma^{n}\mu^_{1}=\lambda\frac{1−\sigma^{N_{s}}}{1−\sigma} \mu^_{1} .
$$

For stiffness parameter κ → 0 (σ → 0), the von Mises-Fisher distribution becomes a uniform distribution on a 2D sphere. In this case, the polymers curl up with mean end-to-end distance of a single segment

$$
limκ→0〈R(N_{s}|\mu^_{1})〉=lim\sigma→0〈R(N_{s}|\mu^_{1})〉=\lambda \mu^_{1} .
$$

In the opposite limit κ → ∞ (σ → 1), the polymers become stiff rods and are extended to their maximum possible length

$$
limκ→∞〈R(N_{s}|\mu^_{1})〉=lim\sigma→1〈R(N_{s}|\mu^_{1})〉=\lambda N_{s} \mu^_{1} ,
$$

thereby showing that the polymers interpolate between an undirected random walk and completely straight rods.

The persistence length P is defined as the spatial decay length of the correlations of polymer segment orientations $e^{−L/P}=〈cos(\theta)〉≡〈\mu^_{N_{s}}⋅\mu^_{1}〉$. For large L = Ns λ, we have

$$
\frac{1}{P}=−limL→∞\frac{1}{L} ln(〈\mu^_{N_{s}}⋅\mu^_{1}〉)
$$



$$
=−limN_{s}→∞\frac{1}{\lambda N_{s}}ln(\sigma^{N_{s}−1})
$$



$$
≈−\frac{1}{\lambda}ln(\sigma) .
$$

For κ ≪ 1, it holds that $\sigma≈κ/3+O(κ^{3})$ and hence

$$
P≈\frac{\lambda}{ln(3/κ)} ,
$$

whereas for κ ≫ 1 we find

$$
P≈\lambda κ .
$$

Therefore, the persistence length is approximated as segment length λ multiplied by concentration parameter κ.

#### Motor velocity field

From each realization of the MT cytoskeleton in the polymer model, we derive a nondimensional vector field termed motor-velocity field $v′_{m}$ by computing the local vectorial sum of MT segments. To this end, we define a coarse-grained cubic grid with nondimensional side length dG = 0.04 ranging from −1 + dG/2 to 1 − dG/2 in x- and y-direction, and from $z_{0}^{A}+dG/2$ to $z_{0}^{P}−dG/2$ in z-direction. The center point for each MT segment is computed, and the orientations for all MT segments whose center points fall within the same grid volume are vectorially summed to give the average local MT orientation. By normalizing the resulting vector field to a mean vector magnitude of 1, we finally construct the motor-velocity field $v_{m}^{′}$. $v_{m}^{′}$ is used subsequently to compute the cytoplasmic flow field, and to simulate active motor-driven cargo transport on the cytoskeleton.

#### Parameter values

For all computations of the MT cytoskeleton, we used NA = 25000 anterior seeding points, giving a total number of points between N = 55764 for wild-type cytoskeleton and N = 84953 for par-1 null mutants.

The length of an individual MT segment λ needs to be short compared to the system length L, yet long enough to allow simulations of even long MTs with feasible computational effort. Here, we chose λ = 0.015 μm. The maximum number of segments per MT is set to $N_{s}^{max}=200$. Care was taken that few MTs reach the maximum length $\lambda N_{s}^{max}$.

Experimental measurements of MT persistence lengths P are on the order of millimeters (van Mameren et al., 2009). However, the effective persistence lengths of MTs in oocytes is likely shorter due to effects of cytoplasmic flows as well as high density of yolk granules and other obstacles in the cytoplasm that induce MT bending. MTs in the oocyte are neither seen to be completely straight (Figure 8, right), nor strongly curled up (Figure 8, left). Therefore, we chose an intermediate value of κ = 18, corresponding to an effective persistence length (Equation 41) of P ≈ 13.5 μm (Figure 8, center).

![Figure 8.](https://cdn.elifesciences.org/articles/06088/elife-06088-fig8-v1.jpg)

**Figure 8.:** Shown are three cross sections through MT cytoskeletons for indicated values of κ. MTs become stiffer with increasing values of κ. Insets show angular distribution for 3 × 103 points drawn from von Mises-Fisher distribution around mean direction $\mu^=e^_{z}$.

Due to their curved nature, the reach of a MT polymers is effectively shorter than the length of a straight rod composed of the same number of segments. For example, for the chosen values of κ and λ, the end-to-end distance of a MT polymer with N = 25 segments (Equation 36) on average 54% as long as a fully extended polymer or straight rod. Therefore, to compare the MT polymer model to a model in which MTs are represented as straight rods necessitates an adjustment in the mean MT length.

### Rod model for the MT cytoskeleton

#### Model setup

In addition to the polymer model for MTs, we test the net orientation of the cytoskeleton by comparing with a second model in which MTs are nucleated continuously around the cell membrane and act as straight rods with a given length distribution. A single MT from a point σ(ρ, ϕ) on the boundary that hits an observation point x in the volume contributes an orientation vector pointing from σ to x to the observation point. Heuristically, this contribution is expected to be weighted by three different factors: (i) the probability density of MT nucleation pΣ(σ) at boundary point σ(ρ, ϕ), (ii) the probability that the nucleated MT rod is oriented in a direction such that it hits the observation point x, and (iii) the probability that the MT rod is at least long enough to reach from σ to x across a distance $r_{\sigma}=‖x−\sigma‖$. Summing up all the weighted orientational contributions from the entire boundary eventually gives the net orientation at a given observation point inside the oocyte.

We denote the joint probability that a MT rod from the surface element dΣ around a point σ reaches a volume element dV around x by p(x, σ)dΣ dV. p(x, σ) is normalized over the entire oocyte surface area Σ and volume V as

$$
\int_{Σ}dΣ\int_{V}dV p(x,\sigma)=1 .
$$

The marginal distribution pΣ(σ) given by

$$
p_{Σ}(\sigma)=\int_{V}dV p(x,\sigma),
$$

defines the probability density of MT nucleation on the oocyte surface. Conversely, the marginal distribution pV(x)

$$
p_{V}(x)=\int_{Σ}dΣ p(x,\sigma),
$$

is proportional to the total density of MTs that reach the observation point x from the entire boundary. Each individual MT rod contributes an orientation unit vector $e^_{x\sigma}=(x−\sigma)/‖x−\sigma‖$. Thus, the net MT orientation at observation point x corrected for the density of contributing MTs can be calculated as

$$
o(x)=\frac{1}{p_{V}(x)}\int_{Σ}dΣ e^_{x\sigma} p(x,\sigma) .
$$

It is convenient to split the joint probability p(x, σ) into the conditional probability and the probability for MT nucleation at the surface

$$
p(x,\sigma)=p(x|\sigma) p_{Σ}(\sigma).
$$

For the nucleation of MTs on the oocyte surface pΣ(σ), we use the same probability density as in the polymer model (Equation 8). To specify the remaining conditional probability p(x|σ), first note that inserting Equation 46 into Equation 43 imposes the normalization condition

$$
1=\int_{V}dV p(x|\sigma).
$$

Consider a local spherical polar coordinate system (rσ, θσ, ϕσ) centered at a given point σ on the oocyte surface with the zσ-axis identical to the locally inwards pointing normal $n^_{\sigma}$. MT rods are assumed to be oriented in any direction into the positive half space zσ > 0 with equal probability. To determine the general structure of the conditional probability density function p(x|σ), we first assume MT rods of cross sectional area A and fixed length l corresponding to a length distribution

$$
ϕ_{\delta}(r_{\sigma})=\delta(l−r_{\sigma}),
$$

with cumulative distribution function

$$
Φ_{\delta}(r_{\sigma})=\int^{​}_{0}^{r_{\sigma}}dr \delta(l−r)=Θ(r_{\sigma}−l)
$$



$$
=1−Θ(l−r_{\sigma}).
$$

The volume Vc = A l of such a cylindrical MT rod can be approximated as integral over the positive half space by

$$
V_{c}=A\int^{​}_{0}^{l}dr_{\sigma}=A\int^{​}_{0}^{∞}dr_{\sigma} Θ(l−r_{\sigma})
$$



$$
=A\int_{0}^{2\pi}dϕ_{\sigma}\int_{0}^{\pi/2}d\theta_{\sigma} sin(\theta_{\sigma})\int_{0}^{∞}dr_{\sigma} r_{\sigma}^{2}\frac{Θ(l−r_{\sigma})}{2\pir_{\sigma}^{2}},
$$



$$
⇔1=\int_{V}dV \frac{Θ(l−r_{\sigma})}{2\pir_{\sigma}^{2}l} ,
$$

where the last step resulted from division by A l. Comparing this result with Equation 47 and using Equation 49, we identify the conditional probability density function for randomly oriented MTs rods of fixed length as

$$
p(x|\sigma)=N_{\delta} \frac{1}{2\pir_{\sigma}^{2}}[1−Φ_{\delta}(r_{\sigma})] .
$$

Herein, the factor $N_{\delta}=1/l$ corresponds to the mean MT length, the term $(2\pir_{\sigma}^{2})^{−1}$ represents the uniform angular distribution on a half sphere, and the expression [1 − Φ(rσ)] is the probability that MT rods are at least rσ long.

To account for the experimentally measured MT length distribution, Equation 51 is finally generalized by replacing Φδ(rσ) by the cumulative distribution used in the polymer model $Φ_{Γ}(r_{\sigma}|n=3,Λ)$ (Equation 31) with $N_{Γ}=1/(2Λ)$. Thus, the complete joint probability distribution p(x, σ) (Equation 46) for a MT emanating from σ(ρ) and contributing to the net orientation at observation point x in the oocyte volume is defined as

$$
p(x,\sigma)=p_{Σ}(s|h_{0},k) N_{Γ} \frac{1}{2\pir_{\sigma}^{2}}[1−Φ_{Γ}(r_{\sigma}|3,Λ)] .
$$

Note that MT straight rods always cover the distance between nucleation and observation point in a straight line. If the anterior surface is curved inwards, these straight lines can temporarily pass outside of the oocyte geometry before reaching the observation point inside the volume again. The rod model does not prevent such unphysical contributions (though the polymer model does prevent this). However, this error does not occur in a geometry with a flat anterior boundary. Calculation of the cytoskeleton in a geometry with flat anterior (Figure 1—figure supplement 1G) does not change the observed topology, suggesting that in practice this error is negligible.

#### Parameter space and comparison to polymer model

The continuum description of the rod model allows one to follow the saddle-node bifurcation in the MT cytoskeleton precisely throughout parameter space. The creation of stable and unstable fixed points always occurs along the AP axis because the system is rotationally symmetric. We therefore compute the uncorrected net orientation o(x)pV(x) (Equation 45) for observation points x only along the symmetry axis as a function of cortical nucleation parameter kP and mean MT length ϵ.

For a cytoskeletal topology without any fixed point, the x-component ox(x)pV(x) will be pointing towards the posterior pole everywhere along the AP axis. A positive value ox(x)pV(x) > 0 everwhere along the central axis therefore defines the regions of a wild-type cytoskeletal topology. If a pair of a stable and a saddle-node is present, however, ox(x)pV(x) will be negative at least one point along the AP axis, while at the same time it will be positive at the grid point closest to the posterior pole xP where the unstable node creates a limited domain of attraction. Combination of both criteria therefore defines the region of parameter space in which the oocyte is split into two different regions of attraction. Finally, a negative value at the posterior pole ox(xP)pV(xP) < 0 is the signature of a cytoskeleton with only a stable point whose domain of attraction covers the entire volume (see Figure 5).

In the ensemble averages of the polymer model, we find that the bifurcation point occurs for small values of kP if ϵ is large, but shifts to larger values of kP if ϵ becomes smaller. Furthermore, the bifurcation point can be crossed solely by varying ϵ while keeping kP fixed (Figure 4—figure supplement 1). In summary, this confirms that the polymer model exhibits the same parameter space structure as the rod model (Figure 5), thus further supporting the similarity of the two models. Moreover, as in the rod model, this parameter space structure is again insensitive to the oocyte shape.

#### Bifurcation normal form

The saddle-node bifurcation normal form in two dimensions is given by

$$
(v_{x}v_{y})=(x^{2}+\lambda−y) ,
$$

wherein λ is the bifurcation parameter. For negative λ, stable and unstable fixed points exist and are located at $x_{\pm}=\pm\sqrt{−\lambda}$. The critical bifurcation point occurs at λ = 0 (Figure 4—figure supplement 1P–T).

### Additional methods

#### Nondimensionalization and mathematical methods

In dimensional units, the system of transport equations for bound and unbound cargo fractions cb and cu is defined as

$$
\partial_{t} c_{b}+\nabla⋅(v_{m} c_{b})=k_{b} c_{u}−k_{u} c_{b},
$$



$$
\partial_{t} c_{u}+\nabla⋅(u c_{u})=−k_{b} c_{u}+k_{u} c_{b}+D \nabla^{2}c_{u} ,
$$

while the Navier-Stokes-Equations and volume forces are defined by

$$
ρ(\partial_{t} u+(u⋅\nabla)u)=−\nablap+\mu \nabla^{2}u+f,
$$



$$
f=a v_{m} ,
$$

with no-slip boundary conditions on the oocyte surface. Note that cytoplasmic streaming is present in oocytes even when oskar mRNA is not expressed (Palacios and St Johnston, 2002), showing that some cargo other than oskar mRNA is transported by kinesin and responsible for driving flow. This justifies that the parameter a in Equation 56 is independent of the concentration of the bound cargo cb.

Computations of the fluid flow field and simulations of cargo transport are performed using a nondimensionalized version of Equations 54–56. For nondimensionalization, we select a length scale L = 50 μm for scaling of space x = L x′, and an advection scale derived from the active motor-driven transport V = 0.5 μm/s (Zimyanin et al., 2008) for scaling of velocities vm = V vm′, implying an advection time scale τ = L/V = 100 s for scaling of time t = τ t′. $v_{m}^{′}$ denotes the coarse-grained motor-velocity field computed from each realization of the MT polymer model (‘MT persistence length’). Defining the mean raction rate constant K = (kb + ku)/2 and a nondimensional reaction parameter β = kb/(2 K) we find the nondimensional version of Equation 54

$$
\partial_{t′}c_{b}^{′}+\nabla′⋅(v_{m}^{′} c_{b}^{′})=2Da(\betac_{u}^{′}−(1−\beta)c_{b}^{′}),
$$



$$
\partial_{t′}c_{u}^{′}+\nabla′⋅(u′ c_{u}^{′})=2Da(−\betac_{u}^{′}+(1−\beta)c_{b}^{′})+Pe^{−1}\nabla^{′2}c_{u}^{′} ,
$$

where Da = L K/V is the Damköhler number and Pe = L V/D is the Peclet number.

For nondimensionalization of Equations 55, 56, we define scales for the pressure $P=\mu V/L$, force density $F=\mu V/L^{2}$ and force-velocity scaling $A=F/V$ to obtain

$$
Re(\partial_{t}^{′} u′+(u′⋅\nabla′)u′)=−\nabla′p′+\nabla^{′2}u′+f′,
$$



$$
f′=a′ v_{m}^{′},
$$

wherein $p′=p/P$, $f′=f/F$, $a′=a/A$, and Re = ρ V L/μ is the Reynolds number. Note that the Reynolds number is defined using the scale V of the active transport field because the flow velocity field u is derived from it and hence varies. To estimate an upper bound on the Reynolds number, we use the viscosity of water μ = 10−3 Pa s and 10 times the density of water ρ = 104 kg/m3 as lower and upper bounds for the viscosity and density of the cytoplasm in the oocyte. This results in an upper bound Re = 2.5 × 10−4, thus justifying neglecting the inertia terms in Equation 58.

#### Parameter values

The unbinding constant ku can be estimated as ratio of the mean active transport velocity and the mean track length of oskar mRNA in stage 9 oocytes as ku = 0.17 s−1 (Zimyanin et al., 2008). The nondimensional parameter β determines the fraction of cargo that resides in the bound state. Given the fact that 13% of oskar mRNA are bound at any given time we set β = 0.13 (Zimyanin et al., 2008). The unbinding constant ku and β can be used to calculate kb = 0.0255 s−1. Therefore, the mean reaction rate constant and the Damkoehler number are K = 0.0978 and Da = 9.775, respectively. Diffusion of mRNP particles in the ooplasm is widely considered to be very slow. Experimentally measured diffusion constants for mRNA transcripts of sizes similar to oskar mRNA (2.9 kB) in mammalian cells are in the range of D = 0.02 μm/s or lower (Mor et al., 2010). With this value, the Peclet number evaluates to Pe = 1250.

The nondimensional scaling parameter a′ (Equation 56) which converts the active transport velocities into forces acting on the cytoplasmic fluid absorbs several unknown quantities including the size of the cargo that drives fluid flow, drag forces on the fluid with local viscosity, the density of such cargo–motor complexes on MTs and any collective effects. The value of a′ determines the mean nondimensional and dimensional fluid flow speeds $〈|u′|〉$ and $V〈|u′|〉$. We regard a′ as a macroscopic, phenomenological parameter. The value a′ = 45 (a′ = 55 for alternative geometry-2) is calibrated such that the resulting mean dimensional fluid flow speeds $V〈|u′|〉$ match the average fluid flow speeds measured experimentally for stage 9 Drosophila oocytes (see Figure 2) (compare to similar approach in He et al. (2014)).

To test the anchoring mechanism, the bound state is replaced by an anchored state to which cargo can only bind at the extreme posterior pole. For the anchoring state we set $k_{u}^{anch}=0$ s−1 and $k_{b}^{anch}=10 k_{b}$, resulting in βanch = 1 (no unbinding), Kanch = 0.1275, and Daanch = 12.75.

#### Computational methods

For computation of the cytoplasmic flow field and subsequent transport simulations, the motor-velocity field $v_{m}^{′}$ and forces f′ from the MT polymer model are shifted and rotated such that the AP axis aligns with the x-axis and the origin of the coordinate system is located in the oocyte center. To compute the cytoplasmic flow field we use the open source FreeFem++ finite element solver (Hecht, 2012). Forces f defined on a 3D cubic grid are interpolated to the unstructured 3D grid used by FreeFem++, and resulting flow velocity vectors are interpolated back to the cubic grid and derived staggered grids.

Cargo simulations of Equations 57 are performed using custom written Matlab code in finite volume formulation on staggered grids as described in Versteeg and Malalasekera (2007) (custom Matlab code available at http://www.damtp.cam.ac.uk/user/gold/datarequests.html). As nondimensional time step we used Δt = 0.005. Each simulation cycles through many pairs of active transport fields $v_{m}^{′}$ and their corresponding cytoplasmic flow fields u′ to account for a dynamically remodelling cytoskeleton and temporally changing cytoplasmic flow fields. Each pair of $v_{m}^{′}$-u′-fields is active for 432 time steps, corresponding to 3.6 min of simulated real time. The set of $v_{m}^{′}$-u′-fields is pre-computed before the start of the transport simulation.

#### Fly stocks and experimental methods

Oocyte MTs were stained as described by Theurkauf et al. (1992) using a FITC-coupled anti-alpha-tubulin antibody at 1:200 (Sigma-Aldrich, St. Louis, MO). The general shape and size of the oocyte was imaged by recording the fluorescence from a par-1 protein trap (PT) GFP line (Lighthouse et al., 2008). Homozygous or heterozygous par-1 PT flies were also used for measurements of cytoplasmic flows by imaging movements of autofluorescent yolk granules. The allelic combination par-1W3/par-16323 was used for imaging cytoplasmic flows in strong par-1 hypomorphs (Shulman et al., 2000). In all cases of flow measurements, flies were yeast fed overnight, dissected under Voltalef 10S oil and imaged at 40× magnification in a confocal microscope. Cytoplasmic flows were recorded with a 405 nm laser, 4 μs pixel dwell time, collecting 13 frames in 25 s intervals for a total movie duration of 5.17 min.

For the test of oskar mRNA localisation under wild-type conditions we used an oskMS, MS2-GFP line (Belaya and St Johnston, 2011). For cold experiments, flies were kept at room temperature (22°C), yeast fed overnight at 25°C, and subsequently kept at 25°C for 6 hr before dissection and fixation. In situ hybridizations and imaging of living tissue were performed according to standard methods (Palacios and St Johnston, 2002). The bicoid mRNA probe was labeled with Digoxigenin-UTP (Boehringer Mannheim).

#### Data analysis

To compare topologies of in vivo cytoplasmic flows with topologies of numerically computed cytoplasmic flow fields, we used PIV to generate vector fields capturing the instantaneous direction and magnitude of particle movements. PIV was performed using the open source code PIVlab (Thielicke and Stamhuis, 2013), and all PIV vector fields obtained from pairs of consecutive movie frames were averaged over the movie duration. For each movie of cytoplasmic streaming, the mean flow speeds were calculated as the average over all PIV vector magnitudes. Flow speeds obtained from PIV were confirmed by automatic particle tracking using open source code by Blair and Dufresne (Blair and Dufresne, 2013). Only particles that could be tracked in at least three consecutive frames were accepted. Note that instantaneous speeds were computed as ratio of particle distance traveled between frames and frame interval. This method avoids underestimation of flow velocities as was pointed out by authors of Serbus et al. (2005), thereby ensuring that our conclusions about the neglibible contribution of flows to transport remain sound.

### Flow fields and oocyte nucleus

#### Autocorrelation function

Cytoplasmic flow patterns not only show a high variability between different oocytes, but also change over time in any individual oocyte. To estimate the rate of change of individual flow fields we calculate the unbiased, discrete vector autocorrelation over time for the sequence of PIV flow fields in each movie according to the expression

$$
C(k)=〈\frac{1}{N−k}\sumi=x,y\sumn=0N−k(u_{i}(n+k) u_{i}(n))〉,
$$

where angular brackets denote the average across all points of the PIV grid, and the peak value of C(k) is normalized to one. Autocorrelation functions from N = 48 movies exhibit a large spread across generally low correlation values, and an exponential fit gives a decay time constant of 4.4 min.

#### Nucleus to oocyte volume ratio

In 2D confocal images, the oocyte nucleus occasionally appears to cover a significant fraction of oocytes, particularly in young oocytes up to stage 8. To quantify the size of the nucleus compared to the size of the oocyte, we therefore estimate the fraction of the oocyte volume that is covered by the nucleus. We first extract the entire boundary of the oocyte using a custom written macro in Fiji (Schindelin et al., 2012). Averaging the boundary shape from below and above the AP axis results in a symmetrized parametric curve denoted by (x(t), y(t)) (Figure 2—figure supplement 1C, blue curve). After subdividing the boundary into anterior (xA(t), yA(t)) and posterior (xP(t), yP(t)) curve, the volume of the respective solids of revolutions can be computed as

$$
V_{i}=\pi\int^{​}dt(y_{i}(t))^{2}\frac{dx_{i}}{dt} .
$$

While the anterior surface is typically curved inwards for stage 9 oocytes, the anterior surface in young oocytes up to stage 8 can be outwards or inwards curved. Hence, depending on the shape of the anterior the volumes of the anterior VA and VP have to be suitably added or subtracted.

The parabolic caps used in the model geometry (Equation 3) can be parameterized along the z-direction, and in dimensional units their volume is then determined by

$$
V_{i}^{\sigma}=\pi\int_{0}^{L z_{0}^{i}}dz(L\sqrt{1−z/(L z_{0}^{i})})^{2},
$$



$$
=\piL^{3}z_{0}^{i}/2 .
$$

Given that the anterior surface in the standard geometry-1 is curved inwards, the total oocyte volume is given by the difference between between the posterior and the anterior cap volumes $V_{P}^{\sigma}−V_{A}^{\sigma}=\piL^{3}(z_{0}^{P}−z_{0}^{A})/2$.

To approximate the volume of the nucleus, we select its shape and fit a circle to the selection in Fiji. Using the circle radius, we calculate the volume of the nucleus as 4/3πr3. We find that the nucleus generally covers less than 2.5% of the oocyte volume (Figure 2—figure supplement 1), thereby showing that the nucleus volume is negligible even in young stage 9 oocytes, and that 2D confocal images convey a poor impression of 3D volumes. Given the small volume of the nucleus and its location at the anterior of wild type oocytes, the nucleus is unlikely to influence oskar mRNP transport towards the posterior, and we therefore neglect it in simulations of cargo transport.

#### Impact on flow field

The nucleus may be expected to disturb the cytoplasmic flow field by means of adding an additional no-slip boundary condition inside the volume. We tested this effect by including a spherical excluded volume at the oocyte anterior surface in the solution of the 3D Stokes equations (Figure 2—figure supplement 1A,F,H). The nucleus leads to a clear local disturbance of the flow field in a cross section that includes the nucleus compared to the flow field without (Figure 2—figure supplement 1E,F). However, taking a perpendicular cross section through the flow fields in which the nucleus is not visible shows that the nucleus rarely changes the flow field (Figure 2—figure supplement 1G,H). This low sensitivity with respect to excluded internal volumes is due to the fact that flows are driven by volume rather than by boundary forces. Note that the flow fields shown in Figure 2—figure supplement 1 still likely overestimate impact of the nucleus because it generally is not spherical and often seen to squeeze deeply into the anterior corners, therefore reaching far less into the oocyte volume than the idealized sphere used here.
