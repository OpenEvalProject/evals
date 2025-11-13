# Nonlinear transient amplification in recurrent neural networks with short-term plasticity

## Authors

- Yue Kris Wu<sup>1</sup> ([ORCID: 0000-0002-9804-2537](https://orcid.org/0000-0002-9804-2537))
- Friedemann Zenke<sup>1</sup> ([ORCID: 0000-0003-1883-644X](https://orcid.org/0000-0003-1883-644X)) †

### Affiliations

1. Friedrich Miescher Institute for Biomedical Research Basel Switzerland
2. Faculty of Natural Sciences, University of Basel Basel Switzerland
3. Max Planck Institute for Brain Research Frankfurt Germany
4. School of Life Sciences, Technical University of Munich Freising Germany

† Corresponding author

## Abstract

To rapidly process information, neural circuits have to amplify specific activity patterns transiently. How the brain performs this nonlinear operation remains elusive. Hebbian assemblies are one possibility whereby strong recurrent excitatory connections boost neuronal activity. However, such Hebbian amplification is often associated with dynamical slowing of network dynamics, non-transient attractor states, and pathological run-away activity. Feedback inhibition can alleviate these effects but typically linearizes responses and reduces amplification gain. Here, we study nonlinear transient amplification (NTA), a plausible alternative mechanism that reconciles strong recurrent excitation with rapid amplification while avoiding the above issues. NTA has two distinct temporal phases. Initially, positive feedback excitation selectively amplifies inputs that exceed a critical threshold. Subsequently, short-term plasticity quenches the run-away dynamics into an inhibition-stabilized network state. By characterizing NTA in supralinear network models, we establish that the resulting onset transients are stimulus selective and well-suited for speedy information processing. Further, we find that excitatory-inhibitory co-tuning widens the parameter regime in which NTA is possible in the absence of persistent activity. In summary, NTA provides a parsimonious explanation for how excitatory-inhibitory co-tuning and short-term plasticity collaborate in recurrent networks to achieve transient amplification.

## Introduction

Perception in the brain is reliable and strikingly fast. Recognizing a familiar face or locating an animal in a picture only takes a split second (Thorpe et al., 1996). This pace of processing is truly remarkable since it involves several recurrently connected brain areas each of which has to selectively amplify or suppress specific signals before propagating them further. This processing is mediated through circuits with several intriguing properties. First, excitatory-inhibitory (EI) currents into individual neurons are commonly correlated in time and co-tuned in stimulus space (Wehr and Zador, 2003; Froemke et al., 2007; Okun and Lampl, 2008; Hennequin et al., 2017; Rupprecht and Friedrich, 2018; Znamenskiy et al., 2018). Second, neural responses to stimulation are shaped through diverse forms of short-term plasticity (STP) (Tsodyks and Markram, 1997; Markram et al., 1998; Zucker and Regehr, 2002; Pala and Petersen, 2015). Finally, mounting evidence suggests that amplification rests on neuronal ensembles with strong recurrent excitation (Marshel et al., 2019; Peron et al., 2020), whereby excitatory neurons with similar tuning preferentially form reciprocal connections (Ko et al., 2011; Cossell et al., 2015). Such predominantly symmetric connectivity between excitatory cells is consistent with the notion of Hebbian cell assemblies (Hebb, 1949), which are considered an essential component of neural circuits and the putative basis of associative memory (Harris, 2005; Josselyn and Tonegawa, 2020). Computationally, Hebbian cell assemblies can amplify specific activity patterns through positive feedback, also referred to as Hebbian amplification. Based on these principles, several studies have shown that Hebbian amplification can drive persistent activity that outlasts a preceding stimulus (Hopfield, 1982; Amit and Brunel, 1997; Yakovlev et al., 1998; Wong and Wang, 2006; Zenke et al., 2015; Gillary et al., 2017), comparable to selective delay activity observed in the prefrontal cortex when animals are engaged in working memory tasks (Funahashi et al., 1989; Romo et al., 1999).

However, in most brain areas, evoked responses are transient and sensory neurons typically exhibit pronounced stimulus onset responses, after which the circuit dynamics settle into a low-activity steady-state even when the stimulus is still present (DeWeese et al., 2003; Mazor and Laurent, 2005; Bolding and Franks, 2018). Preventing run-away excitation and multi-stable attractor dynamics in recurrent networks requires powerful and often finely tuned feedback inhibition resulting in EI balance (Amit and Brunel, 1997; Compte et al., 2000; Litwin-Kumar and Doiron, 2012; Ponce-Alvarez et al., 2013; Mazzucato et al., 2019), However, strong feedback inhibition tends to linearize steady-state activity (van Vreeswijk and Sompolinsky, 1996; Baker et al., 2020). Murphy and Miller, 2009 proposed balanced amplification which reconciles transient amplification with strong recurrent excitation by tightly balancing recurrent excitation with strong feedback inhibition (Goldman, 2009; Hennequin et al., 2012; Hennequin et al., 2014; Bondanelli and Ostojic, 2020; Gillett et al., 2020). Importantly, balanced amplification was formulated for linear network models of excitatory and inhibitory neurons. Due to linearity, it intrinsically lacks the ability to nonlinearly amplify stimuli which limits its capabilities for pattern completion and pattern separation. Further, how balanced amplification relates to nonlinear neuronal activation functions and nonlinear synaptic transmission as, for instance, mediated by STP (Tsodyks and Markram, 1997; Markram et al., 1998; Zucker and Regehr, 2002; Pala and Petersen, 2015), remains elusive. This begs the question of whether there are alternative nonlinear amplification mechanisms and how they relate to existing theories of recurrent neural network processing.

Here, we address this question by studying an alternative mechanism for the emergence of transient dynamics that relies on recurrent excitation, supralinear neuronal activation functions, and STP. Specifically, we build on the notion of ensemble synchronization in recurrent networks with STP (Loebel and Tsodyks, 2002; Loebel et al., 2007) and study this phenomenon in analytically tractable network models with rectified quadratic activation functions (Ahmadian et al., 2013; Rubin et al., 2015; Hennequin et al., 2018; Kraynyukova and Tchumatchenko, 2018) and STP. We first characterize the conditions under which individual neuronal ensembles with supralinear activation functions and recurrent excitatory connectivity succumb to explosive run-away activity in response to external stimulation. We then show how STP effectively mitigates this instability by re-stabilizing ensemble dynamics in an inhibition-stabilized network (ISN) state, but only after generating a pronounced stimulus-triggered onset transient. We call this mechanism NTA and show that it yields selective onset responses that carry more relevant stimulus information than the subsequent steady-state. Finally, we characterize the functional benefits of inhibitory co-tuning, a feature that is widely observed in the brain (Wehr and Zador, 2003; Froemke et al., 2007; Okun and Lampl, 2008; Rupprecht and Friedrich, 2018) and readily emerges in computational models endowed with activity-dependent plasticity of inhibitory synapses (Vogels et al., 2011). We find that co-tuning prevents persistent attractor states but does not preclude NTA from occurring. Importantly, NTA purports that, following transient amplification, neuronal ensembles settle into a stable ISN state, consistent with recent studies suggesting that inhibition stabilization is a ubiquitous feature of cortical networks (Sanzeni et al., 2020). In summary, our work indicates that NTA is ideally suited to amplify stimuli rapidly through the interaction of strong recurrent excitation with STP.

## Results

To understand the emergence of transient responses in recurrent neural networks, we studied rate-based population models with a supralinear, power law input-output function (Figure 1A and B; Ahmadian et al., 2013; Hennequin et al., 2018), which captures essential aspects of neuronal activation (Priebe et al., 2004), while also being analytically tractable. We first considered an isolated neuronal ensemble consisting of one excitatory (E) and one inhibitory (I) population (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig1-v2.jpg)

**Figure 1.:** (A) Schematic of the recurrent ensemble model consisting of an excitatory (blue) and an inhibitory population (red). (B) Supralinear input-output function given by a rectified power law with exponent $\alpha=2$. (C) Firing rates of the excitatory (blue) and inhibitory population (red) in response to external stimulation during the interval from 2 to 4  s (gray bar). The stimulation was implemented by temporarily increasing the input $g_{E}$. (D) Phase portrait of the system before stimulation (left; C orange) and during stimulation (right; C green). (E) Characteristic function $F⁢(z)$ for varying input strength $g_{E}$. Note that the function loses its zero crossings, which correspond to fixed points of the system for increasing external input. (F) Heat map showing the evoked firing rate of the excitatory population for different parameter combinations $J_{E⁢E}$ and $g_{E}$. The gray region corresponds to the parameter regime with unstable dynamics.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Characteristic function $F⁢(z)$ for different inputs $g_{E}$ and $g_{I}$. (B) Firing rates of the excitatory (blue) and inhibitory population (red) in response to stimulation from 2 to 4  s (gray bar). During stimulation $g_{E}$ and $g_{I}$ are simultaneously changed to the stated values.

The dynamics of this network are given by

$$
\tau_{E}⁢\frac{d⁢r_{E}}{d⁢t}=-r_{E}+[J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+g_{E}]_{+}^{\alpha_{E}} ,
$$



$$
\tau_{I}⁢\frac{d⁢r_{I}}{d⁢t}=-r_{I}+[J_{I⁢E}⁢r_{E}-J_{I⁢I}⁢r_{I}+g_{I}]_{+}^{\alpha_{I}} ,
$$

where $r_{E}$ and $r_{I}$ are the firing rates of the excitatory and inhibitory population, $\tau_{E}$ and $\tau_{I}$ represent the corresponding time constants, $J_{X⁢Y}$ denotes the synaptic strength from the population $Y$ to the population $X$, where  $X,Y\in{E,I}$, $g_{E}$ and $g_{I}$ are the external inputs to the respective populations. Finally, $\alpha_{E}$ and $\alpha_{I}$, the exponents of the respective input-output functions, are fixed at two unless mentioned otherwise. For ease of notation, we further define the weight matrix $J$ of the compound system as follows:

$$
J=[J_{EE}−J_{EI}J_{IE} −J_{II}].
$$

We were specifically interested in networks with strong recurrent excitation that can generate positive feedback dynamics in response to external inputs $g_{E}$. Therefore, we studied networks with

$$
det(J)=−J_{EE}J_{II}+J_{IE}J_{EI}<0.
$$

In contrast, networks in which recurrent excitation is met by strong feedback inhibition such that $det(J)>0$ are unable to generate positive feedback dynamics provided that inhibition is fast enough (Ahmadian et al., 2013). Importantly, we assumed that most inhibition originates from recurrent connections (Franks et al., 2011; Large et al., 2016) and, hence, we kept the input to the inhibitory population $g_{I}$ fixed unless mentioned otherwise.

### Nonlinear amplification of inputs above a critical threshold

We initialized the network in a stable low-activity state in the absence of external stimulation, consistent with spontaneous activity in cortical networks (Figure 1C). However, an input $g_{E}$ of sufficient strength, destabilized the network (Figure 1C). Importantly, this behavior is distinct from linear network models in which the network stability is independent of inputs (Materials and methods). The transition from stable to unstable dynamics can be understood by examining the phase portrait of the system (Figure 1D). Before stimulation, the system has a stable and an unstable fixed point (Figure 1D, left). However, both fixed points disappear for an input $g_{E}$ above a critical stimulus strength (Figure 1D, right).

To further understand the system’s bifurcation structure, we consider the characteristic function

$$
F(z)=J_{EE}[z]_{+}^{\alpha_{E}}−J_{EI}[det(J)⋅J_{EI}^{−1}[z]_{+}^{\alpha_{E}}+J_{EI}^{−1}J_{II}z−J_{EI}^{−1}J_{II}g_{E}+g_{I}]_{+}^{\alpha_{I}}−z+g_{E},
$$

where $z$ denotes the total current into the excitatory population and $det(J)$ represents the determinant of the weight matrix (Kraynyukova and Tchumatchenko, 2018; Materials and methods). The characteristic function reduces the original two-dimensional system to one dimension, whereby the zero crossings of the characteristic function correspond to the fixed points of the original system (Eq. (1)-(2)). We use this correspondence to visualize how the fixed points of the system change with the input $g_{E}$. Increasing $g_{E}$ shifts $F⁢(z)$ upwards, which eventually leads to all zero crossings disappearing and the ensuing unstable dynamics (Figure 1E; Materials and methods). Importantly, for any weight matrix $J$ with negative determinant, there exists a critical input $g_{E}$ at which all fixed points disappear (Materials and methods). While for weak recurrent E-to-E connection strength $J_{E⁢E}$, the transition from stable dynamics to unstable is gradual, in that it happens at higher firing rates (Figure 1F), it becomes more abrupt for stronger $J_{E⁢E}$. Thus, our analysis demonstrates that individual neuronal ensembles with negative determinant $det(J)$ nonlinearly amplify inputs above a critical threshold by switching from initially stable to unstable dynamics.

### Short-term plasticity, but not spike-frequency adaptation, can re-stabilize ensemble dynamics

Since unstable dynamics are not observed in neurobiology, we wondered whether neuronal spike frequency adaptation (SFA) or STP could re-stabilize the ensemble dynamics while keeping the nonlinear amplification character of the system. Specifically, we considered SFA of excitatory neurons, E-to-E short-term depression (STD), and E-to-I short-term facilitation (STF). We focused on these particular mechanisms because they are ubiquitously observed in the brain. Most pyramidal cells exhibit SFA (Barkai and Hasselmo, 1994) and most synapses show some form of STP (Markram et al., 1998; Zucker and Regehr, 2002; Pala and Petersen, 2015). Moreover, the time scales of these mechanisms are well-matched to typical timescales of perception, ranging from milliseconds to seconds (Tsodyks and Markram, 1997; Fairhall et al., 2001; Pozzorini et al., 2013).

When we simulated our model with SFA (Eqs. (21)–(23)), we observed different network behaviors depending on the adaptation strength. When adaptation strength was weak, SFA was unable to stabilize run-away excitation (Figure 2A; Materials and methods). Increasing the adaptation strength eventually prevented run-away excitation, but to give way to oscillatory ensemble activity (Figure 2—figure supplement 1). Finally, we confirmed analytically that SFA cannot stabilize excitatory run-away dynamics at a stable fixed point (Materials and methods). In particular, while the input is present, strong SFA creates a stable limit cycle with associated oscillatory ensemble activity (Figure 2—figure supplement 1; Materials and methods), which was also shown in previous modeling studies (van Vreeswijk and Hansel, 2001), but is not typically observed in sensory systems (DeWeese et al., 2003; Rupprecht and Friedrich, 2018).

![Figure 2.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-v2.jpg)

**Figure 2.:** (A) Firing rates of the excitatory (blue) and inhibitory population (red) in the presence of spike-frequency adaptation (SFA). During stimulation (gray bar) additional input is injected into the excitatory population. The inset shows a cartoon of how SFA affects spiking neuronal dynamics in response to a step current input. (B) Left: Same as (A) but in the presence of E-to-E short-term depression (STD). Right: Same as left but inactivating inhibition in the period marked in purple. (C) 3D plot of the excitatory activity $r_{E}$, inhibitory activity $r_{I}$, and the STD variable $x$ of the network in B left. The orange and green points mark the fixed points before/after and during stimulation. (D) Characteristic function $F⁢(z)$ in networks with E-to-E STD. Different brightness levels correspond to different time points in B left. (E) Same as (B) but in the presence of E-to-I short-term facilitation (STF). (F) Inhibition-stabilized network (ISN) index, which corresponds to the largest real part of the eigenvalues of the Jacobian matrix of the E-E subnetwork with STD, as a function of time for the network with E-to-E STD in B left. For values above zero (dashed line), the ensemble is an ISN. (G) Analytical solution of non-ISN (magenta), ISN (green), paradoxical, and non-paradoxical regions for different parameter combinations $J_{E⁢E}$ and the STD variable $x$. The solid line separates the non-ISN and ISN regions, whereas the dashed line separates the non-paradoxical and paradoxical regions. (H) The normalized firing rates of the excitatory (blue) and inhibitory population (red) when injecting additional excitatory current into the inhibitory population before stimulation (left; orange bar in B), and during stimulation (right; green bar in B). Initially, the ensemble is in the non-ISN regime and injecting excitatory current into the inhibitory population increases its firing rate. During stimulation, however, the ensemble is an ISN. In this case, excitatory current injection into the inhibitory population results in a reduction of its firing rate, also known as the paradoxical effect.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Firing rates of the excitatory (blue) and inhibitory population (red) in the presence of strong SFA (left) with $b=200$. The zoomed-in activity from 3.0 s to 3.2 s (right) corresponding to the green period (left) indicates oscillatory behavior in networks with strong SFA. (B) 3D plot of the excitatory activity $r_{E}$, inhibitory activity $r_{I}$, and the SFA variable $a$ of the network in the period marked with the green bar in A. Networks with different conditions starting from different gray dots converge to the same stable limit cycle marked with the black line.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) The onset peak amplitude (triangles) and fixed point activity (circles) as a function of input $g_{E}$ in networks with E-to-E STD. Here, $J_{E⁢E}=1.8$. (B) The ratio of the onset peak amplitude to fixed point activity as a function of input $g_{E}$. The vectical dashed line indicates the input level which leads to unstable network dynamics without E-to-E STD. (C and D) Same as A and B but as a function of $J_{E⁢E}$. Here, $g_{E}=2.0$.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Amplification index,which is defined as the ratio of the peak amplitude to input $g_{E}$, as a function of input $g_{E}$ for NTA (blue) and linear network (orange) in the presence of E-to-E STD. (B) Same as A but for SSN without STP (green).SSN is constructed by keep-ing $J_{EE}$ the same while changing $J_{IE}$ to $J_{II}$ such that the determinant of the weight matrix det(J) becomes positive. (C) Example of firing rates of the excitatory (blue) and inhibitory population (red) in linear networks with E-to-E STD. During stimulation (gray bar) additional input is injected into the excitatory population. Same as Figure 2B (left) but with $\alpha_{E}=\alpha_{1}=1$ and $g_{E}=2$. (D) Example of firing rates of the excitatory (blue) and inhibitory population (red) in SSNs with $g_{E}=2$.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Firing rates of the excitatory (blue) and inhibitory population (red) in response to stimulation in the presence of E-to-I STF with different time constants $\tau_{u}$. The stimulation period from 2 s to 4 s is marked with the gray bar. The stimulation is implemented by changing input $gE$. (B) Peak amplitude (solid line) and fixed point activity (dashed line) of the excitatory population during stimulation with different STF time constants. (C and D) Same as A and B, but with different maximum allowed facilitation levels $U_{max}$.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** (A) Firing rates of the excitatory (blue) and inhibitory population (red) in the presence of E-to-E STD in an example of a network initially in the ISN regime. During stimulation (gray bar) additional input is injected into the excitatory population. (B) ISN index of the network. (C) Depression variable (black) in an example of a network shown in A. The orange dashed line represents the depression variable threshold above which the network exhibits the paradoxical effect. (D) The normalized firing rates of the excitatory (blue) and inhibitory population (red) when injecting additional excitatory current into the inhibitory population before stimulation (left; orange bar in A), and during stimulation (right; green bar in A). Both before stimulation and during stimulation, the ensemble is in the ISN regime and injecting excitatory current into inhibitory population decreases its firing rate. (E) Firing rates of the excitatory (blue) and inhibitory population (red) when a small transient perturbation to excitatory population activity is introduced marked with arrows while freezing inhibition before stimulation (left) and during stimulation (right). The periods in which inhibition is frozen are marked with black bars. Both before stimulation and during stimulation, the ensemble is in the ISN regime and a small transient excitatory perturbation to the excitatory population results in a transient explosion of the excitatory firing rate.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** (A) ISN index of the network with E-to-I STF in Figure 2E (left). The horizontal dashed line indicates an ISN index of 0. (B) The normalized firing rates of the excitatory (blue) and inhibitory population (red) when injecting additional excitatory current into the inhibitory population before stimulation (left, Figure 2E), and during stimulation (right, Figure 2E). The horizontal dashed lines indicate a normalized firing rate of 1.0.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** (A) ISN index of the network with E-to-E STD as a function of input $g_{E}$. The horizontal dashed line indicates an ISN index of 0. For values above zero, the ensemble is an ISN. The vertical dashed line separates the non-paradoxical and paradoxical regions. (B) Firing rates of the excitatory (blue) and inhibitory population (red) in an ensemble with the input level marked with the black dot in A when a small transient perturbation to excitatory population activity is introduced marked with arrows while freezing inhibition. The periods in which inhibition is frozen are marked with the black bar. A small transient perturbation to the excitatory population results in a transient explosion of the excitatory firing rate, indicating that the ensemble is an ISN. (C) The normalized firing rates of the excitatory (blue) and inhibitory population (red) when injecting excitatory input into the inhibitory population of an ensemble with the input level marked with the black dot in A. The horizontal dashed line indicates a normalized firing rate of 1.0. Despite being an ISN, the ensemble does not exhibit the paradoxical effect.

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp8-v2.jpg)

**Figure 2—figure supplement 8.:** (A) Depression variable (black) in an example of a network initially in the non-ISN regime shown in Figure 2B left. The orange dashed line represents the depression variable threshold above which the network exhibits the paradoxical effect. (B) Firing rates of the excitatory (blue) and inhibitory population (red) when a small transient perturbation to excitatory population activity is introduced marked with arrows while freezing inhibition before stimulation (left; Figure 2B left) and during stimulation (right; Figure 2B left). The periods in which inhibition is frozen are marked with black bars. Initially, the ensemble is in the non-ISN regime and the firing rate of the excitatory slightly increases and then returns to its baseline after introducing a small transient perturbation to the excitatory population. During stimulation, however, the ensemble is an ISN. In this case, a small transient perturbation to the excitatory population results in a transient explosion of the excitatory firing rate.

![Figure 2—figure supplement 9.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp9-v2.jpg)

**Figure 2—figure supplement 9.:** (A) Firing rates of the excitatory (blue) and inhibitory population (red) in response to stimulation in a rate-based model. Additional excitatory inputs are injected into excitatory neurons in the period marked in gray. Firing rates are capped at 300 Hz. (B) Same as A but incorporating SFA. (C) Same as A but incorporating E-to-E STD. (D) Same as A but incorporating E-to-I STF. (E) Same as B but incorporating stronger SFA (left). The zoomed-in activity from 3.0 s to 3.2 s (right) corresponding to the green period (left) indicates oscillatory behavior in networks with strong SFA.

![Figure 2—figure supplement 10.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp10-v2.jpg)

**Figure 2—figure supplement 10.:** (A) Spike raster plot of the excitatory (top, blue) and inhibitory population (top, red) in response to stimulation in a spiking neural network model, and firing rates calculated with 10 ms time bins (bottom). Additional excitatory inputs are injected into excitatory neurons in the period marked in gray. (B) Same as A but incorporating SFA. (C) Same as A but incorporating E-to-E STD. (D) Same as A but incorporating E-to-I STF.

![Figure 2—figure supplement 11.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp11-v2.jpg)

**Figure 2—figure supplement 11.:** (A) Firing rates of the excitatory (blue) and inhibitory population (red) in networks with positive determinant in response to external stimulation during the interval from 2 to 4 s (gray bar). The stimulation was implemented by temporarily increasing the input $g_{E}$ . (B) Phase portrait of the system before stimulation (left; A orange) and during stimulation (right; A green). (C) Same as (A) but in the presence of weak SFA (left) and strong SFA (right). (D) Same as (A) but in the presence of E-to-E STD. (E) Same as (A) but in the presence of E-to-I STF.

![Figure 2—figure supplement 12.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig2-figsupp12-v2.jpg)

**Figure 2—figure supplement 12.:** (A) Example of activity when the change in the input of the inhibitory population Δgt is larger than the the change in the input of the excitatory population ΔgE . Here, ΔgE = 1.8, and ΔgI = 3. (B) The ratio of the onset peak amplitude to the baseline activity as a function of the change in the input of the excitatory population ΔgE and the change in the input of the inhibitory population ΔgI . The diagonal dashed line indicates the border at which ΔgE is identical to ΔgI in networks with E-to-E STD. The star symbol represents the example shown in A.

Next, we considered STP, which is capable of saturating the effective neuronal input-output function (Mongillo et al., 2012; Zenke et al., 2015; Eqs. (37)–(39), Eqs. (41)–(43)). We first analyzed the stimulus-evoked network dynamics when we added STD to the recurrent E-to-E connections. Strong depression of synaptic efficacy resulted in a brief onset transient after which the ensemble dynamics quickly settled into a stimulus-evoked steady-state with slightly higher activity than the baseline (Figure 2B, left). After stimulus removal, the ensemble activity returned back to its baseline level (Figure 2B, left; Figure 2C). Notably, the ensemble dynamics settled at a stable steady state with a much higher firing rate, when inhibition was inactivated during stimulus presentation (Figure 2B, right). This shows that STP is capable of creating a stable high-activity fixed point, which is fundamentally different from the SFA dynamics discussed above. This difference in ensemble dynamics can be readily understood by analyzing the stability of the three-dimensional dynamical system (Materials and methods). We can gain a more intuitive understanding by considering self-consistent solutions of the characteristic function $F⁢(z)$. Initially, the ensemble is at the stable low activity fixed point. But the stimulus causes this fixed point to disappear, thus giving way to positive feedback which creates the leading edge of the onset transient (Figure 2B). However, because E-to-E synaptic transmission is rapidly reduced by STD, the curvature of $F⁢(z)$ changes and a stable fixed point is created, thereby allowing excitatory run-away dynamics to terminate and the ensemble dynamics settle into a steady-state at low activity levels (Figure 2D). We found that E-to-I STF leads to similar dynamics (Figure 2E, left; Appendix 1) with the only difference that this configuration requires inhibition for network stability (Figure 2E, right), whereas E-to-E STD stabilizes activity even without inhibition, albeit at physiologically implausibly high activity levels. Importantly, the re-stabilization through either form of STP did not impair an ensemble’s ability to amplify stimuli during the initial onset phase.

Crucially, transient amplification in supralinear networks with STP occurs above a critical threshold (Figure 2—figure supplement 2), and requires recurrent excitation $J_{EE}$ to be sufficiently strong (Figure 2—figure supplement 2C, D). To quantify the amplification ability of these networks, we calculated the ratio of the evoked peak firing rate to the input strength, henceforth called the ‘Amplification index’. We found that amplification in STP-stabilized supralinear networks can be orders of magnitude larger than in linear networks with equivalent weights and comparable stabilized supralinear networks (SSNs) without STP (Figure 2—figure supplement 3). We stress that the resulting firing rates are parameter-dependent (Figure 2—figure supplement 4) and their absolute value can be high due to the high temporal precision of the onset peak and its short duration. In experiments, such high rates manifest themselves as precisely time-locked spikes with millisecond resolution (DeWeese et al., 2003; Wehr and Zador, 2003; Bolding and Franks, 2018; Gjoni et al., 2018).

Recent studies suggest that cortical networks operate as inhibition-stabilized networks (ISNs) (Sanzeni et al., 2020; Sadeh and Clopath, 2021), in which the excitatory network is unstable in the absence of feedback inhibition (Tsodyks et al., 1997; Ozeki et al., 2009). To that end, we investigated how ensemble re-stabilization relates to the network operating regime at baseline and during stimulation. Whether a network is an ISN or not is mathematically determined by the real part of the leading eigenvalue of the Jacobian of the excitatory-to-excitatory subnetwork (Tsodyks et al., 1997). We computed the leading eigenvalue in our model incorporating STP and referred to it as ‘ISN index’ (Materials and methods; Appendix 2). We found that in networks with STP the ISN index can switch sign from negative to positive during external stimulation, indicating that the ensemble can transition from a non-ISN to an ISN (Figure 2F). Notably, this behavior is distinct from linear network models in which the network operating regime is independent of the input (Materials and methods). Whether this switch between non-ISN to ISN occurred, however, was parameter dependent and we also found network configurations that were already in the ISN regime at baseline and remained ISNs during stimulation (Figure 2—figure supplement 5). Thus, re-stabilization was largely unaffected by the network state and consistent with experimentally observed ISN states (Sanzeni et al., 2020).

Theoretical studies have shown that one defining characteristic of ISNs in static excitatory and inhibitory networks is that injecting excitatory (inhibitory) current into inhibitory neurons decreases (increases) inhibitory firing rates, which is also known as the paradoxical effect (Tsodyks et al., 1997; Miller and Palmigiano, 2020). Yet, it is unclear whether in networks with STP, inhibitory stabilization implies paradoxical response and vice versa. We therefore analyzed the condition of being an ISN and the condition of having paradoxical response in networks with STP (Materials and methods; Appendix 2; Appendix 3). Interestingly, we found that in networks with E-to-E STD, the paradoxical effect implies inhibitory stabilization, whereas inhibitory stabilization does not necessarily imply paradoxical response (Figure 2G; Materials and methods), suggesting that having paradoxical effect is a sufficient but not necessary condition for being an ISN. In contrast, in networks with E-to-I STF, inhibitory stabilization and paradoxical effect imply each other (Appendix 2; Appendix 3). Therefore, paradoxical effect can be exploited as a proxy for inhibition stabilization for networks with STP we considered here. By injecting excitatory current into the inhibitory population, we found that the network did not exhibit the paradoxical effect before stimulation (Figure 2H, left; Figure 2—figure supplement 6). In contrast, injecting excitatory inputs into the inhibitory population during stimulation reduced their activity (Figure 2H, right; Figure 2—figure supplement 6). As demonstrated in our analysis, non-paradoxical response does not imply non-ISN (Figure 2—figure supplement 7; Materials and methods). We therefore examined the inhibition stabilization property of the ensemble by probing the ensemble behavior when a small transient perturbation to excitatory population activity is introduced while inhibition is frozen before stimulation and during stimulation. Before stimulation, the firing rate of the excitatory population slightly increases and then returns to its baseline after the transient perturbation (Figure 2—figure supplement 8). During stimulation, however, the transient perturbation leads to a transient explosion of the excitatory firing rate (Figure 2—figure supplement 8). These results further confirm that the ensemble shown in our example is initially a non-ISN before stimulation and can transition to an ISN with stimulation. By elevating the input level at the baseline in the model, the ensemble can be initially an ISN (Figure 2—figure supplement 5), resembling recent studies revealing that cortical circuits in the mouse V1 operate as ISNs in the absence of sensory stimulation (Sanzeni et al., 2020).

Despite the fact that the supralinear input-output function of our framework captures some aspects of intracellular recordings (Priebe et al., 2004), it is unbounded and thus allows infinitely high firing rates. This is in contrast to neurobiology where firing rates are bounded due to neuronal refractory effects. While this assumption permitted us to analytically study the system and therefore to gain a deeper understanding of the underlying ensemble dynamics, we wondered whether our main conclusions were also valid when we limited the maximum firing rates. To that end, we carried out the same simulations while capping the firing rate at 300  Hz. In the absence of additional SFA or STP mechanisms, the firing rate saturation introduced a stable high-activity state in the ensemble dynamics which replaced the unstable dynamics in the uncapped model. As above, the ensemble entered this high-activity steady-state when stimulated with an external input above a critical threshold and exhibited persistent activity after stimulus removal (Figure 2—figure supplement 9). While weak SFA did not change this behavior, strong SFA resulted in oscillatory behavior during stimulation consistent with previous analytical work (Figure 2—figure supplement 9, van Vreeswijk and Hansel, 2001), but did not in stable steady-states commonly observed in biological circuits. In the presence of E-to-E STD or E-to-I STF, however, the ensemble exhibited transient evoked activity at stimulation onset that was comparable to the uncapped case. Importantly, the ensemble did not show persistent activity after the stimulation (Figure 2—figure supplement 9). Finally, we confirmed that all of these findings were qualitatively similar in a realistic spiking neural network model (Figure 2—figure supplement 10; Materials and methods).

In summary, we found that neuronal ensembles can rapidly, nonlinearly, and transiently amplify inputs by briefly switching from stable to unstable dynamics before being re-stabilized through STP mechanisms. We call this mechanism nonlinear transient amplification (NTA) which, in contrast to balanced amplification (Murphy and Miller, 2009; Hennequin et al., 2012), arises from population dynamics with supralinear neuronal activation functions interacting with STP. While we acknowledge that there may be other nonlinear transient amplification mechanisms, in this article we restrict our analysis to the definition above. NTA is characterized by a large onset response, a subsequent ISN steady-state while the stimulus persists, and a return to a unique baseline activity state after the stimulus is removed. Thus, NTA is ideally suited to rapidly and nonlinearly amplify sensory inputs through recurrent excitation, like reported experimentally (Ko et al., 2011; Cossell et al., 2015), while avoiding persistent activity.

### Co-tuned inhibition broadens the parameter regime of NTA in the absence of persistent activity

Up to now, we have focused on a single neuronal ensemble. However, to process information in the brain, several ensembles with different stimulus selectivity presumably coexist and interact in the same circuit. This coexistence creates potential problems. It can lead to multi-stable persistent attractor dynamics, which are not commonly observed and could have adverse effects on the processing of subsequent stimuli. One solution to this issue could be EI co-tuning, which arises in network models with plastic inhibitory synapses (Vogels et al., 2011) and has been observed experimentally in several sensory systems (Wehr and Zador, 2003; Froemke et al., 2007; Okun and Lampl, 2008; Rupprecht and Friedrich, 2018).

To characterize the conditions under which neuronal ensembles nonlinearly amplify stimuli without persistent activity, we analyzed the case of two interacting ensembles. More specifically, we considered networks with two excitatory ensembles and distinguished between global and co-tuned inhibition (Figure 3A). In the case of global inhibition, one inhibitory population non-specifically inhibits both excitatory populations (Figure 3A, left). In contrast, in networks with co-tuned inhibition, each ensemble is formed by a dedicated pair of an excitatory and an inhibitory population which can have cross-over connections, for instance, due to overlapping ensembles (Figure 3A, right).

![Figure 3.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of two neuronal ensembles with global inhibition (left) and with co-tuned inhibition (right). (B) Firing rate dynamics of bi/multi-stable ensemble dynamics (left) and uni-stable (right). In both cases, additional excitatory inputs are injected into excitatory ensemble E1 during the period marked in gray. (C) Analytical solution of uni- and bi/multi-stability regions for global inhibition (left) and co-tuned inhibition (right). Co-tuning results in a larger parameter regime of uni-stability. The triangles correspond to the two examples in B.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Examples of activity in networks with global inhibition (left) and in networks with co-tuned inhibition (right) in the presence of E-to-E STD. (B) Amplification index for networks with global inhibition (black) and network with co-tuned inhibition (gray) as a function of input $g_{E}$ in networks with E-to-E STD. Data points at $g_{E}=2.5$ correspond to the examples shown in A.

Global inhibition supports winner-take-all competition and is therefore often associated with multi-stable attractor dynamics (Wong and Wang, 2006; Mongillo et al., 2008). We first illustrated this effect in a network model with global inhibition. When the recurrent excitatory connections within each ensemble were sufficiently strong, small amounts of noise in the initial condition led to one of the ensembles spontaneously activating at elevated firing rates, while the other ensemble’s activity remained low (Figure 3B, left). A specific external stimulation could trigger a switch from one state to the other in which the other ensemble was active at a high firing rate. Importantly, this change persisted even after the stimulus had been removed, a hallmark of multi-stable dynamics. In contrast, uni-stable systems have a global symmetric state in which both ensembles have the same activity in the absence of stimulation. While the stimulated ensemble showed elevated firing rates in response to the stimulus, its activity returned to the baseline level after the stimulus is removed (Figure 3B, right), consistent with experimental observations (DeWeese et al., 2003; Rupprecht and Friedrich, 2018; Bolding and Franks, 2018). Note that the only difference between these two models is that $J_{E⁢E}$ is larger in the multi-stable example than in the uni-stable one.

Symmetric baseline activity is most consistent with activity observed in sensory areas. Hence, we sought to understand which inhibitory connectivity would be most conducive to maintain it. To that end, we analytically identified the uni-stability conditions, which are determined by the leading eigenvalue of the Jacobian matrix of the system, for networks with varying degrees of EI co-tuning (Materials and methods). We found that a broader parameter regime underlies uni-stability in networks with co-tuned inhibition than global inhibition (Figure 3C). Notably, this conclusion is general and extends to networks with an arbitrary number of ensembles (Materials and methods). In comparison to the ensemble with global inhibition, the ensemble with co-tuned inhibition exhibits weaker — but still strong — NTA (Figure 3—figure supplement 1). Thus, co-tuned inhibition broadens the parameter regime in which NTA is possible while simultaneously avoiding persistent attractor dynamics.

### NTA provides better pattern completion than fixed points while retaining stimulus selectivity

Neural circuits are capable of generating stereotypical activity patterns in response to partial cues and forming distinct representations in response to different stimuli (Carrillo-Reid et al., 2016; Marshel et al., 2019; Bolding et al., 2020; Vinje and Gallant, 2000; Cayco-Gajic and Silver, 2019). To test whether NTA achieves pattern completion while retaining stimulus selectivity, we analyzed the transient onset activity in our models and compared it to the fixed point activity.

To investigate pattern completion and stimulus selectivity in our model, we considered a co-tuned network with E-to-E STD and two distinct excitatory ensembles $E⁢1$ and $E⁢2$. We gave additional input $g_{E⁢1}$ to a Subset 1, consisting of 75% of the neurons in ensemble $E⁢1$ (Figure 4A). We then measured the evoked activity in the remaining 25% of the excitatory neurons in $E⁢1$ to quantify pattern completion. To assess stimulus selectivity, we injected additional input $g_{E⁢1}$ into the entire $E⁢1$ ensemble during the second stimulation phase (Figure 4A) while measuring the activity of $E⁢2$. We found that neurons in Subset 2, which did not receive additional input, showed large onset responses, their steady-state activity was largely suppressed (Figure 4B). Despite the fact that inputs to $E⁢1$ caused increased transient onset responses in $E⁢2$, the amount of increase was orders of magnitude smaller than in $E⁢1$ (Figure 4B). To quantify pattern completion, we defined the

$$
Association index=1+\frac{r_{E⁢1_{2}}-r_{E⁢1_{1}}}{r_{E⁢1_{2}}+r_{E⁢1_{1}}} .
$$

![Figure 4.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of the network setup used to probe pattern completion and stimulus selectivity. To assess the effect on pattern completion, 75% of the neurons (Subset 1) in ensemble E1 received additional input gE1 during Phase one (2–4 s), while we recorded the firing rate of the remaining 25% (Subset 2) in the excitatory ensemble E1. To evaluate the impact on stimulus selectivity, all neurons in E1 received additional inputs gE1 in Phase two (6–8 s) while the firing rate of E2 was measured. A downstream neuron’s ability to discriminate between E1 or E2 being active depends on whether their activity is well separated by a symmetric decision boundary (inset). (B) Examples of firing rates of Subset 2 of E1 (left, blue) and E2 (right, green) with E-to-E STD. (C) Association index as a function of input gE1 for the onset peak amplitude (magenta solid line) and fixed point activity (gray dashed line) for E-to-E STD. (D) Distance to the decision boundary (see panel A, inset) as a function of input gE1 for the onset peak amplitude (magenta solid line) and fixed point activity (gray dashed line) for E-to-E STD. (E and F) Same as C and D but as a function of β, which controls the inner- and inter-ensemble connection strength.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Examples of firing rates of Subset 2 of E1 (blue) and E2 (green) for gE = 3 (left) and for gE = 4 (right) in networks with E-to-E STD. (B) The ratio of the fixed point activity to the baseline activity for unstimulated co-tuned neurons (E1 Subset 2) as a function of input gE in rate-based models with E-to-E STD. The horizontal dashed line indicates a ratio of 1 at which the fixed point activity is identical to the baseline activity.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Association index as a function of input gE1 for the onset peak amplitude (magenta solid line) and fixed point activity (gray dashed line) for E-to-I STF. (B) Distance to the decision boundary as a function of input gE1 for the onset peak amplitude (magenta solid line) and fixed point activity (gray dashed line) for E-to-I STF. (C and D) Same as A and B but as a function of β, which controls the inner- and inter-ensemble connection strength.

Here, $r_{E⁢1_{1}}$ and $r_{E⁢1_{2}}$ correspond to the subpopulation activities of $E⁢1$, respectively. By definition, the Association index ranges from zero to one, with larger values indicating stronger associativity. In addition, to quantify the selectivity between $E⁢1$ and $E⁢2$, we considered a symmetric binary classifier (Figure 4A, inset) and measured the distance to the decision boundary (Materials and methods). Note that the Association index was computed during Phase one and the distance to the decision boundary during Phase two in this simulation paradigm (Figure 4B).

With these definitions, we ran simulations with different input strengths $g_{E⁢1}$. We found that the onset peaks showed stronger association than the fixed point activity (Figure 4C). Note that the Association index at the fixed point remained zero, a direct consequence of $r_{E⁢1_{2}}$ being suppressed to zero. Furthermore, we found that the distance between the transient onset response and the decision boundary was always greater than for the fixed point activity (Figure 4D) showing that onset responses retain stimulus selectivity. While the fixed point activity of the unstimulated co-tuned neurons is zero in the given example, stimulating a subset of neurons in one ensemble can lead to an increase in the fixed point activity of the unstimulated neurons in the same ensemble under certain conditions (Figure 4—figure supplement 1; Appendix 4), which is consistent with pattern completion experiments (Carrillo-Reid et al., 2016; Marshel et al., 2019) showing that unstimulated neurons from the same ensemble can remain active throughout the whole stimulation period.

To investigate how the recurrent excitatory connectivity affects both pattern completion and stimulus selectivity, we introduced the parameter $\beta$ which controls recurrent excitatory tuning by trading off within-ensemble E-to-E strength $J_{E⁢E}$ relative to the inter-ensemble strength $J_{E⁢E}^{^{′}}$ (Figure 4A) such that $J_{E⁢E}=\beta⁢J_{tot}$ and $J_{E⁢E}^{^{′}}=(1-\beta)⁢J_{tot}$. These definitions ensure that the total weight $J_{tot}=J_{E⁢E}+J_{E⁢E}^{^{′}}$ remains constant for any choice of $\beta$. Notably, the overall recurrent excitation strength within an ensemble $J_{E⁢E}$ increases with increasing $\beta$. When $\beta$ is larger than 0.5, the excitatory connection strength within the ensemble $J_{E⁢E}$ exceeds the one between ensembles $J_{E⁢E}^{^{′}}$.

We found that pattern completion ability monotonically increases with $\beta$ with a pronounced onset for $\beta§gt;0.6$ where NTA takes hold (Figure 4E). Moreover, in this regime the two stimulus representations are well separated (Figure 4F) which ensures stimulus selectivity also during onset transients. Together, these findings recapitulate the point that recurrent excitatory tuning is a key determinant of network dynamics. Finally, we confirmed that our findings were also valid in networks with E-to-I STF (Figure 4—figure supplement 2), which is commonly observed in the brain (Markram et al., 1998; Zucker and Regehr, 2002; Pala and Petersen, 2015). In summary, NTA’s transient onset responses maintain stimulus selectivity and result in overall better pattern completion than fixed point activity.

### NTA provides higher amplification and pattern separation in morphing experiments

So far, we only considered input to one ensemble. To examine how representations in our model are affected by ambiguous inputs to several ensembles, we performed additional morphing experiments (Freedman et al., 2001; Niessing and Friedrich, 2010). To that end, we introduced the parameter $p$ which interpolates between two input stimuli which target $E⁢1$ and $E⁢2$ respectively. When $p$ is zero, all additional input is injected into $E⁢1$. For $p$ equal to one, all additional input is injected into $E⁢2$. Finally, $p$ equal to 0.5 corresponds to the symmetric case in which $E⁢1$ and $E⁢2$ receive the same amount of additional input (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig5-v2.jpg)

**Figure 5.:** (A) Schematic of the morphing stimulation paradigm. The fraction of the additional inputs into the two excitatory ensembles is controlled by the parameter p. (B) Peak amplitude of E1 (blue) and E2 (green) as a function of p for E-to-E STD. Brightness levels represent different recurrent E-to-E connection strengths JEE . (C) Same as in B but for fixed point activity. (D) Distance to the decision boundary as a function of p for the peak onset response (magenta solid line) and fixed point activity (gray dashed line) for E-to-E STD in a network with J’IE = 0.4. (E) Same as D but with different E-to-I connection strengths J’IE across ensembles for a network with JEE = 1.2.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Separation index, defined as $(r_{E2}−r_{E1})/(r_{E1}+r_{E2})$, as a function of p for the peak onset response (magenta solid line) and fixed point activity (gray dashed line) for E-to-E STD. Different levels of brightness represent different recurrent E-to-E connection strengths JEE . (B) Same as A but with different E-to-I connection strengths J’IE across ensembles.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Distance to the decision boundary as a function of for the peak onset response (magenta solid line) and fixed point activity (gray dashed line) for E-to-I STF. (B) Same as A but with different E-to-I connection strengths J’IE across ensembles. (C and D) Same as A and B but quantified by Separation index, defined as $(r_{E2}−r_{E1})/(r_{E1}+r_{E2})$.

First, we investigated how the recurrent excitatory connection strength within each ensemble $J_{E⁢E}$ affects the onset peak amplitude and fixed point activity. We found that the peak amplitudes depend strongly on $J_{E⁢E}$, whereas the fixed point activity was only weakly dependent on $J_{E⁢E}$ (Figure 5B and C). When we disconnected the ensembles by completely eliminating all recurrent excitatory connections, activity was noticeably decreased (Figure 5B and C). This illustrates, that recurrent excitation does play an important role in selectively amplifying specific stimuli similar to experimental observations (Marshel et al., 2019; Peron et al., 2020), but that amplification is highest at the onset.

Further, we examined the impact of competition through lateral inhibition as a function of the E-to-I inter-ensemble strength $J_{I⁢E}^{^{′}}$ (Materials and methods). As above, we quantified its impact by measuring the representational distance to the decision boundary for the transient onset responses and fixed point activity. We found that regardless of the specific STP mechanism, the distance was larger for the onset responses than for the fixed point activity, consistent with the notion that the onset dynamics separate stimulus identity reliably (Figure 5D and E). Since the absolute activity levels between onset and fixed point differed substantially, we further computed the relative pattern Separation index $(r_{E⁢2}-r_{E⁢1})/(r_{E⁢1}+r_{E⁢2})$ and found that the onset transient provides better pattern separation ability for ambiguous stimuli with $p$ close to 0.5 (Figure 5—figure supplement 1) provided that the E-to-I connection strength across ensembles $J_{I⁢E}^{^{′}}$ is strong enough. All the while separability for the onset transient was slightly decreased for distinct inputs with $p\in{0,1}$ in comparison to the fixed point. In contrast, fixed points clearly separated such pure stimuli while providing weaker pattern separation for ambiguous input combinations. Importantly, these findings qualitatively held for networks with NTA mediated by E-to-I STF (Figure 5—figure supplement 2). Thus, NTA provides stronger amplification and pattern separation than fixed point activity in response to ambiguous stimuli.

### NTA in spiking neural networks

Thus far, our analysis relied on power law neuronal input-output functions in the interest of analytical tractability. To test whether our findings also qualitatively apply to more realistic network models, we built a spiking neural network consisting of randomly connected 800 excitatory and 200 inhibitory neurons, in which the E-to-E synaptic connections were subject to STD (Materials and methods). Here, we defined five overlapping ensembles, each corresponding to 200 randomly selected excitatory neurons. During an initial simulation phase (0–22 s), we consecutively stimulated each ensemble by giving additional input to their excitatory neurons, whereas the input to other neurons remained unchanged (Figure 6A). In addition, we also tested pattern completion by stimulating only 75% (Subset 1) of the neurons belonging to Ensemble 5 (22–24  s; Figure 6A). We quantified each ensemble’s activity by calculating the population firing rate of the ensemble (Materials and methods). As in the case of the rate-based model, the neuronal ensembles in the spiking model generated pronounced transient onset responses. We then measured the difference of peak ensemble activity and fixed point activity between the stimulated ensemble and the remaining unstimulated ensembles (Materials and methods). As for the rate-based networks, this difference was consistently larger for the onset peak than for the fixed point (Figure 6B and C). Thus, transient onset responses allow better stimulus separation than fixed points also in spiking neural network models.

![Figure 6.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig6-v2.jpg)

**Figure 6.:** (A) Spiking activity of excitatory (blue) and inhibitory (red) neurons in a spiking neural network. From 2 to 20 s, Ensembles 1–5 individually received additional input for 2 s each (colored bars). From 22 to 24 s, 75% of Ensemble 5 neurons (Subset 1) received additional input, whereas the rest 25% of Ensemble 5 neurons (Subset 2) did not receive additional input. The symbols at the top designate the different simulation phases of baseline activity, the onset transients, and the fixed point activity. Different colors correspond to the distinct stimulation periods. (B) Ensemble activity (colors). (C) Difference in ensemble activity between the stimulated ensemble with the remaining ensembles for the transient onset peak and the fixed point. Points correspond to the different stimulation periods. (D) Spiking activity during the interval 0–10 s represented in the PCA basis spanned by the first two principal components which captured approximately 40% of the total variance. The colored lines represent the PC trajectories of the first two stimuli shown in A and B. Triangles, points and crosses correspond to the onset peak, fixed point, and baseline activity, respectively. (E) Ensemble activity of Subset 1 (purple) and Subset 2 (gray) of Ensemble 5 from 16 to 26 s. Onset peaks are marked by triangles.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/71263/elife-71263-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The ratio of the fixed point activity to the baseline activity for unstimulated co-tuned neurons (Ensemble 5, Subset 2) as a function of feedforward input to Subset one in spiking neural networks with E-to-E STD. The horizontal dashed line indicates a ratio of one at which the fixed point activity is identical to the baseline activity. Each point corresponds to a measurement from a randomly initialized network.

Finally, to visualize the neural activity, we projected the binned spiking activity during the first 10  s of our simulation onto its first two principal components. Notably, the PC trajectory does not exhibit a pronounced rotational component (Figure 6D) as activity is confined to one specific ensemble, consistent with experiments (Marshel et al., 2019). Furthermore, we computed the fifth ensemble’s activity for Subset 1 and 2 during the time interval 16–26  s. In agreement with our rate models, neurons in Subset 2 which did not receive additional inputs showed a strong response at the onset (Figure 6E), but not at the fixed point, suggesting that the strongest pattern completion occurs during the initial amplification phase. Finally, we also observed higher-than-baseline fixed point activity in unstimulated neurons of Subset 2 in spiking neural networks (Figure 6—figure supplement 1). Thus, the key characteristics of NTA are preserved across rate-based and more realistic spiking neural network models.

## Discussion

In this study, we demonstrated that neuronal ensemble models with recurrent excitation and suitable forms of STP exhibit nonlinear transient amplification (NTA), a putative mechanism underlying selective amplification in recurrent circuits. NTA combines a supralinear neuronal transfer function, recurrent excitation between neurons with similar tuning, and pronounced STP. Using analytical and numerical methods, we showed that NTA generates rapid transient onset responses during which optimal stimulus separation occurs rather than at steady-states. Additionally, we showed that co-tuned inhibition is conducive to prevent the emergence of persistent activity, which could otherwise interfere with processing subsequent stimuli. In contrast to balanced amplification (Murphy and Miller, 2009), NTA is an intrinsically nonlinear mechanism for which only stimuli above a critical threshold are amplified effectively. While the precise threshold value is parameter-dependent, it can be arbitrarily low provided the excitatory recurrent connections are sufficiently strong (Figure 1F). Importantly, such a critical activation threshold offers a possible explanation for sensory perception experiments which show similar threshold behavior (Marshel et al., 2019; Peron et al., 2020). Following transient amplification, ensemble dynamics are inhibition-stabilized, which renders our model compatible with existing work on SSNs (Ahmadian et al., 2013; Rubin et al., 2015; Hennequin et al., 2018; Kraynyukova and Tchumatchenko, 2018; Echeveste et al., 2020). Thus, NTA provides a parsimonious explanation for why sensory systems may rely upon neuronal ensembles with recurrent excitation in combination with EI co-tuning, and pronounced STP dynamics.

Several theoretical studies approached the problem of transient amplification in recurrent neural network models. Loebel and Tsodyks, 2002 have described an NTA-like mechanism as a driver for powerful ensemble synchronization in rate-based networks and in spiking neural network models of auditory cortex (Loebel et al., 2007). Here, we generalized this work to both E-to-E STD and E-to-I STF and provide an in-depth characterization of its amplification capabilities, pattern completion properties, and the resulting network states with regard to their inhibition-stabilization properties. Moreover, we showed that SFA cannot provide similar network stabilization and explored how EI co-tuning interacts with NTA. Finally, we contrasted NTA to alternative transient amplification mechanisms. Balanced amplification is a particularly well-studied transient amplification mechanism (Murphy and Miller, 2009; Goldman, 2009; Hennequin et al., 2014; Bondanelli and Ostojic, 2020; Gillett et al., 2020; Christodoulou et al., 2021) that relies on non-normality of the connectivity matrix to selectively and rapidly amplify stimuli. Importantly, balanced amplification occurs in networks in which strong recurrent excitation is appropriately balanced by strong recurrent inhibition. It is capable of generating rich transient activity in linear network models (Hennequin et al., 2014), and selectively amplifies specific activity patterns, but without a specific activation threshold. In addition, in spiking neural networks, strong input can induce synchronous firing at the population level which is subsequently stabilized by strong feedback inhibition without the requirement for STP mechanisms (Stern et al., 2018). These properties contrast with NTA, which has a nonlinear activation threshold and intrinsically relies on STP to stabilize otherwise unstable run-away dynamics. Due to the switch of the network’s dynamical state, NTA’s amplification can be orders of magnitudes larger than balanced amplification (Figure 2—figure supplement 3). Interestingly, after the transient amplification phase, ensemble dynamics settle in an inhibitory-stabilized state, which renders NTA compatible with previous work on SSNs but in the presence of STP. Finally, although NTA and balanced amplification rely on different amplification mechanisms, they are not mutually exclusive and could, in principle, co-exist in biological networks.

NTA’s requirement to generate positive feedback dynamics through recurrent excitation, motivated our focus on networks with $det(J)<0$. As demonstrated in previous work (Ahmadian et al., 2013), supralinear networks with $det(J)>0$ and instantaneous inhibition ($\tau_{I}/\tau_{E}→0$) are always stable for any given input, they are thus unable to generate positive feedback dynamics. In addition, networks with $det(J)>0$ can exhibit a range of interesting behaviors, for example, oscillatory dynamics and persistent activity (Kraynyukova and Tchumatchenko, 2018). It is worth noting, however, that for delayed or slow inhibition, stimulation can still lead to unstable network dynamics in networks with $det(J)>0$. Nevertheless, our simulations suggest that our main conclusions about the stabilization mechanisms still hold (Figure 2—figure supplement 11).

NTA shares some properties with the notion of network criticality in the brain, like synchronous activation of cell ensembles (Plenz and Thiagarajan, 2007) and STP which can tune networks to a critical state (Levina et al., 2007). However, in contrast to most models of criticality, in NTA an ensemble briefly transitions to supercritical dynamics in a controlled, stimulus-dependent manner rather than spontaneously. Yet, how the two paradigms are connected at a more fundamental level, is an intriguing question left for future work. Furthermore, recurrent co-tuned inhibition is essential for NTA to ensure uni-stability and selectivity through the suppression of ensembles with different tuning. This requirement is similar in flavor to semi-balanced networks characterized by excess inhibition to some excitatory ensembles while others are balanced (Baker et al., 2020). However, the theory of semi-balanced networks has, so far, only been applied to steady-state dynamics while ignoring transients and STP. EI co-tuning prominently features in several models and was shown to support network stability (Vogels et al., 2011; Hennequin et al., 2017; Znamenskiy et al., 2018), efficient coding (Denève and Machens, 2016), novelty detection (Schulz et al., 2021), changes in neuronal variability (Hennequin et al., 2018; Rost et al., 2018), and correlation structure (Wu et al., 2020). Moreover, some studies have argued that EI balance and co-tuning could increase robustness to noise in the brain (Rubin et al., 2017). The present work mainly highlights its importance for preventing multi-stability and delay activity in circuits not requiring such long-timescale dynamics.

NTA is consistent with several experimental findings. First, our model recapitulates the key findings of Shew et al., 2015 who showed ex vivo that strong sensory inputs cause a transient shift to a supercritical state, after which adaptive changes rapidly tune the network to criticality. Second, NTA requires strong recurrent excitatory connectivity between neurons with similar tuning, which has been reported in experiments (Ko et al., 2011; Cossell et al., 2015; Peron et al., 2020). Third, ensemble activation in our model depends on a critical stimulus strength in line with recent all-optical experiments in the visual cortex, which further link ensemble activation with a perceptual threshold (Marshel et al., 2019). Fourth, sensory networks are uni-stable in that they return to a non-selective activity state after the removal of the stimulus and usually do not show persistent activity (DeWeese et al., 2003; Mazor and Laurent, 2005; Rupprecht and Friedrich, 2018). Fifth, our work shows that NTA’s onset responses encode stimulus identity better than the fixed point activity, consistent with experiments in the locust antennal lobe (Mazor and Laurent, 2005) and research supporting that the brain relies on coactivity on short timescales to represent information (Stopfer et al., 1997; Engel et al., 2001; Harris et al., 2003; El-Gaby et al., 2021). Yet, it remains to be seen whether these findings are also coherent with data on the temporal evolution in other sensory systems. Finally, EI co-tuning, which is conducive for NTA, has been found ubiquitously in different sensory circuits (Wehr and Zador, 2003; Froemke et al., 2007; Okun and Lampl, 2008; Rupprecht and Friedrich, 2018; Znamenskiy et al., 2018).

In our model, we made several simplifying assumptions. For instance, we kept the input to inhibitory neurons fixed and only varied the input to the excitatory population. This step was motivated by experiments in the piriform cortex where the total inhibition is dominated by feedback inhibition (Franks et al., 2011). Nevertheless, significant feedforward inhibition was observed in other areas (Bissière et al., 2003; Cruikshank et al., 2007; Ji et al., 2016; Miska et al., 2018). While an in-depth comparison for different origins of inhibition was beyond the scope of the present study, we found that increasing the inputs to the excitatory population and inhibitory population by the same amount can still lead to NTA (Figure 1—figure supplement 1; Figure 2—figure supplement 12; Materials and methods), suggesting that our main findings can remain unaffected in the presence of substantial feedforward inhibition. In addition, we limited our analysis to only a few overlapping ensembles. It will be interesting future work to study NTA in the case of many interacting and potentially overlapping ensembles and to determine the maximum storage capacity above which performance degrades. Finally, we anticipate that temporal differences in excitatory and inhibitory synaptic transmission may be important to preserve NTA’s stimuli selectivity.

Our model makes several predictions. In contrast to balanced amplification, in which the network operating regime depends solely on the connectivity, an ensemble involved in NTA can transition from a non-ISN to an ISN state. Such a transition is consistent with noise variability observed in sensory cortices (Hennequin et al., 2018) and could be tested experimentally by probing the paradoxical effect under different stimulation conditions (Figure 2G–H; Figure 2—figure supplement 6). Moreover, NTA predicts that onset activity provides a better stimulus encoding and its activity is correlated with the fixed point activity. This signature is different from purely non-normal amplification mechanisms which would involve a wave of neuronal activity across several distinct ensembles similar to a synfire chain (Abeles, 1991). The difference should be clearly discernible in data. Since NTA relies on recurrent excitation between ensemble neurons, it suggests normal dynamics in which distinct ensembles first activate and then inactivate. The resulting dynamics have weak rotational components (Figure 6D) as seen in some experiments (Marshel et al., 2019). Strong non-normal amplification, on the other hand, relies on sequential activation associated with pronounced rotational dynamics (Hennequin et al., 2014; Gillett et al., 2020), as for instance observed in motor areas (Churchland et al., 2012). Although both non-normal mechanisms and NTA are likely to co-exist in the brain, we speculate that strong NTA is best suited for, and thus most like to be found in, sensory systems.

In summary, we introduced a general theoretical framework of selective transient signal amplification in recurrent networks. Our approach derives from the minimal assumptions of a nonlinear neuronal transfer function, recurrent excitation within neuronal ensembles, and STP. Importantly, our analysis revealed the functional benefits of STP and EI co-tuning, both pervasively found in sensory circuits. Finally, our work suggests that transient onset responses rather than steady-state activity are ideally suited for coactivity-based stimulus encoding and provides several testable predictions.

## Materials and methods

### Stability conditions for supralinear networks

The dynamics of a neuronal ensemble consisting of one excitatory and one inhibitory population with a supralinear, power law input-output function can be described as follows:

$$
\tau_{E}⁢\frac{d⁢r_{E}}{d⁢t}=-r_{E}+[J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+g_{E}]_{+}^{\alpha_{E}}
$$



$$
\tau_{I}⁢\frac{d⁢r_{I}}{d⁢t}=-r_{I}+[J_{I⁢E}⁢r_{E}-J_{I⁢I}⁢r_{I}+g_{I}]_{+}^{\alpha_{I}}
$$

The Jacobian $M$ of the system is given by

$$
M=[\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}} −\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})]
$$

