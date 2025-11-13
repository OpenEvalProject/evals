# Optimal information gain at the onset of habituation to repeated stimuli

## Authors

- Giorgio Nicoletti<sup>1</sup> ([ORCID: 0000-0002-7682-0596](https://orcid.org/0000-0002-7682-0596))
- Matteo Bruzzone<sup>4</sup> ([ORCID: 0000-0001-7683-8107](https://orcid.org/0000-0001-7683-8107))
- Samir Suweis<sup>3</sup> ([ORCID: 0000-0002-1603-8375](https://orcid.org/0000-0002-1603-8375))
- Marco dal Maschio<sup>4</sup> ([ORCID: 0000-0003-0150-6647](https://orcid.org/0000-0003-0150-6647))
- Daniel Maria Busiello<sup>3</sup> ([ORCID: 0000-0002-6754-5019](https://orcid.org/0000-0002-6754-5019)) †

### Affiliations

1. ECHO Laboratory, École Polytechnique Fédérale de Lausanne Lausanne Switzerland ([ROR:02s376052](https://ror.org/02s376052))
2. Quantitative Life Sciences section, The Abdus Salam International Center for Theoretical Physics (ICTP) Trieste Italy ([ROR:009gyvm78](https://ror.org/009gyvm78))
3. Department of Physics and Astronomy “Galileo Galilei”, University of Padova Padova Italy ([ROR:00240q980](https://ror.org/00240q980))
4. Department of Biomedical Science, University of Padova Padova Italy ([ROR:00240q980](https://ror.org/00240q980))
5. Padova Neuroscience Center, University of Padova Padova Italy ([ROR:00240q980](https://ror.org/00240q980))
6. Department of Biology, University of Fribourg Fribourg Switzerland ([ROR:022fs9h90](https://ror.org/022fs9h90))
7. Max Planck Institute for the Physics of Complex Systems Dresden Germany ([ROR:01bf9rw71](https://ror.org/01bf9rw71))

† Corresponding author

## Abstract

Biological and living systems process information across spatiotemporal scales, exhibiting the hallmark ability to constantly modulate their behavior to ever-changing and complex environments. In the presence of repeated stimuli, a distinctive response is the progressive reduction of the activity at both sensory and molecular levels, known as habituation. In this work, we solve a minimal microscopic model devoid of biological details, where habituation to an external signal is driven by negative feedback provided by a slow storage mechanism. We show that our model recapitulates the main features of habituation, such as spontaneous recovery, potentiation, subliminal accumulation, and input sensitivity. Crucially, our approach enables a complete characterization of the stochastic dynamics, allowing us to compute how much information the system encodes on the input signal. We find that an intermediate level of habituation is associated with a steep increase in information. In particular, we are able to characterize this region of maximal information gain in terms of an optimal trade-off between information and energy consumption. We test our dynamical predictions against experimentally recorded neural responses in a zebrafish larva subjected to repeated looming stimulations, showing that our model captures the main components of the observed neural habituation. Our work makes a fundamental step towards uncovering the functional mechanisms that shape habituation in biological systems from an information-theoretic and thermodynamic perspective.

## Introduction

Sensing mechanisms in biological systems span a wide range of temporal and spatial scales, from cellular to multi-cellular level, forming the basis for decision-making and the optimization of limited resources (Tkačik and Bialek, 2016; Azeloglu and Iyengar, 2015; Gnesotto et al., 2018; Whiteley et al., 2017; Perkins and Swain, 2009). Emergent macroscopic phenomena such as adaptation and habituation reflect the ability of living systems to effectively process the information they collect from their noisy environment (Nemenman, 2012; Nakajima, 2015; Koshland et al., 1982). Prominent examples include the modulation of flagellar motion operated by bacteria according to changes in the local nutrient concentration (Tu et al., 2008; Tu, 2008; Mattingly et al., 2021), the regulation of immune responses through feedback mechanisms (Cheong et al., 2011; Wajant et al., 2003), the progressive reduction of neural activity in response to repeated looming stimulation (Marquez-Legorreta et al., 2022; Fotowat and Engert, 2023), and the maintenance of high sensitivity in varying environments for olfactory or visual sensing in mammalian neurons (Lan et al., 2012; Menini, 1999; Kohn, 2007; Lesica et al., 2007; Benucci et al., 2013).

In the last decade, advances in experimental techniques fostered the quest for the core biochemical mechanisms governing information processing. Simultaneous recordings of hundreds of biological signals made it possible to infer distinctive features directly from data (Schneidman et al., 2006; Tkačik et al., 2014; Kurtz et al., 2015; Tunstrøm et al., 2013). However, many of these approaches fall short of describing the connection between observed behaviors and underlying microscopic drivers (Nicoletti and Busiello, 2021; Nicoletti and Busiello, 2022a; De Smet and Marchal, 2010; Nicoletti et al., 2022b). To fill this gap, several works focused on the architecture of specific signaling networks, from tumor necrosis factor (Cheong et al., 2011; Wajant et al., 2003) to chemotaxis (Tu et al., 2008; Celani et al., 2011), highlighting the essential structural ingredients for their efficient functioning. An observation shared by most of these studies is the key role of a negative feedback mechanism to induce emergent adaptive responses (Kollmann et al., 2005; De Ronde et al., 2010; Selimkhanov et al., 2014; Barkai and Leibler, 1997). Moreover, any information-processing system, biological or not, must obey information-thermodynamic laws that prescribe the necessity of a storage mechanism (Parrondo et al., 2015). This is an unavoidable feature highlighted in numerous chemical signaling networks (Tu et al., 2008; Kollmann et al., 2005) and biochemical realizations of Maxwell Demons (Flatt et al., 2023; Bilancioni et al., 2023). As the storage of information during processing generally requires energy (Bennett, 1982; Sagawa and Ueda, 2009), sensing mechanisms have to take place out of equilibrium (Gnesotto et al., 2018; Hartich et al., 2015; Skoge et al., 2013; Lestas et al., 2010). Recently, the discovery of memory molecules (Coultrap and Bayer, 2012; Frankland and Josselyn, 2016; Lisman et al., 2002) hinted at the possibility that storing mechanisms might be instantiated directly at the molecular scale. Overall, negative feedback, storage, and out-of-equilibrium conditions seem to be necessary requirements for a system to process environmental information and act accordingly. To quantify the performance of a biological information-processing system, theoretical developments made substantial progress in highlighting thermodynamics limitations and advantages (Sartori et al., 2014; Barato et al., 2014; Lan et al., 2012), making a step towards linking information and dissipation from a molecular perspective (Ouldridge et al., 2017; Flatt et al., 2023; Penocchio et al., 2022).

Here, we consider an archetypal yet minimal model for sensing that is inspired by biological networks (Lan et al., 2012; Tadres et al., 2022; Ma et al., 2009) and encapsulates all these key ingredients, that is negative feedback, storage, and energy dissipation, and study its response to repeated stimuli. Indeed, in the presence of dynamic environments, it is common for a biological system to keep encountering the same stimulus. Under these conditions, a progressive decay in the amplitude of the response is often observed, both at sensory and molecular levels. In general terms, such adaptive behavior is usually named habituation and is a common phenomenon recorded in various systems, from biochemical networks (Rahi et al., 2017; Tadres et al., 2022; Jalaal et al., 2020) to populations of neurons (Malmierca et al., 2014; Shew et al., 2015; Marquez-Legorreta et al., 2022; Fotowat and Engert, 2023). In particular, habituation characterizes many neuronal circuits along the sensory-motor processing pathways in most living organisms, either invertebrates or vertebrates (Malmierca et al., 2014; Shew et al., 2015), where inhibitory feedback mechanisms are believed to modulate the stimulus weight (Lamiré et al., 2022; Fotowat and Engert, 2023; Barzon et al., 2025). Most importantly, the first complete characterization of habituating phenomena dates back to 1966 (Thompson and Spencer, 1966), when different hallmarks of habituation in vertebrate animals were characterized. Despite its widespread occurrence across remarkably different scales, the connection between habituation in the animal kingdom and brainless molecular systems has only recently attracted considerable attention. A limited number of dynamical models have been proposed to explore the similarities and differences between the manifestations of these two fundamentally distinct phenomena (Eckert et al., 2024; Smart et al., 2024). However, dynamical characterizations of habituation still lack a clear identification of the functional role of habituation in regulating information flow, optimal processing, and sensitivity calibration (Benda, 2021), and in controlling behavior and prediction during complex tasks (Bueti et al., 2010; Sederberg et al., 2018; Palmer et al., 2015).

In this work, we explicitly compute the information shared between readout molecules and external stimulus over time. We find that the information gain peaks at intermediate levels of habituation, uncovering that optimal processing performances are necessarily tangled with maximal activity reduction. This region of optimal information gain can be retrieved by simultaneously minimizing dissipation and maximizing information in the presence of a prolonged stimulation, hinting at an a priori optimality condition for the operations of biological systems. Our results unveil the role of habituation in enhancing processing abilities and open the avenue to understanding the emergence of basic learning mechanisms in simple molecular scenarios.

## Results

### Archetypal model for sensing in biological systems

Several minimal models for adaptation are composed of three building blocks (Ma et al., 2009; Tadres et al., 2022; Tu et al., 2008; Celani et al., 2011; Rahi et al., 2017): one responsible for buffering the input signal; one representing the output; and one usually reminiscent of an internal memory. Here, we start with an analogous archetypal architecture. The three building blocks (or units) are represented by a receptor $(R)$, and readout $(U)$ and storage $(S)$ populations.

To introduce our model in general terms, we consider a time-varying environment $H$, representing an external signal characterized by a probability $p_{H}(h,t)$ of being equal to $h$ at time $t$. This input signal is read by the receptor unit $R$. The receptor can be either active ($A$), taking the value $r=1$, or passive ($P$), $r=0$, with these two states separated by an energetic barrier $ΔE$. The transitions between passive and active states can happen through two different pathways, a ‘sensing’ reaction path (superscript $H$) that is stimulated by the external signal $h$, and an ‘internal’ path (superscript $I$) that mediates the effect of the negative feedback from the storage unit (see Figure 1a). We further assume, for simplicity, that the rates follow an effective Arrhenius’ law:

$$
Γ_{P→A}^{(H)}=e^{\beta(h−ΔE)}Γ_{R}^{(H)}Γ_{A→P}^{(H)}=Γ_{R}^{(H)}Γ_{P→A}^{(I)}=e^{−\betaΔE}Γ_{R}^{(I)}Γ_{A→P}^{(I)}=Γ_{R}^{(I)}e^{\betaκ\sigmas/N_{S}}
$$

where the input is modeled as an additional thermodynamic driving with an energy $\betah$, and $Γ_{R}^{(H)}=gΓ_{R}^{(I)}=\tau_{R}^{−1}$ sets the timescale of the receptor. In particular, $g$ represents the ratio between the timescales of the two pathways, and the inverse temperature $\beta=(k_{B}T)^{−1}$ encodes the role of the thermal noise, as lower values of $\beta$ are associated with faster reactions.

![Figure 1.](https://cdn.elifesciences.org/articles/99767/elife-99767-fig1-v1.jpg)

**Figure 1.:** (a) A receptor $R$ transitions between an active ($A$) and passive ($P$) state along two pathways, one used for sensing (red) and affected by the environment $h$, and the other (blue) modified by the energy of storage molecules, $\sigmas$, tuned by inhibition strength $κ$ and storage capacity $N_{S}$. Here, $\beta=(k_{B}T)^{−1}$ encodes the inverse temperature. An active receptor increases the response of a readout population $U$ (orange), which in turn stimulates the production of storage units $S$ (green) that provide negative feedback to the receptor. (b) In the chemical network underlying chemotactic response, we can identify a similar architecture. The input ligand binds to membrane receptors, decreasing kinase activity and producing phosphate groups whose concentration regulates the receptor methylation level. (c) Similarly, in olfactory sensing, odorant binding induces the activation of adenylyl cyclase (AC). AC stimulates a calcium flux, eventually producing phosphorylase calmodulin kinase II (CAMKII) which phosphorylates and deactivates AC. (d) In neural response, multiple mechanisms take place at different scales. In zebrafish larvae, visual stimulation is projected along the visual stream from the retina to the cortex, a coarse-grained realization of the R-U dynamics. Neural habituation emerges upon repeated stimulation, as measured by calcium fluorescence signals ($dF/F_{0}$) and by the corresponding two-dimensional PCA of the activity profiles.

The negative feedback depends on the energy provided by the storage, $\sigmas$, where $s$ is the number of active storage molecules. The parameter $κ$ represents the strength of the inhibition, and $N_{S}$ is the storage capacity. For ease of interpretation, we assume that the activation rate of the receptor due to a reference signal $H_{ref}$ is balanced by the deactivation rate provided by the feedback of a fraction $\alpha=⟨S⟩/N_{S}$ of average active storage population:

$$
⟨log⁡\frac{Γ_{P→A}^{(H)}}{Γ_{A→P}^{(I)}}⟩=\betag(H_{ref}−κ\sigma\alpha)=0→κ=\frac{H_{ref}}{\alpha\sigma}.
$$

This condition sets the inhibition strength by choosing the inhibiting fraction $\alpha$. At this stage, the reference signal represents the typical environmental stimulus to which the system is exposed. This choice rationalizes the physical meaning of the model parameters, but it does not alter the phenomenology of the system. Crucially, the presence of two different transition pathways, motivated by molecular considerations and pivotal in many energy-consuming biochemical systems (De Los Rios and Barducci, 2014; Astumian, 2019; Flatt et al., 2023), creates an internal non-equilibrium cycle in receptor dynamics. Without the storage population, the internal pathway would not be present and the receptor would satisfy an effective detailed balance.

Whenever active, the receptor drives the production of readout population $U$, which represents the direct response of the system to environmental signals. As such, it is the observable characterizing habituation (see Figure 1a). We model its dynamics with a controlled stochastic birth-and-death process (Yan et al., 2019; Hilfinger et al., 2016; Nicoletti and Busiello, 2024a):

$$
∅_{U}→Γ_{u→u+1}^{(r)}UU→Γ_{u+1→u}∅_{U}Γ_{u→u+1}=e^{−\beta(V−cr)}Γ_{U}^{0}Γ_{u+1→u}=(u+1)Γ_{U}^{0}
$$

where $u$ denotes the number of molecules, $Γ_{U}^{0}=\tau_{U}^{−1}$ sets the timescale of readout production, and $V$ is the energy needed to produce a readout unit. When the receptor is active, $r=1$, this energetic cost is reduced by an effective additional driving $\betac$. Active receptors transduce the environmental energy into an active pumping in the readout unit, allowing readout population to encode information on the external signal.

Finally, readout units stimulate the production of the storage population $S$. Its number of molecules $s$ follows again a controlled birth-and-death process:

$$
∅_{S}→Γ_{s→s+1^{(u)}}SS→Γ_{s+1→s}∅_{S}Γ_{s→s+1}(u)=ue^{−\beta\sigma}Γ_{S}^{0}Γ_{s+1→s}=(s+1)Γ_{s}^{0}
$$

where $\sigma$ is the energetic cost of a storage molecule and $Γ_{S}^{0}$ sets the timescale, i.e., $Γ_{S}^{0}=\tau_{S}^{−1}$. For simplicity, we assume that readout molecules can catalytically activate storage molecules from a passive pool (see Figure 1a). Storage units are responsible for encoding the response, playing the role of a finite-time memory.

Our architecture, being devoid of specific biological details, can be adapted to describe systems operating at very different scales (Figure 1b–d). However, we emphasize that the proposed model is intentionally oversimplified compared to realistic biochemical or neural systems, yet it contains the minimal ingredients for habituation to emerge naturally. As such, the examples shown in Figure 1b–d are meant solely to illustrate the core architecture. In particular, while receptors can be readily identified, the role of readout is played by photo-receptors or calcium concentration for olfactory or visual sensing mechanisms (Menini, 1999; Kohn, 2007; Lesica et al., 2007; Benucci et al., 2013; Benda, 2021; Marquez-Legorreta et al., 2022; Fotowat and Engert, 2023), while storage may represent different molecular mechanisms at a coarse-grained level as, for example, memory molecules sensitive to calcium activity (Coultrap and Bayer, 2012), synaptic depotentiation, and neural populations that regulate neuronal response (Marquez-Legorreta et al., 2022; Fotowat and Engert, 2023).

As a final remark, we expect from previous studies (Nicoletti and Busiello, 2024a) that the presence of multiple timescales in the system will be fundamental in shaping information between the different components. Thus, we employ the biologically plausible assumption that $U$ undergoes the fastest evolution, while $S$ and $H$ are the slowest degrees of freedom (Celani et al., 2011; Ngampruetikorn et al., 2020). We have that $\tau_{U}≪\tau_{R}≪\tau_{S}≈\tau_{H}$, where $\tau_{H}$ is the timescale of the environment.

### The hallmarks of habituation

Habituation occurs when, upon repeated presentation of the same stimulus, a progressive decrease to an asymptotic level is observed in some parameters (Thompson and Spencer, 1966; Eckert et al., 2024). In our model, the response of the system is represented by the average number of active readout units, $⟨U⟩(t)$. This behavior resembles recent observations on habituation under analogous external conditions in various experimental systems (Rahi et al., 2017; Jalaal et al., 2020; Tadres et al., 2022; Marquez-Legorreta et al., 2022; Fotowat and Engert, 2023). However, habituation in its strict sense is not sufficient to encompass the diverse array of emergent features recorded in biological systems. In fact, several other hallmarks are closely associated with habituating behavior (Thompson and Spencer, 1966; Smart et al., 2024; Eckert et al., 2024):

These hallmarks have been originally proposed from observations of vertebrate animals, but they are not the sole properties characterizing the most general definition of habituation. However, the list above encompasses the features that can be obtained from a single stimulation, as in our case, and without any ambiguity in the interpretation (for a detailed discussion, we refer to Thompson and Spencer, 1966; Eckert et al., 2024).

To explore the ability of the proposed archetypal mode to capture the aforementioned hallmarks, we consider the simple case of an exponential input distribution, $p_{H}(h,t)∼exp⁡[−h⟨H⟩(t)]$ with uncorrelated signals, that is  $⟨h(t)h(t^{′})⟩=⟨H⟩(t)⟨H⟩(t^{′})$. The time-dependent average $⟨H⟩$ periodically switches between two values, $⟨H⟩_{min}$ and $⟨H⟩_{max}$, corresponding to a (non-zero) background signal and a (strong) stimulation of the receptor, respectively. The system dynamics is governed by four different operators, $W^_{X}$, with $X=R,U,S,H$, one for each unit and one for the environment. The resulting master equation is:

$$
∂_{t}P=[\frac{W^_{R}(s,h)}{\tau_{R}}+\frac{W^_{U}(r)}{\tau_{U}}+\frac{W^_{S}(u)}{\tau_{S}}+\frac{W^_{H}}{\tau_{H}}]P,
$$

where $P$ denotes, in general, the joint propagator $P(u,r,s,h,t|u_{0},r_{0},s_{0},h_{0},t_{0})$, with $u_{0}$, $r_{0}$, $s_{0}$ and $h_{0}$ initial conditions at time $t_{0}$. By taking advantage of the timescale separation, we can write an exact self-consistent solution to Equation 8 at all times $t$ (see Materials and methods and Supplementary Information).

In Figure 2a, we show that the system exhibits habituation in its strict sense. Here, for simplicity, we consider a train of signals arriving at times $t_{1},…,t_{N}$, each lasting a time $T_{s}$ with equal pauses between them of duration $ΔT$. We define the time to habituate, $t^{(hab)}$, as the first time at which the relative change of our observable, $⟨H⟩(t)$, is less than 0.5%, in analogy to Eckert et al., 2024. Clearly, $t^{(hab)}$ is associated with a number of stimuli necessary to habituate, $n^{(hab)}$, i.e.,

$$
\frac{⟨U⟩(t_{n^{(hab)}−1})−⟨U⟩(t_{n^{(hab)}}≡t^{(hab)})}{⟨U⟩(t_{n^{(hab)}})}\leq0.005
$$

![Figure 2.](https://cdn.elifesciences.org/articles/99767/elife-99767-fig2-v1.jpg)

**Figure 2.:** (a) An external signal switch between two values, $⟨H⟩_{min}=0.1$ (background) and $⟨H⟩_{max}=H_{ref}=10$ (stimulus). The inter-stimuli interval is $ΔT=100(a.u.)$ and the duration of each stimulus $T_{s}=100(a.u.)$. The average readout population (black) follows the stimulation, increasing when the stimulus is presented. The response decreases upon repeated stimulation, signaling the presence of habituation. Conversely, the average storage population (gray) increases over time. The black dashed line represents the time to habituate $t^{(hab)}$ (Equation 9). (b) If the stimulus is paused and presented again after a short time, the system habituates more rapidly, that is the number of stimulations to habituate $n^{(hab)}$ is reduced. (c) After waiting a sufficiently long time, the response can be fully recovered. (d) If the stimulation continues beyond habituation, the time to recover the response $t^{(recovery)}$ (Equation 10) increases by an amount $\deltat$ (in red). (e) The relative decrement of the average readout with respect to the initial response, $⟨U⟩^{(in)}$, shows that habituation becomes less and less pronounced as we increase $⟨H⟩_{max}$. (f) As expected, the initial response increases with $⟨H⟩_{max}$. (g) The relative difference between $⟨H⟩(t^{(hab)})$ and $⟨U⟩^{(in)}$, $Δ⟨U⟩$, decreases with the stimulus strength. (h) By changing $ΔT$ and keeping the stimulus duration $T_{s}$ fixed, we observe that more pronounced and more rapid response decrements are associated with more frequent stimulation. Parameters are reported in the Methods, and these hallmarks are qualitatively independent of their specific choice.

Our results do not qualitatively change when choosing a different threshold. Hallmark 1, potentiation of habituation, corresponds to a reduction of $n^{(hab)}$ after one series of stimulation and recovery. This implies a more rapid decrement in the response and a shorter time to achieve habituation, as we show in Figure 2b. Analogously, hallmark 2 is presented in Figure 2c, where we show that by suppressing the stimulus for a sufficiently long amount of time, the response spontaneously recovers to the pre-habituation level. Furthermore, by stimulating the system beyond $t^{(hab)}$, we also observe an increase in the amount of time to achieve complete recovery (hallmark 3). We define this recovery period $t^{(recovery)}$ as the first time required to have a response with a relative strength not greater than 1% with respect to the one at the first stimulus, that is

$$
\frac{⟨U⟩(t_{1})−⟨U⟩(t^{(recovery)})}{⟨U⟩(t_{1})}\leq0.01.
$$

In Figure 2d, we show that the recovery period increases by $∼5%$ as a consequence of this subliminal accumulation.

Within the same setting, in Figure 2e–g we applied stimuli of different strengths $⟨H⟩_{max}$ to study the sensitivity to input intensity (hallmark 4). When normalized by the initial response $⟨U⟩^{(in)}≡⟨U⟩(t_{1})$, less intense stimuli result in stronger response decrements (see Figure 2e). At the same time, as expected, the absolute value of the initial response increases instead (see Figure 2f). Hallmark 4 is clearly captured by Figure 2g, where we quantify the decrease of the normalized total habituation level, $Δ⟨U⟩=⟨U⟩(t^{(hab)})−⟨U⟩^{(in)}$, when exposed to increasing $⟨H⟩_{max}$. The last feature (hallmark 5) is reported in Figure 2h, where we keep the duration of the stimulus $T_{s}$ fixed while changing the inter-stimuli interval $ΔT$. By showing the responses up to the habituation time, we clearly notice that more frequent stimulation is associated with a more rapid and more pronounced response decrement.

Summarizing, despite its simplicity and lack of biological details, our model encompasses the minimal ingredients to capture the main hallmarks defining habituation.

### Information from habituation

In our architecture, habituation emerges due to the increase in the storage population, which provides increasing negative feedback to the receptor and thus lowers the number of active readout units $⟨U⟩(t)$. Crucially, by solving the master equation in Equation 8, we can also study the evolution of the full probability distribution $p_{U,S,H}(t)$. This approach allows us to quantify how the system encodes information on the environment $H$ through its readout population and how it changes during habituation. To this end, we introduce the mutual information between $U$ and $H$ at time $t$ (see Materials and methods):

$$
I_{U,H}(t)=H[p_{U}](t)−\int_{0}^{∞}dhp_{H}(h,t)H[p_{U∣H}](t)
$$

where $H[p](t)$ is the Shannon entropy of the probability distribution $p$, and $p_{U|H}$ denotes the conditional probability distribution of $U$ given $H$ measures information in terms of statistical dependencies, that is of how factorizable the joint probability distribution $p_{U,H}$ is. It vanishes if and only if $U$ and $H$ are independent. Notably, the mutual information coincides with the entropy increase of the readout distribution:

$$
k_{B}I_{U,H}=−k_{B}(H[p_{U|H}]−H[p_{U}])=−ΔS_{U}
$$

where $ΔS_{U}$ is the change in entropy of the readout population due to repeated measurements of the signal (Parrondo et al., 2015).

As in the previous section, we considered a switching signal with $⟨H⟩_{max}=H_{ref}$, the typical environmental stimulus strength. In Figure 3a–b, we plot the mutual information at the first signal, $I_{U,H}^{(in)}$, and when the system has habituated, $I_{U,H}^{(hab)}$, as a function of $\beta$ and $\sigma$. Crucially, we find that there exist parameters for which $I_{U,H}^{(hab)}$ is larger than $I_{U,H}^{(in)}$. This result suggests that the information on $H$ encoded by $U$ in the habituated system is larger than the initial one. We can quantify this effect by introducing the mutual information gain

$$
ΔI_{U,H}=I_{U,H}^{(hab)}−I_{U,H}^{(in)}.
$$

In Figure 3c, we show that $ΔI_{U,H}$ displays a peak in an intermediate region of the $(\beta,\sigma)$ plane. In this region, the corresponding habituation strength

$$
Δ⟨U⟩=⟨U⟩^{(hab)}−⟨U⟩^{(in)}
$$

attains intermediate values, suggesting that too strong habituation can be detrimental (Figure 3d). This behavior is tightly related to the presence of the storage $S$, which acts as an information reservoir for the system. To rationalize this feature, we introduce the feedback information

$$
ΔI_{f}=I_{(U,S),H}−I_{U,H}>0
$$

quantifying how much the simultaneous knowledge of $U$ and $S$ increases information compared to $U$ alone. Indeed, the change in feedback information after habituation, $ΔΔI_{f}=ΔI_{f}^{(hab)}−ΔI_{f}^{(in)}$, peaks in the same region of $ΔI_{U,H}$ (Figure 3e).

![Figure 3.](https://cdn.elifesciences.org/articles/99767/elife-99767-fig3-v1.jpg)

**Figure 3.:** Information and thermodynamics of the model during repeated external stimulation, as a function of the inverse temperature $\beta$ and the energetic cost of storage $\sigma$.(a–b) The mutual information between readout population and external signal at the first stimulus, $I_{U,H}^{(in)}$, is typically lower than the one when the system has habituated, $I_{U,H}^{(hab)}$. (c) The change in the mutual information, $ΔI_{U,H}$, displays a peak in a region of the $(\beta,\sigma)$ space, where the system exhibits optimal information gain during habituation. (d) This region corresponds to intermediate habituation strength, as measured by $Δ⟨U⟩$. (e) The corresponding increase in the feedback information $ΔI_{f}$ indicates that storage is fostering the gain in $ΔI_{U,H}$. (f) Habituation promotes a decrease of the internal energy flux $ΔJ_{int}$, suggesting a synergistic energetic advantage of habituation. (g–h) From the dynamical point of view, in the region of maximal information gain ($\beta=3$, $\sigma=0.6$) the average number of readout units, $⟨U⟩$, decreases over time, while the average storage population, $⟨S⟩$, increases. (i–j) Similarly, both the information encoded on $H$ by the readout, $I_{U,H}$, and the feedback information, $ΔI_{f}$, increase upon repeated stimulations. (k) The absolute value of the internal energy flux, $|J_{int}|$, decreases upon stimulations, while increasing for repeated pauses when the system moves downhill in energy. Model parameters are as specified in the Methods, $⟨H⟩_{min}=0.1$, and $⟨H⟩_{max}=H_{ref}=10$.

For small $\sigma$ we find that $ΔΔI_{f}$ may become negative, indicating that a too strong storage production may ultimately impede the information-theoretic performances of the system. Moreover, producing storage molecules requires energy. We can compute the internal energy flux associated with the storage of information through $S$ as

$$
J_{int}=\sigma\sumu,s[Γ_{s→s+1}p_{U,S^{(u,s,t)}}+−Γ_{s+1→s}p_{U,S^{(u,s+1,t)}}],
$$

which is the total energy flux to produce the internal populations ($U$ and $S$), since $U$ always reaches equilibrium, being the fastest species at play. Its change during habituation is defined as $ΔJ_{int}=J_{int}^{(hab)}−J_{int}^{(in)}$. In Figure 3f, we show that $ΔJ_{int}$ is typically smaller than zero, hinting at a synergistic thermodynamic advantage of habituation.

In Figure 3g–k, we show the evolution of the system for values of $(\beta,\sigma)$ that lie in the region of maximal information gain. The readout activity decreases in time (Figure 3g), due to the habituation driven by the increase of $⟨S⟩$ (Figure 3h). In this region, both $I_{U,H}$ and $ΔI_{f}$ increase over time (Figure 3i–j). We note that the increase in $I_{U,H}$ is concomitant to a reduction of the population that is encoding the signal. Although this may seem surprising, we stress that the mean of $U$ is not directly related to the factorizability of the joint distribution $p_{U,H}$. Finally, in Figure 3k, we show that the absolute value of the internal energy flux $|J_{int}|$ in the presence of the stimulus sharply decreases as well, while increasing during its pauses (the value of $J_{int}$ is negative in the presence of the background signal since the system is moving downhill in energy). This behavior is due to the interplay between storage and readout populations during habituation and signals the fact that the system requires progressively less energy to respond as time passes, while also moving less downhill in energy when the stimulus is paused. This observation suggests that the regime of maximal information gain supports habituation with a concurrent energetic advantage.

### The onset of habituation and its functional role

As habituation, information, and their energetic cost appear to be tightly related, we now investigate whether the region of maximal information gain can be retrieved by means of an a priori optimization principle. To do so, we first focus on the case of a constant environment. We assume that the system can tune its internal parameters to optimally respond to the statistics of a prolonged external signal. Thus, we consider a fixed input statistics given by $p_{H}^{st}(h)∼exp⁡[−h/H^{st}]$, with $H^{st}$ the average signal strength.

When the system reaches its steady state, we compute the information that the readout has on the signal, $I_{U,H}^{st}$ (Figure 4a) and the total energy consumption. To this end, we must take into account two terms. First, the energy flux in Equation 13 represents the rate of change in energy due to the driven storage production. The energy consumption associated with this process per unit energy is $E_{int}^{st}=\tau_{S}J_{int}^{st}/\sigma$. Second, the inhibition pathway is also driving the receptor out of equilibrium, leading to a dissipation per unit temperature given by

$$
\deltaQ_{R}=⟨log⁡(\frac{Γ_{P→A}^{(H)}Γ_{A→P}^{(I)}}{Γ_{A→P}^{(H)}Γ_{P→A}^{(I)}})⟩=\beta(H^{st}+κ\sigma\frac{⟨S⟩}{N_{S}}).
$$

We plot the total energy consumption per unit energy $E_{tot}^{st}=\deltaQ_{R}^{st}+E_{int}^{st}$ in Figure 4a. In order to understand how the system may achieve large values of mutual information while minimizing its intrinsic dissipation, we can maximize the Pareto functional (Seoane and Solé, 2015; Nicoletti and Busiello, 2024b):

$$
L(\beta,\sigma)=\gammaI_{U,H}^{st}(\beta,\sigma)−(1−\gamma)E_{tot}^{st}(\beta,\sigma)
$$

where $\gamma\in[0,1]$ sets the strategy implemented by the system. If $\gamma≪1$, the system prioritizes minimizing dissipation, whereas if $\gamma≈1$ it acts to preferentially maximize information. The set of $(\beta,\sigma)$ that maximize Equation 15 defines a Pareto optimal front in the $(E_{tot}^{st},I_{U,H}^{st})$ space (Figure 4a). At fixed energy consumption, this front represents the maximum information between the readout and the external input that can be achieved. The region below the front is therefore suboptimal. Instead, the points above the front are inaccessible, as higher values of $I_{U,H}^{st}$ cannot be attained without increasing $E_{tot}^{st}$. We note that, since $\beta$ usually cannot be directly controlled by the system, the Pareto front indicates the optimal $\sigma$ to which the system tunes at fixed $\beta$ (see Materials and methods and Appendices for details).

![Figure 4.](https://cdn.elifesciences.org/articles/99767/elife-99767-fig4-v1.jpg)

**Figure 4.:** (a–b) Contour plots in the $(\beta,\sigma)$ plane of the stationary mutual information $I_{U,H}^{st}$, and the total dissipation of the system per unit energy, $\deltaQ_{R}^{st}+E_{int}^{st}$, in the presence of a constant signal $⟨H⟩=H_{ref}=10$. For a given value of $\beta$, the system can optimize $\sigma$ to the Pareto front (black line) to simultaneously minimize energy consumption and maximize information. Below the front, the system exploits the available energy suboptimally, while the region above the front is physically inaccessible. (b) In the presence of a dynamical input switching between $⟨H⟩_{min}=0.1$ and $⟨H⟩_{max}=H_{ref}$, the parameters defining the optimal front capture the region of maximal information gain corresponding to the onset of habituation, where $Δ⟨U⟩$ starts to be significantly smaller than zero. The gray area enclosed by the dashed vertical lines indicates the location of the Pareto front for values of $\beta\in[3−3.5]$. (c) The Pareto front depends on the strength of the external signal $⟨H⟩_{max}$. In particular, for $⟨H⟩_{max}<H_{ref}$, at fixed $\beta$ a larger storage cost $\sigma$ is needed. Conversely, for $⟨H⟩_{max}>H_{ref}$, an optimal system can harvest more information by producing more storage, thus exhibiting a smaller $\sigma$. (d) If we allow the system to adapt its inhibition strength $κ$ to the stimulus (Equation 16), the Pareto fronts for different external signals collapse into a single optimal curve. Model parameters are specified in the Materials and methods.

We now consider once more a system receiving a dynamically switching signal with $⟨H⟩_{max}=H^{st}$. We first focus on the case $H_{ref}=H^{st}$, with $H_{ref}$ the reference signal appearing in Equation 2. Remarkably, we find that the Pareto optimal front in the $(\beta,\sigma)$ plane qualitatively corresponds to the region of maximal information gain, as we show in Figure 4b. This implies that a system that has tuned its internal parameters to respond to a constant signal also learns how to respond optimally to the time-varying input of the same strength, in terms of information gain. Since the region identified by the front leads to intermediate values of $Δ⟨U⟩$, it corresponds to the ‘onset of habituation’, where the system decreases its response enough to reduce the energy dissipation while storing information to increase $I_{U,H}$. Heuristically, the onset of habituation emerges spontaneously when the system attempts to activate its receptor as little as possible, while producing the minimum amount of storage molecules retaining enough information about the external environment.

In Figure 4c, we then study what happens to the optimal front if $⟨H⟩_{max}$ is larger or smaller than the reference signal. We find that, at low $⟨H⟩_{max}$, the Pareto front moves in such a way that a larger storage cost $\sigma$ is needed at fixed $\beta$. This is expected since, at lower signal strengths, it is harder for the system to distinguish the input from the background thermal noise. Conversely, when $⟨H⟩_{max}>H_{ref}$, an optimal system, it needs to reduce $\sigma$ to produce more storage and harvest information. Importantly, we find that if $⟨H⟩_{max}$ remains close to $H_{ref}$, the optimal front remains close to the onset of habituation and thus lies within the region of maximal information gain.

However, we can achieve a collapse of the optimal front if we allow the system to tune the inhibition strength $κ$ to the value of the external signal, that is

$$
κ(⟨H⟩_{max})=\frac{⟨H⟩_{max}}{\alpha\sigma}.
$$

In this way, a stronger input will correspond to a larger $κ$, and thus a stronger inhibition. In Figure 4d, we show that the Pareto fronts obtained with this choice collapse into a single curve. Crucially, this front still corresponds to the region of maximal information gain, although the specific values of $ΔI_{U,H}$ naturally depend on $⟨H⟩_{max}$ (see Supplementary Information). Thus, in this scenario, a system that is capable of adapting the negative feedback to its environment is also able to always tune itself to the onset of habituation at different values of the external stimulus and without tinkering with the energy cost $\sigma$, where its responses are optimal from an information-theoretic perspective.

### The role of information storage

The presence of a storage mechanism is fundamental in our model. Furthermore, its role in mediating the negative feedback is suggested by several experimental and theoretical observations (Celani et al., 2011; Tu et al., 2008; Kollmann et al., 2005; Barkai and Leibler, 1997; De Ronde et al., 2010; Selimkhanov et al., 2014). Whenever the storage is eliminated from our model, habituation cannot take place, highlighting its key role in driving the observed dynamics (see Supplementary Information).

In Figure 5a, we show that the degree of habituation, $Δ⟨U⟩$, and the change in the storage population, $Δ⟨S⟩$, are deeply related to one another. The more $⟨S⟩$ relaxes between two consecutive signals, the less the readout population reduces its activity. This ascribes to the storage population the role of an effective memory and highlights its dynamical importance for habituation. Moreover, the dependence of the storage dynamics on the interval between consecutive signals, $ΔT$, influences information gain as well. Indeed, increasing $ΔT$, we observe a decrease of the mutual information (Figure 5b) on the next stimulus. In the Supplementary Information, we further analyze the impact of different signal and pause durations.

![Figure 5.](https://cdn.elifesciences.org/articles/99767/elife-99767-fig5-v1.jpg)

**Figure 5.:** (a) The system response depends on the waiting time $ΔT$ between two external signals. As $ΔT$ increases, the storage decays, and thus memory is lost (green). Consequently, the habituation of the readout population decreases (yellow). (b) As a consequence, the information $I_{U,H}$ that the system has on the signal $H$ when the new stimulus arrives decays as well. Model parameters for this figure are $\beta=2.5$, $\sigma=0.5$ in the unit measure of the energy, and as specified in the Materials and methods.

We remark here that the proposed model is fully Markovian in its microscopic components, and the memory that governs readout habituation spontaneously emerges from the interplay among the internal timescales. In particular, recent works have highlighted that the storage needs to evolve on a slower timescale, comparable to that of the external input, in order to generate information in the receptor and in the readout (Nicoletti and Busiello, 2024a). To strengthen our conclusions, we remark that an instantaneous negative feedback implemented directly by $U$ (bypassing the storage mechanism) would lead to no time-dependent modulations of the readout and thus no habituation (see Supplementary Information). Similarly, a readout population evolving on a timescale comparable to that of the signal cannot effectively mediate the negative feedback on the receptor since its population increase would not lead to habituation (see Supplementary Information). Thus, negative feedback has to be implemented by a separate degree of freedom evolving on a timescale which is slow and comparable to that of external signal.

### Minimal features of neural habituation

In neural systems, habituation is typically measured as a progressive reduction of the stimulus-driven neuronal firing rate (Malmierca et al., 2014; Shew et al., 2015; Benda, 2021; Marquez-Legorreta et al., 2022; Fotowat and Engert, 2023). To test whether our minimal model can be used to capture the typical neural habituation dynamics, we measured the response of zebrafish larvae to repeated looming stimulations via volumetric multiphoton imaging (Bruzzone et al., 2021). From a whole-brain recording of $≈55000$ neurons, we extracted a subpopulation of $≈2400$ neurons in the optic tectum with a temporal activity profile that is most correlated with the stimulation protocol (see Materials and methods).

Our model can be extended to qualitatively reproduce some features of the progressive decrease in neuronal response amplitudes. We identify a single readout unit with a subpopulation of binary neurons. Then, a fraction of neurons is randomly turned on each time the corresponding readout unit is activated (see Materials and methods). We tune the model parameters to have a comparable number of total active neurons at the first stimulus with respect to the experimental setting. Moreover, we set the pause and signal durations in line with the typical timescales of the looming stimulation. We choose the model parameters $\beta$ and $\sigma$ in such a way that the system operates close to the peak of information gain, with an activity decrease over time that is comparable to the activity decrease in experimental data (see Supplementary Information). In this way, we can focus on the effects of storage and feedback mechanisms without modeling further biological details.

The patterns of the model-generated activity are remarkably similar to the experimental ones (see Figure 6a). We performed a two-dimensional embedding of the neural activity profiles of all recorded neurons via PCA (explained variance $≈70%$) and we plot the temporal evolution in this low-dimensional space (Figure 6b). This procedure reveals that the first principal component (PC) accounts for the evoked neural response, while the second PC mostly reflects the habituation dynamics. We perform the same analysis on data generated from the model as explained above. As we see in Figure 6c, the second PC encodes habituation, as in experimental data, although the neural response in the first PC is replaced by the switching on/off dynamics of the input. This shows that our model is able to capture the main features of the observed neural habituation, without the need for biological details.

![Figure 6.](https://cdn.elifesciences.org/articles/99767/elife-99767-fig6-v1.jpg)

**Figure 6.:** (a) Normalized neural activity profile in a zebrafish larva in response to the repeated presentation of visual (looming) stimulation, and comparison with the fraction of active neurons $⟨N⟩_{act}=N_{act}/N$ in our model with stochastic neural activation (see Methods). Stimuli are indicated with colored dots from blue to red as time increases. (b) PCA of experimental data reveals that habituation is captured mostly by the second principal component, while features of the evoked neural response are captured by the first one. Different colors indicate responses to different stimuli. (c) PCA of simulated neural activations. Although we cannot capture the dynamics of the evoked neural response with a switching input, the core features of habituation are correctly captured along the second principal component. Model parameters are $\beta=4.5$, $\sigma=0.15$ in energy units, and as in the Materials and methods, so that the system is tuned to the onset of habituation.

## Discussion

In this work, we studied a minimal architecture that serves as a microscopic and archetypal description of sensing processes across biological scales. Informed by theoretical and experimental observations, we focused on three fundamental mechanisms: a receptor, a readout population, and a storage mechanism that drives negative feedback. Despite its simplicity, we have shown that our model robustly reproduces the hallmarks associated with habituation in the presence of a single type of repeated stimulation, a widespread phenomenon in both biochemical and neural systems. By quantifying the mutual information between the external signal and readout population, we identified a regime of optimal information gain during habituation. Remarkably, the system can spontaneously tune to this region of parameters if it enforces an information-dissipation trade-off. In particular, optimal systems lie at the onset of habituation, characterized by intermediate levels of activity reduction, as both too-strong and too-weak negative feedback are detrimental to information gain. Finally, we found that, by allowing for a storage inhibition strength that can adapt to the environmental signal, this optimality is input-independent and requires no further adjustment of other internal model parameters. Our results suggest that the functional advantages of the onset of habituation are rooted in the interplay between energy dissipation and information gain, and its general features are tightly linked to the internal mechanisms to store information.

Although minimal, our model can capture basic features of neural habituation, where it is generally accepted that inhibitory feedback mechanisms modulate the stimulus weight (Lamiré et al., 2022). Remarkably, recent works reported the existence of a separate inhibitory neuronal population whose activity increases during habituation (Fotowat and Engert, 2023). Our model suggests that this population might play the role of a storage mechanism, allowing the system to habituate to repeated signals. However, in neural systems, a prominent role in encoding both short- and long-term information is also played by synaptic plasticity (Abbott and Nelson, 2000; Martin et al., 2000) as well as by memory molecules (Coultrap and Bayer, 2012; Frankland and Josselyn, 2016; Lisman et al., 2002), at a biochemical level. A comprehensive analysis of how information is encoded and retrieved will most likely require all these mechanisms at once. Including an explicit connectivity structure with synaptic updates in our model may help in this direction, at the price of analytical tractability. Furthermore, future works may be able to compare our theoretical predictions with experiments in which the modulation of frequency (Fotowat and Engert, 2023) and intensity of stimulation trigger the observed hallmarks. In this way, we could elucidate the roles and features of internal processes characterizing the system under investigation, along with its information-theoretic performance. Overall, the present results hint at the fact that our minimal architecture may provide crucial insights into the functional advantages of habituation in a wide range of biological systems.

Extensions of these ideas are manifold. The definition of a habituated system relies, in this work as well as in other studies (Eckert et al., 2024), on the definition of a response threshold. However, some of the hallmarks might disappear when habituation is defined as a phenomenon appearing in a time-periodic steady state. To overcome this issue, it may be necessary to extend the model to more realistic molecular schemes encompassing the presence of additional storage mechanisms. More generally, understanding the information-theoretic performance of real-world biochemical networks exhibiting habituation remains a fascinating perspective to explore. Upon these premises, the possibility of inferring the underlying biochemical structure from observed behaviors is a fascinating direction (Rahi et al., 2017). Furthermore, since we focused on repetitions of statistically identical signals, it will be fundamental to characterize the system’s response to diverse environments (Hidalgo et al., 2014). To this end, incorporating multiple receptors or storage populations may be needed to harvest information in complex conditions. In such scenarios, correlations between external signals may help reduce the encoding effort as, intuitively, $S$ is acting as an information reservoir for the system. Moreover, such stored information could be used to make predictions on future stimuli and behavior (Bueti et al., 2010; Sederberg et al., 2018; Palmer et al., 2015). Indeed, living systems do not passively read external signals but often act upon the environment. We believe that both storage mechanisms and their associated negative feedback will remain core modeling ingredients.

Our work paves the way to understanding how information is encoded and guides learning, predictions, and decision-making, a paramount question in many fields. On the one hand, it encapsulates key ingredients to support habituation while still being minimal enough to allow for analytical treatment. On the other hand, it may help the experimental quest for signatures of these physical ingredients in a variety of systems. Ultimately, our results show how habituation – a ubiquitous phenomenon taking place at strikingly different biological scales – may stem from an information-based advantage, shedding light on the optimization principle underlying its emergence and relevance for any biological system.

## Materials and methods

### Model parameters

In this section, we briefly recall the free parameters of the model and the values we use in numerical simulations, unless otherwise specified. In particular, the energetic barrier $(V−cr)$ fixes the average values of the readout population both in the passive and active state, namely $⟨U⟩_{P}=e^{−\betaV}$ and $⟨U⟩_{A}=e^{−\beta(V−c)}$ (see Equation 3). Thus, we can fix $⟨U⟩_{P}$ and $⟨U⟩_{A}$ in lieu of $V$ and $c$. Similarly, as in Equation 2, we can set the inhibiting storage fraction $\alpha$ to fix $κ$. At any rate, we remark that the emerging features of the model are qualitatively independent of the specific choice of these parameters. Furthermore, we typically consider the average of the exponentially distributed signal to be $⟨H⟩_{max}=10$ and $⟨H⟩_{min}=0.1$ (see Supplementary Information for details). Overall, we are left with $\beta$ and $\sigma$ as free parameters. $\beta$ quantifies the amount of thermal noise in the system, and at small $\beta$ the thermal activation of the receptor hinders the effect of the signal and makes the system almost unable to process information. Conversely, if $\beta$ is high, the system must overcome large thermal inertia, increasing the dissipative cost. In this regime of weak thermal noise, we expect that, given a sufficient amount of energy, the system can effectively process information. In Table 1, we summarize the specific parameter values we used throughout the main text. Other values to explore the robustness of the model are discussed in the Supplementary Information.

**Table 1.**
 Summary of the model parameters and the values used for numerical simulations, unless otherwise specified.The parameters $\beta$ and $\sigma$ qualitatively determine the behavior of the model and are varied throughout the main text.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MS\begin{document}$  M_{S}$\end{document}</td>
      <td>Maximum number of storage units</td>
      <td>30</td>
    </tr>
    <tr>
      <td>ΔE\begin{document}$  \Delta E$\end{document}</td>
      <td>Receptor energetic barrier</td>
      <td>1</td>
    </tr>
    <tr>
      <td>⟨U⟩P\begin{document}$\langle U\rangle_{P}$\end{document}</td>
      <td>Average readout with passive receptor</td>
      <td>150</td>
    </tr>
    <tr>
      <td>⟨U⟩A\begin{document}$  \langle U\rangle_{A}$\end{document}</td>
      <td>Average readout with active receptor</td>
      <td>MS</td>
    </tr>
    <tr>
      <td>ΓS0\begin{document}$  \Gamma_{S}^{0}$\end{document}</td>
      <td>Inverse timescale of the storage</td>
      <td>1</td>
    </tr>
    <tr>
      <td>g\begin{document}$  g$\end{document}</td>
      <td>Receptor’s pathways timescale ratio</td>
      <td>1</td>
    </tr>
    <tr>
      <td>α\begin{document}$  \alpha$\end{document}</td>
      <td>Inhibiting storage fraction</td>
      <td>2/3</td>
    </tr>
    <tr>
      <td>Href\begin{document}$  H_{\mathrm{ref}}$\end{document}</td>
      <td>Reference signal</td>
      <td>10</td>
    </tr>
    <tr>
      <td>β\begin{document}$  \beta$\end{document}</td>
      <td>Inverse temperature</td>
      <td>-</td>
    </tr>
    <tr>
      <td>σ\begin{document}$  \sigma$\end{document}</td>
      <td>Storage energy cost</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

### Timescale separation

We solve our system in a timescale separation framework (Busiello et al., 2020; Bo and Celani, 2017; Nicoletti and Busiello, 2024a), where the storage evolves on a timescale that is much slower than all the other internal ones, that is

$$
\tau_{U}≪\tau_{R}≪\tau_{S}≈\tau_{H}.
$$

The fact that $\tau_{S}$ is the slowest timescale at play is crucial to making these components act as an information reservoir. This assumption is also compatible with biological examples. The main difficulty arises from the presence of the feedback, that is the signal influences the receptor and thus the readout population, which in turn impacts the storage population and finally changes the deactivation rate of the receptor - schematically, $H→R→U→S→R$, but the causal order does not reflect the temporal one.

We start with the master equation for the propagator $P(u,r,s,h,t|u_{0},r_{0},s_{0},h_{0},t_{0})$,

$$
∂_{t}P=[\frac{W^_{U}(r)}{\tau_{U}}+\frac{W^_{R}(s,h)}{\tau_{R}}+\frac{W^_{S}(u)}{\tau_{S}}+\frac{W^_{H}}{\tau_{H}}]P.
$$

We rescale the time by $\tau_{S}$ and introduce two small parameters to control the timescale separation analysis, $ϵ=\tau_{U}/\tau_{R}$ and $\delta=\tau_{R}/\tau_{H}$. Since $\tau_{S}/\tau_{H}=O(1)$, we set it to 1 without loss of generality. We then write $P=P^{(0)}+ϵP^{(1)}$ and expand the master equation to find $P^{(0)}=p_{U|R}^{st}(u|r)Π$, with $W^_{U}p_{U|R}^{st}=0$. We obtain that $Π$ obeys the following equation:

$$
∂_{t}Π=[\delta^{−1}W^_{R}(s,h)+W^_{S}(u)+W^_{H}]Π.
$$

Yet again, $Π=Π^{(0)}+\deltaΠ^{(1)}$ allows us to write $Π^{(0)}=p_{R|S,H}^{st}(r|s,h)F(s,h,t|s_{0},h_{0},t_{0})$ at order $O(\delta^{−1})$, where $W^_{R}p_{R|S,H}^{st}=0$. Expanding first in $ϵ$ and then in $\delta$ sets a hierarchy among timescales. Crucially, due to the feedback present in the system, we cannot solve the next order explicitly to find $F$. Indeed, after a marginalization over $r$, we find $∂_{t}F=[W^_{H}+W^_{S}(u¯(s,h))]F$, at order $O(1)$, where $u¯(s,h)=\sumu,rup_{U|R}^{st}(u|r)p_{R|S,H}^{st}(r|s,h)$. Hence, the evolution operator for $F$ depends manifestly on $s$, and the equation cannot be self-consistently solved. To tackle the problem, we first discretize time, considering a small interval, that is  $t=t_{0}+Δt$ with $Δt≪\tau_{U}$ and thus $u¯(s,h)≈u_{0}$. We thus find $F(s,h,t|s_{0},h_{0},t_{0})=P(s,t|s_{0},t_{0})P_{H}(h,t|h_{0},t_{0})$ in the domain $t\in[t_{0},t_{0}+Δt]$, since $H$ evolves independently from the system (see also Supplementary Information for analytical steps).

Iterating the procedure for multiple time steps, we end up with a recursive equation for the joint probability $p_{U,R,S,H}(u,r,s,h,t_{0}+Δt)$. We are interested in the following marginalization

$$
p_{U,S}(u,t+Δt)=\sumr=01\int_{0}^{∞}dhp_{u|R}^{st}(u|r)p_{R|S,H}^{st}(r|h,s)p_{H}(h,t+Δt)\sums^{′}=0N_{S}\sumu^{′}=0∞P(s^{′},t→s,t+Δt|u^{′})p_{U,S}(u^{′},s^{′},t)
$$

where $P(s^{′},t→s,t+Δt)$ is the propagator of the storage at fixed readout. This is the Chapman-Kolmogorov equation in the timescale separation approximation. Notice that this solution requires the knowledge of $p_{U,S}$ at the previous time step, and it has to be solved iteratively.

### Explicit solution for the storage propagator

To find a numerical solution to our system, we first need to compute the propagator $P(s_{0},t_{0}→s,t)$. Formally, we have to solve the master equation

$$
∂_{t}P(s_{0}→s|u_{0})=Γ_{S}^{0}[e^{−\beta\sigma}u_{0}P(s_{0}→s^{′})\delta_{s^{′},s−1}+s^{′}P(s_{0}→s^{′})\delta_{s^{′},s+1}−P(s_{0}→s^{′})\delta_{s^{′},s}(s^{′}+e^{−\beta\sigma}u_{0})]
$$

where we used the shorthand notation $P(s_{0}→s)=(s_{0},t_{0}→s,t)$. Since our formula has to be iterated for small timesteps, that is $t−t_{0}=Δt≪1$, we can write the propagator as follows

$$
P(s_{0},t_{0}→s,t_{0}+Δt|u_{0})=p_{S|U}^{st}+\sumνw_{ν}a^{(ν)}e^{\lambda_{ν}Δt}
$$

where $w_{ν}$ and $\lambda_{ν}$ are respectively eigenvectors and eigenvalues of the transition matrix $W^_{S}(u_{0})$,

$$
(W^_{S}(u_{0}))_{ij}=e^{−\beta\sigma}u_{0}if i=j+1(W^_{S}(u_{0}))_{ij}=jif i=j−1(W^_{S}(u_{0}))_{ij}=0otherwise
$$

and the coefficients $a^{(ν)}$ are such that

$$
p_{S|U}(s_{0},t_{0}→s,t_{0}+Δt|u_{0})=p_{S|U}^{st}+\sumνw_{ν}a^{(ν)}=\delta_{s,s_{0}}.
$$

Since eigenvalues and eigenvectors of $W^_{S}(u_{0})$ might be computationally expensive to find, we employ another simplification. As $Δt→0$, we can restrict the matrix only to jumps to the $n$-th nearest neighbors of the initial state $(s_{0},t_{0})$, assuming that all other states are left unchanged in small time intervals. We take $n=2$ and check the accuracy of this approximation against the full simulation for a limited number of timesteps.

### Mean-field relations

We note that $⟨U⟩$ and $⟨S⟩$ satisfies the following mean-field relationship:

$$
\frac{⟨U⟩−⟨U⟩_{r=1}}{⟨U⟩_{r=1}−⟨U⟩_{r=0}}=f_{0}(\frac{⟨S⟩}{N_{S}}),
$$

where $f_{0}(x)$ is an analytical function of its argument (see Supplementary Information). This relation clearly states that only the fraction of active storage units is relevant to determining the habituation dynamics.

### Mutual information

Once we have $p_{U}(u,t)$ (obtained marginalizing $p_{U,S}$ over $s$) for a given $p_{H}(h,t)$, we can compute the mutual information

$$
I_{U,H}(t)=H[p_{U}](t)−\int_{0}^{∞}dhp_{H}(h,t)H[p_{U|H}](t)
$$

where $H$ is the Shannon entropy. For the sake of simplicity, we consider that the external signal follows an exponential distribution $p_{H}(h,t)=\lambda(t)e^{−\lambda(t)h}$. Notice that, in order to determine such quantity, we need the conditional probability $p_{U|H}(u,t)$. In the Supplementary Information, we show how all the necessary joint and conditional probability distributions can be computed from the dynamical evolution derived above.

We also highlight here that the timescale separation implies $I_{S,H}=0$, since

$$
p_{S|H}(s,t|h)=\sumup_{U,S|H}(u,s,t|h)=p_{S}(s,t)\sumu\sumrp_{U|R}^{st}(u|r)p_{R|S,H}^{st}(r|s,h)=p_{S}(s,t).
$$

Although it may seem surprising, this is a direct consequence of the fact that $S$ is only influenced by $H$ through the stationary state of $U$. Crucially, the presence of the feedback is still fundamental in promoting habituation. Indeed, we can always write the mutual information between the signal $H$ and both the readout $U$ and the storage $S$ together as $I_{(U,S),H}=ΔI_{f}+I_{U,H}$, where $ΔI_{f}=I_{(U,S),H}−I_{U,H}=I_{(U,H),S}−I_{U,S}$. Since $ΔI_{f}>0$ (by standard information-theoretic inequalities), the storage is increasing the information of the two populations together on the external signal. Overall, although $S$ and $H$ are independent in this limit, the feedback is paramount in shaping how the system responds to the external signal and stores information about it.

### Pareto optimization

We perform a Pareto optimization at stationarity in the presence of a prolonged stimulation. We seek the optimal values of $(\beta,\sigma)$ by maximizing the functional in Equation 15 of the main text. Hence, we maximize the information between the readout and the signal, simultaneously minimizing the dissipation of the receptor induced by both the signal and feedback process and the dissipation associated with storage production, as discussed in the main text. The dissipative contributions have been computed per unit energy to be comparable with the mutual information. In the Supplementary Information, we detailed the derivation of the Pareto front and investigated the robustness of this optimization strategy.

### Recording of whole brain neuronal activity in zebrafish larvae

Acquisitions of the zebrafish brain activity were carried out in one Elavl3:H2BGCaMP6s larvae at 5 days post fertilization raised at 28 °C on a 12 hr light/12 hr dark cycle according to the approval by the Ethical Committee of the University of Padua (61/2020 dal Maschio). The subject was embedded in 2% agarose gel and brain activity was recorded using a multiphoton system with a custom 3D volumetric acquisition module. Data were acquired at 30 frames per second covering an effective field of view of about $450\times900um$ with a resolution of 512×1024 pixels. The volumetric module acquires a volume of about $180−200um$ in thickness encompassing 30 planes separated by about $7um$, at a rate of 1 volume per second, sufficient to track the slow dynamics associated with the fluorescence-based activity reporter GCaMP6s. Visual stimulation was presented in the form of a looming stimulus with 150 s intervals, centered with the fish eye (see Supplementary Information). Neurons identification and anatomical registrations were performed as described in Bruzzone et al., 2021.

### Data analysis

The acquired temporal series were first processed using an automatic pipeline, including motion artifact correction, temporal filtering with a 3s rectangular window, and automatic segmentation. The obtained dataset was manually curated to resolve segmentation errors or to integrate cells not detected automatically. We fit the activity profiles of about 55,000 cells with a linear regression model using a set of base functions representing the expected responses to each stimulation event. These base functions have been obtained by convolving the exponentially decaying kernel of the GCaMP signal lifetime with square waveforms characterizing the presentation of the corresponding visual stimulus. The resulting score coefficients of the fit were used to extract the cells whose score fell within the top 5% of the distribution, resulting in a population of $≈2400$ neurons whose temporal activity profile correlates most with the stimulation protocol. The resulting fluorescence signals $F^{(i)}$ were processed by removing a moving baseline to account for baseline drifting and fast oscillatory noise (Jia et al., 2011). See Supplementary Information.

### Model for neural activity

Here, we describe how our framework is modified to mimic neural activity. Each readout unit, $u$, is interpreted as a population of $N$ neurons, i.e., a region dedicated to the sensing of a specific input. When a readout population is activated at time $t$, each of its $N$ neurons fires with a probability $p$. We set $N=20$ and $p=0.5$ has been set to have the same number of observed neurons in data and simulations, while $p$ only controls the dispersal of the points in Figure 6c, thus not altering the main message. The dynamics of each readout unit follows our dynamical model. Due to habituation, some of the readout units activated by the first stimulus will not be activated by subsequent stimuli. Although the evoked neural response cannot be captured by this extremely simple model, its archetypal ingredients (dissipation, storage, and feedback) are informative enough to reproduce the low-dimensional habituation dynamics found in experimental data.
