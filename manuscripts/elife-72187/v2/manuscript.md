# Large-scale orientational order in bacterial colonies during inward growth

## Authors

- Mustafa Basaran<sup>1</sup> ([ORCID: 0000-0002-1895-254X](https://orcid.org/0000-0002-1895-254X))
- Y Ilker Yaman<sup>1</sup> ([ORCID: 0000-0003-4094-616X](https://orcid.org/0000-0003-4094-616X))
- Tevfik Can Yüce<sup>1</sup> ([ORCID: 0000-0002-6888-2690](https://orcid.org/0000-0002-6888-2690))
- Roman Vetter<sup>3</sup> ([ORCID: 0000-0003-2901-7036](https://orcid.org/0000-0003-2901-7036))
- Askin Kocabas<sup>1</sup> ([ORCID: 0000-0002-6930-1202](https://orcid.org/0000-0002-6930-1202)) †

### Affiliations

1. Department of Physics, Koç University Istanbul Turkey ([ROR:00jzwgz36](https://ror.org/00jzwgz36))
2. Bio-Medical Sciences and Engineering Program, Koç University Istanbul Turkey ([ROR:00jzwgz36](https://ror.org/00jzwgz36))
3. Computational Physics for Engineering Materials, ETH Zurich Zurich Switzerland ([ROR:05a28rw58](https://ror.org/05a28rw58))
4. Koç University Surface Science and Technology Center, Koç University Istanbul Turkey ([ROR:00jzwgz36](https://ror.org/00jzwgz36))
5. Koç University Research Center for Translational Medicine, Koç University Istanbul Turkey ([ROR:00jzwgz36](https://ror.org/00jzwgz36))

† Corresponding author

## Abstract

During colony growth, complex interactions regulate the bacterial orientation, leading to the formation of large-scale ordered structures, including topological defects, microdomains, and branches. These structures may benefit bacterial strains, providing invasive advantages during colonization. Active matter dynamics of growing colonies drives the emergence of these ordered structures. However, additional biomechanical factors also play a significant role during this process. Here, we show that the velocity profile of growing colonies creates strong radial orientation during inward growth when crowded populations invade a closed area. During this process, growth geometry sets virtual confinement and dictates the velocity profile. Herein, flow-induced alignment and torque balance on the rod-shaped bacteria result in a new stable orientational equilibrium in the radial direction. Our analysis revealed that the dynamics of these radially oriented structures, also known as aster defects, depend on bacterial length and can promote the survival of the longest bacteria around localized nutritional hotspots. The present results indicate a new mechanism underlying structural order and provide mechanistic insights into the dynamics of bacterial growth on complex surfaces.

## Introduction

Bacterial colonization and invasion are collective phenomena. These processes are regulated through a complex interplay of physical and biological interactions in a crowded population. Bacterial morphology, hydrodynamics, surface topology, and topography markedly alter growth mechanisms, morphology, and overall competition among bacteria (Grant et al., 2014; Su et al., 2012; Volfson et al., 2008; Warren et al., 2019; Cho et al., 2007; Smith et al., 2017). Elucidation of the factors regulating collective bacterial growth and their competition is essential to enhance our understanding of evolutionary dynamics, bacterial infection, and the progression of inflammatory diseases.

A characteristic feature of bacterial colonization is the formation of large-scale order. Rod-shaped bacteria display nematic alignment on surfaces, wherein localized stress, surface friction, and elasticity trigger the formation of ordered domains and lead to the emergence of topological defects (Doostmohammadi et al., 2016; Dell’Arciprete et al., 2018; Doostmohammadi et al., 2018; You et al., 2018; You et al., 2021) and various types of self-assembled structures, including edge fingerings (Farrell et al., 2013) and vertical structures (Beroz et al., 2018; Hartmann et al., 2019).

In particular, ±½ topological defects are the typical orientational singularities observed among growing bacterial colonies and biofilms (Doostmohammadi et al., 2016; Doostmohammadi et al., 2018; You et al., 2018; Yaman et al., 2019). These topological defects have biological significance and regulate stress distribution across the structure, alter the physiology of the cells (Saw et al., 2017), and could control entire morphology; eventually, these effects trigger the formation of fruiting bodies (Copenhagen et al., 2020) and bacterial spores in biofilms (Yaman et al., 2019). Liquid crystal theory has successfully predicted the dynamics of these defects; $-\frac{1}{2}$ defects are stationary whereas $+\frac{1}{2}$ defects are generally motile (Shankar and Marchetti, 2019; DeCamp et al., 2015; Giomi et al., 2013). Another interesting structural order in bacterial colonies is anchoring, where the bacteria are tangentially oriented along the edge of the colony (Su et al., 2012; Doostmohammadi et al., 2016; Dell’Arciprete et al., 2018).

In this study, we assess the orientational dynamics of a crowded bacterial population competing for limited space. Unlike regular expanding colonies, if growing bacteria surround a closed area, domains of inward growth are formed. Under these conditions, entire mechanical interactions differ and lead to the formation of asters, formed as radially aligned +1 topological defects. With only a few exemptions (Maroudas-Sacks et al., 2020; Meacock et al., 2021), higher-order topological defects (Thijssen and Doostmohammadi, 2020; Shankar et al., 2018) are not commonly observed in extensile active matter systems, including growing bacterial colonies. These defects only appear under external modifications such as stress (Rivas et al., 2020), confinement (Duclos et al., 2016; Opathalage et al., 2019), and flow (Martínez-Prat et al., 2019). Our results also reveal that velocity profile is an important factor controlling the emergence of these radially aligned structures. Furthermore, we investigate the invasive advantages of this orientation for competing bacterial strains of different lengths.

Inward growth is commonly observed in various biological systems. During wound healing (Basan et al., 2013), cancer cell growth (Lee et al., 2017; Vader et al., 2009), and retina development (Than-Trong and Bally-Cuif, 2015; Azizi et al., 2020), similar dynamic mechanisms are underway. Our results may provide novel mechanistic insights into these dynamics, particularly on the physical conditions for radial structural alignments during these complex growth processes.

## Results

### Experimental observation of aster structures

To observe the dynamics of inward-growing bacterial colonies, we sparsely spread nonmotile Escherichia coli and Bacillus subtilis separately, on a flat agarose surface (see Materials and methods). Time-lapse fluorescence microscopy was then performed to investigate the temporal evolution of growing colonies. With colony growth, the closed area invaded by multiple colonies was observed across the plate. Rough colony interfaces gradually converge to symmetric, relatively smooth, and enclosed circular areas. We refer to these shrinking circular regions as inward-growing bacterial domains because the growth direction is toward the center of the area. Figure 1 displays typical snapshots of the inward growth process (Figure 1a and b, Video 1, Figure 1—video 1). Unlike regular expanding colonies, the bacterial orientation around these domains is generally radial. To assess the orientation, we first analyzed the radial order parameter $S_{R}$ around the center of these domains. The radial order parameter $S_{R}$ can be expressed as:

$$
⟨S_{R}⟩=\frac{1}{N} \sumicos⁡[2(\theta^{i}−ϕ^{i})]
$$

where $\theta^{i}$ is the angular orientation with respect to x-axis and $ϕ^{i}$ is the angular position of the bacterium i in polar coordinates about the colony center. Figure 1d and c displays the bacterial orientation and order parameter $S_{R}(r)$ as a function of radial distance. $S_{R}=+1$ corresponds to radial alignment and $S_{R}=-1$ corresponds to tangential alignment. It is evident that large-scale radial order emerges across these inward-growing domains (Figure 1c and d). These structures strongly resemble +1 topological defects also known as aster structures. We also measured the velocity of the bacterial flow during this process (Figure 1d). We found that the direction of the flow is toward the center. From these measurements, we can conclude this radial inward flow could align the bacteria in a radial direction.

![Figure 1.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig1-v2.jpg)

**Figure 1.:** (a) Early stage of a closed area surrounded by growing bacterial colonies (Bacillus subtilis). (b) Snapshot of the radially aligned bacterial profile immediately before hole closure. (c) A director field superimposed on an inward-growing domain displaying radial alignment. Scale bar 25 μm. (d) The azimuthally averaged radial order parameter (SR) and velocity against the distance from the colony center for the colony snapshot given in (c). Error bars are defined as s.d. (e,g) Simulation of 2D inward colony growth and regular expansion of bacterial colonies. (f,h) Schematic illustration of the velocity field (black arrow) and frictional force (red arrow) on bacteria in the inward and outward growing domain. Cell colors represent the radial order parameter (SR). Red represents radial alignment; blue, tangential alignment.

![Video 1.](https://cdn.elifesciences.org/articles/72187/elife-72187-video1.mp4.jpg)

**Video 1.:** The video shows the fluorescence image of GFP labeled Escherichia coli (BAK 55) during inward growth. The duration of the experiment is 120 min and the total area is 125 × 125 μm2.

### Numerical simulation of bacterial orientation during inward growth

To clarify the impact of flow-induced alignment and differences in orientation between inward-growing and regular expanding colonies, we simulated 2D bacterial growth using a hard rod model. We used the open-source simulation code GRO (Jang et al., 2012) which provides a fast platform to observe bacterial growth (see Materials and methods). To determine the morphology of the inward-growing domain, we initially distributed bacteria in a random orientation. With growth, bacteria form small colonies, which eventually fuse into a growing annulus (Figure 1e). To visualize the large-scale order, we color-coded bacteria on the basis of their radial orientation, with red representing radial orientation, and blue representing tangential orientation around the center of the hole (Figure 1e, Video 2). These simulation results captured the experimentally observed radial order across the colony.

![Video 2.](https://cdn.elifesciences.org/articles/72187/elife-72187-video2.mp4.jpg)

**Video 2.:** This video is associated with Figure 1f.

However, regular expanding colonies only formed microdomains with random local orientations (Figure 1g, Figure 1—video 2). Regular expanding colonies represent the outward growth initiating from a single bacterium displayed in Figure 1g. Based on these simulations, the primary difference between regular expanding and inward-growing colonies is the sudden change in the direction of the surface drag force which depends on the velocity (Figure 1f and h). In inward-growing colonies, this force flips its sign at a critical radius where the local radial velocity of the colony vanishes.

To further quantify the effects of the critical radius, we determined the stress distribution and radial velocity profile $v_{r}$ , in growing colonies. Figure 2 summarizes the comparison and time evolution of these parameters. We first focused on radial and azimuthal stress profiles. We noted that the stresses ($\sigma_{rr}$ and $\sigma_{\theta\theta}$) (Figure 2—figure supplement 1) are maximum around the critical radius during inward growth (Figure 2a and b). The stress profiles initially show the quadratic form which is particularly dictated by the radial velocity profile (Beroz et al., 2018).

![Figure 2.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig2-v2.jpg)

**Figure 2.:** (a, b) Plot of azimuthally averaged radial stress distribution ($\sigma_{rr}$) at different time points of regular expanding and inward-growing colonies against the distances from the center of the colony. Time points are given in cell division time (t). (c,d) Plot of the azimuthally averaged radial order parameter (SR) across the colonies. Radial order emerges not only below the critical radius but also beyond this level. Negative radial order corresponds to a tangential orientation or active anchoring. (e,f) Comparison of azimuthally averaged radial velocity (vr) profiles of regular expanding and inward-growing colonies. Regular expanding colonies display a linear profile; however, inward-growing colonies form a nonlinear velocity profile. Error bars are defined as s.d. and averaged over 25 simulations. (g) Snapshots of gradual rotation of a single bacterium (green) into a radial orientation during inward growth. Similar bacterial rotation can be seen in experimental results (Figure 2—figure supplement 5).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Plot of azimuthally averaged stress distribution ($\sigma_{\theta\theta}$ and $|\sigma_{r\theta}|$) at different time points of regular expanding and inward-growing colonies against the distances from the center of the colony.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig2-figsupp2-v2.jpg)

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (a) Plot of the radius of the regular expanding colony against time. (b) Plot of the inner and outer radius of the bacterial colony of the inward-growing colony against time. Critical radius is determined by where vr equals to zero. Critical radius shows constant profile immediately before hole closure.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (a) Plot of the inner radius of inward-growing bacterial domain against time. (b) Plot of radial velocity (vr) of the inner edge of the inward-growing bacterial domain in the experiment against time.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig2-figsupp5-v2.jpg)

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** Under both conditions, colonies can develop radial alignment.

Then we observed that, as colonies grew, only inward-growing colonies developed substantial radial order $S_{R}(r)$ (Figure 2c and d). Furthermore, radial velocity profiles $v_{r}$ significantly differed between regular expanding and inward-growing colonies. In contrast with regular expanding colonies, which have a linear radial velocity profile, inward-growing colonies developed radially nonlinear velocity, which vanishes at the critical radius (Figure 2e and f, Figure 2—figure supplement 3). Experimentally, similar profiles were measured (Figure 2—figure supplement 4). This profile gradually rotated the bacteria into the radial direction (Figure 2g, Figure 2—figure supplement 5). Based on these results, the velocity profile appears to be the key physical parameter regulating the flow-induced alignment and the formation of the radial order.

### Velocity profile and radial alignment

To better understand the association between the velocity profile on radial alignment, we first focused on the development of a minimum theoretical model based on active nematics. The theory of active nematics and liquid crystal physics provides a robust framework for understanding the dynamics of bacterial orientation. The primary characteristic of expanding colonies is the constant growth rate of the colony structure. The incompressibility criteria in 2D results in a linear relation between bacterial growth rate and radial velocity profile of the colony, $v_{r}=grr= \frac{Λ}{2}r$ , where $gr$ is the local growth rate and $Λ$ is the exponential bacterial growth rate. These coefficients are related to incompressible expanding bacterial colonies.

This relation was previously referred to as a Hubble-like constant owing to its similarity to the expansion of the universe (Dell’Arciprete et al., 2018). We considered the same approximations to obtain insights into bacterial orientation during inward growth. First, we used the assumption that without molecular field and convection terms, the time evolution of the orientational angle $\theta$ is simply regulated as follows (see Materials and methods):

$$
\frac{d\theta}{dt}=\frac{ξg^{′}r}{2S}sin⁡(2(ϕ−\theta))
$$

where $ϕ$ is the angular position of the bacteria in polar coordinates, and $ξ$ is the flow alignment parameter. Furthermore, $g(r)$ is the local growth rate of the colony and its spatial derivative $g^{′}(r)$ regulating the stability of the bacterial orientation. The constant growth rate observed in regular expanding colonies does not provide any orientational preference, $\frac{d\theta}{dt}=0$. However, this condition significantly differs during inward growth, wherein the local growth rate can be expressed as follows:

$$
g(r)=\frac{v_{r}}{r}=\frac{Λ}{2}\frac{(r^{2}−R_{c}^{2})}{r^{2}} and g^{′}(r)=Λ\frac{R_{c}^{2}}{r^{3}}>0
$$

Our assumption of a constant critical radius (Figure 2—figure supplement 3b) indicates that the spatial derivative of the growth rate is positive everywhere across the colony, $g^{′}(r)>0$, suggesting the possibility of a stable state with $\theta=ϕ$ . The stable radial orientation stimulates aster formation, being referred to as a +1 topological defect. This finding is significant because $g`r\neq0$ is generally possible in compressible structures and also only around leading edges of growing colonies due to sudden drop (Dell’Arciprete et al., 2018). Although bacterial colonies are not compressible, inward growth and the shrinking hole structure alter the overall velocity profile and lead to an essential local growth rate.

The radial orientation is stable throughout the colony and not only below the critical radius. To clarify this point, we simulated colony growth under a fixed circular wall mimicking the stationary critical radius (Figure 2—figure supplement 6). We observed a similar radial alignment. These results indicate the association between the circular confinement owing to the critical radius which dictates velocity profiles and the stability of bacterial orientations.

### Nemato-hydrodynamics and continuum modeling

Thereafter, we investigated whether the same defects were obtained through the continuum nemato-hydrodynamics equations of growing active matter (Giomi et al., 2012; Olmsted and Goldbart, 1992; Mishra, 2017). Due to coarse graining over specific physical details, the continuum model could provide generality of our observation. The model is based on continuity, Navier–Stokes equations, and dynamics of the order parameter tensor $Q$ (see Materials and methods). The coupled differential equations governing the primary material fields density $ρ$, $Q$, and velocity $ν$ can be expressed as follows:

$$
\frac{Dρ}{Dt}=Λρ+D_{ρ}∇^{2}ρ
$$



$$
\frac{D(ρν)}{Dt}= ∇⋅\sigma−\gammaρν
$$



$$
\frac{DQ}{Dt}= ξu+Q⋅\omega−\omega⋅Q+Γ^{−1}H
$$

Here, $\frac{D}{Dt}$ is the material derivative, and the stress tensor is given as:

$$
\sigma=−pI−a(ρ)Q−ξH+ Q⋅H−H⋅Q
$$

Here, $a(ρ)Q$ represents the active stress originating from the extensile nature of bacterial growth. $u$ and $\omega$ are the traceless strain rate and vorticity, respectively (see Materials and methods). The critical parameter $ξ$ is the flow alignment parameter. The details of the frictional drag coefficient per unit density $\gamma$, the molecular field $H$, pressure $p$, rotational diffusion constant $Γ,$ and small diffusion coefficient $D_{ρ}$ are given in Material and methods. These equations were initially solved for growing bacterial colonies (Volfson et al., 2008; Doostmohammadi et al., 2016; Dell’Arciprete et al., 2018; You et al., 2018; Atis et al., 2019) and successfully predicted the active nematic nature and domain formations among colonies of rod-shaped bacteria. We solved them numerically with finite element method (FEM) (see Materials and methods). As a benchmark, we compared the simulations with regular expanding colonies. Figure 3 summarizes the results of these continuum simulations. As expected, regular expanding colonies exhibited only local alignment (Figure 3a and c, Figure 3—video 1) corresponding to microdomains. However, inward-growing colonies developed robust radial alignment and order not only below but also beyond the critical radius (Figure 3b and d, Video 3). Inward-growing colonies also displayed the expected nonlinear velocity profile required for radial alignment (Figure 3e and f , Figure 3—videos 2 and 3, Figure 3—figure supplement 1). Moreover, a sudden drop of the velocity profile near the inner and outer colony edges also resulted in tangential orientation. These results from continuum simulation suggest that similar radial alignment could also be observed in other active matter systems under the same radial velocity profiles.

![Figure 3.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig3-v2.jpg)

**Figure 3.:** (a,b) Scalar order parameter (S) overlapped with the director field pattern of both regular expanding and inward-growing bacterial colonies. Comparison of azimuthally averaged (c,d) radial order parameter (SR) and (e,f) radial velocity (vr) profiles of the colonies against the distance from the center of the colony. In contrast with regular expanding colonies, inward-growing domains developed radial order throughout the colony. A sudden velocity drop near the edge of the colonies resulted in tangential orientation. Error bars are defined as s.d.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a,b) Velocity field superimposed on a density profile of regular expanding and inward-growing colony. (c,d) Plot of azimuthally averaged density against the distance from the colony center for regular expanding and inward-growing colony.

![Video 3.](https://cdn.elifesciences.org/articles/72187/elife-72187-video3.mp4.jpg)

**Video 3.:** The scalar order parameter is overlapped with the director field pattern. This video is associated with Figure 3b.

### Inward-growing domains in multi-layered colonies

Growing bacterial colonies on elastic substrates generally form multi-layered structures. We investigated whether these multi-layered structures could change the radial alignment during inward growth. Herein, experimentally we observed inward-growing domains only around the inner edge surrounded by dense multi-layered structures. This is because merging colonies and the accumulated stress trigger multi-layer formation and limit the size of monolayer region around the edge (Figure 4—figure supplement 1). We investigated whether these multi-layered structures affect the radial alignment during inward growth by performing three-dimensional (3D) FEM simulations based on recently developed algorithms (Yaman et al., 2019; Vetter et al., 2015; Vetter et al., 2013). Our previous computational tool (GRO) cannot simulate bacterial growth in 3D. Our FEM algorithms are relatively slow, but this approach is very powerful to capture detailed bacterial growth in three-dimentional complex environments. The bacterial cells were modeled as growing elastic rods that undergo controlled cell division during colony growth. We first tested the 3D capability of FEM simulations by replicating similar radial alignment under spherical confinement (Figure 4—figure supplement 2). Then we focused on growing colonies on flat surfaces with surface friction. Figure 4 shows the prototypical FEM simulation outcome from inward-growing colonies. As expected, accumulated stress triggers verticalization and multi-layer formation around the critical radius of the colony (Figure 4a and b and Video 4). However, a bacterial monolayer was observed only around the inner and outer leading edges of the colony. The formation of a monolayer region around growing colonies has been investigated in great detail (Warren et al., 2019). We found that these monolayers could also result in planar radial alignment (Video 5). The width of the monolayer was approximately Δr = 90±30 µm (Figure 4c). This width defines the size of the aster structures observed herein.

![Video 4.](https://cdn.elifesciences.org/articles/72187/elife-72187-video4.mp4.jpg)

**Video 4.:** Color represents vertical displacement. This video is associated with Figure 4b.

![Video 5.](https://cdn.elifesciences.org/articles/72187/elife-72187-video5.mp4.jpg)

**Video 5.:** Color represents the radial order parameter. This video is associated with Figure 4a.

![Figure 4.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig4-v2.jpg)

**Figure 4.:** (a,b) Snapshot of inward-growing bacterial domains obtained through the finite element model simulation in 3D. The colors represent (a) the radial order parameter ( $S_{R}$ ) and (b) the vertical displacement of the bacteria during growth. L is the bacterial length. (c) Experimental snapshot of the inward-growing domain indicating the transition between mono- to multi-layer. Δr represents the width of the monolayer bacteria domain.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Using PDMS and glass flat surfaces as vertical confinement, cannot generate large bacterial monolayers. Bright white regions around the center correspond to the second and the third layers. Scale bar corresponds to 100 μm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** A confined colony can develop strong radial alignment. Gray surfaces were added for visualization purposes. Cell colors represent the radial order. The blue color on the surface indicates surface anchoring.

### Inward-growing domains in monolayer colonies

So far, we experimentally studied naturally emerged inward-growing domains on agar surfaces. These domains are randomly formed across the plate. Due to random seeding of bacteria, outward growing edges of multiple colonies merge and form multi-layered structures. In these experiments particularly, the confinement is defined by crowded multi-layered environments. Thus, observing critical radius, outer growing edge and detailed velocity profiles are not possible around these dense regions. Our simulations showed that the initial annulus shape could overcome these limitations. We asked whether we could induce similar annulus structures by patterning the initial distribution of bacteria to observe both inward and outward growing domains. We first tried to imprint bacteria on an agarose surface using soft PDMS molds. However, the wet surface and capillary effect quickly disturbed the initial bacterial patterns defined by the mold. Then we preferred non-contact lithographic techniques for patterning. Using a photomask (Figure 5—figure supplement 1), we exposed randomly distributed bacteria with blue light to define an initial growth geometry by killing the remaining part of the pattern (see Materials and methods). Figure 5a shows the time evolution of growing bacteria starting from annulus-shaped initial distribution. We observed that on a regular agar surface, again multi-layer formation dominates the overall colony morphology. Only very narrow monolayer regions are observable around the inner and outer edges of the colony. We then focus our attention on how to eliminate this multi-layering process. A simple glass or PDMS confinement cannot eliminate this multi-layering (Figure 4—figure supplement 1). Previous studies showed that attractive biochemical interactions between bacteria and surface could generate additional strong friction force (Duvernoy et al., 2018). Altogether friction force, stress accumulation, and verticalization of bacteria in a monolayer colony trigger the formation of these multi-layered structures. This process is mainly controlled by the competition between vertical force and lateral compression in the colony (Grant et al., 2014; Beroz et al., 2018; Duvernoy et al., 2018; You et al., 2019). Above the critical stress level, the orientation of rod-shaped bacteria becomes unstable and triggers the extrusion. Performing FEM simulations, we noticed that this extrusion process occurs around the center of the annuls and it can be controlled by surface friction (Figure 5—figure supplement 2). Although we don’t know the detailed biological mechanism behind the friction force, it is evident that minimizing the surface friction can increase the size of the monolayer colony. Then, we tested the same bacterial patterning on different membranes to find a surface with low friction by minimizing biochemical interaction. We noted that only polycarbonate (PC) surfaces are useful for this purpose, and they support large monolayer colonies while providing a sufficient bacterial growth rate (Figure 5—figure supplement 3, Figure 5—video 1, see Materials and methods). The size of these monolayer colonies was approximately 600 µm. As we observed in our previous simulations (Figure 4), at a later stage, the second layer formation appeared around the center of these annulus shapes which is close to the critical radius (Figure 5a, Figure 5—video 2). Similarly, we observed strong radial alignment across the colony (Figure 5c and d, Figure 5—figure supplements 4 and 5). We did not observe any radial alignment in regular isolated monolayer colonies. Instead, we clearly observed orientational defects and microdomains in these monolayer colonies on PC surfaces (Figure 5—figure supplement 6). Inward and outward growing monolayer domains also provided the nonlinear velocity profile (Figure 5e), which is essential for radial alignment. We noticed that during this process critical radius shows a constant profile (Figure 5f, Figure 5—figure supplement 7, Figure 5—video 2). The other interesting form of bacterial growth is biofilm formation which has filamentous and nematic internal structures. As a next step, we similarly tested the radial alignment dynamics of these bacterial biofilms during the inward growth process, starting from the same initial distribution. We used a biofilm-forming strain B. subtilis 168 (Yaman et al., 2019) and observed similar strong radial alignment across the biofilms (Figure 5—video 3, Figure 5—figure supplement 8). Our FEM simulations also captured the alignment process of growing elastic bacterial biofilm structures (Figure 5—video 4, Figure 5—figure supplement 8c,d).

![Figure 5.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-v2.jpg)

**Figure 5.:** (a,b) Snapshot of inward-growing bacterial colonies (Bacillus subtilis) on different surfaces. Initial bacterial distribution is defined by non-contact lithographic techniques with blue light exposure. Inward-growing domains are formed by merging colonies originating from annulus-shaped initial distribution. (a) On an agarose surface, growing colonies easily form multi-layer structures and provide narrow monolayer inward-growing domains. However, (b) on a low friction polycarbonate (PC) surface, bacteria form monolayer colonies and provide large-scale inward-growing domains. Scale bar 500 μm. (c) Magnified fluorescence image superimposed with director field of the inward-growing domain indicating the radial alignment of bacteria. Δr represents the width of the monolayer region. Scale bar 50 μm. (d) Radial order parameter (SR) and (e) radial velocity profile (vr) as a function of distance across the monolayer colony. Velocity profile was extracted by using PIV algorithms around the center of the annulus shape (Figure 5—video 2). (f) The experimentally measured inner and outer and critical radius. d, e, f are averaged over four different colonies, starting from the same initial annulus-shaped distribution.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp1-v2.jpg)

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Snapshot of inward-growing bacterial domains with the color representing compressive stress (a) on individual bacteria, velocity profile (b), and azimuthally averaged $\sigma_{rr}$ radial, $\sigma_{\theta\theta}$ hoop stress, the velocity profile, and the positions of the first five extrusion events triggering the multi-layering process (c).(d–f) Snapshot of the colonies under different surface friction. Snapshots were taken during the first extrusion event before multi-layer formation. The first verticalization processes are shown in red circles. (g) The width of the monolayer colony obtained through the finite element model simulation on flat surfaces as a function of friction coefficients.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Nutrition can leak from Luria-Bertani (LB) plate through the holes and provide a sufficient growth environment for bacteria.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** The bottom edge corresponds to the inner radius of the annulus shape. Large-scale radial alignment occurs around the colony. Scale bar 50 μm.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** The bottom side corresponds to the inner leading edge of the colony. Scale bar 50 μm.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp6-v2.jpg)

**Figure 5—figure supplement 6.:** Scale bar 50 μm.

![Figure 5—figure supplement 7.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp7-v2.jpg)

**Figure 5—figure supplement 7.:** Scale bar 20 μm. The left side corresponds to the inward-growing domain.

![Figure 5—figure supplement 8.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig5-figsupp8-v2.jpg)

**Figure 5—figure supplement 8.:** (a) Time evolution of growing chaining bacterial colonies starting from annulus-shaped initial geometry. (b) Magnified fluorescence images indicating the radial alignment of the biofilm around the inner radius. The regions are highlighted in (a). (c) Finite element method (FEM) simulation of growing biofilm structure. (d) Magnified images of simulation results indicating the radial alignment.

### Biological significance

Finally, to assess the biological significance of radial alignment, we investigated whether these structures potentially affect the competition among bacteria during inward growth. In general, near the leading edge of a bacterial colony, competition strongly depends on physical parameters. The most prominent example is a genetic drift based on random fluctuations (Hallatschek et al., 2007; Kayser et al., 2018). This phenomenon could be altered through steric interactions among the cells, which can potentially alter the evolutionary dynamics of competing bacteria (Farrell et al., 2017). Although bacterial orientation is generally tangential at the expanding colony edge, radial bacterial alignment potentially contributes to inward growth. We hypothesized that longer rod-shaped bacteria potentially have an advantage owing to the torque balance. The basic premise is that the torque depends on the length of the bacteria, resulting in rapid radial alignment. Radial alignment further leads to lane formation and promotes an invasive advantage to the longest one, which could be beneficial in terms of approaching nutritional hotspots localized around the defect core more effectively.

To assess this competition, we initially simulated the growth dynamics of a mixed population with different division lengths from the same random initial distribution on a circle (Figure 6—figure supplement 1). This is the most challenging condition to test the impact of the length difference on the bacterial alignment. Although the initial distribution of the bacteria is random, long bacteria can develop a higher radial order during inward growth (Figure 6a–f). This radial order gradually allows the longest bacteria to approach the center of the defect more effectively (Figure 6g). The bacterial growth is local, and it can create strong segregation within the colonies. The impact of the length could be more significant in segregated colonies. To visualize the difference, we initially segregated the bacterial strains with different lengths around the edge of the colony. Similar segregation can be commonly observed around the edge of the colony owing to random fluctuations. These segregations can also occur during inward growth (Figure 6—figure supplement 2). Instead of expanding segments owing to perimeter inflation, we observed shrinking segments owing to the deflation of the hole geometry. Computationally, the advantage of radial alignment was more evident in segregated bacterial colonies (Figure 6h). Interestingly, in a monolayer colony, radial alignment promotes the invasion of both the center and the leading outer edge of the colony through the longest bacteria (Figure 6g). After the complete invasion of the center, the radial lanes buckle (Figure 6—figure supplement 3, Videos 6 and 7). However, experimental verification of this competition remains challenging. Although precise regulation of the aspect ratio of bacterial morphology is well established (Dion et al., 2019), cell length can still not be independently tuned without perturbing other essential physiological properties, including growth rate and the biofilm-forming potential of the bacteria.

![Video 6.](https://cdn.elifesciences.org/articles/72187/elife-72187-video6.mp4.jpg)

**Video 6.:** RFP and GFP labeled bacteria are initially segregated. Color represents the bacterial type. This video is associated with Figure 6h.

![Video 7.](https://cdn.elifesciences.org/articles/72187/elife-72187-video7.mp4.jpg)

**Video 7.:** RFP and GFP labeled bacteria are initially segregated. Color represents the bacterial type. This video is associated with Figure 6h.

![Figure 6.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig6-v2.jpg)

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Starting from random initial annulus distribution, the longest bacteria could develop higher radial order (SR ) shown in Figure 6a–c. The zoomed versions of (SR ) are given in Figure 6a. This packed and random distribution is hypothetical initial distribution to test the worst-case scenario to challenge bacterial competition. The relative packing fraction is shown in Figure 6g.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Competing RFP and GFP labeled, identical bacterial strains were mixed and printed on an agar surface using a sharp cylindrical object.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/72187/elife-72187-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** The longest bacteria can invade the center more effectively. After a complete invasion of the center, the radial lanes buckle.

## Discussion

Radially aligned structures can be considered as a +1 aster defect. These are ubiquitous topological structures observed in biological (Roostalu et al., 2018; Ross et al., 2019; Kruse et al., 2004; Julicher et al., 2007) or synthetic (Sokolov et al., 2019; Snezhko and Aranson, 2011) active matter systems. For instance, microtubules can form nematic alignment or asters during mitosis, depending on the extensile or contractile activity. Bacterial colonies can be considered an extensile active material platform, generally supporting the formation of only ±½ topological defects. This study shows that stable radially aligned, aster structures can also emerge during inward growth. In particular, we report the critical role of the colony velocity profile during this process, which depends on numerous factors. Although the bacterial growth rate is constant throughout the colony, growth geometry, confinement, or boundary conditions can alter the velocity profile. Together, these biomechanical interactions change the bacterial orientation and stability, thus generating ordered structures. Different types of ordered structures have been observed in bacterial biofilms (Yan et al., 2016) and 3D colonies (Warren et al., 2019). Furthermore, we believe that the velocity profile of growing structures on flat surfaces plays a significant role in bacterial alignment. Future studies are required to investigate the contribution of these effects.

We should emphasize that inward-growing bacterial colonies and wrinkling thin circular sheets have geometric similarities (Davidovitch et al., 2011). In these elastic circular objects, under axisymmetric tensile load, azimuthal stress (hoop stress, $\sigma_{\theta\theta}$ ) show transition from tensile to compressive profile which eventually creates radial wrinkling pattern below critical radius. However, unlike elastic objects, growing bacterial colonies can only develop compressive stress due to negligible attractive force between bacteria. Experimental measurement of internal stress could provide more details, but it remains challenging. We noticed that the packing fraction of the bacteria shows a correlated profile (Figure 2—figure supplement 2). However, particularly for aligned bacteria, it is still very difficult to extract this information. In the future, new molecular probes could be useful for the experimental measurement of accumulated stress in the bacterial colonies (Chowdhury et al., 2016; Prabhune et al., 2017).

Finally, this study reveals the potential biological significance of radial alignment during the invasion. These ordered structures provide additional advantages and promote the survival of the longest bacteria. These results link the orientational properties and competition dynamics of bacterial colonies. Our findings are of potential relevance for the understanding of complex dynamics of bacterial infections and the progression of inflammatory diseases.

## Materials and methods

### Bacterial preparation and growth conditions

Bacterial cultures (BAK47 and BAK51) were grown in Luria-Bertani (LB) broth at 37°C on a shaker. An overnight culture was diluted 100× and grown for 8 hr. The culture was diluted 10,000×, and 10 µl of culture was seeded on an LB agarose plate. These isolated bacteria on plates were grown at 21°C for 12 hr and then imaged. Strains used in experiments are described in Table 1. In B. subtilis bacterial strains, the flagella-producing gene (hag) was mutated to eliminate the swimming-induced motion. The background strain TMN1138 was obtained from R Losick Lab.

**Table 1.**
 List of strains used in this study.


<table>
  <thead>
    <tr>
      <th>Strain</th>
      <th>Parent</th>
      <th>Operation</th>
      <th>Genotype</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BAK47</td>
      <td>168</td>
      <td>Transformed with plasmid ECE321 from Bacillus Genetic Stock Center</td>
      <td>amyE::Pveg-sfGFP (Spc)</td>
    </tr>
    <tr>
      <td>BAK115</td>
      <td>TMN1138</td>
      <td>Transformed with plasmid ECE327 from Bacillus Genetic Stock Center</td>
      <td>amyE::Pveg-mKate (Spc) sacA::Phag-mKate2L (Kan) hagA233V (Phleo)</td>
    </tr>
    <tr>
      <td>BAK51</td>
      <td>TMN1138</td>
      <td>Transformed with plasmid ECE321 from Bacillus Genetic Stock Center</td>
      <td>amyE::Pveg-sfGFP (Spc) sacA::Phag-mKate2L (Kan) hagA233V (Phleo)</td>
    </tr>
    <tr>
      <td>BAK 55</td>
      <td>DH5alpha</td>
      <td>Transformed with plasmid 107741 from Addgene</td>
      <td>pDawn-sfGFP</td>
    </tr>
  </tbody>
</table>

### Microscopy imaging

Fluorescence time-lapse imaging was performed using a Nikon inverted and Stereo SMZ18 microscopes. Images were obtained using a Andor EMCCD camera. Time intervals between successive images were set to 5–10 min.

### 2D hard-Rod simulations of a growing colony

We used the open-source simulation program GRO based on a hard-rod model. The code is available from https://depts.washington.edu/soslab/gro/. We modified the original code to be able to change the initial bacterial position and to extract the orientation of the bacteria. Sample files and scripts used for modifications are available on GitHub (https://github.com/mustafa-basaran/Large_Scale_Orientation_Bacteria, copy archived at swh:1:rev:fd7673254fa57874676b183f9a944d9e457c3ac0; Basaran, 2021).

### Bacterial patterning

We used photolithographic techniques to define the initial distribution of the bacteria by killing with structured blue light illumination. We used 15 min exposure under 5 mW/mm2 480 nm uniform light beam. We think the killing mechanism is mainly based on the local drying process. The geometry was defined by chromium photomask. The mask (Figure 5—figure supplement 1) was fabricated by using Heidelberg DWL 66+ Direct Writing Lithography System and developed with chromium etchant. We have tested different annulus-shaped patterns by tuning the inner and outer radius. Due to light diffraction, the final exposed pattern depends on the spacing between the PC filter and a mask. Our optimized pattern has 400 μm inner and 800 μm outer radius.

### Growing monolayer colonies on low friction surfaces

In order to minimize surface friction, we replaced the agarose surface with a filter membrane. We have tested several membrane filters, including nylon, polycarbonate (PC), polyethersulfone, cellulose acetate. Only white PC filters with 0.4 μm pore size supported stable and large-scale monolayer colony formation. We noted that the brown PC filter has similar low surface friction; however, it has strong light absorption and does not allow noncontact lithography due to heavy condensation on the photomask.

### SEM imaging

A PC filter paper with a pore size of 0.4 µm was placed on LB agar surface. After seeding the 10,000× diluted bacteria on the filter paper, bacteria were grown on the paper for 12 hr at 21°C. Then the filter paper was peeled off from the surface, and the colonies were fixed using paraformaldehyde and left to dry. Fixed colonies were coated with 20 nm gold and imaged using a Zeiss Ultra Plus Field Emission Electron Microscope.

### Calculating stress distribution in a growing colony

The stress inside the colony can be calculated from the virial expansion (Volfson et al., 2008) $\sigma_{i}= \frac{1}{2a_{i}^{`}}\sumjr_{ij}F_{ij}$ , $a_{i}^{`}$ is the effective area, $r_{ij}$ is the position of the contact, and $F_{ij}$ is the interaction force between the cells. Using the following transformations, we calculated the stress in polar coordinate

$$
\sigma_{rr}= \sigma_{xx}∗cos^{2}⁡(\theta)+\sigma_{yy}∗sin^{2}⁡(\theta)+\sigma_{xy}∗sin⁡(\theta)∗cos⁡(\theta)
$$



$$
\sigma_{\theta\theta}= \sigma_{xx}∗sin^{2}⁡(\theta)+\sigma_{yy}∗cos^{2}⁡(\theta)+\sigma_{xy}∗sin⁡(\theta)∗cos⁡(\theta)
$$



$$
\sigma_{\thetar}= cos⁡(\theta)sin⁡(\theta)(\sigma_{yy}−\sigma_{xx})+\sigma_{xy}∗cos⁡(2∗\theta)
$$

Due to negligible lateral friction between bacteria, we ignore $\sigma_{xy}$ and our equations become:

$$
\sigma_{rr}= \sigma_{xx}∗cos^{2}⁡(\theta)+\sigma_{yy}∗sin^{2}⁡(\theta)
$$



$$
\sigma_{\theta\theta}= \sigma_{xx}∗sin^{2}⁡(\theta)+\sigma_{yy}∗cos^{2}⁡(\theta)
$$



$$
\sigma_{\thetar}= cos⁡(\theta)sin⁡(\theta)(\sigma_{yy}−\sigma_{xx})
$$

### 3D FEM simulations of growing bacterial colonies

For the 3D computer simulations, we employed an open-source (https://libmesh.github.io/) parallel finite element library written in C++ (Vetter et al., 2013). Sample files and scripts used for analysis are available on GitHub (https://github.com/mustafa-basaran/Large_Scale_Orientation_Bacteria, copy archived at swh:1:rev:fd7673254fa57874676b183f9a944d9e457c3ac0; Basaran, 2021). Analogous to Yaman et al., 2019, the bacteria were modeled as an isotropic, linearly elastic continuum whose initial stress-free shapes were spherocylinders. The bacteria were assumed to maintain a uniform circular cross-section with radius $r=0.5 m$, a mass density of $1gcm^{-3}$ , a Young’s modulus of $E=5300Pa$, and a Poisson ratio of $ν=⅓$ 1/3. The total elastic energy U of each bacterium comprised the usual terms for axial dilatation or compression, bending, and torsion (Vetter et al., 2015):

$$
U= \frac{E\pir^{2}}{2}\int_{0}^{L}\epsilon^{2}+\frac{r^{2}}{4}κ^{2}+\frac{1}{1+ν}\phi^{2}ds
$$

where $L$ denotes the bacterium length, $\epsilon$ the axial Cauchy strain, $κ$ the scalar midline curvature, and $\phi$ the twist per unit length. Hertzian steric forces were exchanged between overlapping bacterial elements in a normal direction. Tangential forces and torques exchanged during contact between bacterium pairs and between bacteria and the substrate was computed with a slip-stick friction model with a uniform isotropic Coulomb friction coefficient. We modeled the substrate as an elastic half-space onto which the bacterial colony was placed, and exerted a perpendicular gravitational force on the bacteria. The bacteria were grown exponentially in length over time by continuously increasing each element’s equilibrium length. For this study, the finite element program was extended to allow for cell division when the bacterial length surpassed a division threshold $L_{\theta}=5 m$. When $L>L_{\theta}$ , the bacteria were split into two pieces at a random position drawn from a normal distribution about their center with a standard deviation of $L/10$, but no further away from the center than $L/5$. To evolve the colony in time, Newton’s translational and rotational equations of motion were integrated with a Newmark predictor-corrector method of second order. To equilibrate the colony during growth, viscous damping forces were added.

In order to simulate inward-growing biofilm structure, we used our previous biofilm model (Yaman et al., 2019) and the same parameters. Eight identical replica of small biofilm structures are circularly distributed to form an initial annulus shape. We used fracture strain (0.3) to relax the extreme bending condition by triggering filament division.

### Radial velocity profile

To calculate radial velocity profile, $v_{r}$ , during inward growth, we assume there is a critical radius $R_{c}$ , where $v_{r}$ is equal to zero. For $r<R_{c}$ and the initial domain size equals to $A_{in}$ :

$$
At=A_{in}e^{Λt}=\piR_{c}^{2}-r^{2}
$$

If we take derivative wrt time.

$$
A_{in}Λe^{Λt}=-2\pir\frac{dr}{dt}
$$



$$
v_{r}r,t=\frac{dr}{dt}=-\frac{ΛAt}{2\pir}=\frac{Λr^{2}-R_{c}^{2}}{2r}
$$

For outer growth where $r>R_{c}$

$$
At=A_{out}e^{Λt}=\pir^{2}-R_{c}^{2}
$$

Similarly, the time derivative is

$$
A_{out}Λe^{Λt}=2\pir\frac{dr}{dt}
$$



$$
v_{r}r,t=\frac{dr}{dt}=\frac{ΛAt}{2\pir}=\frac{Λr^{2}-R_{c}^{2}}{2r}
$$

which results in the same equation. Consider that for $r$ lower than $R_{c}$ , velocity will be negative (inward direction) and for $r$ greater than $R_{c}$ velocity will be positive (outward direction).

### Continuum modeling

For the continuum modeling, Equations 4–7 were solved with the FEM in COMSOL Multiphysics. The material derivative is given by $D/Dt=\partial_{t}+v∙\nabla+\nabla∙v$ . $u$ and $\omega$ are the strain rate and vorticity tensors, respectively, with components $u_{ij}=\partial_{i}v_{j}+\partial_{j}v_{i}-\delta_{ij}\nabla∙v/2$ and $\omega_{ij}=\partial_{i}v_{j}-\partial_{j}v_{i}/2$ . We constructed a traceless and symmetric Q-tensor field:

$$
Q_{\alpha\beta}=Sn_{\alpha}n_{\beta}-\frac{1}{2}\delta_{\alpha\beta}
$$

and we defined scalar order parameter:

$$
Sr=2\sqrt{Q_{xx}^{2}r+Q_{xy}^{2}r}
$$

The molecular field $H$ can be obtained starting from the Landau-de Gennes free energy density given as:

$$
f_{LdG}=\frac{1}{2}Κ\nablaQ^{2}+\frac{1}{2}\alphaρtrQ^{2}+\frac{1}{4}\betaρtrQ^{2}^{2}
$$

Therefore, $H=\delta/\deltaQ \intdAf_{LdG}=Κ\nabla^{2}Q-\alphaρQ-\betaρtrQ^{2}Q$. In the simulations, the relationships $aρ=a_{0}ρ$ ,$\betaρ=\frac{\alpha_{0}}{2}ρ$, $\alphaρ=\alpha_{0}ρ_{c}-ρ$, and $p=G*max\frac{ρ}{ρ_{0}}-1,0$ were used. We set the initial cell density $ρ_{0}=1$, growth rate $Λ=0.005$, frictional drag coefficient per unit density $\gamma=0.2$ , flow aligning parameter $ξ$ = 0.7, rotational diffusion constant $Γ=1$, and the remaining parameters $a_{0}=0.002$, $\alpha_{0}=0.01$, $ρ_{c}=ρ_{0}/2=0.5$, $G=2$, $D_{ρ}=0.04$, $Κ=0.01$.

### Approximation for growth-induced alignment

The following approximation and equations are received from Dell’Arciprete et al., 2018. These approximations were used to explain the tangential alignment of bacteria at the edge of growing colonies. The equation of motion for 2D nematodynamics without any free energy and no spatial variation of $Q$ can be written as:

$$
\frac{\partialQ_{\alpha\beta}}{\partialt}+v_{\gamma}\partial_{\gamma}Q_{\alpha\beta}=ξu_{\alpha\beta}-Q_{\alpha\gamma}\omega_{\gamma\beta}+\omega_{\alpha\gamma}Q_{\gamma\beta}
$$

If we assume

$$
v_{r}=grr
$$

From this formulation we can conclude that:

$$
v_{\alpha}=grx_{\alpha}
$$

where $x_{\alpha}$ is the Cartesian component of the position vector

$$
\partial_{\beta}v_{\alpha}=g\delta_{\alpha\beta}+g`rr_{\alpha}r_{\beta}
$$

where $r_{\alpha}=\frac{x_{\alpha}}{r}$. Now this tensor is symmetric, with calculating $u_{\alpha\beta}$ and $\omega_{\alpha\beta}=0$ putting it in Equation 17 above we get:

$$
\frac{\partialQ_{\alpha\beta}}{\partialt}=ξg`rr_{\alpha}r_{\beta}-\frac{\delta_{\alpha\beta}}{2}
$$

With writing $Q_{\alpha\beta}$ using:

$$
Q_{\alpha\beta}=S[cos^{2}⁡\theta−\frac{1}{2}sin⁡\thetacos⁡\thetasin⁡\thetacos⁡\thetasin^{2}⁡\theta−\frac{1}{2}]
$$



$$
=\frac{S}{2}[cos⁡(2\theta)sin⁡(2\theta)sin⁡(2\theta)−cos⁡(2\theta)]
$$

In polar coordinates $r,ϕ$ right-hand side of Equation 21 is:

$$
\frac{∂Q}{∂t}=\frac{ξg^{′}r}{2}[cos⁡(2ϕ)sin⁡(2ϕ)sin⁡(2ϕ)−cos⁡(2ϕ)]
$$

If we combine Equation 23 and Equation 24:

$$
−Ssin⁡(2\theta)\frac{d\theta}{dt}=\frac{ξg^{′}r}{2} cos⁡(2ϕ)
$$



$$
Scos⁡(2\theta)\frac{d\theta}{dt}=\frac{ξg^{′}r}{2} sin⁡(2ϕ)
$$

Multiply first equation (Equation 25) by $-sin2ϕ$ and second equation (Equation 26) by $cos2ϕ$ and sum them up:

$$
\frac{d\theta}{dt}=\frac{ξg^{′}r}{2S}[sin⁡(2ϕ)cos⁡(2\theta)−cos⁡(2ϕ)sin⁡(2\theta)]
$$



$$
\frac{d\theta}{dt}=\frac{ξg^{′}r}{2S}sin⁡(2(ϕ−\theta))
$$

Thus if $g^{′}>0$, equation above has a stable equilibrium for $\theta=ϕ$ (aster).

### Code availability

The codes utilized previously published open-source software from https://depts.washington.edu/soslab/gro/ and are made available on GitHub (https://github.com/mustafa-basaran/Large_Scale_Orientation_Bacteria, swh:1:rev:fd7673254fa57874676b183f9a944d9e457c3ac0; Basaran, 2021).