To ensure that the system is stable, the product of $M$’s eigenvalues $\lambda_{1}⁢\lambda_{2}$, which is equivalent to the determinant of $M$, has to be positive. In addition, the sum of the two eigenvalues $\lambda_{1}+\lambda_{2}$, which corresponds to $tr(M)$, has to be negative. We therefore obtained the following two stability conditions

$$
\lambda_{1}⁢\lambda_{2}=-\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}-1)⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})+\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢J_{E⁢I}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}⁢J_{I⁢E}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}}§gt;0
$$



$$
\lambda_{1}+\lambda_{2}=\tau_{E}^{-1}⁢(J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}-1)-\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})§lt;0
$$

Notably, the stability conditions depend on the firing rate of the excitatory population $r_{E}$ and the inhibitory population $r_{I}$. Since firing rates are input-dependent, the stability of supralinear networks is input-dependent. In contrast, in linear networks in which $\alpha_{E}=\alpha_{I}=1$, the conditions can be simplified to

$$
\lambda_{1}⁢\lambda_{2}=-\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(J_{E⁢E}-1)⁢(1+J_{I⁢I})+\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢J_{E⁢I}⁢J_{I⁢E}§gt;0
$$



$$
\lambda_{1}+\lambda_{2}=\tau_{E}^{-1}⁢(J_{E⁢E}-1)-\tau_{I}^{-1}⁢(1+J_{I⁢I})§lt;0
$$

