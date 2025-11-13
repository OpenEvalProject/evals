# Myosin V executes steps of variable length via structurally constrained diffusion

## Authors

- David Hathcock<sup>1</sup> ([ORCID: 0000-0003-4551-9239](https://orcid.org/0000-0003-4551-9239)) †
- Riina Tehver<sup>2</sup> ([ORCID: 0000-0001-7406-3387](https://orcid.org/0000-0001-7406-3387))
- Michael Hinczewski<sup>3</sup> ([ORCID: 0000-0003-2837-7697](https://orcid.org/0000-0003-2837-7697)) †
- D Thirumalai<sup>4</sup>

### Affiliations

1. Department of Physics, Cornell University Ithaca United States
2. Department of Physics and Astronomy, Denison University Granville United States
3. Department of Physics, Case Western Reserve University Cleveland United States
4. Department of Chemistry, University of Texas Austin United States

† Corresponding author

## Abstract

The molecular motor myosin V transports cargo by stepping on actin filaments, executing a random diffusive search for actin binding sites at each step. A recent experiment suggests that the joint between the myosin lever arms may not rotate freely, as assumed in earlier studies, but instead has a preferred angle giving rise to structurally constrained diffusion. We address this controversy through comprehensive analytical and numerical modeling of myosin V diffusion and stepping. When the joint is constrained, our model reproduces the experimentally observed diffusion, allowing us to estimate bounds on the constraint energy. We also test the consistency between the constrained diffusion model and previous measurements of step size distributions and the load dependence of various observable quantities. The theory lets us address the biological significance of the constrained joint and provides testable predictions of new myosin behaviors, including the stomp distribution and the run length under off-axis force.

## Introduction

Molecular motors are cellular machines that function by converting chemical energy into mechanical work (Schliwa and Woehlke, 2003). Motors play key roles in many intracellular biological processes, including signaling and the transport of cargo (Sun and Goldman, 2011). Members of the myosin superfamily, one class of molecular motors, perform these functions by binding to actin filaments and generating energy through ATP hydrolysis. Myosin V, a dimeric transport motor, is composed of two stiff polymer chains joined at a pivot with an actin-binding head at the end of each chain (Reck-Peterson et al., 2000). The motor walks forward along the actin, stepping hand-over-hand, by alternating head detachment, with the free head performing a diffusive search for actin binding sites during each step (Shiroguchi and Kinosita, 2007). Such unidirectional motility requires coordination between the two heads with preferential detachment of the rear head, the so called ‘gating’ mechanism, which is regulated by the strain within the lever arms while the heads are bound to actin (Veigel et al., 2002; Veigel et al., 2005; Purcell et al., 2005; Sakamoto et al., 2008). Myosin V propels itself toward the plus (barbed) end of the actin using two changes in the lever arm orientation. The power stroke, executed by an actin-bound head, swings the lever arm forward, while the recovery stroke, executed during diffusion, returns the lever to its original orientation, which favors binding to forward actin sites (Shiroguchi et al., 2011). Most frequently, myosin V takes ≈ 74 nm steps, roughly equal in length to the actin helical pitch, but shorter and longer steps also occur (Yildiz et al., 2003). The near correspondence of the step size with the pitch, as well as the narrow step distribution, allows myosin V to approximately maintain its azimuthal orientation with respect to the actin over multiple steps (Sun and Goldman, 2011). Mutant myosins with altered lever arms show a linear relation between mean step size and arm length (Sakamoto et al., 2005; Oke et al., 2010). Under moderate backward force myosin V remains highly processive, up to a stall force ≈ 1.9 - 3 pN, (Mehta et al., 1999; Veigel et al., 2002; Kad et al., 2008; Uemura et al., 2004; Cappello et al., 2007; Gebhardt et al., 2006), at which the mean velocity of the motor goes to zero.

While myosin V is one of the most extensively studied motors, new functional features continue to be discovered as the spatiotemporal resolution of experimental imaging improves. Most recently Andrecka et al. (2015) achieved simultaneous millisecond temporal and nanometer spatial resolution with interferometric scattering microscopy in which the position of the gold nanoparticle attached to one of the motor heads was used to track the diffusion of the free head during its step. This measurement and recent electron micrographs of freely floating myosin taken by Takagi et al. (2014) indicate that the joint between the myosin V lever arms does not rotate freely, but instead has structural constraints giving rise to a preferred inter-arm joint angle. The presence of a joint constraint seems to contradict previous diffusion measurements by Dunn and Spudich (2007) and other experiments (Shiroguchi and Kinosita, 2007; Fujita et al., 2012; Beausang et al., 2013) which indicated a freely rotating joint. Further, a number of theoretical and numerical studies based on free diffusion models have been remarkably successful in quantitatively describing various aspects of myosin V motility (Hinczewski et al., 2013; Craig and Linke, 2009; Mukherjee et al., 2017).

To address these apparent conflicts, we extend a minimal model of myosin V previously introduced by Hinczewski et al. (2013), incorporating a constraint on the relative orientation of the two lever arms. The model combines a coarse-grained polymeric description of the diffusive search (Thirumalai and Ha, 1998) with the reaction network of discrete states taken by the motor heads during the mechanochemical stepping cycle (Vilfan, 2005a; Bierbaum and Lipowsky, 2011; Sumi, 2017). The large persistence length of the myosin V lever arms allows us to derive an approximate but accurate semi-analytical expression for the equilibrium distribution of positions occupied by the free head during the diffusive search. The kinetic network accounts for not only forward steps, but also foot stomps (the head reattaching near the site of detachment) and backward steps which have been observed experimentally (Kodera et al., 2010) and become more prominent as the resistive force increases. In contrast to the simplified model of Hinczewski et al. (2013), here we include the full set of available binding sites on the double-helical actin filaments, enabling a description of the distributions of steps and stomps taken by myosin V. The backward force applied by the load induces conformational changes in the lever arms, altering the diffusive search for binding sites and the associated binding probabilities. The effects of the magnitude of the resistive force and direction are easily incorporated into the theory. We supplement the analytical theory with Brownian dynamics (BD) simulations of myosin stepping dynamics, the results of which largely concur with analytical predictions. In addition to addressing the constrained diffusion hypothesis, our model provides the most comprehensive accounting to date of the full range of sub-stall experimental data, including step-size distributions and the load dependence of several physical observables.

The polymer model gives direct insights into the connection between structural features of myosin V, including the inter-arm joint constraint, and both the diffusive search and kinetics of the motor. With a joint constraint, our model predicts diffusion profiles similar to that observed by Andrecka et al. (2015). By computing the changes in diffusion as the constraint strength is varied, we estimate upper and lower bounds on the constraint energy. Fitting the model to experimental measurements of myosin V step distributions (Yildiz et al., 2003; Sakamoto et al., 2005; Oke et al., 2010) and the force dependence of the backward-to-forward step ratio (Kad et al., 2008) and mean run length/velocity (Mehta et al., 1999; Uemura et al., 2004; Clemen et al., 2005; Gebhardt et al., 2006; Kad et al., 2008), we confirm the consistency of the constrained diffusion picture with previous experimental data on myosin V. Interestingly, while the joint constraint considerably alters the diffusive search space, it has relatively small influence on the myosin V step size and force response. A free diffusion model, for instance, produces similar kinetic behaviors. Our model allows us to address questions related to the biological significance of the joint constraint. We find, for example, that the constraint does not necessarily speed up the binding time, despite narrowing the space of the diffusive search. However it does narrow the width of the forward step distributions on actin, allowing the head to more consistently target the actin binding sites at half-helical length intervals. Finally, the model provides testable predictions of new quantities yet to be probed by experiments, including the stomp distribution near the stall regime and the robust run length under off-axis forces.

## Results

### Theoretical model for myosin V dynamics

In the following sections we describe the main features of our polymer structural model for myosin V, the actin filament geometry, and how the model allows us to predict diffusion and stepping behavior, including the probabilities of various kinetic pathways. The full mathematical details of the analytical theory can be found in Appendix 1. The details of the BD simulations, which we used to validate the analytical theory results, are described in Appendix 2.

### Polymer model and actin filament geometry

Following Hinczewski et al. (2013), we model the actin-binding heads and lever arm domains of myosin V as semi-flexible polymer chains with length $L$ and persistence length $l_{p}$. We will denote each polymer chain as a ‘leg’ of the motor (consisting of the combined head and lever arm domains), and refer to trailing or leading legs depending on whether a given leg is further away from or closer to the barbed (plus) end of actin, respectively. Several experiments measuring myosin step distributions and other properties have been carried out comparing wild-type myosin V to mutants where the lever arm length is altered through addition or deletion of IQ motifs (Yildiz et al., 2003; Sakamoto et al., 2005; Oke et al., 2010). We assume the actin-binding head and IQ motifs are each approximately 5 nm in length, so that wild-type myosin V (with 6IQ motifs) has $L=35nm$ nm and the 4IQ and 8IQ mutants have $L=25nm$ nm and $L=45nm$ nm respectively. The persistence length has estimated values ranging from $l_{p}≈100nm$ nm (Howard and Spudich, 1996) to $l_{p}≈375nm$ nm (Vilfan, 2005a). While fitting our model to experimental data we allow the persistence length to vary within this range, though the model predictions are qualitatively similar for any $l_{p}≫L$ in the stiff leg regime.

The two polymer legs are connected at a joint forming the myosin V dimer (see Figure 1 for an illustration of the geometry). Recent experimental evidence suggests this this joint does not not rotate freely, but instead has a preferred joint angle $\theta_{p}$ giving rise to constrained diffusion (Takagi et al., 2014; Andrecka et al., 2015). In our model, this preferred angle is enforced by a potential $ℋ_{J}=\mu_{c}⁢k_{B}⁢T⁢[1-cos⁡(\theta_{J}-\theta_{p})]$, which is minimum when the inter-leg angle at the joint $\theta_{J}$ is equal to the preferred angle. The parameter $\mu_{c}$ is the constraint strength, designating the energy cost to deviations from $\theta_{p}$, while $k_{B}$ is Boltzmann’s constant and T is temperature. Note that for small angle differences $\theta_{J}-\theta_{p}$, the constraint potential $ℋ_{J}≈\frac{1}{2}⁢\mu_{c}⁢k_{B}⁢T⁢(\theta_{J}-\theta_{p})^{2}$ is approximately harmonic. In the limit $\mu_{c}→0$ the joint becomes freely rotating with no preferred angle, the case considered previously Hinczewski et al. (2013). This cosine potential is used throughout the paper, but below we briefly discuss how the form of the inter-leg potential affects the diffusion of the free head. The tail domain, which attaches to cargo, transmits a load force $𝐅$ to the joint. The direction of the force is parameterized by $\theta_{F}$, measured clockwise from the $-𝐳^$ axis, and $ϕ_{F}$, measured counterclockwise from the $𝐱^$ axis. Our main focus is on the behavior of myosin V under zero force and backward force ($\theta_{F}=ϕ_{F}=0$), but we also consider off-axis forces at the end of the Results section.

![Figure 1.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig1-v2.jpg)

**Figure 1.:** (A) Side view, with the actin filament plus end oriented toward the $𝐳^$ direction. Small circles on the actin monomers denote the binding sites $𝐫_{n}$, described by Equation 1. The site $n=0$ corresponds to the position of the bound head. The bound polymer leg has a preferred post-power stroke direction in the $x-z$ plane defined by a constraint angle $\theta_{c}$ relative to the $𝐳^$ axis. Due to the hypothesized structural constraint at the joint, the preferred angle between the lever arms is $\theta_{p}$. The force transmitted through the tail domain has a polar angle $\theta_{F}$ relative to the $-𝐳^$ direction. (B) Front view, with the actin plus end pointing out of the page. Each binding site has an associated outward pointing normal direction with azimuthal angle $ϕ_{n}$. As an example, one such angle is shown for the red-colored site. All azimuthal angles are measured counter-clockwise with respect to the $𝐱^$ direction. For binding to occur, the head has to be in the vicinity of the site, and oriented approximately along the normal. We approximately capture this condition by a binding criterion that requires the azimuthal angle of the free leg, $ϕ_{f}$, to be anti-parallel to $ϕ_{n}$ within a cutoff range $\pm\delta⁢ϕ_{ac}$, highlighted in light red. The load force may have an off-axis component with azimuthal angle $ϕ_{F}$.

The actin-binding heads, located at the ends of the polymer legs in our model, can bind to various sites along the double-helical filamentous actin structure. Actin is composed of two filaments each containing 13 actin subunits per helical rotation, with one binding site per subunit. The filaments run parallel to the $𝐳^$ axis, leading to a geometry in which the binding sites $𝐫_{n}$, $n=0,\pm1,\pm2,…$ have positions

$$
𝐫_{n}=R⁢(cos⁡ϕ_{n}-1)⁢𝐱^+R⁢sin⁡ϕ_{n}⁢𝐲^+(n/2)⁢Δ⁢z⁢𝐳^,
$$

where $R=5.5nm$ nm is the radius of the helix, $Δ⁢z=72/13≈5.5nm$ nm is the size of each actin subunit, and $ϕ_{n}=-12⁢\pi⁢n/13$ is the angle between adjacent subunits (Lan and Sun, 2006). Equation 1 and all the other key analytical quantities in our theory are summarized in Table 1 for ease of reference. Even and odd $n$ respectively correspond to subunits on the 1st and 2nd filaments of the double helix. Wild-type myosin V steps most frequently to the half-helical sites $n=\pm13$ located at $z=\pm36nm$ nm, while mutants favor other sites depending on their lever arm length (Sakamoto et al., 2005; Oke et al., 2010).

**Table 1.**
 Summary of main analytical results.


<table>
  <thead>
    <tr>
      <th>Quantity</th>
      <th>Meaning</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>𝐫n</td>
      <td>position of actin subunits</td>
      <td>Equation 1</td>
    </tr>
    <tr>
      <td>tfpn</td>
      <td>first passage time to subunit n</td>
      <td>Equation 3</td>
    </tr>
    <tr>
      <td>𝒫⁢(𝐫)</td>
      <td>equilibrium distribution of the free head position</td>
      <td>following Equation 3</td>
    </tr>
    <tr>
      <td>𝒫Tn</td>
      <td>binding probabilities for trailing leg</td>
      <td>Equation 4</td>
    </tr>
    <tr>
      <td>𝒫Ln</td>
      <td>binding probabilities for leading leg</td>
      <td>following Equation 4</td>
    </tr>
    <tr>
      <td>𝒫distn</td>
      <td>distribution of head-to-head distances</td>
      <td>Equation 5</td>
    </tr>
    <tr>
      <td>𝒫T⁢(zn)</td>
      <td>convolved trailing leg step distribution</td>
      <td>following Equation 5</td>
    </tr>
    <tr>
      <td>𝒫L⁢(zn)</td>
      <td>convolved leading leg step distribution</td>
      <td>preceding Equation 6</td>
    </tr>
    <tr>
      <td>𝒫⁢(zn)</td>
      <td>full convolved step distribution</td>
      <td>Equation 6</td>
    </tr>
    <tr>
      <td>μ^c′</td>
      <td>constraint direction (under force)</td>
      <td>Equation 7</td>
    </tr>
    <tr>
      <td>𝒯′</td>
      <td>power stroke effectiveness (under force)</td>
      <td>Equation 7</td>
    </tr>
    <tr>
      <td>𝒫b/𝒫f</td>
      <td>backward-to-backward step ratio</td>
      <td>Step ratio section</td>
    </tr>
    <tr>
      <td>zrun</td>
      <td>mean run length</td>
      <td>Equation 10</td>
    </tr>
    <tr>
      <td>vrun</td>
      <td>mean run velocity</td>
      <td>preceding Equation 11</td>
    </tr>
    <tr>
      <td>trun</td>
      <td>mean run time</td>
      <td>Equation 11</td>
    </tr>
  </tbody>
</table>

When myosin V is bound to an actin filament, the lever arm can be in two orientations. After the leg has bound, but before the power stroke has been executed, the lever arm points toward the pointed (minus) end of the actin. After the power stroke, the leg rotates toward the barbed (plus) end of the actin and is held at an angle $\theta_{c}$ above the actin. Similar to the inter-leg constraint described above, in our model the preferred forward tilting angle is enacted through a harmonic potential, $ℋ_{c}=\frac{1}{2}⁢ν_{c}⁢k_{B}⁢T⁢(𝐮^_{0}-𝐮^_{c})^{2}$. The constraint has strength $ν_{c}$, the unit vector $𝐮^_{0}$ is the tangent to the bound leg at the binding point, and the unit vector $𝐮^_{c}$ defines the preferred direction, which lies in the $𝐱^-𝐳^$ plane at an angle $\theta_{c}$ from the $𝐳^$ axis. As we will see below, steps and stomps occur only when the bound leg is in the post-power stroke orientation. For the purposes of modeling these aspects of the dynamics we do not need to consider a separate constraint potential for diffusion while the bound leg has the pre-power stroke orientation.

Volume exclusion effects introduce another constraint on the orientation of the myosin legs during diffusion. For instance, the myosin heads are unlikely to be found in close proximity due to steric repulsion. Such exclusion interactions apply not only to the myosin heads, but also to the legs, which have to be brought close together in order to accommodate small head separations. Though these interactions can’t be explicitly included in the coarse-grained polymer model, we capture the effective repulsion between the myosin heads using the potential $ℋ_{V}=k_{B}⁢T⁢(d_{V}/r)^{6}$, where $r$ is the distance between the bound and free myosin heads and $d_{V}$ is the effective length scale of the repulsion. The magnitude of $d_{V}$ depends on the details of the interacting legs between the heads, in particular their length $L$L. Using BD simulations described below (which explicitly include all volume exclusion interactions between the myosin legs), we estimate $d_{V}≈$ 20, 27.5, and 35 nm for 4IQ, 6IQ, and 8IQ myosin respectively.

### Brownian Dynamics simulations

We also study the stepping dynamics of myosin V using BD simulations. In the simulations, myosin V is treated as two connected and interacting polymer chains. The Hamiltonian that prescribes the interactions and the resulting structural features like the persistence length, is outlined in Appendix 2. A BD trajectory begins with the trailing lever arm unbinding from actin (mimicking the effect of ATP binding). A power stroke moves the unbound head quickly forward, after which it executes a diffusive search until it finds an energetically favorable actin binding site. As in the analytical model, the actin binding sites are given by Equation 1. We trace the diffusive search and record the binding locations. The reported data is averaged over 200 randomized trajectories. The simulations allow us to include the finite sizes of the lever arms, the effect of the volume excluded by actin, and a glass cover-slip that is used in certain experimental setups. Additionally we can test different functional forms for the binding criterion and power stroke execution.

### Kinetic pathways

Myosin V can exhibit a wide range of behaviors, shown schematically in Figure 2, including steps and stomps involving each polymer leg. Before following a particular kinetic pathway, Myosin V starts in a waiting state where both legs are strongly bound to the actin and each head has an associated ADP molecule. Each leg is in the post-power stroke orientation, pointed toward the plus end of the actin, and the leading leg is bent backward under tension. The motor then goes through one of many kinetic pathways, which can be broken into the five categories described below.

![Figure 2.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig2-v2.jpg)

### Forward steps

The myosin sits in the waiting state until the ADP molecule unbinds from the trailing head, allowing an ATP molecule to take its place. With the bound ATP, the trailing leg is only weakly associated to the actin and therefore quickly detaches. We assume (except for modeling one run velocity experiment described below) that the ATP concentration is near saturation levels, so that ATP binding occurs rapidly. Then the detachment process occurs roughly at the rate of ADP dissociation $t_{d1}^{-1}=12s^{-1}$ s–﻿1, which has been measured experimentally (De La Cruz et al., 1999). Following detachment of the trailing leg, the leading leg, previously under tension, undergoes rapid diffusive relaxation: since the leading leg had been bent backwards, away from its preferred post-power stroke orientation, the leg relaxes toward the preferred orientation, thus leading to the entire system swinging forward toward the plus end of actin (Hinczewski et al., 2013; Dunn and Spudich, 2007). The timescale $t_{r}$ of this relaxation depends on the load, but is generally $≲$ 5 μs, based on both theoretical and numerical considerations Hinczewski et al. (2013). Over much longer timescales, the free leg diffusively searches until it reaches a binding site on the actin. If we let the bound leg be attached at the origin $𝐫=0$ then the available binding sites are located at $𝐫_{n}$ given by Equation 1, and forward steps occur when the free leg reaches a site with $n>0$, assuming the following additional binding criteria are also fulfilled.

Before the detached head can bind to actin, the ATP must hydrolyze, ATP → ADP + $P_{i}$, which has two primary functions. First, during hydrolysis the free head undergoes the recovery stroke, rotating the head into the pre-power stroke orientation, so that binding to forward sites along the actin is conformationally favorable. Second, the hydrolysis produces an ADP molecule, which is required for the head to strongly associate with actin and successfully bind. The ATP hydrolysis occurs at rate $t_{h}^{−1}$ = 750 s—1 (De La Cruz et al., 1999) and we assume the reverse reaction rate is negligible.

Once ATP hydrolysis is completed, the free head must diffuse close enough to the actin to appreciably interact and bind. We assume that binding occurs when the head is within a distance $a$ from an actin binding site. An upper bound for the capture radius $a$ is the Debye screening length, which under physiological conditions (KCL concentrations of 25 – 400 mM) is $\lambda_{D}≈1.9-0.5nm$ nm (Craig and Linke, 2009). On these length scales, the detached head can interact with the binding site and we expect near certain binding at slightly shorter distances. Below we find that for $a=0.4nm$ nm the model produces quantitative agreement with experimental data. Finally, in addition to requiring close proximity of the free head to an actin binding site, the detached myosin head must also be in the correct orientation for binding to occur (the full details of this binding criterion are described in the section ‘First Passage Times and the Binding Acceptance Region’ below.)

### Trailing leg stomps

This kinetic pathway starts identically to the forward steps described above, namely the trailing leg dissociation is followed by ATP binding and hydrolysis. In this case, however, the diffusive search finds a site $𝐫_{n}$ with $n<0$. Instead of executing a hand-over-hand step, the myosin stomps and the heads remain in the same relative order on the actin, with a comparably small change in the center of mass position of the myosin. As before, we assume the binding occurs once the head is within a distance $a$ from a binding site with the free leg in a sufficiently acceptable orientation.

The recovery stroke is executed during ATP hydrolysis and before binding, so that the pre-power stroke orientation of the head favors binding to forward sites. After a forward step, the lever arm points toward the minus end of the actin in a relaxed pre-power stroke state. To bind to sites behind the bound leg, however, the free lever arm must bend and point toward the plus end of the actin despite its pre-power stroke orientation with respect to the head. This unnatural configuration puts the free leg under additional strain, so that there is an energy barrier to binding at backward actin sites. We model this effective barrier by reducing the probability of binding when the free head reaches a radius $a$ of actin sites with $n<0$. Instead of binding with certainty, the myosin head binds with probability $b<1$, which we call the binding penalty. The reduced binding probability, a consequence of the recovery stroke, increases the relative probability that the myosin will step forward, contributing to the biased motion along the actin filament.

### Backward steps

The other possible kinetic pathways start with the leading head detaching from the actin, in contrast to the trailing head detachment which initiates forward steps and trailing leg stomps. After the power stroke, the leading lever arm is under considerable backward tension. This tension dramatically suppresses the release of ADP from the leading head by a factor of 50–70 (Kodera et al., 2010; Rosenfeld and Sweeney, 2004). Since these events are very rare, an alternative detachment pathway is dominant: the leading head dissociates from the actin but retains the associated ADP molecule (Kodera et al., 2010; Purcell et al., 2005). This detachment pathway occurs at a slower rate than trailing head detachment, $t_{d2}^{-1}=(g⁢t_{d1})^{-1}$, where $g>1$ is the gating ratio. Under backward force of ∼2 pN, single-headed myosin V has been observed to detach from actin at a rate of 1.5 s—1 (Purcell et al., 2005), while previous theoretical calculations using the above described polymer model estimate the backward force on the leading leg to be 2.7 pN (Hinczewski et al., 2013) when myosin V sits in the waiting state with both legs bound. We therefore use $t_{d2}^{-1}=1.5s^{-1}$ s—1, which corresponds to the gating ratio $g=8$.

Once the leading head unbinds from the actin, it executes a diffusive search until it reaches an actin binding site. Note that the bound leg is in the post-power stroke state, so the diffusion is statistically identical to that which occurs during forward steps and trailing leg stomps. In this case, however, the free head has an associated ADP molecule immediately after detachment, so the free leg can rebind without undergoing ATP hydrolysis. Furthermore, because ATP hydrolysis is not executed, the free head remains in the post-power stroke state orientation which favors binding to backward sites. If we let the bound leg be at the origin $𝐫=0$, a backward step occurs when the diffusive search finds an actin site $𝐫_{n}$ with $n<0$. Hence, the free head orientation favors binding to these sites and binding occurs with probability 1 when the head diffuses within a distance $a$ of the target site and the free leg is within the acceptance region.

### Leading leg stomps

Similar to the trailing leg stomps described above, the myosin V can also execute a leading leg stomp (Kodera et al., 2010; Andrecka et al., 2015). This kinetic pathway begins with leading leg detachment, identical to the backward step. To perform a stomp, the free head diffuses to an actin binding site $𝐫_{n}$ with $n>0$. Since the free head is in the pre-power stroke state, binding to these forward sites requires an unnatural deformation of the free leg, which as in the case of trailing leg stomps, introduces an effective energy barrier to these events. Therefore, when the free head diffuses within a radius $a$ of a target site with the free leg in the acceptance region, binding occurs with probability $b<1$, given by the binding penalty.

### Termination

The final kinetic pathway occurs when the bound myosin head detaches before the free head finds an open actin binding site, terminating the processive run of myosin V. We assume that the bound leg has a constant detachment rate equal to $t_{d1}^{-1}$, independent of the backward load force exerted on the motor.

These five pathways complete the kinetic description of myosin V procession. The first four pathways, forward steps, leading and trailing leg stomps, and backward steps, each return the myosin to its waiting state with both legs bound, while termination is a complete dissociation from the actin. Therefore the myosin will continue to execute steps and stomps until termination which ends the run. For notational convenience below, we will denote the binding penalty of a given actin site $𝐫_{n}$ following trailing head detachment as $b_{n}$. Then $b_{n}=1$ for $n>0$, there is no penalty for forward steps, and $b_{n}=b<1$ if $n<0$. The binding penalty following leading head detachment is $b_{-n}$. If we sum the probabilities over all binding sites possible in a given pathway, we get the overall probability of each type of step and stomp. We define $𝒫_{f}$, $𝒫_{Ls}$, $𝒫_{Ts}$, $𝒫_{b}$, and $𝒫_{t}$ to be the overall probability of myosin executing a forward step, leading/trailing leg stomp, backward step, and termination respectively, starting from the waiting state. The above pathways are dominant when the backward load forces are below or slightly above the stall force, for which experimental estimates range from $≈1.9-3pN$ pN (Mehta et al., 1999; Veigel et al., 2002; Kad et al., 2008; Uemura et al., 2004; Cappello et al., 2007; Gebhardt et al., 2006). For large super-stall forces ($≳4$ pN), the myosin can experience power stroke reversal, swinging the leading lever arm back toward the minus end of the actin (Sellers and Veigel, 2010). At these high forces the diffusive search can therefore occur with the bound leg in the pre-power stroke orientation, so additional pathways must be added to the above model to accurately describe the super-stall behavior of myosin V. We restrict our focus to the sub-stall and stall regimes.

### First passage times and the binding acceptance region

The key quantities necessary for our theoretical description of myosin V processivity are the mean first passage times, $t_{fp}^{n}$, of the free head to each of the actin binding sites $𝐫_{n}$. These determine the relative binding probabilities for each of the many possible target actin sites. Combined with the above described step and stomp pathways, this gives us a complete kinetic description of myosin V informed by the polymer nature of the lever arms. Below we use the first passage times to compute various experimentally observable quantities including step distributions, the forward/backward step ratio, and the mean run length and velocity.

Our polymer model admits an accurate approximate analytical expression for the mean first passage time. In past theoretical work by Hinczewski et al. (2013), it was shown that the mean first passage time is approximately

$$
t_{fp}^{n}≈\frac{1}{4⁢\pi⁢D_{h}⁢a⁢𝒫⁢(𝐫_{n})},
$$

where $a$ is the capture radius, $𝒫⁢(𝐫)$ is the probability density of the free head being at position $𝐫$, and $D_{h}=5.7\times10^{-7}cm^{2}/s$ cm2/s is the diffusion constant of the myosin V head which was estimated using the program HYDROPRO (Ortega et al., 2011) with the Protein Data Bank structure 1W8J (Coureux et al., 2004). Here $𝒫⁢(𝐫)$ is the equilibrium distribution achieved at timescales greater than $t_{r}$, the relaxation timescale of the polymer. This result relies on the separation of timescales between the polymer relaxation of the lever arms and the first passage of the diffusive search. Previous BD simulations (Hinczewski et al., 2013) found that the lever arm relaxation timescale is $t_{r}≲5$ μs, which is two orders of magnitude smaller than the smallest mean first passage times, $t_{fp}^{min}∼𝒪⁢(0.1⁢⁢ms)$. Another requirement is that the time to diffuse the distance $a$, $t_{a}=a^{2}/D_{h}≈2.8ns$ ns be much smaller than the relaxation time $t_{r}$. This condition, which is clearly satisfied since $t_{a}/t_{r}≈5\times10^{-4}≪1$, guarantees that after the free head reaches the capture radius it can undergo fast microscopic rearrangements required to bind without significant conformational changes in the rest of the lever arm.

In our model there is an additional condition necessary for binding: the free leg must be within the angular acceptance region with respect to the actin subunit. Therefore, we are actually interested in the mean first passage time to finding a binding site and simultaneously having the correct orientation. Electron and atomic force microscopy imaging of myosin V indicate that while bound the myosin head attaches approximately perpendicular to the outer surface of an actin subunit (Oke et al., 2010; Kodera et al., 2010). This binding, which involves the interaction of a specific region of the head with a corresponding region on the actin subunit, is mimicked in our coarse-grained model through an angular criterion: we require that the angle between the free leg and the outward pointing normal ($𝐫^_{n}\times𝐳^$) at the target actin site be smaller than $\delta⁢ϕ_{ac}$, which defines a conical acceptance region in which binding is allowed. Based on fits to experiments described below, we set $\delta⁢ϕ_{ac}=55.6^{∘}$. We assume binding occurs with probability 1 when the free head is within a distance $a$ from a binding site and the free leg is inside the acceptance region.

Though this angular criterion is straightforward to implement in our BD simulations, for the analytical theory it significantly complicates the calculation. Hence we simplify the angular criterion in the analytical model, in a way that preserves most of the physical effect while making the derivation of the mean first passage time tractable. Instead of a conical acceptance region around the outward pointing normal to the target actin site, we only require an azimuthal angle similar to the normal. This amounts to replacing the probability density $𝒫⁢(𝐫_{n})$ in Equation 2 with the joint density of finding the free head at position $𝐫_{n}$ and the free leg simultaneously having azimuthal orientation similar to that of the binding site, $𝒫(𝐫_{n},\deltaϕ_{1}>(ϕ_{f}+\pi)-ϕ_{n}>-\deltaϕ_{2})$. Here $ϕ_{f}$ is the azimuthal angle of the end-to-end vector for the free myosin leg and $ϕ_{n}=-12⁢\pi⁢n/13$ is the azimuthal angle of an actin binding site (note the factor of $\pi$ enters because the free leg points toward the binding site). The angles are shown in Figure 1B. The acceptance region defined by $(\delta⁢ϕ_{1},\delta⁢ϕ_{2})$ will for simplicity be taken as symmetric, $\delta⁢ϕ_{1}=\delta⁢ϕ_{2}=\delta⁢ϕ_{ac}$, but we do not rule out the possibility that asymmetry in the myosin head or actin binding pocket favors binding from one direction. Similar effects have been previously observed for myosin V, for instance the suppression of ADP dissociation and head detachment depends asymmetrically on the direction of off-axis forces (Oguchi et al., 2010). The acceptance region requirement increases the first passage time, because in some cases the free head will diffuse to a binding site but have the wrong orientation and fail to bind. Therefore, the required separation of timescales still holds and, with a symmetric acceptance region, the mean first passage time is,

$$
t_{fp}^{n}≈\frac{1}{4\piaD_{h}𝒫(𝐫_{n},\deltaϕ_{ac}>|(ϕ_{f}+\pi)-ϕ_{n}|)}.
$$

The use of the simplified angular criterion in the analytical theory gives results similar to the BD simulations, where the full conical acceptance region was used.

The properties of the polymer legs as well as the influence of the binding acceptance conditions are implemented through the joint distribution $𝒫(𝐫_{n},\deltaϕ_{ac}>|(ϕ_{f}+\pi)-ϕ_{n}|)$. Adapting a polymer mean field theory (Hinczewski et al., 2013; Thirumalai and Ha, 1998) and exploiting the fact that the myosin lever arms are in the stiff regime $l_{p}≫L$, we derive an approximate analytical expression for this distribution. We also derive an expression for $𝒫⁢(𝐫)$ at any point $𝐫$ in space, which describes the equilibrium distribution of the free leg during diffusion and captures the effects of the inter-leg structural constraint, the bound leg constraint, and the load force (Appendix 1). Assuming the binding events along with trailing/leading head detachment and hydrolysis are each Poisson processes with rates $(t_{fp}^{n})^{-1}$, $t_{d1}^{-1}$, $t_{d2}^{-1}$, and $t_{h}^{-1}$ respectively, we derive the probabilities of passage through each kinetic pathway and analytical expressions for observable quantities including step distributions as well as mean run length and velocity.

### Estimating the joint constraint strength from the free head spatial distribution during stepping

Until recently, the joint between the myosin V lever arms was believed to be freely rotating, allowing the detached head to perform a full three-dimensional diffusive random walk while searching for actin binding sites. This hypothesis was supported by the work of Dunn and Spudich (2007), who used darkfield microscopy to image (from above) the diffusive path of 40 nm gold nanoparticles attached to the leg of myosin V. Their measured diffusion contours are radially symmetric about the inter-leg joint implying a freely rotating hinge. Other experiments also suggest a freely rotating joint (Shiroguchi and Kinosita, 2007; Fujita et al., 2012; Beausang et al., 2013), while theoretical and numerical models based on the free diffusion hypothesis largely agree with experimental data (Hinczewski et al., 2013; Craig and Linke, 2009; Mukherjee et al., 2017). Despite this body of evidence, recent experiments with improved spatiotemporal imaging resolution indicate that the myosin V joint might not freely rotate, instead preferring a particular inter-leg angle due to structural constraints. In particular, electron micrographs of Takagi et al. (2014) show that in the absence of actin, myosin V has a weakly preferred inter-leg angle of approximately 110°. Further, by tracking 20 nm gold particles attached to the N-terminus of the myosin head with interferometric scattering microscopy, Andrecka et al. (2015) observed a multi-peaked diffusion contour, contradicting the presence of a freely rotating joint.

Our polymer model accounts for structural constraints on diffusion encoded through the inter-leg angle preference $\theta_{p}$ and constraint strength $\mu_{c}$. We let $\theta_{p}=83.0^{∘}$, as determined by fitting to step distribution and force dependence experiments discussed below. While this value is somewhat smaller that the actin-free Takagi et al. (2014) observations, we do not expect an exact correspondence. In particular, the observed angle will be larger than $\theta_{p}$ due to volume exclusion interactions and the effective preferred angle in the presence of actin may be further altered through the influence of the bound leg on the overall conformation of the protein. The presence of a joint constraint changes the diffusion of the free leg so that it swings through a nearly one-dimensional arc while searching for binding sites rather than exploring the full three-dimensional space. In order to visualize the diffusion, we use the probability density of the location of the free head $𝒫⁢(𝐫)$ projected onto the two dimensional $z-x$, $z-y$, and $y-x$ planes as well as the cylindrical plane $z-ρ$, where $ρ=x^{2}+y^{2}$. The projection is performed by integrating over the remaining degree of freedom, for instance $𝒫⁢(x,z)=\int𝑑y⁢𝒫⁢(𝐫)$.

The diffusion contour measured by Andrecka et al. (2015) and shown in Figure 3I, corresponds to the $z-x$ projection since they imaged through a glass surface parallel to both the myosin bound leg and direction of motion. We evaluated this contour using our analytical theory for several values of the inter-leg constraint strength, $\mu_{c}=0$, 3, 5, and 12 (Figure 3A–D). These calculations agree well with diffusion contours measured from Brownian dynamics simulations for the same values of $\mu_{c}$ (Figure 3E–H). Our results show that a non-zero inter-leg constraint $\mu_{c}>0$ is required to produce a multi-peaked contour similar to that measured by Andrecka et al. (2015). In particular, when $\mu_{c}=5$ the predicted diffusion agrees well with the experimental data, while $\mu_{c}=3$ and $\mu_{c}=12$ respectively produce contours with lower and higher peaks than the measured distribution. Therefore, we estimate the energy of the inter-leg constraint lies within this range $3K_{B}T≲\mu_{c}K_{B}K≲12K_{B}T$. Incidentally, the upper bound 12 kBT is also approximately the energy at which our model can no longer accurately predict the multi-peaked step distribution of 8IQ mutants discussed in the next section.

![Figure 3.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-v2.jpg)

**Figure 3.:** Contours of the myosin V free head position distribution $𝒫⁢(𝐫)$ projected onto the $z-x$ plane.Top row: theoretical predictions for (A) free diffusion ($\mu_{c}=0$) and (B–D) constrained diffusion with inter-leg constraint strength (B) $\mu_{c}=3$, (C) $\mu_{c}=5$, and (D) $\mu_{c}=12$. Bottom row: the corresponding contours measured from Brownian dynamics simulations, with inter-leg constraint strength (E) $\mu_{c}=0$, (F) $\mu_{c}=3$, (G) $\mu_{c}=5$, and (H) $\mu_{c}=12$. (I) Experimental measurements of the diffusion by Andrecka et al. (2015). Adding an inter-leg constraint potential produces a multi-peaked diffusion pattern. The heights of the peaks are similar to the experimental measurements for $3≲\mu_{c}≲12$. Note that the $x=0$ axis in the experimental data corresponds to the position of the gold bead attached to the myosin head when the head is bound to actin. Given the ∼5 nm size of the head and ∼10 nm radius of the bead, this accounts for the approximately 15 nm vertical shift between the theoretical/simulation distributions and experiment. In the former the $x=0$ axis corresponds to the top of the actin filament (where the bound head is attached).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Alternative projections of the constrained diffusion ($\mu_{c}=5$).Top row: theoretical calculations of the diffusion projected onto the (A) $z-x$, (B) $y-x$, and (C) $z-y$ planes, and (D) the cylindrical plane $z-ρ$. Bottom row: diffusion contours measured from Brownian dynamics simulations, again projected onto the (E) $z-x$, (F) $y-x$, and (G) $z-y$ planes, and (H) the cylindrical plane $z-ρ$. Agreement between theory and simulations is excellent.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Alternative projections of the free diffusion ($\mu_{c}=0$).Top row: theoretical calculations of the diffusion projected onto the (A) $z-x$, (B) $y-x$, and (C) $z-y$ planes, and (D) the cylindrical plane $z-ρ$. Bottom row: diffusion contours measured from Brownian dynamics simulations, again projected onto the (E) $z-x$, (F) $y-x$, and (G) $z-y$ planes, and (H) the cylindrical plane $z-ρ$. In the analytical theory we include a joint Hamiltonian that penalizes small inter-leg angles. This mimics the effects of steric repulsion between the legs, which are explicitly included in the BD simulations. With this adjustment to the theory, agreement between the theory and simulations is excellent.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The constraint strength was set to $\mu_{c}=5$. The force $F$ = 2 pN is in the stall regime, just above the stall force. Top row: theoretical calculations of the diffusion projected onto the (A) $z-x$, (B) $y-x$, and (C) $z-y$ planes, and (D) the cylindrical plane $z-ρ$. Bottom row: diffusion contours measured from Brownian dynamics simulations, again projected onto the (E) $z-x$, (F) $y-x$, and (G) $z-y$ planes, and (H) the cylindrical plane $z-ρ$. The theory and simulations agree qualitatively, showing the diffusion is rotated toward the minus end of the actin compared to that at zero load (Figure 3—figure supplement 1). Quantitative discrepancies are primarily due to a small difference in the stall force between the theoretical and numerical models.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** The constraint strength was set to $\mu_{c}=5$. Top row: theoretical calculations of the diffusion projected onto the (A) $z-x$, (B) $y-x$, and (C) $z-y$ planes, and (D) the cylindrical plane $z-ρ$. Bottom row: diffusion contours measured from Brownian dynamics simulations, again projected onto the (E) $z-x$, (F) $y-x$, and (G) $z-y$ planes, and (H) the cylindrical plane $z-ρ$. Notice the difference in probability and length scales in this figure versus those preceding. The 4IQ mutant has a nearly identical diffusion pattern to the wild-type myosin, scaled down due to the decreased lever arm length.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** The constraint strength was set to $\mu_{c}=5$. Top row: theoretical calculations of the diffusion projected onto the (A) $z-x$, (B) $y-x$, and (C) $z-y$ planes, and (D) the cylindrical plane $z-ρ$. Bottom row: diffusion contours measured from Brownian dynamics simulations, again projected onto the (E) $z-x$, (F) $y-x$, and (G) $z-y$ planes, and (H) the cylindrical plane $z-ρ$. Notice the difference in probability and length scales in this figure versus those preceding. The 8IQ mutant has a nearly identical diffusion pattern to the wild-type myosin, scaled up due to the increased lever arm length.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** (A) The log of the KL divergence $D_{K⁢L}⁢(𝒫_{cos}|𝒫)$ between the free head spatial probability densities $𝒫_{cos}⁢(𝐫)$ and $𝒫⁢(𝐫)$ corresponding to the cosine potential used in the main text and $H_{J}=\mu_{c}k_{B}T[(Δ\theta)^{2}/2+h_{3}(Δ\theta)^{3}/3!+h_{4}(Δ\theta)^{4}/4!]$ respectively. The minimum KL divergence occurs at $(h_{3},h_{4})=(0,1)$, which is the quartic expansion of the cosine potential. The stars indicate the potentials used to compute diffusion contours in panels B–D. The $x-z$ diffusion contours are shown for (B) the harmonic potential $(h_{3}=h_{4}=0)$, as well as potentials with (C) $(h_{3},h_{4})=(2,4)$, and (D) $(h_{3},h_{4})=(-2,-2)$. The harmonic potential produces diffusion that is nearly identical to the cosine potential (Figure 3C), while the contour shown in C has only subtle differences. The diffusion shown in D is qualitatively different because the potential has an additional energy minimum giving rise to a new peak in the distribution. In all cases we set $\mu_{c}=5$, as in the main text.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** Data was taken using Brownian Dynamics simulations with a glass cover-slip cutting off half the 3-dimensional space, modeled with a soft-core repulsive potential as described in Appendix 2. The cover-slip is at $y$ = —5.5 nm, parallel to the $x-z$ plane and is indicated by the dashed line in the relevant diffusion projections. Top row: BD simulations of free diffusion ($\mu_{c}=0$), projected onto the (A) $z-x$, (B) $y-x$, and (C) $z-y$ planes, and (D) the cylindrical plane $z-ρ$. Bottom row: BD simulations of free diffusion ($\mu_{c}=5$), again projected onto the (E) $z-x$, (F) $y-x$, and (G) $z-y$ planes, and (H) the cylindrical plane $z-ρ$. The $z-x$ diffusion contour is not considerably altered by the cover-slip in both the free and constrained diffusion models. Therefore, the multi-peaked contour measured by Andrecka et al. (2015) is not an artifact of entropic forces due to volume exclusion.

For the cases where the constraint is strong enough to induce a bimodal distribution, the two peaks are roughly equal in height both in the analytical theory and in simulations. In constrast, the experimental distribution is asymmetric, with the peak closer to the actin about 1.5 times higher than the one further away from the actin. While we cannot rule out that some aspect of this asymmetry may be due to additional structural features not present in the model, it is also likely to be at least in part an artifact of the finite time resolution of the experiment and possibly consequences of attaching a gold nanoparticle to infer the motility of the detached motor head. The peak region further away from actin is the one that is initially visited after detachment of the trailing head. If one cannot resolve the precise moment of detachment, one might not be able to fully capture this portion of the distribution in the experimental data. In fact, Andrecka et al. (2015) measured the distribution for a range of ATP concentrations, and as the ATP was progressively increased from 1µM to 1 mM, the height of the far peak decreased relative to the near peak, even though the distribution should in principle be independent of ATP. Detachment is much more rapid at high ATP, however, and the resulting practical difficulties in collecting trajectories were mentioned in the paper.

The other projections complete the picture of the free head diffusion. These are shown for the constrained diffusion model ($\mu_{c}=5$) in Figure 3—figure supplement 1 and for the free diffusion model ($\mu_{c}=0$) in Figure 3—figure supplement 2. When the inter-leg constraint is present, the $y-x$ (front view) and $z-y$ (top view) projections together show that during its diffusive search the free leg swings out away from the actin axis at a particular height, with motion similar to that of a drawing compass. We also computed and simulated diffusion contours for myosin V under 2 pN backward force (Figure 3—figure supplement 3) as well as for the 4IQ ((Figure 3—figure supplement 4) and 8IQ mutants (Figure 3—figure supplement 5). Under force, the free head distribution rotates toward the minus end of the actin changing which target binding sites are most likely to be found during a step. The diffusion of mutants is almost identical to wild-type myosin V, but is scaled up or down based on lever arm length. This suggests that qualitative differences in stepping between mutants (discussed below) are due entirely to actin geometry.

Our calculation of the free head spatial distribution allows us to test how different forms of the inter-leg potential affect the diffusive step of myosin V. Figure 3—figure supplement 6 shows the Kullback-Leibler (KL) divergence $D_{K⁢L}⁢(𝒫_{cos}|𝒫)=\intd^{3}⁢𝐫⁢𝒫_{cos}⁢(𝐫)⁢log⁡[𝒫_{cos}⁢(𝐫)/𝒫⁢(𝐫)]$ between the free head distribution $𝒫_{cos}⁢(𝐫)$ arising from the cosine joint potential $ℋ_{J}=\mu_{c}k_{B}T[1−cos⁡(\theta_{J}−\theta_{p})]$ introduced above, and the distribution $𝒫⁢(𝐫)$ arising from a general quartic inter-leg potential $ℋ_{J}=\mu_{c}k_{B}T[(Δ\theta)^{2}/2+h_{3}(Δ\theta)^{3}/3!+h_{4}(Δ\theta)^{4}/4!]$, where $Δ⁢\theta=\theta_{J}-\theta_{p}$. Also shown in this figure are the $x-z$ diffusion contours for a few representative alternative potentials. This calculation provides a quantitative picture of how much the diffusion changes over a range of joint potentials. Specifically, our results are insensitive to the form of the potential when the anharmonic terms ($h_{3}$, $h_{4}$, etc.) are small enough to not introduce a new energy minimum in the physically relevant range of inter-leg joint angles ($Δ\theta≲\pi/2$). In this case, the resulting diffusion contour is bimodal and qualitatively similar to that shown in Figure 3.

The imaging techniques used by Andrecka et al. (2015) require a glass cover-slip which excludes half the space available for the myosin diffusive search. They report no evidence of interactions between the myosin and the surface. However, entropic forces due to volume exclusion do influence the diffusion. While it is unlikely these effects would induce a multi-peaked diffusion contour, we explicitly check this by adding a potential barrier excluding half of space in Brownian dynamics simulations (see Figure 3—figure supplement 7). Our results rule out the appearance of a multi-peaked distribution due solely to volume exclusion and confirm the cover-slip only slightly changes the shape of the diffusion contours.

The discrepancy between the single-peaked distribution of the Dunn and Spudich (2007) experiment and the the multi-peaked distribution of Andrecka et al. (2015) remains a controversy, but as noted in the latter work it can be partially resolved by adding localization noise and re-binning their data, accounting for the differences in gold nanoparticle size and the associated measurement precision between the two experiments. The fact that Dunn and Spudich (2007) attached their gold nanoparticle labels on the lever arm closer to the joint may also have contributed to concealing the constrained diffusion: the closer the label is to the joint, the closer together the two peaks appear in the distribution, and the harder it becomes to distinguish one from two peaks given finite experimental spatial resolution.

In the following sections, we use our model to test the constrained diffusion hypothesis against the large body of existing experimental data on myosin V. In the Discussion, we compare the constrained and free diffusion models and suggest further experiments to more conclusively discern between these competing myosin V diffusion hypotheses.

### Constrained diffusion model predicts zero force step distributions

The spatial fluctuations of motor proteins, among them distributions of step sizes, have long been an intriguing aspect of their behavior (Das and Kolomeisky, 2008). Let us first consider the step size distribution under zero backward force, one of the most commonly measured aspects of myosin V dynamics. The classic experiment by Yildiz et al. (2003) measured one of the first myosin step distributions using fluorescence imaging with one nanometer accuracy (FIONA). Later experiments using FIONA (Sakamoto et al., 2005) and electron microscopy (Oke et al., 2010) determined step distributions for both wild-type myosin as well as 4IQ and 8IQ mutants. The FIONA experiments measure the distance travelled by the trailing head while executing a forward step, while the electron micrographs were used to directly determine the number of actin sites separating legs while bound. These experiments qualitatively agree, with the wild-type distribution peaked at the half-helical site ($z$ = 36 nm) and an approximately linear relation between step size and lever arm length, though Sakamoto et al. (2005) measured slightly shorter 4IQ steps than Oke et al. (2010). Furthermore, Sakamoto et al. (2005) found that, due to the longer leg length, 8IQ mutants can reach the full helical actin sites ($z$ = 72 nm), giving rise to multi-peaked step distributions. This effect was not observed by Oke et al. (2010), which they note is likely because their image processing technique did not resolve large steps for which the myosin is stretched out very close to the actin.

Our polymer model gives the step distributions in terms of the structural parameters and kinetic rates described in the preceding sections. As shown in Appendix 1, after trailing leg detachment the probability of a step/stomp to site n is

$$
𝒫_{T}^{n}=\frac{b_{n}⁢t_{d1}^{2}}{t_{fp}^{n}⁢(1+r_{T}⁢t_{d1})⁢(t_{d1}+t_{h})},
$$

where $r_{T}=\sum_{n}b_{n}⁢(t_{fp}^{n})^{-1}$. The step/stomp probabilities for the leading leg $𝒫_{L}^{n}$ are given by the same expression with the substitutions, $b_{n}→b_{-n}$, $t_{h}→0$, and $r_{T}→r_{L}=\sum_{n}b_{-n}⁢(t_{fp}^{n})^{-1}$ to account for the lack of ATP hydrolysis and recovery stroke in these pathways. The trailing leg detachment occurs with probability $g⁢(1+g)^{-1}$ while the leading leg detachment occurs with probability $(1+g)^{-1}$. Thus, the probability of observing a bound myosin with $n$ subunits between the leading and trailing heads is

$$
𝒫_{dist}^{n}=\frac{g}{1+g}⁢(𝒫_{T}^{n}+𝒫_{T}^{-n})+\frac{1}{1+g}⁢(𝒫_{L}^{n}+𝒫_{L}^{-n}),n>0.
$$

This distribution (normalized to remove termination pathways), describes the probability of finding $n$ actin sites between bound heads, which was measured in the Oke et al. (2010) experiment. The overall step sizes, that is the distances traveled by the trailing leg in executing a forward step, have a distribution given by the convolution $𝒫_{T}⁢(z_{n})=(𝒫_{dist}*𝒫_{T})⁢[n]$, where $z_{n}=n⁢Δ⁢z/2$. The distribution $𝒫_{T}⁢(z_{n})$ includes both steps and stomps. For comparison to forward step distributions measured in experiments, we exclude the stomps by disallowing binding behind the bound leg and setting $𝒫_{T}^{n}=0$ for $n<0$ in the convolution. To account for the measurement resolution in FIONA experiments, we convolve this distribution with 1 nm Gaussian noise and bin the data identically to Sakamoto et al. (2005).

To fit step distributions, we fix the binding penalty $b$, capture radius $a$, and power stroke effectiveness defined as $𝒯=1+20⁢ν_{v}/(20+7⁢κ⁢ν_{c})$, where $κ=L/l_{p}$, determined via fitting to force dependence data (described below). The variable $𝒯$ measures the energy loaded by the power stroke in the effective spring formed by the lever arms (Hinczewski et al., 2013). We vary the bound leg constraint angle $\theta_{c}$, the acceptance region size $\delta⁢ϕ_{ac}$, and inter-leg preferred angle $\theta_{p}$ to minimize the Kullback-Leibler (KL) divergence between experimental step distributions and theoretical predictions for 4, 6, and 8 IQ myosin V. We also let the persistence length $l_{p}$ and bound leg constraint strength $ν_{c}$ vary along curves of constant $𝒯$, but the model predictions are robust to such parameter variation. Informed by these fits, we choose a set of parameters for which agreement between theory and experiment is excellent for all distributions. We further refine the parameter choices by alternating between fitting step distributions and force dependence behavior, feeding the parameters determined by one fit into the other. We find that $\theta_{c}=65.0^{∘}$, $\delta⁢ϕ_{ac}=55.6^{∘}$ and $\theta_{p}=83.0^{∘}$ optimizes the agreement between our theory and the full set of experimental step distributions. These and all the other parameter values in the model are summarized in Table 2. This constraint angle is similar to that indicated by imaging experiments (Walker et al., 2000; Kodera et al., 2010; Lewis et al., 2012), while the preferred inter-leg angle is slightly smaller than that observed for unbound myosin V (Takagi et al., 2014), which, as noted above, could be due to volume exclusion effects and the influence of binding to actin. The azimuthal constraint $\delta⁢ϕ_{ac}$ corresponds to an acceptance region of ∼111°, which plays a key role in restricting binding too far from the half-helical and full-helical actin sites. Step distributions and direct measurements of the azimuthal trajectory of myosin indicate steps with large azimuthal rotations are rare (Lewis et al., 2012), likely due to orientational binding constraints.

The theoretical head separation distributions are shown in Figure 4, row 1 alongside data from Oke et al. (2010) while in Figure 4, row 2 we plot the full convolved step distributions. Since Oke et al. (2010) were not able to resolve large head separations for 8IQ mutants, we compute an alternative ‘small steps’ distribution in which large head separation (> 18 actin subunits) is not considered. The theoretical distribution peaks and width agree well with Oke et al. (2010), especially for the 4IQ mutant. For 6IQ and 8IQ myosin V, the distributions are slightly broader, more similar to Sakamoto et al. (2005). In particular, we capture the multi-peaked 8IQ distribution, with peaks at about 78 nm, 110 nm, and 135 nm (indicated by arrows in panel F). The first peak comes from steps in which the free leg detaches from the half-helical site behind the bound leg and steps to the half-helical site ahead of the bound leg. Similarly, the second peak corresponds to steps with one head-to-head distance (during detachment or binding) being the full helical length and the other being the half-helical length. Finally, the third, smallest peak corresponds to the free leg starting and ending at the full helical distance. One might expect the rich stepping behavior of the 8IQ mutant to be inconsistent with the constrained diffusion hypothesis. If the joint does not freely rotate, can the myosin reach both the half- and full-helical actin subunits? Our model shows that a 5 KBT joint constraint energy is sufficiently weak to allow multi-peaked step distributions, but strong enough to considerably alter the diffusion (see previous section). We also tested large constraint energies and found that for $\mu_{c}k_{B}T≈10−12k_{B}T$ we could no longer simultaneously fit the multi-peaked 8IQ step distribution and other step distributions. This upper bound on the joint constraint energy is similar to that estimated from diffusion contours.

![Figure 4.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig4-v2.jpg)

**Figure 4.:** Top row: raw step distributions for (A) the 4IQ mutant, (B) the 6IQ wild-type, and (C) the 8IQ mutant. Bottom row: full (convolved) step distributions for (D) the 4IQ mutant, (E) the 6IQ wild-type, and (F) the 8IQ mutant, with three theoretical peak locations indicated by arrows. Theoretical distributions are shown as histograms with Brownian dynamics simulations and experimental data from Oke et al. (2010), Sakamoto et al. (2005), and Yildiz et al. (2003) indicated by symbols. The raw data from Oke et al. (2010) is convolved and binned in the bottom row. Since the imaging methods used in this experiment did not resolve large steps taken by the 8IQ mutant, in panel C we show an alternative theory (in red) with a cutoff where only small steps are allowed. The actin monomers drawn below the top row are shaded according to the analytical theory results, with the darkest color normalized to the peak of the distribution.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Same as Figure 4, but analytical theory and Brownian dynamics simulations used the free diffusion model. The analytical model was fit to data using the procedure described in the main text. We used parameters: $l_{p}=320nm$, $\theta_{c}=59.7^{∘}$, $ν_{c}=140$, $\mu_{c}=0$, $a=0.3nm$, $b=0.07$, and $\delta⁢ϕ_{ac}=57.0^{∘}$, with all other parameters identical to Table 2. Agreement with experimental measurements is comparable to that for the constrained diffusion model.

**Table 2.**
 Summary of myosin V model parameters.For the parameters identified as fit to experiments, the following approach was used: as described in the text, $\theta_{c}$, $\theta_{p}$, and $\delta⁢ϕ_{a⁢c}$ were varied to fit the step distributions, while $b$, $a$, and $𝒯=1+20⁢ν_{c}/(20+7⁢κ⁢ν_{c})$ were varied to fit the force response data. Parameters $l_{p}$ and $ν_{c}$ were also allowed to vary along curves of constant $𝒯$ while fitting the step distributions.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mechanical Parameters</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Leg contour length, L</td>
      <td>35 nm</td>
      <td>Craig and Linke, 2009</td>
    </tr>
    <tr>
      <td>Head diffusivity, Dh</td>
      <td>5.7 × 10—7 cm2/s</td>
      <td>Ortega et al., 2011; Coureux et al., 2004</td>
    </tr>
    <tr>
      <td>Leg persistence length, lp</td>
      <td>350 nm</td>
      <td>Fit to experiment*, Howard and Spudich, 1996; Vilfan, 2005a</td>
    </tr>
    <tr>
      <td>Bound leg constraint angle, θc</td>
      <td>65.0°</td>
      <td>Fit to experiment*, Lewis et al., 2012</td>
    </tr>
    <tr>
      <td>Bound leg constraint strength, νc</td>
      <td>261</td>
      <td>Fit to experiment</td>
    </tr>
    <tr>
      <td>Inter-leg preferred angle, θp</td>
      <td>83.0°</td>
      <td>Fit to experiment*, Takagi et al., 2014</td>
    </tr>
    <tr>
      <td>Inter-leg constraint strength, μc</td>
      <td>5</td>
      <td>Fit to experiment</td>
    </tr>
    <tr>
      <td>Binding Parameters</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Actin radius, R</td>
      <td>5.5 nm</td>
      <td>Lan and Sun, 2006</td>
    </tr>
    <tr>
      <td>Actin monomer size, Δ⁢z</td>
      <td>72/13 nm</td>
      <td>Lan and Sun, 2006</td>
    </tr>
    <tr>
      <td>Actin rotation angles , ϕn</td>
      <td>—12πn/13</td>
      <td>Lan and Sun, 2006</td>
    </tr>
    <tr>
      <td>Capture radius, a</td>
      <td>0.4 nm</td>
      <td>Fit to experiment*, Craig and Linke, 2009</td>
    </tr>
    <tr>
      <td>Binding penalty, b</td>
      <td>0.045</td>
      <td>Fit to experiment</td>
    </tr>
    <tr>
      <td>Acceptance region, δ⁢ϕac</td>
      <td>55.6°</td>
      <td>Fit to experiment</td>
    </tr>
    <tr>
      <td>Chemical Rates</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hydrolysis rate, th-1</td>
      <td>750 s—1</td>
      <td>De La Cruz et al., 1999</td>
    </tr>
    <tr>
      <td>TH detachment rate†, td⁢1-1</td>
      <td>12 s—1</td>
      <td>De La Cruz et al., 1999</td>
    </tr>
    <tr>
      <td>LH detachement rate, td⁢2-1</td>
      <td>1.5 s—1</td>
      <td>Purcell et al., 2005</td>
    </tr>
    <tr>
      <td>Gating ratio, g=td⁢2/td⁢1</td>
      <td>8</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Fits restricted to physically plausible parameter ranges as determined from the indicated literature.†The TH detachment rate assumes saturating ATP conditions. This is used throughout the paper except for the low ATP run velocity calculation (see Run velocity)._

The BD simulation step distributions are consistent with the results of the analytical model, as seen in Figure 4. Additionally, the simulations allow us to directly visualize examples of individual stepping trajectories. Figure 4—video 1 through Figure 4—video 3 show steps of three different sizes for the 6IQ wild-type without the inter-leg constraints ($\mu_{c}=0$). Figure 4—video 4 through Figure 4—video 6 are analogous, but with the constraint present ($\mu_{c}=5$).

### Myosin V exhibits robust step distributions under load

As a backward load force is applied to myosin V, forward steps decrease slightly in size while trailing leg stomps and backward steps become more likely. To elucidate this transition, we derive the combined leading and trailing leg step distribution (including stomps). To begin, in addition to the trailing leg steps considered above, we must also consider the distributions of steps and stomps originating from leading leg detachment. In this case, the bound leg position is behind the free leg starting position. So the initial distance between the heads is distributed as $𝒫_{-dist}^{n}=𝒫_{dist}^{-n}$. The leading leg step distribution is then given by the convolution $𝒫_{L}⁢(z_{n})=(𝒫_{-dist}*𝒫_{L})⁢[n]$, with $z_{n}=n⁢Δ⁢z/2$, and the combined leading/trailing leg step distribution is,

$$
𝒫⁢(z_{n})=\frac{g}{1+g}⁢𝒫_{T}⁢(z_{n})+\frac{1}{1+g}⁢𝒫_{L}⁢(z_{n}),
$$

where $𝒫_{T}⁢(z_{n})$ is as defined in the preceding section. The force dependence of this distribution comes from the influence of the force on the myosin lever arm, which bends under the load giving rise to a new effective constraint direction $𝐮^_{c}^{′}$ and new power stroke effectiveness $𝒯^{′}$,

$$
𝐮^_{c}^{′}=\frac{𝒯⁢𝐮^_{c}+\beta⁢F⁢L⁢𝐅^}{𝒯^{′}} and 𝒯^{′}=\sqrt{𝒯^{2}+(\beta⁢F⁢L)^{2}+2⁢𝒯⁢\beta⁢F⁢L⁢𝐅^⋅𝐮^_{c}},
$$

where $F$ is the magnitude of the load force with direction $𝐅^$, $L$ is the myosin leg length, and $\beta=1/(k_{B}⁢T)$. For backward forces, $𝐅^=-𝐳^$, the lever arm bends toward the minus end of the actin increasing the effective constraint angle, but decreasing the power stroke effectiveness.

In Figure 5A, we show the combined distribution Equation 6 for sub-stall backward forces, $F$ = 0.0 and 1.0 pN, at stall force, $F$ = 1.9 pN, and above stall force, $F$ = 2.5 pN. In this plot, peaks near +72 nm are forward steps, peaks near 0 nm are trailing or leading stomps, and peaks near –﻿72 nm are backward steps. At zero force forward steps are dominant, exhibiting the experimentally observed step distribution, while forward leg stomps also occur less frequently. The myosin remains resilient as the force increases to 1 pN, with the step distribution shifting backward by approximately a single actin binding site. This result is consistent with the step distribution under 1 pN backward force measured by Clemen et al. (2005), which was nearly identical to zero force step distributions.

![Figure 5.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig5-v2.jpg)

**Figure 5.:** (A) Distributions for zero force $F$ = 0 pN (solid line), sub-stall force $F$ = 1 pN (dashed line), stall force $F$ = 1.9 pN (dot-dashed line), and super-stall force $F$ = 2.5 pN (dotted line). The peaks near 72 nm, 0 nm and –﻿72 nm correspond to forward steps, stomps, and backward steps respectively. Applying force shifts the forward step distribution backward slightly (by about 1 actin subunit) and increases the probability of stomps and backward steps. (B) Normalized forward step distributions for $F$ = 0 pN, $F$ = 1 pN, and $F$ = 1.9 pN. Even when other kinetic pathways are dominant the shape of the forward step distribution remains robust to load force.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Shown are the normalized forward step distribution measured from BD trajectories with zero force and under backward load of 1 pN and 2 pN. The distribution is fairly robust, shifting back about one actin subunit per piconewton of applied force, in qualitative agreement with the analytical model (Figure 5B).

Further increasing the force to stall at 1.9 pN, we see that the probability of forward steps dramatically decreases. Interestingly, even though forward steps are no longer kinetically dominant, the location and shape of their distribution remains robust, as shown in Figure 5B (BD simulations show the same qualitative behavior, see Figure 5—figure supplement 1). The stall force is defined to be the force at which the expected run length of the myosin is zero. Our calculation shows that stall is due to the emergence of a backward step distribution identical to the that for forward steps. Thus, at stall force the myosin takes forward and backward steps with equal probability, making no progress along the actin. In this regime, however, the dominant kinetic pathway is trailing leg stomps which give rise to the large peak around 0 in the step/stomp distribution. Finally, increasing the force further eliminates all forward steps, increasing the prevalence of trailing stomps while shifting the backward step distribution by about one actin binding site.

An interesting prediction made by the model is the distribution of stomps, which is particularly apparent above stall force and has comparable width to the zero force step distribution. With ever improving imaging technology, it may soon be possible to reliably detect such variation in stomping experimentally. Because stomps are the dominant kinetic pathway in this force regime, many stomping events could be observed if sufficient imaging precision is achieved. Such measurements would provide further insights into how myosin V executes foot stomps. If the measured distribution significantly differs from our theoretical prediction, perhaps alternative mechanisms are involved in foot stomping. Since the leading head retains its ADP molecule after unbinding, it can in principle rebind quickly. Therefore, it is possible that leading foot stomps are dependent on non-equilibrium diffusion that occurs before the myosin legs relax to equilibrium. Further experiments are required to complete our understanding of myosin foot stomping.

The predictions made in Figure 5 will require optical trap experiments in which a load force is applied to a cargo. If the contours of the distribution of the free head are to be simultaneously measured then it becomes necessary to also attach a gold nanoparticle (Andrecka et al., 2015). The analyses of the results of such experiments, which could test our predictions, might be complicated due to hydrodynamics effects of both the cargo and the gold nanoparticle.

### Probing the biological function of the joint constraint: effects on timing and consistency of stepping

In addition to making behavioral predictions, our model also provides insights into the potential biological function of the structural joint constraint. As discussed above, our computed diffusion contours and the measurements of Andrecka et al. (2015) indicate that the joint constraint reduces the diffusion search space from fully three-dimensional to nearly one-dimensional, with the free head locations concentrated along a curve. How does this effect influence the stepping behavior of myosin V? One might expect that restricting the search space would affect both mean binding times and the step distributions.

Let us first consider the subject of binding times. As discussed above, binding in the model is more complex than just waiting for the head to diffuse within the capture radius $a$ of a binding site on actin. For the trailing leg, successful binding cannot occur until the head has hydrolyzed ATP and undergone the recovery stroke. Thus the mean timescale for ATP hydrolysis, $t_{h}$, sets the lower bound on the mean binding time. After the recovery stroke, if the trailing leg diffuses near one of the backward ($n<0$) binding sites, the probability of binding is reduced by a factor $b<1$ because the post-recovery-stroke head is not in an orientation that favors backward binding. Since polymer relaxation is fast between capture attempts, in effect this approximates partially absorptive reaction kinetics (Šolc and Stockmayer, 1971): the post-recovery-stroke head must make on average $1/b$ diffusive excursions near an $n<0$ site before it is captured. The net result of these two constraints, as derived in Appendix 1, is that the mean binding time for the trailing leg is:

$$
t_{T}=r_{T}^{−1}+t_{h},wherer_{T}=\sumnb_{n}(t_{ fp}^{n})^{−1}.
$$

Here, $b_{n}=b$ for $n<0$, $b_{n}=1$ for $n>0$. In contrast, if one is interested in the mean time for the head to diffuse within a distance $a$ of any of the binding sites, this is given by $t_{diff}=[\sum_{n}(t_{fp}^{n})^{-1}]^{-1}$ (irrespective of whether it is a trailing or leading head). Figure 6 shows $t_{T}$ versus $t_{diff}$ as a function of applied force F, and we always see $t_{T}>t_{diff}$, as expected from the above constraints. For small $F$ the trailing leg kinetics is dominated by forward steps. $t_{diff}<t_{h}$ in this regime, but even though the head can diffuse rapidly to forward binding sites, it does not bind until hydrolysis occurs. As the force is increased toward the stall regime, trailing leg stomps become the dominant pathway. The mean binding time $t_{T}$ increases by an order of magnitude, from about 1.6 ms at $F=0$ to a peak of 25 ms at $F=1.8$ pN. This is because the force biases the system toward backward binding sites (trailing leg stomps), but binding to those sites requires multiple diffusive attempts even after hydrolysis has occurred, because of the head orientation.

![Figure 6.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig6-v2.jpg)

**Figure 6.:** Myosin V timescales as a function of $F$, the backward load force.$t_{diff}$ is the mean timescale for the detached head to diffuse within radius $a$ of any of the actin binding sites. $t_{T}$ and $t_{L}$ are the mean times for the trailing and leading heads to bind after detachment. For comparison, $t_{h}$ is the mean timescale of ATP hydrolysis.

This increase may be reflected in an interesting experimental observation. Veigel et al. (2002) used an actin filament attached to beads in an optical trap, and studied the interactions between individual myosin V motors and the filament. By sinusoidally oscillating one bead (and hence the filament) they could use the amplitude of the resulting fluctuations to determine the stiffness of the motor-actin complex over time. Intervals of reduced stiffness were interpreted as times when only one head was bound, and hence the unbound head is undergoing a diffusive search. At low loads ($F<1$ pN) these intervals averaged around ∼18 ms, while at near-stall loads the intervals lasted for hundreds of milliseconds. This order of magnitude relative increase is consistent with our prediction for $t_{T}$ as a function of $F$, with the interpretation that what they were observing at high loads was primarily trailing head stomping. The absolute timescales in the experiment are larger than in the theory (for example the predicted $t_{T}$ = 1.6 ms at $F=0$ versus the experimental value of ∼18 ms), but this is likely due to the fact that the sinusoidal forcing (at 75 Hz with peak-to-peak amplitude 250 nm) is a substantial perturbation to the system that makes it harder for the head to bind (hence increasing mean binding times). However the relative increase of the binding times with force is captured by our model. Other experiments, where a gold nanoparticle is attached to one of the motor legs (Dunn and Spudich, 2007; Andrecka et al., 2015), have found binding timescales on the order of tens of milliseconds in the low load regime. Here there is another experimental artifact in play: as discussed in Hinczewski et al. (2013), the drag from the gold nanoparticle can substantially increase diffusion times, with $t_{T}$ becoming much larger than $t_{h}$ at $F=0$ because of slow diffusion.

To complete the description of the binding times, we note that the situation after leading leg detachment has several differences. Because the ADP molecule is retained, ATP hydrolysis is not necessary for rebinding, and the post power stroke orientation of the head favors backward rather than forward sites (with the latter penalized by a factor of $b$). The resulting leading leg mean binding time $t_{L}$ is:

$$
t_{L}=r_{L}^{−1},wherer_{L}=\sumnb_{−n}(t_{fp}^{n})^{−1}.
$$

At small loads the primary pathway for the leading leg is stomping. Since the head orientation necessitates multiple diffusive attempts to rebind for leading stomps, $t_{L}$ is much larger than $t_{diff}$ for small $F$, as seen in Figure 6. At larger loads backward stepping becomes the dominant pathway after leading leg detachment, and the combination of the backwards force and the favorable head orientation makes backward stepping nearly diffusion-limited, with $t_{L}$ approaching $t_{diff}$.

Based on the above discussion of binding times, we can guess that the effect of the structural constraint $\mu_{c}$ might be relatively limited: while $\mu_{c}$ does indeed affect the diffusive search space, for forward stepping at low loads the binding timescale is dominated by the ATP hydrolysis time $t_{h}$. Despite the fact that increasing $\mu_{c}$ restricts the search space (and hence potentially makes diffusion faster), we find that $t_{T}$ at $F=0$ does not substantially decrease and can increase depending on the preferred inter-leg angle (Figure 7, dashed lines). While adding the constraint makes it easier to find a few target binding sites, it simultaneously makes it harder to find other sites, so that the overall change in binding time is small. Furthermore, we emphasize that head detachment (not the binding time) is the rate limiting action in the stepping cycle at low loads. Thus, the mean binding time only influences the motor dynamics indirectly, through determination of the mean number of steps taken before complete dissociation. To have any impact on motor performance, the mean binding time would have to decrease more substantially than we have found here.

![Figure 7.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig7-v2.jpg)

**Figure 7.:** Forward step distribution width (solid lines) and mean binding time after trailing leg detachment (dashed lines) for $F=0$ as a function of the inter-leg constraint strength $\mu_{c}$.We carried out this calculation for $\theta_{p}=83^{∘}$ (the value used throughout this paper) as well as $\theta_{p}=65^{∘}$ and $95^{∘}$. As the constraint is increased the step distribution narrows, while changes in the binding time are relatively small.

So if the timing of the steps is not significantly affected, what about the step distributions? We computed these for several values of $\mu_{c}$ and found that increasing the joint constraint energy narrowed the distributions. Figure 7 (solid lines) shows the standard deviation of the forward step distribution $\sigma_{step}$ as a function of $\mu_{c}$ for preferred inter-leg angle $\theta_{p}=83^{∘}$ (the value used in above fits), 65°, and 95°. The standard deviation decreases, independent of angle preference, by approximately 0.1 nm per $k_{B}T$ of constraint energy. The constraint therefore plays a role in improving the consistency with which steps are made to a particular few target actin binding sites near the half helical length.

Finally, we conjecture that the joint constraint may also play a role in obstacle avoidance inside the crowded confines of a cell. Our diffusion contours (Figure 3, Figure 3—figure supplement 1, Figure 3—figure supplement 2) indicate that in the constrained diffusion model, the free head is significantly closer to the actin filaments throughout the diffusion. We believe that crowding could further restrict the conformational space explored by the free head, thus resulting in an even narrower step size distribution in vivo. Myosin V procession in the presence of obstacles would be an interesting topic for future study.

### Load dependence: step ratio, run length, and run velocity

For our final test of the constrained diffusion model we compare theoretical predictions to experiments on the load dependence of the forward-backward step ratio, the mean run length, and the mean run velocity (Figure 8). To fit the load dependence data, we require that the stall force and zero force run length agree with experimentally determined values, as further described below. This is achieved by varying the power stroke effectiveness $𝒯$, the binding penalty $b$, and capture radius $a$. All other parameters were held fixed as determined by experimental data or fitting the step distributions. As noted previously, we alternate between fitting the step distributions and force dependence to achieve optimal agreement between the theory and experiments.

![Figure 8.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig8-v2.jpg)

**Figure 8.:** (A) Backward-to-forward step ratio $𝒫_{b}/𝒫_{f}$; (B) mean run length $z_{run}$; (C) mean run velocity $v_{run}$. Analytical theory results are drawn as curves, experimental results as symbols. The legend symbols are the same as those in Hinczewski et al. (2013), for ease of comparison, but the theory curves have been updated.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** Same as Figure 8, but using the analytical free diffusion model, fit to experiments as described in the main text. We used parameters: $l_{p}=320nm$, $\theta_{c}=59.7^{∘}$, $ν_{c}=140$, $\mu_{c}=0$, $a=0.3nm$, $b=0.07$, and $\delta⁢ϕ_{ac}=57.0^{∘}$, with all other parameters identical to Table 2. Agreement with experimental measurements is comparable to that for the constrained diffusion model.

#### Step ratio

The backward-to-forward step ratio is defined as $𝒫_{b}/𝒫_{f}$, where $𝒫_{b}=1/(1+g)⁢\sum_{n<0}𝒫_{L}^{n}$ is the probability of taking a backward step and $𝒫_{f}=g/(1+g)⁢\sum_{n>0}𝒫_{T}^{n}$ is the probability of taking a forward step. The step ratio measured by Kad et al. (2008) exponentially increases for large load force as the myosin transitions from forward to backward stepping. The step ratio $𝒫_{b}/𝒫_{f}=1$ at $F=1.9pN$ pN, when forward and backward steps are equally likely.

For the full range of physically reasonable parameters, we find that the force at which the step ratio is one is nearly identical to the stall force (defined as the force for which the run length $z_{run}=0$). Therefore, as part of our fitting process, we require the stall force be Fstall = 1.9 pN. This value is within the range measured in other experiments. The agreement between the stall force and the force at which the step ratio is 1, is a consequence of the symmetry between the forward and backward step distributions shown in Figure 5A.

Interestingly, for intermediate forces beginning around F ≈ 1 pN, there is a small increase in the step ratio before the exponential divergence near the stall force. We find that this effect is due to the binding penalty and only occurs for $b≲0.1$. Taking $b=0.045$, the step ratio predicted by the model agrees well with the experimental data as shown in Figure 8A.

#### Run length

The run length is the distance travelled by the myosin V along the actin in a given run. By averaging over the step distribution (Equation 6), we compute the mean run length,

$$
z_{run}=\frac{1}{2}⁢\frac{\sum_{n}z_{n}⁢𝒫⁢(z_{n})}{𝒫_{t}⁢(1-𝒫_{t})},
$$

where $𝒫_{t}$ is the termination probability and $z_{n}=n⁢Δ⁢z/2$ as above. In this expression the numerator is the mean step size while the denominator accounts for the mean number of steps occurring in a run and normalization of the distribution $𝒫⁢(z_{n})$. In Appendix 1 we show that the mean number of steps is $⟨N_{run}⟩=1/𝒫_{t}$. Finally, the factor of 1/2 accounts for the fact that the center of mass of the myosin moves half the distance of the head domain in a given step.

Experimental estimates, mostly performed with zero load force, report mean run lengths in the range 0.7 – 2.4 μm , with the large variation likely due to measurement conditions (Sakamoto et al., 2000; Baker et al., 2004; Pierobon et al., 2009). We choose a representative value $z_{run}=1.3$ μm for fitting the model. With this choice, the computed run length under force also is in reasonable agreement with measurements by Clemen et al. (2005) as shown in Figure 8B.

#### Run velocity

The mean run velocity is $v_{run}=z_{run}/t_{run}$, where $t_{run}$ is the mean time elapsed during a processive run. In Appendix 1, we find

$$
t_{run}=\frac{\sum_{n}𝒫_{T}^{n}}{𝒫_{t}⁢(1-𝒫_{t})}⁢(\frac{g}{1+g}⁢t_{d⁢1}+t_{T})+\frac{\sum_{n}𝒫_{L}^{n}}{𝒫_{t}⁢(1-𝒫_{t})}⁢(\frac{g}{1+g}⁢t_{d⁢1}+t_{L}),
$$

where the mean trailing/leading binding times $t_{T}$ and $t_{L}$ are given by Equations 8 and 9. The other timescale in this expression $t_{wait}=g⁢t_{d⁢1}/(1+g)$ is the mean waiting time between detachment events. Each time is weighted by the respective probability of occurrence and the mean number of steps taken.

The theoretical mean run velocity agrees well with the experimental data shown in Figure 8C. In addition to fitting the drop to zero run length at the stall force, our model also captures the gradual decrease in run velocity at low forces ($≲1pN$), which is due to small backward shifts in the step distribution under load. This effect is not seen in the previous simplified model in which only half-helical steps were considered. We also compare to the large force measurements of Gebhardt et al. (2006), which observed myosin V walking backward with velocity ≈ 90 nm/s under 3 pN backward force. This experiment was performed at 1 μM ATP concentration, which lowers the ATP binding rate and associated trailing leg dissociation rate. Therefore, for this comparison we set td1 = 2.2 s—1 as estimated from experimental kinetics (Hinczewski et al., 2013; Gebhardt et al., 2006). The low ATP run velocity is shown as the dashed curve in Figure 8C. The backward velocity under 3 pN force is comparable, though slightly smaller than the measured value. This small discrepancy, as well as disagreement with high force data (at 5 and 10 pN force), is likely due to additional kinetic pathways in the super-stall regime, such as the power stroke reversal discussed above.

### Robust procession under off axis loads

While we have focused on verifying the consistency of structurally constrained diffusion with the full range of experiments, our model also provides a fast analytical framework for studying complex behaviors of myosin V. As an example, we consider procession under off-axis load forces, which are not parallel to the axis of the actin filaments. Off-axis loads are likely especially relevant in vivo where the myosin navigates a crowded environment.

Experiments by Oguchi et al. (2010) measured the distance myosin V walked against off-axis loads applied by a bead in an optical trap. To apply the off-axis force, the actin was attached to a glass stage which was shifted perpendicularly to the actin axis after the myosin had taken two steps. For forces that were approximately ±25° off-axis on average, the myosin walked slightly further (∼10 nm on average) than under backward force. The force at termination as well as the on-axis component of the termination force were also larger for off-axis loads. We emulated these experiments using Monte Carlo simulations, adjusting the load force after each step or stomp based on the distance from the starting location and shifting the force off axis after two steps. The average simulated run length and termination force each increased under off-axis loads (not shown), agreeing qualitatively with experiments.

We also directly compute the mean run length under a constant 1 pN load using Equation 10 for a large range of off-axis forces parameterized by the spherical angles $\theta_{F}$ and $ϕ_{F}$. The percent difference between the run length with off-axis force $(\theta_{F},ϕ_{F})$ and the run length under backward force is shown in Figure 9. Our model estimates that at worst, changing the direction of a constant load force can decrease the run length by ∼15%, while many off-axis directions lead to considerable increases in run length. The shortest run length for 1 pN force occurs at $(ϕ_{F}=0$, $\theta_{F}≈20^{∘})$. This particular $\theta_{F}$ is slightly larger than that ($\theta_{F}≈6^{∘}$) which maximizes the effective constraint angle $\theta_{c}^{′}=arctan⁡(𝐱^⋅𝐮^_{c}^{′}/𝐳^⋅𝐮^_{c}^{′})$, but has a larger $𝒯^{′}$, which strengthens the preference for locations along the constraint direction so that diffusion to forward actin sites becomes more difficult. The competition between these two effects leads to the minimized run length. For fully off-axis force ($ϕ_{F}=\pm90^{∘}$, $\theta_{F}>0$), all run lengths are larger than those under backward force. These results further corroborate the robust processivity of myosin V under off-axis loads observed experimentally by Oguchi et al. (2010).

![Figure 9.](https://cdn.elifesciences.org/articles/51569/elife-51569-fig9-v2.jpg)

**Figure 9.:** Shown is the percent change in run length from that under backward force $z_{run}⁢(\theta_{F},ϕ_{F})/z_{run}⁢(0,0)-1$ computed using Equation 9. In the worst case ($\theta_{F}≈20^{∘},ϕ_{F}=0$) the run length is decreased by $∼15%$. The run length most dramatically increases under fully off-axis forces ($\theta_{F}>0,ϕ_{F}=\pm90^{∘}$).

## Discussion

### Constrained versus free diffusion: simplified effective theories

Our theoretical analysis presented above largely supports the constrained diffusion hypothesis. The $z-x$ diffusion contour produced by the constrained diffusion model closely resembles that measured by Andrecka et al. (2015) and we find strong quantitative agreement between the model predictions and experimental data for zero force step distributions and force dependence of the step ratio, run length, and run velocity. While this evidence is convincing, we emphasize that with relatively minor parameters changes the free diffusion model also makes similarly accurate predictions, with the exception of the diffusion contours. As is particularly apparent from comparison of the $z-x$ and $y-x$ projections (Figure 3—figure supplement 2), free diffusion doesn’t produce multi-peaked distributions, implying that the freely rotating myosin explores the entire three dimensional space, contrary to the results of Andrecka et al. (2015). With respect to other experiments, however, the free diffusion model performs favorably, agreeing with step distribution and force dependence data nearly as well as the constrained diffusion model (see Figure 4—figure supplement 1 and Figure 8—figure supplement 1).

The similarity between the predictions of the constrained and free diffusion models can be explained through further analysis of the diffusion contours close to the actin. While the global diffusion patterns are very different from one another, close to the actin they look quite similar. Therefore, both the one-dimensional path under constrained diffusion and the full three-dimensional exploration under free diffusion favor binding to similar actin sites, namely those near the half-helical length of actin. This means that the free diffusion model accurately describes both step distributions and force dependence behavior. Since the diffusion time scale is much smaller than the head detachment time, the run velocity as a function of force is also quite similar between models.

The similarity between the free and constrained diffusion model predictions for on-actin behavior indicates that experimental measurements of such quantities (step distributions, run length, etc.) cannot effectively discern the true structure of the myosin V joint. The diffusive search, however, is dramatically influenced even by a small joint structural constraint. Therefore, to further probe the presence and consequences of structural constraints, experiments should directly measure the free leg diffusion. In particular, the $y-x$ projection of the diffusion shows particularly stark contrast between the constrained and free diffusion models. This contour corresponds to imaging the myosin from the front along the axis of the actin.

While our analysis and the most recent experiments suggest that myosin V has structurally constrained diffusion, the free diffusion model is still useful as a simplified effective theory for stepping behavior on the actin filaments. The precise values of physical parameters likely cannot be accurately determined with the free diffusion model, but extrapolation from fits to existing experimental data allows for valuable behavioral predictions. Both the free and constrained diffusion models can contribute to our understanding of the function of myosin V in complicated environments, for instance with off-axis load forces (see above). In fact, previous work (Hinczewski et al., 2013), indicates that the force dependence of average quantities, such as the forward step probability, step ratio, or run length, are well described by a further simplified model that only allows steps to the half-helical actin sites. Such a model cannot describe step distributions, but does contribute to our understanding of myosin V’s resilience under backward force and robust motility under perturbations to structural parameters. Since our computed and simulated diffusion contours indicate a similarity between the constrained diffusion model and simplified free diffusion models near the actin, the latter remain quite useful for studying certain behaviors of myosin V.

### Conclusion

We have developed a comprehensive low-force model of myosin V, incorporating the polymeric nature of the lever arms, the joint angle preference which gives rise to a structurally constrained diffusive search, and the full set of kinetic pathways involving all actin binding sites. The analytical model allows us to compute bounds on the joint constraint energy and captures experimental results for step distributions and the force dependence of the step ratio, run length, and run velocity. While our results are largely in support of the constrained diffusion hypothesis, the theory also provides insight about how simplified models (eg. free diffusion) can provide a useful analytical description of some myosin V behaviors. Finally, using the model we can make predictions about experimentally measurable quantities including stomp distributions and robust run length under off-axis forces. To conclude we discuss limitations and potentially interesting extensions to the model for future studies.

Throughout the present study, we have assumed that myosin V walks along a single static actin filament. In reality, the many actin filaments within a cell can come together forming crossing and branching network structures (Pollard et al., 2000). Furthermore, bending and rotational fluctuations of the actin also occur and have been characterized experimentally (Egelman et al., 1982). A recent study observed myosin V walking on actin rafts (Bao et al., 2013), while fluctuations have been considered in previous theoretical work on step distributions (Vilfan, 2005b). New actin geometries and fluctuations could be easily incorporated in our model by convolving the distribution of actin binding site locations with the distribution for the position of the free myosin head.

One regime in which our model fails is under very large super-stall loads. In particular, the large backward run velocity measured by Gebhardt et al. (2006) at 5 pN and 10 pN backward force are not captured by the model. This alternative behavior is likely due to the power stroke reversal noted above and observed in experiments (Sellers and Veigel, 2010), which would promote more frequent large backward steps. It is also likely that under such extreme forces the detachment rates of the myosin heads are altered. By adding new power stroke reversal kinetic pathways, we expect our model to better capture the large force behavior of myosin V.

Finally, our methods may be more broadly applied to the large class of processive molecular motors that operate through the combination of chemical reactions and a diffusive Brownian search. Of particular interest are myosins VI and X, which operate through a similar set of kinetic pathways, but have heterogenous lever arms with both stiff and flexible components (Sun and Goldman, 2011). Perhaps applying our approach can resolve the controversy over the conformation of the myosin VI lever arm (Spink et al., 2008; Mukherjea et al., 2009; Thirumalai and Zhang, 2010). Beyond the myosin superfamily, we anticipate our approach may also prove useful for understanding kinesin and dynein motors as well as other biomolecules that can be suitably modeled by fluctuating polymer chains.

## Materials and methods

The theoretical methods used above are fully described in Appendix 1, while the details of the Brownian dynamics simulations are in Appendix 2.
