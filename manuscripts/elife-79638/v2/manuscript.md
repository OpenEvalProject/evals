# Dynamics of cooperative excavation in ant and robot collectives

## Authors

- S Ganga Prasath<sup>1</sup> ([ORCID: 0000-0002-4545-911X](https://orcid.org/0000-0002-4545-911X))
- Souvik Mandal<sup>2</sup> ([ORCID: 0000-0002-9552-5613](https://orcid.org/0000-0002-9552-5613))
- Fabio Giardina<sup>1</sup>
- Jordan Kennedy<sup>1</sup>
- Venkatesh N Murthy<sup>2</sup> ([ORCID: 0000-0003-2443-4252](https://orcid.org/0000-0003-2443-4252))
- L Mahadevan<sup>1</sup> ([ORCID: 0000-0002-5114-0519](https://orcid.org/0000-0002-5114-0519)) †

### Affiliations

1. School of Engineering and Applied Sciences, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
2. Department of Molecular and Cellular Biology, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
3. Center for Brain Science, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
4. Department of Physics, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
5. Department of Organismic and Evolutionary Biology, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))

† Corresponding author

## Abstract

The solution of complex problems by the collective action of simple agents in both biologically evolved and synthetically engineered systems involves cooperative action. Understanding the resulting emergent solutions requires integrating across the organismal behavior of many individuals. Here, we investigate an ecologically relevant collective task in black carpenter ants Camponotus pennsylvanicus: excavation of a soft, erodible confining corral. These ants show a transition from individual exploratory excavation at random locations to spatially localized collective exploitative excavation and escape from the corral. Agent-based simulations and a minimal continuum theory that coarse-grains over individual actions and considers their integrated influence on the environment leads to the emergence of an effective phase space of behaviors, characterized in terms of excavation strength and cooperation intensity. To test the theory over the range of both observed and predicted behaviors, we use custom-built robots (RAnts) that respond to stimuli to characterize the phase space of emergence (and failure) of cooperative excavation. Tuning the amount of cooperation between RAnts, allows us to vary the efficiency of excavation and synthetically generate the entire range of macroscopic phases predicted by our theory. Overall, our approach shows how the cooperative completion of tasks can arise from simple rules that involve the interaction of agents with a dynamically changing environment that serves as both an enabler and a modulator of behavior.

## Introduction

Collective behavior is seen in organisms across many length scales, from the microscopic to the macroscopic (Nowak, 2006; Camazine et al., 2020; Gordon, 1999; Seeley, 2009; Couzin and Krause, 2003). These behaviours are often functional and serve as solutions to problems associated with tasks that cannot be solved efficiently at the individual level and range from brood care to foraging for food, protection from enemies and predation of prey, building complex architectures etc (Feinerman et al., 2018; Ocko and Mahadevan, 2014; Hölldobler and Wilson, 2009; Peleg et al., 2018; Rasse and Deneubourg, 2001). Since collective behavior involves multiple individuals, this necessarily involves some form of communication and/or cooperation that takes different forms across scales - from quorum sensing in unicellular bacterium and slime molds, to the waggle dance in bees, and various forms of physical signal propagation in animal societies and human organizations (Rasse and Deneubourg, 2001; Alcock, 2001; Pennisi, 2009; Nowak, 2006; Elster, 1998; Couzin and Krause, 2003).

The importance of environmental signals is particularly clearly seen in examples of collective task execution in social insects that have a long history of documented cooperative behavior (Hölldobler et al., 1990; Gordon, 1999; Perna and Theraulaz, 2017; Mikheyev and Tschinkel, 2004). Super-organisms made of individuals respond to local stimuli with stereotypical actions that leave their ‘mark’ on the environment, creating a spatio-temporal memory, commonly known as stigmergy (Hölldobler and Wilson, 2009). While stigmergy is usually associated with scalar pheromone fields, a broader definition might include the use of signaling via chemical, mechanical and hydrodynamic means (Buhl et al., 2005; Mikheyev and Tschinkel, 2004), as has been quantified in recent studies of bees (Ocko and Mahadevan, 2014; Peleg et al., 2018). To understand how collective task execution arises, we need to understand how individuals switch from local uncoordinated behavior to collective cooperation that translates to successful task execution in different social systems. From a biological perspective, this naturally involves understanding the neural circuits, physiology and ethology of an individual. A complementary perspective at the level of the collective is that of characterizing a ‘crude view of the whole’, which entails the quest for a small set of rules that are sufficient for task completion, along with the range of possible solutions that arise from these rules that might be tested experimentally. And finally, given the ability to engineer minimally responsive biomimetic agents such as robots (Rahwan et al., 2019), a question that suggests itself is that of the synthesis of effective behaviors using these agents. This allows us to explore regions of phase space that are hard to explore with social insects, and also to learn about the robustness of these behaviors using imperfect agents in uncertain and noisy physical environments, before looking for them in-vivo.

Here we use an ecologically relevant task in carpenter ants Camponotus Pennsylvanicus: excavation and tunneling, to quantify the dynamics of successful task execution by tracking individual ants, create a quantitative framework that takes the form of mathematical models for agent behavior, and finally synthesize the behavior using robots that can sense and act. Our work complements and builds on earlier studies on excavation (Buhl et al., 2005; Tschinkel, 2004; Deneubourg and Franks, 1995; Deneubourg et al., 2002) in social insects that looked at the effects of population size and the role of cooperation on the efficiency of digging, while developing 1-dimensional models to understand the excavation process. We go beyond these studies by (i) quantifying the collective behavior of ants by tracking them in space-time, following the dynamics of their interaction, and the process of excavation of the confining substrate, (ii) developing a theoretical framework that couples the change in ant density, substrate density and the rate of antennation in space and time to capture the collective execution of the task in terms of a few non-dimensional parameters that define the range of behaviors of the agents, (iii) synthesizing and recreating this collective task using custom-built robots that can respond to each other and the environment . An important outcome of our study is a phase diagram that shows the emergence of different collective behaviors associated with task completion as a function of just two dimensionless parameters that characterize the local rules underlying individual behavior and the nature of communication between agents such as ants and robots.

## Materials and methods

### Excavation in carpenter ants

We start with ants drawn from a mature colony of C. Pennsylvanicus that consist of a queen, the sole egg layer, and workers from three morphologically different castes - major, median, and minor (Hansen and Klotz, 2005). Although all ants perform different tasks like foraging, nest-keeping, and brood care to varied degrees, during excavation, major ants, equipped with their large mandibles, generally take the lead role, while median and minor ants transport the debris out of the nest. Ants communicate primarily through their antennae by using them to sense pheromones released by other ants and by touching other ants to identify their caste. It is this inter-organismal information exchange that enables the collective solution of complex tasks.

Our experiments consist of a dozen worker ants from the same colony that are anesthetized (using $C⁢O_{2}$) and then brought into a confining ring-like corral made out of agarose (height 10mm, inner radius 35mm and outer radius 55mm) flanked above and below by two hard plastic sheets. To mimic their natural environment in a nest, we eliminated visible light and used infrared light to monitor the ants using video (see Figure 1(a)). We performed 4 experiments with a collective of 12 majors ants and 3 sets of experiments with a mixture of 4 major, 4 media and 4 minor ants. Once we introduce O2 into the corral, the ants regain activity but stay still for a while before moving. They first exhibit wall-following until one or more of the ants initiates an exploratory excavation at a random location along the corral (ref Figure 2). After an initial exploratory phase the ants switch to an exploitative strategy in which they excavate a tunnel at a specific location and eventually break through the corral (see Video 1 and the sequence in Figure 1(b)). In contrast with the behavior of the 12 ant collective, when a single Major ant is introduced into the arena, the ant is unable to excavate through the agar barrier (see Video 1).

![Figure 1.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig1-v2.jpg)

**Figure 1.:** (a) Colony members of the black carpenter ant Camponotus pennsylvanicus are confined to a porous boundary made out of Agarose. The boundary is represented by its radius $R⁢(ϕ,t)$ ($ϕ$ - polar angle, $t$ - time). Bottom part shows the side-view schematic of the experimental set-up with the boundary made of agarose and background IR light source used to image the ants in the dark. (b) Temporal progression of excavation experiments as 12 ants cooperatively tunnel through the agarose confinement. The white line is the tracked location of the inner wall which grows in size as the excavation progresses. (c) Confinement area $A⁢(t)$ as a function of time (scaled by time to excavate out of the corral $T$), normalized by initial circular confinement with radius $R_{o}$. (d) Evolution of the orientation distribution of the ant density, $P_{ϕ}^{a}(ϕ,t)$ obtained by averaging along the radial direction. Ants start from an initially isotropic state and localize at an angle $ϕ_{b}$ along the boundary. $T$ here is the excavation time. (e) Dynamics of the radial distribution of ant density $P_{r}^{a}(r,t)$ as a function of radial distance, $r$ obtained by averaging a sector of $\pi/6$ around the excavation site. We see that the ant density front propagates through the corral. The density is plotted for the same times as in (f) Evolution of the power spectrum $|R^⁢(k,t)|^{2}$ of first five Fourier modes capturing the number of tunnels formed during excavation $R⁢(ϕ,t)=\sum_{k}R^⁢(k,t)⁢e^{i⁢k⁢ϕ}$. Inset shows the real part of the Fourier coefficient, $ℜ⁡(R^)$ at different time instants indicating that many modes are present in the boundary shape.

We can quantify this transition from rotationally isotropic exploration to localized excavation by considering both the behavior of individual ants or their effective density $ϱ_{a}⁢(r,ϕ,t)$ as a function of the polar coordinates $(r,ϕ)$ and time t. We choose to use an effective coarse-grained density for two reasons: it is a more natural variable in the limit of large populations that vary in space and time, and is also amenable to building effective theories with fewer parameters that are easier to analyze and thus also compare to experiments. The ant density is obtained by averaging the position of the ants over a time window larger than the time taken for them to perform one task cycle , that starts with excavation at the boundary and ends with dropping debris in the interior of the corral (see Appendix 1 for further details). Over time, we see that the ant density becomes localized at a particular angle and location along the corral; here large-scale excavation eventually leads to excavation and escape from the corral (see Figure 2 and Appendix 1—figure 1 for the coarse-grained spatio-temporal evolution of the ant density, obtained by this averaging procedure). Simultaneously, collective excavation leads to an increase of the volume of excavated material, as shown in Figure 1(c) (see also Toffin et al., 2009). By averaging the ant density over radial positions, in Figure 1(d) we show the orientation distribution of the ant density $P_{ϕ}^{a}(ϕ,t)=\intϱ_{a}(r,ϕ,t)dr$ is initially isotropic, and gradually starts to localize at a particular (arbitrary) value of the angle as time increases.

![Figure 2.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig2-v2.jpg)

**Figure 2.:** Evolution of the ant density field, $ϱ_{a}⁢(x,t)$ (in units of #/mm2) as the tunneling progresses for experiments with 12 major ants.The density field is obtained by averaging the ant locations over 250 s during the tunneling process. In the second columns is the evolution of the boundary shape, $R⁢(ϕ)$ as a function of time where we see multiple excavation sites being explored before one of them succeeds. The darker spots in the image are the debris that the ants deposit as they excavate the boundary.

![Video 1.](https://cdn.elifesciences.org/articles/79638/elife-79638-video1.mp4.jpg)

**Video 1.:** $(i)$ Single ant: We confined 1 ant (major, media and minor individually) and capture their dynamics to see if they are capable of tunneling on their own; $(i⁢i)$ Multiple castes assemblage: We confined 12 ants, 4 for each of major, minor and media castes, and capture the dynamics of excavation as they tunnel through the boundary; $(i⁢i⁢i)$ Major ant collective excavation: We confined 12 major ants and capture the dynamics of excavation as they tunnel through the boundary.2.

Averaging the density over the localized region, in Figure 1(e) we show the radial distribution of the ant density $P_{r}^{a}(r,t)=\intϱ_{a}(r,ϕ,t)S(ϕ)dϕ$ (where $S⁢(ϕ)$ is a smoothing kernel localized around the excavation site) starts out by being initially uniform, and gradually propagates radially outwards as time increases. Consistent with localization and concomitant excavation (Figure 1(f) inset, Appendix 1—figure 2(c)), we see that the multiple azimuthal Fourier modes compete with each other initially before an elliptic mode (corresponding to a strongly localized state) is amplified as excavation progresses (shown in Figure 1(f), Appendix 1—figure 2(b)). All together, our quantitative observations show that an initially isotropic and homogeneous distribution of ants in the corral induces exploration of multiple potential tunneling paths that transitions into the exploitative excavation of one specific location that eventually leads to an excavation route.

### Model of cooperative excavation

In order to understand the dynamics of this cooperative excavation we first model the ants using discrete agents that mimic the microscopic behaviors of ants before turning to a coarse-grained field theoretic model for the evolution of the ant, pheromone and substrate density in space and time. In the agent-based model each ant is represented as a circular disk of radius $a$ with center position $r_{j}⁢(t)$ and orientation $p^_{j}⁢(t)$ where $j=1⁢⋯⁢n$, $n$ being the number of ants in the domain (see Figure 3(a)). We approximate the confining corral in the experiments using discrete boundary elements which the agents can pick and place in the interior of the domain (see Figure 3(b)). Initially, a random collection of agents engages in exploration within the corral in the absence of external gradients, consistent with observations (Trible et al., 2017) but their motion is rectified either by the presence of pheromone gradients or reinforcing antennating signals (Hölldobler et al., 1990; Reinhard and Srinivasan, 2009; Waters and Bassler, 2005; Gordon et al., 1993; Hillen and Painter, 2009; Toffin et al., 2009). Antennation involves information moving with the ants while pheromone gradients leads to information being laid down in the fixed environment. However, when ants move slowly relative to the time for the decay of the memory associated with antennation with other ants, the dynamics of both these processes is similar. Then the signals laid down (or transported) by ants increases locally at a rate proportional to their density (Gordon, 2021), and is subject to degradation and diffusion slowly. Accounting for these effects, we arrive at the following dynamical equations for the evolution of $r_{j}(t),\theta_{j}(t),c(x,t)$ as:

$$
r˙_{j}(t)=v_{o}p^(t)⏟Self-propulsion,
$$



$$
\theta˙_{j}=G∇_{⊥}c⏟Antennation feedback+η_{j}(t)⏟Exploration,
$$



$$
∂_{t}c=D_{c}∇^{2}c⏟Diffusion+ k_{}+\sumj=1nH(r_{j}(t);a)⏟Production−k_{−}c⏟Decay.
$$

![Figure 3.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig3-v2.jpg)

**Figure 3.:** (a) Schematic of the agents in our simulation captured by their position $r⁢(t)$ and orientation $p^⁢(t)$ moving at speed vo. These agents generate an antennating field $c⁢(x,t)$ at a constant rate $k_{}$ which decays at a rate $k_{−}$. (b) Progression of cooperative excavation of the corral by 5 agents as they pick elements from the boundary and drop them in the interior (see sec. Appendix 2—table 1 for parameters). Color bar shows the magnitude of antennating field and it varies between 0–130. (c) Snapshot of the dynamics at the end of simulations corresponding to $T_{stop}=266$ for the number of agents $n=3,13,100$. We see that agents can go from excavating successfully to being trapped in their own communication field. (d) Box plot showing the time taken to excavate out of the corral $T/t_{s}$ (non-dimensionalized using $t_{s}$ - time taken for an agent to travel the entire domain) as a function of the number of agents $n$ in the corral when $T_{stop}=266$. For very small and very large number of agents the collective does not excavate out as the median $T/t_{s}=T_{stop}$ and they escape fastest for $n=8$.

Here, the orientation of the agent in Equation 1 is given by $p^_{j}=(cos⁡\theta_{j},sin⁡\theta_{j})$ with $\theta_{j}$ being the heading angle, vo the characteristic speed of the agent, $η_{j}$ is a Gaussian white noise with correlation function $⟨η_{j}^{k}⁢(t)⁢η_{j}^{l}⁢(t^{′})=2⁢D_{a}⁢\delta_{k,l}⁢\delta⁢(t-t^{′})⟩$. The agents produce an antennating field at a rate $k_{}$ which decays at a rate $k_{-}$ centered around the agent, and captured by the function $ℋ(r_{j},a)={1$ if $|x−r_{j}|^{2}−a^{2}\leq0$, and vanishes otherwise}. We assume that the gradient in the antennating field along the local normal, on the right hand side of Equation 2, determines the rotation of the agents with  $G$ being the rotational gain. In order for the agents to initiate the excavation process, they can pick the elements from the boundary and drop them in the interior of the corral only when the local concentration of the antennating field is larger than a critical threshold $c^{*}$, consistent with observations (Gordon, 2021; Gordon et al., 1993). Figure 3(b) shows snapshots (see Video 2 for a movie of the simulations) of the agent-based simulations following Equations 1–3 showing that the agents excavate successfully out of the corral when the gradient following behavior is strong (see Appendix 2 for details). Given this, we expect the time taken to escape from the corral is a function of the number of agents. In Figure 3(c and d) we see that as we vary the number of agents from $n=1-100$ , for very small or large number of agents in the corral, the agents are unable to escape over the time of simulations, $T_{stop}$ (ref. Figure 3(c and d)), seen as saturation in the excavation time $T/t_{s}$.

![Video 2.](https://cdn.elifesciences.org/articles/79638/elife-79638-video2.mp4.jpg)

**Video 2.:** Dynamics of excavation from agent-based simulation for different number of agents ($n=1,5,10,22,100$) in the corral for parameters in tab Appendix 2—table 1 We see successful escape as well as trapped dynamics as highlighted in Figures 3 and 4.

In our agent-based simulations, we can encode the detailed behavior of individual ants and thus account for nuances and variations across the population. However, these simulations are computationally expensive as one needs to couple the dynamics of the antennating field (governed by a partial differential equation) with the motion of discrete agents while also evaluating the mutual interactions between all the agents in the corral. A complementary perspective that allows us to gain insights into the relevant parameters that govern the macroscopic dynamics of the collective is afforded by a theoretical framework that averages over the fast times and short length scale actions of the agents, considering spatial variations over scales much larger than a ‘mean-free path’ and ‘collision time’ associated with agent-agent interactions. Our effective theory attempts to couple three slowly-varying spatio-temporal fields: the ant density $ϱ_{a}⁢(x,t)$, a communication field $c⁢(x,t)$ representing antennation and pheromone-based communication, and the corral density $ϱ_{s}⁢(x,t)$, shown schematically in Figure 4(a). In the continuum picture, the agents’ random motion is captured using diffusion of the density while the rectified motion due to pheromone gradients is captured through chemotaxis, in addition to being self-propelled with a velocity $u_{a}$ that is related to the local environment. Finally, motivated by observations of antennation (Gordon, 1999; Pagliara et al., 2018), we assume that when the ants are stimulated by the presence of the corral past a threshold of antennation, $c^{*}$ they start excavating. The rate of excavation is assumed to be proportional to the difference in the pheromone concentration relative to the threshold value (see further details). Accounting for these effects, we arrive at the following dynamical equations for the evolution of $ϱ_{a}⁢(x,t)$ and $ϱ_{s}⁢(x,t)$ that are coupled to Equation 3 for the evolution of the communication field:

$$
∂_{t}ϱ_{a}=−∇⋅(u_{a}ϱ_{a})⏟Self-propulsiveadvection+ ∇⋅(D_{a}∇ϱ_{a}⏟Diffusive flux−χϱ_{a}∇c⏟Tactile feedback),
$$



$$
∂_{t}ϱ_{s}=−k_{s}ϱ_{s}{ Θ(c−c^{∗})⏟Antennatingfield threshold }\times{ Θ(ϱ_{a}−ϱ_{a}^{∗})⏟Ant densitythreshold }.
$$

In Equation 4, the ant advection velocity is assumed to have the form $u_{a}=v_{o}⁢(1-ϱ_{s}/ϱ_{o})⁢p^$ where vo is the characteristic speed of the agents, and $p^$ is a unit vector pointing along the radial ($\theta$) direction, and the term $(1-ϱ_{s}/ϱ_{o})$ reflects the fact that excavating ants are slowed down by their labor; $D_{a}$ is the diffusivity of ants, $χ$ is a chemotactic gain associated with the antennating-field-following behavior (related to the gain $G$ in the agent-based model). Here is the average density of the ants defined by where is the domain size. This is a natural scale of the ant density as Equation 4 is in conservative form and the net density of the ants is preserved over the evolution. In Equation 5, ks is the rate of excavation of the corral and $ϱ_{a}^{*},c^{*}$ are respectively the threshold concentration of ant density and antennating field required to initiate excavation. We assume that the behavioral switches have simple switch-like responses modeled here via the Heaviside function $Θ⁢(x)$ (or its regularization via hyperbolic or Hill functions). It is useful to note that in the absence of excavation dynamics, our framework reduces to the well known Keller-Segel model for chemotaxis (see Hillen and Painter, 2009 for a recent review) (also detailed in Appendix 2). The coupling of ant behavior to the dynamics of excavation introduces the all-important notion of functional collective behavior linking active agents, communication channels (the antennating and pheromone fields) and a dynamic, erodible corral that characterizes progress towards task completion.

### Model parametrization and description

The evolution of the ant density in Equation 4 is a combination of three dynamical processes: ant migration, diffusion and biased motion due to antennating. There are three time-scales associated with these three processes: a diffusion time-scale $\tau_{a}∼l^{2}/D_{a}$, a collective migration time-scale $\tau_{v}∼l/v_{o}$ and a time-scale associated with taxis  $\tau_{x}∼l^{2}/χ⁢c_{o}$, where $l$ is a characteristic length-scale. This last scale can be either the width of the corral to be excavated $L$ (which is assumed to be of same order as width of initial ant density profile la), the length-scale associated with the balance between antennating field diffusion and decay, $l∼(D_{c}/k_{-})^{1/2}$ or the length-scale due to the advection of ant density and diffusion, $l∼D_{a}/v_{o}$. The antennating field in Equation 3 is governed by three processes, the generation of the antennating field, as well as its decay and diffusion. This leads to three more time-scales : an antennating field production time-scale $\tau_{}∼c_{o}/(k_{}⁢ϱ_{o})$, a diffusion time-scale $\tau_{c}∼l^{2}/D_{c}$, and a decay time-scale $\tau_{-}∼1/k_{-}$. Lastly, the dynamics of excavation from the corral which follows Equation 5 is governed by a characteristic time-scale $\tau_{s}∼1/k_{s}$. The list of all seven time-scales and length-scales associated with the different processes in the model are in Appendix 2—table 2. In terms of the different time-scales (see Appendix 2 for a list along with their ranges), there are a total of six dimensionless parameters, of which two non-dimensional numbers are qualitatively important in capturing the etho-space of collective excavation: (i) the scaled cooperation parameter defined as $C=\tau_{a}/\tau_{x}=χ⁢c_{o}/D_{a}$ which determines the relative strength of antennation (gradient-following) to ant diffusion with co being the maximum amplitude of the antennating field, (ii) the scaled excavation rate, $E=\tau_{v}/\tau_{s}=k_{s}⁢l/v_{o}$. Here, $l/v_{o}$ is the characteristic time-scale of ant motion, with $l∼min⁢[(D_{c}/k_{-})^{1/2},l_{a}]$, where la is the ant size (see Appendix 2 for details). The other four dimensionless parameters follow from the ratio of the time scale of ant motion and the diffusive time-scale as $V=\tau_{x}/\tau_{a}=v_{o}⁢l/D_{a}$. The ratio of the rate of production of pheromone and the rate of diffusion or decay, leading to the parameters  $k^_{\pm}=\tau_{-}/\tau_{}=k_{}⁢ϱ_{o}/(k_{-}⁢c_{o})$ and $D_{c}=\tau_{-}/\tau_{c}=D_{c}/(l^{2}⁢k_{-})$ so that the complete set of non-dimensional numbers that capture the dynamics of the ant collective is given by

$$
C=\frac{χ⁢c_{o}}{D_{a}},E=\frac{k_{s}⁢l}{v_{o}},V=\frac{v_{o}⁢l}{D_{a}},k^_{\pm}=\frac{k_{}⁢ϱ_{o}}{k_{-}⁢c_{o}},D_{c}=\frac{D_{c}}{l^{2}⁢k_{-}}.
$$

In terms of these parameters, the dynamics of the ant density, the antennating field and the corral density given by Equations 3–5 can be written in non-dimensional form as

$$
∂_{t}ϱ_{a}+∇⋅[(C∇c+V(1−ϱ_{s}))ϱ_{a}]=∇^{2}ϱ_{a},
$$



$$
∂_{t}c=D_{c}∇^{2}c+k^_{\pm}ϱ_{a}−c,
$$



$$
∂_{t}ϱ_{s}=−\frac{1}{4}Eϱ_{s}(1+tanh⁡[\alpha_{c}(c−c^{∗})])\times(1+tanh⁡[\alpha_{c}(ϱ_{a}−ϱ_{a}^{∗})]).
$$

To complete the formulation of our model, we also need to specify some initial conditions and boundary conditions for the ant density, the pheromone density, and the location of the corral boundary which are detailed in the Appendix 2.

## Results

### Linear analysis

Before we consider the different limits of the phase-space defined by the non-dimensional numbers, we show that the excavation process is an instability triggered by the scaled excavation parameter $E$ in the system. Starting with the homogeneous state $ϱ_{a}^{ss}=ϱ_{a}^{∗},c^{ss}=c^{∗}=k_{+}ϱ_{o}/k_{−},ϱ_{s}^{ss}=1$ which satisfies the Equations 6–8, and perturbing about this configuration using a plane wave ansatz (in 1D) we write: ${ϱ_{a}(x,t)−ϱ_{a}^{ss},c(x,t)−c^{ss},ϱ_{s}^{ss}−ϱ_{s}(x,t)}={ϱ~_{a}(k),c~(k),ϱ~_{s}(k)}exp⁡(ikx+Ωt)$ where we assume that $||ϱ~_{a}||,||c~⁢(k)||,||ϱ~_{s}⁢(k)||≪1$. Then the linearized counterparts of the Equations 6–8 for the ant density, antennating field and the corral density read as: $(Ωk^{2})ϱ~_{a}+ikVϱ~_{s}ϱ_{o}=k^{2}Cc~$ ,: $c~=k^_{\pm}ϱ~_{a}/(Ω+1+D_{c}k^{2})$,  $Ω⁢ϱ~_{s}=-E⁢ϱ~_{s}/2$. From this, we see that the growth rate $Ω=-E/2$, is independent of all other parameters in the system, i.e. excavating begins when $E>0$, once the ants have created a sufficiently large spatially diffuse antennating field. To understand the dynamics of excavation of the corral and the different phases of collective behavior, we now explore the role of the other non-dimensional numbers.

### Limits of phase-space

Next we discuss the different limits of the phase-space defined by the non-dimensional numbers ${C,E,V,k^_{\pm},D_{c}}$ and the thresholds $ϱ_{a}^{*},c^{*}$.

#### Small thresholds, when ϱ*≪ϱo and c*≪co

When $ϱ_{a}^{*}≪ϱ_{o}$ and $c^{*}≪c_{o}$, we see the appearance of partial tunneling even with an initially inhomogeneous ant density $ϱ_{a}$, independent of the pheromone dynamics. However, depending on on the value of the ratio $\tau_{s}/\tau_{v}$, the ants can either excavate through the corral completely ($\tau_{v}/\tau_{s}≪1$) or partially ($\tau_{v}/\tau_{s}\leq1$) (ref Appendix 2—table 3). If the ants are moving randomly, i.e. in the diffusion-dominated regime, they can still tunnel through the corral if $\tau_{c}∼\tau_{s}$ and partial tunnel through the corral if $\tau_{c}≲\tau_{s}$. In non-dimensional terms, this translates to the relations  $V∼O(1),C≪1$ or $V,C≪1$ and $E∼O(1)$ for the corral evolution. (Appendix 2—figure 1 shows the results of simulations of both the tunneling and the partial tunneling behavioral phases).

#### Cooperation dominated regimes when C≫1 and E, V→0

For efficient excavation, the ants need to work collectively by being localized and excavating fast. Spatial localization leads to cooperation via feedback from the antennating field (see Figure 4(b)) while for successful excavation, ants need to migrate towards the corral and tunnel through it, so that their effective speed vo needs to be non-zero. To quantify these behaviors, we first look at the dynamics of the ant density and the antennating field in the absence of migration i.e. $V→0$ or corral evolution. This leads to three regimes:

$$
−D_{c}∇^{2}c= k_{}ϱ_{a},
$$

$$
∂_{t}ϱ_{a}+χ∇⋅(ϱ_{a}∇_{c})=D_{a}∇_{ϱ_{a}}^{2}.
$$

$$
∂_{t}ϱ_{a}+\frac{χk_{}}{k_{−}}∇⋅(ϱ_{a}∇ϱ_{a})= D_{a}∇^{2}ϱ_{a}.
$$

To understand the balance between diffusion of the antennating field and its decay,  we note the appearance of a natural length scale $l∼(D_{c}/k_{−})^{1/2}$ which defines the zone of influence of the field and provides a measure of the non-dimensional tunneling rate indicated in Figure 8. All together, our analysis shows that the dynamics of the antennating field controls the aggregation or diffusion of ant density. But for efficient excavation, especially when the activation thresholds for excavation and localization $ϱ_{a}^{*},c^{*}$ are large, we need both cooperation and finite velocity of migration. A catalog of the various regimes associated with partial tunneling, jamming, or diffusion as the dimensionless problem parameters are varied is listed in Appendix 2—table 3.

To understand how these different limits translate to the dynamics of excavation from the corral induced by the ants, we now consider the case when $E, V\neq0$, and solve the governing Equations 4; 5 in a one-dimensional setting (ref Appendix 2). We see that we can capture the two limits of the excavation behavior seen in experiments; for large excavation rates $E>1$ and cooperation parameter, $C>1$, we see coordinated excavation (shown in Figure 4(b) and Figure 5 in a two-dimensional setting), while decreasing the cooperation parameter leads to disorganized excavation (shown in Figure 4(c)) (see Appendix 2—figure 1). While a direct comparison with the behavior of ants is not easy owing to the difficulty of inferring the dynamics of information transfer through antennation, the minimal assumptions we have made about the antennating field dynamics suffice to capture the macroscopic behavior of the collective. All together, our agent-based model and the phase-field model shows the emergence of cooperativity without the need for a plan, optimization principle, or internal representations of the world; instead environmentally mediated communication between agents (Mataric, 1993) coupled to local behavioral rules suffice to realize robust excavation.

![Figure 4.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig4-v2.jpg)

**Figure 4.:** (a) Schematic of the model showing the interaction between the different spatio-temporal fields required to capture cooperative excavation of ants: ant density, $ϱ_{a}⁢(x,t)$; concentration of antennating field, $c⁢(x,t)$ capturing inter-ant communication; density of corral, $ϱ_{s}⁢(x,t)$ representing the soft corral which the ants excavate. We capture the dynamics of excavation by ants close to the excavation site using the one-dimensional version of Equations 3–5. (b, c) Temporal progression of the corral density, antennating field and the ant density showing successful excavation for high cooperation captured using the non-dimensional number, C (representing non-dimensional strength of cooperation amongst ants) and faster excavation, captured using E. For reduced cooperation ants’ diffusion dominates and only partial tunnels are formed (see Appendix 2 for details). $T$ here is the time for excavating out of the corral. The agent density is a gaussian function centered around $x=0.5$.

![Figure 5.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig5-v2.jpg)

**Figure 5.:** Two dimensional simulations showing the evolution of the ant density $ϱ_{a}$, antennating field $c$ and the corral density $ϱ_{s}$ by evolving Equations 3–5, capturing successful tunneling for non-dimensional numbers $C=0.8,E=1.44$ and time of simulation $T=20.0$.The list of dimensional parameters used in the simulation are indicated in the Appendix 1—figure 1(f). Radius of the outer boundary, $R_{o}$ is 5 non-dimensional units and the inner boundary is $R_{i}=2.5$ (see Appendix 2 for details). Color bar shows the magnitude of different variables and they vary between 0 and 1.

### Robotic collective excavation

Although our quantitative observations of the collective behavior of the ants is qualitatively captured by both our agent-based and continuum models, a natural question we can ask is whether the coarse-grained averaging over of the communication field affects the emergence of the task in experiments, especially since we are unable to measure or directly control the microscopic behaviors of the ants. To go beyond our ability to explain the observations of ant behavior using our theoretical framework, we asked if we might be able to recreate the behavior in artificially engineered mimics, and probe a larger range of the parameters and phase-space spanned by the scaled excavation and cooperation parameters $C,E$, than our experiments allowed us to - see Table 1 for a list of the relevant variables across ants, models and robots Figure 5.

**Table 1.**
 List of relevant variables and basic behaviors, for ant experiments, theoretical models and robotic implementation.


<table>
  <thead>
    <tr>
      <th>Ants</th>
      <th>Theoretical model</th>
      <th>Robots</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Discrete ants</td>
      <td>Ant density,ϱa⁢(x,t)</td>
      <td>Discrete robots</td>
    </tr>
    <tr>
      <td>Antennae communication</td>
      <td>Communication field,c⁢(x,t)</td>
      <td>Photormone field</td>
    </tr>
    <tr>
      <td>Agarose corral</td>
      <td>Substrate density,ϱs⁢(x,t)</td>
      <td>Boundary elements</td>
    </tr>
    <tr>
      <td>Motility</td>
      <td>Self-propulsive advection,ua</td>
      <td>Mobile agents</td>
    </tr>
    <tr>
      <td>Exploratory behavior</td>
      <td>Density diffusion,Da⁢∇⁡ϱa</td>
      <td>Random walk</td>
    </tr>
    <tr>
      <td>Tactile feedback</td>
      <td>Antennating field taxis,χ⁢ϱa⁢∇⁡c</td>
      <td>Phototaxis</td>
    </tr>
    <tr>
      <td>Biting behavior</td>
      <td>Excavation rate, ks</td>
      <td>Collection and deposition</td>
    </tr>
    <tr>
      <td>Neural control</td>
      <td>Dynamics of ant density</td>
      <td>Behavioral rules</td>
    </tr>
  </tbody>
</table>

For this, we turn to a robotic platform to synthesize collective functional behaviors that arise from simple behavioral rules underlying individual programmable robots. Our custom designed robot ants (RAnts) are inspired by many earlier attempts to create artificial agents that are mobile and follow simple rules (Braitenberg, 1986; Brooks, 1991; Simon, 1996), can respond to virtual pheromone fields (Sugawara et al., 2004; Garnier et al., 2007) and are capable of robotic excavation (Aguilar et al., 2018). Our autonomous wheeled robots can exhibit emergent embodied behavior (Bricard et al., 2013), and are flexible enough to allow for a range of stigmergic interactions with the environment (Werfel et al., 2014; Petersen et al., 2019). This is made possible by having each RAnt equipped with an infrared distance sensor to detect obstacles and other RAnts, a retractable magnet that can pick up and drop wall elements with a ferromagnetic ring (shown in Figure 6(a)), and the ability to measure a virtual pheromone field generated by a light projected (from below) onto the surface of a transparent arena they operate in (see Figure 6(a, b), Theraulaz and Bonabeau, 1995; Sugawara et al., 2004; Garnier et al., 2007; Wang et al., 2021). The intensity of this ‘photormone’ field follows the antennating field Equation 2 and thus follows the dynamics of a field that is linked to the locations of the RAnts and diffuses and decays away from it. The photormone field is realized by a projected luminous field on the arena, which the robots can sense. This allows us to use a local form of Equations 4; 5 to define a robot’s behavior in terms of an excavation rate E, a cooperation parameter C, and a threshold concentration for tunneling $c^{*}$. This is encoded in the behavior-based rules (see Figure 6(c) and Appendix 3 for more details), that induces the following behavior: $(i)$ follow gradient of projected photormone field; $(i⁢i)$ avoid obstacles and other RAnts at higher photormone locations; $(i⁢i⁢i)$ pick up obstacles from high photormone locations and drop them at low concentration levels. Since the robots have no symbolic representation of the different signals they sense (e.g. they cannot distinguish another RAnt from a wall element, since both merely produce a bump in the sensor signal), the observed behavior emerges from this simple sequence by depending on the current state of the environment and the robot.

![Figure 6.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig6-v2.jpg)

**Figure 6.:** (a) Robot Ant (RAnt) set-up. A mobile RAnt is placed in an arena 50 cm in diameter surrounded by three layers of cylindrical boundary elements totalling 200 elements. The outermost layer is prevented from being pushed out of the arena by a circular ring. A scalar concentration field (photormone field) is projected onto a plane whose intensity can be measured by a RAnt. The position of each RAnt is tracked using a webcam. Each RAnt can pick up and drop the discrete boundary elements using a retractable magnet. (b) Series of snapshots at different times of the excavation process for a cooperation parameter C=1. (c) Flowchart of the RAnt programming. A base locomotion speed vb is stored internally and the rate of change $Ω$ of the heading is a function of the cooperation parameter C, the photormone concentration $c$, and a stochastic process $W$ (Brownian motion). A photormone threshold $c^{*}$ determines whether an object is grasped (with probability E) after it is detected by the distance sensor. (d) Orientation distribution of the RAnt density $P_{ϕ}^{r}(ϕ,t)$ as a function of the azimuthal position $ϕ$ is the orientation of the excavated tunnel. The density is plotted for different times. (e) Radial distribution of the RAnt density $P_{r}^{r}(r,t)$ within a sector of $\pi/2$ centered around the position of the excavated tunnel as a function of distance from the center of the arena $r$. The density is plotted for the same times as in (d). (f) Confinement area $A⁢(t)$ as a function of time, normalized by initial circular confinement with radius $R_{o}$ for different cooperation parameter C. (g) Normalized excavation time $T$ as a function of cooperation parameter C, averaged over 5 experiments per cooperation parameter. Every experiment was run until the first RAnt excavated out or the experiment duration exceeded 15 min.

Varying the parameter $C\in[0,1]$ allows us to tune the individual behavior from random motion ($C=0$) to tracking the photormone gradient ($C=1$) (see Video 3). Varying the non-dimensional excavation rate $E$ changes the frequency at which the robots execute pick-and-drop behavior with detected objects, and serves to mimic what arises in ants as a function of their morphology and caste (see Appendix 1 for more details). For specific values of these parameters, we followed the collective behavior of RAnts by averaging their position over several pick-and-drop timescales to obtain the RAnt density field $ϱ_{r}⁢(r,ϕ,t)$, just as for ants. When all the RAnts are programmed to have a cooperation parameter $C=1$, RAnts initially explore the region without picking the boundary element until the photormone concentration $c∼c^{*}$, which happens once a particular location has enough visits by other RAnts. Just as for ants, we calculate the radially averaged RAnt density $P_{ϕ}^{r}(ϕ,t)=\intϱ_{r}(r,ϕ,t)dr$; Figure 6(d) shows how RAnt density localizes at a (random) value of the azimuthal angle. As excavation progresses, the RAnt density propagates radially outwards as a density front just as in ants, shown in Figure 6(e) in terms of the quantity $P_{r}^{r}(r,t)=\intϱ_{r}(r,ϕ,t)dϕ$ (also shown in Figure 7 for different trails when $C=1$). Concommitantly, as excavation progresses, the corral area increases (Toffin et al., 2009); interestingly the scaled corral area $A⁢(t)/\pi⁢R_{0}^{2}$ is independent of the cooperation parameter $C$ as shown in Figure 6(f) (all RAnts were programmed to have the same excavation rate).

![Video 3.](https://cdn.elifesciences.org/articles/79638/elife-79638-video3.mp4.jpg)

**Video 3.:** $(i)$ Dynamics of excavation by RAnts as they cooperatively tunnel through the corral for $C=1$ and without cooperation, $C=0$; $(i⁢i)$ Jammed phase: When the pick-and-place in RAnts is deactivated (corresponding to $E=0$), they get jammed for $C=1$; Diffused phase: When the pick-and-place in RAnts is deactivated and the RAnts do not follow the antennating field (corresponding to $C=0$), they diffuse around.3.

![Figure 7.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig7-v2.jpg)

**Figure 7.:** Ultimate distribution of boundary elements and averaged RAnt density field (in units of #/cm2) over the full duration of experiments for different trials.

![Video 4.](https://cdn.elifesciences.org/articles/79638/elife-79638-video4.mp4.jpg)

However, cooperation does change the time for excavation; in Figure 6(g) we show the average excavation time (scaled by the characteristic time it takes for a rant to traverse the arena) and see that $T/t_{s}$ decreases with an increase in the cooperation parameter $C$. RAnts excavated out every time for $C>0.5$, but are unable to complete excavation for low values of the cooperation parameter (within a 15-min time window). Our results show that it is the localized collective excavation of RAnts mediated by photormone-induced cooperation that is responsible for efficient tunneling and excavation; for low values of $C$, tunneling is defocused and global, and thus not as effective (see Appendix 3—figure 2). When $E→0$ (vanishing probability for a successful pick up) but $C$ is large(see Figure 8 and Appendix 2 for theoretical predictions), the RAnts get jammed because they follow the photormone field they generate but are unable to tunnel through the boundary constriction. On the other hand, when $E$ <1 and $C$<1 the agents do not cooperate and their diffusive behavior prevents successful tunneling. The range of strategies can be visualized in a two-dimensional phase space spanned by the variables $E$ and $C$ shown in Figure 8. Low values of $C$ and $E$ lead to diffusive (and non-functional) behavior, while high values of these variables lead to coordinated excavation, with the other two quadrants corresponding to jammed states (large $C$, small $E$) and partially tunneled states (large $E$, small $C$). Interestingly, these states are also observed as transients in our ant experiments, for example in the initially diffused state that is characterized by random motion inside the corral, when transiently jammed states and partial tunneling occur (see Videos 1 and 4).

![Figure 8.](https://cdn.elifesciences.org/articles/79638/elife-79638-fig8-v2.jpg)

**Figure 8.:** In the robotic experiments we tune the Cooperation parameter C and the Excavation rate E while in the ant experiments we change the caste mixture. In the ant experiments we see the jammed and diffused phases transiently before the ants relax to cooperative excavation.

## Discussion

Our analysis of collective behavior in a functional task, excavation, uses quantitative observations of ants to build theoretical and computational models to explain them, and recreate these behaviors using a swarm robotic system (see Video 4 for a summary). Our simple dynamical models involving individual agents as well as an effective continuum theory provide a phase diagram that shows how the transition from an individually exploratory strategy to an exploitative cooperative solution is mediated by the local chemical and mechanical environment. Our study suggested algorithms that we then deployed in an engineered system of robots that individually follow a minimal set of behavioral rules that mould the environment and are modulated by it.; the malleable environment serves both as a spatial memory as well as a computational platform (using the spatio-temporal photormone field and the corral). Our simulations of agent-based models and robotic experiments further suggest that a coarse-grained framework linking behavior, communication and a modulated environment is relatively robust to failure of and stochasticity in the behavior of individual agents (i.e. variations in initial conditions and number of agents), in the communication channels and in the corral geometry, in contrast to engineering approaches that aim to control all agents and optimize costs.

Different strategies such as collective excavation, jamming, and diffusion then arise as a function of the relative strength of the cooperation (representing the ability to follow gradients and detect threshold values) and excavation parameters (representing the ability to move material), as manifested in a phase diagram, and the emergence of cooperation arises due to the relatively slow decay of an environmental signal (the pheromone/antennating/photormone field), coupled to a threshold excavation rate. Since the ability to solve complex eco-physiological problems such as collective excavation is directly correlated with a selective (functional) advantage in an evolutionary setting, perhaps collective behavior must always be studied in a functional context.