and are thus input-independent.

### ISN index for supralinear networks

If an ensemble is unstable without feedback inhibition, then the ensemble is an ISN (Tsodyks et al., 1997). To determine whether a given system is an ISN, we analyzed the stability of the E-E subnetwork, which is determined by the real part of the leading eigenvalue of the Jacobian of the E-E subnetwork. In the following, we call this leading eigenvalue the ‘ISN index’, which is defined as follows:

$$
ISN index=\tau_{E}^{-1}⁢(J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}-1)
$$

A positive ISN index indicates the system is an ISN. Otherwise, the system is non-ISN. For supralinear networks in which $\alpha_{E}§gt;1$, the ISN index depends on the firing rates, inputs can therefore switch the network from non-ISN to ISN. In contrast, $\alpha_{E}=1$ for linear networks which renders the ISN index firing rate independent.

### Characteristic function

To investigate how network stability changes with input, we trace the steps of Kraynyukova and Tchumatchenko, 2018 and define the characteristic function $F⁢(z)$ as follows:

$$
F(z)=J_{EE}[z]_{+}^{\alpha_{E}}−J_{EI}[det(J)⋅J_{EI}^{−1}[z]_{+}^{\alpha_{E}}+J_{EI}^{−1}J_{II}z−J_{EI}^{−1}J_{II}g_{E}+g_{I}]_{+}^{\alpha_{I}}−z+g_{E}
$$

