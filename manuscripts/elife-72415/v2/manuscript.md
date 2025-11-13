# Sensing complementary temporal features of odor signals enhances navigation of diverse turbulent plumes

## Authors

- Viraaj Jayaram<sup>1</sup> ([ORCID: 0000-0002-9607-2214](https://orcid.org/0000-0002-9607-2214))
- Nirag Kadakia<sup>2</sup> ([ORCID: 0000-0001-9978-6450](https://orcid.org/0000-0001-9978-6450))
- Thierry Emonet<sup>1</sup> ([ORCID: 0000-0002-6746-6564](https://orcid.org/0000-0002-6746-6564)) †

### Affiliations

1. Department of Physics, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
2. Department of Molecular, Cellular and Developmental Biology, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
3. Quantitative Biology Institute, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))

† Corresponding author

## Abstract

We and others have shown that during odor plume navigation, walking Drosophila melanogaster bias their motion upwind in response to both the frequency of their encounters with the odor (Demir et al., 2020) and the intermittency of the odor signal, which we define to be the fraction of time the signal is above a detection threshold (Alvarez-Salvado et al., 2018). Here, we combine and simplify previous mathematical models that recapitulated these data to investigate the benefits of sensing both of these temporal features and how these benefits depend on the spatiotemporal statistics of the odor plume. Through agent-based simulations, we find that navigators that only use frequency or intermittency perform well in some environments – achieving maximal performance when gains are near those inferred from experiment – but fail in others. Robust performance across diverse environments requires both temporal modalities. However, we also find a steep trade-off when using both sensors simultaneously, suggesting a strong benefit to modulating how much each sensor is weighted, rather than using both in a fixed combination across plumes. Finally, we show that the circuitry of the Drosophila olfactory periphery naturally enables simultaneous intermittency and frequency sensing, enhancing robust navigation through a diversity of odor environments. Together, our results suggest that the first stage of olfactory processing selects and encodes temporal features of odor signals critical to real-world navigation tasks.

## Introduction

The complexity of natural odor plumes makes olfactory navigation a difficult task. Turbulent flows produce rapid changes in the local odor concentrations, and instantaneous odor gradients often do not point toward the source (Celani et al., 2014; Crimaldi and Koseff, 2001). Encounters between the animal and odorized packets of air are intermittent, with durations and frequencies spanning many orders of magnitude (Celani et al., 2014). Moreover, distinct flow conditions result in distinct spatiotemporal statistics: near boundaries and with lower mean wind speeds, odor plumes are smoother, with odor concentrations consistently above detectable thresholds (Connor et al., 2018). But roughness in the physical landscape – sands, rough terrain, vegetation – and shifting winds can cause plumes to break up into discrete odor filaments, interspersed with long periods of undetectable concentrations (Cardé and Willis, 2008; Murlis et al., 1992; Riffell et al., 2008). There, encounters with odor filaments can occur over a wide range of frequencies from 0.1 Hz (Riffell et al., 2008) to 5 Hz or more (Demir et al., 2020).

To navigate plumes exhibiting this degree of temporal complexity, animals must be able to detect odor encounters quickly and accurately. Indeed, many organisms have evolved olfactory receptor neurons (ORNs) that respond to chemical signals with high temporal precision (Gorur-Shandilya et al., 2017; Jacob et al., 2017; Nagel and Wilson, 2011; Szyszka et al., 2014; Szyszka et al., 2012). ORN firing responses are strongly time-locked to the arrival time of an odor (Gorur-Shandilya et al., 2017), and fast synaptic mechanisms (Fox and Nagel, 2021; Martelli et al., 2013) allow this information to be passed quickly downstream, within milliseconds, to projection neurons (PNs) in the antennal lobe, driving rapid behavioral responses (Bhandawat et al., 2010). Such precision has been suggested to allow accurate encoding of temporal features of the odor signal (Nagel et al., 2015), such as the frequency of odor arrivals.

In addition to these fast responses, Drosophila ORNs also adapt their firing rates and gain to prolonged stimuli (Cao et al., 2016; Gorur-Shandilya et al., 2017; Nagel and Wilson, 2011), priming them to accurately encode future odor signals (Kadakia and Emonet, 2019) without losing temporal precision as intensity changes (Gorur-Shandilya et al., 2017; Martelli et al., 2013). Likewise, in honeybees, the temporal resolution of odor pulses increases over time in a pulsed odor environment (Szyszka et al., 2014), while in the moth Agrotis ipsilon, ORN responses adjust to optimally encode odor signals that occur most frequently in the environment (Levakova et al., 2018). Olfactory neurons in insects are thus sensitive to the temporal features of odor signals on both short and long timescales (Nagel et al., 2015).

Temporal precision in olfaction extends beyond insects. In mice, plume dynamics as fast as tens of milliseconds are encoded downstream in mitral and tufted cells (Ackels et al., 2021). In crustaceans, odors are encoded by bursting ORNs (or bORNs), which burst only if odors arrive at some phase relative to an intrinsic bursting cycle (Park et al., 2014). These cycles vary over orders of magnitudes across the bORN population, providing a natural template to encode the timing between odor arrivals (Park et al., 2016).

Naturally, such precisely resolved temporal odor information shapes navigational decisions. When tracking pheromones, flying male moths fly faster and straighter upwind when receiving odor hits at higher frequencies than lower ones (Mafra-Neto and Cardé, 1994; Vickers and Baker, 1994). Walking silkworm moths switch from zigzagging motion to straighter trajectories upwind in higher-frequency environments (Kanzaki et al., 1992). One model (Vickers and Baker, 1994) has suggested that odor hits suppress an otherwise persistent internal counterturning mechanism, allowing moths to maintain straight trajectories if odors are frequent or long. Alternatively, flying flies counterturn shortly after passing through the odor (Budick and Dickinson, 2006; van Breugel and Dickinson, 2014), indicating that counterturning can be also driven by the loss of the plume rather than an internal mechanism. In water, crabs navigate successfully in environments with higher-odor intermittency, but fail to find odor sources as pulses become more infrequent (Keller and Weissburg, 2004).

Two recent studies in eLife have quantified in great detail, using both experiment and extensive mathematical modeling, the olfactory navigational strategies of walking Drosophila in wind tunnels. One of these (Álvarez-Salvado et al., 2018) focused on spatially uniform but temporally varying environments, where the odor was presented in spatially uniform pulses lasting anywhere from 1 to 10 s. In this environment, walking flies maintained upwind headings and increased walking speed over the duration of the odor pulses, albeit with a degree of desensitization over time. This suggests that when odor encounters are long and persistent the intermittency of the odor signal – which we define to be the percentage of time the odor signal is above threshold – is a main driver of navigational decisions. The second study (Demir et al., 2020) instead challenged flies to navigate spatiotemporally complex odor plumes that were generated by stochastically perturbing a thin ribbon of odor. In this plume, odor encounters were much shorter (~0.1–0.3 s), more frequent (~3 Hz), and less predictable. In that study, fly navigation was reproduced by a model in which only the frequency of odor encounters controlled upwind orientation, independent of their duration or concentration. These two studies used the same organism with the same locomotive repertoire. The two distinct models they uncovered naively suggest that flies are able to sense distinct temporal features of odor plumes and use these various inputs to shape navigational decisions.

Here, we use mathematical modeling and numerical simulations to investigate how and under what conditions these two temporal features – odor intermittency and encounter frequency – can enhance the navigation of turbulent odor plumes. To examine the contribution to navigation from these two temporal features alone, we ignore other sensory modalities, such as concentration gradient sensing, bilateral sensing, and vision. We first demonstrate analytically that the dynamical model proposed in the first study above picks out (in appropriate limits) odor signal intermittency, while the model in the second study responds to the frequency of odor hits. These two temporal features are complementary and can be varied independently, forming a natural basis of temporal sensing. We devised a simple model that incorporates intermittency sensing and frequency sensing in a minimal way, and uses these two ‘sensors’ to drive upwind orientations. Using agent-based simulations, we first show that this combined model requires both sensors to successfully navigate both measured plumes used in the two studies. We then applied the navigational model to simulated plumes, leveraging an advecting-diffusing packet framework that mimics odor motion in turbulent flows (Farrell et al., 2002). We find that to robustly navigate a variety of plumes agents should use both intermittency and frequency sensing. However, there is a trade-off in performance when using both temporal features simultaneously, which persists across a variety of plumes. This predicts a strong benefit to modulating the weight of these two sensors, and we propose simple experiments to test whether flies or other insects indeed carry out such adaptation on slower timescales. Finally, we explore how simultaneous frequency and intermittency sensing is enabled by the Drosophila olfactory circuit, using previously developed models of ORNs and their synaptic connections to PNs (Gorur-Shandilya et al., 2017; Nagel et al., 2015). We find that PNs respond independently to both features and enable effective navigation through various environments, suggesting that the first stage of olfactory processing is appropriately tuned for naturalistic navigation tasks.

## Results

### Two experimentally constrained models implicate distinct odor signal features in olfactory navigation

Our study is motivated by two models recently extracted from experimental observations of walking Drosophila navigating odor plumes (Álvarez-Salvado et al., 2018; Demir et al., 2020). Here, we examine how they each respond to distinct temporal features of the odor concentration. We focus on temporal changes in odor concentration rather than odor flux (which depends also on air speed) as Drosophila melanogaster ORN responses are invariant to air speed (Zhou and Wilson, 2012). In the first model (Figure 1A; Álvarez-Salvado et al., 2018), the instantaneous odor concentration $odor(t)$ is first compressed into the range 0–1 using an adaptive Hill function:

$$
C(t)=\frac{odor(t)}{odor(t)+k_{d}+A(t)}.
$$

![Figure 1.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig1-v2.jpg)

**Figure 1.:** (A) Two experimentally informed models (Álvarez-Salvado et al., 2018; Demir et al., 2020) of Drosophila olfactory navigation transform odor signals in distinct ways. Left column: the intermittency model compresses the odor signal with an adaptive nonlinearity into a representation $Ct$ , bounded between 0 and 1. $Ct$ is then exponentially filtered with timescale $\tau_{ON}=0.72s$ to generate $ONt$ . Right column: the frequency model thresholds the odor signal (dashed line in top plot) into a binary representation $wt$ , which is then passed through an exponential filter with timescale $\tau_{F}=2s$ to generate $Ft$ . (B) Response of each of the models (bottom two plots) to a binary odor signal (top plot) of high intermittency, high frequency (region 1), high intermittency, low frequency (region 2), and low intermittency, high frequency (region 3). The intermittency model is sensitive to the intermittency of the signal – in regions 1 and 2, it approaches a high value asymptotically, but a low value when intermittency is low, even if the frequency remains high (region 3). The asymptotic values of the intermittency model (dashed lines) are $\frac{I}{1+I}$, where I is signal intermittency (Materials and methods). Conversely, the frequency model exhibits sensitivity to the frequency of encounters, tending asymptotically towards $f⋅\tau_{F}$, where $f$ is the signal frequency (dashed line). The frequencies in the three regions are 2 Hz, 0.5 Hz, and 2 Hz, the encounter durations are 0.45 s, 1.8 s, and 0.1 s, and the intermittencies are thus 0.9, 0.9, and 0.1.

The half-max is set by $At$ , a low-pass-filtered sliding average of the instantaneous odor concentration

$$
\tau_{A}\frac{dA}{dt}=odor(t)−A(t).
$$

This mimics the gain adaptation of ORNs to the mean signal (Cao et al., 2016; Gorur-Shandilya et al., 2017). At the onset of a sudden increase in odor concentration, the compressed signal $Ct$ increases instantaneously before relaxing back to ~0.5 with timescale $\tau_{A}=9.8$ s. The compressed signal $Ct$ is then exponentially filtered into an ‘ON’ function,

$$
ON(t)=\int_{0}^{t}\frac{1}{\tau_{ON}}⋅e^{\frac{t^{′}−t}{\tau_{ON}}}⋅C(t^{′})dt^{′},
$$

which drives odor-elicited behavioral actions. When $ON(t)$ is high, the fly accelerates and biases its heading upwind; when $ON(t)$ is low, the fly’s orientation randomizes and drifts downwind and its walking speed reduces (Álvarez-Salvado et al., 2018). We show analytically (Materials and methods) that the value of $ON(t)$ – and therefore the navigational actions – is largely determined by the intermittency of the odor signal, defined as the percentage of time an odor signal is present. Thus, we refer to this model as the intermittency model.

In the second model (Figure 1A; Demir et al., 2020), a detection threshold is used to detect when the odor arrives. This results in a binary time series $wt$ , which spikes as a $\delta$-function each time the odor concentration crosses the threshold from below, and is 0 otherwise. The frequency of odor encounters is then estimated by filtering $wt$ with an exponential:

$$
F(t)=\int_{0}^{t}e^{\frac{t^{′}−t}{\tau_{F}}}w(t^{′})dt^{′}.
$$

Thus, $Ft$ rises by 1 at each threshold crossing, before decaying exponentially with timescale $t_{w}$ until the next odor hit. In this model, $Ft$ plays a similar role as $ONt$ in the previous model, in that it drives behavioral response to odors. When $Ft$ increases, flies increase their bias upwind and stop less frequently and for a shorter time (Demir et al., 2020). Since $Ft$ is effectively a running average of the frequency of odor hits, we refer to this model as the frequency model.

To illustrate how each of these two sensory modalities respond to the temporal features of odor signals, we plotted the output of each filter in response to square-wave odor pulses of given frequency and intermittency (Figure 1B). These two features can be independently tuned – an odor signal can be high frequency and high intermittency if the whiffs (periods above threshold) are interrupted frequently with blank periods that are very short (region 1 in Figure 1B), while it can have high intermittency but low whiff frequency if whiffs are interrupted with short blank periods occurring more sparsely (region 2 in Figure 1B). In the first two regions of the signal, where intermittency is high, the response of the $ON(t)$ model approaches a high value after an initial transient, while it drops to a lower steady state in region 3 where the signal intermittency is lower. The steady-state response of $ON(t)$ is sensitive to the signal intermittency, but is independent of the whiff frequency, as indicated by the average response asymptote $\frac{I}{1+I}$, which monotonically increases with intermittency (Materials and methods). In contrast, the frequency model responds strongly in regions 1 and 3, where whiff frequency is high, consistent with its asymptotic response $f∙\tau_{F}$ (Materials and methods). This happens irrespective of the disparity in signal intermittency between these regions (Figure 1B, bottom trace). Note that both models are sensitive to the temporal characteristics of the signal, but not absolute concentration.

Though these two models were extracted from the same model organism with the same locomotive repertoire – fruit files walking in a 2D arena – the experiments were performed in very different odor and flow conditions. The intermittency model was first extracted from flies navigating a uniformly odorized region of odor within a laminar airflow (Álvarez-Salvado et al., 2018). Using simulations, the model was then shown to qualitatively recapitulate navigational behavior in a measured near-bed turbulent plume (Connor et al., 2018; Figure 2A), which we call the high-intermittency plume, in which the odor signal was ever-present and varied on relatively long timescales of several seconds or more (Figure 2B). In contrast, the frequency model was fit to trajectories of flies navigating a plume with a high degree of spatial complexity (Figure 2D) generated by perturbing a fast laminar flow with stochastic lateral jets, which we call the high-frequency plume. In that experiment, odor whiffs occurred frequently (2–5 Hz) (Figure 2E and F) and were much shorter (~100 ms) (Figure 2E). The two navigational models these experiments informed were clearly shaped by the plumes’ natural features: in the first, odor intermittency reached as high as 100% and whiff frequencies rarely surpassed 1 Hz (Figure 2C), whereas in the latter, the signal had intermittency mostly below 30% but whiff frequencies of several Hz (Figure 2F). Together, these two experiments and corresponding models suggest that flies use both odor frequency and intermittency to navigate upwind in different environments. This prompted us to ask how this dual-sensing capability might enhance the efficacy and robustness of navigation in different conditions.

![Figure 2.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig2-v2.jpg)

**Figure 2.:** (A) Snapshot of measured high-intermittency plume, reproduced from data in Connor et al., 2018. Colored dots: locations corresponding to odor series in (B). (B) Odor concentration time series at different locations in high-intermittency plume. (C) Intermittency versus whiff frequency for 10,000 uniformly distributed points in the high-intermittency plume. Statistics were calculated over the length of the full video. We see a range of intermittencies and many points with high intermittencies but relatively low frequencies. (D, E) High-frequency plume and representative time series, reproduced from data in Demir et al., 2020. (F) Analogous to (C) for the high-frequency plume. Data is clustered within a higher range of frequencies but low intermittencies.

### Dual intermittency and frequency sensing enhances navigation robustness in distinct environments

To next investigate how these dual-sensing capabilities – odor intermittency sensing and frequency sensing – shape navigational performance in distinct odor landscapes, we incorporated them into a combined navigational model. It is known that odor signals influence many behavioral actions, including accelerating, turning, and stopping (Álvarez-Salvado et al., 2018; Baker and Vickers, 1997; Demir et al., 2020; Mafra-Neto and Cardé, 1994; Vickers and Baker, 1994). Given the near-universal response of insects to turn upwind or bias their turns upwind in the presence of odor (Baker et al., 2018), here we assumed agents walk at a constant speed unless they are turning and focused on signal-driven changes in orientation. Turns occur randomly at a Poisson rate $\lambda_{turn}$, and turn magnitudes are sampled from a normal distribution $N30^{o},8^{o}$ as found before (Demir et al., 2020). Turn directions (sign of the orientation change) are modeled as

$$
p(turnupwind|turning)=\frac{1}{1+e^{−g_{I}ON−g_{F}F}}.
$$

Thus, the likelihood that a turn is directed upwind (versus downwind) increases sigmoidally with a linear combination of $Ft$ and $ONt$. In the absence of signal, upwind and downwind turns are equally likely: $Pupwindturn=0.5$. To allow frequency sensing to be adaptive, we set the detection threshold for $Ft$ to be variable and equal to $\frac{1}{2}At$, where $At$ is defined in Equation 2. The ‘sensor gains’ $g_{I}$ and $g_{F}$ were set to 3.9 and 0.2, respectively, by comparing to experimental data (Materials and methods). For now, we hold the gains fixed at these ‘base’ values $g_{I0}=3.9$ and $g_{F0}=0.2$; below, we investigate the performance of different $g_{I}$ and $g_{F}$. Finally, we define intermittency-only and frequency-only sensing models by setting $g_{F}$ and $g_{I}$ to 0, respectively.

To examine how frequency and intermittency contribute to navigational performance in this combined model, we simulated $N$ agents navigating both the high-intermittency and high-frequency plumes. The initial position and orientations of the agents were randomized uniformly. Performance was quantified as the fraction of agents that reach within 15 mm of the source in the presence of an odor signal, $\frac{N_{s}}{N}$ , minus the fraction of agents, $\frac{N_{c}}{N}$ , that reach the source by chance, that is, when no signal is present. Individual trajectories of successful flies in either plume look similar: when oriented away from the source, agents are quickly able to reorient within the plume region and navigate to the source with relatively straight trajectories combined with occasional corrective kinks (Figure 3B). Overall, agents navigated successfully in both plumes (Figure 3C), and performance was relatively robust to initial angle and position (Figure 3D). However, when either frequency sensing $g_{F}=0$ or intermittency sensing $g_{I}=0$ was removed, performance degraded (Figure 3D) in one of the plumes and became more sensitive to initial conditions. Though not wholly surprising that removing sensors degrades performance, this suggests that a simple linear combination robustly navigates two disparate odor plumes, without exhibiting any obvious failure modes due to interference between sensors.

![Figure 3.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig3-v2.jpg)

**Figure 3.:** (A) Our model linearly combines an intermittency sensor (red) and whiff frequency sensor (blue) to bias upwind motion. For both sensors, the odor signal is transformed using an adaptive compression step $At$ (Álvarez-Salvado et al., 2018) before being converted into a turning bias. Following (Demir et al., 2020), turns occur stochastically at a constant Poisson rate $\lambda_{turn}$ , while the sensor output B biases the likelihood that turns are upwind. Turn magnitudes are chosen from a normal distribution with mean 30° and SD 8° (Demir et al., 2020). (B) Example successful trajectories in the high-intermittency and high-frequency plume (Figure 2). (C) Percentage of agents that reach within 15 mm of the source when signal is present minus same percentage when signal is absent, for the model with only intermittency sensing ($g_{F}=0$; red), only frequency sensing ($g_{I}=0$; blue), or both ($g_{F},g_{I}$ nonzero; purple), in the high-intermittency plume (top) and high-frequency plume (bottom). Error bars: SEM calculated by bootstrapping the data 1000 times (Materials and methods). (D) Distribution of initial downwind position x (first column), crosswind position y (second column), and orientation (third column) for successful agents for the high-intermittency (top row) and high-frequency (bottom row) plumes. Colors correspond to same models as in (C). Upwind heading is 180°, and shaded regions represent SEMs obtained from bootstrapping (Materials and methods) (E) Time-averaged relative filter weight $≔\frac{g_{I}ON-g_{F}F}{g_{I}ON+g_{F}F}$ for different points in the two plumes.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) The simplified model linearly combines a pure intermittency sensor (red) and whiff frequency sensor (blue) to bias upwind motion. Turns occur as above. (B) Example successful trajectories in the high-intermittency and high-frequency plume (see Figure 2). (C) Percentage of agents that reach within 15 mm of the source when signal is present minus same percentage when signal is absent, for the model with only intermittency sensing ($g_{F}=0$; red), only frequency sensing ($g_{I}=0$; blue), or both ($g_{F},g_{I}$ nonzero; purple), in the high-intermittency plume (top) and high-frequency plume (bottom). Error bars: SEM calculated by bootstrapping the data 1000 times (Materials and methods). (D) Distribution of initial downwind position x (first column), crosswind position y (second column), and orientation (third column) for successful agents for the high-intermittency (top row) and high-frequency (bottom row) plumes. Colors correspond to same models as in (D). Upwind heading is 180°, and shaded regions represent SEMs obtained from bootstrapping (Materials and methods). (E) Time-averaged relative filter weight $≔\frac{g_{I}I-g_{F}F}{g_{I}I+g_{F}F}$ for different points in the two plumes.

Our upwind bias function (Equation 5), though phenomenological, is a natural choice in that it allows an increased upwind response to both the $ON$ and $F$ filters. In fact, it very closely approximates a logical OR gate for the two filters (Materials and methods; Equations 34-35). This raises the question of whether this particular logical operation is ideal. We similarly investigated an AND gate implementation, finding clear failure modes (Materials and methods).

We expect that the two sensors do not contribute equally at all times to the navigation and that the relative contribution of either sensor may depend on plume statistics or on the location within a plume (Rigolli et al., 2021). For example, in the high-frequency plume, the intermittency sensor is likely to also be active near the plume centerline, where the signal is more likely to be present, while in the high-intermittency plume the frequency sensor is likely to be active on the edges where the presence of odor is less certain. To quantify this, we measured the relative weight of each sensor $\frac{g_{I}ONt-g_{F}Ft}{g_{I}ONt+g_{F}Ft}$ , which interpolates between pure intermittency sensing (+1) and pure frequency sensing (–1). As expected, the intermittency sensor dominates in the high-intermittency plume, whereas the frequency sensor dominates in the high-frequency plume (Figure 3E). Still, this dominance is not absolute. For example, frequency sensing plays a role near the conical boundary of the high-intermittency plume. Likewise, intermittency contributes along the centerline of the high-frequency plume.

These modest but significant contributions led us to next wonder how the sensors might be relatively weighted to optimize navigational performance and how this weighting might change in different plumes. Therefore, for tractability, we constructed a simpler model that eliminated some parameters. Firstly, we retained the frequency sensor $Ft$ (Equation 4), but used a fixed odor detection threshold K rather than an adaptive threshold as before. Secondly, we replaced the $ONt$ function with:

$$
I(t)=\frac{1}{2}⋅\int_{0}^{t}\frac{1}{\tau_{I}}⋅e^{\frac{t^{′}−t}{\tau_{I}}}⋅Θ(odor(t^{′})−K)dt^{′}.
$$

where $Θ$ is the Heaviside step function. The primary change from $ONt$ is the replacement of adaptive odor compression with a fixed binarizing odor threshold. The factor of ½ is kept for ease of comparison between $It$ and $ON(t)$, so that both filters asymptotically approach ½ in the presence of continuous odor (Materials and methods). Filtering timescales were set at $\tau_{I}=\tau_{F}=2s$ for both $It$ and $Ft$ . While these changes do affect some quantities, like the relative filter weight in the two environments, the overall effect on navigational success is minimal (Figure 3—figure supplement 1). Thus, to study the effect of various model parameters in detail, we used this simplified model for all further investigations.

### Optimal performance requires distinct weighting of frequency and intermittency in different environments

Upwind bias, and therefore navigation performance, depends on the sensor gains (Equation 5), which up to now we have fixed to experimentally informed values (the ‘base’ gains). To investigate the influence of relative sensor weight in navigation, we quantified navigational performance as a function of both the sensor weights $g_{I}$ and $g_{F}$ and the plume’s spatiotemporal complexity. To remove constraints due to the limited spatial and temporal resolution of the recorded plume videos, and to easily investigate a wide range of environments, we switched to simulated plumes using a simple dispersion model (Farrell et al., 2002). Gaussian packets of odor are released from a source at a fixed Poisson rate $\lambda$ and advected by a velocity field composed of a uniform downwind velocity $U$. Normally distributed random perturbations $η_{x}$ and $η_{y}$ are added to the packet positions in the crosswind and downwind directions, respectively, at each time step, to account for the effects of turbulent diffusivity. The turbulent diffusivity models the effects of turbulent eddies as a diffusive process, but with diffusion constant $κ$ that can greatly exceed molecular diffusivity. In addition, the Gaussian packets grow in size with an effective diffusivity $D$ to account for the combined effects of molecular diffusion and smaller eddies in the wind flow (Figure 4A and B). Varying $U$ and $D$ allowed us to generate plumes with diverse temporal statistics. $U=36mm/s$ and $D=52mm^{2}/s$ resulted in a plume with longer whiff durations and high intermittency (Figure 4C and E). Increasing the wind speed to $U=300$ mm/s and decreasing effective diffusivity to $D=10mm^{2}/s$ resulted instead in a high-frequency plume with much shorter whiffs (Figure 4D and F). In each plume, we simulated 10,000 agents with uniformly distributed initial position and heading angle, where each agent navigated with a fixed set of gains $g_{I}$ and $g_{F}$ . We investigated various choices of $g_{I}$ and $g_{F}$ , from 0 to 50× the base gains.

![Figure 4.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig4-v2.jpg)

**Figure 4.:** (A) Example of a simulated odor plume, following the framework in Farrell et al., 2002. Gray circles denote Gaussian odor packets. (B) Example trajectory of a single-odor packet in these simulations and illustration of its growth. (C) Same as Figure 2C but for the simulated high-intermittency plume. (D) Same as (C) but for the simulated high-frequency plume. (E) Example odor concentration time series in a simulated high-intermittency plume. (F) Same as (C), for a high-frequency plume. (G) Normalized success percentage $S´$ within the simulated high-intermittency plume after adding noise to I and F. $S´$ is computed by first calculating the success percentage as in Figure 3C for each pair of gains $g_{I},g_{F}$ and then normalizing by the maximum success percentage over all $g_{I},g_{F}$ . Gains are measured in multiples of the base gains, defined in Materials and methods. (H) Same as (G), but for the simulated high-frequency plume. (I) $S´$ in the simulated high-intermittency plume versus $S´$ in the simulated high-frequency plume, where each dot represents a different $g_{I},g_{F}$ . Points are colored by the relative weighting of the two sensors (see Materials and methods for calculation details). Note here that a finer set of gains was considered than in (G) and (H) and normalization was done with respect to these gains. The pair $g_{I},g_{F}$ that maximized the geometric mean of normalized success percentage across the two plumes is indicated as optimal. The concavity of the front suggests a sharp trade-off in performance in one plume versus the other.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Normalized success in the simulated high-intermittency plume (A) and simulated high-frequency plume (B) for different sets of $I$ and $F$ gains. We see strong performance in (B) for a large region at high-intermittency gains $g_{I}$ .

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Normalized success in the simulated high-intermittency plume (A) and simulated high-frequency plume (B) for different values of $\tau_{I}$ and $\tau_{F}$ . Performance varies with $\tau_{F}$ and much more slowly with $\tau_{I}$ . (C) Normalized success in the simulated high-frequency plume for different values of $\tau_{F}$ and $g_{F}$ . Performance is roughly symmetric about $\tau_{F}=g_{F}$ , as expected.

The $g_{I}$ and $g_{F}$ maximizing performance in our simulated high-intermittency plume was reasonably constrained, with a clear maximum occurring around the experimentally derived base gain (Figure 4—figure supplement 1). However, in the simulated high-frequency plume, a variety of gains led to similarly maximal performance (Figure 4—figure supplement 1), including some with values an order of magnitude larger than the base gains. Performance was largely independent of $\tau_{I}$ over nearly two orders of magnitude (unchanged even for a null algorithm that drives upwind orientation whenever odor is present, i.e., $\tau_{I}=0$) and scaled with $\tau_{F}$ in a way that could be absorbed into the $g_{F}$, (Figure 4—figure supplement 2; Materials and methods), so these trends were fundamentally due to the sensor gains rather than other model features. On the other hand, models with extreme gain factors could compound the effects of noise, leading to a lack of robustness in natural conditions. We therefore added Gaussian noise to the I and F filters – noise amplitude was 5% of the average value of I (F) in the center of the simulated high-intermittency (high-frequency) plume. This removed maxima at high gains but retained clear maxima at lower gains (Figure 4G and H). Interestingly, the unique maxima sat fairly close to the base gain values (values of 1 in Figure 4G and H), suggesting a degree of tuning within the biological fly olfactory circuit. Finally, the optimal gains for the simulated high-intermittency and high-frequency plumes had $g_{F}=0$ and $g_{I}=0$, respectively, indicating that optimal performance in either plume requires silencing the nonrelevant sensors. This inherent trade-off illustrates that simply augmenting the sensory capability can at times degrade performance. This suggests a benefit for sensor specialization in distinct environments.

### Performance trade-off between intermittency sensing and frequency sensing in different environments

To get a better understanding of how navigational performance in these two simulated plumes depends on the sensor weights, we did a tighter sweep of gains near the performance maxima (Figure 4G and H) for each plume. For each set of gains, we then plotted performance in the high-intermittency plume against that in the high-frequency plume. For comparison, we also plotted the set of gains $(g_{I}^{∗},g_{F}^{∗})$ that maximized the geometric mean of normalized success in both plumes (indicated in Figure 4I). The resulting scatterplot quantifies the performance in the two plumes for different navigational models, where each model is parameterized by its sensor weights $g_{I}$ and $g_{F}$ . In general, the scatterplot fills out a region near the origin, bounded by a curve that forms a ‘Pareto front’ of navigational performance. This Pareto front reveals a performance trade-off for the different models: combinations of $g_{I}$ and $g_{F}$ that are weighted toward I do better in the high-intermittency plume, while combinations weighted toward F outperform in the high-frequency plume (Figure 4I). There was no fixed set of gains that performs optimally in both plumes. Importantly, the apparent concavity of the Pareto front illustrates a somewhat steep trade-off and suggests that flies might be better off modulating gains and switching between using intermittency and frequency sensors to bias upwind motion, as opposed to using both simultaneously.

We then wondered how this trade-off manifests across a more diverse spectrum of plumes. The computational simplicity of the turbulent plume model allowed us to study a wide array of turbulent plumes differing in their temporal statistics. We fixed the gains to the values that optimized the geometric mean between the high-intermittency and high-frequency plumes, $(g_{I}^{∗},g_{F}^{∗})$, and then varied the environmental parameters $U$ and $D$ to smoothly interpolate between the high-frequency and high-intermittency plumes investigated above. Success was roughly uniform in the different environments (Figure 5A). However, removing the frequency sensor ($g_{F}^{}=0$) significantly improved performance in the slowly advecting and highly diffusive plumes (low U; high D), which tend to be smoother in their concentration profiles. The reverse was true when we removed intermittency sensing ($g_{I}=0$), exemplifying a trade-off in navigational performance that persists across this wide range of odor environments. Together with the results presented above (Figure 3), this suggests that while a naïve summation of temporal sensors may be beneficial in some cases, in general, navigation can always be improved by some degree of specialization.

![Figure 5.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig5-v2.jpg)

**Figure 5.:** Normalized success percentage for a frequency and intermittency-sensing model (A), only intermittency-sensing model (B), and only frequency-sensing model (C) for a range of simulated odor plumes. Success percentage is normalized such that the best performance of the three models is set to 1 for each environment. Gains for (A) were chosen to optimize the geometric mean of performance in the simulated high-intermittency and high-frequency plumes. Gains in (B) and (C) were chosen by taking the gains in (A) and then setting gF (A) and gI (C) to 0.

### Biophysical neural filtering of odor signals enables independent frequency and intermittency sensing and aids in navigation

Our results so far suggest that dual sensing of two complementary odor signal features, intermittency and frequency, aids navigation across a diversity of odor plumes, albeit with a trade-off. To what extent is this dual-sensing capability enabled by the Drosophila olfactory circuit? Prior experimental and modeling work has shown that synaptic and circuit mechanisms in the olfactory periphery allow for accurate signal transmission across a range of frequencies (Martelli and Fiala, 2019; Nagel et al., 2015), while fast ORN adaptation allows signals to be encoded without saturation (Gorur-Shandilya et al., 2017). These various mechanisms suggest that the natural structure of the fly olfactory circuit may be well-primed for robust encoding of multiple temporal features of the odor signal.

We thus combined prior models (Gorur-Shandilya et al., 2017; Nagel et al., 2015) into a single model of odor binding, ORN firing, and PN response, and fed this naively into a behavioral module to investigate navigational performance. At the first stage of processing, odors bind an olfactory receptor/co-receptor (Or/Orco) complex, which can be active (ion channel open) or inactive (closed). Assuming fast binding dynamics, the average activity $a$ of the complex is

$$
a=1+e^{ϵ}⋅\frac{1+\frac{C}{K_{off}}}{1+\frac{C}{K_{on}}}^{-1}
$$

where C is the odor concentration, $ϵ$ is the free energy difference between the active and inactive states when unbound, and where the dissociation constant between odorant and the complex in the inactive state, $K_{off}$ , is much higher than that for the active state, $K_{on}$ . To model adaptation, receptor activity feeds back into $ϵ$ via

$$
\frac{dϵ}{dt}=\betaa-a_{0}
$$

where $\beta$ is an adaptation rate and $a_{0}$ is a baseline activity. ORN firing rate is then obtained by passing $a$ through a linear filter and static nonlinearity (Figure 6A; see Materials and methods). Finally, $ϵ$ is bounded from below ($ϵ§amp;gt;ϵ_{L}$) so that ORNs shut off with sufficiently weak odor.

![Figure 6.](https://cdn.elifesciences.org/articles/72415/elife-72415-fig6-v2.jpg)

**Figure 6.:** (A) A schematic for how we combine the models of Gorur-Shandilya et al., 2017 and Nagel et al., 2015 to convert odor signals to projection neuron (PN) membrane potentials. (B) Time-averaged PN membrane potentials in square-wave environments of different frequency and intermittency. Responses were simulated for 30 s and last 20 s were averaged. (C) Performance of different navigation models considered in the simulated high-intermittency plume. Success was computed as in Figures 3 and 4. (D) Same as (C) but for the simulated high-frequency plume. Note that in (C) and (D) no noise was added to the filter outputs for any of the models.

ORN firing rate is converted into a PN membrane potential through a postsynaptic conductance with two timescales (Nagel et al., 2015). Conductances are weakened over time via synaptic depression, also with two timescales (Figure 6A). This depression is modeled by a scaling factor of the conductance, $A_{fast}t$ (analogously for $A_{slow}t$):

$$
\frac{dA_{fast}}{dt}=-r_{fast}stA_{fast}t+\frac{1-A_{fast}t}{\tau_{Afast}}
$$

where $s$ is the ORN firing rate, $r_{fast}$ is the rate that $A$ decays with increased firing rate, and $\tau_{Afast}$ is the timescale it takes for $A_{fast}$ to relax back to 1. This scaling factor then affects the synaptic conductance via

$$
\frac{dq_{fast}}{dt}=k_{fast}s(t)⋅A_{fast}(t)−\frac{q_{fast}(t)}{\tau_{gfast}}
$$

where $q_{fast}$ is the fast conductance (analogous for the slow conductance). The fast and slow conductances are summed to give a total synaptic conductance $q_{syn}$ . The PN membrane potential $Vt$ then obeys

$$
\frac{dV}{dt}=\frac{-Vt-E_{leak}+q_{syn}tR_{m}Vt-E_{syn}}{\tau_{m}}
$$

where $E_{leak},E_{syn}$ are the reversal potential for leak and synaptic currents, respectively, $R_{m}$ is the resistance of the membrane, and $\tau_{m}$ is the timescale of the membrane. For parameter values, see Materials and methods and Nagel et al., 2015.

We first looked to see how the PN membrane potential responds to environments of different temporal statistics. As in Figure 1, we simulated the potential in square-wave environments of varying frequencies and intermittencies. We find that average membrane potential increases with frequency and intermittency independently (Figure 6B). This suggested that this membrane potential could be used to navigate environments where only one of intermittency or frequency is high. To test this, we considered a navigator that used the difference between the membrane potential and its resting potential (i.e., $E_{leak}$) to generate an upwind bias:

$$
p(turnupwind|turning)=\frac{1}{1+e^{−g_{PN}(V−E_{leak})}}
$$

where $g_{PN}$ is the base gain for this model chosen analogously to the other base gains (see Materials and methods). While the circuit-inspired model was outperformed by the single-sensor models when these were used in matching environments (i.e., the F model in the high-frequency plume and the I model in the high-intermittency plume) (Figure 6C and D), it performed better than the individual F and I models when those were used in suboptimal environments. Thus, the dual-sensing capability of the ORN-PN circuit translates directly to more effective navigation across diverse plumes. Of course, as our results above showed, some degree of modulation of the gains could further enhance performance (Figures 4I and 6C and D, purple) – say by amplifying frequency sensing in certain plumes. It would be interesting to investigate whether any such modulation is enacted by the insect olfactory circuit.

## Discussion

In this work, we used numerical simulations to explore the value of two temporal features of the signal – odor intermittency and encounter frequency – in navigating naturalistic odor plumes spanning a range of spatial and temporal complexity. These two features are a natural set in that they can be varied independently to create a variety of odor signals (Figure 1). Other complementary and complete quantities could be used, such as whiff and blank duration (Rigolli et al., 2021), but we focused on these since they are directly implicated by various experiments in walking D. melanogaster. The navigation model we proposed reduces two experimentally informed models of fly olfactory navigation into elementary transformations that separately extract odor intermittency and encounter frequency, and then uses these two ‘sensors’ to bias the agent upwind. Our model is phenomenological, exploring the utility of different odor signal features in different environments, and so does not necessarily implicate any particular neural architectures. An interesting finding here is that the optimal agent in the two simulated plumes assigned weights to the sensors that resembled the weights inferred from experiment (Demir et al., 2020; Figure 4G and H, Materials and methods). This suggests that the manner in which temporal features are extracted and processed within the Drosophila olfactory circuit may already be adapted to natural plume environments.

Our work explores normative strategies, so our results have no bearing on whether such adaptation actually occurs. There is, however, evidence that such adaptation may exist at the level of individual neurons: for example, moth ORNs adjust their encoding efficiency to the local statistics of pheromones (Levakova et al., 2018). Additionally, upwind orientation was found to be independent of intermittency for fixed frequencies (Demir et al., 2020), suggesting that such adaptation of sensor weight may actually be present in walking Drosophila. Our work suggests future experiments, based on simple modifications of existing experimental paradigms, that could be used to quantify this slower-scale adaptation. One could present the complex odor plumes we generated in our recent work (Demir et al., 2020), while modulating the overall statistics on a slower scale via the speed or strength of the upwind lateral perturbations, the wind speed, or both, and record how upwind orientation depends on frequency or intermittency. Additionally, in general, flying flies are more likely to experience more complex, high-frequency odor environments than walking flies due to flying flies being far from solid boundaries (Connor et al., 2018). Thus, if such modulation of sensor weight occurs, flying flies might naturally assign more weight to frequency sensing, which could be tested experimentally in wind tunnels for flight (van Breugel and Dickinson, 2014).

A key finding here is that the known circuitry of the Drosophila olfactory periphery, namely, in ORNs (Gorur-Shandilya et al., 2017; Nagel et al., 2015) and PNs (Nagel et al., 2015), responds to both odor intermittency and frequency, aiding robust navigation across many odor environments. This suggests that the known neural circuitry at the first stages of olfactory processing is tuned, to some degree, to naturalistic navigation tasks. In our simulations, this model is still suboptimal, and performance might be improved by including the effect of lateral inhibition, which has been shown to modulate the frequency range encoded by PNs (Nagel et al., 2015), as well as further processing in later stages of the circuit (Rapp and Nawrot, 2020). Also, we did not include much slower adaptive components (~10 s) of synaptic depression that modulate activity of Drosophila PNs (Martelli and Fiala, 2019). Given that this timescale is similar to that of the behavioral adaptation found by Álvarez-Salvado et al., 2018, it is plausible that this modulation could improve navigation. It has also been shown that knockdown of the priming factor unc13A impedes fast components of ORN-PN synaptic transmission in Drosophila (Fulterer et al., 2018; Pooryasin et al., 2021) and affects behavioral responses to signals at higher frequencies (Fox and Nagel, 2021). It would be illuminating to test how unc13A knockdown affects navigation in complex plumes of different frequency content.

In the latter half of this study, we simulated a variety of odor plumes using a simple drift-diffusion model (Farrell et al., 2002). A more precise approach would be to numerically integrate the Navier–Stokes equations describing the wind flow, together with advective-diffusive scalar transport describing the dispersion of a scalar concentration field (Rigolli et al., 2021). In such simulations, resolving odor concentrations to the viscous scale is very computationally expensive. This would likely preclude the investigation over more than a handful of distinct odor plumes, as our simplified model allowed us to explore here. On the other hand, such detailed simulations show that even in a single plume the statistics of the odor change significantly with distance from the source, and therefore animals may benefit from modulating sensory strategies during navigation (Rigolli et al., 2021). This is consistent with our finding that frequency sensing contributes more near the edges of the plume than it does near the centerline, and vice versa for intermittency sensing.

There are several aspects of olfactory navigation not considered in this work. In particular, we have neglected the role of bilateral sensing between the two antennae. In insects, bilaterally resolved concentration sensing has been demonstrated in flies (Gaudry et al., 2013) and implicated in navigation of laminar ribbons (Duistermars et al., 2009). Bilateral sensing has also been demonstrated in mice (Rajan et al., 2006), sharks (Gardiner and Atema, 2010), and even humans (Wu et al., 2020), and has been implicated in effective navigation in aquatic environments (Michaelis et al., 2020). Spatially resolved information has been shown theoretically to provide more information about an agent’s position relative to the source of the odor (Boie et al., 2018) and aid olfactory navigation strategies, even in plumes with elements of stochasticity and turbulence (Hengenius et al., 2021). For very closely spaced antennae as in flies (<1 mm), these gradients are very difficult to resolve and so are often not useful for navigation (Celani et al., 2014; Crimaldi and Koseff, 2001; Shraiman and Siggia, 2000). Nonetheless, it would be interesting to consider the effect of bilateral comparisons of intermittency and frequency, particularly when modeling the navigation of species with larger antennae.

To this end, it has already been shown that bilateral comparisons of frequency allow agents to track the edges of some turbulent odor plumes (Michaelis et al., 2020). Additionally, recent work (Rigolli et al., 2021) has shown that odor intensity and temporal statistics are more useful in the central and outer regions of a turbulent plume, respectively, for predicting distance to the source. It is possible that in high-intermittency plumes organisms might use frequency to track the edges of odor plumes or even execute offset responses, such as those detailed in Álvarez-Salvado et al., 2018. Moreover, it has recently been shown that flies can use bilateral information to detect the direction of motion of odor signals (Kadakia et al., 2021), and that this information is particularly relevant in turbulent environments. In more diffuse and smooth plumes, odor velocity is less well-defined, and might be of more limited use. An interesting extension would be investigating how odor velocity could be incorporated optimally with odor intermittency and frequency in effective navigation.

For the sake of simplicity, we considered a model where agents move with a constant speed and only change orientation through a discretized turning paradigm, suggested by Demir et al., 2020. However, more diverse actions such as stopping and walking (Demir et al., 2020), speed modulation (Álvarez-Salvado et al., 2018; Mafra-Neto and Cardé, 1994), continuous heading modulation (Álvarez-Salvado et al., 2018), and casting/counter-turning behavior Álvarez-Salvado et al., 2018; Budick and Dickinson, 2006; Mafra-Neto and Cardé, 1994; Pang et al., 2018; Vickers and Baker, 1994 have also been observed in insect olfactory navigation. In future work, it will be worth investigating the role of intermittency and frequency in modulating behaviors such as these in different environments.

Finally, we have not explored the role of learning. The frequency and intermittency filters we used had no timescale longer than a few seconds, precluding history-dependent behavioral effects over longer timescales. History dependence in navigational decisions has been observed in flying fruit flies (Pang et al., 2018), where the magnitude of fly turns decreased with the number of signal encounters, in desert ants (Buehlmann et al., 2015), where ants used the existence of previously learned olfactory cues to navigate in a new environment, and in mice (Gire et al., 2016), where gradient climbing was abandoned for foraging when mice were sufficiently conditioned on known odor locations. Theoretical strategies such as infotaxis, where agents navigate by using cues to learn an internal probabilistic representation of their environment (Vergassola et al., 2007), also have some support in experiment (Calhoun et al., 2014; Pang et al., 2018). We find that robust navigation is enhanced by modulating intermittency and frequency sensing in time, and incorporating history dependence in our models could be done straightforwardly, with a few added parameters. Pairing this with behavioral experiments of the type suggested above would provide a fruitful direction for future study.

## Materials and methods

### Simulating ON and F responses to square waves

The frequency response function is defined as the convolution between the whiff onset time series $wt$ and an exponential filter with decay timescale $\tau_{F}$ where the whiff time series is a sum of delta functions occurring at the onset of each whiff. Thus, we have

$$
F(t)=\int_{−∞}^{t}w(t−s)e^{\frac{−s}{\tau_{F}}}ds=\sumk\int_{−∞}^{t}\delta(t−t_{k}−s)e^{\frac{−s}{\tau_{F}}}ds=\sumke^{\frac{−t−t_{k}}{\tau_{F}}}
$$

where $k$ enumerates the whiffs. Note that $Ft+Δt=Fte^{\frac{-Δt}{\tau_{F}}}$ . Therefore, in discrete time steps we have $wt+Δt=1$ if $odort§amp;lt;K$ and $odort+Δt\geqK$ and 0 otherwise and $Ft+Δt=Ft⋅e^{\frac{-Δt}{\tau_{F}}}$ if $wt+Δt=0$ and $Ft+Δt=Ft⋅e^{\frac{-Δt}{\tau_{F}}}+1$ if $wt+Δt=1$.

For $ONt$ , we use Euler’s method to numerically integrate Equation 2 to obtain $At$ and then similarly integrate the following equation:

$$
\frac{dON}{dt}=\frac{1}{\tau_{ON}}(C(t)−ON(t))
$$

where $Ct$ is defined in Equation 1, and the above equation is equivalent to Equation 3. $\tau_{F}$ was set to 2 s (Demir et al., 2020) while $\tau_{A}$ and $\tau_{ON}$ were set to 9.8 s and 0.72 s, respectively (Álvarez-Salvado et al., 2018). The detection threshold was assumed to be below the signal amplitude, and $k_{d}$ was set to be 1% of the signal amplitude.

### Calculation of ON, I, and F responses to square waves

To illustrate how the ON and F filters respond to the frequency and duration of odor signals, we consider their response to square-wave odor pulses of given frequency $f$, duration $D$, and amplitude $S_{0}$ . We first consider the ON response. To understand the ON response, we first calculate $At$ . From Equation (2), we have

$$
\frac{dA}{dt}=\frac{1}{\tau_{A}}⋅(odor−A)
$$

Let $A_{n}$ denote the value of $A$ at the offset of the $nth$ pulse of signal and $A_{n}^{∗}$ denote the value of $A$ at the onset of the $nth$ pulse. We wish to obtain a recursive relation for $A_{n}$, which will allow us to solve for $A_{n}$ and from there obtain the value of $A$ at all times. At the offset of a pulse, $odor=0$ and $A$ will exponentially decay with time scale $\tau_{A}$ until the onset of the next pulse. This time of decay is given by $\frac{1}{f}-D$. Hence at the onset of the next pulse, $A_{n+1}^{∗}=A_{n}⋅e^{−(\frac{1}{\tau_{A}}⋅(\frac{1}{f}−D))}$ . At this point, for a time period $D$, that is, until the offset of the $(n+1)th$ pulse, $A$ obeys the equation

$$
\frac{dA}{dt}=\frac{1}{\tau_{A}}⋅(S_{0}−A)
$$

with initial value $A_{n+1}^{∗}$ . Hence,

$$
\int_{A_{n+1}^{∗}}^{A_{n+1}}\frac{dA}{S_{0}−A}=\frac{D}{\tau_{A}}
$$



$$
A_{n+1}=A_{n}e^{\frac{−1}{f\tau_{A}}}+S_{0}(1−e^{\frac{−D}{\tau_{A}}})
$$



$$
A_{n}=A_{0}e^{\frac{−n}{f\tau_{A}}}+S_{0}(1−e^{\frac{−D}{\tau_{A}}})\sumk=0n−1e^{\frac{−k}{f\tau_{A}}}
$$



$$
=A_{0}e^{\frac{−n}{f\tau_{A}}}+S_{0}(1−e^{\frac{−D}{\tau_{A}}})⋅\frac{1−e^{\frac{−n}{f\tau_{A}}}}{1−e^{\frac{−1}{f\tau_{A}}}}.
$$



$$
A_{n}≈\frac{S_{0}(1−e^{\frac{−D}{\tau_{A}}})}{1−e^{\frac{−1}{f\tau_{A}}}}.
$$

Since this is the value of $At$ at the end of a pulse, it will be the maximum value of $At$ over one period. Ultimately, however, we are interested in computing $ONt,$ which obeys the equation

$$
\frac{dON}{dt}=\frac{1}{\tau_{ON}}⋅(\frac{odor}{odor+kd+A(t)}−ON).
$$

To understand the response of $ON$, we can consider three different signal timescales. If the signal fluctuates quickly with respect to $\tau_{A}$, that is, $D$ and $\frac{1}{f}-D$«$\tau_{A}$ , then for $t≫\tau_{A}$ one can approximate $At$ with its average value over one period, which is given by

$$
f⋅⟮\int_{0}^{\frac{1}{f}−D}\frac{S_{0}(1−e^{\frac{−D}{\tau_{A}}})}{1−e^{\frac{−1}{f\tau_{A}}}}⋅e^{\frac{−t}{\tau_{A}}}dt+\int_{0}^{D}\frac{S_{0}(1−e^{\frac{−D}{\tau_{A}}})}{1−e^{\frac{−1}{f\tau_{A}}}}e^{\frac{−(\frac{1}{f}−D)}{\tau_{A}}}⋅e^{\frac{−t}{\tau_{A}}}S_{0}⋅(1−e^{\frac{−t}{\tau_{A}}})dt⟯
$$



$$
=S_{0}⋅f⋅D
$$

Notice $f∙D=I$, the intermittency of the signal. Hence in this limit, and assuming $S_{0}≫kd$, when the signal is present, we have

$$
\frac{dON}{dt}=\frac{1}{\tau_{ON}}⋅(\frac{1}{1+I}−ON)
$$

Thus, $ONt$ obeys the same dynamics as $At$ , except that it adapts to a square wave of amplitude $\frac{1}{1+I}$ instead of $S_{0}$ and with a different timescale. Thus by the same reasoning as for $At$ , the maximum value of $ONt$ over one period (once $t≫\tau_{A},\tau_{ON}$) is approximately $\frac{1}{1+I}∙\frac{1-e^{\frac{-D}{\tau_{ON}}}}{1-e^{\frac{-1}{f\tau_{ON}}}}$, and the average value over one period is $I∙\frac{1}{1+I}$ .

If instead $\tau_{A}≈D$ or $\tau_{A}≪D$, then $At≈odort$, and we get

$$
\frac{dON}{dt}=\frac{1}{\tau_{ON}}⋅(\frac{1}{2}−ON)
$$

Finally, we can consider the case where $\tau_{A}≫D$ and $\tau_{A}≪\frac{1}{f}-D$ . In this case, $At≈0$ and $ONt$ adapts to a square wave with amplitude ≈ 1. The average value of $ONt$ is $I$ (and the maximum value would be $\frac{1-e^{\frac{-D}{\tau_{ON}}}}{1-e^{\frac{-1}{f\tau_{ON}}}}$).

In summary, we see that in all these cases the average value of $ON$ depends only on the intermittency and increases monotonically with intermittency.

For $F$, it is easiest to consider $F_{n}$ as the value of $F$ just after the onset of the $nth$ pulse. Since $F$ increases by 1 at the onset of each pulse and then decays exponentially with timescale $\tau_{F}$ until the onset of the next pulse, one has

$$
F_{n+1}=F_{n}⋅e^{\frac{−1}{f\tau_{F}}}+1.
$$

Hence,

$$
F_{n}=F_{0}⋅e^{\frac{−(n−1)}{f\tau_{F}}}+\frac{1−e^{\frac{−n}{f\tau_{F}}}}{1−e^{\frac{−1}{f\tau_{F}}}}
$$

where $F_{0}$ is the value of $F$ right before the onset of the first pulse. For $t≫\tau_{F}$, we have $n≫f\tau_{F}$ and $F_{n}≈\frac{1}{1-e^{\frac{-1}{f\tau_{F}}}}$ . Since $F$ jumps at the onset of a pulse and then decays, this is the maximum value of $F$. The average value of $F$ over one period is thus

$$
\frac{1}{1−e^{\frac{−1}{f\tau_{w}}}}⋅f⋅\int_{0}^{\frac{1}{f}}e^{\frac{−t}{\tau_{w}}}dt=f⋅\tau_{w}
$$

Hence, the average value of $F$ is linearly proportional to the frequency of the signal.

In a square wave, the $It$ filter obeys the exact same dynamics as $At$ , except with a pre-factor of $1/2$ (assuming the amplitude of the wave is above the detection threshold) and thus has an asymptotic average response of $I/2$ .

### Connection of navigation model to logical gates

We claim that Equation 5 is very similar to an OR gate in the variables $g_{I}ON$ and $g_{F}F$. To see this, let us first define what we mean by an OR gate. Normally, an OR gate in two binary variables A and B returns a 1 if any one of A, B is nonzero. This results in the following ‘truth table’:

#### Standard OR gate

<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

and can be expressed algebraically as $A+B-AB$. In our case, however, we want a null output to result in ½ since this should be the probability of turning upwind when no signal is present. Similarly, our variables of interest are $g_{I}ON$ and $g_{F}F$, which are nonbinary and in principle unbounded. Since in general we will want null outputs to be ½ and full outputs to be 1, it is natural instead to consider as variables A and B sigmoidal transformations of $g_{I}ON$ and $g_{F}F$. Thus, we can define for our purposes

$$
A=\frac{1}{1+e^{-g_{I}ON}}
$$



$$
B=\frac{1}{1+e^{-g_{F}F}}
$$

Then the truth table of an OR gate would look like the following table:

#### Navigation model OR gate

<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1/2</td>
      <td>1/2</td>
      <td>1/2</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1/2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1/2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

We then wish to determine an algebraic combination of A and B that will result in this output. Like in the case of a standard OR gate, it is easy to see we must go to second-order expressions in A and B. Due to the symmetry of the output in A and B, we need only consider symmetric second-order expressions:

$$
output=a_{0}+a_{1}A+B+a_{2}A⋅B+a_{3}A^{2}+B^{2}
$$

This gives us four equations with four unknowns (one equation for each row of our table), but one can see that the middle two equations are redundant and thus we have a free variable. One can thus set $a_{3}=0$ and get as an OR gate in our case:

$$
output=-1+2A+B-2AB
$$

In other words, for a full logical OR function we would have

$$
p_{}(turnupwind|turning)=−1+2(\frac{1}{1+e^{−x}}+\frac{1}{1+e^{−y}})−2⋅\frac{1}{1+e^{−x}}⋅\frac{1}{1+e^{−y}}
$$

where we have defined $x=g_{I}ON$ and $y=g_{F}F$. With this definition, Equation 5 then reads

$$
p(turnupwind|turning)=\frac{1}{1+e^{−(x+y)}}
$$

Comparing the two expressions, one can show numerically that they differ by at most 0.025, meaning for any $ON$ and $F$ values, $p(turnupwind|turning)$ for a true OR gate and for our model will differ by at most 2.5%. Hence, we claim that our model is a simple expression that well-approximates an OR gate. One can analogously compute what an AND gate would look like in our framework, giving

$$
p_{}(turnupwind|turning)=1+2AB−(A+B)
$$

We simulated agents in the video plumes using this strategy as well, and unsurprisingly, they performed poorly in both plumes. The performance in the high-frequency plume was slightly worse than the performance of the intermittency-only model in that plume, and the performance in the high-intermittency plume was slightly worse than that of the frequency-only model in that plume.

### Agent-based simulation in recorded odor plumes

The first plume recording we used is the same as used in Álvarez-Salvado et al., 2018. We call this plume the high-intermittency plume. The odor detection threshold of the agents was set by analyzing the signal in a region outside the plume. In this region, pixel values of 0 were removed and nonzero values were fit to a Gaussian. The detection threshold was then set to be the 3 standard deviations above the mean of this fit. 10,000 agents were initialized with uniformly distributed starting position, where the x-position was between 50 mm and 300 mm from the source and the y-position went from 80 mm below the source to 80 mm above the source. The initial heading angle was uniformly distributed from 0 to 360°. The simulation was run for the length of the video (240 s), and the discrete time step was set to be the reciprocal of the frame rate (1/15 s).

The second plume recording we used was taken from Demir et al., 2020. We call this the high-frequency plume. The odor detection threshold of each agent was set the same way it was in Demir et al., 2020. Again 10,000 agents were initialized with uniformly distributed initial position and heading. The initial x-position was between 38.45 mm and 288.45 mm, and the initial y-position was between –74 mm and 86 mm. Initial heading was uniformly distributed from 0 to 360°. The simulation was run for 123.3 s, starting from the 600th frame of the video to the last frame, at 89.94 frames/s, corresponding to the frame rate used in Demir et al., 2020. The first 600 frames were dropped so that the plume had expanded to full size when the simulations began.

In both simulations, odor signal was computed by averaging over an elliptical antenna-sensing region in front of the agent, as in Demir et al., 2020. The length of the region’s major axis was 1.5 mm, and the length of the minor axis was 0.5 mm. The ellipse was centered 1 mm in front of the agent. For all models, odor values below the detection threshold described above were set to 0 to minimize the effect of camera shot noise. When computing the $ON$ filter, the $k_{d}$ value was also set at this detection threshold value. If agents went outside the frame region, then they were allowed to continue but received zero signal in those regions. Thus, there were no walls in these simulations.

For these simulations, $F$ was computed as for the square-wave pulses, with a detection threshold as described above, but we also enforced that the whiff time series $wt$ could not register two whiffs less than 40 ms apart to capture the idea that the time resolution of individual whiffs is not arbitrarily precise and to avoid spurious detections due to the random fluctuations in the signal, as suggested by Demir et al., 2020.

### Determination of base gains from experiment

The base gains, $g_{I0}$ and $g_{F0}$ , which were used for the simulations in Figure 3, and in multiples of which the gains in Figures 4 and 5 are reported, were determined the following way. Demir et al., 2020 experimentally extracted a sigmoidal turning bias, as in Equation 6, except only using the $F$ filter and reported a gain of 0.242. We thus set $g_{F0}=0.242$. $g_{I0}$ was set so that the contribution from $I$ in the high- intermittency plume would be roughly the same size as the contribution from $F$ in the high-frequency plume. So defining $I_{0}$ and $F_{0}$ to be typical $I$ and $F$ values in the high-intermittency and high-frequency plumes, respectively, we have $g_{I0}I_{0}=g_{F0}F_{0}$ . We thus determined a $g_{I0}$ of 1.936. For the PN model, we considered $V_{0}$ to be the average value of the membrane potential in a high-intermittency environment and then set $g_{PN}V_{0}-E_{leak}=g_{F0}F_{0}$ , where $E_{leak}$ was set to –70 mV (see below). We thus determined $g_{PN}$ to be 0.057 /mV. Finally, for the parameters dictating the navigational actions, the turn rate was set to 1.3 /s, walking speed to 10.1 mm/s, and filter decay timescale $\tau$ to 2 s, all in accordance with the findings of Demir et al., 2020. Note that the same timescale was used for the $I$ and $F$ filters.

### Statistical methods

Error bars for success rates (Figure 3C) were computed by bootstrapping data from a simulation of 10,000 flies – 1000 resamples were used with each resample size being equal to 10,000. Similarly, for the histograms of successful initial conditions, the data was resampled 1000 times, where each resample size was the size of the original data and means and standard deviations were computed and used for each histogram bin.

### Agent-based simulation in simulated odor plumes

The simulated odor plumes were created using the strategy laid out by Farrell et al., 2002. Plumes consisted of growing Gaussian packets of odor concentration, released as a Poisson process with rate $\lambda$, that were advected by a uniform mean wind velocity and perturbed by turbulent diffusivity. The concentration at a point $x,y$ due to a packet centered at $x_{i},y_{i}$ was computed as

$$
odor_{i}(x,y)=\frac{C_{0}}{\pi(R_{0}^{2}+4Dt_{i})}exp(\frac{−r_{i}^{2}}{(R_{0}^{2}+4Dt_{i})}),
$$

where $r^{2}=x-x_{i}^{2}+y-y_{i}^{2}$ , $R_{0}$ is the initial packet radius, $t_{i}$ is the time since the release of this particular packet, $D$ is a diffusivity that governs the packet growth, meant to account for molecular diffusivity and the effects of small eddies ,and $C_{0}$ sets the initial concentration amplitude. The total $odorx,y,t$ is then the sum over all packets that have been released up to time $t$. The packet center was computed the following way:

$$
x_{i}(t+Δt)=x_{i}(t)+UΔt+η_{1}
$$



$$
y_{i}(t+Δt)=y_{i}(t)+η_{2},
$$

where $U$ denotes the mean wind velocity, and $η_{1}$ and $η_{2}$ are Gaussian white noise perturbations with mean 0 and standard deviation $\sqrt{2κΔt}$ , representing the effects of turbulent dispersion with eddy diffusivity $κ$.

In general, parameters were chosen to be physically realistic and also give concentration time series and odor plumes that were qualitatively similar to those in the videos. To set $C_{0}$ , we defined the detection threshold to be 1 and enforced that an agent more than 1.6 standard deviations away from an initial packet would not be able to detect its presence. See the following table:

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Explanation</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>U</td>
      <td>Wind speed</td>
      <td>36−300mm/s</td>
    </tr>
    <tr>
      <td>D</td>
      <td>Packet growth diffusivity</td>
      <td>10−52mm2/s</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>Eddy diffusivity</td>
      <td>1000mm2/s</td>
    </tr>
    <tr>
      <td>λ</td>
      <td>Packet release rate</td>
      <td>5Hz</td>
    </tr>
    <tr>
      <td>R0</td>
      <td>Initial packet radius</td>
      <td>10mm</td>
    </tr>
    <tr>
      <td>C0</td>
      <td>Initial packet intensity</td>
      <td>3827.24(a.u.)</td>
    </tr>
    <tr>
      <td>K</td>
      <td>Odor detection threshold</td>
      <td>1(a.u.)</td>
    </tr>
  </tbody>
</table>

The order of magnitude for $D$ was set by the fact that attractive odorants for D. melanogaster tend to have molecular diffusivities of around $10mm^{2}/s$ , for example, ethyl acetate. The eddy diffusivity $κ$ was set in accordance with Drivas et al., 1996. The release rate and initial size were chosen to be similar to those in Farrell et al., 2002. The wind speed was chosen to be similar to those used experimentally in Demir et al., 2020 and (Álvarez-Salvado et al., 2018).

Additionally, to improve computational efficiency, packets were no longer tracked once their $x$ position was so large that even if all released packets were at that position, the sum of their contributions would still be less than the detection threshold.

10,000 agents were initialized with uniformly distributed initial position and angle, with $x$ between 50 mm and 400 mm, $y$ between –110 mm and 110 mm, and $0°§amp;lt;\theta§amp;lt;360°$, where $x$ and $y$ positions are defined relative to the source location, as in Figure 3. Plumes were simulated for enough time steps so that the expected $x$ position of a packet released at time 0 would be equal to the maximum initial $x$ for navigating agents, before navigating agents were introduced and simulated for 120 s. Once again, a trajectory’s success was defined by whether it got within 15 mm of the source location.

To define the antenna-sensing region, space was discretized into ‘pixels’ with 0.154 mm as the pixel width, matching the spatial resolution of the high-frequency plume. The concentration was then computed by averaging over the pixels in an elliptical region, with the region defined as in the previous section.

To set the level of noise added to the $I$ and $F$ filters, we first computed a characteristic $I$ value in the simulated high-intermittency plume, $I_{0}$ , by averaging $I$ values over a region $192mm<x<205mm$ and $0mm<y<9mm$ and then averaging over the length of the simulation. We did the same for $F$ values in the simulated high-frequency plume to obtain $F_{0}$ . The values we obtained were $I_{0}=0.388$ and $F_{0}=3.14$. We then used 5% of these values as the standard deviation for Gaussian white noise to be added to the output of the $I$ and $F$ filters, respectively, at each time step. We also used $I_{0}$ and $F_{0}$ as representative $I$ and $F$ values in order to assign a single relative filter weight with which to color each set of gains in Figure 4G.

### Investigating the role of filter timescales

To understand how performance depended on the filter timescales $\tau_{I}$ and $\tau_{F}$ , we varied the two timescales independently, and for each pair of timescales simulated 10,000 flies in the two simulated plumes explored thus far. No noise was added to the sensor outputs, and gains were set at the base gains. Given that the average response of the intermittency filter is independent of the filtering timescale, it is unsurprising that for the fixed $\tau_{F}$ performance does not change significantly for values of $\tau_{I}$ nearly two orders of magnitude apart and only starts to degrade once the timescale gets on the order of 10 s (Figure 4—figure supplement 2A and B). This degradation is also expected: at very long timescales, it requires significant time for the $I$ filter to reach an appreciable value, even in the case of constant odor. There was also no significant difference in performance in either plume between an $I$-only model with an infinitely fast ($\tau_{I}=0$) timescale (and thus flat response power spectrum) and an $I$-only model with a 2 s timescale. This is to be expected as even with an infinitely fast timescale such a model has an upwind bias if and only if the signal is present and thus is only responding to the intermittency of the signal. We also see that performance is impacted by varying $\tau_{F}$ (Figure 4—figure supplement 2A and B) but that this is largely equivalent to fixing $\tau_{F}$ but varying $g_{F}$ instead (Figure 4—figure supplement 2C), as predicted by Equation 29.

### ORN and PN circuit model

ORN firing rates were computed from Equations 7 and 8. Once odor activity $a$ was obtained, it was convolved with a normalized sum of two gamma distributions, $N⋅Γ_{1}-0.5⋅Γ_{2}$ , where the timescales for the two gamma distributions were 6 ms and 8 ms, respectively (Gorur-Shandilya et al., 2017), and the shape parameters 2 and 3, respectively, giving the shape seen in Figure 6A. This convolution was then multiplied by 300 Hz to get a firing rate. Since the model is only valid in regions where $K_{on}§amp;lt;odor§amp;lt;K_{off}$ , we set any odor less than $K_{on}$ to 0. In the simulated plumes, $K_{on}$ was set to 1 and $K_{off}$ was set to 400. $a_{0}$ was set to 0.15 in order to get a baseline firing rate of about 40 Hz in the presence of continuous odor. In order to ensure the activity would go to 0 once there was no signal, $ϵ$ was bounded below by $ϵ_{L}$ and $ϵ_{L}$ was set to be greater than the steady-state $ϵ$ when no signal is present, which is given by $ln⁡(\frac{1}{a_{0}}−1)≈1.73$. Thus, $ϵ_{L}$ was set to 2.5 and activity less than $\frac{1}{1+e^{ϵ_{L}}}$ was set to 0. $\beta$ was set to 0.8 /s, in accordance with Gorur-Shandilya et al., 2017.

Once the ORN firing activity was obtained, PN membrane voltages were obtained using Equations 9–11. All parameters in Equations 9–11 were taken from Nagel et al., 2015. Since the fastest timescales were around 5 ms, responses were calculated through Euler integration with a timescale of 0.5 ms.
