# Size-dependent patterns of cell proliferation and migration in freely-expanding epithelia

## Authors

- Matthew A Heinrich<sup>1</sup> ([ORCID: 0000-0002-9041-5554](https://orcid.org/0000-0002-9041-5554))
- Ricard Alert<sup>2</sup> ([ORCID: 0000-0002-1885-9177](https://orcid.org/0000-0002-1885-9177))
- Julienne M LaChance<sup>1</sup>
- Tom J Zajdel<sup>1</sup>
- Andrej Košmrlj<sup>1</sup> ([ORCID: 0000-0001-6137-9200](https://orcid.org/0000-0001-6137-9200))
- Daniel J Cohen<sup>1</sup> ([ORCID: 0000-0001-5819-1135](https://orcid.org/0000-0001-5819-1135)) †

### Affiliations

1. Department of Mechanical and Aerospace Engineering, Princeton University Princeton United States
2. Lewis-Sigler Institute for Integrative Genomics, Princeton University Princeton United States
3. Princeton Center for Theoretical Science, Princeton University Princeton United States
4. Princeton Institute for the Science and Technology of Materials (PRISM), Princeton University Princeton United States

† Corresponding author

## Abstract

The coordination of cell proliferation and migration in growing tissues is crucial in development and regeneration but remains poorly understood. Here, we find that, while expanding with an edge speed independent of initial conditions, millimeter-scale epithelial monolayers exhibit internal patterns of proliferation and migration that depend not on the current but on the initial tissue size, indicating memory effects. Specifically, the core of large tissues becomes very dense, almost quiescent, and ceases cell-cycle progression. In contrast, initially-smaller tissues develop a local minimum of cell density and a tissue-spanning vortex. To explain vortex formation, we propose an active polar fluid model with a feedback between cell polarization and tissue flow. Taken together, our findings suggest that expanding epithelia decouple their internal and edge regions, which enables robust expansion dynamics despite the presence of size- and history-dependent patterns in the tissue interior.

## Introduction

Writing in 1859, physiologist Rudolf Virchow presented the concept of the ‘Zellenstaat’ or ‘Cell State,’ describing tissues as ‘a society of cells, a tiny well-ordered state’ (Virchow, 1855). This social framework motivated Abercrombie and Heaysman, 1954 work on cellular behavior that elucidated how encounters between cells can regulate locomotion and proliferation via contact inhibition. Since then, concerted interdisciplinary effort has been brought to bear on understanding how cell-cell interactions give rise to the complex collective behaviors driving so many crucial biological processes. One of the most foundational collective behaviors is collective cell migration—the directed, coordinated motion of cellular ensembles that enables phenomena such as gastrulation, wound healing, and tumor invasion (Friedl and Gilmour, 2009). Given this importance, considerable effort spanning biology, engineering, and physics has been directed towards understanding how local cellular interactions can give rise to globally coordinated motions (Alert and Trepat, 2020; Hakim and Silberzan, 2017).

Studies of collective cell migration are most often performed using epithelial tissues due to their fundamental role in multicellular organisms and strong cell-cell adhesion, which in turn gives rise to elegant, cohesive motion. Moreover, given that epithelia naturally form surfaces in vivo, studying epithelial layers in vitro has a physiological basis that can inform our understanding of processes such as healing (Poujade et al., 2007), envelopment (Steinberg, 2007), and boundary formation (Dahmann et al., 2011). These features have made epithelia both the gold standard in collective cell migration studies, and one of the most well-studied models for biological collective behaviors.

Due to the complexity of collective behaviors, much effort has gone towards reductionist assays that restrict degrees of freedom and ensemble size to simplify analysis and interpretation. One such approach is to confine a tissue within predefined boundaries using micropatterning to create adhesive and non-adhesive regions (Doxzen et al., 2013; Deforet et al., 2014; Notbohm et al., 2016; Pérez-González et al., 2019; Peyret et al., 2019; Petrolli et al., 2019). Such confinement mimics certain in vivo contexts such as constrained tumors as well as aspects of compartmentalization during morphogenesis (Lecuit and Lenne, 2007). Alternately, many studies have explored the expansion of tissues that initially grow into confluence within confinement but are later allowed to migrate into free space upon removal of a barrier. A popular assay of this type relies on rectangular strips of tissue that are allowed to expand in one or both directions (Poujade et al., 2007; Trepat et al., 2009; Petitjean et al., 2010; Reffay et al., 2011; Nnetu et al., 2012; Serra-Picamal et al., 2012; Zhang et al., 2017; Uroz et al., 2018; Tlili et al., 2018), where averaging along the length of the strip can reveal coordinated population-level behaviors such as complex migration patterns, non-uniform traction force fields, and traveling mechanical waves. Other studies have focused on the isotropic expansion of micro-scale (< 500 μm diameter) circular tissues using the barrier stencil technique (Jang et al., 2017) as well as photoswitchable substrates (Rolli et al., 2012). Still more work has explored approaches to induce directional migration, from geometric cues to applied electric fields (Vedula et al., 2012; Cohen et al., 2014).

In contrast to micro-scale confinement assays, other work has focused on large, freely-expanding tissues of uncontrolled initial size and shape, which grow from either single cells (Puliafito et al., 2012; Huergo et al., 2011) or cell-containing droplets (Lee et al., 2013; Beaune et al., 2014). Related experiments track long-term growth of cell colonies via images taken once per day over several days, but this low temporal resolution cannot access timescales over which migration is important (Huergo et al., 2011; Simpson et al., 2013). Thus, there is still a lack of assays to study long-term expansion and growth of large-scale tissues with precisely-controlled initial conditions, especially initial tissue size, shape, and density.

To address this gap, we leveraged bench-top tissue patterning (Poujade et al., 2007; Cohen et al., 2016) to precisely pattern macro-scale circular epithelia of two sizes (>1 mm in diameter) and performed long-term, high frequency, time-lapse imaging after release of a barrier. To elucidate the consequences of size effects on the tissue, we tracked every cell, relating the overall expansion kinetics to cell migration speed, cell density, and cell-cycle dynamics. We find that, whereas the tissue edge dynamics is independent of the initial conditions, the tissue bulk exhibits size-dependent patterns of cell proliferation and migration, including large-scale vortices accompanied by dynamic density profiles. Together, these data comprise the first comprehensive study of macro-scale, long-term epithelial expansion, and our findings demonstrate the importance of exploring collective cell migration across a wider range of contexts, scales, and constraints.

## Results

### Expansion of millimeter-scale epithelia of different sizes and shapes

We began by characterizing the overall expansion and growth of tissues with the same cell density but different initial diameters of 1.7 mm and 3.4 mm (a 4X difference in area, with tissues hereafter referred to as either ‘small’ or ‘large’), using an MDCK cell line stably expressing the 2-color FUCCI cell-cycle marker (Sakaue-Sawano et al., 2008; Streichan et al., 2014; Uroz et al., 2018; Beaune et al., 2014; Benham-Pyle et al., 2016). We patterned the tissues by culturing cells in small and large circular silicone stencils for ∼18 hr (Cohen et al., 2016; Poujade et al., 2007), whereupon stencils were removed and tissues were allowed to freely expand for 46 hr (Figure 1A, Figure 1—video 1), while images were collected at 20 min intervals using automated microscopy (see Materials and Methods). Our cell seeding conditions and incubation period were deliberately tuned to ensure that the stencils did not induce contact inhibition of proliferation prior to stencil removal (checking FUCCI to ensure the tissue was not arrested in G1). Upon stencil removal, tissues expanded while maintaining their overall circular shape throughout the 2 day experiment. Unless otherwise noted, cell density at stencil removal was ∼2700 cells/mm2, a value consistent with active and growing confluent MDCK epithelia (Streichan et al., 2014; Uroz et al., 2018).

![Figure 1.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig1-v2.jpg)

**Figure 1.:** (A) Footprint throughout 46 hr growth period of representative small (left) and large (right) circular tissues, with the tissue outlines drawn at 4 h increments. Initial diameters were 1.7 mm and 3.4 mm. (B) Small circles exhibit faster relative area, $A⁢(t)/A_{0}$, increase than large circles, where A0 and $A⁢(t)$ are the areas of tissues at the beginning of the experiment and at time t, respectively. Purple points show the relative area increase, $A⁢(t+t_{0})/A⁢(t_{0})$, of small tissues from the time $t_{0}=30$ h when they reached the size of the large circles. (C) Average tissue density $ρ⁢(t)=N⁢(t)/A⁢(t)$ has non-monotonic evolution in small tissues but monotonically increases in large tissues, where $N⁢(t)$ is the number of cells in a tissue at time t. (D) Edge radial velocity vr is largely independent of initial tissue size and cell density. We grouped initial cell densities as $ρ_{1}=[2350,3050]$ cells/mm2, $ρ_{2}=[1650,2350]$ cells/mm2, and $ρ_{3}=[1300,1650]$ cells/mm2. (E) Experimental data on tissue shape and model fits. Assuming a constant migration speed vn in direction normal to the edge, we can predict the area expansion dynamics of elliptical tissues with different aspect ratios. The model fits our data for all tissues with $v_{n}≈29.5$ µm/hr, yielding normalized $χ^{2}$ values of 0.79, 0.13, and 0.06 for aspect ratios of 8, 4, and 1 respectively ($χ^{2}$< 1 indicates a good fit; see Materials and methods). In B, data are from n = 16 tissues across five independent experiments (small and large circles). In C, n = 11 across four experiments for small circles, and n = 9 across three experiments for large circles. In D, n = 16 across five independent experiments for small and large circles, $ρ=ρ_{1}$; n = 13 across three experiments for small circles, $ρ=ρ_{2}$; and n = 11 across three experiments for small circles, $ρ=ρ_{3}$. In E, n = 4 across two experiments for a/b = 1 and a/b = 4, and n = 5 across two experiments for a/b = 8. Shaded regions correspond to standard deviations.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Relative proliferation $N⁢(t)/N⁢(0)$ for small and large tissues. Purple points show the relative proliferation, $N⁢(t+t_{0})/N⁢(t_{0})$, of small tissues from the time t0 when they reached the starting size of the large circles. Error bars for purple points are smaller than marker size. Data are from 16 tissues across five independent experiments for small and large tissues. .

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Elliptical tissues spread with different normal velocities along their major and minor axes. Data are from elliptical tissues with the same initial area than small circular tissues. (B) Normal expansion velocity is roughly independent of the local radius of curvature rc of the tissue edge for large radii of curvature. For radii of curvature smaller than ∼1 mm, the normal velocity decreases with decreasing rc. This plot includes data both from circular tissues and from the major and minor axes of elliptical tissues, excluding the first 16 hr of expansion to eliminate any affects from initial front acceleration. See Materials and methods for calculation of rc. .

First, we measured relative areal increase (Figure 1B) and relative cell number increase (Figure 1—figure supplement 1) of small and large tissues. By 46 hr, small and large tissues had increased in area by 6.4X and 3.3X, respectively, while cell number increased by 9.2X and 5.5X, respectively. Since proliferation outpaces area expansion in long-term growth, average tissue density increased by the end of the experiment. The evolution of average tissue density was more complex, however, as small tissues experienced a density decrease from 4 to 12 hr while large tissues exhibited a monotonic increase in cell density (Figure 1C). Accordingly, at any given time after stencil removal, large tissues had a higher density than small tissues. Non-monotonic density evolution has been observed in thin epithelial strips (Poujade et al., 2007) and likely arises from competition between migration and proliferation dynamics, which we discuss later.

We then related area expansion to the kinematics of the tissue edge. To quantify edge motion, we calculated the average radial velocity of the tissue boundary, $v_{r}⁢(t)$, at 1 hr intervals over 46 hr (Materials and methods). We found that vr is independent of both tissue size and a wide range of initial cell densities, in all cases reaching ∼30 μm/h after ∼16 hr (Figure 1D). Before reaching this constant edge velocity, vr ramps up during the first 8 hr after stencil removal, and, notably, overshoots its long-time value by almost 30%. We hypothesize that the overshoot is due to the formation of fast multicellular finger-like protrusions that emerge at the tissue edge in the early stages of expansion and then diminish (Figure 1—video 2). This hypothesis is supported by a recent model showing that edge acceleration (as observed during the first 8 hr in Figure 1D) leads to finger formation (Alert et al., 2019). It is remarkable that the edge radial velocity $v_{r}⁢(t)$ is independent of the initial tissue size and density, especially considering that cell density evolution shows opposite trends at early stages of expansion for small and large tissues (Figure 1C). This observation suggests that the early stages of epithelial expansion are primarily driven by cell migration rather than proliferation or density-dependent decompression and cell spreading.

The observation that vr is independent of tissue size ought to explain why small tissues have faster relative area expansions than large tissues. We hypothesized that the relation between tissue size and areal increase could be attributed primarily to the perimeter-to-area ratio. Assuming a constant edge velocity vn normal to the tissue boundary, the tissue area increases as $d⁢A=P⁢v_{n}⁢d⁢t$, where P is the perimeter of tissue and $d⁢t$ is a small time interval. Thus, the relative area increase $d⁢A/A=(P/A)⁢v_{n}⁢d⁢t$ scales as the perimeter-to-area ratio, which is inversely proportional to the radius for circular tissues, so the relative area increases faster for smaller tissues (Figure 1B).

To verify that the perimeter-to-area ratio is proportional to the relative area increase, we analyzed elliptical tissues with the same area and cell density but different perimeters (Figure 1—video 3). Increasing the perimeter-to-area ratio of a tissue by increasing its aspect ratio indeed leads to faster relative area expansion (Figure 1E). A simple, edge-driven expansion model with linear increase of the tissue major and minor axes predicts $A⁢(t)/A⁢(0)=(a+v_{n}⁢t)⁢(b+v_{n}⁢t)/(a⁢b)$, where a and b are the initial major and minor axes of the tissue. This model fits our data well assuming the same edge speed $v_{n}≃29.5$ μm/h for all tissues (Figure 1E). This observation suggests that edge speed is mostly independent of edge curvature. However, we measure a smaller edge speed at the major axes of ellipses, which are high-curvature points with radius of curvature $r_{c}≲0.75 mm$ (Figure 1—figure supplement 2). Such high curvatures are concentrated around the major axes of our elliptical tissues. However, most of the tissue edge has a smaller curvature, and therefore advances at a curvature-independent speed. Further, even high curvature regions blunt due to expansion over time (see Figure 1—video 3). As a result, our model with a single edge speed $v_{n}≃29.5$ μm/h is sufficient to capture the area expansion of both circular and elliptical tissues (Figure 1E).

Together, our findings demonstrate that epithelial shape and size determine area expansion dynamics via the perimeter-to-area ratio. This relationship results from the fact that tissues exhibit a constant, size-independent, migration-driven edge speed normal to tissue boundary. Since initial tissue size does not affect boundary dynamics, but does impact the relative growth and expansion of the tissue, we hypothesize that cells in the tissue bulk exhibit tissue size-dependent behaviors.

### Spatiotemporal dynamics of migration speed and radial velocity

Having demonstrated the role of the boundary in the expansion of large-scale epithelia, we sought to relate tissue areal expansion rate to internal collective cell migration dynamics. We used Particle-Image-Velocimetry (PIV, Materials and methods) to obtain flow fields describing cell migration within freely expanding epithelia (Poujade et al., 2007; Petitjean et al., 2010; Angelini et al., 2010; Cohen et al., 2014; Aoki et al., 2017). We constructed kymographs (Materials and Methods) to display the full spatiotemporal flow patterns of the tissue (Figure 2A,B; Serra-Picamal et al., 2012; Zhang et al., 2017), averaging over the angular direction and over 16 tissues (for representative kymographs, see Figure 2—figure supplement 1). We also separately show time evolution (Figure 2C) and spatial profiles (Figure 2D) of speed and radial velocity to compare small and large tissues.

![Figure 2.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig2-v2.jpg)

**Figure 2.:** (A,B) Average kymographs of (A) speed and (B) radial velocity vr throughout expansion for small (left) and large (right) tissues. (C) Evolution of the average speed of boundary (top) and center (bottom) zones, defined as regions extending ∼200 μm from the tissue center and tissue edge, respectively. This width of the zones corresponds approximately to the velocity-velocity correlation length for MDCK cells (Petitjean et al., 2010). While the speed in the edge zone remains high in both small and large tissues, the speed in the center zone begins to decrease ∼24 hr sooner in large tissues than in small tissues, as the central zone of the small tissues has particularly high speed from 18 to 36 hr. (D) Profiles of speed (top) and radial velocity (bottom) at 36 hr, from the edge of the tissue inwards. Arrows indicate that the tissues are indexed from the edge of the tissue inwards. All data are from n = 16 tissues across five independent experiments (small and large circles). Speed and radial velocity profiles of large and small tissues match closely for the first 500 μm from the tissue edge. The average difference between the profiles in this zone is 0.39 μm/h (speed) and 0.27 μm/h (radial velocity), respectively, while the smallest standard deviation for any point in either profile is 0.56 μm/h.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Representative kymographs and heatmaps for speed (A–D) and radial velocity (E–H) for different choices of PIV window size (see Materials and methods). Panels A,B,E,F were obtained using a PIV window of 115—115 μm, as in Figure 2. Panels C,D,G,H were obtained using a PIV window of 57—57 μm, which contains four times fewer pixels than the larger window of panels A,B,E,F. Dashed lines indicate timepoint of 36 hr to which heatmaps correspond. Kymographs and heatmaps in each column are from the same representative tissue.

Kymographs of speed and radial velocity reveal the existence of an edge region of fast, outward, radial cell motion (Figure 2A,B), with speeds similar to the radial edge velocity reported in Figure 1D. Up to ∼500 μm from the tissue edge, the speed and radial velocity profiles are practically identical for small and large tissues (Figure 2D), showing that cell motion near the tissue edge is independent of tissue size.

The tissue centers, in contrast, exhibit size-dependent behaviors. For both small and large tissues, a wave front of cell speed and radial velocity propagates toward the tissue centers at ∼90 μm/h (Figure 2A and B, dashed lines). This is approximately 3X faster than the tissue edge speed, consistent with previously described waves of strain rate in cell monolayers (Serra-Picamal et al., 2012). Soon after the wave of radial velocity reaches the center, it retreats, leaving a region of low radial velocity that increases in extent in the center of both small and large tissues (Figure 2B). This decrease of radial velocity is accompanied by a reduction in cell speed in the center of large tissues but not in small tissues, in which cell speed remains high until 36 hr (Figure 2A and C Bottom). We examine the behavior of this high-speed but low-radial-velocity central region of small tissues in the next section.

### Emergence of large-scale vortices

The propagation of low radial velocity out from the center of small tissues coincides with the formation and expansion of a millimeter-scale, persistent vortex (see Figure 3A, Figure 3—video 1 for representative vortex). These large vortices are observed in both small and large tissues (Figure 3—video 2), but they only reach tissue-spanning sizes in small tissues.

![Figure 3.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig3-v2.jpg)

**Figure 3.:** (A) Vortical flows seen from 10 hr traces of cell trajectories in small (left) and large (right) tissues. We color each trajectory according to its local orientation. (B) Growth rate of perturbations of wave vector modulus q around the unpolarized state of the tissue bulk, Equation 3. Perturbations with wavelength longer than $2⁢\pi/q_{c}$ grow ($Ω>0$), leading to large-scale spontaneous flows in the tissue bulk. We show curves for the following values of the polarity-velocity coupling parameter: $ν_{s}=0,1,2,3,4$ mm−1. For the remaining parameters, we took $T_{a}=100$ Pa/μm, $ξ=100$ Pa⋅s/μm2, $η=25$ MPa⋅s, $\gamma=10$ kPa⋅s, $a=20$ Pa, $K=10$ nN, as estimated in Pérez-González et al., 2019. (C) Average kymographs of vorticity show that the vortex in small tissues appears in the center and expands to >1 mm (n = 16), while vorticity in large tissues is present only during the early stages of tissue expansion (n = 16). The black bars indicate a characteristic vortex size. (D) Characteristic vortex size (marker size), time (horizontal axis), and intensity (vertical axis) of each tissue’s maximal vortex intensity. Small tissue vortices are generally more intense, with $p<0.0001$. (E) For small tissues, the time of maximal vortex intensity decreases with the initial cell density.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Radial and tangential displacements of 18 h cell trajectories for a representative small tissue as a function of the initial radial position of each cell trajectory. Trajectories were selected from the vortex-dominated period of 24–42 hr. The tangential displacement (blue markers) most clearly reveals the presence of the vortex, with 350 μm tangential displacement throughout the central 750 μm of the tissue. At the outer zone, tangential displacements drop to 0 μm. In contrast, radial displacement (red markers) increases roughly linearly from the center to the outer edge of the tissue, with no sharp change when moving from the central to the outer region. The fact that radial displacements are largely insensitive to the vortical flows explains why the presence of a vortex has no noticeable impact on the overall expansion of the tissue. Together, the radial and tangential displacements of the tissue reveal a spiraling vortical flow that combines tangential shear with radial expansion.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Representative kymograph and heatmap of vorticity for (A) small and (B) large tissues.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Averaged kymographs of enstrophy, which partition the vorticity power in modes of different wavelengths for each timepoint. (A) From left to right, enstrophy kymographs of small tissues for decreasing starting density. Initial densities were grouped as in Figure 1D. Decreasing starting density clearly delays the onset of high power, long wavelength (small wavevector) vorticity. Small tissue enstrophy peaks at a wavevector of $∼3.14⁢m⁢m^{-1}$, which corresponds to a wavelength of 2 mm. Data from n = 16 tissues for $ρ=ρ_{1}$ (left); n = 13 tissues for $ρ=ρ_{2}$ (middle); and n = 11 tissues for $ρ=ρ_{3}$ (right). (B) Average kymograph of enstrophy for large tissues ($ρ=ρ_{1}$, n = 16). The peak at large wavelength is not evident since the vortex is not as prevalent in large tissues. The initial cell density ranges $ρ_{1}$, $ρ_{2}$, and $ρ_{3}$ are the same as in Figure 1D.

To visualize the form and scale of these vortices, we tracked individual cell motion and colored cell trajectories according to their orientation (Püspöki et al., 2016) for a representative small and large tissue vortex (see Figure 3A and Materials and Methods). We plotted trajectories for the time periods that the vortex was most apparent, which was 20–40 hr in the small tissue (Figure 3A, left) and 10–30 hr in the large tissue (Figure 3A, right). During the vortex period in small tissues, cell trajectories are primarily radial in the boundary zone, but mainly tangential in the entire central zone (Figure 3A left, see Figure 3—figure supplement 1 for vortex trajectory quantification).

To understand the emergence of the vortices, we build on a continuum physical model of tissue spreading that describes the cell monolayer as a two-dimensional compressible active polar fluid (Blanch-Mercader et al., 2017; Pérez-González et al., 2019; Alert et al., 2019). Consistent with our velocity measurements (Figure 2C), we assume that cells at the edge zone are radially polarized and motile, whereas cells in the bulk of the tissue are unpolarized and non-motile. We describe cell polarization at a coarse-grained level via a polarity field $𝐩$ that obeys the following dynamics (Alert and Trepat, 2020):

$$
\partial_{t}⁡𝐩=\frac{𝐡}{\gamma}+ν_{s}⁢𝐯.
$$

Here, γ is the rotational viscosity that damps polarity changes. Respectively, $𝐡=-a⁢𝐩+K⁢\nabla^{2}⁡𝐩$ is the so-called molecular field that governs polarity relaxation: the first term drives the polarity to zero, and the second term opposes spatial variation of the polarity field. As a result of these terms, the radial polarity at the tissue edge decays over a length scale $L_{c}=\sqrt{K/a}$ into the tissue bulk.

With respect to previous models of tissue spreading, we add the last term in Equation 1, which couples the polarity to the tissue velocity field $𝐯$. This coupling is a generic property of active polar fluids interacting with a substrate (Brotto et al., 2013; Kumar et al., 2014; Oriola et al., 2017; Maitra et al., 2020). Previous works in agent-based models showed that similar polarity-velocity alignment interactions (Alert and Trepat, 2020) can lead to waves (Petrolli et al., 2019), flocking transitions (Szabó et al., 2006; Henkes et al., 2011; Basan et al., 2013; Malinverno et al., 2017; Giavazzi et al., 2018), and vortical flows (Rappel et al., 1999; Camley et al., 2014; Li and Sun, 2014; Segerer et al., 2015; Barton et al., 2017; Lin et al., 2018) in small, confined, and polarized tissues. Here, using a continuum model, we propose that cell polarity not only aligns with but is also generated by tissue flow, and we ask whether this polarity-velocity coupling can lead to large-scale spontaneous flows in the unpolarized bulk of unconfined tissues.

To determine the flow field $𝐯$, we impose a balance between internal viscous stresses in the tissue, with viscosity η, and external cell-substrate forces, including viscous friction with coefficient ξ, active traction forces with coefficient Ta, and the cell-substrate forces associated with the polarity-velocity coupling $ν_{s}$:

$$
η⁢\nabla^{2}⁡𝐯=ξ⁢𝐯-T_{a}⁢𝐩-ν_{s}⁢𝐡.
$$

This force balance predicts that even if cell polarity, and hence active traction forces, are localized to a narrow boundary layer of width $L_{c}∼50$ μm (Blanch-Mercader et al., 2017; Pérez-González et al., 2019), cell flow can penetrate a length $∼\lambda=\sqrt{η/ξ}$ into the tissue. Based on our measurements (Figure 2D), we estimate $\lambda∼0.5-1$ mm, which is larger than the velocity correlation length of $∼200$ μm in the tissue bulk (Petitjean et al., 2010).

A linear stability analysis of Equations 1 and 2 shows that perturbations of wave number q around the quiescent ($𝐯=0$) and unpolarized ($𝐩=0$) state grow with a rate

$$
Ω⁢(q)=-\frac{a}{\gamma}⁢(1+L_{c}^{2}⁢q^{2})+\frac{T_{a}⁢ν_{s}-a⁢ν_{s}^{2}⁢(1+L_{c}^{2}⁢q^{2})}{ξ⁢(1+\lambda^{2}⁢q^{2})}.
$$

This result shows that, if $T_{a}⁢ν_{s}>a⁢(ξ/\gamma+ν_{s}^{2})$, the unpolarized state of an active polar fluid described by Equations 1 and 2 is unstable ($Ω>0$) to perturbations of wavelength longer than a critical value $2⁢\pi/q_{c}$ given by $Ω⁢(q_{c})=0$ (Figure 3B). This analysis suggests that, for tissues larger than this critical value $∼2⁢\pi/q_{c}$, the quiescent tissue bulk becomes unstable and starts to flow spontaneously at large scales, consistent with the emergence of large-scale vortices. The mechanism of this instability is the positive feedback between flow-induced cell polarization and the flows due to migration of polarized cells. The fact that a critical size of the order of millimeters is required for this long-wavelength instability might explain why large-scale vortices have not been observed in previous studies, which considered smaller tissues.

### Vortex kinematics

To quantify the kinematics of the large-scale vortical flows, we obtained the vorticity field $\omega⁢(𝐫,𝐭)=\nabla\times𝐯⁢(𝐫,𝐭)$. Before averaging over tissues, we took the dominant direction of rotation of each tissue to correspond to positive vorticity. This direction was counterclockwise in 51.5% of tissues and clockwise in 49.5% of tissues, with a sample size of 68. With this convention, the vortex core always has positive vorticity. Accordingly, the outer region of the vortex exhibits negative vorticity (Figure 3C, see Figure 3—figure supplement 2 for kymographs and heatmaps of vorticity representative tissues), which corresponds to the counter-rotation that occurs when the central vortical flow transitions to the outer radial flow (Figure 3A, left). We define a characteristic vortex radius as the radial position of the center of the negative-vorticity region, which is ∼1 mm at 36 hr in small tissues (Figure 3C, black bars).

To analyze vortex dynamics across different tissues with varying vortex positioning, and to quantitatively capture the onset and strength of vortices, we calculated the enstrophy spectrum $ℰ⁢(q,t)=|\omega~⁢(𝐪,t)|^{2}$, where $\omega~⁢(𝐪,t)=\int(d⁢𝐫/A)⁢\omega⁢(𝐫,t)⁢e^{i⁢𝐪⋅𝐫}$ are the spatial Fourier components of the vorticity field $\omega⁢(𝐫,t)$ (Alert et al., 2020). The enstrophy spectrum is the power spectral density of the vorticity field as a function of the wave-vector modulus q, and therefore provides a measure of the vortex intensity at a length scale $2⁢\pi/q$. The kymographs of the enstrophy spectrum show that most of the vortex’s intensity is found at a characteristic length scale of ∼1 mm (Figure 3—figure supplement 3).

For each tissue we characterized the maximal vortex strength by the maximum value of $ℰ⁢(q,t)$ as well as its associated wavelength $2⁢\pi/q$ and time of occurrence. We represented these three quantities on a scatter plot, which shows that vortices in small tissues have generally higher intensity than those in large tissues (Figure 3D). Vortices in small tissues are also larger relative to tissue size, since the absolute size of vortices in small and large tissues is similar (Figure 3D). Furthermore, vortex strength peaks several hours later in small tissues than in large tissues (Figure 3D). We hypothesized that this difference is due to large tissues featuring a faster density increase than small tissues (Figure 1C). To test this hypothesis, we varied the initial cell density of small tissues and observed that the time of maximum vortex intensity decreases with increasing density (Figure 3E, Figure 3—figure supplement 3). These results prompted us to examine spatiotemporal cell density evolution.

### Spatiotemporal dynamics of cell density

Given that cell density appears to affect vortex formation and is known to control contact inhibition of locomotion and proliferation (Schnyder et al., 2020), we explored the spatiotemporal evolution of cell density. Constructing average kymographs in the same way as for speed, radial velocity, and vorticity, we observe that the vortex region in the center of small tissues is accompanied by an unexpected local density minimum (Figure 4A). Strikingly, snapshots of small and large tissues reveal that large-scale vortices occur in low-density regions, regardless of location within the tissue (Figure 4—figure supplement 1). However, given that vortices in large tissues are often off-centered, the low-density region does not appear in their average kymograph of cell density (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig4-v2.jpg)

**Figure 4.:** (A) Averaged kymographs of cell density for small (left, n = 11) and large (right, n = 9) tissues. Small tissues develop a central low-density region that persist more than 20 hr. (B) Cell density, ρ, at the center of large tissues increases gradually, while cell density at the center of small tissues has non-monotonic evolution. (C) For different initial tissue sizes and densities, the evolution of the cell density, ρ, at the boundary zone converges to similar values at about 12 hr, which coincides with the end of the overshoot of edge radial velocity in Figure 1D. Center and boundary zones are defined as in Figure 2B. (D) Simulated evolution of cell densities obtained from the numerical solution of the continuity equation using the average radial velocity measurements $v_{r}⁢(r,t)$ (Figure 2B) and a uniform and constant cell proliferation rate corresponding to a 16 h cell doubling time. In (B,C) the initial cell density ranges and number of replicates $ρ_{1}$, $ρ_{2}$, and $ρ_{3}$ are the same as in Figure 1D.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** A region of low cell density co-occurs with the vortex in representative small and large tissues, centered and off-centered. Representative tissues include small tissues with vortex/low density region in the center-right (A) and center (B) as well large tissues with vortex/low density region the center (C) and right-of-center (D). In both small (E) and large (F) tissues, high-vorticity large-scale flows (high values on the vertical axis) tend to occur close to the center of the tissue, and in regions of low cell density. In panels (E) and (F), marker color indicates the distance of each point relative to the center of the tissue. For data analysis details, see Methods.

To investigate the effects of initial conditions, we tracked the density evolution of the center and boundary zones across tissues with different starting densities and sizes, grouping initial densities into three ranges as before (Figure 4B and C). As with the average density in Figure 1C, the density monotonically increases in large tissues centers but is non-monotonic in small tissues. Notably, the cell density at the center of small tissues of different initial cell densities reach a common minimum during the 16–32 hr time period (Figure 4B), which includes the vortex onset time. At the boundary zone, the long-time evolution of the cell density is independent of initial tissue size and density (Figure 4C). This common long-time evolution is reached at about 12 hr (Figure 4C), which coincides with the time at which the edge radial velocity stabilizes upon the overshoot (Figure 1D).

To understand the unexpected transient density decrease at the center of small tissues, we sought to explain it as the result of combined advective transport based on the measured radial flow fields $𝐯_{r}⁢(𝐫,t)$ and homogeneous cell proliferation at a rate $k⁢(𝐫,t)=k_{0}$ throughout the tissue. To test this hypothesis, we solved the continuity equation for the cell density field $ρ⁢(𝐫,t)$,

$$
\frac{\partial⁡ρ}{\partial⁡t}=-\nabla⋅(ρ⁢𝐯)+k_{0}⁢ρ,
$$

using the average radial velocity profiles $v_{r}⁢(r,t)$ measured by PIV (Figure 2D), and a proliferation rate $k_{0}=1.04$ h−1, which corresponds to a cell doubling time of 16 hr (Materials and methods). This minimal model recapitulates the major features of the evolving density profiles for both small and large tissues (compare Figure 4D with Figure 4A). Therefore, the unexpected formation of a central low-density region results from the combination of outward tissue flow and proliferation within the colony. However, further research is required to determine the biophysical origin of the non-monotonic density evolution. Moreover, having assumed a density-independent proliferation rate, our model predicts a cell density in the center of large tissues higher than the one measured at the end of the experiment, and it does not quantitatively reproduce the cell density profiles at the edge regions. These discrepancies suggest that more complex cell proliferation behavior is required to fully recapitulate the density dynamics in expanding cell monolayers.

### Spatiotemporal dynamics of cell cycle

To better understand how tissue expansion affects cell proliferation, we analyzed the spatiotemporal dynamics of cell-cycle state. Our cells stably express the FUCCI markers, meaning that cells in the G0-G1-S phase of the cell cycle (referred to here as G1) fluoresce in red (shown as magenta), and cells in the S-G2-M phase of the cell cycle (referred to here as G2) fluoresce in green (Sakaue-Sawano et al., 2008). Additionally, immediately-post-mitotic cells do not fluoresce and appear dark. Small and large tissues are initially well mixed with green and magenta cells, confirming that cells are actively cycling throughout the tissue at the time of stencil removal (Figure 5—figure supplement 1). During tissue expansion, spatiotemporal patterns of cell-cycling behavior emerge (Figure 5A, Figure 5—video 1).

![Figure 5.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig5-v2.jpg)

**Figure 5.:** Transition from the G1 (magenta) to the G2 (green) phase of the cell cycle corresponds to DNA replication (during S phase). Subsequently, a cell proceeds to mitosis (M phase, dark), and eventually back to the G1 phase upon cell division. (A) Fluorescence images of the Fucci marker of cell-cycle state at the end of the experiment (46 hr) of representative small and large tissues overlaid with nuclei positions (gray). The boundary zone of both tissues has more cells in the G2 than in the G1 phase, along with a substantial proportion of dark cells (inset). Scale bars 1 mm. (B) Average kymographs (small, n = 5; large, n = 11) of cell-cycle-state fraction. In small tissues, a G1-dominated transition zone, which appears as a vertical magenta streak from 16 hr onward, is interposed between G2-dominated center and edge zones. While the size of small tissues from 30 to 46 hr matches that of large tissues from 0 to 16 hr (dashed boxes), cell-cycle states between these times are clearly distinct. (C) Fraction of cell-cycle states in the boundary zone. (D) Fraction of cell-cycle states in the center zone. Center and boundary zones are defined as in Figure 2. For C and D, n = 5 for small tissues and n = 11 for large tissues. (E) Scatter plot of density and speed, with color indicating the fraction of cells at G1 and G2, corresponding to each PIV pixel of the final timepoint of a representative small (left) and large (right) tissue.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Cells within both small and large tissues are actively cycling at the time of stencil removal. (A) Initial timepoint of representative small tissue. (B) Initial timepoint of representative large tissue. .

To quantitatively investigate these cell-cycle patterns, we obtained the local fractions of G1, G2, and post-mitotic cells by evaluating cell cycle state for each cell nucleus (see Materials and Methods). We then overlaid kymographs of the G1 and G2 cell-cycle-state fractions (Figure 5B) and plotted the time evolution of G1, G2, and post-mitotic fractions together (Figure 5C,D). Immediately after stencil removal, we observe a cell division pulse in all tissues, which manifests in a decrease in G2 and increase in post-mitotic fraction (Figure 5C,D). After about 12 hr of tissue expansion, the boundary region becomes primarily populated by rapidly-cycling cells (Figure 5B,C), which results in a predominance of cells in this region that either have recently divided (post-mitotic, black) or are likely to divide soon (G2, green). The high numbers of post-mitotic cells indicate that cells in G1 rapidly proceed to mitosis. Given that the edge radial speed overshoots during the first 12 hr of tissue expansion (Figure 1D), future work is necessary to characterize the effect of cell cycling on edge motion at early stages of expansion.

In the central region of small tissues (Figure 5B left, D left), we observe cell-cycling dynamics similar to the boundary region. Thus, in the tissue-spanning vortex of small tissues, cells are also rapidly cycling. The fraction of cells in G1 only starts to increase at ∼40 hr (Figure 5D left), coinciding with the weakening of the vortex (Figure 3C left). In contrast, the center zone of large tissues undergoes strong cell-cycle arrest at the G1-G2 transition at about 30 hr, also coinciding with the weakening of the vortex in large tissues (Figure 5B right, D right). Cells already past G1 at this time continue to division and re-enter G1, evidenced by the steady increase in local fraction of G1 accompanied by a steady decrease in G2 after 30 hr. Similar cell-cycle arrests were previously reported both in growing epithelia (Streichan et al., 2014) and in spreading 3D cell aggregates (Beaune et al., 2014). Before the onset of cell-cycle arrest, the center of large tissues exhibits large-scale coordinated cell-cycling dynamics in the form of anti-phase oscillations, with peaks in G2 fraction accompanied by troughs in G1 fraction (Figure 5B right, D right).

Finally, we sought to link cell-cycle dynamics to the kinematics of tissue expansion by studying correlations between local measurements of cell cycle, cell speed, and cell density (Figure 5E). Here, each point represents one PIV window, with color indicating its average cell-cycle state. As expected, cell speed is negatively correlated with cell density. Further, in large tissues, the cell-cycle state transitions from G1-dominated to G2-dominated when cell density increases above ∼5000 cells/mm2 and cell speed falls below ∼12 μm/h (Figure 5E right). In this regime, the decrease of cell speed with increasing cell density bears similarities to previously-reported glass transitions and contact inhibition of locomotion (Angelini et al., 2011; Zimmermann et al., 2016; Garcia et al., 2015). Small tissues, by contrast, lack the G1-dominated, slow, high-density cell population (Figure 5E, left) found in the center of large tissues. Taken together, our findings emphasize that cell cycling, cell flow, and cell density patterns are inextricably linked and depend on the initial size of an expanding tissue.

## Discussion

We began this study by asking how changes in initial size affect the long-term expansion and growth of millimeter-scale epithelia. By means of high spatiotemporal resolution imaging and precisely controlled initial conditions, our assays systematically dissected tissue expansion and growth from the overall boundary kinematics (Figure 1) to the internal flow patterns (Figures 2, 3 and 4) and cell-cycle dynamics (Figure 5). While we demonstrated that ‘small’ tissues increase in area relatively much faster than do ‘large’ tissues, our data suggest a surprising and stark decoupling of the outer and inner regions of an expanding epithelium. Notably, the behaviors of the edge zones are largely independent of tissue size, cell density, and history, while interior dynamics depend strongly on these factors.

Unexpectedly, the overall tissue growth and expansion dynamics (Figure 1) could be attributed to one dominant feature: these epithelia expanded at the same edge speed regardless of initial tissue size, shape, and cell density. The only exception is the major axes of ellipses, where the normal edge speed is smaller when the radius of curvature is $r_{c}<0.75$ mm. This observation, combined with the fact that the velocity penetration length is 500 mm (Figure 2D), suggests that a tissue must be 1 mm in diameter for the tissue edge to move independently of bulk flows. As a result of this robust edge motion, the areal expansion rate of the tissue is dictated by its perimeter-to-area ratio. To further emphasize the decoupling of the boundary and internal dynamics of epithelia, consider that the key findings in Figure 1 neither predict nor depend upon the radically different internal dynamics we observed within ‘small’ and ‘large’ tissues. For instance, despite the roiling vortices occupying large portions of ‘small’ tissues and the pronounced, large-scale contact inhibition of ‘large’ tissues–two antithetical phenomena–no hints of these behaviors can be detected in the motion of the boundary.

Critically, the type and timing of internal dynamics are dictated not by the current size but by the expansion history of a given tissue. While a small tissue eventually expands to reach the initial size of a large tissue, it exhibits different internal dynamics from the large tissue at this size (Figure 6). This difference in internal dynamics is perhaps easiest to observe in spatiotemporal evolution of cell cycle (Figure 6D, Figure 5B dashed boxes); the small-tissue footprint from 30 to 46 hr closely matches the large-tissue footprint from 0 to 16 hr, but the cell cycle distribution during these time periods bears almost no similarities. This applies as well to other important bulk properties of the tissue (Figure 6A–C), as cell cycle is tightly linked to cell speeds and density (Figure 5E). For example, at equal current sizes, the center of initially-small tissues features high vorticity with decreasing cell speed whereas initially-large tissues exhibit low vorticity and increasing cell speed (Figure 6A,B). Respectively, at equal current sizes, while absolute cell densities in the tissue centers share some overlap, it is notable that the rate of density change at the tissue center is increasing faster in initially-small tissues than in initially-large tissues (Figure 6C). However, the most striking differences in cell density evolution occur not at equal current sizes but during the early stages of tissue expansion: whereas the cell density at the center of large tissues increases at all times, the center of small tissues features a marked density decrease between ∼8 and ∼24 hr (Figure 4A,B). Overall, while edge dynamics are stereotyped and conserved across different sizes, our findings suggest that initial tissue size impacts the bulk dynamics by altering the constraints under which the tissue grows. We expect that tissues with sizes between our two choices would exhibit similar edge dynamics and internal patterns that cross over between our small and large tissues.

![Figure 6.](https://cdn.elifesciences.org/articles/58945/elife-58945-fig6-v2.jpg)

**Figure 6.:** Here, we quantify the internal state of the tissue in terms of the cell speed in tissue center (A), maximal vortex power (B), cell density in tissue center (C), and fraction of cells in the G1 phase of the cell cycle in tissue center (D). At late times, initially-small tissues reach radii that initially-large tissues had at early times. When they have the same current size (overlap region in between dashed lines), initially-small and initially-large tissues have distinct internal dynamics of cell migration and cell proliferation. The tissue center zone in A, C, and D was defined as in Figure 2.

The vortices are a particularly striking example of such size- and history-dependent internal patterns (Figure 3, Figure 6B). Our active fluid model suggests that the vortices emerge from a dynamical instability of the tissue bulk, which occurs when the tissue reaches a critical size. Thus, whereas the instability itself is a bulk phenomenon independent of the tissue edge, edge-driven expansion allows small tissues to reach the critical size that triggers the instability. In addition, our data suggest a strong correlation between vortex formation and the development of non-monotonic density profiles. Not only did small tissues exhibit co-occurrence of vortices with density decreases in the tissue center, but also off-center vortices in large tissues always co-localized with a local density decrease (Figure 4—figure supplement 1). Our model does not currently describe cell density, and hence cannot explain the relationship between vortex formation and local density decreases. Thus, our experimental findings call for the development of more detailed models that couple cell density to both the velocity and the polarity fields, accounting for how density gradients influence cell polarization (Alert and Trepat, 2020).

The pronounced decoupling between boundary and internal dynamics in epithelia confers stability to the overall expansion of the tissue, making it robust to a wide range of internal perturbations. From the perspective of collective behavior, we speculate that such robust boundary dynamics may be beneficial in a tissue such as an epithelium whose teleology is to continuously expand from its free edges to sheath organ surfaces. Further, the ability to accurately predict epithelial expansion with a single parameter, the edge speed, will have practical uses in experimental design and tissue-engineering applications. Finally, given that many of the phenomena presented here only occurred due to the millimetric scale of our unconfined tissues and the long duration of the experiments, our results showcase the value of pushing the boundaries of large-scale, long-term studies on freely-expanding tissues.

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
      <td>Cell line (canine)</td>
      <td>MDCK-FUCCI</td>
      <td>Streichan et al., 2014. Wildtype: ECACC-00062107</td>
      <td>N/A</td>
      <td>RFP signal is G1, GFP is G2.</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DMEM - low glucose</td>
      <td>Sigma-Aldrich, Inc</td>
      <td>Cat.D5523</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>fetal bovine serum</td>
      <td>Atlanta Biologicals</td>
      <td>Cat.S11550</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Silicone stencil material, 250 µm thick.</td>
      <td>Stockwell Elastomerics</td>
      <td>Cat.HT6240-40D</td>
      <td>Tissue patterning material</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI</td>
      <td>NIH ImageJ Project</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>Mathworks, Inc</td>
      <td>2019A</td>
      <td>All code compatible back to at least 2015B</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Machine Learning Tools</td>
      <td>Laboratory code LaChance and Cohen, 2020</td>
      <td>—see References</td>
      <td>Full code on GitHub</td>
    </tr>
  </tbody>
</table>

### Cell culture

All experiments were performed with MDCK-II cells expressing the FUCCI cell-cycle marker system as received from: Streichan et al., 2014. After treatment with Mycoplasma Removal Agent (MPI Biological), cells tested negative for mycoplasma (MycoProbe, R and D Systems). We cultured cells in MDCK media consisting of low-glucose (1 g/L) DMEM with phenol red (Gibco, USA), 1 g/L sodium bicarbonate, 1% streptomycin/penicillin, and 10% FBS (Atlanta Biological, USA). Cells were maintained at 37°C and 5% CO2 in humidified air.

### Tissue patterning

We coated tissue-culture plastic dishes (BD Falcon, USA) with type-IV collagen (MilliporeSigma, USA) by incubating 150 μL of 50 μg/mL collagen on the dish under a glass coverslip for 30 min at 37°C, washing three times with deionized distilled water (DI), and allowing the dish to air-dry. We then fabricated silicone stencils with cutouts of desired shape and size and transferred the stencils to the collagen coated surface of the dishes. Stencils were cut from 250 μm thick silicone (Bisco HT-6240, Stockwell Elastomers) using a Silhouette Cameo vinyl cutter (Silhouette, USA). We then seeded the individual stencils with cells suspended in media at 1000 cells/mL. Suspended cells were concentrated at $∼2.25\times10^{6}$ cells/mL and pipetted cells into the stencils at the appropriate volume. Care was taken not to disturb the collagen coating with the pipette tip. To allow attachment of cells to the collagen matrix, we incubated the cells in the stencils for 30 min in a humidified chamber before flooding the dish with media. We then incubated the cells for an additional 18 hr to allow the cells to form monolayers in the stencils, after which the stencils were removed with tweezers. Imaging began 30 min after stencil removal. Media without phenol red was used throughout seeding and imaging to reduce background signal during fluorescence imaging.

### Live-cell time-lapse imaging

All imaging was performed with a 4X phase contrast objective on an automated, inverted Nikon Ti2 with environmental control (37°C and humidified 5% CO2) using NIS Elements software and a Nikon Qi2 CMOS camera. Phase contrast images were captured every 20 min, while RFP/GFP channels were captured every 60 min at 25% lamp power (Sola SE, Lumencor, USA) and 500 ms exposure time. No phototoxicity was observed under these conditions for up to 48 hr. Final images were composited from 4 × 4 montages of each dish using NIS Elements.

### Tissue edge radial velocity

Tissues were segmented to make binary masks using a custom MATLAB (Mathworks) script. Tissue edge radial velocity was measured from the binary masks within more than 200 discrete sectors of the tissue; the edge radial velocity of all sectors were averaged to arrive at the tissue average edge radial velocity. Radial velocity at each sector was calculated for each timepoint as the rate of change of the average extent of the boundary pixels of the sector, utilized a rolling average of 3 timepoints (1 hr) to account for capture phase offsets resulting from capturing phase and fluorescence images at different frequencies. Sectors originated from the center of each tissue at the initial timepoint and were ∼20 µm wide at the edge of the tissue at the starting point.

### Radius of curvature for the major and minor axes of elliptical tissues

Curvature at the major and minor axes of growing tissues was approximated at each time-point by fitting an ellipse to the tissue footprint and taking the radius of curvature at the minor and major axes as $b^{2}/a$ and $a^{2}/b$, respectively, where a is the major semi-axis length and b is the minor semi-axis length.

### Statistical tests and goodness of fit

Normalized $χ^{2}$ values in Figure 1E were calculated as $\frac{1}{N}⁢\sum_{i=1}^{N}\frac{(u_{i}-\mu_{i})^{2}}{\sigma_{i}^{2}},$ where N is the number of time-points in the curve, ui are the model predictions, and $\mu_{i}$ and $\sigma_{i}$ are the mean and standard deviation of the measured values, respectively. With these definitions, a fit with $χ^{2}<1$ is good.

The P-value in Figure 3D was calculated using a Mann-Whitney U test, and the two-tailed p-value of $p<10^{-4}$ indicates that the large and small vortex power data indeed come from different populations.

### Cell counts

The FUCCI system contains a period after M-phase where cells go dark, making FUCCI unreliable for cell counting. Instead, we developed and trained a convolutional neural network to reproduce nuclei from 4X phase contrast images using our in-house Fluorescence Reconstruction Microscopy tool (LaChance and Cohen, 2020) . The output of this neural network was then segmented in ImageJ to determine nuclei footprints and centroids.

### Tissue PIV and density measurements

Tissue velocity vector fields were calculated from 2 × 2 resized phase contrast image sequences using the free MATLAB package PIVLab (Thielicke and Stamhuis, 2014) with the FFT window deformation algorithm. We used a 1 st pass window size of 64 × 64 pixels and second pass of 32 × 32 pixels, with 50% pixel overlaps. This resulted in a 115 × 115 μm window. The window size was chosen to be smaller than the velocity-velocity correlation length but large enough to enable fast computation of PIV fields for many tissues. As seen in Figure 2—figure supplement 1, using a window size of 57 × 57 μm, which contains only a few cells, yields higher resolution velocity fields but does not qualitatively affect the measured speed and radial velocity. We focus on large-scale features of the velocity field, which are not affected by choosing a smaller PIV window size.

Local density was also calculated for each PIV window by counting the number of approximate nucleus centroids in that window. Data from PIV were smoothed in time with a moving average of 3 time points centered at each timepoint as before.

### Average kymographs

First, we constructed kymographs for individual tissues using distance from the tissue center as the spatial index for each measurement window corresponding to a kymograph pixel. We did not plot kymograph pixels for which more than 95% of the measurements at that distance were beyond the tissue footprint. We then averaged the individual tissue kymographs, aligning by the centers.

### Trajectory colorization

We first generated a plot of all relevant trajectories (Tinevez et al., 2017) colorized randomly in grayscale using a custom MATLAB (Mathworks) script. We then used the Fiji plugin OrientationJ on this plot to colorize the resulting image according to orientation (Püspöki et al., 2016).

### Cell density simulation

To test whether the observed spatiotemporal evolution of density $ρ⁢(r,t)$ could be explained by flow of material (rather than divisions, extrusions, and cell death), we solved the continuity equation for a homogenous tissue in a circular geometry with spatiotemporal evolution of average radial velocity $v_{r}⁢(r,t)$ as measured from PIV in experiments ( Figure 2B). The continuity equation is

$$
\frac{\partial⁡ρ}{\partial⁡t}=-\nabla⋅𝐣+k_{0}⁢ρ,
$$

where a homogeneous cell proliferation rate $k_{0}=1.04⁢h^{-1}$ is assumed throughout the tissue, which corresponds to the cell doubling time of 16 hr. The current density is $𝐣=ρ⁢𝐯_{𝐫}-D⁢\nabla⁡ρ$, where we included a diffusion term with a small diffusion constant $D=0.22⁢mm^{2}/h$ for numerical stability.

The continuity Equation (5) was discretized using the finite volume method (Eymard et al., 2000), which is briefly summarized below. The tissue domain was divided into an inner circle $Ω_{0}$ of radius $r_{1/2}=\frac{1}{2}⁢Δ⁢r$ and circular annuli $Ω_{i}$ with inner radii $r_{i-1/2}=(i-\frac{1}{2})⁢Δ⁢r$ and outer radii $r_{i+1/2}=(i+\frac{1}{2})⁢Δ⁢r$, respectively, where $i=1,2,3,…$ and $Δ⁢r=115⁢\mu⁢m$ corresponds to the width of 1 window in the PIV analysis. The continuity Equation (5) was then integrated over the inner circle $Ω_{0}$ and circular annuli $Ω_{i}$ as

$$
\frac{1}{A_{0}}\int_{0}^{r_{1/2}}(2\pirdr)\frac{∂ρ}{∂t}=\frac{1}{A_{0}}\int_{0}^{r_{1/2}}(2\pirdr)[−∇⋅j+k_{0}ρ],
$$



$$
\frac{1}{A_{i}}\int_{r_{i−1/2}}^{r_{i+1/2}}(2\pirdr)\frac{∂ρ}{∂t}=\frac{1}{A_{i}}\int_{r_{i−1/2}}^{r_{i+1/2}}(2\pirdr)[−∇⋅j+k_{0}ρ],
$$

where $A_{0}=\pi⁢r_{1/2}^{2}$ is the area of the inner circle $Ω_{0}$ and $A_{i}=\pi⁢r_{i+1/2}^{2}-\pi⁢r_{i-1/2}^{2}$ is the area of the circular annulus $Ω_{i}$. The integrals in Equation (6a, b) can be approximated as

$$
(7a)\frac{∂ρ(0,t)}{∂t}=−\frac{2\pi}{A_{0}}r_{1/2}j(r_{1/2},t)+k_{0}ρ(0,t),(7b)\frac{∂ρ(r_{i},t)}{∂t}=−\frac{2\pi}{A_{i}}[r_{i+1/2}j(r_{i+1/2},t)−r_{i−1/2}j(r_{i−1/2},t)]+k_{0}ρ(r_{i},t).
$$

Here, density profiles $ρ⁢(r_{i},t)$ are evaluated at $r_{i}=i⁢Δ⁢r$ for all $i=0,1,2,…$. Current densities are evaluated as $j⁢(r_{i+1/2},t)=ρ⁢(r_{i+1/2},t)⁢v_{r}⁢(r_{i+1/2},t)-D⁢[ρ⁢(r_{i+1},t)-ρ⁢(r_{i},t)]/Δ⁢r$ for all $i=0,1,2,…$, where $ρ⁢(r_{i+1/2},t)=[ρ⁢(r_{i},t)+ρ⁢(r_{i+1},t)]/2$ and $v_{r}⁢(r_{i+1/2},t)=[v_{r}⁢(r_{i},t)+v_{r}⁢(r_{i+1},t)]/2$. Density profiles $ρ⁢(r_{i},t)$ were then obtained by integrating Equation (7) with the forward Euler method using a time step $Δ⁢t=20$ min to align with experimental data collection of radial velocity profiles $v_{r}⁢(r_{i},t)$ from Figure 2B. The initial conditions were $ρ(r_{i},0)=2700 cells/mm^{2}$ for $r_{i}<r_{t⁢i⁢s⁢s⁢u⁢e}$ and $ρ⁢(r_{i},0)=0⁢cells/mm^{2}$ for $r_{i}>r_{t⁢i⁢s⁢s⁢u⁢e}$, where $r_{t⁢i⁢s⁢s⁢u⁢e}$ is the radius of tissue at the beginning of experiment. For comparison with experimental data (see Figure 4), we thresholded the kymographs of simulated density at $100⁢cells/mm^{2}$, which corresponds to much lower density than a confluent tissue.

### Relating local cell density to vortex centers

For panels (E) and (F) in Figure 4—figure supplement 1, we applied a Fourier low-pass filter on vorticity fields, retaining only large-scale vorticity fluctuations (with wavelengths longer than 1 mm). We excluded the tissue edge region (500 μm from the boundary) that is outward polarized and does not exhibit vortical flows. Each point in panels (E) and (F) corresponds to a point in the filtered vorticity field, plotted against the cell density in that point.

### Cell cycle analysis

The Fucci system consists of an RFP and GFP fused to proteins Cdt1 and Geminin, respectively (Sakaue-Sawano et al., 2008). Cdt1 levels are high during G1 and low during the rest of the cell cycle, while Geminin levels are high during the S, G2, and M phases (Sakaue-Sawano et al., 2008; Streichan et al., 2014). After capturing the appropriate fluorescence images, preprocessing was implemented identically for GFP and RFP channels to normalize channel histograms. To determine local cell cycle fraction, we determined the median value of RFP and GFP signal for each cell nucleus and manually selected thresholds for RFP and GFP signals separately to classify cell cycle for each cell as G0-G1-S (RFP above threshold), S-G2-M (RFP below threshold and GFP above threshold), or postmitotic (RFP and GFP below threshold). Local cell cycle fraction of each state could then be easily computed for each PIV pixel. Note that S phase (both RFP and GFP signals above threshold) did not prove to be a reliable feature for segmentation.

### Code and data availability

Data for representative small, large, and ellipse tissues (Heinrich et al., 2020) and analysis Matlab scripts (Heinrich, 2020) have been made available (copy archived at https://github.com/elifesciences-publications/FreelyExpandingTissues).