where

$$
z=J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+g_{E}
$$

is the current into the excitatory population. The characteristic function simplifies the original two-dimensional system to a one-dimensional system, and the zero crossings of $F⁢(z)$ correspond to the fixed points of the original system. For $z\geq0$, we note:

$$
\frac{dF(z)}{dz}=J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−J_{EI}\alpha_{I}(det(J)⋅J_{EI}^{−1}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}+J_{EI}^{−1}J_{II})r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}−1=−\tau_{E}\tau_{I}\lambda_{1}\lambda_{2}
$$

Therefore, if the derivative of $F⁢(z)$ evaluated at one of its roots is positive, the corresponding fixed point is a saddle point. Note that as $r_{E}$ and $r_{I}$ increase, the term in parenthesis becomes dominant. To ensure that $\lambda_{1}⁢\lambda_{2}$ is negative also for large $r_{E}$ and $r_{I}$, the determinant of the weight matrix $det(J)$ has to be positive. Therefore, $det(J)$ has a decisive impact on the curvature of $F⁢(z)$. In systems with negative determinant, $F⁢(z)$ bends upwards for large $z$. In contrast, $F⁢(z)$ asymptotically bends downwards in systems with positive determinant. Hence, the high-activity steady-state of systems with negative determinant is unstable. In addition, we can simplify the above condition to the determinant of the weight matrix which is a necessary condition for network stability at any firing rate:

