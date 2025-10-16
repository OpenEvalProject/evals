# Active contraction of microtubule networks

## Authors

- Peter J Foster<sup>1</sup> ([ORCID: 0000-0003-1818-5886](https://orcid.org/0000-0003-1818-5886)) †
- Sebastian Fürthauer<sup>2</sup>
- Michael J Shelley<sup>2</sup>
- Daniel J Needleman<sup>1</sup>

### Affiliations

1. John A. Paulson School of Engineering and Applied Sciences, FAS Center for Systems Biology Harvard University Cambridge United States
2. Courant Institute of Mathematical Science New York University New York United States
3. Department of Molecular and Cellular Biology Harvard University Cambridge United States

† Corresponding author

## Abstract

10.7554/eLife.10837.001 Many cellular processes are driven by cytoskeletal assemblies. It remains unclear how cytoskeletal filaments and motor proteins organize into cellular scale structures and how molecular properties of cytoskeletal components affect the large-scale behaviors of these systems. Here, we investigate the self-organization of stabilized microtubules in Xenopus oocyte extracts and find that they can form macroscopic networks that spontaneously contract. We propose that these contractions are driven by the clustering of microtubule minus ends by dynein. Based on this idea, we construct an active fluid theory of network contractions, which predicts a dependence of the timescale of contraction on initial network geometry, a development of density inhomogeneities during contraction, a constant final network density, and a strong influence of dynein inhibition on the rate of contraction, all in quantitative agreement with experiments. These results demonstrate that the motor-driven clustering of filament ends is a generic mechanism leading to contraction. DOI: http://dx.doi.org/10.7554/eLife.10837.001

## Introduction

The mechanics, motions, and internal organization of eukaryotic cells are largely determined by the cytoskeleton. The cytoskeleton consists of filaments, such as actin and microtubules, and molecular motors, which consume chemical energy to exert forces on and arrange the filaments into large-scale networks. Motor proteins, including dynein and roughly 14 different families of kinesin (Wordeman, 2010), organize microtubules to form the spindle, which segregates chromosomes during cell division. The motor protein myosin organizes actin filaments into networks which drive cell motility, polarity, cytokinesis, and left-right symmetry breakage (Mitchinson and Cramer, 1996; Mayer et al., 2010; Naganathan et al., 2014). The non-equilibrium nature of motor activity is essential for the organization of the cytoskeleton into these diverse sub-cellular structures, but it remains unclear how the interactions between filaments, different motor proteins, and other biomolecules influence the behaviors of the networks they form. In particular, it is difficult to extrapolate from the biochemical properties of motors characterized in reconstituted systems to the biological function of those motors in vivo. To address this question, we study self-organization of cytoskeletal filaments in Xenopus extracts, which recapitulate the biochemical complexity of the in vivo system.

The self-organization of cytoskeletal filaments has been extensively studied in cell extracts and in reconstituted systems of purified components. Actin can form macroscopic networks that exhibit a myosin-dependent bulk contraction (Murrell and Gardel, 2012; Bendix et al., 2008; Köhler and Bausch, 2012; Alvarado et al., 2013; Szent-Györgyi, 1943). Microtubule networks purified from neuronal extracts have also been observed to undergo bulk contraction (Weisenberg and Cianci, 1984), while microtubules in mitotic and meiotic extracts are found to assemble into asters (Gaglio et al., 1995; Mountain et al., 1999; Verde et al., 1991). Aster formation in meiotic Xenopus egg extracts is dynein-dependent, and has been proposed to be driven by the clustering of microtubule minus ends by dynein (Verde et al., 1991). It has also been suggested that dynein binds to the minus ends of microtubules in spindles and clusters the minus ends of microtubules to form spindle poles (Heald et al., 1996; Burbank et al., 2007; Khodjakov et al., 2003; Goshima et al., 2005; Elting et al., 2014) and dynein has been shown to accumulate on microtubule minus ends in a purified system (McKenney et al., 2014). Purified solutions of microtubules and kinesin can also form asters (Nédélec et al., 1997; Hentrich and Surrey, 2010; Urrutia et al., 1991), or under other conditions, dynamic liquid crystalline networks (Sanchez et al., 2012). Hydrodynamic theories have been proposed to describe the behaviors of cytoskeletal networks on length scales that are much greater than the size of individual filaments and motor proteins (Prost et al., 2015, Marchetti et al., 2013). These phenomenological theories are based on symmetries and general principles of non-equilibrium physics, with the details of the microscopic process captured by a small number of effective parameters. As hydrodynamic theories are formulated at the continuum level, they cannot be used to derive the values of their associated parameters, which must be obtained from more microscopic theories (Prost et al., 2015, Marchetti et al., 2013) or by comparison to experiments (Mayer et al., 2010; Brugués and Needleman, 2014).

A key feature of networks of cytoskeletal filaments and motor proteins that enters hydrodynamic theories, and differentiates these non-equilibrium systems from passive polymer networks, is the presence of additional, active stresses (Prost et al., 2015, Marchetti et al., 2013). These active stresses can be contractile or extensile, with profound implications for the large-scale behavior of cytoskeletal networks. Contractile stresses can result from a preferred association of motors with filament ends (Kruse and Jülicher, 2000; Hyman and Karsenti, 1996), nonlinear elasticity of the network (Liverpool et al., 2009), or the buckling of individual filaments (Murrell and Gardel, 2012; Lenz, 2014; Soares e Silva et al., 2011). Extensile active stresses can arise from polarity sorting or result from the mechanical properties of individual molecular motors (Gao et al., 2015; Blackwell et al. 2015). In networks with dynamically growing and shrinking filaments, polymerization dynamics can also contribute to the active stress. Experimentally, acto-myosin systems (Murrell and Gardel, 2012; Bendix et al., 2008; Köhler and Bausch, 2012; Alvarado et al., 2013; Szent-Györgyi, 1943) and microtubule networks from neuronal extracts (Weisenberg and Cianci, 1984) are observed to be contractile, while purified solutions of microtubules and kinesin can form extensile liquid crystalline networks (Sanchez et al., 2012). It is unclear which microscopic properties of filaments and motor proteins dictate if the active stress is contractile or extensile in these different systems.

Here, we investigate the motor-driven self-organization of stabilized microtubules in Xenopus meiotic egg extracts. These extracts are nearly undiluted cytoplasm and recapitulate a range of cell biological processes, including spindle assembly and chromosome segregation (Hannak and Heald, 2006). We have discovered that, in addition to microtubules forming asters in this system as previously reported (Verde et al., 1991), the asters assemble themselves into a macroscopic network that undergoes a bulk contraction. We quantitatively characterized these contractions and found that their detailed behavior can be well understood using a simple coarse-grained model of a microtubule network in which dynein drives the clustering of microtubule minus ends. This end clustering mechanism leads to a novel form of active stress, which drives the system to a preferred microtubule density. Our results suggest that the dynein-driven clustering of microtubule minus ends causes both aster formation and network contraction, and have strong implications for understanding the role of dynein in spindle assembly and pole formation. Furthermore, the close agreement we find between experiments and theory demonstrates that simple continuum models can accurately describe the behavior of the cytoskeleton, even in complex biological systems.

## Results

To further study the motor-induced organization of microtubules, we added 2.5

![Figure 1.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig1-v2.jpg)

**Figure 1.:** Xenopus egg extracts.(A) Experiments were performed in thin rectangular channels of width , height W0, and length H0. (L0B) In some regions of the channel, microtubules organize into asters, with minus ends localized in the aster core (Scale bar, m). (5 μC) Isolated asters fuse together over minute timescales (Scale bar, m). (5 μD) Aster-like structures form in other regions of the channel (Scale bar, m) (10 μE) Aster-like structures show large scale movement on minute timescales. (Scale bar, m). (25 μF) NUMA localizes to the network interior (Scale bar, m). (20 μG) Closeup of aster-like structure showing NUMA localized on the interior (Scale bar, m).10 μDOI: http://dx.doi.org/10.7554/eLife.10837.003

To characterize these large-scale motions, we next imaged networks at lower magnification, obtaining a field of view spanning the entire channel width. The networks, which initially filled the entire channel (width W0 = 1.4 mm), underwent a strong contraction, which was uniform along the length of the channel (Figure 2A, Video 3). The contractile behavior of these microtubule networks is highly reminiscent of the contractions of actin networks in these extracts (Bendix et al., 2008), but in our experiments actin filaments are not present due to the addition of 10 μgmL Cytochalasin D. We characterized the dynamics of microtubule network contractions by measuring the width, W(t), of the network as a function of time (Figure 2B). Occasionally, we observed networks tearing along their length (Video 4), yet these tears seemed to have little impact on the contraction dynamics far from the tearing site, arguing that the Poisson ratio of the network is ≈ 0. We then calculated the fraction contracted of the network:

![Figure 2.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig2-v2.jpg)

**Figure 2.:** Xenopus egg extracts.(A) Low magnification imaging shows that microtubules form a contractile network (Scale bar, m). (500 μB) The width of the microtubule network decreases with time (n =  experiments). (Inset) Representative plot of 6(t) (Blue line) and fit from (ϵEquation 2) (Pink line), with , ϵ∞=0.81 min, τ=3.49 min.Tc=1.06DOI: http://dx.doi.org/10.7554/eLife.10837.006

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (t) from data in ϵFigure 1F (Blue lines) along with fits from (Equation 2) (Pink lines).DOI: http://dx.doi.org/10.7554/eLife.10837.007

The time course of ϵ(t) was found to be well fit by an exponential relaxation:

(2)ϵ(t)≃ϵ∞1-e-(t-Tc)τ,

where ϵ∞ is the final fraction contracted, τ is the characteristic time of contraction, and Tc is a lag time before contraction begins (Figure 2B, inset, Figure 2—figure supplement 1).

We next sought to investigate which processes determine the timescale of contraction and the extent that the network contracts. For this, we exploited the fact that different mechanisms predict different dependence of the timescale τ on the channel dimensions. For instance, in a viscoelastic Kelvin-Voight material driven to contract by a constant applied stress, τ = η/E depends solely on the viscosity η and the Young’s modulus E and is independent of the size of the channel (Oswald, 2009). In contrast, in a poroelastic material driven by a constant stress, τ ∝ W02 (Coussy, 2004), where W0 is the width of the channel. Thus, studying how τ varies with channel width provides a means to test the validity of these models.

We fabricated microfluidic channels of varying width,

![Figure 3.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig3-v2.jpg)

**Figure 3.:** (A) Microtubules form contractile networks in channels with various widths (Scale bar, 500 m, t=10 min). (μB) Width of the networks as a function of time in channels with various widths. (C) Fraction contracted as a function of time, (ϵt), calculated from the data in B. The networks all contract to a similar final fraction, while the timescale of contraction differs. (D) The scaling of the characteristic time, , with channel width does not vary as τ, as would result for a poroelastic timescale, and is not a constant, independent of width, as would result from a viscoelastic timescale. The scaling is well described by an active fluid model (green line analytic scaling, fit to (W02Equation 6); green dots numerical solution). (E) The characteristic time, , is found to be independent of channel height. The dashed line is the mean value of τ. (τF)  is constant for all channel widths and heights, indicating that the network contracts to a constant final density. The dashed line is the mean value of ϵ∞. All panels display mean ϵ∞ s.e.m. ± DOI: http://dx.doi.org/10.7554/eLife.10837.010

In all cases, the networks contracted to a similar final fraction, ϵ∞, of ≈ 0.77, irrespective of channel geometry (Figure 3F). Since the Taxol concentration was held constant, all experiments started with the same initial density of microtubules, regardless of the dimensions of the channel. Thus, all networks contracted to the same final density. By using fluorescence intensity as a proxy for tubulin concentration (see Materials and methods), we estimate the final concentration of tubulin in the network to be ρ0≈ 30 μM. Remarkably, this is comparable to the concentration of microtubules in reconstituted meiotic spindles in Xenopus extracts (Needleman et al., 2010), which is ≈ 60 μM. As neither the simple viscoelastic nor poroelastic models are consistent with these results, we sought to construct an alternative model of the contraction process. Since Taxol stabilizes microtubules in these experiments, the density of microtubules ρ is conserved throughout the contraction process, implying

(3)∂tρ=-∇→⋅(ρv→),

where v→ is the local velocity of the microtubule network. The velocity v→ is set by force balance. If the relevant timescales are long enough that the microtubule network can be considered to be purely viscous, and if the network’s motion results in drag, then the equation for force balance is

(4)η∇2v→-γv→=∇→⋅σ,

where η and γ are the viscosity and drag coefficients, respectively, and σ is an active stress caused by motor proteins which drive the contraction of the microtubule network. The observation that the timescale of contraction, τ, is independent of channel height (Figure 3E) shows that the drag does not significantly vary with channel height, and thus could arise from weak interactions between the microtubule network and the device wall.

We obtain an expression for the active stress,

![Figure 4.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig4-v2.jpg)

**Figure 4.:** (A) Microtubule sliding by dynein drives microtubule minus ends together. (B) Minus end clustering leads to the formation of aster-like structures. Due to steric interactions between microtubules, there is an upper limit to the local microtubule density. (C) The microtubule network is composed of interacting asters. Motor activity driving aster cores together leads to bulk contraction of the network.DOI: http://dx.doi.org/10.7554/eLife.10837.012

In an orientationally disordered suspension of microtubules, we expect dynein mediated collection of microtubule minus ends to drive a contractile stress which is proportional to the number of motor molecules m and the local density of microtubules ρ, (see Appendix).

As only a finite number of microtubules can fit near the core of an aster, steric collisions will counteract the contractile stress at high densities (Figure 4B).

Since most motion in the suspension is motor driven, thermal collisions can be ignored, and the extensile stress driven by steric interactions will be be proportional to the number of motor molecules m and quadratic in the local density of microtubules ρ (see Appendix).

Taken together, these two effects lead to the active stress

(5)σ=sρ(ρ-ρ0)𝕀,

where s is the strength of the active stress, ρ0 is the final density at which the effects of dynein mediated clustering and steric repulsion between microtubules balance, and 𝕀 is a unit tensor (see Appendix).

Importantly, since the contractile and extensile parts of the active stress both depend linearly on the number of motor molecules, the prefered density ρ0 that the suspension will reach after contraction depends only on the interaction geometry between microtubules and motors and not on the actual number of active motors. Only the strength s of the active stress will be affected if the number of active motors could be changed.

Taken together, Equations (3,4,5) constitute an active fluid theory of microtubule network contraction by minus end clustering. We note that this theory could be reformulated, essentially without change, as the clustering of aster cores, again driven by dynein mediated clustering of minus ends. Isotropy of interactions remains a fundamental assumption.

We first investigated if this active fluid theory can explain the dependence of the timescale of contraction on sample geometry. An analysis of the equations of motion, Equations (3,4,5), near equilibrium predicts that the timescale of contractions obeys

(6)τ(W0)=αηsρ02+βγsρ02W02,

where α = 2.2  ±  0.05 and β = 0.085  ±  0.006 are dimensionless constants, which we determined numerically (see Appendix). This predicted scaling is both consistent with the experimental data and simulations of the full theory (Figure 3D). Fitting the scaling relationship to the data allows combinations of the parameters to be determined, giving η∕(sρ02) = 0.82  ±  0.20 min and γ∕(sρ02) = 1.0 ×10-5±0.7×10-5 min∕(μm2) (mean  ±  standard error). Combining this measurement with an estimate for the network viscosity taken from measurements in spindles of η ≈ 2×102Pa⋅s (Shimamoto et al., 2011), we can estimate the dynein-generated active stress to be sρ02 ≈ 4Pa which is consistant with having ≈ 0.4 dynein per microtubule minus end each exerting an average force of 1 pN (Nicholas et al., 2015).

To further explore the validity of the active fluid theory of contraction by microtubule minus end clustering, we explored other testable predictions of the theory. This theory predicts that: (i) the preferred density of the network ρ0 is constant and does not depend on the initial conditions. This is consistent with the constant ϵ∞ measured experimentally (Figure 3F); (ii) since contractions are driven by stress gradients (Equation 4) and stress depends on microtubule density (Equation 5) the density discontinuity at the edge of the network should produce large-stress gradients, leading to an inhomogeneous density profile in the network during contraction; (iii) the magnitude of the active stress, s, is proportional to the number of active motors, but the final density of the network, ρ0, is independent of the number of molecular motors (see Appendix). Thus, reducing the number of motors should lead to slower contractions, but still yield the same final density.

We first examined prediction (ii), that the stress discontinuity at the edge of the network should lead to a material buildup in the film. To test this, we averaged the fluorescence intensity along the length of the channel (see Materials and Methods) and found that the microtubule density does indeed increase at the network’s edge during contraction (

![Figure 5.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig5-v2.jpg)

**Figure 5.:** (A) Time series of contraction showing intensity averaged along the length of the channel. The average intensity peaks at the network’s edges due to increased local microtubule density. (Scale bars, 500 m) (μB) Comparison of measured density profiles (solid lines) with density profiles from simulation (dashed lines). Data are plotted at 1 min intervals starting at t = 40 s. (C) Representative frame from PIV showing the network’s local velocity component along the network’s width. (D) Comparison between measured (solid red line) and simulated (dashed red line) velocity along the width of the channel at t = 80 s. The measured and simulated velocities increase superlinearly with distance from the center of the network, as can be seen by comparison to a linear velocity profile (dashed black line).DOI: http://dx.doi.org/10.7554/eLife.10837.013

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Data are plotted at 2 min intervals starting at t = 40 s.DOI: http://dx.doi.org/10.7554/eLife.10837.014

Finally, we sought to determine the molecular basis of the contraction process, and check prediction (iii), that the number of motors driving the contraction affects the rate of contraction, but not the final density the network contracts to. Aster assembly is dynein-dependent in

![Figure 6.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig6-v2.jpg)

**Figure 6.:** (A) Fraction contracted as a function of time, (t), when dynein is inhibited using p150-CC1. (ϵB) The characteristic time of contraction, , increases with increasing p150-CC1 concentration. Solid green line indicates fit of sigmoid function. (τC)  has no apparent variation with p150-CC1 concentration. Solid green line indicates the mean value of ϵ∞. All panels display mean ϵ∞ s.e.m. ± DOI: http://dx.doi.org/10.7554/eLife.10837.015

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Comparison of (t) curves for samples where Kinesin-5 was inhibited using STLC and control where no STLC was added. (ϵB) Simultaneous inhibition of dynein with p150-CC1 and Kinesin-5 with STLC does not rescue the effects of dynein inhibition alone. All panels display mean  s.e.m. ± DOI: http://dx.doi.org/10.7554/eLife.10837.016

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/10837/elife-10837-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (t) from experiments with 2 ϵM p150-CC1 (blue lines) along with fits from μEquation (2) (pink lines).DOI: http://dx.doi.org/10.7554/eLife.10837.017

## Discussion

Here, we have shown that networks of stabilized microtubules in Xenopus egg extracts undergo a bulk contraction. By systematically varying the width of the microfluidic channel in which the network forms, we demonstrated that the timescale of contraction is not a poroelastic or viscoelastic timescale. A simple active fluid model of network contraction by dynein-driven clustering of microtubule minus ends correctly predicts the dependence of the contraction timescale on channel width, the nonuniform density profile in the network during contraction, and that inhibiting dynein affects the timescale of contraction but not the final density that the network contracts to. Parameters of this model can be measured by the scaling of the contraction timescale with channel width and by a detailed analysis of the inhomogeneities in the network that develop during contraction. Both methods give similar values.

Our results demonstrate that the behaviors of a complex biological system can be quantitatively described by a simple active matter continuum theory. These active matter theories aim to describe the behavior of cytoskeletal systems at large-length scales and long-timescales by effectively averaging all of the molecular complexity into a small set of coarse-grained parameters. Previously, these theories have been predominately applied to describe biological systems near non-equilibrium steady states (Prost et al., 2015; Brugués et al., 2014). In the present work, we augment previous theories with a nonlinear active stress term derived from microscopic considerations to capture the far from steady state dynamics of the contraction process. This approach allows us to quantitatively explain our experimental results using a theory with only four parameters, while a complete microscopic model would require understanding the behavior of the thousands of different proteins present in Xenopus egg extracts. Furthermore, the considerations of the model are general, and it will be interesting to consider whether the end clustering mechanism proposed here could contribute to contraction in actin networks as well.

In our model, the active stress which drives network contraction results from the motor-induced clustering of microtubule minus ends, the same process thought to be responsible for aster formation and spindle pole focusing (Gaglio et al., 1995; Mountain et al., 1999; Verde et al., 1991, Elting et al., 2014; Heald et al., 1996; Burbank et al., 2007; Khodjakov et al., 2003; Goshima et al., 2005). Our results, and previous data (Verde et al., 1991; Heald et al., 1996; Burbank et al., 2007), are consistent with minus end clustering in Xenopus egg extracts primarily arising from the activity of dynein. The ability of dynein to cluster microtubule minus ends could result from dynein being able to accumulate on the minus end of one microtubule, while simultaneously walking towards the minus end of another (Hyman and Karsenti, 1996; McKenney et al. 2014; Figure 4A). There is indication that such behaviors may indeed occur in spindles (Elting et al., 2014), and pursuing a better understanding of those processes is an exciting future direction that will help to clarify the function of dynein in spindles.

The observation that microtubule networks contract in Xenopus egg extracts suggests that motor-induced stresses in spindles are net contractile and not extensile as previously assumed (Brugués and Needleman, 2014). The contribution of dynein to spindle pole focusing may ultimately be due to these contractile stresses. The presence of contractile stresses from dynein might also explain both the observation that the fusion of spindles is dynein-dependent (Gatlin et al., 2009), and the apparently greater cohesion between microtubules at spindle poles, (where dynein is localized [Gatlin et al., 2010]). It is unclear what processes set the density of microtubules in the spindle, and the finding that the active stress generated from minus end clustering saturates at a preferred microtubule density could play an important role.

## Materials and methods

## Preparation of Xenopus extracts

CSF-arrested extracts were prepared from Xenopus llaevis oocytes as previously described (Hannak and Heald, 2006). Crude extracts were sequentially filtered through 2.0, 1.2, and 0.2 micron filters, frozen in liquid nitrogen, and stored at −80°C until use.

## Preparation of microfluidic devices

Channel negatives were designed using AutoCAD 360 (Autodesk) and Silhouette Studio (Silhouette America) software, cut from 125-micron-thick tape (3M Scotchcal, St. Paul, MN) using a Silhouette Cameo die cutter, and a master was made by adhering channel negatives to the bottom of a petri dish. PDMS (Sylgard 184, Dow Corning, Midland, MI; 10:1 mixing ratio) was cast onto the masters and cured overnight at 60°C. Devices and coverslips were each corona treated with air plasma for 1 min before bonding. Channels containing a degassed solution of 5 mg/mL BSA (J.T. Baker, Center Valley, PA) supplemented with 2.5% w/w Pluronic F127 (Sigma, St. Louis, MO) were incubated overnight at 12°C. Unless stated otherwise, the microfluidic devices had a length of 18 mm, a height of 0.125 mm, and a width of 1.4 mm.

## Protein purification

GST-tagged p150-CC1 plasmid was a gift from Thomas Surrey (Uteng et al., 2008). GST-p150-CC1 was expressed in E. coli BL21 (DE3)-T1R(Sigma) for 4 hr at 37°C. The culture was shifted to 18°C for 1 hr before adding 0.2 mM IPTG and the culture was grown overnight at 18°C. Cells were centrifuged, resuspended in PBS supplemented with Halt Protease Inhibitor Cocktail (Thermo Scientific, Rockford, IL) and benzonase (Novagen, San Diego, CA) before lysis by sonication. GST-p150-CC1 was purified from clarified lysate using a GSTrap column FF (G.E. Healthcare, Sweden) as per the manufacturer’s instructions. GST-p150-CC1 was dialyzed overnight into 20 mM Tris-HCl, 150 mM KCl, and 1 mM DTT. The GST tag was cleaved using Prescission Protease (overnight incubation at 4°C). After removing free GST and Prescission Protease using a GSTrap FF column, p150-CC1 was concentrated, frozen in liquid nitrogen, and stored at -80°C until use.

## Bulk contraction assay

20 μL aliquots of filtered extract were supplemented with ∼1 μM Alexa-647 labeled tubulin and 2.5 μM Taxol before being loaded into channels. For dynein inhibition experiments, 1 μL of either p150-CC1 or buffer alone was added to the extract immediately before Taxol addition. For Kinesin-5 inhibition experiments, 100 μM STLC (Sigma Aldrich) was added concurrently with Taxol. Channels were sealed with vacuum grease and imaged using a spinning disk confocal microscope (Nikon Ti2000, Yokugawa CSU-X1), an EMCCD camera (Hamamatsu), and a 2x objective using Metamorph acquisition software (Molecular Devices). t=0 is defined when the imaging begins, ≈ 1 min after Taxol addition to the extract. After a brief lag time, the microtubule networks spontaneously begin contraction. Images were analyzed using ImageJ and custom build MATLAB and Python software (available at https://github.com/peterjfoster/eLife). Parameters were fit to contraction data using timepoints where ϵ(t)> 0.1.

## Final density estimation

The final density was estimated using contraction experiments with 2.5 μM Taxol in 0.9 mm channels. For each experiment, the frame closest to t = τ + Tc was isolated, where τ and Tc are the timescale of contraction and the offset time respectively, obtained from fits of the time course of contraction to Equation 2 of the main text. After correcting for the camera offset and inhomogeneous laser illumination, the average fluorescence intensity of the network, ρN and the average fluorescence intensity in the channel outside the network, ρM were calculated. The fluorescence intensity in the channel but outside the network comes from monomeric fluorescently labeled tubulin and was assumed to be constant throughout the channel. The fractional concentration was then estimated as ρ(τ+Tc)=ρN-ρMρN+ρM. Using this measurement along with the fit curves for ϵ(t) and under the assumption that the network contracts in the z direction such that ϵ(t) in the z direction is the same as along the width, the inferred fractional concentration at t = ∞ was calculated as

ρ(t=∞)=ρ(τ+Tc)(1-ϵ∞)2(1-ϵ∞(1-e-1))2

Assuming the fluorescently labeled tubulin incorporates into microtubules at the same rate as endogenous tubulin, we can multiply the derived fractional density ρ(t = ∞) by the tubulin concentration in extract, ≈18 μM (Parsons and Salmon, 1997) to arrive a final network tubulin concentration of ≈30 μM.

## Density profile measurements

Images from contraction experiments were corrected for the camera offset and inhomogeneous laser illumination before being thresholded in order to segment the microtubule network from background fluorescence. Rotations of the channel relative to the CCD were detected by fitting linear equations to edges of the microtubule network. If the average of the slopes from the top and bottom of the network was greater than 1/(the number of pixels in the length of the image), a rotated, interpolated frame was constructed where pixels were assigned based on the intensity of the pixel in the original frame weighted by their area fraction in the interpolated pixel. Frames were averaged along the length of the channel before background signal subtraction. For density profiles compared with simulations, the edge peaks of the density profile were identified and pixels between the two peaks were retained. Profiles were normalized such that the integral of the profile was set to 1.

## Particle imaging velocimetry

Particle Imaging Velocimetry was performed using PIVLab software (Thielicke and Stamhuis, 2014) using the FFT window deformation algorithm with a 16-pixel interrogation area and 8 pixel step for the first pass and an 8 pixel interrogation area with a 4-pixel step for the second pass. After PIV was performed, intensity images were thresholded to segment the microtubule network from the background, and only velocity vectors within the microtubule network that were > 8 pixels from the network’s edges were retained.
