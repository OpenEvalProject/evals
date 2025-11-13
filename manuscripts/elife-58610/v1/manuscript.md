# The biomechanical role of extra-axonemal structures in shaping the flagellar beat of Euglena gracilis

## Authors

- Giancarlo Cicconofri<sup>1</sup> ([ORCID: 0000-0003-1704-7609](https://orcid.org/0000-0003-1704-7609))
- Giovanni Noselli<sup>1</sup> ([ORCID: 0000-0001-8637-713X](https://orcid.org/0000-0001-8637-713X))
- Antonio DeSimone<sup>1</sup> ([ORCID: 0000-0002-2632-3057](https://orcid.org/0000-0002-2632-3057)) †

### Affiliations

1. SISSA - International School for Advanced Studies Trieste Italy
2. The BioRobotics Institute, Scuola Superiore Sant’Anna Trieste Italy

† Corresponding author

## Abstract

We propose and discuss a model for flagellar mechanics in Euglena gracilis. We show that the peculiar non-planar shapes of its beating flagellum, dubbed 'spinning lasso', arise from the mechanical interactions between two of its inner components, namely, the axoneme and the paraflagellar rod. The spontaneous shape of the axoneme and the resting shape of the paraflagellar rod are incompatible. Thus, the complex non-planar configurations of the coupled system emerge as the energetically optimal compromise between the two antagonistic components. The model is able to reproduce the experimentally observed flagellar beats and the characteristic geometric signature of spinning lasso, namely, traveling waves of torsion with alternating sign along the length of the flagellum.

## Introduction

Flagella and cilia propel swimming eukaryotic cells and drive fluids on epithelial tissues of higher organisms (Alberts et al., 2015). The inner structure of the eukaryotic flagellum is an arrangement of microtubules (MTs) and accessory proteins called the axoneme (Ax). A highly conserved structure in evolution, the Ax typically consists of nine cylindrically arranged MT doublets cross-bridged by motor proteins of the dynein family. An internal central pair of MTs is connected by radial spokes to the nine peripheral doublets, determining the typical '9+2’ axonemal structure. Motor proteins hydrolyze ATP to generate forces that induce doublet sliding. Due to mechanical constraints exerted by linking proteins (nexins) and the basal body, dynein-induced sliding of MTs translates into bending movements of the whole structure. Motor proteins are thought to self regulate their activity via mechanical feedback, generating the periodic beats of flagella, see, for example, Brokaw, 2009 and Lindemann and Lesich, 2010.

Despite a general consensus on the existence of a self-regulatory mechanism, the inner working of the Ax is not fully understood and it is still the subject of active research (Wan and Jékely, 2020). While bending-through-sliding is the accepted fundamental mechanism of flagellar motility, how specific flagellar shapes are determined is not yet clear. Nodal cilia present in early embryonic development display markedly non-planar beats (Buceta et al., 2005). On the other hand, for the most studied swimming microorganisms, such as animal sperm cells and the biflagellate alga Chlamydomonas reinhardtii, the flagellar beat is, to a good approximation, planar. For these organisms, beat planarity is thought to be induced by the inter-doublet links between one pair of MTs, typically those numbered 5 and 6 (Lin et al., 2012). These links inhibit the relative sliding of the 5-6 MTs pair, thus selecting a beating plane that passes through the center of the Ax and the midpoint between the inhibited MTs.

A remarkable deviation from the flagellar structure of the aforementioned organisms is found in euglenids and kinetoplastids. These flagellated protists have an extra element attached alongside the Ax (Cachon et al., 1988), a slender structure made of a lattice-like arrangement of proteins called 'paraxial’ or 'paraflagellar’ rod (PFR), see Figure 1. The latter name is more common, but the former is possibly more accurate (Rosati et al., 1991). PFRs are attached via bonding links to up to four axonemal MTs, depending on the species (Walne and Dawson, 1993). PFRs are thought to be passive but, at least in the case of Euglena gracilis, some degree of activity is not completely ruled out (Piccinni, 1975).

![Figure 1.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig1-v1.jpg)

**Figure 1.:** (a) A specimen of freely swimming Euglena gracilis, and (b) a sketch of the cross-section of its flagellum, as seen from the distal end. The flagellar inner structure is composed by the paraflagellar rod (PFR, textured), and the axoneme (Ax). The PFR is connected via bonding links to the axonemal doublets 1, 2, and 3. The inner structure of the flagellum is enclosed by the flagellar membrane (dotted contour). By inhibiting MTs’ sliding, the PFR selects the spontaneous bending plane of the Ax (dashed line). As a key geometric feature, the solid line that joins the Ax center $𝐫^{a}$ and the PFR center $𝐫^{p}$ crosses at an angle $ϕ^{p}$ the spontaneous bending plane. Doublets are numbered following the convention adopted in the electron microscopy studies Melkonian et al., 1982 and Bouck et al., 1990, to facilitate comparison. The opposite convention, in which microtubules are numbered in increasing order in the anti-clockwise direction when seen from the distal end of the Ax, is far more common in structural studies of cilia.

E. gracilis has two flagella, designated as dorsal and ventral. The ventral flagellum remains within the reservoir, an invaginated region of the cell. The dorsal, PFR-bearing, flagellum emerges from the reservoir and serves as a propulsive apparatus by means of periodic beating. In this paper, we show that the beating style of E. gracilis, sometimes dubbed ‘spinning lasso’ (Bovee, 1982), is characterized by a distinctive geometric signature, namely, traveling torsional peaks with alternating sign along the length of the flagellum. Moreover, we put forward and test the hypothesis that this distinctive beating style arises from the PFR-Ax mechanical interaction.

In order to put our hypothesis into context, we observe that the flagellar beat of PFR-bearing kinetoplastid organisms, such as Leishmania and Crithidia, is planar (Gadelha et al., 2007). An apparent exception to beat planarity in kinetoplastids is found in the pathogenic parasite Trypanosoma brucei, which shows a characteristic non-planar 'drill-like’ motion (Langousis and Hill, 2014). It has been claimed that the flagellar structure alone could account for the emergence this motion (Koyfman et al., 2011). However, the flagellum of T. brucei is not free, like that of Leishmania and Crithidia, but it is attached to the organism for most of its length, wrapped helically around the cell body. According to Alizadehrad et al., 2015, the flagellum-body mechanical interaction can alone explain T. brucei’s distinctive motion. Confirming this conclusion, Wheeler, 2017 showed that T. brucei mutants with body-detached flagellum generate fairly planar beating. It is conjectured that the PFR-Ax bonds operate as the 5-6 interdoublet links in Chlamydomonas and sperm cells, inhibiting MTs sliding and selecting a plane of beat (Woolley et al., 2006).

The spinning lasso beat of E. gracilis does not conform to this scenario. Indeed, E. gracilis beating style is characterized by high asymmetry and non-planarity. The full 3d flagellar kinematics of freely swimming cells has recently been revealed by Rossi et al., 2017 thanks to a mixed approach based on hydrodynamic theory and image analysis. As we report in the first part of this paper, the geometry of the spinning lasso is characterized by traveling waves of torsion with alternating sign along the flagellum length.

We argue that the key to the emergence of non-planarity lies in a prominent structural asymmetry of the PFR-Ax attachment in euglenid flagella. Figure 1 shows a sketch of the cross-section of the euglenid flagellum redrawn from the electron microscopy studies by Melkonian et al., 1982 and Bouck et al., 1990. Following the latter studies, we number MTs in increasing order in the clockwise direction, as seen from the distal end of the Ax. Notice that a different convention is commonly used in structural studies of cilia and flagella, see, for example, Lin and Nicastro, 2018. The PFR is attached to MTs 1, 2, and 3. We consider two lines. One line (dashed) passes through the center of the Ax and MT 2, in the middle of the bonding complex. The other (solid) line connects the center of the Ax and the center of the PFR. The two lines cross each other. This is the structural feature on which we build our model.

In modeling the flagellar complex, we assume that the bonding links to the PFR select the local spontaneous beating plane of the Ax, from the same principle of MTs’ sliding inhibition discussed above. The local spontaneous beating plane so generated passes through the dashed line in Figure 1. We follow closely Hilfinger and Jülicher, 2008 and Sartori et al., 2016a in our modeling of the Ax, while we use a simple elastic spring model for the PFR. We show that, under generic actuation, the two flagellar components cannot be simultaneously in their respective states of minimal energy, and this crucially depends on the offset between the spontaneous beating plane of the Ax (dashed line in Figure 1) and the line joining the PFR-Ax centers (solid line in Figure 1). Instead, the typical outcome is an elastically frustrated configuration of the system, in which the two competing components drive each other out of plane. Under dyneins activation patterns that, in the absence of extra-axonemal structures, would produce an asymmetric beat similar to those of Chlamydomonas (Qin et al., 2015), or Volvox (Sareh et al., 2013), the model specifically predicts the torsional signature of the spinning lasso.

Interestingly, the lack of symmetry of the spinning lasso beat produces swimming trajectories with rotations coupled with translations (Rossi et al., 2017). In turn, cell body rotations have a key role in the light-guided navigation behavior of phototactic unicellular organisms (Goldstein, 2015), and of E. gracilis in particular, which has recently attracted renewed attention (Giometto et al., 2015; Ogawa et al., 2016; Tsang et al., 2018). Rotations along the major axis of the cell body produced by the spinning lasso beat allow the light-sensing apparatus of the organism to constantly scan the environment, and align E. gracilis with light intensity gradients.

In light of these observations, our analysis shows that the beat of the euglenid flagellum can be seen as an example of a biological function arising from the competition between antagonistic structural components. It is not dissimilar from the body-flagellum interaction in T. brucei, which generates 3d motility. But the principle is much more general in biology and many other examples can be found across kingdoms and species, and at widely different scales. For instance in plants, a mechanism of seed dispersal arises from the mechanical competition between the two valves of the seed pods, see, for example Armon et al., 2011 for Bauhinia variegata and Hofhuis et al., 2016 for Cardamine hirsuta. Contraction by antagonistic muscles is key for animal movement and, in particular, for the functioning of hydrostatic skeletons (used from wormlike invertebrates to arms and tentacles of cephalopods, to the trunk of elephants, see Kier, 2012). The mechanical coupling of the helical periplasmic flagella to the rod-shaped cell cylinder determines the flat-wave morphology of the Lyme disease spirochete Borrelia burgdorferi (Dombrowski et al., 2009). Antagonistic contraction along perpendicularly oriented families of fibres is at work at the subcellular level, for example in the antagonistic motor protein dynamics in contractile ring structures important in eukaryotic cell division and development, see, for example Coffman et al., 2016. At the same subcellular scale, competing elastic forces arising from lipid-protein interactions are often crucial in determining the stability of complex shapes of the cellular membrane (Moser von Filseck et al., 2020), and in the case of the overall structure of the coronavirus envelope (Schoeman and Fielding, 2019).

### Observations

We first analyze the experimental data from the 3d reconstruction of the beating euglenid flagellum obtained in Rossi et al., 2017 for freely swimming organisms. Swimming E. gracilis cells follow generalized helical trajectories coupled with rotation around the major axis of the cell body. It is precisely this rotation that allows for a 3d reconstruction of flagellar shapes from 2d videomicroscopy images. E. gracilis takes many beats to close one complete turn around its major axis. So, while rotating, cells expose their flagellar beat to the observer from many different sides. Stereomatching techniques can then be employed to reconstruct the flagellar beat in full (assuming periodicity and regularity of the beat). Figure 2 shows $N=10$ different curves in space describing the euglenid flagellum in different instants within a beat taken from Rossi et al., 2017. The reconstruction fits well experimental data from multiple specimens. The figure also illustrates the computed torsion of the flagellar curve at each instant (not previously published). Torsion, the rate of change of the binormal vector, is the geometric quantity that measures the deviation of a curve from a planar path (see the ‘Results’ Section below for the formal definition). The 'spinning lasso’ exhibits here a distinct torsional signature: torsion peaks of alternate sign that travel from the proximal to the distal end of the flagellum. We return to this point below.

![Figure 2.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig2-v1.jpg)

**Figure 2.:** (a) $N=10$ flagellar configurations in evenly spaced instants (phases) within a periodic beat. (b) The same configurations overlapped and color coded according to their phases. (c) Computed torsion $\tau=\tau⁢(s)$ as a function of the flagellar arc length $s$. The plot is presented in terms of the normalized quantities $\tau/L^{-1}$ and $s/L$, where $L$ is the total length of the flagellum. Panels (a-b) are adapted from Figure 5.E of Rossi et al., 2017.

To further investigate E. gracilis’ flagellar beat, we observed stationary cells trapped at the tip of a capillary. In this setting, the flagellum is not perturbed by the hydrodynamic forces associated with E. gracilis’ rototranslating swimming motion. The beat can then manifest itself in its most 'pristine’ form. We recorded trapped cells during periodic beating. We rotated the capillary and recorded the same beating cell from different viewpoints. Videomicroscopy images from one specimen are shown in Figure 3 and Video 1. While with fixed specimens we cannot reconstruct reliably the 3d flagellar shapes, Figure 3 shows that there is a high stereographical consistency with the flagellar shapes obtained from swimming organisms. Flagellar non-planarity is thus not intrinsically associated with swimming, which reinforce the idea that the mechanism that generates non-planar flagellar shapes might be structural in origin. Moreover, these observations justify the choice we made in our study to focus on a model of flagellar mechanics for stationary organisms, allowing for substantial simplifications.

![Figure 3.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig3-v1.jpg)

**Figure 3.:** (a) A specimen of Euglena gracilis trapped at the tip of a capillary (bottom). The typical outline of its beating flagellum is that of a looping curve, which is consistent with the outline of a simple curve with two concentrated torsional peaks of alternate sign along the length of the curve, that is, a torsion dipole (top). (b) Close-up images of the same specimen of capillary-trapped (CT) E. gracilis as seen from different viewpoints, upon successive ∼90° turns of the capillary tube. The body orientation with respect to the objective is estimated from the anatomy of the cell, and in particular from the position of the eyespot (a visible light-sensing organelle present on the cell surface). Microscopy images are decorated with the tracked outlines of the flagellum in different phases (same color coding as in Figure 2). The outlines (2d projections) of the 3d reconstructed flagellar beat of freely swimming (FS) specimens are shown for comparison.

![Video 1.](https://cdn.elifesciences.org/articles/58610/elife-58610-video1.mp4.jpg)

Getting back to the torsion measurement in Figure 2, we show here that the pattern of torsional peaks of alternate sign is consistent with E. gracilis’ flagellar shapes as seen from common 2d microscopy, for either swimming or trapped organisms. Typically, the 2d outline (i.e. the projection on the focal plane) of a beating euglenid flagellum is that of a looping curve, see Figure 3 and, for example Tsang et al., 2018 for independent observations. Consider now an idealized 3d model of the spinning lasso geometry: a 'torsion dipole’. This simple geometric construction, shown in Figure 3, consists of a curve with two singular points of concentrated torsion with opposite sign. If we move along the curve, from proximal end to distal end, we first remain on a fixed plane (blue). Then the plane of the curve abruptly rotates by 90° (red plane) first, and then back by 90° in the opposite direction (yellow plane). These abrupt changes correspond to concentrated torsional peaks of opposite sign. When seen in a two-dimensional projection, the torsion dipole generates a looping curve, which closely matches euglenid flagella’s outlines during a spinning lasso beat.

### Mechanical model

We model Ax and PFR as cylindrical structures with deformable centerlines, see Figure 4. The euglenid flagellum is the composite structure consisting of Ax and PFR attached together. We suppose that the Ax is the only active component of the flagellum, whereas the PFR is purely passive. Our mechanical model builds on the definition of the total internal energy of the flagellum

$$
𝒲=𝒲_{pas}^{a}+𝒲_{act}^{a}+𝒲^{p}
$$

which is given by the sum of three terms: the passive (elastic) internal energy $𝒲_{p⁢a⁢s}^{a}$ of the Ax, the active internal energy $𝒲_{a⁢c⁢t}^{a}$ of the Ax (generated by dynein action), and the (passive, elastic) internal energy $𝒲^{p}$ of the PFR. The passive internal energy of the Ax is given by

$$
𝒲_{p⁢a⁢s}^{a}=\frac{1}{2}⁢\int_{0}^{L}B^{a}⁢(U_{1}⁢(s)^{2}+U_{2}⁢(s)^{2})+C^{a}⁢U_{3}⁢(s)^{2}⁢d⁢s,
$$

where $U_{1}$ and $U_{2}$ are the bending strains of the Ax, $U_{3}$ is the twist, $B^{a}$ and $C^{a}$ are the bending and twist moduli (respectively), and $L$ is the total length of the Ax centerline $𝐫^{a}$. Bending strains and twist depend on the arc length $s$ of the centerline, and they are defined as follows. We associate to the curve $𝐫^{a}$ an orthonormal frame $𝐝_{i}⁢(s)$, with $i=1,2,3$, which determines the orientation of the orthogonal sections of the Ax (enclosed by light blue circles in Figure 4). The unit vectors $𝐝_{1}⁢(s)$ and $𝐝_{2}⁢(s)$ define the plane of the orthogonal section at s. The unit vector $𝐝_{1}⁢(s)$ lies on the line that connects the center of the Ax to MT 2, the center of the bonding links complex, see Figure 1. The unit vector $𝐝_{3}⁢(s)=\partial_{s}⁡𝐫^{a}⁢(s)$ lies perpendicular to the orthogonal section. Bending strains and twist are then given by

$$
U_{1}=∂_{s}d_{2}⋅d_{3},U_{2}=∂_{s}d_{3}⋅d_{1},andU_{3}=∂_{s}d_{1}⋅d_{2}.
$$

Thus, $U_{1}$ and $U_{2}$ measure the bending of the Ax on the local planes $𝐝_{2}$-$𝐝_{3}$ and $𝐝_{3}$-$𝐝_{1}$, respectively, while the twist $U_{3}$ is given by the rotation rate of the orthonormal frame around the tangent $𝐝_{3}$ to the centerline.

![Figure 4.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig4-v1.jpg)

**Figure 4.:** (a) Geometry of the Ax. MTs lie on a tubular surface $C(s,ϕ)$ parametrized by generalized polar coordinates $s$ and $ϕ$, where $s$ is the arc length of the axonemal centerline $𝐫^{a}$. The unit vectors $𝐝_{1}⁢(s)$ and $𝐝_{2}⁢(s)$ lie on the orthogonal cross sections of the Ax (light blue circles). The material sections of the Ax are given by the curves $ϕ↦𝐂⁢(s,ϕ)$ (red), which connect points of neighbouring axonemal MTs corresponding to the same arc length $s$. Bend deformations of the axoneme are generated by the shear (collective sliding) of MTs. The shear is quantified by the angle between the orthogonal sections and the material sections of the Ax. (b) Geometry of the euglenid flagellum, detail of the Ax-PFR attachment. The unit vectors $𝐠_{1}⁢(s)$ and $𝐠_{2}⁢(s)$ generate the plane of the PFR’s cross sections. The vector $𝐠_{1}⁢(s)$ is parallel to the outer unit normal to the axonemal surface $𝐍⁢(s,ϕ^{p})$, while $𝐠_{2}⁢(s)$ is parallel to the tangent vector to the material section $\partial_{ϕ}⁡𝐂⁢(s,ϕ^{p})$.

We remark that the right-hand side of Equation 2 is formally identical to a classical expression arising in Kirchhoff’s theory for elastic rods (Goriely, 2017). Our rod is however non-standard because it consists of a hollow tubular structure arising as the envelope of nine individual MTs. In Appendix 1, we model each of the MTs as a standard rod with (full cross-section and) bending and twisting moduli $B^{m}$ and $C^{m}$. We then show that the geometry and deformations of the Ax (centerline $𝐫^{a}$, frame vectors $𝐝_{1}$, $𝐝_{2}$, and $𝐝_{3}$, bending strains and twist) determine the geometry and deformations of the individual MTs. By summing the elastic contributions of individual MTs, we obtain Equation 2 as the elastic energy of the assembly, with $B^{a}=9⁢B^{m}$ and $C^{a}=9⁢C^{m}$.

The active internal energy of the Ax is defined as minus the total mechanical work of the dyneins

$$
𝒲_{a⁢c⁢t}^{a}=-\int_{0}^{L}(H_{1}⁢(s)⁢\gamma_{1}⁢(s)+H_{2}⁢(s)⁢\gamma_{2}⁢(s))⁢𝑑s-(H^_{1}⁢\gamma_{1}⁢(L)+H^_{2}⁢\gamma_{2}⁢(L)),
$$

where $\gamma_{1}$ and $\gamma_{2}$ are the two variables that quantify the shear (i.e., collective sliding) of MTs, while $H_{1}$ and $H_{2}$ are the corresponding shear forces exerted by molecular motors. Following Sartori et al., 2016b we also allow for singular shear forces, $H^_{1}$ and $H^_{2}$, concentrated at the distal end of the Ax. These forces arise naturally, as we remark after Equation 23 in the ‘Results’ Section.

The active internal energy can be written in a more natural way at the level of individual MT pairs in terms of the work done by the sliding forces $F_{j}$ generated by the dyneins cross-bridging MTs $j$ and $j+1$ against their relative sliding displacements $\sigma_{j}$, for $j=1,2,…,9$. These forces and displacements are defined in detail in Appendix 1, and their work computed in Equation 35. The way Equation 35 gives rise to the equivalent reformulation (Equation 4) in terms of global cross-section variables, the forces $H_{i}$ and shears $\gamma_{i}$, is also discussed there. Here, we simply notice that the structural constraints of the Ax lead to simplifications on the kinematics. These constraints do not allow MTs to slide by whatever amount, and the sliding of MT pairs $\sigma_{j}$ are not independent. Rather, there are only two degrees of freedom that determine MTs sliding, which are given by the shear variables $\gamma_{1}$ and $\gamma_{2}$. Moreover, again due to the structural constraints of the Ax, the shear variables are coupled to the bending strains (Equation 3), as discussed further below. In Appendix 1, we derive the linear relations between the shear variables and the individual sliding of MT pairs (Equation 36). We also compute the relations between the dynein forces $F_{j}$ acting on each pair of adjacent MTs and the shear forces $H_{1}$ and $H_{2}$ (Equation 37). The singular shear forces $H^_{1}$ and $H^_{2}$ arise from concentrated sliding forces $F^_{j}$ at the distal end of the Ax in an analogous way.

To explain how the shear variables $\gamma_{1}$ and $\gamma_{2}$ are related to the MTs' kinematics, we observe that the MTs centerlines $𝐫^{j}$, for $j=1,2⁢…⁢9$ , are given by $𝐫^{j}⁢(s)=𝐂⁢(s,ϕ_{j})$, where $ϕ_{j}=2⁢\pi⁢(2-j)/9$, and

$$
𝐂⁢(s,ϕ)≈𝐫^{a}⁢(s)+ρ^{a}⁢(cos⁡ϕ⁢𝐝_{1}⁢(s)+sin⁡ϕ⁢𝐝_{2}⁢(s)+(cos⁡ϕ⁢\gamma_{1}⁢(s)+sin⁡ϕ⁢\gamma_{2}⁢(s))⁢𝐝_{3}⁢(s))
$$

is the parametrization of the cylindrical surface of the Ax ($ρ^{a}$ is the Ax radius) in terms of the centerline arc length $s$ and the angle $ϕ$. A special axonemal deformation with $\gamma_{2}=0$ is shown in Figure 4. In this case, the Ax is bent into a circular arc, and the centerline $𝐫^{a}$ lies on the plane generated by the unit vectors $𝐝_{1}$ and $𝐝_{3}$. The shear variable $\gamma_{1}⁢(s)\neq0$ has here a simple geometrical interpretation. For each fixed $s$ the curve $ϕ↦𝐂⁢(s,ϕ)$ describes what we call the ‘material’ section of the Ax at $s$ (red curves in Figure 4). The material section is a planar ellipse centered in $𝐫^{a}⁢(s)$ which connects points of neighboring MTs’ corresponding to the same arc length. Equation 5 says that $\gamma_{1}⁢(s)$ is the tangent of the angle at which the material sections at $s$ intersect the orthogonal sections at $s$.

As mentioned above, the kinematic constraints of the Ax couple the shear variables with bending strains. We have

$$
\gamma_{1}⁢(s)=\int_{0}^{s}U_{2} and \gamma_{2}⁢(s)=-\int_{0}^{s}U_{1}.
$$

The above formulas (whose detailed derivation is given in Appendix 1) underlie the essential mechanism of axonemal motility: collective sliding of MTs generates bending of the whole Ax. We point out here that there is no coupling between the shear variables $\gamma_{1},\gamma_{2}$ and the twist $U_{3}$, a fact that will have consequences in the remainder.

The special axonemal deformation in Figure 4 shows the case in which $U_{1}⁢(s)=0$ and $U_{2}⁢(s)=K$, so that the Ax is bent into a circular arc of radius $1/K$. While $\gamma_{2}⁢(s)=0$, the shear variable $\gamma_{1}⁢(s)=K⁢s$ increases linearly with $s$. Material and orthogonal sections coincide at the base (the basal body impose no shear at $s=0$) and the angle between them grows as we move along the centerline towards the distal end of the Ax. In order for the Ax to bend, MTs from one side of the Ax must be driven toward the distal end while the others must be driven toward the proximal end.

We remark here that Equation 4 defines the most general active internal energy generated by molecular motors, and we do not assume at this stage any specific (spatial) organization of dynein forces. We will introduce specific shear forces later in the ‘Results’ Section.

The PFR is modelled as an elastic cylinder with circular cross sections of radius $ρ^{p}$ and rest length $L$. We assume that the PFR can stretch and shear. The total internal energy of the PFR is given by

$$
𝒲^{p}=\frac{1}{2}⁢\int_{0}^{L}D^{p}⁢(V_{1}⁢(s)^{2}+V_{2}⁢(s)^{2})+E^{p}⁢V_{3}⁢(s)^{2}⁢d⁢s
$$

where $V_{1}$ and $V_{2}$ are the shear strains, $V_{3}$ is the stretch, $D^{p}$ and $E^{p}$ are the shear and stretching moduli, respectively. We are neglecting here the PFR’s bending and twisting stiffness. Classical estimations on homogeneous elastic rods, see, for example Goriely, 2017, show that bending and twist moduli scale with the fourth power of the cross section radius, whereas shear and stretching moduli scale with the second power and hence they are dominant for small radii. We assume that dynein forces are strong enough to induce shear in the PFR, thus PFR’s bending and twist contributions to the energy of the flagellum become negligible. We are also neglecting Poisson effects by treating the PFR cross-sections as rigid.

The PFR shear strains and stretch are defined as follows. The cross-sections centers of the PFR lie on the curve $𝐫^{d}$, and their orientations are given by the orthonormal frame $𝐠_{i}⁢(s)$, with $i=1,2,3$. The unit vectors $𝐠_{1}⁢(s)$ and $𝐠_{2}⁢(s)$ determine the cross section plane centered at $𝐫^{p}⁢(s)$, while the unit vector $𝐠_{3}⁢(s)$ is orthogonal to it. The curve $𝐫^{p}$ is not parametrized by arc length and $𝐠_{3}$ is not in general aligned with the tangent to $𝐫^{p}$. Shear strains and stretch are given by the formulas

$$
V_{1}=\partial_{s}⁡𝐫^{p}⋅𝐠_{1},V_{2}=\partial_{s}⁡𝐫^{p}⋅𝐠_{2},and V_{3}=∥\partial_{s}⁡𝐫^{p}∥-1.
$$

The shear strains thus depend on the orientation of the cross sections with respect to the centerline (tangent), while the stretch measures the elongation of the centerline.

The PFR-Ax attachment couples the kinematics of the two substructures, see Figure 4. In the remainder, we formalize the attachment constraint and we show how the PFR’s shear strains and stretch (Equation 8), and thus the flagellar energy (Equation 1), are completely determined by the Ax kinematic variables.

For each $s$, the PFR cross-section centered at $𝐫^{p}⁢(s)$ is in contact with the Ax surface at the point $𝐂⁢(s,ϕ^{p})$ for a fixed angle coordinate $ϕ^{p}$, see Figure 1 and Melkonian et al., 1982. The PFR centerline is given by

$$
𝐫^{p}⁢(s)=𝐂⁢(s,ϕ^{p})+ρ^{p}⁢𝐍⁢(s,ϕ^{p}),
$$

where $𝐍⁢(s,ϕ^{p})≈𝐝_{1}⁢(s)⁢cos⁡ϕ^{p}+𝐝_{2}⁢(s)⁢sin⁡ϕ^{p}$ is the outer unit normal to the axonemal surface at $𝐂⁢(s,ϕ^{p})$. The normal vector $𝐍⁢(s,ϕ^{p})$ lies on the plane of the PFR cross-section centered at $𝐫^{p}⁢(s)$. Indeed, we have $𝐠_{1}⁢(s)=𝐍⁢(s,ϕ^{p})$ for the first unit vector of the PFR orthonormal frame. Only one more degree of freedom remains, namely $𝐠_{2}⁢(s)$, which must be orthogonal to $𝐍⁢(s,ϕ^{p})$, to fully characterize the orientations of the PFR cross-sections. Here is where the bonding links attachments are introduced in the model. The bonding links of the PFR cross-section centered at $𝐫^{p}⁢(s)$ are attached to three adjacent MTs at the same MTs’ arc length $s$. The individual attachments are therefore located on the material section of the Ax at $s$. Given this, $𝐠_{2}⁢(s)$ is imposed to be parallel to $\partial_{ϕ}⁡𝐂⁢(s,ϕ^{p})$, the tangent vector to the material section of the Ax at the point of contact $𝐂⁢(s,ϕ^{p})$, see Figure 4. This condition critically couples MTs’ shear to the orientations of the PFR cross-sections, as further demonstrated below.

To summarize, we have the following formulas for the PFR orthonormal frame vectors

$$
𝐠_{1}⁢(s)=𝐍⁢(s,ϕ^{p}),𝐠_{2}⁢(s)=\partial_{ϕ}⁡𝐂⁢(s,ϕ^{p})/∥\partial_{ϕ}⁡𝐂⁢(s,ϕ^{p})∥,and 𝐠_{3}⁢(s)=𝐠_{1}⁢(s)\times𝐠_{2}⁢(s).
$$

By replacing the expressions in Equations 9-10 in Equation 8, we obtain formulas for the shear strains and stretch of the PFR in terms of the Ax kinematic parameters. The shear strain $V_{1}$ and the stretch $V_{3}$ are found to be of order $ρ^{p}∼ρ^{a}$ (see Appendix 1 for detailed calculations). Since $ρ^{p}$ is small compared to the length scale $L$ of both PFR and Ax, we neglect these quantities. The only non-negligible contribution to the PFR energy is thus given by the shear strain $V_{2}$. After linearization, we have $V_{2}≈-sin⁡ϕ^{p}⁢\gamma_{1}+cos⁡ϕ^{p}⁢\gamma_{2}$. The PFR energy in terms of Ax kinematic parameters is then given by

$$
𝒲^{p}≈\frac{1}{2}⁢\int_{0}^{L}D^{p}⁢(-sin⁡ϕ^{p}⁢\gamma_{1}⁢(s)+cos⁡ϕ^{p}⁢\gamma_{2}⁢(s))^{2}⁢𝑑s.
$$

The shear of axonemal MTs determines the orientation of the PFR cross-sections. In Figure 5 (middle pictures), we show an example of this kinematic interplay. The Ax is again bent in an arc of a circle on the plane $𝐝_{1}-𝐝_{3}$, with $U_{1}⁢(s)=0$, $U_{2}⁢(s)=K$, $\gamma_{1}⁢(s)=K⁢s$, and $\gamma_{2}⁢(s)=0$. PFR and Ax centerlines run parallel to each other, indeed from Equation 9 we have that $\partial_{s}⁡𝐫^{a}≈\partial_{s}⁡𝐫^{p}$ for every deformation. The linking bonds impose a rotation of the cross sections of the PFR as we progress from the proximal to the distal end of the flagellum, generating shear strain $V_{2}⁢(s)=-sin⁡ϕ^{p}⁢\gamma_{1}⁢(s)=-sin⁡ϕ^{p}⁢K⁢s$ on the PFR. This mechanical interplay leads to non-planarity of the euglenid flagellar beat. This mechanism is controlled by the offset between the PFR-Ax joining line and the local spontaneous bending plane of the Ax, as further discussed in the ‘Results’ Section.

![Figure 5.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig5-v1.jpg)

**Figure 5.:** The Ax-PFR mechanical interplay is explained in a three-steps argument (left to right). Consider first the two separated structures in their spontaneous configurations (left). The Ax is bent into a planar arc while the PFR is straight. Then, the PFR is forced to match to the Ax, while the latter is kept in its spontaneous configuration (middle). The attachment constraint induces shear strains in the PFR, such that the composite system cannot be in mechanical equilibrium without external forcing. When the composite system is released (right), it reaches equilibrium by the relaxation of the PFR shear, which induces additional distortion of the Ax. At equilibrium, an optimal energy compromise is reached, which is characterized by an emergent non-planarity.

### Equilibria

Under generic (steady) dynein actuation, that is, given $H_{1}$ and $H_{2}$ (not time-dependent), and in the absence of external forces, the flagellum deforms to its equilibrium configuration $\delta⁢𝒲=0$. Bending strains and twist at equilibrium solve the equations

$$
B^{a}⁢\partial_{s}⁡𝐔-𝐇^{⊥}-D^{p}⁢𝐞_{p}⊗𝐞_{p}⁢\int_{0}^{s}𝐔= and C^{a}⁢\partial_{s}⁡U_{3}=0,
$$

where $𝐔=(U_{1},U_{2})$ is the bending vector, $𝐞_{p}=(cos⁡ϕ^{p},sin⁡ϕ^{p})$, and $𝐇^{⊥}=(-H_{2},H_{1})$. We use the symbol $𝐚⊗𝐛$ to denote the matrix with components $(𝐚⊗𝐛)_{i⁢j}=a_{i}⁢b_{j}$. The field Equation 12 is complemented by the boundary conditions

$$
B^{a}⁢𝐔⁢(L)+𝐇^^{⊥}= and U_{3}⁢(L)=0,
$$

where $𝐇^^{⊥}=(-H^_{2},H^_{1})$. Equations 12, 13 can be interpreted as the torque balance equations of the Ax. The derivative of the (elastic) bending moment and the internal shear stresses balance the torque per unit length exerted by the PFR on the Ax, which is given by the $D^{p}$-dependent term appearing in the first equation. The torque depends on the integral of the bending vector, making the balance equations non-standard (integrodifferental instead of differential). This dependency is due to the fact that the torque arises from the shear deformations of the PFR, which are induced by the shear of axonemal MTs, which is, in turn, related to axonemal bending strains via the integral relations (Equation 6). The torque exerted by the PFR on the Ax is sensitive to the direction given by the unit vector $𝐞_{p}$, hence it depends on the angle $ϕ^{p}$ between the Ax-PFR joining line and the unit vector $𝐝_{1}$.

### Hydrodynamics

We consider here our mechanical model in the presence of external forces. For simplicity, we ignore the possible forces exerted by the cell surface on the non-emergent portion of the flagellum, located inside the reservoir of the cell. Indeed, we suppose that the flagellum is immotile and straight in the region inside the reservoir. We can assume, therefore, that our model effectively describes the flagellum from its emergence point outwards. The only forces the flagellum is subject to come from fluid interaction, which we assume to act all along its length. We consider the extended functional

$$
ℒ=𝒲+\int_{0}^{L}𝚲⋅(\partial_{s}⁡𝐫^{a}-𝐝_{3})
$$

where $𝚲$ is the Lagrange multiplier vector enforcing the constraint $\partial_{s}⁡𝐫^{a}=𝐝_{3}$. We treat the fluid-flagellum interaction in the local drag approximation of Resistive Force Theory, see for example Wolgemuth et al., 2000. In this approximation, viscous forces and torques depend locally on the translational and rotational velocity of the flagellum, represented here for simplicity by the translational and rotational velocity of the Ax. The external viscous forces $𝐅$ and torques $𝐆$ (per unit length) acting on the flagellum are given by

$$
F=−\mu_{⊥}(Id−d_{3}⊗d_{3})∂_{t}r^{a}−\mu_{||}d_{3}⊗d_{3}∂_{t}r^{a}andG=−\mu_{r}(∂_{t}d_{1}⋅d_{2})d_{3},
$$

where $\mu_{⊥}$, $\mu_{||}$, and $\mu_{r}$ are the normal, parallel, and rotational drag coefficient (respectively), and $𝐈𝐝$ is the identity tensor. The principle of virtual work imposes

$$
\delta⁢ℒ=\int_{0}^{L}𝐅⋅\delta⁢𝐫^{a}+𝐆⋅\delta⁢𝜽
$$

for every variation $\delta⁢𝐫^{a}$ and $\delta⁢𝜽=\delta⁢\theta_{1}⁢𝐝_{1}+\delta⁢\theta_{2}⁢𝐝_{2}+\delta⁢\theta_{3}⁢𝐝_{3}$, where $\delta⁢\theta_{1}=(\delta⁢𝐝_{2}⋅𝐝_{3})$, $\delta⁢\theta_{2}=(\delta⁢𝐝_{3}⋅𝐝_{1})$, and $\delta⁢\theta_{3}=(\delta⁢𝐝_{1}⋅𝐝_{2})$. Linearizing the force balance equations derived from Equation 16 we obtain the following equations for bending strains and twist

$$
\mu_{⊥}⁢\partial_{t}⁡𝐔=-B^{a}⁢\partial_{s}^{4}⁡𝐔+\partial_{s}^{3}⁡𝐇^{⊥}+D^{p}⁢𝐞_{p}⊗𝐞_{p}⁢\partial_{s}^{2}⁡𝐔
$$



$$
and \mu_{r}⁢\partial_{t}⁡U_{3}=C^{a}⁢\partial_{s}^{2}⁡U_{3},
$$

which are decoupled from the extra unknown $𝚲$. Equations 17 and 18 are complemented by the boundary conditions

$$
B^{a}⁢𝐔|_{s=L}+𝐇^^{⊥}=,(B^{a}⁢\partial_{s}⁡𝐔-𝐇^{⊥}-D^{p}⁢𝐞_{p}⊗𝐞_{p}⁢\int_{0}^{s}𝐔)|_{s=L}=,U_{3}|_{s=L}=0,\partial_{s}⁡U_{3}|_{s=L}=0,
$$



$$
(B^{a}⁢\partial_{s}^{2}⁡𝐔-\partial_{s}⁡𝐇^{⊥}-D^{p}⁢𝐞_{p}⊗𝐞_{p}⁢𝐔)|_{s=0}=,and (B^{a}⁢\partial_{s}^{3}⁡𝐔-\partial_{s}^{2}⁡𝐇^{⊥}-D^{p}⁢𝐞_{p}⊗𝐞_{p}⁢\partial_{s}⁡𝐔)|_{s=0}=.
$$

The details of the derivation of Equations 17–20 are provided in Appendix 2.

Once we solve for $U_{1}$, $U_{2}$, and $U_{3}$ either the equilibrium Equations 12, 13 or the dynamic Equations 17–20, the shape of the flagellum can be recovered. In particular, we obtain the orthonormal frame $𝐝_{i}$ with $i=1,2,3$ by solving Equation 53, while the centerline of the Ax is recovered by integrating $\partial_{s}⁡𝐫^{a}=𝐝_{3}$.

## Results

We analyze the geometry of the centerline $𝐫^{a}$ which, due to the slenderness of the flagellar structure, is a close proxy for the shape of the flagellum.

In general, the shape of a curve is determined by its curvature $κ$ and torsion $\tau$. Since $𝐫^{a}$ is parametrized by arc length, the two quantities are given by the formulas $∂_{s}t=κn$ and $\partial_{s}⁡𝐛=-\tau⁢𝐧$, where $𝐭=\partial_{s}⁡𝐫^{a}$, $𝐧=\partial_{s}⁡𝐭/|\partial_{s}⁡𝐭|$, and $𝐛=𝐭\times𝐧$ are the tangent, normal, and binormal vector to the curve $𝐫^{a}$, respectively. Given $κ$ and $\tau$, $𝐫^{a}$ is uniquely determined up to rigid motions.

From the previous definitions and from Equation 3 we obtain the relations between curvature, torsion, bending, and twist. In compact form these relations are given by

$$
U_{1}+i⁢U_{2}=κ⁢e^{i⁢ψ} and \tau=\partial_{s}⁡ψ+U_{3},
$$

which hold for $𝐔\neq0$. In Equation 21 we introduced the angle $ψ$ that the bending vector $𝐔=(U_{1},U_{2})$ forms with the line $U_{2}=0$, see Figure 6. Now, at equilibrium (Equation 12) we have

$$
U_{3}=0,
$$

under any dynein actuation. In other words, axonemal deformations are twistless. This is, fundamentally, a consequence of the fact that shear of axonemal MTs and twist are uncoupled (Equation 6). The torsion of the centerline $𝐫^{a}$ is our main focus, since we are interested in emergent non-planarity. Combining Equation 21 and Equation 22 we have that torsion can arise only from the rotation rate $\partial_{s}⁡ψ$ of the bending vector $𝐔$ along the length of the flagellum. This last observation will be important in the following.

![Figure 6.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig6-v1.jpg)

**Figure 6.:** (a) The bending vector $𝐔⁢(s)=(U_{1}⁢(s),U_{2}⁢(s))$ traces a curve on the plane of the bending parameters $U_{1}$ and $U_{2}$. The norm of the bending vector determines the curvature $κ⁢(s)=|𝐔⁢(s)|$ of the flagellum. The rate of change of the angle $ψ⁢(s)$ determines the torsion $\tau=\partial_{s}⁡ψ$. (b–f) Bending vectors’ traces of flagellar equilibrium configurations under the same (steady) dynein actuation, but different values of the material parameter $ν=D^{p}/(B^{a}⁢L^{-2})$. Equilibria are minimizer of the energy $𝒲=𝒲^{a}+𝒲^{p}$. For small values of $ν$, the Ax component of the energy $𝒲^{a}$ dominates. In this case, $𝐔$ is close to the target bending vector $(0,U_{2}^{*})$ where $U_{2}^{*}⁢(s)=A_{0}+A_{1}⁢sin⁡(2⁢\pi⁢s/L)$. For large values of $ν$ the PFR component of the energy $𝒲^{p}$ dominates, and equilibria are dragged closer to the line orthogonal to the vector $𝐞_{p}$ (dashed green). The bending vector undergoes rotations which result in torsional peaks of alternating sign.

### Dyneins’ actuation induced by sliding inhibition

Under the assumptions Equation 22 and Equation 24, the flagellar energy (Equation 1) can be rewritten as

$$
𝒲=\frac{1}{2}\int_{0}^{L}B^{a}‖U−(U_{1}^{∗}U_{2}^{∗})‖^{2}+D^{p}(\int_{0}^{s}e_{p}⋅U)^{2}−B^{a}(U_{1}^{∗}^{2}+U_{2}^{∗}^{2}),whereU_{1}^{∗}(s)=(H^_{2}+\int_{s}^{L}H_{2})/B^{a}andU_{2}^{∗}(s)=−(H^_{1}+\int_{s}^{L}H_{1})/B^{a}
$$

are the target bending strains generated by the dynein forces. The use of this terminology is clear from Equation 23. The effect of dynein actuation at equilibrium (when the energy is minimized) is to bring the bending strains $U_{1}$ and $U_{2}$ as close as possible to $U_{1}^{*}$ and $U_{2}^{*}$, respectively. The emerging bending strains and the target bending strains might not match due to the interference by the PFR component of the energy ($D^{p}\neq0$). From the formulas for the target bending strains in Equation 23, we can infer the importance of the concentrated shear forces $H^_{1}$ and $H^_{2}$. Without these forces, admissible spontaneous configurations of the Ax would be ruled out. If the concentrated shear forces are null, for example, the Ax cannot spontaneously bend into a circular arc. Indeed, for a circular arc of radius $1/K$ on the plane $𝐝_{1}$-$𝐝_{3}$ we must have $U_{2}^{*}=0$ and $U_{2}^{*}=K$. In this case, from Equation 23 we have that $-H_{1}/B^{a}=\partial_{s}⁡U_{2}^{*}=0$, which implies $H_{1}=0$ and $H^_{1}=-B^{a}⁢K$, so the concentrated forces must be non null.

Our working hypothesis is that MTs' sliding stretches the Ax-PFR bonding links, which, in turn, inhibits sliding of MTs’ 1, 2, and 3, and triggers a dynein organization (via mechanical feedback) similar to the one present in Chlamydomonas. We take this feedback-based self-organization process as a given, and we consider a force pattern that produces local spontaneous bending on the plane $𝐝_{1}⁢(s)$-$𝐝_{3}⁢(s)$, as shown in Figure 1. This is equivalent to require that $U_{1}^{*}=0$, which leads to the following condition on the shear forces

$$
H_{2}=H^_{2}=0.
$$

### Emergence of non-planarity

We consider here the equilibrium Equation 12 under the hypothesis (Equation 24). We look at the equilibrium configurations for every possible value of the angle $ϕ^{p}$ between the Ax-PFR joining line and the spontaneous bending plane of the Ax, even though the value of actual interest for E. gracilis is $ϕ^{p}≈-2⁢\pi/9$. We can prove analytically the following statement: if the Ax-PFR joining line is neither parallel nor orthogonal to the spontaneous bending plane of the Ax, then the emergent flagellar shapes are non-planar.

Indeed, suppose $H_{1}\neq0$. From Equation 21 and Equation 22 it follows that the shape of the flagellum is planar $(\tau=0)$ if and only if the angle $ψ$ of the bending vector $𝐔⁢(s)=(U_{1}⁢(s),U_{2}⁢(s))$ is constant. The bending vector must therefore be confined on a line for every $s$. In this case there must be two constants $c_{1}$ and $c_{2}$ such that $U_{1}⁢(s)=c_{1}⁢U⁢(s)$ and $U_{2}⁢(s)=c_{2}⁢U⁢(s)$ for some scalar function $U$. Now, if a planar $𝐔$ is a solution of Equation 12, we must have

$$
c_{1}B^{a}∂_{s}U−D^{p}cos⁡ϕ^{p}(c_{1}cos⁡ϕ^{p}+c_{2}sin⁡ϕ^{p})\int_{0}^{s}U=0,
$$



$$
c_{2}B^{a}∂_{s}U−D^{p}sin⁡ϕ^{p}(c_{1}cos⁡ϕ^{p}+c_{2}sin⁡ϕ^{p})\int_{0}^{s}U=H_{1},
$$

with $c_{1}⁢U⁢(L)=0$ and $c_{2}⁢U⁢(L)=-H^_{1}/B^{a}$. If $ϕ^{p}∉{0,\pi/2,\pi,3⁢\pi/2}$ the system of Equations 25, 26 admits no solution. Indeed, suppose first that $H^_{1}=0$. Since $H_{1}\neq0$ we must have $(c_{1},c_{2})\neq(0,0)$. However, in this case, Equation 25 admits the unique solution $U=0$, which is incompatible with Equation 26. If $H^_{1}\neq0$, then the boundary conditions impose $c_{1}=0$, but in this case Equation 25 has again $U=0$ as a unique solution, which is incompatible with both the boundary conditions and with Equation 26. Our statement is thus proved.

For $ϕ^{p}≈-2⁢\pi/9$, the characteristic value for E. gracilis, the non-planarity of flagellar shapes is not just possible. It is the only outcome under any non-trivial dynein actuation.

### Structural incompatibility and torsion with alternating sign

Alongside the previous analysis, there is a less technical way to infer the emergence of non-planarity from our model. We look here more closely to the flagellum energy, and we think in terms of structural incompatibility between Ax and PFR, seen as antagonistic elements of the flagellum assembly, see Figure 5.

Under the assumptions Equation 22 and Equation 24, the flagellar energy is given by

$$
𝒲=𝒲^{a}+𝒲^{p},where𝒲^{a}=\frac{1}{2}\int_{0}^{L}B^{a}‖U−(0U_{2}^{∗})‖^{2}−B^{a}U_{2}^{∗}^{2}and𝒲^{p}=D^{p}(\int_{0}^{s}e_{p}⋅U)^{2},
$$

with $U_{2}^{*}$ as in Equation 23. The energy has two components, $𝒲^{a}$ that depends on the Ax bending modulus $B^{a}$, and $𝒲^{p}$ that depends on the PFR shear modulus $D^{p}$. We can vary these material parameters and explore what the resulting minima of $𝒲$, that is, the equilibrium configurations (Equations 12-13), must look like. We consider the nondimensional parameter $ν=D^{p}/(B^{a}⁢L^{-2})$. When $ν≪1$ the Ax component $𝒲^{a}$ of the energy dominates. In this case, at equilibrium, the bending vector has to be close to the target bending vector $𝐔≈(0,U_{2}^{*})$. In particular, then, $𝐔⁢(s)$ will be confined near the line $U_{1}=0$ for every $s$. In the case $ν≫1$ the PFR component $𝒲^{p}$ dominates, and the energy is minimized when $𝐔⁢(s)$ lies close to the line generated by the vector $𝐞_{p}^{⊥}=(-sin⁡ϕ_{p},cos⁡ϕ_{p})$. Clearly, if the latter line is different from $U_{1}=0$, the two extreme regimes $ν≪1$ and $ν≫1$, each of which favours one of the two individual components, aim at two different equilibrium configurations. In other words, Ax and PFR are structurally incompatible.

When neither of the two energy components dominates, the emergence of non-planarity can be intuitively predicted with the following reasoning. In the intermediate case of $ν∼1$, we expect the equilibrium configurations to be a compromise among the two extreme cases, with the bending vector $𝐔⁢(s)$ being ‘spread out’ in the region between the two extreme equilibrium lines. The spreading of the bending vector is aided by the concentrated shear force at the tip, which imposes $𝐔⁢(L)=(0,U_{2}^{*}⁢(L))$ irrespectively of the PFR stiffness. The bending vector is then ‘pinned’ at $s=L$ on the $U_{1}=0$ line while it gets dragged toward the line generated by $𝐞_{p}^{⊥}$ for large values of $ν$. Hence the spreading. The bending vector will then span an area and, consequently, undergo rotations. Since torsion is determined by the rotation rate of the bending vector ($\tau=\partial_{s}⁡ψ$), the resulting flagellar shapes will be non-planar.

Figure 6 illustrates a critical example in which the previous intuitive reasoning effectively plays out. We consider a target bending of the kind $U_{2}^{*}⁢(s)=A_{0}+A_{1}⁢sin⁡(2⁢\pi⁢s/L)$, a fair idealization of the asymmetric shapes of a Chlamydomonas-like flagellar beat (Geyer et al., 2016). We take $ϕ^{p}=-\pi/4$ (larger than the E. gracilis value, to obtain clearer graphs). For $ν=0$, the bending vector lies inside the $U_{1}=0$ line, and its amplitude oscillates. For positive values of $ν$, when the PFR stiffness is 'turned on’, the oscillating bending vector is extruded from the $U_{1}=0$ line. For large values of $ν$ it gets closer and closer to the line generated by $𝐞_{p}^{⊥}$. The bending vector spans an area and, following the oscillations, it rotates clock-wise and anti-clock-wise generating an alternation in the torsion sign. This is the geometric signature of the spinning lasso.

In Appendix 3, we relaxed the planar constraint (Equation 24), and considered different weakly non-planar spontaneous configurations, by perturbing Chlamydomonas-like target bending strains. Each configuration presents a different (non-null) torsional profile when the antagonistic mechanical interaction of the PFR is absent $ν=0$. For larger values of $ν$, each perturbation assumes the typical spinning lasso geometry (torsional peaks of alternate sign), regardless of the native ($ν=0$) torsional profile. This shows that the PFR-Ax interactions strongly influence the flagellar shape outcome even when the perfectly planar constraint on the spontaneous bending is relaxed.

### Hydrodynamic simulations and comparison with observations

Our model is able to predict the torsional characteristic of the euglenid flagellum in the static case, and in absence of external forces. We test here the model in the more realistic setting of time-dependent dynein actuation in the presence of hydrodynamic interactions.

We first observe that, as in the static case, the dynamic equations for $𝐔$ and $U_{3}$ are decoupled (Equations 17, 18), and that dynein forces do not affect twist. We have then twistless kinematics under any actuation also in the dynamic case, at least after a time transient. We can simply assume Equation 22 for all times, so the torsion of $𝐫^{a}$ is still completely determined by the bending vector.

We consider a dynein actuation that generates Chlamydomonas-like shapes in a flagellum with no extra-axonemal structures. The shear forces $H_{1}$ and $H^_{1}$ employed in our simulation are shown in Figure 7. The same figure also shows the emergent bending strains of a PFR-free flagellum actuated by said forces, beating in a viscous fluid. The dynamic equations for this system are simply Equations 17, 18 with $D^{p}=0$. The resulting bending strains, which generate a planar beat, resembles the experimentally observed Chlamydomonas flagellar curvatures reported in Qin et al., 2015.

![Figure 7.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig7-v1.jpg)

**Figure 7.:** (a-b) Dyneins’ shear forces. (c) Resulting bending strains and torsion for an Ax actuated by the force pattern (a–b), beating in a viscous fluid, and free of extra-axonemal structures. The beat is planar (Chlamydomonas-like). (d) Resulting bending strains and torsion for an euglenid flagellum (composite structure Ax+PFR) actuated by (a–b) and beating in a viscous fluid. The Ax-PFR interaction generates torsional peaks with alternate sign traveling from the proximal to the distal end of the flagellum. (e) Resulting shapes for the euglenid flagellum at different instants within a beat, and comparison with experimental observations.

Finally, Figure 7 presents the emergent bending strains of the beating euglenid (PFR-bearing) flagellum, together with the corresponding flagellar torsion. The spinning lasso torsional signature is clearly present. Indeed, the fluid-structure interaction does not disrupt the Ax-PFR structural incompatibility, which still generates non-planar shapes with traveling waves of torsional peaks with alternating sign and the typical looping-curve outlines, Figure 2. All the details on the methods and parameters employed in the simulations are given in Appendix 4. Video 2 shows a comparison between the simulated flagellar beat and the experimental observations.

![Video 2.](https://cdn.elifesciences.org/articles/58610/elife-58610-video2.mp4.jpg)

### Swimming simulations

The unique flagellar beat of E. gracilis is at the base of the distinctive behavior of the organism, producing the typical roto-translational trajectories of swimming cells. This has been demonstrated by swimming simulations using the experimentally measured flagellar shapes in Rossi et al., 2017 with a Resistive Force Theory approach to model hydrodynamic interactions between the cell and the surrounding fluid. Similar conclusions are reached with a Boundary Element Method for the computation of the fluid flows induced by the same measured history of the flagellar shapes, see Giuliani et al., 2021. We carried out here analogous simulations using the theoretical waveforms produced by our model.

The application of Resistive Force Theory hydrodynamics to the waveforms shown in Figure 7 produces swimming paths similar to the typical observed trajectories. Swimming cell simulations are reported in Figure 8, see also Video 3. The cell is propelled by the flagellum, following a generalized right-handed helical trajectory while rotating around its major axis. After each full turn of the helix the cell completes one full body rotation. For more details on the implementation and physics behind swimming simulation see Appendix 5.

![Figure 8.](https://cdn.elifesciences.org/articles/58610/elife-58610-fig8-v1.jpg)

**Figure 8.:** (a) Side view and (b) top view of swimming cell simulation resulting from the flagellar beat generated by our model. The dimension of the cell body is not to scale with displacements for visualization purposes.

![Video 3.](https://cdn.elifesciences.org/articles/58610/elife-58610-video3.mp4.jpg)

## Discussion and outlook

We have shown how the origin of the peculiar shapes of the euglenid flagellum can be explained by the mechanical interplay of two antagonistic flagellar components, the Ax and the PFR. Our conclusions are based mainly on the hypothesis that sliding inhibition by the PFR organizes dynein activity, and localizes the spontaneous bending plane of the Ax as the one that passes from the Ax center through the MTs bonded to the PFR. This is in agreement with the current understanding of the mechanism that generates beat planarity in other PFR-bearing flagellar systems. Non-planarity in E. gracilis can arise because of a marked asymmetry in the Ax-bonding links-PFR complex in the euglenid flagellum, which is not found in kinetoplastids such as Leishmania (Gluenz et al., 2010) or Trypanosoma (Portman and Gull, 2010).

In the absence of a precise knowledge of the dynein actuation pattern, we tested our mechanical model under shear forces that would, in the absence of extra-axonemal structures, realize a beat similar to those found in model systems like Chlamydomonas. We appreciate that the emergent distortion of the Ax, generated by the Ax-PFR interplay, could in principle lead to different actuation patterns, consistently with the hypothesis of dynein actuation via mechanical feedback. Including dynein feedback in the euglenid flagellum model we proposed will require further study, and can potentially open new avenues for the study of ciliary motility in general. While the existence of a mechanical feedback between molecular motors and the flagellar scaffold is fairly accepted, there are several competing theories arguing in favour of different feedback mechanisms. The structural and kinematic peculiarities of the E. gracilis beat may provide a challenging new model system to test the relative merits of these alternative theories.

Along with the mechanism that let the euglenid flagellar shapes emerge, it is worth considering how this characteristic flagellar beat is integrated in the overall behavior of the organism. The spinning lasso produces the typical roto-translational motion of E. gracilis cells. Cell body rotation is in turn associated with phototaxis. Indeed, rotation allows cells to veer to the light source direction when stimulated, or escape in the opposite direction, when the signal is too strong. Here, the key biochemical mechanism could be the one often found in nature, by which periodic signals generated by lighting and shading associated with body rotations are used for navigation, in the sense that the existence of periodicity implies a lack of proper alignment (Goldstein, 2015). It is known that the PFR is directly connected with the light-sensing apparatus (Rosati et al., 1991), and might even be contractile (Piccinni, 1975). Transient light stimuli have been shown to change flagellar beat patterns. While the euglenid flagellum consistently present looping outlines (the 2d trace of a torsion dipole), its extension from the cell body changes with changing light intensity signals, resulting in a variety of 'quantized’ phototaxis behaviors (Tsang et al., 2018). With suitable modifications, our model could provide a starting point to address the (possible) mechanisms of active contraction of the PFR, light perception, and their interplay. Further study on euglenid flagellar motility and phototaxis could lead to a more comprehensive understanding of the biomechanical role of PFR, both in phototaxis and in general.

The very basic question of 'why' euglenids have evolved a structure such as PFR is an interesting challenge, but beyond the scope of the model we have developed in this paper. Our results confirm, however, the interest of euglenids as model systems for responsive unicellular organisms: E. gracilis, in particular, is a unicellular organism exhibiting a variety of motility behaviors (flagellar swimming and metaboly, see Leander et al., 2017) and capable of responding to a variety of stimuli, from light to confinement, see Noselli et al., 2019.

## Materials and methods

Strain SAG 1224-5/27 of Euglena gracilis obtained from the SAG Culture Collection of Algae at the University of Göttingen was maintained axenic in liquid culture medium Eg. Cultures were transferred weekly. Cells were kept in an incubator at 15°C at a light:dark cycle of 12 hr under a cold white LED illumination with an irradiance of about $50⁢\mu⁢mol⋅m^{-2}⋅s^{-1}$.

An Olympus IX 81 inverted microscope with motorized stage was employed in all the experiments. These were performed at the Sensing and Moving Bioinspired Artifacts Laboratory of SISSA. The microscope was equipped with a LCAch 20X Phc objective (NA 0.40) for the imaging of cells trapped at the tip of a glass capillary using transmitted brightfield illumination. The intermediate magnification changer (1.6 X) of the microscope was exploited to achieve higher magnification. Micrographs were recorded at a frame rate of $1,000⁢fps$ with a Photron FASTCAM Mini UX100 high-speed digital camera.

Tapered capillaries of circular cross section were obtained from borosilicate glass tubes by employing a micropipette puller and subsequently fire polished. At each trial, observation a glass capillary was filled with a diluted solution of cells and fixed to the microscope stage by means of a custom made, 3d-printed holder. The holder allowed for keeping the capillary in place and rotating it about its axis, so as to image a cell specimen from distinct viewpoints. Cells were immobilized at the tip of the capillary by applying a gentle suction pressure via a syringe connected to the capillary by plastic tubing. Occasionally, large body deformations of the cells were observed, a behavior commonly known as ‘metaboly’ which E. gracilis often manifest under confinement. The observations reported in this paper are restricted to specimens with immotile cell bodies, that is, in absence of metaboly. This choice allows for a clear capture of the flagellar beat. The absence of metaboly also suggests minimal impact on cell behavior in response to capillary entrapment.