$$
det(J)=−J_{EE}J_{II}+J_{IE}J_{EI}>0
$$

To investigate how the network stability changes with input $g_{E}$, we examined how $F⁢(z)$ varies with changing input $g_{E}$ by calculating the derivative of $F⁢(z)$ with respect to $g_{E}$,

$$
\frac{dF(z)}{dg_{E}}=\alpha_{I}J_{II}[det(J)⋅J_{EI}^{−1}[z]_{+}^{\alpha_{E}}+J_{EI}^{−1}J_{II}z−J_{EI}^{−1}J_{II}g_{E}+g_{I}]_{+}^{\alpha_{I}−1}+1
$$

Since $\frac{d⁢F⁢(z)}{d⁢g_{E}}$ is positive, increasing $g_{E}$ always shifts $F⁢(z)$ upwards, eventually leading to the vanishing of all roots and, thus, unstable dynamics in supralinear networks with negative $det(J)$. In scenarios in which feedforward input to the inhibitory population also changes, we have

$$
\frac{dF(z)}{dt}=\frac{∂F(z)}{∂g_{E}}\frac{dg_{E}}{dt}+\frac{∂F(z)}{∂g_{I}}\frac{dg_{I}}{dt}=(\alpha_{I}J_{II}[det(J)⋅J_{EI}^{−1}[z]_{+}^{\alpha_{E}}+J_{EI}^{−1}J_{II}z−J_{EI}^{−1}J_{II}g_{E}+g_{I}]_{+}^{\alpha_{I}−1}+1)Δg_{E}−\alpha_{I}J_{EI}[det(J)⋅J_{EI}^{−1}[z]_{+}^{\alpha_{E}}+J_{EI}^{−1}J_{II}z−J_{EI}^{−1}J_{II}g_{E}+g_{I}]_{+}^{\alpha_{I}−1}Δg_{I}
$$

When the change in stimulation strength into the excitatory ($Δ⁢g_{E}$) and the inhibitory population ($Δ⁢g_{I}$) are the same, $\frac{d⁢F⁢(z)}{d⁢t}$ is always positive provided $J_{I⁢I}$ is greater than $J_{E⁢I}$. Hence, depending on the value of $\frac{J_{I⁢I}}{J_{E⁢I}}$, stimulation can lead to unstable network dynamics even when the input to the inhibitory population increases more than to the excitatory population.

### Spike-frequency adaptation (SFA)

We modeled SFA of excitatory neurons as an activity-dependent negative feedback current (Benda and Herz, 2003; Brette and Gerstner, 2005):

$$
\tau_{E}⁢\frac{d⁢r_{E}}{d⁢t}=-r_{E}+[J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+g_{E}]_{+}^{\alpha_{E}}-a
$$



$$
\tau_{I}⁢\frac{d⁢r_{I}}{d⁢t}=-r_{I}+[J_{I⁢E}⁢r_{E}-J_{I⁢I}⁢r_{I}+g_{I}]_{+}^{\alpha_{I}}
$$



$$
\tau_{a}⁢\frac{d⁢a}{d⁢t}=-a+b⁢r_{E}
$$

where $a$ is the adaptation variable, $\tau_{a}$ is the adaptation time constant, and $b$ is the adaptation strength.

#### Stability conditions in networks with SFA

The Jacobian $M_{SFA}$ of the system with SFA is given by

$$
M_{SFA}=[\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−\tau_{E}^{−1}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}−\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})0\tau_{a}^{−1}b0−\tau_{a}^{−1}]
$$

The characteristic polynomial of the system with SFA can be written as follows (Horn and Johnson, 1985):

$$
\lambda^{3}−tr(M_{SFA})\lambda^{2}+(A_{11}+A_{22}+A_{33})\lambda−det(M_{SFA})=0
$$

where $tr(M_{SFA})$ and $det(M_{SFA})$ are the trace and the determinant of the Jacobian matrix $M_{SFA}$, A11, A22, and A33 are the matrix cofactors. More specifically,

$$
tr(M_{SFA})=\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})−\tau_{a}^{−1}
$$



$$
A_{11}=|-\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})00-\tau_{a}^{-1}|=\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})⁢\tau_{a}^{-1}
$$



$$
A_{22}=|\tau_{E}^{-1}⁢(J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}-1)-\tau_{E}^{-1}\tau_{a}^{-1}⁢b-\tau_{a}^{-1}|=-\tau_{E}^{-1}⁢(J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}-1)⁢\tau_{a}^{-1}+\tau_{a}^{-1}⁢b⁢\tau_{E}^{-1}
$$



$$
A_{33}=|\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}−\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})|=−\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})+\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}
$$



$$
A_{11}+A_{22}+A_{33}=\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})\tau_{a}^{−1}−\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)\tau_{a}^{−1}+\tau_{a}^{−1}b\tau_{E}^{−1}−\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})+\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}
$$



$$
det(M_{SFA})=\tau_{E}^{−1}(J_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})\tau_{a}^{−1}−\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}\tau_{a}^{−1}−\tau_{a}^{−1}b\tau_{E}^{−1}\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})
$$

To ensure that the dynamics of the system are stable, the real parts of the eigenvalues of the Jacobian at the fixed point, and thus all roots of the characteristic polynomial have to be negative. Since the product of the roots is equal to $det(M_{SFA})$, $−det(M_{SFA})$ has to be positive. We then have

$$
b>\frac{\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}(J_{EE}−det(J)⋅\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})}{1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}}−1
$$

Since SFA does not modify the synaptic connections, the term $J_{EE}−det(J)⋅\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}$ is positive for networks with $det(J)<0$.

In the large $r_{E}$ limit, if $b$ is small such that the above condition cannot be fulfilled, $det(M_{SFA})$ is then positive, suggesting that the Jacobian of the system has always at least one positive eigenvalue. Therefore, the dynamics of the system cannot be stabilized in the presence of small $b$.

In addition, $A_{11}+A_{22}+A_{33}$ is equal to $\lambda_{1}⁢\lambda_{2}+\lambda_{2}⁢\lambda_{3}+\lambda_{1}⁢\lambda_{3}$, with the roots of the characteristic polynomial $\lambda_{1}$, $\lambda_{2}$, and $\lambda_{3}$. If all roots are real and negative, $A_{11}+A_{22}+A_{33}$ has to be positive. If one root is real and negative and two other roots are complex conjugates, to ensure that all roots have negative real parts, one necessary condition is $A_{11}+A_{22}+A_{33}§gt;0$. From the $tr(M_{SFA})$ and $det(M_{SFA})$ conditions, we have

$$
A_{11}+A_{22}+A_{33}§gt;\tau_{a}^{-1}⁢(-\tau_{a}^{-1}+b⁢\tau_{E}^{-1})-b⁢\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})
$$

As a result, if $\tau_{a}^{-1}⁢(-\tau_{a}^{-1}+b⁢\tau_{E}^{-1})-b⁢\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})§gt;0$, $A_{11}+A_{22}+A_{33}$ is guaranteed to be positive. We therefore have

$$
b⁢[\tau_{a}^{-1}⁢\tau_{E}^{-1}-\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})]§gt;\tau_{a}^{-2}
$$

Note that $\tau_{a}$ has to be small, in other words, SFA has to be fast, so that $\tau_{a}^{-1}⁢\tau_{E}^{-1}-\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})$ is positive for arbitrary $r_{I}$. For positive $\tau_{a}^{-1}⁢\tau_{E}^{-1}-\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})$, we have

$$
b§gt;\frac{\tau_{a}^{-2}}{\tau_{a}^{-1}⁢\tau_{E}^{-1}-\tau_{E}^{-1}⁢\tau_{I}^{-1}⁢(1+J_{I⁢I}⁢\alpha_{I}⁢r_{I}^{\frac{\alpha_{I}-1}{\alpha_{I}}})}
$$

Since $\tau_{a}$ has to be small, the above condition cannot be satisfied for small $b$.

Next, we consider the system with large $b$. Suppose that the firing rate $r_{E}$ and $r_{I}$ in the initial network are of order 1, and $b$ is of order $K$, where $K$ is a large number. We therefore have $−tr(M_{SFA})∼O(1)$, $A_{11}+A_{22}+A_{33}∼O⁢(K)$, and $−det(M_{SFA})∼O(K)$. The discriminant of the characteristic polynomial is

$$
(−tr(M_{SFA}))^{2}(A_{11}+A_{22}+A_{33})^{2}−4(A_{11}+A_{22}+A_{33})^{3}−4(−tr(M_{SFA}))^{3}(−det(M_{SFA}))−27(−det(M_{SFA}))^{2}+18(−tr(M_{SFA}))(A_{11}+A_{22}+A_{33})(−det(M_{SFA}))=(A_{11}+A_{22}+A_{33})^{3}[\frac{(−tr(M_{SFA}))^{2}}{A_{11}+A_{22}+A_{33}}−4−\frac{4(−tr(M_{SFA}))^{3}(−det(M_{SFA}))}{(A_{11}+A_{22}+A_{33})^{3}}−\frac{27(−det(M_{SFA}))^{2}}{(A_{11}+A_{22}+A_{33})^{3}}+\frac{18(−tr(M_{SFA}))(−det(M_{SFA}))}{(A_{11}+A_{22}+A_{33})^{2}}]
$$

Clearly, in the large $b$ limit, the discriminant is negative, suggesting that the characteristic polynomial has one real root and two complex conjugate roots (Irving, 2004).

As the input $g_{E}$ increases, the complex conjugate eigenvalues cross the imaginary axis when $tr(M_{SFA})(A_{11}+A_{22}+A_{33})$ equals $det(M_{SFA})$. As a result, the system undergoes a supercritical Hopf bifurcation. We numerically confirmed that the resulting limit cycle is stable (Figure 2—figure supplement 1), consistent with previous work (van Vreeswijk and Hansel, 2001). Thus, the system shows oscillatory behavior instead of stable steady state.

### Short-term plasticity (STP)

We modeled E-to-E STD following previous work (Tsodyks and Markram, 1997; Varela et al., 1997):

$$
\tau_{E}⁢\frac{d⁢r_{E}}{d⁢t}=-r_{E}+[x⁢J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+g_{E}]_{+}^{\alpha_{E}}
$$



$$
\tau_{I}⁢\frac{d⁢r_{I}}{d⁢t}=-r_{I}+[J_{I⁢E}⁢r_{E}-J_{I⁢I}⁢r_{I}+g_{I}]_{+}^{\alpha_{I}}
$$



$$
\frac{d⁢x}{d⁢t}=\frac{1-x}{\tau_{x}}-U_{d}⁢x⁢r_{E}
$$

