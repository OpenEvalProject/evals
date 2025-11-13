# Hydrodynamic model of fish orientation in a channel flow

## Authors

- Maurizio Porfiri<sup>1</sup> ([ORCID: 0000-0002-1480-3539](https://orcid.org/0000-0002-1480-3539)) †
- Peng Zhang<sup>2</sup> ([ORCID: 0000-0001-8237-1259](https://orcid.org/0000-0001-8237-1259))
- Sean D Peterson<sup>4</sup> ([ORCID: 0000-0001-8746-2491](https://orcid.org/0000-0001-8746-2491)) †

### Affiliations

1. Department of Biomedical Engineering, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
2. Department of Mechanical and Aerospace Engineering, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
3. Center for Urban Science and Progress, New York University Tandon School of Engineering New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
4. Mechanical and Mechatronics Engineering Department, University of Waterloo Waterloo Canada ([ROR:01aff2v68](https://ror.org/01aff2v68))

† Corresponding author

## Abstract

For over a century, scientists have sought to understand how fish orient against an incoming flow, even without visual and flow cues. Here, we elucidate a potential hydrodynamic mechanism of rheotaxis through the study of the bidirectional coupling between fish and the surrounding fluid. By modeling a fish as a vortex dipole in an infinite channel with an imposed background flow, we establish a planar dynamical system for the cross-stream coordinate and orientation. The system dynamics captures the existence of a critical flow speed for fish to successfully orient while performing cross-stream, periodic sweeping movements. Model predictions are examined in the context of experimental observations in the literature on the rheotactic behavior of fish deprived of visual and lateral line cues. The crucial role of bidirectional hydrodynamic interactions unveiled by this model points at an overlooked limitation of existing experimental paradigms to study rheotaxis in the laboratory.

## Introduction

Swimming animals display a complex behavioral repertoire in response to flows (Chapman et al., 2011). Particularly fascinating is the ability of several fish species to orient and swim against an incoming flow, a behavior known as rheotaxis. While intuition may suggest that vision is necessary for fish to determine the direction of the flow, several experimental studies of midwater species swimming in a channel have documented rheotaxis in the dark above a critical flow speed (Coombs et al., 2020). When deprived of vision, fish lose the ability to hold station and they may perform sweeping, cross-stream movements from one side of the channel to other (Bak-Coleman et al., 2013; Bak-Coleman and Coombs, 2014; Elder and Coombs, 2015; Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/75225/elife-75225-fig1-v2.jpg)

**Figure 1.:** (a) Illustration of the problem with notation, showing a fish swimming in a background flow described by Equation 4. (b) Schematic of the cross-stream sweeping movement of some fish species swimming without visual cues; snapshots of fish at earlier time instants are illustrated by lighter shading.

In addition to vision, fish may rely on an array of compensatory sensory modalities to navigate the flow, which utilizes tactile, proprioceptive, olfactory, electric, kinematic, and hydrodynamic signals (Montgomery et al., 2000; von der Emde, 1999). For example, fish could sense and actively respond to linear accelerations caused by the surrounding flow using their vestibular system (Pavlov and Tjurjukov, 1995). Similarly, with the help of tactile sensors on their body surface, fish could maintain their orientation against a current through momentary contacts with their surroundings (Arnold, 1969; Lyon, 1904). Several modern studies have unveiled the critical role of the lateral line system, an array of mechanosensory receptors located on the surface of fish body (Montgomery and Baker, 2020), in their ability to orient against a current (Baker and Montgomery, 1999; Montgomery et al., 1997), hinting at a hydrodynamics-based rheotactic mechanism that has not been fully elucidated. When deprived of vision, can fish rely only on lateral line feedback to perform rheotaxis? Is there a possibility for rheotaxis to be achieved through a purely passive hydrodynamic mechanism that does not need any sensing?

Through experiments on zebrafish larvae swimming in a laminar flow in a straight tube, Oteiza et al., 2017 have recently unveiled an elegant hydrodynamic mechanism for fish to actively perform rheotaxis. Utilizing their mechanosensory lateral line, fish can sense the flow along different parts of their body, which is sufficient for them to deduce local velocity gradients in the flow and adjust their movements accordingly. As further elaborated upon by Dabiri, 2017, the insight offered by Oteiza et al., 2017 is grounded in the fundamental relationship between vorticity and circulation given by the Kelvin-Stokes’ theorem, so that fish movements will be informed by local sampling of the vorticity field. While offering an elegant pathway to explain rheotaxis, the framework of Oteiza et al., 2017 does not include a way for rheotaxis to be performed in the absence of information about the local vorticity field. Several experimental studies have shown that fish can perform rheotaxis even when their lateral line is partially or completed ablated, provided that the flow speed is sufficiently large (Bak-Coleman et al., 2013; Bak-Coleman and Coombs, 2014; Baker and Montgomery, 1999; Elder and Coombs, 2015; Montgomery et al., 1997; Oteiza et al., 2017; Van Trump and McHenry, 2013).

Mathematical modeling efforts seeking to clarify the mechanisms underlying rheotaxis are scant (Burbano-L and Porfiri, 2021; Chicoli et al., 2015; Colvert and Kanso, 2016; Oteiza et al., 2017), despite experiments on rheotaxis dating back more than a century (Lyon, 1904). A common hypothesis of existing mathematical models is that the presence of the fish does not alter the flow physics with respect to the background flow, thereby neglecting interactions between the fish and the walls of the channel. For example, the model by Oteiza et al., 2017 implements a random walk in a virtual flow, matching experimental measurements of the background flow in the absence of the animal through particle image velocimetry. A similar line of approach was pursued by Burbano-L and Porfiri, 2021 for the study of multisensory feedback control of adult zebrafish.

Thus, according to these models, the fish acts as a perfectly non-invasive sensor that probes and reacts to the local flow environment without perturbing it. There are countless examples in fluid mechanics that could question the validity of such an approximation, from coupled interactions between a fluid and a solid in vortex-induced vibrations (Williamson and Govardhan, 2004) to laminar boundary layer response to environmental disturbances that range from simple decay of the perturbation to bypass transition (Saric et al., 2002). We expect that accounting for bidirectional coupling between the fluid flow and the fish will help clarify many of the puzzling aspects of rheotaxis.

To shed light on the physics of rheotaxis, we formulate a mathematical model based on the paradigm of the finite-dipole, originally proposed by Tchieu et al., 2012. Within this paradigm, a fish is viewed as a pair of point vortices of equal and opposite strength separated by a constant distance in a two-dimensional plane. The application of the finite-dipole has bestowed important theoretical advancements in the study of hydrodynamic interactions between swimming animals (Gazzola et al., 2016; Filella et al., 2018; Kanso and Cheng Hou Tsang, 2014; Kanso and Michelin, 2019; Porfiri et al., 2021), although numerical validation of the framework against full solution of Navier-Stokes equations is lacking – conducting such a validation is also part of this study. Upon validating the dipole model, we investigate the bidirectional coupling between a fish and the surrounding fluid flow in a channel. Our work contributes to the recent literature on minimal models of fish swimming (Gazzola et al., 2014; Gazzola et al., 2015; Sánchez-Rodríguez et al., 2020) that builds on seminal work by Lighthill, 1975, Taylor, 1997 and Wu, 2006 to elucidate the fundamental physical underpinnings of locomotion and inform the design of engineering systems.

We focus on an ideal condition, where fish are deprived of all sensing systems, other than the lateral line that gives them access to information about the flow. Such flow information is coupled, however, to the motion of the fish itself, which acts as an invasive sensor and perturbs the background flow. Just as fish motion influences the local flow field, so too does the local flow field alter fish motion through advection. Predictions from the proposed model are compared against existing empirical observations on fish rheotaxis, compiled through a comprehensive literature review of published work since 1900. Data presented in the literature are used to offer context to the predicted dependence of rheotaxis performance on local flow characteristics, individual fish traits, and lateral line feedback.

## Results

### Model of the fluid flow

Consider a single fish swimming in an infinitely long two-dimensional channel of width $h$ (Figure 1(a)). Let one wall of the channel be at $y=0$ and the other at $y=h$, with $x$ pointing along the channel. The fish position at time $t$ is given by $r→_{f}⁢(t)=x_{f}⁢(t)⁢i^+y_{f}⁢(t)⁢j^$, where $i^$ and $j^$ are the unit vectors in the $x$ and $y$ directions, respectively. The orientation of the fish with respect to the $x$ axis is given by $\theta_{f}⁢(t)$ (positive counter-clockwise) and its self-propulsion velocity is $v→_{f}=v_{0}⁢(cos⁡\theta_{f}⁢i^+sin⁡\theta_{f}⁢j^)=v_{0}⁢v^_{f}$, where v0 is the constant speed of the fish and $v^_{f}$ is a unit vector in the swimming direction.

The flow is modeled as a potential flow, which is a close approximation of the realistic flow field around a fish. This simple linear fluid model is intended to capture the mean flow physics, thereby averaging any turbulence contribution. The fish is modeled as a dipole, the potential field of which at some location $r→=x⁢i^+y⁢j^$ is given by

$$
ϕ_{f}⁢(r→,r→_{f},\theta_{f})=-r_{0}^{2}⁢(\frac{(r→-r→_{f})⋅v→_{f}}{||r→-r→_{f}||^{2}}),
$$

where r0 is the characteristic dipole length-scale (on the order of the amplitude of the fish tail beating), so that the circulation of each vortex is $2⁢\pi⁢r_{0}⁢v_{0}$. This potential field is constructed assuming a far-field view of the dipole (Filella et al., 2018), wherein r0 is small in comparison with the characteristic flow length scale, which is satisfied for $ρ=r_{0}/h≪1$. The velocity field at $r→$ due to the dipole (fish) is $u→_{f}=\nabla⁡ϕ_{f}$.

A major contribution of the proposed model is the treatment of the fish as an invasive sensor that both reacts to and influences the background flow, thereby establishing a coupled interaction between the fish and the surrounding environment. A fish swimming in the vicinity of a wall will induce rotational flow near the boundary. In the inviscid limit, this boundary layer is infinitesimally thin and can be considered as wall-bounded vorticity (Batchelor, 2000). Employing the classical method of images (Newton, 2011), the influence of the wall-bounded vorticity on the flow field is equivalent to that of a fictitious fish (dipole) mirrored about the wall plane. For the case of a fish in a channel, this results in an infinite number of image fish (dipoles) (Figure 2), the position vectors for which are

$$
r→_{<,n}^{+}=x_{f}i^+(y_{f}−2(n+1)h)j^,
$$



$$
r→_{<,n}^{−}=x_{f}i^+(−y_{f}−2nh)j^,
$$



$$
r→_{>,n}^{+}=x_{f}i^+(y_{f}+2(n+1)h)j^,
$$



$$
r→_{>,n}^{−}=x_{f}i^+(−y_{f}+2(n+1)h)j^,
$$

![Figure 2.](https://cdn.elifesciences.org/articles/75225/elife-75225-fig2-v2.jpg)

**Figure 2.:** Schematic of the fish (black) in the channel (thick lines) and the set of images (gray) needed to generate the channel. The streamlines generated by the fish in an otherwise quiescent fluid are shown in the channel colored by local velocity magnitude (red: high; blue: low). Dashed and solid lines are mirroring planes for the method of images, the pattern for which continues ad infinitum.

where $n$ is a non-negative integer representing the $n$-th set of images. Subscripts “<” and “>” correspond to position vectors of the images at $y<0$ and $y>h$, respectively. Likewise, superscript “±” denotes the orientation of the image dipole as $\pm\theta_{f}$; that is, a position vector with superscript “+” indicates that the associated image has the same orientation as the fish.

The potential function for a given image is found by replacing $r→_{f}$ in Equation 1 with its position vector from Equation 2d and adjusting the sign of $\theta_{f}$ in Equation 1 to match the superscript of its vector. The potential field at $r→$ due to the image dipoles is

$$
ϕ_{w}(r→,r→_{f},\theta_{f})=\sumn=0∞(ϕ_{f}(r→,r→_{<,n}^{+},\theta_{f})+ϕ_{f}(r→,r→_{<,n}^{−},−\theta_{f})+ϕ_{f}(r→,r→_{>,n}^{+},\theta_{f})+ϕ_{f}(r→,r→_{>,n}^{−},−\theta_{f})).
$$

Thus, the velocity field due to the wall is computed as $u→_{w}=\nabla⁡ϕ_{w}$, and the overall velocity field induced by the fish is $u→_{f}+u→_{w}$. (A closed-form expression for the series in terms of trigonometric and hyperbolic functions is presented in Appendix 1) Overall, the presence of the walls distorts the flow generated by the dipole, both compressing the streamlines between the fish and the walls in its proximity and creating long-range swirling patterns in the channel (Figure 2).

The presence of a background flow in the channel is modelled by superimposing a weakly rotational flow,

$$
u→_{b}⁢(r→)=U_{0}⁢(1-4⁢ϵ⁢(\frac{y}{h}-\frac{1}{2})^{2})⁢i^,
$$

which has speed U0 at the channel centerline and $U_{0}⁢(1-ϵ)$ at the walls, $ϵ$ being a small positive parameter. As $ϵ→0$, a uniform (irrotational) background flow is recovered: such a flow is indistinguishable from the one in Figure 2, provided that the observer is moving with the background flow.

For $ϵ≪1$, the imposed velocity profile approximates that of a turbulent channel flow, wherein a modest degree of velocity profile curvature is present near the channel centerline. We note that this velocity profile does not satisfy the no-slip boundary condition (zero velocity on the walls), and the flow is entirely described by only two parameters (U0 and $ϵ$). For $ϵ≃1$, the profile approaches that of a laminar flow with parabolic dependence on the cross-stream coordinate. The overall fluid flow in the channel is ultimately computed as $u→=u→_{f}+u→_{w}+u→_{b}$.

The circulation in a region $ℛ$ in the flow field centered at some location $y$ is $Γ=\int_{ℛ}\omega⁢dA$, where $\omega=(\nabla\timesu→)⋅k^$ is the local fluid vorticity ($k^=i^\timesj^$). For the considered flow field, we determine

$$
\omega⁢(r→)=\frac{8⁢U_{0}⁢ϵ}{h}⁢(\frac{y}{h}-\frac{1}{2}),
$$

whereby the irrotational component of the flow field does not contribute to the circulation, and the circulation at a point (per unit area) is equivalent to the local vorticity.

### Numerical validation of the dipole model

Despite the success of dipole-based models in the study of fish swimming (Filella et al., 2018; Gazzola et al., 2016; Porfiri et al., 2021; Tchieu et al., 2012), their accuracy against complete Navier-Stokes simulations remains elusive. The potential flow framework in which these models are grounded neglects boundary layers and the resulting wakes that emerge from viscous effects. Quantifying the extent to which these effects influence the flow field generated by the fish is part of this study.

Specifically, computational fluid dynamics (CFD) simulations were conducted to detail the flow field around a fish during steady swimming. The simulation setup was based upon a giant danio of body length $l=7.3⁢cm$ in a channel of width $h=15.0⁢cm$. The length of the simulation domain was $L=50.0⁢cm$ ($∼6.8⁢l$) with the fish model placed at the channel centerline $20⁢cm$ ($∼2.7⁢l$) downstream of the inlet. The body undulation of the giant danio was imposed a priori in the simulation, based on data from Najafi and Abtahi, 2022. The time-resolved flow field around the fish was quantified by solving the incompressible Navier-Stokes equations. Details on the setup of the numerical framework and convergence analysis supporting its accuracy are included in Appendix 2.

The mean velocity field averaged over a tail beating cycle is displayed in Figure 3(a). The predominant flow feature observed in the mean field is a flow circulation from the head to the tail of the fish with left-right symmetry and compression of the streamlines near the channel walls. The highest velocity is found at the head of the fish with a thrust wake and recirculation region downsteam of the animal – both at a lower velocity than the anterior flow. The largest velocity in the wake is less than 20% of the peak values recorded ahead of the fish. Additional simulation results are included in Appendix 2. The flow field predicted by the dipole model is in good agreement with numerical simulations, as shown in Figure 3. The dipole model is successful in capturing the circulation from the head to the tail and the compression of the streamlines near the walls. These features are expected to be the main drivers of the interaction between the fish and the channel walls, thereby supporting the value of a dipole model for a first-order analysis of the hydrodynamics of rheotaxis.

![Figure 3.](https://cdn.elifesciences.org/articles/75225/elife-75225-fig3-v2.jpg)

**Figure 3.:** (a) Mean velocity field around the steady swimming giant danio relative to the background flow. (b) Velocity field predicted by a dipole with $\theta=\pi$ located at $0.315⁢l$ from the fish head along its centerline relative to the background flow. The selection of the dipole location and strength is detailed in Appendix 2.

### Model of fish dynamics

From knowledge of the fluid flow in the channel, we compute the advective velocity $U→⁢(r→_{f},\theta_{f})$ and hydrodynamic turn rate $Ω⁢(r→_{f},\theta_{f})$ at the fish location, which encode the influence of the confining walls and background flow on the translational and rotational motion of the fish, respectively. Neglecting the inertia of the fish so that it instantaneously responds to changes in the fluid flow, we determine (Filella et al., 2018)

$$
r→˙_{f}⁢(t)=U→⁢(r→_{f}⁢(t),\theta_{f}⁢(t))+v→_{f}⁢(\theta_{f}⁢(t)),
$$



$$
\theta˙_{f}⁢(t)=Ω⁢(r→_{f}⁢(t),\theta_{f}⁢(t))+\lambda⁢(r→_{f}⁢(t),\theta_{f}⁢(t)),
$$

where λ is the feedback mechanism based on the circulation measurement through the lateral line.

The advective velocity is found by de-singularizing the total velocity field $u→$ at $r→=r→_{f}$, which is equivalent to calculating the sum of the velocity due to the walls and the background flow in correspondence of the fish (Milne-Thomson, 1996)

$$
U→⁢(r→_{f},\theta_{f})=(u→_{w}⁢(r→,r→_{f},\theta_{f})+u→_{b}⁢(r→))|_{r→=r→_{f}}=-\frac{\pi^{2}⁢v_{0}⁢ρ^{2}}{12}⁢[(1+3⁢csc^{2}⁡(\frac{\pi⁢y_{f}}{h}))⁢cos⁡\theta_{f}⁢i^-(1-3⁢csc^{2}⁡(\frac{\pi⁢y_{f}}{h}))⁢sin⁡\theta_{f}⁢j^]+U_{0}⁢(1-4⁢ϵ⁢(\frac{y_{f}}{h}-\frac{1}{2})^{2})⁢i^.
$$

Equation (7) indicates that the walls have a retarding effect on the swimming speed of the fish that increases in magnitude the closer the fish gets to either wall of the channel. A fish swimming with orientation $\theta_{f}=0$ at the center of the channel, for example, will swim with velocity $r→˙_{f}⁢(t)=v_{0}⁢(1-(\pi^{2}/3)⁢ρ^{2})⁢i^+U_{0}⁢i^$. This effect should not be mistaken as traditional viscous drag, which is not included in potential flow theory; rather, it should be intended as the impact of nearby solid boundaries.

Hydrodynamic turn rate is incorporated by considering the difference in velocity experienced by the two constituent vortices comprising the dipole, namely,

$$
Ω(r→_{f},\theta_{f})=−v^_{f}⋅[∇(u→_{w}(r→,r→_{f},\theta_{f})+u→_{b}(r→))|_{r→=r→_{f}}]v^_{f}^{⊥}=−\frac{\pi^{3}ρ^{2}v_{0}}{4h}cot⁡(\frac{\piy_{f}}{h})csc^{2}⁡(\frac{\piy_{f}}{h})cos⁡\theta_{f}+\frac{8U_{0}ϵ}{h}(\frac{y_{f}}{h}−\frac{1}{2})cos^{2}⁡\theta_{f},
$$

where $v^_{f}^{⟂}=k^\timesv^_{f}$; see Materials and methods section for the mathematical derivation. Equation (8) indicates that interaction with the walls causes the fish to turn towards the nearest wall; for example, a fish at $y_{f}=3/4⁢h$, will experience a turn rate due to the wall of $(\pi^{3}⁢ρ^{2}⁢v_{0})/(2⁢h)⁢cos⁡\theta_{f}$, such that it will be rotated counter-clockwise if swimming downstream and clockwise if swimming upstream. On the other hand, the turning direction imposed by the background flow is always positive (counter-clockwise) in the right half of the channel and negative (clockwise) in the left half, irrespective of fish orientation, so that a fish at $y_{f}=3/4⁢h$ will always be rotated counter-clockwise. As a result, the fish may turn towards or away from a wall, depending on model parameters and orientation.

Based on experimental observations and theoretical insight (Burbano-L and Porfiri, 2021; Oteiza et al., 2017), we hypothesize that hydrodynamic feedback, that is, lateral line measurements of the surrounding fluid that fish can employ to navigate the flow, is related to the measurement of the circulation in a region surrounding the fish. This hypothesis is supported by experimental evidence presented in Oteiza et al., 2017, which indicated the ability of fish to sense variations in the local velocity gradients to perform rheotaxis. Therein, the authors also found that partial ablation of the lateral line leads to the loss of the rheotactic behavior, hinting at the importance of the flow information on both sides of the fish body for the estimation of the flow circulation.111 Temporal fluctuations, as in turbulent flows, are neglected in our model. As such, we assume time-averaged circulation sensing from the lateral line. We consider a rectangular region $ℛ$ of width r0 along the fish body length $l$. For simplicity, we assume a linear feedback mechanism, $\lambda⁢(r→_{f},\theta_{f})=K⁢Γ⁢(r→_{f},\theta_{f}),$ where we made evident that circulation is computed about the fish location and $K$ is a non-negative feedback gain. Assuming that the fish size is smaller than the characteristic length scale of the flow, we linearize the vorticity along the fish in Equation 5 as $\omega⁢(r→)≈\omega⁢(r→_{f})+\nabla⁡\omega⁢(r→_{f})⋅v^_{f}⁢Δ⁢l$. By computing the integral from $Δ⁢l=-l/2$ to $l/2$, we obtain

$$
\lambda⁢(r→_{f},\theta_{f})=K⁢r_{0}⁢l⁢\frac{8⁢U_{0}⁢ϵ}{h}⁢(\frac{y_{f}}{h}-\frac{1}{2}).
$$

Compared to established practice for modeling fish behavior in response to visual stimuli (Calovi et al., 2014; Couzin et al., 2005; Gautrais et al., 2009; Zienkiewicz et al., 2015), the proposed model introduces nonlinear dynamics arising from the bidirectional coupling between the motion of the fish and the flow physics in its surroundings. We note that the employed feedback in Equation 9 neglects additional potential sensing mechanisms, including vision (Lyon, 1904), acceleration sensing through the vestibular system (Pavlov and Tjurjukov, 1995), and pressure sensing through sensory afferents in the fins (Hardy et al., 2016), which might enhance the ability of fish to navigate the flow.

### Analysis of the planar dynamical system

Given that the right hand side of equation set Equation 6a and Equation 6b is independent of the streamwise position of the fish, the equations for the cross-streamwise motion and the swimming direction can be separately studied, leading to an elegant nonlinear planar dynamical system. We center the cross-stream coordinate about the center of the channel and non-dimensionalize it with respect to $h$, introducing $ξ=y_{f}/h-1/2$. The governing equations become

$$
ξ˙=[1-\frac{\pi^{2}⁢ρ^{2}}{12}⁢(3⁢csc^{2}⁡(\pi⁢(ξ+\frac{1}{2}))-1)]⁢sin⁡\theta_{f},
$$



$$
\theta˙_{f}=-\frac{\pi^{3}⁢ρ^{2}}{4}⁢cot⁡(\pi⁢(ξ+\frac{1}{2}))⁢csc^{2}⁡(\pi⁢(ξ+\frac{1}{2}))⁢cos⁡\theta_{f}+8⁢\alpha⁢ξ⁢(cos^{2}⁡\theta_{f}+κ),
$$

where we non-dimensionalized by the time needed for the fish to traverse the channel in the absence of a background flow, that is, $h/v_{0}$, and introduced $\alpha=U_{0}⁢ϵ/v_{0}$ and $κ=K⁢r_{0}⁢l$ (see Materials and methods section for estimation of these parameters from experimental observations).

In search of the equilibria of the dynamical system, we note that swimming downstream or upstream ($\theta_{f}=0$ and π, respectively) solves Equation 10a for any choice of the cross-stream coordinate, the value of which is determined from the solution of Equation 10b for the corresponding orientation $\theta_{f}$. In the case of downstream swimming, the only solution of the resulting transcendental equation is $ξ=0$. For upstream swimming, depending on the value of the parameter $\beta=(\alpha⁢(1+κ))/ρ^{2}$, we have one or three solutions: if $\beta<\beta^{∗}=\pi^{4}/32$, the only solution is $ξ=0$, otherwise, in addition to $ξ=0$, there are two solutions symmetrically located with respect to the centerline that approach the walls as $\beta→∞$ (Figure 4(a), see Materials and methoods section for mathematical derivations).

![Figure 4.](https://cdn.elifesciences.org/articles/75225/elife-75225-fig4-v2.jpg)

**Figure 4.:** (a) Cross-stream equilibria for upstream swimming as a function of β. (b,c) Phase plot for downstream and upstream swimming in the case $\alpha=0.1$, $ρ=0.1$, and $κ=1$, so that $\beta=20$. In all panels, red refers to unstable equilibria and green to stable equilibria.

Local stability of these equilibria is determined by studying the eigenvalues of the state matrix of the corresponding linearized dynamics. For all the considered dynamics, the trace of the state matrix is zero, so that the equilibria can be saddle points (unstable) or neutral centers (stable), if the determinant is negative or positive, respectively (Bakker, 1991; see Materials and methods section for mathematical derivations). In the case of downstream swimming, the determinant is always negative, such that the equilibrium $(\theta_{f}=0,ξ=0)$ is a saddle point (Figure 4(b)). For upstream swimming, the equilibrium $(\theta_{f}=\pi,ξ=0)$ is stable if $\beta>\beta^{∗}$, leading to periodic oscillations similar to experimental observations (Bak-Coleman et al., 2013; Bak-Coleman and Coombs, 2014; Elder and Coombs, 2015; Figure 1(b)); the other two equilibria located away from the centerline are always unstable (Figure 4(b and c)). Oscillations about the centerline during rheotaxis have a radian frequency $\omega_{0}≃(\pi^{2}/2)⁢ρ⁢\sqrt{\beta/\beta^{*}-1}$, such that the frequency increases with the square root of β and is zero at $\beta^{*}$ (see Materials and methods section for the mathematical derivation).

## Discussion

There is overwhelming evidence that fish can negotiate complex flow environments by responding to even small flow perturbations (Liao, 2007). However, seldom are these perturbations included in mathematical models of fish behavior, which largely rely on vision cues (Calovi et al., 2014; Couzin et al., 2005; Gautrais et al., 2009; Zienkiewicz et al., 2015). In this paper, we proposed a hydrodynamic model for the bidirectional coupling between fish swimming and fluid flow in the absence of any sensory input but lateral line feedback – encapsulated by a simple linear feedback mechanism. The model reduces to a nonlinear planar dynamical system for the cross-stream coordinate and orientation, of the kind that are featured in nonlinear dynamics textbooks for their elegance, analytical tractability, and broad physical interest (Sastry, 2013).

The planar system anticipates several of the surprising features of rheotaxis. In particular, this study provides some potential answers to the question raised by Coombs et al., 2020: “…what role, if any, do passive (e.g. wind vane) mechanisms play in rheotaxis and how are these influenced by fish factors (e.g. body shape) and flow dynamics?” Through the mathematical analysis of the model, we uncovered an equilibrium at the channel centerline for upstream swimming whose stability is controlled by a single non-dimensional parameter that summarizes flow speed, lateral line feedback, flow gradient, channel width, and fish size. Above a critical value of this parameter, the model predicts that rheotaxis is stable and fish will begin periodic cross-stream sweeping movements whose amplitude can be as large as the channel width. Interestingly, the model anticipates rheotaxis even without sensory feedback, through only passive hydrodynamic mechanisms.

Our mathematical proof of the existence of a nontrivial threshold for β above which upstream swimming becomes stable finds partial support in experimental observations on a number of species in the absence of visual cues (see Appendix 3, where we have performed a bibliographical survey on experimental studies about rheotaxis). Several of these experiments have indicated the existence of a threshold in the flow speed or flow gradient above which fish successfully perform rheotaxis. Importantly, we predict that the presence of channel walls is necessary for the emergence of such a threshold, since for $ρ→0$, $\beta→∞$, thereby automatically guaranteeing the stability of upstream swimming. Based on our estimation of α and ρ from available data, β can be as small as 10-1 and exceed 102, thereby encompassing the critical value $\beta^{*}≃3$ (see Materials and methods section for estimation of model parameters). We should exercise care in drawing comparisons with experiments, which only control for visual feedback, in contrast with the model where we block all sensory modalities except of the lateral line. As reviewed by Coombs et al., 2020, water-motion cues can also be accessible to tactile or other cutaneous senses, beyond the lateral line that is included in our model. In addition, body-motion cues are not limited to visual senses, whereby they can be accessed by tactile and vestibular senses. Hence, a one-to-one comparison between experiments and theory is presently not possible.

The model predicts the emergence of rheotaxis in the absence of any sensory information. Setting $κ=0$ in our model eliminates hydrodynamic feedback, yet, the fish is able to perform rheotaxis at sufficiently large flow speeds and steep flow gradients. This finding would support the possibility of a completely passive mechanism for rheotaxis. To date, there is no experiment on live animals that can be used to support this claim, owing to the necessity to eliminate all sensory modalities without compromising fish ability to swim. In practice, this may be unfeasible to do. As discussed in Coombs et al., 2020, existing approaches for disabling senses suffer from potential pitfalls, including: (i) unintended effects on the overall fish behavior, which are likely to occur in an effort to block at once vestibular, tactile, and lateral line senses, and (ii) difficulty in guaranteeing complete blockage of a sensory modality, which, like the lateral line, can be distributed throughout the whole body.

A potential line of approach to explore the possibility of a complete passive form of rheotaxis is through experiments with robotic fish ( Duraisamy et al., 2019; Wang et al., 2020; Zhang et al., 2016), mimicking locomotory patterns of live animals and allowing to precisely control sensory input. In this vein, we foresee experiments with robotic fish in a complete open-loop operation that does not utilize any sensory input. The robotic fish developed in our previous study (Kopman and Porfiri, 2013; Kopman et al., 2015) could offer a versatile platform to conduct such an experiment. Such a robot is actuated by a built-in step motor to undertake a periodic tail beating with a predetermined frequency. All its electronics is encased in the frontal section of the robot, so that its size and shape can be readily adjusted though rapid prototyping.

Although free swimming experiments on the robotic fish would be ideal, practicality may suggest to constraint the streamwise and vertical location of the robot while allowing cross-stream motions and heading changes. Such a setup shall also include a load cell to measure the drag on the robot, providing an independent measure to set the tail beat frequency – similar to CFD simulations (see Appendix 2). Also, we would recommend measuring energy expenditure by the robotic fish to gain insight into the hydrodynamic costs and benefits of rheotaxis. Experimental parameters encapsulated in β, including inlet flow speed, channel width, and robot length can be all controlled, and the flow curvature at the centerline can be measured through velocimetry techniques. In the experiments, one shall track the motion of the robotic fish to score conditions in which stable rheotaxis is observed and extract other salient information, such as the frequency of cross-stream sweeping, if present.

The model predicts that increasing κ broadens the stable region, leading to more robust rheotaxis, which is in qualitative agreement with experimental observations – including experiments on animals with intact versus compromised lateral lines (see Appendix 3). The model prediction on the influence of the environment on rheotaxis, including the flow gradient and flow channel size, also parallels the literature on rheotaxis (see Appendix 3). For example, observations by Oteiza et al., 2017 suggest that increasing the flow gradient $ϵ$ enhances hydrodynamic feedback in zebrafish, resulting in improved rheotaxis.

Our analysis also indicates that wider channels should promote rheotaxis by lowering the critical speed above which swimming against the flow becomes a stable equilibrium. This mathematical finding is indirectly supported by experimental observations (see Appendix 3), and bears relevance in the design of experimental protocols for the study of rheotaxis. Confining the subject in a narrow channel will promote bidirectional hydrodynamic interactions with the walls, so that small movements of the animal will reverberate into sizeable changes in the flow physics that will mask the gradient of the background flow. Similarly, in partial alignment with experimental observations, the model predicts a lower threshold for longer fish, owing to a magnification of the hydrodynamic feedback received by a longer body (see Appendix 3). Again, we warn care in drawing comparisons due to the presence of other senses in real experiments, which are not modelled in our work.

Finally, the model anticipates the onset of periodic cross-stream sweeping, which has been studied in some experiments on fish swimming in channels without vision (Coombs et al., 2020). While there is not conclusive experimental evidence regarding the dependence of the frequency of oscillations on flow conditions, the model is in qualitative agreement with experiments by Elder and Coombs, 2015, showing a sublinear dependence on the flow speed. Therein, it is shown that the radian frequency has a weak positive tendency with respect to the flow speed for Mexican tetra swimming with or without cues from the lateral line. Above $2⁢cm⁢s^{-1}$, the animals can successfully perform rheotaxis and display sweeping oscillations at about three cycles per minute and increase to about four cycles per minute at $12⁢cm⁢s^{-1}$. These correspond to a radian frequency on the order of $0.1⁢rad⁢s^{-1}$, which is similar to what we would predict for β ranging from 100 to 101 and ρ of the order of $10^{-1}$ (recall that the time is scaled with respect to time required by the animal to traverse the channel from wall to wall in the absence of a background flow). We acknowledge that the current model does not describe contact and impact with the walls of the channel, which could be important in further detailing the onset of cross-sweeping motions that could involve stick-and-slip at the bottom of the channel (Van Trump and McHenry, 2013).

Just as other minimal models of fish swimming have helped resolve open questions on scaling laws (Gazzola et al., 2014), gait (Gazzola et al., 2015), and drag (Sánchez-Rodríguez et al., 2020), the proposed effort addresses some of the baffling aspects of rheotaxis through a transparent and intuitive treatment of bidirectional hydrodynamic interactions between fish and their surroundings. The crucial role of these bidirectional interactions hints that active manipulation of their surroundings by fish offers them a pathway to overcome sensory deprivation and sustain stable rheotaxis.

The proposed model is not free of limitations, which should be addressed in future research. The current model neglects the elasticity and inertia of the fish, which might reduce the accuracy in the prediction of rheotaxis, especially transient phenomena. Future research should refine the dipole paradigm toward a dynamic, unsteady model that accounts for added mass effects and distributed elasticity, similar to those used in the study of swimming robots (Colgate and Lynch, 2004; Sfakiotakis et al., 1999). The model could also be expanded to account for additional sensory modalities, such as vision, vestibular system, and tactile sensors on the fish body surface. We argue that pursuing any of these extensions shall require detailed experimental data, beyond what the literature can currently offer. Experiments are also needed to refine the linear hydrodynamic feedback mechanism that we hypothesized for the lateral line; in this vein, future experiments could be designed to parametrically vary the flow speed and quantify the activity level of lateral line nerve fibers through neurophysiological recordings (Mogdans, 2019). Beyond the inclusion and refinement of individual sensory modalities, we envision research toward the incorporation of a multisensory framework, as the one introduced by Coombs et al., 2020. Such a framework identifies several motorsensory integration sites in the central nervous system that could contribute to rheotaxis, thereby calling for modeling efforts at the interface of neuroscience and fluid mechanics.

Despite its limitations, the proposed minimalistic model is successful in anticipating some of the puzzling aspects of rheotaxis and points at the possibility of attaining rheotaxis in a purely passive manner, without any sensory input. Most importantly, the model brings forward a potential methodological oversight of laboratory practice in the study of rheotaxis, caused by bidirectional hydrodynamic interactions between the swimming fish and the fluid flow. To date, there is no gold standard for the selection of the size of the swimming domain, which is ultimately chosen on the basis of practical considerations, such as facilitating behavioral scoring and creating a laminar background flow. The model demonstrates that the width of the channel has a modulatory effect on the threshold speed for rheotaxis and the cross-stream swimming frequency, which challenges the comparison of different experimental studies and confounds the precise quantification of the role of individual sensory modalities on rheotaxis. Overall, our effort warrants reconsidering the behavioral phenotype of rheotaxis, by viewing fish as an invasive sensor that modifies the encompassing flow and hydrodynamically responds to it.

## Materials and methods

### Derivation of the turn rate equation for the fish dynamics

The expression for the turn rate in Equation 8 is obtained from the original finite-dipole model by Tchieu et al., 2012, in the limit of small distances between the vortices in the pair ($r_{0}→0$).

Specifically, eqution (2.11) from Tchieu et al., 2012, adapted to the case of a single dipole reads

$$
\theta˙_{f}=Re[\frac{(U(r→_{f,r})−iV(r→_{f,r}))−(U(r→_{f,l})−iV(r→_{f,l}))}{r_{0}}e^{i\theta_{f}}],
$$

where subscript $l$ and $r$ refer to the left and right vortices forming the pair and $U→=Ui^+Vj^$ is the advective velocity field acting on the dipole. The advective field consists of the interactions with the walls and the background flow, so that $U→(r→)=u→_{w}(r→,r→_{f},\theta_{f})+u→_{b}(r→)$; in the case of Tchieu et al., 2012, such a field encompasses the velocity field induced by any other dipole in the plane. Left and right vortices are defined so that $r→_{f,l}=r→_{f}+r_{0}⁢v^_{f}^{⟂}/2$ and $r→_{f,r}=r→_{f}-r_{0}⁢v^_{f}^{⟂}/2$, which yields $r→_{f,l}-r→_{f,r}=v^_{f}^{⟂}⁢r_{0}$.

By carrying out the complex algebra in Equation 11, we determine

$$
\theta˙_{f}=(\frac{−U→(r→_{f,l})+U→(r→_{f,r})}{r_{0}})⋅v^_{f},
$$

which supports the intuition that the dipole will turn counter-clockwise if the right vortex would experience a stronger velocity along the swimming direction. Upon linearizing the term in parenthesis in the neighborhood of $r→_{f}$, this expression becomes

$$
\theta˙_{f}=−∇U→(r_{f}→)v^_{f}^{⊥}⋅v^_{f}.
$$

The chosen approach is consistent from the standpoint of vortex dynamics, by which each vortex in the pair advects in response to local fluid velocity. In this vein, the fish is interpreted as a bluff body, which rotates according to a difference in the drag experienced by its left and right sides. Such a difference is amplified by the pectoral fins, which enhance the effect of any left-to-right asymmetry in the surrounding fluid flow. In the literature, this description is termed T-dipole, in opposition to the so-called A-dipole that introduces two fiducial points along the direction of motion of the dipole that govern its turning (Kanso and Cheng Hou Tsang, 2014). Whether one representation is superior to the other in terms of accuracy is yet to be clarified; our choice of using a T-dipole is based on its theoretical consistency and intuition on the underlying flow physics. Potential avenues for resolution include detailed CFD simulations of free swimming fish or experiments with robotic fish. For completeness, in Appendix 4, we report model predictions based on the A-dipole.

### Determination of the equilibria of the planar dynamical system

By setting $\theta_{f}=0$ or $\theta_{f}=\pi$ in equation set (Equation 10a, Equation 10b), we determine that ξ should be equal to some constant, which is a root of the following transcendental equation:

$$
\frac{\pi^{3}}{32}cot⁡(\pi(ξ+\frac{1}{2}))csc^{2}⁡(\pi(ξ+\frac{1}{2}))=\pm\betaξ,
$$

where the positive sign corresponds to $\theta_{f}=0$ and the negative sign to $\theta_{f}=\pi$. Here, $\beta=\alpha⁢(1+κ)/ρ^{2}$ as introduced from the main text.

As shown in Figure 5, for $\theta_{f}=0$, there is only one root of the equation ($ξ=0$; see the intersection between the solid red line and the solid black curve), while up to three roots can rise for $\theta_{f}=\pi$ depending on the value of β. For β smaller than a critical value $\beta^{*}$, only $ξ=0$ is a solution (see the intersection between the solid blue line and the solid black curve), while for $\beta>\beta^{∗}$ two additional solutions, symmetrically located with respect to the origin emerge (see the intersections between the dashed blue line and the solid black curve). The critical value $\beta^{*}$ is identified by matching the slope of the black curve at $ξ=0$, so that $\beta^{*}=\pi^{4}/32$. Notably, the two solutions symmetrically located with respect to the centerline approach the walls as $\beta→∞$.

![Figure 5.](https://cdn.elifesciences.org/articles/75225/elife-75225-fig5-v2.jpg)

**Figure 5.:** (a) Plot of the function $\frac{\pi^{3}}{32}⁢cot⁡(\pi⁢(ξ+\frac{1}{2}))⁢csc^{2}⁡(\pi⁢(ξ+\frac{1}{2}))$ (black), superimposed with three lines of different slope: 200 (red), -200 (dashed blue), and -2 (solid blue). (b) Zoomed-in view of the curves in (a) showing that the blue line can only intersect the black curve at the origin.

### Local stability analysis of the planar dynamical system

To examine the local stability of the equilibria of the planar dynamical system, we linearize equation set (Equation 10a, Equation 10b). The state matrix of the linearized dynamics, $A$, describes the local behavior of the nonlinear system when perturbed in the vicinity of the equilibrium, that is,

$$
\deltaq˙(t)=A\deltaq(t),
$$

where $\deltaq=[\deltaξ,\delta\theta_{f}]^{T}$ is the variation about the equilibrium. The eigenvalues of the $A$ are indicative of local stability about each equilibrium.

For $\theta_{f}=0$ and $ξ=0$, the state matrix is given by

$$
A=[01-\frac{\pi^{2}⁢ρ^{2}}{6}8⁢(1+κ)⁢\alpha+\frac{\pi^{4}⁢ρ^{2}}{4}0].
$$

Given that the trace of the matrix is zero ($tr⁢A=0$), the analysis of the stability of the equilibrium resorts to ensuring the sign of the determinant to be positive ($detA>0$). Specifically, if the determinant is positive, the eigenvalues are imaginary and the equilibrium is a neutral center (stable, although not asymptotically stable), otherwise one of the eigenvalues is positive and the equilibrium is a saddle point (unstable) (Bakker, 1991). Hence, stability requires that

$$
\frac{1}{24}(−6+\pi^{2}ρ^{2})(32\alpha(1+κ)+\pi^{4}ρ^{2})>0.
$$

Since the first factor is always negative ($ρ≪1$) and the second is positive, the inequality is never fulfilled and the equilibrium is a saddle point (unstable) (Figure 4(a and b)).

For $\theta_{f}=\pi$ and $ξ=0$, the state matrix is given by

$$
A=[0-1+\frac{\pi^{2}⁢ρ^{2}}{6}8⁢(1+κ)⁢\alpha-\frac{\pi^{4}⁢ρ^{2}}{4}0].
$$

Similar to the previous case, stability requires that $detA>0$, that is,

$$
\frac{1}{24}(−6+\pi^{2}ρ^{2})(−32\alpha(1+κ)+\pi^{4}ρ^{2})>0.
$$

Due to the sign change in the first summand appearing in the second factor with respect to the previous case, stability becomes possible. Specifically, the equilibrium is a neutral center (stable) for $\beta>\beta^{∗}=\pi^{4}/32$, which is also the necessary condition for the existence of the two equilibria symmetrically located with respect to the channel centerline (Figure 4(a and c)).

When $\beta>\beta^{∗}$, we register the presence of two more equilibria at $\pmξ\neq0$. The state matrix takes the form

$$
A=[0-1-\frac{\pi^{2}⁢ρ^{2}}{12}+\frac{1}{4}⁢\pi^{2}⁢ρ^{2}⁢sec^{2}⁡(\pi⁢ξ)8⁢(1+κ)⁢\alpha-\frac{1}{4}⁢\pi^{4}⁢ρ^{2}⁢(2-cos⁡(2⁢\pi⁢ξ))⁢sec^{4}⁡(\pi⁢ξ)0],
$$

Also in this case, stability requires that $detA>0$, that is,

$$
\frac{1}{48}(−12+3\pi^{2}ρ^{2}sec^{2}⁡(\piξ)−\pi^{2}ρ^{2})(−32\alpha(1+κ)+\pi^{4}ρ^{2}(2−cos⁡(2\piξ))sec^{4}⁡(\piξ))>0
$$

Once again, for $ρ≪1$, we can assume that the first factor in parenthesis is negative. (This assumption is grounded upon Equation 14, which yields that $(ξ\pm1/2)=O(ρ^{2/3})$; since $cos⁡(\piξ)^{2}=O((ξ\pm1/2)^{2})$, we have that $ρ^{2}sec^{2}⁡(\piξ)→0$ as $ρ→0$.) Hence, we obtain

$$
\beta>\frac{\pi^{4}}{32}(2−cos⁡(2\piξ))sec^{4}⁡(\piξ),
$$

which is not satisfied for any choice of $\beta>\beta^{∗}$. Thus, the two equilibria away from the channel centerline, close to the walls are always saddle points (unstable) (Figure 4(a and c)).

We comment that the local stability analysis requires only knowledge of the curvature of the flow field at the centerline of the channel. Hence, should one contemplate alternative profiles for the background flow, linear stability results shall not change. Higher-order parameterizations for the flow profile will result into nonlinear dependencies on ξ that do not affect the linear analysis. Likewise, while we considered a linear feedback mechanism to integrate lateral information via a simple gain, one may explore nonlinear relationships between λ and $Γ$. The linear stability analysis shall not change, whereby these nonlinear forms will result into dependencies on higher powers of ξ.

### Frequency of cross-stream sweeping

The linearized planar system about the stable focus in Equation 18 is equivalent to a classical second-order system in terms of the cross-stream coordinate, similar to a mass-spring model. Hence, the radian resonance frequency of the system is

$$
\omega_{0}=\sqrt{det⁡A}≃\frac{\pi^{2}}{2}⁢ρ⁢\sqrt{\frac{\beta}{\beta^{*}}-1}.
$$

where the last approximation holds for $ρ≪1$. Equation (23) shows that, close to the threshold, the frequency of oscillations is small and it increases with β and ρ.

### Estimation of model parameters

In a typical experimental setup on rheotaxis, the width of the channel, $h$, is on the order of three to ten times the body length of the animal, $l$. For example, experiments from Elder and Coombs, 2015 on Mexican tetras of $l=8.3⁢cm$ were conducted in a channel with $h=25⁢cm$. Similarly, in the experiments on adult zebrafish from Burbano-L and Porfiri, 2021, $l=3.6⁢cm$ and $h=13.8⁢cm$, and in the experiments on zebrafish larvae from Oteiza et al., 2017, $l=4.2⁢mm$ (inferred from the animals’ age) and $h=1.27$ – $4.76⁢cm$. The distance between the vortices simulating a fish, r0, should be on the order of a tail beat, which has a typical value of $0.2⁢l$(Gazzola et al., 2014). As a result, it is tenable to assume that $ρ^{2}$ is between $10^{-4}$ and $10^{-2}$.

A safe estimation of the velocity of the animal in the absence of the background flow, v0, would be on the order of few body lengths per second (Gazzola et al., 2014). The speed used for the background flow across experiments, U0, tend to be of the same order as the magnitude of v0, leaning toward values close to one body length per second (Coombs et al., 2020). For instance, data on zebrafish from Burbano-L and Porfiri, 2021 suggest $v_{0}=5.7⁢cm⁢s^{-1}$ and $U_{0}=3.2⁢cm⁢s^{-1}$. The estimation of the non-dimensional parameter $ϵ$ associated with the shear in the flow is more difficult, since data on the velocity profiles are seldom reported. That being said, for channel flow of sufficiently high Reynolds number, the velocity profile in the channel is expected to be blunt, approximating a uniform flow profile near the channel center (White, 1974). Thus, it is tenable to treat $ϵ$ as a small parameter, between 10-2 and 10-1. For flow of low Reynolds number (Oteiza et al., 2017) ($Re<100$), the velocity gradient in the channel has been observed to be large, corresponding to $ϵ$ values in the range of 10-1 and 1. By combining these estimations, we propose that α ranges between 0 and 1.

An estimation of κ is difficult to offer, whereby feedback from the lateral line has only been included in few studies (Burbano-L and Porfiri, 2021; Chicoli et al., 2015; Colvert and Kanso, 2016; Oteiza et al., 2017). Using the data-driven model from Burbano-L and Porfiri, 2021, it is tenable to assume values on the order of 101 for individuals showing high rheotactic performance. This gain can also be estimated by comparing the threshold speeds of fish, $U_{c}$, with and without the lateral line, through $\frac{U_{c}⁢(LL-)}{U_{c}⁢(LL+)}=1+κ$, according to Equation 29 in Appendix 3. The significant increase in the threshold speed following lateral line ablation in Baker and Montgomery, 1999 indicates that $κ\in[2,7]$, while the indistinguishable threshold speed between LL+ and LL- fish in a few other studies (Bak-Coleman and Coombs, 2014; Elder and Coombs, 2015; Van Trump and McHenry, 2013) may suggest that $κ∼0$. In Table 1, we summarize the model parameters identified from data in the experimental studies detailed in Appendix 3.

**Table 1.**
 Estimation of model parameters from data in the literature.


<table>
  <thead>
    <tr>
      <th>Reference</th>
      <th>ρ</th>
      <th>ϵ</th>
      <th>α</th>
      <th>κ</th>
      <th>β</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bak-Coleman et al., 2013</td>
      <td>∼0.05</td>
      <td>[10-2,10-1]</td>
      <td>[0,0.17]</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Bak-Coleman and Coombs, 2014</td>
      <td>∼0.04</td>
      <td>[10-2,10-1]</td>
      <td>[0,0.16]</td>
      <td>∼0</td>
      <td>[0,100]</td>
    </tr>
    <tr>
      <td>Baker and Montgomery, 1999 and Montgomery et al., 1997</td>
      <td>∼0.1</td>
      <td>[10-2,10-1]</td>
      <td>∗[0,0.32]</td>
      <td>[2,7]</td>
      <td>[0,256]</td>
    </tr>
    <tr>
      <td>Elder and Coombs, 2015</td>
      <td>∼0.066</td>
      <td>[10-2,10-1]</td>
      <td>∗[0,0.24]</td>
      <td>∼0</td>
      <td>[0,55]</td>
    </tr>
    <tr>
      <td>Kulpa et al., 2015</td>
      <td>∼0.04</td>
      <td>∼1 near center of jet</td>
      <td>∼1.3</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Oteiza et al., 2017</td>
      <td>[0.018,0.066]</td>
      <td>[0.20,0.82]</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Peimani et al., 2017</td>
      <td>∼0.044</td>
      <td>∼1</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Suli et al., 2012</td>
      <td>∼0.018</td>
      <td>[0.1,1]</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Van Trump and McHenry, 2013</td>
      <td>[0.055,0.127]</td>
      <td>[10-2,10-1]</td>
      <td>∗[0,0.32]</td>
      <td>∼0</td>
      <td>[0,106]</td>
    </tr>
  </tbody>
</table>

_LL+ cavefish swimming speed v0∼5cm/s in zero background flow in Bak-Coleman and Coombs, 2014 is used to estimate α._
