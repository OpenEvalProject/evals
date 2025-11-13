# Dynamics of diffusive cell signaling relays

## Authors

- Paul B Dieterle<sup>1</sup> ([ORCID: 0000-0001-8129-7456](https://orcid.org/0000-0001-8129-7456))
- Jiseon Min<sup>2</sup>
- Daniel Irimia<sup>3</sup> ([ORCID: 0000-0001-7347-2082](https://orcid.org/0000-0001-7347-2082))
- Ariel Amir<sup>4</sup> ([ORCID: 0000-0003-2611-0139](https://orcid.org/0000-0003-2611-0139)) †

### Affiliations

1. Department of Physics, Harvard University Cambridge United States
2. Department of Molecular and Cellular Biology, Harvard University Cambridge United States
3. BioMEMS Resource Center and Center for Surgery, Innovation and Bioengineering, Department of Surgery, Massachusetts General Hospital Boston United States
4. John A. Paulson School of Engineering and Applied Sciences, Harvard University Cambridge United States

† Corresponding author

## Abstract

In biological contexts as diverse as development, apoptosis, and synthetic microbial consortia, collections of cells or subcellular components have been shown to overcome the slow signaling speed of simple diffusion by utilizing diffusive relays, in which the presence of one type of diffusible signaling molecule triggers participation in the emission of the same type of molecule. This collective effect gives rise to fast-traveling diffusive waves. Here, in the context of cell signaling, we show that system dimensionality – the shape of the extracellular medium and the distribution of cells within it – can dramatically affect the wave dynamics, but that these dynamics are insensitive to details of cellular activation. As an example, we show that neutrophil swarming experiments exhibit dynamical signatures consistent with the proposed signaling motif. We further show that cell signaling relays generate much steeper concentration profiles than does simple diffusion, which may facilitate neutrophil chemotaxis.

## Introduction

Prototypical diffusive signaling – in which individual cells communicate with neighbors by releasing diffusible molecules into the extracellular medium – is a relatively slow process. Signaling molecules undergoing random walks in the extracellular medium have a root mean square displacement that grows like the square root of both the time since emission, t, and the signaling molecule diffusivity, D. It follows that the distance an individual cell can signal also grows like the square root of time. Thus, for thousands of cells coordinating actions over millimeters, simple diffusive signaling with small molecules ($D≈10^{-10}$ m2/s) takes hours. These length and times scales are incommensurate with observed behavior in developmental biology (Chang and Ferrell, 2013; Cheng and Ferrell, 2018; Vergassola et al., 2018), immune response (Reátegui et al., 2017), and microbial consortia (Parkin and Murray, 2018), in which cells exchanging diffusible molecules coordinate activity over millimeters in tens of minutes.

Indeed, when many cells collectively integrate environmental cues and participate in the signaling, they can propagate diffusive waves with a fixed speed, v, in the asymptotic limit. This effect and its analogs have long been studied in the context of excitable media (Keener and Sneyd, 2009; Keener, 1987; Muratov, 2000) and observed in biological phenomena as diverse as natural cell signaling circuits (Noorbakhsh et al., 2015; Pálsson and Cox, 1996; Kessler and Levine, 1993; Gelens et al., 2014), synthetic cell signaling circuits (Parkin and Murray, 2018), apoptosis (Cheng and Ferrell, 2018), range expansions (Tanaka et al., 2017; Fisher, 1937; Kolmogorov et al., 1937; Barton and Turelli, 2011; Gandhi et al., 2016; Birzu et al., 2018), and development (Chang and Ferrell, 2013; Vergassola et al., 2018; Muratov and Shvartsman, 2004; Nolet et al., 2020). In this way, small groups of cells can transmit signals more quickly than simple diffusion allows by recruiting the help of their neighbors.

While diffusive waves have been observed in a variety of biological processes, they have also been experimentally probed in a variety of spatial contexts – in quasi-1D tubes (Cheng and Ferrell, 2018; Chang and Ferrell, 2013; Nolet et al., 2020), in quasi-2D droplets and chambers (Nolet et al., 2020; Afanzar et al., 2020), on 2D surfaces in fly eggs (Vergassola et al., 2018), and on substrates of finite thickness (Parkin and Murray, 2018; Pálsson and Cox, 1996). And while the phenomenology of diffusive waves has been studied for years, in the context of cell signaling it is less well-understood how the propagation and initiation of such waves are affected by the dimensionalities of the cellular distribution and the diffusive environment – or even how to identify the system dimensionality – as previous modeling work has largely assumed quasi-1D dynamics (Kessler and Levine, 1993; Meyer, 1991; Gelens et al., 2014; Vergassola et al., 2018). Also unclear is how robust the resulting signaling dynamics are to underlying biological details, such as the shape of the function governing cell activation and signaling molecule emission.

Here, we revisit the propagation and initiation of diffusive waves in the context of cell signaling. Through a comprehensive study of single-component relays — in which cells measure the local concentration of a signaling molecule and participate in the emission of the same molecule — we show that the asymptotic wave dynamics of diffusive relays are governed by simple scaling laws. In some system dimensionalities, these scaling laws are identical to famous results from the 20th century (Fisher, 1937; Kolmogorov et al., 1937; Luther, 1906); in other system dimensionalities, we show that these well-known scaling laws can be drastically altered. For example, cells confined to two (or one) dimensions with signaling molecule diffusion in three (or two) dimensions give rise to a diffusive wave whose speed has no dependence on D: a wave driven by diffusion whose speed does not depend on the rate of diffusion. In contrast to the dramatic effect of system dimensionality, these scaling laws are insensitive to many biological details, including the functional form of cellular activation — the dependence of signaling molecule emission rate on the local concentration. We additionally account for other phenomena – molecule decay, pulsed emission, and the discreteness of cells – that do affect the asymptotic wave dynamics; in so doing, we provide an intuitive rubric for determining under what conditions these effects alter the wave propagation speed.

In our studies of wave initiation, we systematically examine under what conditions a group of cells can trigger the formation of a diffusive wave. Here again, our results provide predictive relationships between biophysical inputs and the resulting dynamics, which are at once dramatically affected by dimensionality and largely insensitive to the details of activation and cellular uptake.

Finally, we show that neutrophil swarming experiments (Reátegui et al., 2017) display dynamics consistent with our model. In this context, our results elucidate a potential design principle of diffusive relays: they create large concentration gradients. Whereas simple diffusion of a signaling molecule from a central source creates a shallow concentration profile that falls off like $exp⁡(-r^{2}/4⁢D⁢t)$, relays give rise to steep concentration profiles with gradients that quickly propagate outward and decay only modestly inside the wave front. As such, for cells like neutrophils – which use a small molecule, leukotriene B4 (LTB4), as an intercellular signaling molecule and chemoattractant (4, 18, 19) – relays may provide a method for cells to collectively generate large, continous chemical gradients that may serve to guide directional migration; the continuous gradients generated by single-component relays contrast with the pulse trains of chemotactic cues observed in, for example, Dictyostelium discoideum (Kessler and Levine, 1993; Pálsson and Cox, 1996).

## Results

### Model construction

We begin by considering a static group of cells uniformly distributed in two dimensions – for example, atop a solid surface – and described by an area density $ρ$ (Figure 1A). We assume a cell at position $𝐫$ senses the local concentration of a signaling molecule, $c⁢(𝐫,t)$, and participates in the emission at a concentration-dependent rate $a⁢f⁢(c)$ with a the maximum rate and $f⁢(c)$ a dimensionless function. Once secreted into the extracellular medium, the signaling molecules diffuse with diffusivity D. Treating the cells and signaling molecule concentration in the continuum limit – we discuss the validity of doing in the next section and in Appendix 6: Assessing the validity of a continuum analysis – gives rise to a single equation that governs the time evolution of $c⁢(𝐫,t)$:

$$
\frac{\partial⁡c}{\partial⁡t}=D⁢\nabla^{2}⁡c+a⁢ρ⁢\delta⁢(z)⁢f⁢(c)
$$

where the Dirac delta function $\delta⁢(z)$ accounts for the fact that the cells are confined to the plane. The source function $f⁢(c)$ is in general a complicated non-linear function of c. It can include uptake, release, and cell-induced degradation of the signaling molecule – or any other process proportional to the local cell density. We will consider this general case shortly. To start, we consider a simple case in which cells measure the local signaling molecule concentration, c, and participate in the emission only if c exceeds a threshold concentration, $C_{th}$. In such a case, the activation function $f⁢(c)$ is well described by a Heaviside step function $Θ⁢[c-C_{th}]$ and the concentration dynamics obey

$$
\frac{\partial⁡c}{\partial⁡t}=D⁢\nabla^{2}⁡c+a⁢ρ⁢\delta⁢(z)⁢Θ⁢[c-C_{th}].
$$

Additionally, while we at first consider cells scattered in a two-dimensional plane, one can study the signaling dynamics of cells in a one-dimensional channel or a three-dimensional environment with similar analyses. Below, we discuss the connections between the cell signaling dynamics in all these scenarios, and all are treated in depth in Appendix 2: Asymptotic wave ansatz.

![Figure 1.](https://cdn.elifesciences.org/articles/61771/elife-61771-fig1-v2.jpg)

**Figure 1.:** (A) Schematic illustrating the diffusive relay motif. Cells (pink with purple nucleus) release a signaling molecule that diffuses (blue clouds). They do so when the local concentration exceeds a threshold, $C_{th}$. This gives rise to a diffusive wave with wave speed v. (B) Snapshot concentration profiles. Asymptotic theory (Equation (6), black lines) and numerical simulation of Equation (2) (red dots, details of the numerical methods can be found in Materials and methods) are in good agreement and show outward-propagating waves. Here, $D=10^{-10}$ m2/s, $v=2$ µm/s, and $h⁢C_{th}/a⁢ρ=D/v^{2}$. Numerical simulations assume that a cell colony of size $r_{i}=4⁢D/v$ (dashed vertical line) centered at the origin starts signaling $t=0$. (C) Numerical wave speed as measured at $t=100⁢D/v^{2}$ (markers) agrees well with theory (Equation (5), black line) as we independently vary D (circles) and $h⁢C_{th}/a⁢ρ$ (diamonds) relative to the panel B values (red circle and diamond).

### Asymptotic wave dynamics

Our first step in understanding diffusive signaling relays is to solve for the asymptotic dynamics of Equation (2). Since such relays involve cells signaling their neighbors, which then signal their own neighbors, one can imagine that diffusive relays give rise to diffusive waves. We therefore make the ansatz that the concentration $c⁢(𝐫,t)=c⁢(r,z,t)$ can be described by an outward-traveling wave of the form $c(r,z,t)=c(r~=r-vt,z)$ (Fisher, 1937; Kolmogorov et al., 1937; Tanaka et al., 2017). Here, $r~$ is the distance from the wave front – negative when inside the wave front, positive when beyond – and v is the wave speed. In essence, we wish to examine the wave from the perspective of an observer moving at the wave front. With $C_{th}≡c(r~=0,z=0)$ and $r≫D/v$, we take Equation (2) and arrive at the following equation governing asymptotic behavior:

$$
0=D(\frac{∂^{2}c}{∂r~^{2}}+\frac{1}{r}\frac{∂c}{∂r~}+\frac{∂^{2}c}{∂z^{2}})+v\frac{∂c}{∂r~}+aρ\delta(z)Θ[c−C_{th}]≈D(\frac{∂^{2}c}{∂r~^{2}}+\frac{∂^{2}c}{∂z^{2}})+v\frac{∂c}{∂r~}+aρ\delta(z)Θ[c−C_{th}]=D(\frac{∂^{2}c}{∂r~^{2}}+\frac{∂^{2}c}{∂z^{2}})+v\frac{∂c}{∂r~}+aρ\delta(z)Θ[−r~].
$$

Since we consider $r≫D/v$, we may ignore the $D⁢(\partial⁡c/\partial⁡r~)/r$ term due to the dominance of $v⁢\partial⁡c/\partial⁡r~$. This is effectively the same as ignoring the curvature of the wave front and has the effect of reducing our asymptotic analysis of cells in two dimensions into an asymptotic analysis of cells in one dimension (Tanaka et al., 2017). The asymptotic dynamics of cells distributed in three spatial dimensions allow for a similar manipulation (see Appendix 2: Asymptotic wave ansatz).

We wish to find a solution to Equation (3) for various diffusive – that is, extracellular – environments. In doing so, we hope to solve for the spatial dependence of the concentration profiles $c⁢(r~,z)$ as well as a relationship that will tell us how the signaling dynamics – in this case, the wave speed v – depend on the biophysical system parameters like the cell density, $ρ$; the concentration threshold, $C_{th}$; and the signaling molecule emission rate, a.

But first, we note that Equation (3) provides two quantities of value: a natural length scale $D/v$ and a natural time scale $D/v^{2}$. For a small diffusing molecule with $D≈10^{-10}$ m2/s and a wave speed of $v≈1$ µm/s – approximately the numbers relevant for several experimental systems (Cheng and Ferrell, 2018; Chang and Ferrell, 2013; Parkin and Murray, 2018; Vergassola et al., 2018; Pálsson and Cox, 1996) including, as we show below, neutrophil swarming (Reátegui et al., 2017) – we recover $D/v≈100$ µm and $D/v^{2}≈100$ s. We have already used the natural length scale $D/v$ to derive Equation (3) and to show that cells in 2D have the same asymptotic dynamics as cells in 1D or 3D, and we can use these scales to further justify several other approximations we have made so far. For instance, the approximation that the out-of-plane cell density can be described by $\delta⁢(z)$ is valid when the cell size $H≪D/v$; similarly, decay of the signaling molecule can be neglected for a decay rate $\gamma≪(D/v^{2})^{-1}$ while pulsed emission gives rise to the same asymptotic wave speed if the width of the pulse $\tau$ satisfies $\tau≫D/v^{2}$. Finally, we note that the use of Equation (2) as a starting point is justified when the mean distance d between neighboring cells satisfies $d⁢v/4⁢D≪1$. A thorough, mathematical discussion of all the above, including a demonstration of why $D/v$ and $D/v^{2}$ are the appropriate scales, is presented in Appendix 2: Asymptotic wave ansatz.

When the extracellular medium thickness $h≪D/v$, diffusion of the signaling molecule is effectively two-dimensional as we can take $\partial^{2}⁡c/\partial⁡z^{2}→0$ and $\delta⁢(z)→1/h$. In this limit, Equation (3) becomes

$$
h≪D/v:0=D\frac{∂^{2}c}{∂r~^{2}}+v\frac{∂c}{∂r~}+\frac{aρ}{h}Θ[c−C_{th}]=D\frac{∂^{2}c}{∂r~^{2}}+v\frac{∂c}{∂r~}+\frac{aρ}{h}Θ[−r~]
$$

which we can solve to find the asymptotic dynamics of cells in 2D (1D, 3D) with effective signaling molecule diffusion in 2D (1D, 3D) – the thin extracellular medium limit (Figure 1). This corresponds to the long-pulse, long-decay time limit of the model constructed by Kessler and Levine, 1993 and is similar to the model considered by Meyer, 1991. Adding signaling molecule decay to Equation (4) would yield a model first considered by McKean, 1970 in the context of nerve impulse propagation.

Before solving Equation (4) exactly, we make two crucial observations from which we can derive the functional form of the wave speed, v. First, because the source (furthest right) term in Equation (4) is proportional to $a⁢ρ/h$, all concentrations in the problem, including $C_{th}$, are proportional to $a⁢ρ/h$. As the non-source terms in Equations (4) and (1) are linear, the only role $a⁢ρ/h$ serves is to set the concentration scale of the dynamics. Thus, $C_{th}$, a, $ρ$, and h combine to give us a single model parameter to describe the threshold concentration, $h⁢C_{th}/a⁢ρ$, which has units of time (measured in s). Second, the only other parameter in the problem besides v – which we want to calculate – is the diffusion constant, D, which has units of length squared divided by time (measured in m2/s). Thus, the only combination of these two parameters that will give a speed (measured in m/s) is $(a⁢ρ⁢D/h⁢C_{th})^{1/2}$. By this simple dimensional analysis argument, the wave speed v can only be $v=\alpha⁢(a⁢ρ⁢D/h⁢C_{th})^{1/2}$ for some constant $\alpha$. Formally, the above procedure is equivalent to non-dimensionalizing Equation (4), as discussed in Appendix 2: Asymptotic wave ansatz.

By the same reasoning, any activation function $f⁢(c)$ – a Heaviside step function, a Hill function, or even a bistable function – that can parameterized by a single concentration $C_{th}$ and emission rate a must give the same scalings if it has a traveling wave solution. While we focus on positive activation functions in this work, we emphasize that if signaling molecule degradation is dominated by cell-induced processes like uptake, then signaling molecule degradation is also proportional to the cell density and the resulting (presumably bistable) production curve will yield dynamics that are also beholden to this scaling law.

One can confirm this scaling law for Heaviside activation by solving Equation (4) for $r~>0$ and $r~<0$, then matching boundary conditions at $r~=0$. This analysis indeed reveals that

$$
h≪D/v: C_{th}=aρD/hv^{2} ⟹ v=\sqrt{aρD/hC_{th}}
$$

while

$$
h≪D/v:c(r~)={−aρr~/hv+aρD/hv^{2}r~\leq0aρDe^{−r~v/D}/hv^{2}r~\geq0.
$$

The concentration of signaling molecule thus grows linearly in the distance inside the wave front and decays exponentially in the distance beyond the wave front. We compare numerical simulations of Equation (2) (see Materials and methods for details) with the above asymptotic formulae for wave speeds and concentration profiles in Figure 1B/C. For $r≫D/v$, the asymptotic formulae describe well both the concentration profile and the wave speed.

The wave speed relationship given in Equation (5) is analogous to the Fisher-Kolmogorov wave speed (Fisher, 1937; Kolmogorov et al., 1937; Gelens et al., 2014) – with $h⁢C_{th}/a⁢ρ$ replacing the doubling time as the characteristic time scale in the problem – and has been discussed in beautiful previous work (Gelens et al., 2014; Meyer, 1991), starting with Luther, 1906. Amazingly, Luther’s formula, which posits the scaling relation $v∼\sqrt{D}$, holds even in scenarios beyond those considered here; for instance, waves driven by oscillatory activation dynamics – as are relevant for intercellular signaling in Dictyostelium discoideum (Kessler and Levine, 1993; Pálsson and Cox, 1996) and developmental trigger wave propagation (Gelens et al., 2014; Chang and Ferrell, 2013) – are subject to this same scaling. One can understand this through simple dimensional analysis. These more complex scenarios add signaling molecule decay and a periodically modulated source function to the above model. Thus, to our set of parameters, D (measured in m2/s) and $h⁢C_{th}/a⁢ρ$ (measured in s), we add a modulation time $\tau$ (measured in seconds) and decay rate $\gamma$ (measured in 1/s). As D is the only parameter involving a length scale, it must be that $v∼\sqrt{D}$ even in these more complex scenarios.

By way of contrast, Vergassola et al., 2018 have shown that an unconventional scaling of $v∼D^{3/4}$ can result from time-dependent dynamics of the source term at the wave front, a phenomenon that breaks our assumption that all cells obey the same time-independent source function $f⁢(c)$. Similarly, as we will now show, the dimensionality of the system can also have a dramatic effect on wave speed scaling laws.

Next, we consider a thick extracellular medium for which $h≫D/v$. Such a configuration is relevant for signaling in bacterial consortia atop thick, permeable substrates (Parkin and Murray, 2018) or anywhere that a lower dimensional tissue abuts a thick and permeable extracellular environment as can be found, for example, in the retina. Here, the signaling molecules can diffuse out of plane (Figure 2A). Because the cells sit atop a solid boundary, signaling molecules can only diffuse in the upper half of the plane and the source term in Equation (3) acquires a factor of two to account for this boundary condition:

$$
h≫D/v:0=D(\frac{∂^{2}c}{∂r~^{2}}+\frac{∂^{2}c}{∂z^{2}})+v\frac{∂c}{∂r~}+2aρ\delta(z)Θ[c−C_{th}]=D(\frac{∂^{2}c}{∂r~^{2}}+\frac{∂^{2}c}{∂z^{2}})+v\frac{∂c}{∂r~}+2aρ\delta(z)Θ[−r~].
$$

![Figure 2.](https://cdn.elifesciences.org/articles/61771/elife-61771-fig2-v2.jpg)

**Figure 2.:** (A) Schematic of cells (pink with purple nucleus) performing a diffusive relay in which signaling molecules (blue clouds) can diffuse out-of-plane. Here, such relays give rise to a diffusion-constant-independent wave speed, v. (B) Snapshot concentration profiles of the signaling molecule show good agreement between numerical simulation of Equation (2) (blue dots, details of numerical methods can be found in Materials and methods) and asymptotic theory (Equation (9), black lines). Here, $D=10^{-10}$ m2/s and $v=2$ µm/s with $C_{th}/a⁢ρ=2/\pi⁢v$. The initial signaling colony is of size $r_{i}=4⁢D/v$ (dashed vertical line). (C) Numerical wave speed as measured at $t=100⁢D/v^{2}$ (markers) agrees well with theory (Equation (8), black line) as we independently vary D (circles) and $C_{th}/a⁢ρ$ (diamonds) relative to the panel B values (blue circle and diamond). As predicted, v is indeed D-independent in this system.

Effectively, we have cells in 2D with diffusion in 3D. We note that this case is asymptotically equivalent to cells in 1D emitting into a semi-infinite 2D environment. Thus, comparing to Equation (6), we can see that the asymptotic dynamics are not determined by the dimension of the cell distribution or the diffusive environment, but by the difference in dimension between them.

The same dynamics hold for cells on a curved surface (such as epithelia) as long as the length scale of the curvature and the thickness of the extracellular medium are both large compared to $D/v$. If the length scale of the curvature is large compared to $D/v$, but the extracellular medium is thin compared to $D/v$, then the dynamics will be of cells in a 2D plane with diffusion in 2D. Similarly, cells on the surface of a tube with diffusion in the tube's interior will interpolate between these two limits: when the radius of the tube is large compared to $D/v$, the dynamics will be of cells in 2D and diffusion in 3D; when the radius of the tube is small compared to $D/v$, the dynamics will be of diffusion and cells in 1D.

Examining Equation (7) as we did Equation (4) reveals that every concentration in a thick extracellular medium is proportional to $a⁢ρ$. Thus, we have two independent parameters in Equation (7): $C_{th}/a⁢ρ$ (measured in s/m) and D (m2/s). The only combination of these parameters that will give a wave speed (measured in m/s) is $a⁢ρ/C_{th}$. It therefore must be the case that $v=\alpha⁢a⁢ρ/C_{th}$ with $\alpha$ a constant – a wave driven by diffusion whose wave speed is independent of the rate of diffusion. We again stress that this is true for any activation function that has a traveling wave solution and can be parameterized by a single concentration $C_{th}$ and a single emission rate a. (For Hill function activation, $\alpha≈2/\pi$ for $n\geq2$, see Appendix 5: Asymptotic wave dynamics with Hill function activation.) Thus, the scaling laws governing the asymptotic dynamics are insensitive to the details of single-cell activation.

It is worth reflecting on the fact that some system geometries give a wave whose speed is diffusion constant-independent. This finding implies that, at least in some contexts, the size of the signaling molecule has little to do with the resultant cell signaling speed. We note that this is in contrast with the more standard wave speed scaling in Equation (5), in which smaller (lower molecular weight, higher D) signaling molecules result in a faster wave, all else equal.

A full solution of Equation (7), obtained in Appendix 2: Asymptotic wave ansatz by combining a partial Fourier transform in the z-dimension and the methods used to solve Equation (4), yields

$$
h≫D/v:C_{th}=2⁢a⁢ρ/\pi⁢v⟹v=2⁢a⁢ρ/\pi⁢C_{th}
$$

and

$$
h≫D/v: c(r~)≈{2aρ(−r~/\pivD)^{1/2}r~≪−D/vaρ(D/\pir~v^{3})^{1/2}e^{−vr~/D}r~≫D/v.
$$

So for cells in a thick extracellular medium, the concentration grows like the square root of the distance inside the wave front and decays exponentially beyond the wave front. As with the 2D diffusive environment, we verify these relationships numerically (Figure 2B/C, see Materials and methods for details of the numerical simulations). We see that the wave speed is indeed D-independent over two orders of magnitude in the diffusion constant.

The diffusive relay signaling motif therefore gives rise to diffusive information waves for which Equation (5) and Equation (8) provide predictive relationships between wave speed, threshold concentration, cell density, extracellular medium thickness, and emission rate for a variety of system dimensionalities. Similarly, Equation (6) and Equation (9) provide quantitative functional predictions of the concentration profiles generated by diffusive relays. By dimensional analysis, these scaling laws are insensitive to the details of activation. Nonetheless, other details – signaling molecule decay, pulsed emission, discreteness of cells – can alter these robust scaling laws (Keener, 2000; Dieterle P and Amir A, 2020. Manuscript in preparation). We explicitly discuss these corrections in the appendices (see Appendix 3: Pulsed emission and decay and Appendix 6: Assessing the validity of a continuum analysis), where we also discuss the dynamics of cells in 1D with 3D diffusion and the properties of waves in an arbitrary extracellular medium thickness. Both signaling molecule decay and pulsed emission decrease the steepness of the concentration gradient inside the wave front, and both decrease the wave speed. We emphasize that, in all cases, the asymptotic dynamics are not determined by the dimension of the diffusive or cellular environment, but by the difference in dimension between the two.

### Signaling wave initiation

Armed with a knowledge that diffusive relays birth diffusive waves, we now ask whether such waves are always initiated. As with the asymptotic dynamics, wave initiation depends on the system dimensionality. Here, however, the dimensionality of the diffusive environment alone determines qualitative behavior. Much previous work in chemical waves and excitable media has shown that a delicate interplay of activation, repression, and diffusion can give rise to a host of dimension-dependent wave initiation phenomena (Foerster et al., 1989; Weise and Panfilov, 2011); our task here is to study the dimension-dependent dynamics of concentration build up in single-component relays.

To begin, we consider an ‘initiating colony’ of radius ri in which cells emit a diffusible signaling molecule with rate a (Figure 3A). The surrounding cells respond by emitting the same signaling molecule according to some activation function, $f⁢(c)$. Here, we take $f⁢(c)$ to be a Hill function of degree n (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/61771/elife-61771-fig3-v2.jpg)

**Figure 3.:** (A) Schematic demonstrating wave initiation. Cells within some initial signaling volume of radius ri begin signaling at some rate a. The signaling wave is initiated when the concentration at nearby cells exceeds the threshold concentration, $C_{th}$. (B) Cells near the initial signaling volume participate in the emission according an activation function, $f⁢(c)$. For instance, in the case of Hill function activation, $f⁢(c)=[1+(C_{th}/c)^{n}]^{-1}$. C: Initiation times for Heaviside activation, in which $f⁢(c)=Θ⁢[c-C_{th}]$. Numerics (thick colored lines) and approximate asymptotic theory (Equations (10) and (11), thin black lines) of the initiation time’s dependence on ri for cells and diffusion in 1D or 2D (left) or cells in 2D with diffusion in 3D (right). For cells and diffusion in 1D, Equation (10) provides a good approximation in the limits $v⁢r_{i}/D≪1$ and $v⁢r_{i}/D≫1$. Similarly, for cells and diffusion in 2D, Equation (11) governs the large and small $v⁢r_{i}/D$ limits. In both of these cases, the wave always initiates, but the initiation time can be orders of magnitude larger than $D/v^{2}$ if $r_{i}≪D/v$. For cells and diffusion in 3D (right), signaling waves do not initiate for $v⁢r_{i}/D<\sqrt{3}$. Here again, the asymptotic theory Equation (12) is in good agreement with numerics.

In one- and two-dimensional diffusive environments, a continuously emitting source leads to a diverging concentration throughout the space. However, in three-dimensional diffusive environments, a continuously emitting source gives rise to a steady-state concentration with $1/r$ tails (Krapivsky et al., 2010).

We therefore expect that an initiating colony of cells, regardless of its radius ri (in fact, even if it consists of a single cell – see Appendix 7: Initiation dynamics), will be able initiate a diffusive wave in one- and two-dimensional environments; meanwhile, a colony in a three-dimensional environment may fail to initiate a diffusive wave. This is indeed what we observe.

In Figure 3C, we demonstrate this dramatic dimension-dependence in the case of switch-like activation, for which $f⁢(c)=Θ⁢[c-C_{th}]$. To find the initiation time $t_{init}$, we integrate Green’s functions of the diffusion equation (see Appendix 7: Initiation dynamics for details) to calculate the concentration profile created by cells continuously emitting with rate a inside the initiating colony. When the concentration at ri is equal to the threshold – $C_{th}=c⁢(r_{i},t_{init})$ – cells outside the initiating colony begin to participate in the relay and the wave is initiated. Below, we characterize the initiation time as a function of ri and the characteristic time and length scales – $D/v^{2}$ and $D/v$, respectively – of a given system, thus linking the initiation dynamics to the asymptotic wave speed, v. A summary of these results as a function of dimension, along with a summary of the asymptotic dynamics, can be found in Table 1.

**Table 1.**
 Summary of asymptotic and initiation dynamics with Heaviside activation.For different system dimensionalities, we summarize the asymptotic wave speed, v; the initiation time for small initial signaling colony size, $t_{init},\frac{v⁢r_{i}}{D}≪1$; and the initiation time for large initial signaling colony size, $t_{init},\frac{v⁢r_{i}}{D}≫1$. One-dimensional diffusive environments are assumed to be narrow channels of width h in each direction perpendicular to the channel length. The cell density $ρ$ has units 1/m for cells in 1D, 1/m2 for cells in 2D, and 1/m3 for cells in 3D. When the diffusive and cell dimensions do not match, the environment is assumed to be semi-infinite.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>tinit,</th>
      <th>tinit,</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>v</td>
      <td>v⁢riD≪1</td>
      <td>v⁢riD≫1</td>
    </tr>
    <tr>
      <td>Cells in 1D, diff. in 1D</td>
      <td>(a⁢ρ⁢Dh2⁢Cth)1/2</td>
      <td>∼(Dv⁢ri)2</td>
      <td>2⁢D/v2</td>
    </tr>
    <tr>
      <td>Cells in 1D, diff. in 2D</td>
      <td>2⁢a⁢ρπ⁢h⁢Cth</td>
      <td>∼exp(2⁢Dv⁢ri)2</td>
      <td>4⁢D/π⁢v2</td>
    </tr>
    <tr>
      <td>Cells in 2D, diff. in 2D</td>
      <td>(a⁢ρ⁢Dh⁢Cth)1/2</td>
      <td>∼exp(2⁢Dv⁢ri)2</td>
      <td>2⁢D/v2</td>
    </tr>
    <tr>
      <td>Cells in 2D, diff. in 3D</td>
      <td>2⁢a⁢ρπ⁢v</td>
      <td>no waves</td>
      <td>4⁢D/π⁢v2</td>
    </tr>
    <tr>
      <td>Cells in 3D, diff. in 3D</td>
      <td>(a⁢ρ⁢DCth)1/2</td>
      <td>no waves</td>
      <td>2⁢D/v2</td>
    </tr>
  </tbody>
</table>

For cells in 1D with 1D diffusion, the initiation time in the limits of small ($r_{i}≪D/v$) and large ($r_{i}≫D/v$) initiating colonies is:

$$
t_{init}≈{(\piD/4v^{2})(D/vr_{i})^{2}r_{i}≪D/vt_{min,1,1}=2D/v^{2}r_{i}≫D/v.
$$

When $r_{i}≪D/v$, the signaling molecules quickly diffuse across and away from the initiating colony. Thus, it is hard for the colony to build up a concentration that exceeds $C_{th}$. Correspondingly, the initiation time increases like $1/r_{i}^{2}$ for small ri. Meanwhile, for $r_{i}≫D/v$, the size of the initiating colony becomes irrelevant and reaches a minimum value of $t_{min,1D}$, determined entirely by the characteristic time scale $D/v^{2}$. The full dependence of $t_{init}$ on ri is pictured in Figure 3C, where we show that the above limits are valid approximations.

Next, we consider cells in 2D with diffusion in 2D. Here, for $r_{i}≪D/v$, the initiation time scales harshly as

$$
t_{init}∼{(r_{i}^{2}/4D)e^{(2D/vr_{i})^{2}}r_{i}≪D/vt_{min,2,2}=t_{min,1,1}=2D/v^{2}r_{i}≫D/v.
$$

Results in the above limits are corroborated by numerical simulation in Figure 3C, where we show initiation times for the limits above and for intermediate values of $v⁢r_{i}/D$.

Lastly, we consider cells in 3D with 3D diffusion and find that there is a critical initial signaling colony size of $r_{i}=\sqrt{3}⁢D/v$ below which the wave will not initiate. Around the critical colony size, $t_{init}$ diverges as $(v⁢r_{i}/D)^{6}⁢[(v⁢r_{i}/\sqrt{3}⁢D)^{2}-1]^{-2}$. If $r_{i}≫D/v$, then $t_{init}$ again plateaus at a constant value $t_{min,3D}$ that only depends on the characteristic time scale $D/v^{2}$:

$$
t_{init}≈{no initiationr_{i}<\sqrt{3} D/v\frac{(D/9\piv^{2})(vr_{i}/D)^{6}}{[(vr_{i}/\sqrt{3}D)^{2}−1]^{2}}r_{i}≈\sqrt{3} D/vt_{min,3D}=2D/v^{2}r_{i}≫\sqrt{3} D/v.
$$

These analytic expressions again agree well with numerical simulation, as seen in Figure 3C. In Appendix 7: Initiation dynamics, we work out the case of cells in 2D with diffusion in 3D, for which there is a minimum initiating colony size of $r_{i}=D/v$. There, we also show that the qualitative findings presented above also hold for systems with discrete cells.

The critical initiating colony size for a 3D environment is reminiscent of elegant work on range expansions (Tanaka et al., 2017; Barton and Turelli, 2011). There, the effects of diffusive migration and population growth compete with each other, and a critical mass is needed to initiate the spatial advance of a particular genotype. Here, the dimension-dependent dynamics of concentration build-up dictate that a signaling wave which will always initiate in one- and two-dimensional environments requires a critical initial colony size in 3D.

Because the signaling wave always initiates in one- and two-dimensional environments, it can in principle be initiated by a single cell. As random activation of a single cell can initiate a signaling wave that fixes the entire population to maximal activation, these signaling dynamics have typically been thought of as unstable (Deneke and Di Talia, 2018). Yet, as we have shown here, even in one- and two-dimensional environments, the initiation time for colonies smaller than $D/v$ can be many orders of magnitude larger than the characteristic time scale of $D/v^{2}$ (Figure 3D). Thus, even though this signaling modality is technically unstable, it is robust against stochastic activation of a small number of cells over very long time scales.

In effect, then, even strictly positive-valued activation functions require a ‘critical mass’ of cells to initiate a signaling wave. In the context of neutrophil swarming – which we will shortly consider in more detail – this critical mass may provide a basis by which the immune system ‘decides’ whether to initiate a full-scale swarming response. In vitro experiments (Reátegui et al., 2017) indicate that small colonies of a pathogen can indeed fail to incite a swarm. Moreover, since the critical size of an initiating colony goes like $D/v$, we can see that relays utilizing smaller (lower molecular weight, higher D) signaling molecules require larger critical masses, all else equal.

Finally, we note that for cells with a Hill-like activation function $f⁢(c)=c^{n}/(c^{n}+C_{th}^{n})$ of order $n\geq2$, the above results for switch-like activation provide a good quantitative approximation of the initiation times (see Appendix 8: Wave initiation with Hill function activation). Moreover, for cells in 3D with Hill activation functions of order $n>3$, there is a critical colony size just as for switch-like activation. These results highlight the role of spatial degrees of freedom in determining the wave initiation dynamics and stability.

### Application to neutrophil swarming and gradient generation

With a firm understanding of the diffusive wave and initiation dynamics, we now turn our sights to understanding a specific model system: neutrophil swarming. In beautiful work across several organisms (Lämmermann et al., 2013; Isles et al., 2019; Reátegui et al., 2017), experimentalists have observed striking behavior: an acute injury or infection can elicit rapid, highly directive motion of neutrophils – the most prevalent white blood cells – toward the site of the injury or infection. These experiments have demonstrated that a lipid small molecule called leukotriene B4 (LTB4) – along with many larger, slower-diffusing proteins (Reátegui et al., 2017) – governs the long-range recruitment of swarming neutrophils (Lämmermann et al., 2013; Afonso et al., 2012; Reátegui et al., 2017; Isles et al., 2019). Reategui et al. have noted the presence of several other pro- and anti-inflammatory lipid small molecules during swarming, though their precise roles are less clear. LTB4 serves to activate the neutrophils and also acts as a chemoattractant (Afonso et al., 2012) when receptors for LTB4 are blocked, swarming behavior is significantly impaired (Lämmermann et al., 2013; Reátegui et al., 2017). The release of LTB4 has been thought to work as a relay, although the precise mechanistic details of this relay remain unclear (Lämmermann and Germain, 2014; Kienle and Lämmermann, 2016).

In vitro experiments performed with human neutrophils are particularly relevant given the results discussed so far. In these experiments, human-derived neutrophils are injected into a chamber, then settle onto the surface of a glass slide, resulting in a uniform sprinkling of cells in 2D. Also on the glass slide are circular 'targets' (of size ri) coated in zymosan, a fungal surface protein that elicits a swarming response (Reátegui et al., 2017). Some cells land on or near the target, giving an initial condition as in Figure 3A. These cells begin signaling their neighbors, which in turn migrate towards the target (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/61771/elife-61771-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of the simple diffusion model. Here, cells on the target (within ri) signal distant neighbors by continuously emitting a single signaling molecule. If the neighboring cells have a chemotactic response, they migrate toward the target with some noise – that is, some non-zero angle $\theta$ with respect to the target. Otherwise, they move around with no sustained directionality. (B) Experimental data (color plot) reproduced from Reátegui et al., 2017 showing the information wave front in neutrophil swarming experiments. By tracking the neutrophils in space and time, they observe highly directed motion of the neutrophils towards the target (pink) starting around $t=200$ s. There is a clear boundary in space and time – the information wave front – between the regions where cells migrate toward the target (pink) and jostle around with no particular direction (white and light blue). While a relay theory (black line) is consistent with the convex shape of the information wave front, simple diffusive signaling by only the cells on the target (gray line) is not. The diffusion constants for both models is $D=1.25\times10^{-10}$ m2/s. The threshold concentrations for the relay and simple diffusion models are $C_{th}/a⁢ρ≈3.66\times10^{5}$ s/m and $2.91\times10^{4}$ s/m, respectively. The parameters for the relay model are chosen to fit the wave front by eye while the simple diffusion model parameters are chosen to give the same signaling distance at $t=500$ s. (C) Gradients created by signaling relays (black) and simple diffusion (gray) models in panel B. The dashed vertical lines indicate the location of the information wave front. As time increases from left to right, the relay signaling motif gives an information wave that signals cells faster than simple diffusion in the long time limit. Cells within the wave front (to the left of the dashed lines that indicate the wave fronts) experience significantly larger gradients when the cells utilize a relay, which may facilitate efficient chemotaxis.

By tracking individual cells in time, one can deduce their migratory direction as a function of time. A typical metric for quantifying the directionality a cell’s migration is the chemotactic index – the cosine of the angle $\theta$ between a cell’s motion and the direction of the target (Figure 4A). One can average over the cells at a given distance r and time t to construct a plot of the average directionality $⟨cos⁡\theta⟩$ in space and time. As pictured in Figure 4B, such a plot reveals a clear divide in space and time between cells that are highly directed toward the target (pink) and those without any particular directionality (white and light blue). We refer to the boundary of this divide as an information wave front – cells that lie underneath the curve have received the signal and begun chemotaxing toward the target while those above the curve have not.

Interestingly, the information wave front is convex with respect to the origin – a dramatic departure from what simple diffusive signaling by cells on the target would yield (Figure 4A/B), and from what Reategui et al. observe in experiments with neutrophils whose LTB4 receptors have been blocked (see Appendix 10: Simple diffusion model for more). We therefore posit that the cells may be participating in a relay in which they emit LTB4 in response to the same and check to see if this is consistent with the observed information wave front.

To do so, we perform a numerical simulation of Equation (2) with an additional term to account for the signaling of cells that land on the target. For this analysis, we assume a circular target of radius $r_{i}≈100$ µm, though the targets fabricated by Reategui et al. are smaller, oblong objects. Here, the diffusive environment is effectively three dimensional and the cells are close enough to allow for the use of a continuum model like Equation (2) (see below). Our model assumes switch-like activation of neutrophils, which we associate with the onset of directed chemotaxis. We ignore the inward migration of cells in this analysis, as it has a negligible effect on the information wave propagation since the cells move at a speed $u≈0.3$ µm/s $≪v$ (see Appendix 11: Quantifying the effects of chemotaxis). Thus, as mentioned above, Equation (2) effectively has two parameters: $C_{th}/a⁢ρ$ and D. Fitting these two parameters to the observed information wave front gives $C_{th}/a⁢ρ≈3.67\times10^{5}$ s/m and $D≈1.25\times10^{-10}$ m2/s, the latter of which is consistent with the diffusion constant of a small molecule like LTB4. This implies a wave speed of $v≈1.7$ µm/s. Thus, we are validated in using a continuum model with a thick extracellular medium, as for this experiment the extracellular medium thickness $h=2$ mm $≫D/v$ and the mean distance between neutrophils, $d=50$ µm, satisfies $v⁢d/4⁢D≈0.17≪1$. The cell thickness $H≈10$ µm indeed satisfies $H≪D/v$, meaning the use of the delta function to describe the cell distribution is valid. Finally, as LTB4 has a lifetime $1/\gamma$ of many minutes (Bray, 1983) and $D/v^{2}≈40$ s $≪1/\gamma$, we can indeed ignore signaling molecule decay. These fit parameters give a curve that matches the transient dynamics over the field of view of the experiment (Figure 4). Thus, our relay model gives dynamics that are consistent with the dynamics of neutrophil swarming experiments – namely, the observed convex shape of the information wave front. Larger field-of-view and longer time-course experiments with varying cell densities and larger targets will provide a deeper mechanistic understanding of such relays, while also testing the scaling predictions of Equation (5) and Equation (8).

The fit value of $C_{th}/a⁢ρ=3.67\times10^{5}$ s/m is consistent with the neutrophil’s LTB4 receptor affinity. To show this, we first note that Reategui et al. measured the LTB4 emission rate under similar conditions as the relay experiment analyzed above; they found that $a≈40$ molecules per second per cell (see Appendix 9: Sensitivity of the information front to fit parameters for details). Using the cell density of $ρ=1/d^{2}=(50⁢\mu⁢m)^{-2}$, we find that $C_{th}≈500 pM$. This value is within the range of the measured BLT1 receptor affinity for LTB4, which is reported to be approximately 0.1 − 2 nM (Yokomizo, 2015).

Finally, we comment on the matter of why neutrophils might employ such signaling relays. As we have shown above, relays lead to 'fast' communication, in the sense that they give rise to diffusive waves which travel a distance $v⁢t$ in a time t, compared to the $∼\sqrt{D⁢t}$ distance of simple diffusion. However, there is another potential reason to use diffusive relays: they create strong gradients that may help cells chemotax effectively.

To get an idea of the gradients we are working with, we compare those generated by a relay – calculated by solving Equation (2) and approximated in Equation (9) – to a comparable simple diffusion model, such as that pictured in Figure 4B. (In Appendix 10: Simple diffusion model, we present the same comparison for a thin extracellular medium.) As is well-known, a burst-like emission of a diffusible molecule creates shallow, Gaussian concentration profiles away from the source; the same is true for continuous emission of a fixed source. Thus, the gradients that individual cells or small colonies of cells can create through simple diffusive signaling are orders of magnitude shallower than the collective gradients generated by relays (Figure 4C). This hints that neutrophils may use relays not solely for their improved signaling speed, but also for the strong resulting chemotactic gradients.

## Discussion

In this work, we have shown how simple cell signaling relays can give rise to diffusive waves whose properties are robust to many underlying details. Our work especially highlights the importance of the dimensionality of the extracellular medium, as seemingly innocent changes to the environment can have large effects on the resulting diffusive waves. The strong effect of system dimensionality is reminiscent of previous work on diffusive dynamics, which showed how dimensionality can effect Turing pattern instabilities (Levine and Rappel, 2005).

Although we have characterized the asymptotic dynamics, initiation, and potential design principles of these waves in several scenarios, many interesting problems remain as yet unsolved. First, as noted by Lammermann and colleagues (Lämmermann and Germain, 2014; Kienle and Lämmermann, 2016), it is unclear how the complexities of in vivo extracellular environments affect these results, particularly in the context of neutrophil swarming. Ambient flow (for example, in blood vessels), constrictions, and complex diffusive environments may lead to dynamics of biological relevance beyond those discussed here. Additionally, it would be interesting to study how different models of chemoreception and cellular uptake – topics of theoretical (Muratov and Shvartsman, 2004) and experimental (Youk and Lim, 2014; Scherber et al., 2012; Tweedy et al., 2016) relevance – affect our conclusions.

As an experimental test of our model, we propose studying neutrophil swarming dynamics over a wide field of view with varying cell densities and extracellular medium thicknesses. For diffusive waves with approximately our experimentally inferred parameters for neutrophil swarming ($D/v≈100\mu$ µm), one could probe the thin extracellular medium limit of $h≪D/v$ with microfluidic chambers of tens of microns in height. Similarly, with mm-scale chambers introduced by Reátegui et al., 2017 and discussed in the previous section, one can reach the limit of a thick extracellular medium. Experiments in these two limits would provide quantitative tests of our theory. In particular, varying cell density would provide a test of the dimensionality-dependent relations for collective signaling wave speed, Equations (5) and (8).

On a mechanistic level, although a relay mechanism would allow neutrophils to quickly coordinate their response, it remains unclear how inflammatory response is modulated in such a scenario. If inflammation during neutrophil swarming is governed by a fast-travelling wave, then how do the cells collectively turn off response? One possibility is that signaling pathways in neutrophil swarm resolution – for instance, those involving LXA4 (Reátegui et al., 2017) production and emission – work by a similar relay mechanism; it is also possible that LTB4 production is governed by other fast-diffusing signaling molecules whose presence is necessary for LTB4 production, thereby limiting the relay’s recruitment range.

Studies of the neutrophil relay mechanism may provide an interesting contrast to similar intercellular signaling dynamics in Dictyostelium discoideum (Pálsson and Cox, 1996; Kessler and Levine, 1993; Noorbakhsh et al., 2015) and microbial consortia (Parkin and Murray, 2018). The former provides a particularly striking contrast, since the waves that drive Dictyostelium signaling are pulsatile in nature, yet are also used to coordinate chemotactic response. Whereas continuous emission relays create continuous, steep concentration profiles, pulsatile relays in Dictyostelium create traveling wave packets of high concentration, each of which elicits a chemotactic response. We see no evidence of ‘jumps’ in chemotactic response during neutrophil swarming. It is not clear what drives one organism to adopt pulsatile signaling over relays with continuous emission, or vice versa.

Finally, it would also be interesting to leverage the design principles we have discussed for engineering synthetic relays, a field with a rich history (Parkin and Murray, 2018; Brenner et al., 2008; Brenner et al., 2007; Basu et al., 2005). To that end, our results provide a general framework for determining how system dimensionality, diffusion constants, activation functions, cell density, etc. affect cell signaling and wave initiation. Experimental work on this problem and others would provide tests of our many quantitative predictions.

## Materials and methods

To find the information wave front for cells in n dimensions and diffusion in m dimensions with continuous emission and Heaviside activation, we make use of the Green’s function for the diffusion equation with sources in n dimensions and diffusion in m dimensions, $G_{n,m}⁢(r,t;R,T)$. These equations are enumerated in Appendix 7: Initiation dynamics; $d⁢T⁢d⁢R⁢a⁢ρ⁢G_{n,m}⁢(r,t;R,T)$ describes the concentration created at a radius r and time t by a tiny ring of sources at radius R with density $ρ$ that emit at rate a for duration $d⁢T$ at time T.

To find the information front, one is looking for a curve $r_{c}⁢(t)$ such that $C_{th}=c⁢(r_{c}⁢(t),t)$. Thus, with an initial signaling colony of size ri, one must solve the problem:

$$
C_{th}=a⁢ρ⁢\int_{0}^{t}𝑑T⁢\int_{0}^{max⁡[r_{i},r_{c}⁢(T)]}𝑑R⁢G_{n,m}⁢(r_{c}⁢(t),t;R,T).
$$

This constraint equation considers every radius at time T and, if it is less than $r_{c}⁢(T)$, adds a concentration contribution of $a⁢ρ⁢d⁢T⁢d⁢R⁢G_{n,m}⁢(r_{c}⁢(t),t;R,T)$ at $r_{c}⁢(t)$; the sum of all these contributions must be equal to $C_{th}$. If one wishes to find the information front for a simple diffusive theory, one performs the same integral as above, but truncates the integration over R at ri.

This method is preferable to brute PDE solving (for example, on a grid) since the former requires fine-grained meshing over the out-of-plane dimension when considering systems of, for example, cells in 2D and diffusion in 3D. In contrast, our Green’s function method requires only numerical integration over the in-plane sources; the Green’s functions appropriately keep track of the out-of-plane dynamics for us.

To solve this problem, we first find the initiation time, then find $r_{c}⁢(t)$ at discrete times, incrementing in steps of $Δ⁢t≪D/v^{2}$ (we use $Δ⁢t=D/10⁢v^{2}$ in the main text and Appendices, which gives convergence of the information wave front). Linear interpolation between these points defines a continuous curve $r_{c}⁢(t)$.

An explicit implementation of this method is provided at github./pdieterle/diffWavePropAndInit (Dieterle, 2020; copy archived at swh:1:rev:f8d9feffd57d05f47c8c14c6d9850643b2858d0a).