where $x$ is the depression variable, which is limited to the interval $(0,1)$, $\tau_{x}$ is the depression time constant, and $U_{d}$ is the depression rate. The steady-state solution $x^{*}$ is given by

$$
x^{*}=\frac{1}{1+U_{d}⁢r_{E}⁢\tau_{x}}
$$

Similarly, we modeled E-to-I STF as

$$
\tau_{E}⁢\frac{d⁢r_{E}}{d⁢t}=-r_{E}+[J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+g_{E}]_{+}^{\alpha_{E}}
$$



$$
\tau_{I}⁢\frac{d⁢r_{I}}{d⁢t}=-r_{I}+[u⁢J_{I⁢E}⁢r_{E}-J_{I⁢I}⁢r_{I}+g_{I}]_{+}^{\alpha_{I}}
$$



$$
\frac{d⁢u}{d⁢t}=\frac{1-u}{\tau_{u}}+U_{f}⁢(U_{m⁢a⁢x}-u)⁢r_{E}
$$

where $u$ is the facilitation variable constrained to the interval $(1,U_{max})$ , $U_{m⁢a⁢x}$ is the maximal facilitation value, $\tau_{u}$ is the time constant of STF, and $U_{f}$ is the facilitation rate. The steady-state solution $u^{*}$ is given by

$$
u^{*}=\frac{1+U_{f}⁢U_{m⁢a⁢x}⁢r_{E}⁢\tau_{u}}{1+U_{f}⁢r_{E}⁢\tau_{u}}
$$

#### Stability conditions for networks with E-to-E STD

The Jacobian $M_{STD}$ of the system with E-to-E STD is given by

$$
M_{STD}=[\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{E}^{−1}J_{EE}\alpha_{E}r_{E}^{\frac{2\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}} −\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})0−U_{d}x0−\tau_{x}^{−1}−U_{d}r_{E}]
$$

and the characteristic polynomial can be written as follows:

$$
\lambda^{3}−tr(M_{STD})\lambda^{2}+(A_{11}+A_{22}+A_{33})\lambda−det(M_{STD})=0
$$

where $tr(M_{STD})$ and $det(M_{STD})$ are the trace and the determinant of the Jacobian matrix $M_{STD}$, A11, A22, and A33 are the matrix cofactors. More specifically,

$$
tr(M_{STD})=\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})−\tau_{x}^{−1}−U_{d}r_{E}
$$

In the case of unstable dynamics, $r_{E}$ goes to infinity due to run-away excitation. However, the depression variable $x$ approaches zero in this limit, as $lim_{r_{E}→∞}⁡x=lim_{r_{E}→∞}⁡\frac{1}{1+U_{d}⁢r_{E}⁢\tau_{x}}=0$. Therefore, in the large $r_{E}$ limit, $−tr(M_{STD})$ is positive.

$$
A_{11}+A_{22}+A_{33}=\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})(\tau_{x}^{−1}+U_{d}r_{E})+\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)(−\tau_{x}^{−1}−U_{d}r_{E})−\tau_{E}^{−1}J_{EE}\alpha_{E}r_{E}^{\frac{2\alpha_{E}−1}{\alpha_{E}}}(−U_{d}x)−\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})+\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}
$$

Similarly, in the large $r_{E}$ limit, $A_{11}+A_{22}+A_{33}$ is positive.

$$
det(M_{STD})=\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})(\tau_{x}^{−1}+U_{d}r_{E})−\tau_{E}^{−1}J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}\tau_{I}^{−1}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}(\tau_{x}^{−1}+U_{d}r_{E})−\tau_{E}^{−1}J_{EE}\alpha_{E}r_{E}^{\frac{2\alpha_{E}−1}{\alpha_{E}}}U_{d}x\tau_{I}^{−1}(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})
$$

Similarly, in the large $r_{E}$ limit, $−det(M_{STD})$ is positive.

According to the Descartes’ rule of signs, the number of positive roots is at most the number of sign changes in the sequences of polynomial’s coefficients. Therefore, there are no positive roots for the above characteristic polynomial and the network dynamics can be stabilized by E-to-E STD.

#### Characteristic function approximation for networks with E-to-E STD

As demonstrated above, E-to-E STD is able to restabilize the system, there exists a stable steady state for which the STD variable $x$ is constant $x=x^{*}$. Because $x$ changes slowly compared to the neuronal dynamics, we can approximate it as constant which results in a natural reduction to a 2D system in which the weights with STD are modified. The stability of this 2D system can be readily characterized by the characteristic function $F⁢(z)$ (Kraynyukova and Tchumatchenko, 2018), which depends on the previous steady state value of $x$. The characteristic function approximation with E-to-E STD can therefore be written as follows:

$$
F(z)=xJ_{EE}[z]_{+}^{\alpha_{E}}−J_{EI}[det(J_{STD})⋅J_{EI}^{−1}[z]_{+}^{\alpha_{E}}+J_{EI}^{−1}J_{II}z−J_{EI}^{−1}J_{II}g_{E}+g_{I}]_{+}^{\alpha_{I}}−z+g_{E}
$$

where

$$
det(J_{STD})=|xJ_{EE}−J_{EI}J_{IE}−J_{II}|=−xJ_{EE}J_{II}+J_{IE}J_{EI}
$$

Note that $det(J_{STD})$ can now change its sign due to E-to-E STD, the characteristic function can therefore change its bending shape. We used this relation to visualize how E-to-E STD effectively changes the network stability of the reduced system in Figure 2D.

#### Conditions for ISN in networks with E-to-E STD

Here, we identify the condition of being in the ISN regime in supralinear networks with E-to-E STD. When the level of inhibition is frozen, the Jacobian of the system reduces to the following:

$$
M_{1}=[\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)\tau_{E}^{−1}J_{EE}\alpha_{E}r_{E}^{\frac{2\alpha_{E}−1}{\alpha_{E}}}−U_{d}x−\tau_{x}^{−1}−U_{d}r_{E}]
$$

For the system with frozen inhibition, the dynamics are stable if

$$
tr(M_{1})=\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{x}^{−1}−U_{d}r_{E}<0
$$

and

$$
det(M_{1})=\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)(−\tau_{x}^{−1}−U_{d}r_{E})+\tau_{E}^{−1}J_{EE}\alpha_{E}r_{E}^{\frac{2\alpha_{E}−1}{\alpha_{E}}}U_{d}x>0
$$

Therefore, if the network is an ISN at the fixed point, the following condition has to be satisfied:

$$
x§gt;min⁢(\sqrt{\frac{1}{J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}}},\frac{\tau_{x}+\tau_{E}+\tau_{E}⁢\tau_{x}⁢U_{d}⁢r_{E}}{\tau_{x}⁢J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}})
$$

Furthermore, we define the largest real part of the eigenvalues of $M_{1}$ as the ISN index for networks with E-to-E STD. More specifically,

$$
ISN index=Re[\frac{\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)−\tau_{x}^{−1}−U_{d}r_{E}}{2}+\sqrt{\frac{1}{4}(\tau_{E}^{−1}(xJ_{EE}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}−1)+\tau_{x}^{−1}+U_{d}r_{E})^{2}−\tau_{E}^{−1}J_{EE}\alpha_{E}r_{E}^{\frac{2\alpha_{E}−1}{\alpha_{E}}}U_{d}x}]
$$

#### Conditions for paradoxical response in networks with E-to-E STD

Next, we identify the condition of having the paradoxical effect in supralinear networks with E-to-E STD. To that end, we exploit a separation of timescales between the fast neural activity and the slow STP variable. Therefore, set the depression variable to its value at the fixed point corresponding to the fixed point value of $r_{E}$. The excitatory nullcline is defined as follows

$$
\tau_{E}⁢\frac{d⁢r_{E}}{d⁢t}=-r_{E}+[\frac{1}{1+\tau_{x}⁢U_{d}⁢r_{E}}⁢J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+g_{E}]_{+}^{\alpha_{E}}=0
$$

For $r_{E,I}§gt;0$, we have

$$
r_{I}=\frac{\frac{1}{1+\tau_{x}⁢U_{d}⁢r_{E}}⁢J_{E⁢E}⁢r_{E}-r_{E}^{\frac{1}{\alpha_{E}}}+g_{E}}{J_{E⁢I}}
$$

The slope of the excitatory nullcline in the $r_{E}/r_{I}$ plane where $x$ axis is $r_{E}$ and $y$ axis is $r_{I}$ can be written as follows

$$
k_{S⁢T⁢D}^{E}=\frac{1}{J_{E⁢I}}⁢(-\frac{J_{E⁢E}}{(1+\tau_{x}⁢U_{d}⁢r_{E})^{2}}⁢\tau_{x}⁢U_{d}⁢r_{E}+\frac{J_{E⁢E}}{1+\tau_{x}⁢U_{d}⁢r_{E}}-\frac{1}{\alpha_{E}}⁢r_{E}^{\frac{1}{\alpha_{E}}-1})
$$

Note that the slope of the excitatory nullcline is nonlinear. To have paradoxical effect, the slope of the excitatory nullcline at the fixed point of the system has to be positive. Therefore, the STD variable $x$ at the fixed point has to satisfy the following condition

$$
x§gt;\sqrt{\frac{1}{J_{E⁢E}⁢\alpha_{E}⁢r_{E}^{\frac{\alpha_{E}-1}{\alpha_{E}}}}}
$$

The inhibitory nullcline can be written as follows

$$
\tau_{I}⁢\frac{d⁢r_{I}}{d⁢t}=-r_{I}+[J_{I⁢E}⁢r_{E}-J_{I⁢I}⁢r_{I}+g_{I}]_{+}^{\alpha_{I}}=0
$$

In the region of rates $r_{E,I}§gt;0$, we have

$$
r_{I}=\frac{J_{I⁢E}⁢r_{E}-r_{I}^{\frac{1}{\alpha_{I}}}+g_{I}}{J_{I⁢I}}
$$

The slope of the inhibitory nullcline can be written as follows

$$
k_{S⁢T⁢D}^{I}=\frac{J_{I⁢E}}{J_{I⁢I}+\frac{1}{\alpha_{I}}⁢r_{I}^{\frac{1-\alpha_{I}}{\alpha_{I}}}}
$$

In addition to the positive slope of the excitatory nullcline, the slope of the inhibitory nullcline at the fixed point of the system has to be larger than the slope of the excitatory nullcline. We therefore have

$$
J_{EI}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}J_{IE}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}}(\tau_{x}^{−1}+U_{d}r_{E})>(1+J_{II}\alpha_{I}r_{I}^{\frac{\alpha_{I}−1}{\alpha_{I}}})(−\frac{J_{EE}U_{d}r_{E}}{1+\tau_{x}U_{d}r_{E}}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}+\frac{J_{EE}}{1+\tau_{x}U_{d}r_{E}}\alpha_{E}r_{E}^{\frac{\alpha_{E}−1}{\alpha_{E}}}(\tau_{x}^{−1}+U_{d}r_{E})−(\tau_{x}^{−1}+U_{d}r_{E}))
$$

The above condition is the same as the stability condition of the determinant of the Jacobian of the system with E-to-E STD (Eq. (49)). Therefore, the condition is always satisfied when the system with E-to-E STD is stable.

Based on the condition of being ISN shown in Eq. (55) and the condition of having paradoxical effect shown in Eq. (60), we therefore can conclude that in supralinear networks with E-to-E STD, the paradoxical effect implies inhibitory stabilization, whereas inhibitory stabilization does not necessarily imply paradoxical responses. This is consistent with recent work by Sanzeni et al., 2020, in which threshold-linear networks with STP have been studied. Here, we showed analytically that the conclusion holds for any rectified power-law activation function with positive $\alpha$.

To visualize the conditions in a two-dimensional plane, we reduced the conditions into a function of $J_{E⁢E}$ and $x$. For Figure 2G, $r_{E}=1$. In Figure 2—figure supplement 5 and Figure 2—figure supplement 8, the depression variable thresholds above which the network exhibits the paradoxical effect were calculated based on Eq. (60).

### Uni-stability conditions

The system is said to be ‘uni-stable’, when it has a single stable fixed point. We first identified the uni-stability condition for networks with global inhibition. To that end, we considered a general network with $N$ excitatory populations and $N$ inhibitory populations. To treat this problem analytically, we did not take STP into account in our analysis. The Jacobian matrix of networks with global inhibition $Q$, can be written as follows,

$$
Q=[J_{E←E}J_{E←I}J_{I←E}J_{I←I}]
$$

where $J_{E←E}$, $J_{E←I}$, $J_{I←E}$, and $J_{I←I}$ are $N$ by $N$ block matrices defined below.

$$
J_{E←E}=[a−eka⋯kakaa−e⋯ka⋮⋮⋱⋮kaka⋯a−e]
$$



$$
J_{E←I}=−bJ_{N,N}
$$



$$
J_{I←E}=cJ_{N,N}
$$



$$
J_{I←I}=[−d−f−d⋯−d−d−d−f⋯−d⋮⋮⋱⋮−d−d⋯−d−f]
$$

where $a=\tau_{E}^{-1}⁢J_{E⁢E}⁢\alpha_{E}⁢[z_{E}]_{+}^{\alpha_{E}-1}$, $b=\tau_{E}^{-1}⁢J_{E⁢I}⁢\alpha_{E}⁢[z_{E}]_{+}^{\alpha_{E}-1}$, $c=\tau_{I}^{-1}⁢J_{I⁢E}⁢\alpha_{I}⁢[z_{I}]_{+}^{\alpha_{I}-1}$, $d=\tau_{I}^{-1}⁢J_{I⁢I}⁢\alpha_{I}⁢[z_{I}]_{+}^{\alpha_{I}-1}$, $e=\tau_{E}^{-1}$, and $f=\tau_{I}^{-1}$. Here, $z_{E}$ and $z_{I}$ denote the total current into the excitatory and inhibitory population, respectively. Note that all these parameters are non-negative. Parameter $k$ controls the excitatory connection strength across different populations. $J_{N,N}$ is a $N$ by $N$ matrix of ones.

The eigenvalues of the Jacobian $Q$ are roots of its characteristic polynomial,

$$
det((J_{E←E}−\lambda1)(J_{I←I}−\lambda1)−J_{E←I}J_{I←E})=0
$$

where $1$ represents the identity matrix of size $N$. The characteristic polynomial can be expanded to:

$$
[(a-e-k⁢a-\lambda)⁢(-f-\lambda)]^{N-1}⁢[(a-e+(N-1)⁢k⁢a-\lambda)⁢(-N⁢d-f-\lambda)+N^{2}⁢b⁢c]=0
$$

We therefore had four distinct eigenvalues:

$$
\lambda_{1}=a-e-k⁢a
$$



$$
\lambda_{2}=-f
$$

and

$$
\lambda_{3/4}=\frac{1}{2}[(a−e−f−Nd+(N−1)ka)\pm\sqrt{(a−e−f−Nd+(N−1)ka)^{2}−4((−af+ef+kaf)−N(a−e)d−Nkaf−N(N−1)kad+N^{2}bc)}]
$$

Note that the eigenvalues $\lambda_{1}$ and $\lambda_{2}$ have an algebraic and geometric multiplicity of ($N$–1), whereas the eigenvalues $\lambda_{3}$ and $\lambda_{4}$ have an algebraic and geometric multiplicity of 1.

In analogy to networks with global inhibition, the Jacobian matrix of networks with co-tuned inhibition $R$, can be written as

$$
R=[J_{E←E}J_{E←I}J_{I←E}J_{I←I}]
$$

where $J_{E←E}$, $J_{E←I}$, $J_{I←E}$, and $J_{I←I}$ are $N$ by $N$ block matrices defined as follows:

$$
J_{E←E}=[a−eka⋯kakaa−e⋯ka⋮⋮⋱⋮kaka⋯a−e]
$$



$$
J_{E←I}=[−Nb+(N−1)mb−mb⋯−mb−mb−Nb+(N−1)mb⋯−mb⋮⋮⋱⋮−mb−mb⋯−Nb+(N−1)mb]
$$



$$
J_{I←E}=[Nc−(N−1)mcmc⋯mcmcNc−(N−1)mc⋯mc⋮⋮⋱⋮mcmc⋯Nc−(N−1)mc]
$$



$$
J_{I←I}=[−Nd+(N−1)md−f−md⋯−md−md−Nd+(N−1)md−f⋯−md⋮⋮⋱⋮−md−md⋯−Nd+(N−1)md−f]
$$

where $m$ controls the degree of co-tuning in the network. If $m=0$, the network decouples into $N$ independent ensembles and inhibition is perfectly co-tuned with excitation. In the case $m=1$, inhibition is global and the block matrices become identical to the above case of global inhibition.

The eigenvalues of the matrix $R$ are given as the roots of the characteristic polynomial defined by:

$$
det((J_{E←E}−\lambda1)(J_{I←I}−\lambda1)−J_{E←I}J_{I←E})=0
$$

which yields the following expression:

$$
[\lambda^{2}-(a-e-k⁢a-N⁢d+N⁢m⁢d-f)⁢\lambda-(a-e-k⁢a)⁢(N⁢d-N⁢m⁢d-f)+N^{2}⁢b⁢c⁢(1-m)^{2}]^{N-1}⁢[(a-e+(N-1)⁢k⁢a-\lambda)⁢(-N⁢d-f-\lambda)+N^{2}⁢b⁢c]=0
$$

We therefore had four distinct eigenvalues:

$$
\lambda_{1/2}^{^{′}}=\frac{1}{2}⁢[(a-e-k⁢a-N⁢d+N⁢m⁢d-f)\pm\sqrt{(a-e-k⁢a+N⁢d-N⁢m⁢d+f)^{2}-4⁢N^{2}⁢b⁢c⁢(1-m)^{2}}]
$$



$$
\lambda_{3/4}^{^{′}}=\frac{1}{2}[(a−e−f−Nd+(N−1)ka)\pm\sqrt{(a−e−f−Nd+(N−1)ka)^{2}−4((−af+ef+kaf)−N(a−e)d−Nkaf−N(N−1)kad+N^{2}bc)}]
$$

The eigenvalues $\lambda_{1}^{^{′}}$ and $\lambda_{2}^{^{′}}$ have an algebraic and geometric multiplicity of ($N$–1), whereas the eigenvalues $\lambda_{3}^{^{′}}$ and $\lambda_{4}^{^{′}}$ have an algebraic and geometric multiplicity of 1. We noted that $\lambda_{3}=\lambda_{3}^{^{′}}$, $\lambda_{4}=\lambda_{4}^{^{′}}$.

To compare under which conditions networks with different structures are uni-stable, we examined the different eigenvalues derived above. As $\lambda_{2}§lt;0$, and $\lambda_{1}^{^{′}}§gt;\lambda_{2}^{^{′}}$, we only had to compare $\lambda_{1}^{^{′}}$ to $\lambda_{1}$. For networks with co-tuned inhibition, we have $m§lt;1$,

$$
\lambda_{1}^{^{′}}=\frac{1}{2}[(a−e−ka−Nd+Nmd−f)+\sqrt{(a−e−ka+Nd−Nmd+f)^{2}−4N^{2}bc(1−m)^{2}}]<\frac{1}{2}[(a−e−ka−Nd+Nmd−f)+\sqrt{(a−e−ka+Nd−Nmd+f)^{2}}]=a−e−ka=\lambda_{1}
$$

The inequality, $\lambda_{1}^{^{′}}§lt;\lambda_{1}$, indicates that networks with co-tuned inhibition have a broad parameter regime in which they are uni-stable than networks with global inhibition. Note that in the absence of a saturating nonlinearity of the input-output function and in the absence of any additional stabilization mechanisms, systems with positive eigenvalues of the Jacobian are unstable. In this case, networks with co-tuned inhibition have a broad parameter regime of being stable than networks with global inhibition.

To visualize the conditions in a two-dimensional plane, we reduced the conditions into a function of $a$ and $d$. For Figure 3C, $k=0.1$, $m=0.5$ and $b⁢c=0.9⁢a⁢d$.

### Distance to the decision boundary

To calculate the distance to the decision boundary in Figures 4 and 5, Figure 4—figure supplement 2 and Figure 5—figure supplement 2, we first projected the excitatory activity in Phase two onto a two-dimensional Cartesian coordinate system in which the horizontal axis is the activity of the first excitatory ensemble $r_{E⁢1}$ and the vertical axis is the activity of the second excitatory ensemble $r_{E⁢2}$. We denote the location of the projected data point in the Cartesian coordinate system by ($x$, $y$), where $x$ and $y$ equal $r_{E⁢1}$ and $r_{E⁢2}$, respectively. The distance $L$ between the projected data and the decision boundary which corresponds to the diagonal line in the coordinate system can be expressed as follows:

$$
L=\sqrt{x^{2}+y^{2}}⁢sin⁢(|45^{o}-arcsin⁢(\frac{x}{\sqrt{x^{2}+y^{2}}})|)
$$

Note that the inverse trigonometric function arcsin gives the value of the angle in degrees.

### Inhibitory feedback pathways for suppressing unwanted neural activation

To identify the important neural pathways for the suppression of unwanted neural activation, we analyzed how the activity of the second excitatory ensemble $r_{E⁢2}$ changes with the input to the first excitatory ensemble $g_{E⁢1}$. To that end, we considered a general weight matrix for networks with two interacting ensembles

$$
J=[J_{E1E1}J_{E1E2}−J_{E1I1}−J_{E1I2}J_{E2E1}J_{E2E2}−J_{E2I1}−J_{E2I2}J_{I1E1}J_{I1E2}−J_{I1I1}−J_{I1I2}J_{I2E1}J_{I2E2}−J_{I2I1}−J_{I2I2}]
$$

We can write the change in firing rate of the excitatory population in the second ensemble $\delta⁢r_{E⁢2}$ as a function of the change in the input to the other $\delta⁢g_{E⁢1}$:

$$
\deltar_{E2}=\frac{1}{det(1−FJ)}[(−f_{E2}^{^{′}}J_{E2E1})f_{I1}^{^{′}}J_{I1I2}f_{I2}^{^{′}}J_{I2I1}+f_{E2}^{^{′}}J_{E2I1}(−f_{I1}^{^{′}}J_{I1E1})(1+f_{I2}^{^{′}}J_{I2I2})+f_{E2}^{^{′}}J_{E2I2}(1+f_{I1}^{^{′}}J_{I1I1})(−f_{I2}^{^{′}}J_{I2E1})−(−f_{E2}^{^{′}}J_{E2E1})(1+f_{I1}^{^{′}}J_{I1I1})(1+f_{I2}^{^{′}}J_{I2I2})−f_{E2}^{^{′}}J_{E2I1}f_{I1}^{^{′}}J_{I1I2}(−f_{I2}^{^{′}}J_{I2E1})−f_{E2}^{^{′}}J_{E2I2}(−f_{I1}^{^{′}}J_{I1E1})f_{I2}^{^{′}}J_{I2I1}]f_{E1}^{^{′}}\deltag_{E1}
$$

where $1$ is the identity matrix. And $F$ is given by

$$
F=[f_{E1}^{^{′}}0000f_{E2}^{^{′}}0000f_{I1}^{^{′}}0000f_{I2}^{^{′}}]
$$

where $f_{E⁢1}^{^{′}}$, $f_{E⁢2}^{^{′}}$, $f_{I⁢1}^{^{′}}$ and $f_{I⁢2}^{^{′}}$ are the derivatives of the input-output functions evaluated at the fixed point.

Assuming that $J_{E⁢1⁢E⁢1}=J_{E⁢2⁢E⁢2}=J_{E⁢E}$, $J_{I⁢1⁢E⁢1}=J_{I⁢2⁢E⁢2}=J_{I⁢E}$, $J_{E⁢1⁢I⁢1}=J_{E⁢2⁢I⁢2}=J_{E⁢I}$, $J_{I⁢1⁢I⁢1}=J_{I⁢2⁢I⁢2}=J_{I⁢I}$, $J_{E⁢1⁢E⁢2}=J_{E⁢2⁢E⁢1}=J_{E⁢E}^{^{′}}$, $J_{I⁢1⁢E⁢2}=J_{I⁢2⁢E⁢1}=J_{I⁢E}^{^{′}}$, $J_{E⁢1⁢I⁢2}=J_{E⁢2⁢I⁢1}=J_{E⁢I}^{^{′}}$ and $J_{I⁢1⁢I⁢2}=J_{I⁢2⁢I⁢1}=J_{I⁢I}^{^{′}}$, we find

$$
\deltar_{E2}=\frac{1}{det(1−FJ)}[(−f_{E2}^{^{′}}J_{EE}^{^{′}})f_{I1}^{^{′}}J_{II}^{^{′}}f_{I2}^{^{′}}J_{II}^{^{′}}+f_{E2}^{^{′}}J_{EI}^{^{′}}(−f_{I1}^{^{′}}J_{IE})(1+f_{I2}^{^{′}}J_{II})+f_{E2}^{^{′}}J_{EI}(1+f_{I1}^{^{′}}J_{II})(−f_{I2}^{^{′}}J_{IE}^{^{′}})−(−f_{E2}^{^{′}}J_{EE}^{^{′}})(1+f_{I1}^{^{′}}J_{II})(1+f_{I2}^{^{′}}J_{II})−f_{E2}^{^{′}}J_{EI}^{^{′}}f_{I1}^{^{′}}J_{II}^{^{′}}(−f_{I2}^{^{′}}J_{IE}^{^{′}})−f_{E2}^{^{′}}J_{EI}(−f_{I1}^{^{′}}J_{IE})f_{I2}^{^{′}}J_{II}^{^{′}}]f_{E1}^{^{′}}\deltag_{E1}
$$

By further assuming that the weight strengths across ensembles are weak and ignoring the corresponding higher-order terms, we get

$$
\deltar_{E2}≈\frac{1}{det(1−FJ)}[f_{E2}^{^{′}}J_{EI}^{^{′}}(−f_{I1}^{^{′}}J_{IE})(1+f_{I2}^{^{′}}J_{II})+f_{E2}^{^{′}}J_{EI}(1+f_{I1}^{^{′}}J_{II})(−f_{I2}^{^{′}}J_{IE}^{^{′}})−(−f_{E2}^{^{′}}J_{EE}^{^{′}})(1+f_{I1}^{^{′}}J_{II})(1+f_{I2}^{^{′}}J_{II})−f_{E2}^{^{′}}J_{EI}(−f_{I1}^{^{′}}J_{IE})f_{I2}^{^{′}}J_{II}^{^{′}}]f_{E1}^{^{′}}\deltag_{E1}=\frac{1}{det(1−FJ)}[(\frac{J_{II}^{^{′}}}{J_{EI}^{^{′}}}f_{I2}^{^{′}}−(\frac{1}{J_{EI}}+f_{I2}^{^{′}}\frac{J_{II}}{J_{EI}}))J_{EI}^{^{′}}J_{EI}J_{IE}f_{E2}^{^{′}}f_{I1}^{^{′}}+(\frac{J_{EE}^{^{′}}}{J_{IE}^{^{′}}}(1+J_{II}f_{I2}^{^{′}})−J_{EI}f_{I2}^{^{′}})J_{IE}^{^{′}}f_{E2}^{^{′}}(1+f_{I1}^{^{′}}J_{II})]f_{E1}^{^{′}}\deltag_{E1}
$$

Note that $\frac{J_{E⁢E}^{^{′}}}{J_{I⁢E}^{^{′}}}$ and $\frac{J_{I⁢I}^{^{′}}}{J_{E⁢I}^{^{′}}}$ are terms regulating the respective excitatory and inhibitory input from one ensemble to the excitatory and inhibitory population in another ensemble. The term $det(1−FJ)$ is positive to ensure the stability of the system.

To suppress the activity of the excitatory population in the second ensemble $r_{E⁢2}$, in other words, to ensure that $\delta⁢r_{E⁢2}§lt;0$, $J_{I⁢E}^{^{′}}$ or/and $J_{E⁢I}^{^{′}}$ have to be large. Therefore, we identified $J_{I⁢E}^{^{′}}$ and $J_{E⁢I}^{^{′}}$ as important synaptic connections which lead to suppression of the unwanted neural activation, suggesting that inhibition can be provided via $J_{I⁢E}^{^{′}}$ through the $E⁢1$-$I⁢2$-$E⁢2$ pathway or via $J_{E⁢I}^{^{′}}$ through the $E⁢1$-$I⁢1$-$E⁢2$ pathway.

For Figures 4 and 5, the rate-based model consists of two ensembles, each of which is composed of 100 excitatory and 25 inhibitory neurons with all-to-all connectivity.

### Spiking neural network model

The spiking neural network model was composed of $N_{E}$ excitatory and $N_{I}$ inhibitory leaky integrate-and-fire neurons. Neurons were randomly connected with probability of 20%. The dynamics of membrane potential of neuron i, $U_{i}$, as defined by Zenke et al., 2015:

$$
\tau^{m}⁢\frac{d⁢U_{i}}{d⁢t}=(U^{rest}-U_{i})+g_{i}^{ext}⁢(t)⁢(U^{exc}-U_{i})+g_{i}^{inh}⁢(t)⁢(U^{inh}-U_{i})
$$

Here, $\tau^{m}$ is the membrane time constant and $U^{rest}$ is the resting potential. Spikes are triggered when the membrane potential reaches the spiking threshold $U^{thr}$. After a spike is emitted, the membrane potential is reset to $U^{rest}$ and the neuron enters a refractory period of $\tau^{ref}$. Inhibitory neurons obeyed the same integrate-and-fire formalism but with a shorter membrane time constant.

Excitatory synapses contain a fast AMPA component and a slow NMDA component. The dynamics of the excitatory conductance are described by:

$$
\tau^{ampa}⁢\frac{d⁢g_{i}^{ampa}}{d⁢t}=-g_{i}^{ampa}+\sumj\inexcJ_{i⁢j}⁢S_{j}⁢(t)
$$



$$
\tau^{nmda}⁢\frac{d⁢g_{i}^{nmda}}{d⁢t}=-g_{i}^{nmda}+g_{i}^{ampa}
$$



$$
g_{i}^{exc}⁢(t)=ξ⁢g_{i}^{ampa}⁢(t)+(1-ξ)⁢g_{i}^{nmda}⁢(t)
$$

Here, $J_{i⁢j}$ denotes the synaptic strength from neuron $j$ to neuron i. If the connection does not exist, $J_{i⁢j}$ was set to 0. $S_{j}⁢(t)$ is the spike train of neuron $j$, which is defined as $S_{j}⁢(t)=\sum_{k}\delta⁢(t-t_{j}^{k})$, where $\delta$ is the Dirac delta function and $t_{j}^{k}$ the spikes times $k$ of neuron $j$. $ξ$ is a weighting parameter. The dynamics of inhibitory conductances are governed by:

$$
\tau^{gaba}⁢\frac{d⁢g_{i}^{inh}}{d⁢t}=-g_{i}^{inh}+\sumj\ininhJ_{i⁢j}⁢S_{j}⁢(t)
$$

In the spiking neural network models, SFA of excitatory neurons is modeled as follows,

$$
\tau^{m}⁢\frac{d⁢U_{i}}{d⁢t}=(U^{rest}-U_{i})+g_{i}^{ext}⁢(t)⁢(U^{exc}-U_{i})+(g_{i}^{inh}⁢(t)+a_{i}⁢(t))⁢(U^{inh}-U_{i})
$$



$$
\frac{d⁢a_{i}}{d⁢t}=-\frac{a_{i}}{\tau_{a}}+b⁢S_{i}⁢(t)
$$

where i is the index of excitatory neurons.

The dynamics of E-to-E STD are given by

$$
\frac{d⁢x_{i⁢j}}{d⁢t}=\frac{1-x_{i⁢j}}{\tau_{x}}-U_{d}⁢x_{i⁢j}⁢S_{j}⁢(t)
$$



$$
\tau^{ampa}⁢\frac{d⁢g_{i}^{ampa}}{d⁢t}=-g_{i}^{ampa}+\sumj\inexcx_{i⁢j}⁢J_{i⁢j}⁢S_{j}⁢(t)
$$

where i represents the index of excitatory neurons.

The dynamics of E-to-I STF are governed by

$$
\frac{d⁢u_{i⁢j}}{d⁢t}=\frac{1-u_{i⁢j}}{\tau_{u}}+U_{f}⁢(U_{m⁢a⁢x}-u_{i⁢j})⁢S_{j}⁢(t)
$$



$$
\tau^{ampa}⁢\frac{d⁢g_{i}^{ampa}}{d⁢t}=-g_{i}^{ampa}+\sumj\inexcu_{i⁢j}⁢J_{i⁢j}⁢S_{j}⁢(t)
$$

where i denotes the index of inhibitory neurons.

For Figure 6, each excitatory and inhibitory neuron received external excitatory input from 300 neurons firing with Poisson statistics at an average firing rate of 0.1 Hz at baseline. During stimulation, the excitatory neurons corresponding to the activated ensemble received external excitatory input from 300 neurons firing with Poisson statistics at an average firing rate of 0.5 Hz. The ensemble activity is computed from the instantaneous firing rates of the respective ensembles with 10ms bin size. The difference in ensemble activity for the peak amplitude is calculated by subtracting the average maximal ensemble activity of the unstimulated ensembles from the maximal ensemble activity of the activated ensemble. Similarly, the difference in ensemble activity for the fixed point is calculated by subtracting the average ensemble activity of the unstimulated ensembles at the fixed point from the ensemble activity of the activated ensemble at the fixed point. Fixed point activity is computed by averaging the activity of the middle 1 second within the 2-second stimulation period.

For Figure 2—figure supplement 10, each excitatory and inhibitory neuron received external excitatory input from 300 neurons firing with Poisson statistics at an average firing rate of 0.1 Hz at the baseline. During stimulation, each excitatory neuron received external excitatory input from 300 neurons firing with Poisson statistics at an average firing rate of 0.3 Hz.

For Figure 6—figure supplement 1, the firing rates of 300 neurons are varying from $4/15$ Hz to $7/15$ Hz.

### Simulations

Simulations were performed in Python and Mathematica. All differential equations were implemented by Euler integration with a time step of 0.1 ms. All simulation parameters are listed in Tables 1–5 and Appendix 5—Tables 1–10. The simulation source code to reproduce the figures is publicly available at https://github.com/fmi-basel/gzenke-nonlinear-transient-amplification (Wu, 2021 copy archived at swh:1:rev:6ff6ff10b9f4994a0f948a987a66cc82f98451e1).

**Table 1.**
 Parameters for Figure 1C–E.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Value</th>
      <th>Unit</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>JE⁢E</td>
      <td>1.8</td>
      <td>-</td>
      <td>E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢E</td>
      <td>1.0</td>
      <td>-</td>
      <td>E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I</td>
      <td>1.0</td>
      <td>-</td>
      <td>I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I</td>
      <td>0.6</td>
      <td>-</td>
      <td>I-to-I connection strength</td>
    </tr>
    <tr>
      <td>αE</td>
      <td>2</td>
      <td>-</td>
      <td>Power of excitatory input-output function</td>
    </tr>
    <tr>
      <td>αI</td>
      <td>2</td>
      <td>-</td>
      <td>Power of inhibitory input-output function</td>
    </tr>
    <tr>
      <td>τE</td>
      <td>20</td>
      <td>ms</td>
      <td>Time constant of excitatory firing dynamics</td>
    </tr>
    <tr>
      <td>τI</td>
      <td>10</td>
      <td>ms</td>
      <td>Time constant of inhibitory firing dynamics</td>
    </tr>
    <tr>
      <td>gEb⁢s</td>
      <td>1.55</td>
      <td>-</td>
      <td>Input to the E population at baseline</td>
    </tr>
    <tr>
      <td>gEs⁢t⁢i⁢m</td>
      <td>3.0</td>
      <td>-</td>
      <td>Input to the E population during stimulation</td>
    </tr>
    <tr>
      <td>gI</td>
      <td>2.0</td>
      <td>-</td>
      <td>Input to the I population</td>
    </tr>
    <tr>
      <td colspan="4">Parameters for Figure 1F</td>
    </tr>
    <tr>
      <td>JI⁢E</td>
      <td>0.45</td>
      <td>-</td>
      <td>E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I</td>
      <td>1.0</td>
      <td>-</td>
      <td>I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I</td>
      <td>1.5</td>
      <td>-</td>
      <td>I-to-I connection strength</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Parameters for Figure 2.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Value</th>
      <th>Unit</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>τa</td>
      <td>200</td>
      <td>ms</td>
      <td>Time constant of SFA</td>
    </tr>
    <tr>
      <td>b</td>
      <td>1.0</td>
      <td>-</td>
      <td>Strength of SFA</td>
    </tr>
    <tr>
      <td>τx</td>
      <td>200</td>
      <td>ms</td>
      <td>Time constant of STD</td>
    </tr>
    <tr>
      <td>Ud</td>
      <td>1.0</td>
      <td>-</td>
      <td>Depression rate</td>
    </tr>
    <tr>
      <td>τu</td>
      <td>200</td>
      <td>ms</td>
      <td>Time constant of STF</td>
    </tr>
    <tr>
      <td>Uf</td>
      <td>1.0</td>
      <td>-</td>
      <td>Facilitation rate</td>
    </tr>
    <tr>
      <td>Um⁢a⁢x</td>
      <td>6.0</td>
      <td>-</td>
      <td>Maximal facilitation value</td>
    </tr>
    <tr>
      <td colspan="4">Note that these values are also applied elsewhere unless mentioned otherwise.</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Parameters for Figure 3 bi/multi-stable example.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Value</th>
      <th>Unit</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>JE⁢E</td>
      <td>1.4</td>
      <td>-</td>
      <td>Within-ensemble E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢E</td>
      <td>0.6</td>
      <td>-</td>
      <td>Within-ensemble E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I</td>
      <td>1.0</td>
      <td>-</td>
      <td>Within-ensemble I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I</td>
      <td>0.6</td>
      <td>-</td>
      <td>Within-ensemble I-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢E′</td>
      <td>0.14</td>
      <td>-</td>
      <td>Inter-ensemble E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢E′</td>
      <td>0.6</td>
      <td>-</td>
      <td>Inter-ensemble E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I′</td>
      <td>1.0</td>
      <td>-</td>
      <td>Inter-ensemble I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I′</td>
      <td>0.6</td>
      <td>-</td>
      <td>Inter-ensemble I-to-I connection strength</td>
    </tr>
    <tr>
      <td>gE⁢1b⁢s</td>
      <td>2.2</td>
      <td>-</td>
      <td>Input to the E1 population at baseline</td>
    </tr>
    <tr>
      <td>gE⁢1s⁢t⁢i⁢m</td>
      <td>3.0</td>
      <td>-</td>
      <td>Input to the E1 population during stimulation</td>
    </tr>
    <tr>
      <td>gE⁢2</td>
      <td>2.2</td>
      <td>-</td>
      <td>Input to the E2 population</td>
    </tr>
    <tr>
      <td>gI</td>
      <td>2.0</td>
      <td>-</td>
      <td>Input to the I population</td>
    </tr>
    <tr>
      <td colspan="4">Parameters for Figure 3 uni-stable example</td>
    </tr>
    <tr>
      <td>JE⁢E</td>
      <td>1.3</td>
      <td>-</td>
      <td>Within-ensemble E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JE⁢E′</td>
      <td>0.13</td>
      <td>-</td>
      <td>Inter-ensemble E-to-E connection strength</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Parameters for Figures 4 and 5.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Value</th>
      <th>Unit</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NE</td>
      <td>200</td>
      <td>-</td>
      <td>Number of excitatory neurons</td>
    </tr>
    <tr>
      <td>NI</td>
      <td>50</td>
      <td>-</td>
      <td>Number of inhibitory neurons</td>
    </tr>
    <tr>
      <td>N</td>
      <td>2</td>
      <td>-</td>
      <td>Number of ensembles</td>
    </tr>
    <tr>
      <td>JE⁢E</td>
      <td>1.2/(NE/2-1)</td>
      <td>-</td>
      <td>Within-ensemble E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢E</td>
      <td>1.0/(NE/2)</td>
      <td>-</td>
      <td>Within-ensemble E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I</td>
      <td>1.0/(NI/2)</td>
      <td>-</td>
      <td>Within-ensemble I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I</td>
      <td>1.0/(NI/2-1)</td>
      <td>-</td>
      <td>Within-ensemble I-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢E′</td>
      <td>0.36/(NE/2-1)</td>
      <td>-</td>
      <td>Inter-ensemble E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢E′</td>
      <td>0.4/(NE/2)</td>
      <td>-</td>
      <td>Inter-ensemble E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I′</td>
      <td>0.1/(NI/2)</td>
      <td>-</td>
      <td>Inter-ensemble I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I′</td>
      <td>0.1/(NI/2)</td>
      <td>-</td>
      <td>Inter-ensemble I-to-I connection strength</td>
    </tr>
    <tr>
      <td>gI</td>
      <td>2.0</td>
      <td>-</td>
      <td>Input to the I population</td>
    </tr>
    <tr>
      <td colspan="4">Parameters for Figure 4</td>
    </tr>
    <tr>
      <td>gE⁢1b⁢s</td>
      <td>1.35</td>
      <td>-</td>
      <td>Input to the E1 population</td>
    </tr>
    <tr>
      <td>gE⁢1s⁢t⁢i⁢m</td>
      <td>4.0</td>
      <td>-</td>
      <td>Input to the E1 population during stimulation</td>
    </tr>
    <tr>
      <td>gE⁢2</td>
      <td>1.35</td>
      <td>-</td>
      <td>Input to the E2 population</td>
    </tr>
    <tr>
      <td colspan="4">Parameters for Figure 5</td>
    </tr>
    <tr>
      <td>gE⁢1b⁢s</td>
      <td>1.35</td>
      <td>-</td>
      <td>Input to the E1 population at baseline</td>
    </tr>
    <tr>
      <td>gE⁢1s⁢t⁢i⁢m</td>
      <td>1.35 + (4.0–1.35) (1-p)</td>
      <td>-</td>
      <td>Input to the E1 population during stimulation</td>
    </tr>
    <tr>
      <td>gE⁢2b⁢s</td>
      <td>1.35</td>
      <td>-</td>
      <td>Input to the E2 population at baseline</td>
    </tr>
    <tr>
      <td>gE⁢2s⁢t⁢i⁢m</td>
      <td>1.35 + (4.0–1.35)p</td>
      <td>-</td>
      <td>Input to the E2 population during stimulation</td>
    </tr>
    <tr>
      <td colspan="4">Here, p is a parameter between 0 and 1 controlling the additional inputs to E1 and E2.</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Parameters for Figure 6.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Value</th>
      <th>Unit</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NE</td>
      <td>400</td>
      <td>-</td>
      <td>Number of excitatory neurons</td>
    </tr>
    <tr>
      <td>NI</td>
      <td>100</td>
      <td>-</td>
      <td>Number of inhibitory neurons</td>
    </tr>
    <tr>
      <td>Urest</td>
      <td>–70</td>
      <td>mV</td>
      <td>Resting membrane potential</td>
    </tr>
    <tr>
      <td>Uexc</td>
      <td>0</td>
      <td>mV</td>
      <td>Excitatory reversal potential</td>
    </tr>
    <tr>
      <td>Uinh</td>
      <td>–80</td>
      <td>mV</td>
      <td>Inhibitory reversal potential</td>
    </tr>
    <tr>
      <td>τref</td>
      <td>3</td>
      <td>ms</td>
      <td>Duration of refractory period</td>
    </tr>
    <tr>
      <td>τexcm</td>
      <td>20</td>
      <td>ms</td>
      <td>Membrane time constant of excitatory neurons</td>
    </tr>
    <tr>
      <td>τinhm</td>
      <td>10</td>
      <td>ms</td>
      <td>Membrane time constant of inhibitory neurons</td>
    </tr>
    <tr>
      <td>τampa</td>
      <td>5</td>
      <td>ms</td>
      <td>Time constant of AMPA receptor</td>
    </tr>
    <tr>
      <td>τgaba</td>
      <td>10</td>
      <td>ms</td>
      <td>Time constant of GABA receptor</td>
    </tr>
    <tr>
      <td>τnmda</td>
      <td>100</td>
      <td>ms</td>
      <td>Time constant of NMDA receptor</td>
    </tr>
    <tr>
      <td>ξ</td>
      <td>0.5</td>
      <td>-</td>
      <td>Receptor weighting factor</td>
    </tr>
    <tr>
      <td>JE⁢E</td>
      <td>0.19</td>
      <td>-</td>
      <td>Within-ensemble E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢E</td>
      <td>0.10</td>
      <td>-</td>
      <td>Within-ensemble E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I</td>
      <td>0.10</td>
      <td>-</td>
      <td>Within-ensemble I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I</td>
      <td>0.06</td>
      <td>-</td>
      <td>Within-ensemble I-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢E′</td>
      <td>0.019</td>
      <td>-</td>
      <td>Inter-ensemble E-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢E′</td>
      <td>0.05</td>
      <td>-</td>
      <td>Inter-ensemble E-to-I connection strength</td>
    </tr>
    <tr>
      <td>JE⁢I′</td>
      <td>0.04</td>
      <td>-</td>
      <td>Inter-ensemble I-to-E connection strength</td>
    </tr>
    <tr>
      <td>JI⁢I′</td>
      <td>0.006</td>
      <td>-</td>
      <td>Inter-ensemble I-to-I connection strength</td>
    </tr>
  </tbody>
</table>
