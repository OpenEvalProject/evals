# A mathematical model explains saturating axon guidance responses to molecular gradients

## Authors

- Huyen Nguyen<sup>1</sup> ([ORCID: 0000-0002-5775-7915](https://orcid.org/0000-0002-5775-7915))
- Peter Dayan<sup>3</sup> ([ORCID: 0000-0003-3476-1839](https://orcid.org/0000-0003-3476-1839))
- Zac Pujic<sup>1</sup>
- Justin Cooper-White<sup>4</sup>
- Geoffrey J Goodhill<sup>1</sup> ([ORCID: 0000-0001-9789-9355](https://orcid.org/0000-0001-9789-9355)) †

### Affiliations

1. Queensland Brain Institute The University of Queensland St. Lucia Australia
2. School of Mathematics and Physics The University of Queensland St. Lucia Australia
3. Gatsby Computational Neuroscience Unit University College London London United Kingdom
4. Australian Institute for Bioengineering and Nanotechnology The University of Queensland St. Lucia Australia

† Corresponding author

## Abstract

Correct wiring is crucial for the proper functioning of the nervous system. Molecular gradients provide critical signals to guide growth cones, which are the motile tips of developing axons, to their targets. However, in vitro, growth cones trace highly stochastic trajectories, and exactly how molecular gradients bias their movement is unclear. Here, we introduce a mathematical model based on persistence, bias, and noise to describe this behaviour, constrained directly by measurements of the detailed statistics of growth cone movements in both attractive and repulsive gradients in a microfluidic device. This model provides a mathematical explanation for why average axon turning angles in gradients in vitro saturate very rapidly with time at relatively small values. This work introduces the most accurate predictive model of growth cone trajectories to date, and deepens our understanding of axon guidance events both in vitro and in vivo.

## Introduction

For the brain to function correctly, it must be wired correctly. Indeed, many neurodevelopmental disorders are likely the result of wiring defects (Yaron and Zheng, 2007; Geschwind and Levitt, 2007; Lin et al., 2009; Stoeckli, 2012). Axon guidance, where axons grow and navigate to their targets, occurs primarily via the sensing of molecular cues in the environment. A critical mechanism by which such cues act is believed to be concentration gradients, causing axons to be attracted or repelled in particular directions (Mortimer et al., 2008; Lowery and Van Vactor, 2009). However, despite major advances in understanding which molecules are involved in this process (Tessier-Lavigne and Goodman, 1996; Dickson, 2002; Chilton, 2006; Kolodkin and Tessier-Lavigne, 2011), an accurate quantitative model describing how axon trajectories are influenced by such guidance cues is still lacking.

In vivo, axon trajectories may potentially be influenced by many cues. In vitro assays allow individual influences, such as that from the concentration gradient of a single guidance factor, to be isolated and quantified. A substantial mystery posed by in vitro axonal chemotaxis assays is the relatively weak turning produced, even over long periods of time. The naive prediction that axons would promptly turn until they become fully aligned with the gradient turns out not to be true. In an early study of chemotactic responses of chick sensory neurons to a gradient of nerve growth factor in a diffusion chamber, only 60% of nerve tips were preferentially directed toward the gradient direction after 46 hr of growth (Letourneau, 1978). The growth cone turning assay over 1–2 hr produces average turning angles typically ranging from 10 to 25°, with high variability (Song et al., 1997; Höpker et al., 1999; Xiang et al., 2002; Ming et al., 2002; Thompson et al., 2011). A similarly weak response is observed in the Dunn chamber (Kent et al., 2010; Dudanova et al., 2012; Ruiz de Almodovar et al., 2011; Dudanova et al., 2010; Yam et al., 2009). More recent studies using microfluidic technologies over timescales ranging from hours to days have also elicited average axon turning angles only up to 10–15° (Wang et al., 2008; Morel et al., 2012; Taylor et al., 2015; Sloan et al., 2015). Why average turning angles are so small, and what this means for axon guidance in vivo, are unclear.

One of the key properties of in vitro axon growth that might explain this mystery is that it is often very straight (Katz et al., 1984; Katz, 1985). Axons are under mechanical tension from the pull of the growth cone (Bray, 1973; Bray, 1979), and this tension stimulates the elongation of the axon by stretching (Bray, 1984; Zheng et al., 1991). Traction forces generated in the growth cone arise from the coupling of the continuous retrograde flow of actin to the substrate through adhesion receptors (Franze and Guck, 2010; Betz et al., 2011; Athamneh and Suter, 2015). For reasons which are not clear, axons tend not to bend and follow the highly random movements of their growth cones. Rather, they usually form a straight line between their tip and a location where they are firmly attached to the substrate (i.e. a focal adhesion (Kaverina et al., 2002)). We call such locations anchor points; they can be at the soma, at a branch point, or at some other seemingly sporadic location along the axon. Although it is not clear how this tension leads to elongation, the growth cone advances largely in the stretch direction along the axon, resulting in relatively straight paths.

To determine quantitatively what effect this might have on axonal trajectories requires mathematical modelling. Growth cone movements were first analyzed in detail in (Katz et al., 1984; Katz, 1985). Subsequently, various phenomenological models have been built that differ as to how they treat stochasticity, and mechanisms for directional preference, namely turning or growth rate modulation. One set attempted to fit the dynamics of growth cone movement to a random walk with drift (Buettner et al., 1994; Odde and Buettner, 1995; Maskery et al., 2004; Pearson et al., 2011). Li et al. simulated trajectories by assuming the turning angle of the growth cone is in proportion to the angle between the neurite and the resultant filopodial tension (Li et al., 1995). In (Borisyuk et al., 2008), the axon growth angle depends on the tendency to turn toward the gradient angle and noise. The noise term is small (2–5°), leading to straight paths that resemble axon growth in the tadpole spinal cord. Another set of models has concentrated on how asymmetric receptor binding across the growth cone might be used as the basis of a turning signal (Goodhill et al., 2004; Xu et al., 2005; Mortimer et al., 2010), but without considering the consequence for whole trajectories. A third group of models considers the possibility that the velocity of the growth cone is influenced by an attractive gradient from the target cells, and chemoattractants and chemorepellants released from other growth cones and itself (Hentschel and Ooyen, 1999; Krottje and van Ooyen, 2007). However, none of these models has been closely compared with the details of experimentally measured trajectories in gradients, and parameters such as variability in step sizes, the distribution of instantaneous turning angles, and straightness of real paths, have not been addressed. Thus, the question of whether there is a model that can adequately capture all these characteristics of real trajectories remains open. Without such a model, it is difficult to determine if trajectories observed in vivo are in fact consistent with gradient guidance.

Here, we present a new computational model for axonal trajectories based on the combined influence of anchor points, a tendency to turn toward the gradient direction, and random noise. We found experimentally that the gradient had no effect on the step sizes; thus, we only model the turning angles. Critically, the model predicts rapid near saturation of average turning angles with time. To test this model quantitatively, we then introduce a new microfluidics assay for studying axonal response to gradients, and using timelapse imaging characterize the behavior of axons over several hours of growth in both attractive and repulsive gradients. We find that our model fits the behavior observed very closely. We then investigate by simulation the effect of increasing the number of anchor points, and find that this increases the average fidelity of turning but at the cost of higher variability. Together, this work both explains why turning response to gradient saturates so rapidly and reveals the quantitative principles that are required to reproduce accurately in vitro axonal trajectories in response to chemotactic gradients. The model identifies straightness as a limiting factor on how much axons can turn and suggests that the frequency of anchor points plays a key role in the axonal turning response to a gradient.

## Results

### A mathematical model of growth cone trajectories

We modelled three basic influences on the direction of axon growth: a tendency to grow straight, the effect of a chemotactic gradient, if present, and random movement noise. In a fixed coordinate system with arbitrary zero angle direction, we define θ(t) as the bearing of the growth cone at time step t, ϕ(t) as the angle of the vector connecting the growth cone to its anchor point, and Ψ as the gradient direction (terminology is summarized in Table 1). We define ‘bearing change’ as Δθ($t$), the change in θ(t) at time step t, distinct from ‘turning angle’ ψturn, the total change in θ from the initial direction of growth over long periods of time. For simulations we identify each timestep as 5 min of real time. The model (Figure 1) is then

**Table 1.**
 Summary of model parameters (GC: growth cone).


<table>
  <tbody>
    <tr>
      <td>Symbol</td>
      <td>Meaning</td>
    </tr>
    <tr>
      <td>θ</td>
      <td>GC’s current bearing</td>
    </tr>
    <tr>
      <td>Φ</td>
      <td>GC’s overall angle</td>
    </tr>
    <tr>
      <td>Ψ</td>
      <td>Gradient direction</td>
    </tr>
    <tr>
      <td>Δθ</td>
      <td>Bearing change</td>
    </tr>
    <tr>
      <td>ψturn</td>
      <td>Turning angle after 80 min</td>
    </tr>
    <tr>
      <td>a</td>
      <td>Persistence strength</td>
    </tr>
    <tr>
      <td>b</td>
      <td>Bias strength</td>
    </tr>
    <tr>
      <td>ξ</td>
      <td>Noise in bearing change</td>
    </tr>
    <tr>
      <td>σ</td>
      <td>Standard deviation of ξ</td>
    </tr>
    <tr>
      <td>s</td>
      <td>Step size every 5 min</td>
    </tr>
    <tr>
      <td>L</td>
      <td>Distance from origin to GC</td>
    </tr>
    <tr>
      <td>S</td>
      <td>Straightness index</td>
    </tr>
    <tr>
      <td>r</td>
      <td>Anchoring rate</td>
    </tr>
  </tbody>
</table>

![Figure 1.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig1-v1.jpg)

**Figure 1.:** (A) The axon starts growing from the soma (black segment) at initiation angle ϕ(0). At each time point, the bearing is θ(t), and the bearing change between t and t + 1 is Δθ($t$). ϕ($t$) is the angle of the vector connecting the current position of the growth cone with the anchor point. Ψ is the fixed gradient direction. (B) The turning angle ψturn at time $t$ is the angle between the initial direction of growth, and the line joining the initial and current positions of the growth cone. (C) Simulation of the growth cone angle using Equation (1) in the noiseless case (ξ = 0) with the same $a$ = 1 and different values of b. The dashed line is the power law $ϕ(t)∝t^{\frac{-b}{a+b}}$. In the long time limit, this law accurately describes the angle of the growth cone. (D) Simulations of the trajectories for different combinations of $a$ and $b$ in the absence of noise. Larger $b$ leads to stronger turning. When $a$ = 0, the growth cone very rapidly aligns with the gradient. The persistence term ($t$ > 0) leads to incomplete turning.

$$
\Delta\theta(t)=a∠(ϕ(t),\theta(t))+b∠(Ψ,\theta(t))+ξ
$$

where $a$ scales persistence to move in the same direction as the overall direction of the axon, $b$ scales the bias due to the gradient, and ξ is random noise in the bearing changes. The symbol ∠($x, y$) denotes the signed angle between the unit vectors with angles $x$ and $y$, and constrains the resultant angle to be between −π and π. The step size is the distance moved after one time step and will later be estimated empirically.

We consider first the noiseless case (ξ = 0) in long- and finite-time regimes, and then consider the effects of noise. Figure 1C shows the results of setting ξ = 0, with a fixed step size of $s $= 3 μm, and simulating the model for long times with the same $a$ = 1 and different values of $b$ (0.1, 0.2 and 0.3). Turning angles rapidly saturate, which can be understood analytically (see 'Materials and methods'): in the $t→∞$ limit, the growth cone angle follows a power law with respect to time $ϕ(t)∝t^{(\alpha-1)}$ or $log (ϕ(t)) = const + (\alpha−1) log(t)$ (where $\alpha = a/(a+b)$) (Figure 1C). This relationship generally holds for $t>exp(4) ≈ 4$ h, meaning that for long times, the rate of change of angle decreases and this rate is determined by the power law exponent $b$/($a$ + $b$). Since comparison with empirical data (see later) shows that the biologically relevant regime is $b$ ≪ $a$, the exponent is generally small. Thus, while ultimately axons in the model do eventually align with the gradient, this process takes an exceedingly long time. This explains the slow and decreasing change in the turning angle over time in the noiseless case.

The finite $t$ regime of this equation is difficult to solve analytically, since $ϕ(t)$ depends on the entire history of growth cone movements. Simulations using different combinations of $a$ and $b$ are shown in Figure 1D. For the cases of $a\neq0$, after 150 time steps (12.5 hr of real time), the resultant turning angle was far from completely aligned with the gradient. Although the bias term bent the trajectory in the direction of the gradient, there was a straightening effect due to the persistence term, constantly pulling the growth cone toward the overall growth direction of the axon. As expected, the pull due to the gradient increased with larger b (Figure 1D). Thus, the persistence term prevented the axon from completely aligning with the gradient. Also apparent is that without noise, the trajectories were all very straight (with straightness index [see 'Materials and methods'] greater than 0.98). Thus, the microscopic constraint imposed by the persistence term leads to the macroscopic phenomenon of incomplete turning.

When we introduced Gaussian noise into the bearing changes (in radians) (ξ ~ N(0, σ), σ=π/4) with the same parameters and initial conditions as above for 1000 axons, the behavior was qualitatively similar: after an initial period of relatively rapid turning, turning angles tended to an almost steady state which was not aligned with the gradient even after a long time. However, the average final turning angle was even less than that of the noiseless case. This is because the noise created more random wandering of the growth cone, further reducing the directional effect of the gradient (Figure 2A–B). After 20–40 min, for b = 0.1, the turning angle distribution of the population was 7 ± 25° (mean ± std). Assuming a normal distribution of turning angles, this means that many of the axons were no longer roughly perpendicular to the gradient, and thus only continued to turn extremely slowly. Therefore, over time the influence of the gradient on the whole population of axons weakened. The persistence term also created a resistance against large turns due to the gradient. Increasing b/a increased the turning angle, but did not alter its rapid saturation with time (Figure 2C). Lastly, we examined the effect on the straightness by varying the standand deviation of the noise σ from 0 to π radians. As the steps became more noisy, the paths became less straight (Figure 2D).

![Figure 2.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig2-v1.jpg)

**Figure 2.:** (A) Long-term behavior of growth cones: Simulation of 9 axons with fixed growth rate and noise in bearing changes (ξ ∼ N(0, π/4) radians) starting at ϕ(0) = 90° subject to the gradient direction Ψ = 0 with persistence $a$ = 1 and bias $b$ = 0.1 (blue), $b$ = 0.2 (red) and $b$ = 0.3 (black) after 150 steps (12.5 hr of real time). (B) The trajectories with the same parameters without noise. (C) The turning angles over time (mean ± SEM) of 1000 axons for different values of $b$ (0.1,0.2, 0.3) and $a$ = 1. (D) Straightness (mean ± std) decreases as the noise variance increases.

In summary, the noiseless case generated very straight axons and growth cone angles that followed power laws with respect to time in the long time limit. Similarly, in the noisy case, the rate of change of the average turning angle was initially rapid and then slowed down even more rapidly with time. In both cases, the persistence term was a limiting factor on how much and how fast the axons could turn. Thus, this model captures, at least qualitatively, the behavior that axons turn only slightly in gradients, and even for long times do not generally become completely aligned with the gradient.

### Stable gradient generation for guidance assays

Having established the basic behaviour of the model, we then asked whether it could reproduce in detail real axon trajectory statistics. We therefore analyzed the trajectories of superior cervical ganglion neurons in a new microfluidics device (Figure 3A–C). This device generated linear gradients, by the mixing of high and low solutions of a chemotropic factor. The gradient was visualized using 40 kDa dextran-tetramethylrhodamine (Figure 3D), and gradients were stable for at least 20 hr (Figure 3E,F).

![Figure 3.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig3-v1.jpg)

**Figure 3.:** (A) The design of the chamber: the two solutions were pumped into the inlets and mix in the mixing channels before flowing into the growth chamber where the cells are plated. The mixing channels were of height 50 μm and width 50 μm. Scale bar 1 mm. (B, C) Photo of the experimental setup: two glass syringes attached to a Harvard pump injected the solutions into the chamber bonded on a 35 mm plastic plate. (D) Two solutions, one of which contained 0.1% (v/v) dextran fluorescently labelled with tetramethylrhodamine, were used to visualize the gradient. Brighter regions indicate higher concentrations. Scale bar 200 μm. (E, F) Line-scan measurements of fluorescence intensity across the device show a linear gradient which persists for at least 20 hr ($t$ = 0h (E) and $t$ = 20h (F) ). The shaded errorbars show standard deviations across 10 chambers.

### SCG neurons were guided in the microfluidic assay

We measured the response to nerve growth factor (NGF) gradients of axons from dissociated P1-P3 SCG neurons. We chose this model system because almost 100% of these neurons express the NGF receptor TrkA (Wetmore and Olson, 1995; Verge et al., 1992).

Three conditions were investigated: a control without flow or gradient, an attractive gradient of nerve growth factor (NGF), and a gradient of NGF with added KT5720, which converts attraction to repulsion by lowering levels of cAMP in the growth cone (Song et al., 1997). Cells were injected into the growing chambers and grown for 2 hr before gradient onset. In the control condition, cells were grown over several hours with 0.3 nM NGF. In the NGF gradient condition, two solutions of concentrations 0 nM and 10 nM NGF were pumped into the growing chamber through the two inlets. Previous work using Scatchard analysis estimated that Kd = 0.9 ± 0.3 nM (Wehrman et al., 2007) and showed that SCG neuronal outgrowth is severely inhibited at the saturating NGF concentration of 40 nM (Ohta et al., 1990). Given the healthy growth in our assay, it is clear that the concentration in the gradient condition was below saturation point. We analyzed trajectories for 300 axons per condition. These were obtained from 23 individual chambers in the control case, 27 chambers in the NGF gradient case, and 24 chambers in the NGF gradient plus KT5720 case. In most experiments, 2 chambers were run in parallel, so the total numbers of experiments in each case were 12, 15, and 13, respectively. For the measurement of turning angles, we selected only axons that started growing between 70° and 110° relative to the gradient (when present). An asymmetric concentration field of guidance cue across the growth cone leads to turning (Song et al., 1997; Hentschel and Ooyen, 1999; Xiang et al., 2002; Ming et al., 2002) and axons growing in this range experienced between 94% (i.e. sin 70°) to 100% (i.e. sin 90°) of the maximum possible concentration difference across the growth cone. Thus, we expected the impact of the gradient would be strongest on these axons (Figure 4A). We tracked the growth cones every 5 min for as long as possible until they collapsed or branched or collided with other cells, axons or the edges of the chamber. The SCG axons were clearly attracted in the NGF gradient (Figure 4B). When the protein kinase A inhibitor KT5720 was added to the high and low solutions at concentration 70 nM, attraction was converted into repulsion as previously described (Song et al., 1997; Forbes et al., 2012) (Figure 4B). These results confirm that the gradient in the microfluidic assay elicited a guidance response in SCG axons. From the timelapse imaging data, we then selected the subset of axons that did not branch or retract following growth for several hours in the attractive NGF gradient, and measured the turning angles of the population over time. The average turning angle reached the steady state quickly and did not increase significantly with time, matching the prediction of the model (Figure 4C).

![Figure 4.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig4-v1.jpg)

**Figure 4.:** (A) Images of a representative axon initially almost perpendicular to the gradient at the beginning and end of the measurement after 80 min. Scale bar 20 μm. The red dots are the positions of the growth cone. (B) Summary of turning angles in the three conditions (mean ± SEM): control 0.2 ± 2.1° (n=120), NGF gradient (0–10 nM) 9.3 ± 1.9° (n=143), NGF gradient (0–10 nM) + KT5720−8.8 ± 2.2° (n=112). *: p < 0.01 t-test in both cases. (C) The means (red) and standard deviations (blue) of turning angles of 143 axons over time for the attractive case.

### The gradient did not affect axon branching

One possible way that the gradient could affect the axons is by causing biased branching [c.f. (Simpson et al., 2013)], or changes in branching rates. To test whether the NGF gradient changed the branch extension and retraction rates, we compared the number of branches per cell after 5 hr of growth and did not detect any difference (p = 0.9 Kolmogorov–Smirnov test, Figure 5A). We measured the intervals between successive branching events in the same cell in each condition and did not find any difference in the branching rate (p = 0.7 Kolmogorov–Smirnov test, Figure 5B). Similarly, the lifetimes of the branches were unaffected by the gradient (p = 0.2 Kolmogorov–Smirnov test, Figure 5C). We counted the number of branches pointing up and down the gradient per cell and did not find any difference (p = 0.8 Kolmogorov–Smirnov test, Figure 5D). Thus, the gradient had no effect on axon branching and retraction.

![Figure 5.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig5-v1.jpg)

**Figure 5.:** (A) Histogram of the number of cells with different numbers of branches after 5 hr of growth. The number (mean ± std) of branches per neuron in the control condition was 4.2 ± 1.8 (n=324 cells) and in the gradient condition was 4.4 ± 1.9 (n=297 cells), p = 0.9 Kolmogorov–Smirnov test. (B) The distribution of interval times between two successive branching events of the same cell. The interval (mean ± std) in the control condition was 23.1 ± 22.8 min (n=315 intervals) and in the gradient condition was 24.1 ± 23.5 min (n=287 intervals), p = 0.7 KS test. (C) Branch lifetime (mean ± std) in the control condition was 87 ± 79 min (n=245 branches) and in the gradient condition was 92 ± 81 min (n=213 branches), p = 0.2 KS test. (D) Histogram of the number of branches pointing up the gradient vs down the gradient (p = 0.8, KS test).

### Flow did not affect the statistics of steps

To test whether fluid flow in the chamber biased the statistics of the steps, axons growing in the gradient condition with fluid flow were divided into four quadrants with different relative angles to the fluid flow: two quadrants growing perpendicular to the flow, one quadrant growing with the flow, and the other growing against the flow (Figure 6A). Comparing the distribution of bearing changes between the four quandrants, and with axons from the control condition without any flow, showed no influence of the flow (p = 0.7 in Figure 6B and p = 0.4 in Figure 6C, Kruskal-Wallis test). The means of the bearing changes in quadrants 2 and 4 were non-zero, and the bearing changes accumulated over time to result in a non-zero average turning angle of the population. However, these differences in means were very small (approximately 1°), and there were no significant statistical difference among the distributions. Therefore, the positive turning angles in the NGF gradient (and negative turning angles in the NGF gradient + KT5720) were due to the effect of the gradient, not bias from the flow.

![Figure 6.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig6-v1.jpg)

**Figure 6.:** (A) Axons growing in different directions were grouped into four quadrants. (B) Growth cones’ step sizes in different quadrants. n values refer to the number of steps in each quadrant. There was no significant difference between the quadrants (p = 0.7 Kruskal-Wallis test). (C) Grow cones’ bearing changes in different quadrants (p = 0.4 Kruskal-Wallis test).

### Growth cone trajectories were generally straight

Axon growth is shown in Videos 1–3 and Figure 7A–C. The growth cone often wandered quite randomly, but nevertheless usually the axon segment remained very straight from the growth cone to the cell body or last axon branch point (Figure 7A–C). This implies that often the entire axon segment was pulled sideways across the substrate (as can be seen directly in the movies). Thus, despite the irregular trajectory of the centre of the growth cone, the tension force on the growth cone from the axon was usually pointing directly back to the last anchor point, consistent with the assumptions of the model. To quantify this further, we measured the angle of this 20 μm segment and the angle to the anchor point ϕ and found them to be almost the same (Figure 7D,E). Thus, we can understand the term ϕ as the tension due to the most distal segment.

![Figure 7.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig7-v1.jpg)

**Figure 7.:** (A–C) Timelapse images of three example growth cones. Red arrows point to the putative anchor points and green arrows point to the growth cones. Time is shown in hours and minutes. (D) We measured the angle of the neck of the growth cone (the last 20 μm, black line) and the overall growth cone angle (blue line) after 1 hr from the start of the experiment. (E) The two angles were highly correlated, due to the straightness of the axon.

![Video 1.](https://cdn.elifesciences.org/articles/12248/elife-12248-media1.mp4.jpg)

**Video 1.:** One-minute interval phase contrast timelapse imaging of a growth cone in a microfluidic chamber.

![Video 2.](https://cdn.elifesciences.org/articles/12248/elife-12248-media2.mp4.jpg)

**Video 2.:** One-minute interval phase contrast timelapse imaging of a growth cone in a microfluidic chamber.

![Video 3.](https://cdn.elifesciences.org/articles/12248/elife-12248-media3.mp4.jpg)

**Video 3.:** One-minute interval phase contrast timelapse imaging of a growth cone in a microfluidic chamber.

The trajectories (i.e. the locus of the centre of the growth cone) in three conditions are plotted in Figures 8–10. Note that these paths are not the same as the final image of the axon, which generally pointed straight back from the final position of the growth cone to the anchor point. Visually, the paths appear mostly straight with occasional large turns, consistent with a long tail for the bearing change distribution. The mean straightness index for the trajectories was S = 0.72 (Figure 11A).

![Figure 8.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig8-v1.jpg)

**Figure 8.:** The red segments indicate the initial direction of the axon and the blue segments show the traces of the growth cones’ trajectories. Scale bar = 100 μm.

![Figure 9.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig9-v1.jpg)

**Figure 9.:** Only axons in the box were selected for turning angle measurements as they were almost perpendicular to the gradient, hence most affected by it. Scale bar = 100 μm.

![Figure 10.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig10-v1.jpg)

**Figure 10.:** Only axons in the box were selected for turning angle measurements. Scale bar = 100 μm.

![Figure 11.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig11-v1.jpg)

**Figure 11.:** (A) Distribution of straightness indices of all paths with mean straightness of 0.72. (B) There was no correlation between bearing change and step size (R2 = 0.1, p = 0.7). (C) The distribution of bearing changes (blue) in radians in the control condition can be fitted to a mixture of two von Mises distributions (red) $P(x)=0.5\frac{exp(3cos(x))}{2\pi I_{0}(3)}+0.03$. (D) Step sizes in the control, attractive and repulsive gradients conditions were similar and well-fitted by the gamma distribution P(x) ∝ x2 exp(−x/24) (red). (E) Step sizes of individual growth cones (blue) can be described by gamma distributions (red) (9 examples shown). (F) This distribution of the average step sizes (blue) of individual growth cones was well-fitted by a Gaussian distribution N(0.7, 0.24) (red). (G) Mean square displacement and standard deviation of 300 growth cones growing over 100 mins in the control condition was super-linear, indicating that growth cone trajectories were straighter than predicted by a simple random walk. (H) Autocorrelation of bearing changes (mean ± std) showed that successive bearing changes were anti-correlated.

### Step size and bearing change distributions were similar across conditions

There was little correlation between the bearing change magnitude and step size (Figure 11B). The distribution of bearing changes in radians was well fitted by a mixture of a von Mises and a uniform distribution (−π < x < π) (Figure 11C). That is there was a great deal of randomness in bearing changes, but with a peak in probability near the forward direction. Thus, growth cones tended to move in a straight line instead of turning uniformly randomly. This is inconsistent with the assumptions of several previous models (Buettner et al., 1994; Odde and Buettner, 1995; Maskery et al., 2004).

Accumulating across all the growth cones, the distributions of step sizes over 5 min were statistically indistinguishable across the three conditions (Kruskal-Wallis test p = 0.35), and were well fitted by a gamma distribution (Figure 11D). That is, the most likely step size was around 0.5 μm/min, but the distribution had a long tail, so that longer step sizes were also seen. The distribution of step sizes for each individual growth cone were also well fit by gamma distributions (Figure 11E). However, individual growth cones had idiosyncratic mean values. The distribution of these mean values could be well fitted by a Gaussian distribution (Figure 11F).

Nevertheless, the mean square displacement was clearly not linear, implying that a simple random walk is not suitable to describe the movement (Figure 11G). Successive steps were anti-correlated (Figure 11H), which was not accounted for in a previous model (Pearson et al., 2011). This helps the paths remain relatively straight: if successive steps were positively correlated, the paths would become more bent over time. Due to large noise in the bearing changes, bearing changes more than one step apart were uncorrelated.

### Turning angles over time were well predicted by the model

Having established the key statistics of steps from the data, we now asked if the simple model in Equation (1) could replicate the observed trajectories and explain the phenomenon of saturated turning. We sampled the mean speed $v_{mean}$ of each growth cone from a truncated Gaussian distribution of mean 0.7 μm/min and standard deviation 0.24 μm/min. At each time point (5-min interval), the growth cone sampled a step size from the gamma distribution $Γ(4∕u,v_{mean}*u∕4)$ where u was a uniform random number. The bearing changes evolved according to Equation (1). We found that the random noise ξ in bearing changes (in radians) could be well fit by the mixture von Mises distribution

$$
P(ξ) = c\frac{exp(d cos(ξ))}{2\pi I_{0}(d)} + (1-c)
$$

where $c$ and $d$ are parameters to be fit. This distribution is not necessarily the same as that of the bearing changes in Figure 11F. As the bearing change is the sum of three random terms, its distribution is broader than the distribution of the noise term. To estimate the four free parameters $a,b,c,d$, we input the initiation angles $ϕ(0)$ and used the model to generate the distribution of turning angles $ψ_{turn}$. We then estimated the likelihood function that the turning angle data was generated from the model with the given parameters $L(ψ_{turn}|a,b,c,d,ϕ(0))$ .

We found the values of a,b,c,d that maximized the likelihood (the parameters mostly likely to have generated our empirical turning angle data) were a = 0.7, b = 0.09, c = 0.75, d = 6. The statistics over 5000 simulated trajectories using these parameters are shown in Figure 12, and some example trajectories are shown in Figure 13. Similarly, we fitted the model to the control data and repulsive gradient and found a = 0.002 and b=−0.08, respectively, with other parameters remaining at very similar values as before. Notably, the simulated turning angles changed little over time (Figure 12A), consistent with our preliminary prediction and the data (Figures 1E, 4C). Thus, with realistic step sizes and bearing change noise distributions, the model was able to capture the phenomenon of saturated turning with quantitatively accurate means and variances over time. The distribution of turning angles and step sizes also closely matched the real data (Figure 12B,C). The simulated straightness distribution was also very smilar to the real distribution (p = 0.2, t-test) (Figure 12D). The model also captured the distribution of bearing changes, the mean square displacement and the anticorrelation between successive bearing change, which was a consequence of the persistence term straightening the paths (Figure 12D–F). If successive steps were positively correlated, the paths would become more bent over time. This correlation was rapidly lost beyond one time lag because of the large noise.

![Figure 12.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig12-v1.jpg)

**Figure 12.:** (A) The evolution of simulated turning angles (mean ± std) of n=5000 growth cones over time in the attractive gradient condition. (B) Simulated turning angles after 16 steps (80 min) had mean 9.8° and standard deviation of 24.2°, similar to the empirical data in red in Figure 4B. (C) Distribution of simulated step lengths (blue), fitted with the empirical distribution (red). (D) Straightness of simulated trajectories (mean 0.75, blue), compared with empirical distribution (red) (p = 0.2, t-test). (E) Simulated bearing changes (blue) fitted with the mixture of von Mises distributions given in Figure 11D (red). (F) Mean square displacement of simulations (blue) and data (red). (G) Autocorrelation of simulated bearing changes.

![Figure 13.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig13-v1.jpg)

**Figure 13.:** (A) control, (B) NGF gradient, (C) NGF gradient + KT5720.

Unlike previous models, we did not assume constant steps or a uniform distribution of bearing changes but rather derived these from empirical data. The model was then able to predict the evolution of the average turning angle over time, the straightness profile and the anticorrelation in bearing changes. Most importantly, it could explain the phenomenon of slow and saturated turning, due to a weak bias term relative to the persistence term. A microscopic factor in each step led to a macroscopic phenomenon of limited, variable turning and straight paths. This often overlooked feature of axon growth turned out to be critical in our model in limiting the overall turning. We also found little difference between the attractive and repulsive case, indicating that attractive and repulsive gradients employed similar mechanisms and could not reduce the variability of axon trajectories.

### Multiple anchor points achieved sharp turns but also increased variability

The in vitro data we have presented here was well-fitted by assuming the only anchor point is where the axon emerges from the soma or the branch point. However, the in vivo environment is much more complex, and axons may establish anchor points with the substrate at multiple positions as they extend. We therefore investigated in the model what effect this would have on turning angles. We assumed that at each timestep, the probability of that point becoming a new anchor point was fixed, while leaving the evolution at each step as before. The average number of anchor points per timestep (i.e. 5 min) is denoted by r. We analyzed two cases: anchoring probabilistically at each time step (Figure 14A–C), and anchoring at regular intervals (Figure 14D–F). We simulated the trajectories for T = 150 timesteps with the same parameters as Figure 2A (a = 1, b = 0.1, ξ = 0 or ξ ∼ N (0, π/4) radians). In both cases, more anchor points led to sharp turns in the trajectories and larger mean turning angle (Figure 14G), since the growth cone now was more free from its initial position. However, it increased the variability in the turning (Figure 14G). Given the same rate of anchoring, whether the growth cone put down new anchor points probabilistically or regularly made little difference to the mean turning. We compared the mean square final angle ⟨ϕ(T)2⟩ which is the sum of the bias ⟨ϕ(T)⟩2 and the variance (ϕ(T)). Ideally, the growth cone should completely align with the gradient, that is ϕ(T)=0. Figure 14H shows the bias/variance trade off. Although more anchor points introduced larger variance in the final angle, they achieved greater turning, that is smaller ϕ(T). Figure 14I shows that in the case without movement noise (ξ = 0) and regular anchoring, the growth cone angle ϕ(t) also followed a power law in the large t limit, similarly to the case without anchoring (Figure 1C). However, the exponent of this power law was larger, demonstrated by a steeper slope between log(t) and log(ϕ(t)), meaning that the growth cone aligned with the gradient faster with more anchor points. Thus, increasing the rate of anchoring leads to stronger turning, but increases the variance of the responses.

![Figure 14.](https://cdn.elifesciences.org/articles/12248/elife-12248-fig14-v1.jpg)

**Figure 14.:** (A–C) Trajectories of growth cones with probability of putting down a new anchor r= 0.01, 0.05, 0.1 at each timestep and the same parameters as Figure 2A (a = 1, b = 0.1, T = 150 timesteps). The black plots are without noise in the bearing changes, the blue plots are with noise $ξ~N(0,\pi/4)$ radians in the bearing changes and the red dots are the anchor points. More anchor points lead to higher variability but also stronger turning. The means and standard deviations of turning angles and the values for the noiseless versus the noisy case in brackets for r = 0.01, 0.05, 0.1 are 32 ± 9° (30 ± 36°), 55 ± 8° (49 ± 57°) and 67 ± 5° (60 ± 56°), respectively. (D–F) Trajectories of growth cones with the same rate of putting down new anchor points as A-C but at regular intervals. The means and standard deviations of turning angles and the values for the noiseless versus the noisy case in brackets are 27° (24 ± 17°), 57° (54 ± 51°), 69° (66 ± 51°). (G) The means and standard deviations of turning angles after 150 timesteps as a function of the anchoring rate at regular intervals in the noiseless and the noisy case. (H) The mean square of the final growth cone angle (in degrees) $⟨ϕ(T)^{2}⟩$ for different anchoring rates r after 150 steps. $⟨ϕ(T)^{2}⟩$ is the sum of the bias term $⟨ϕ(T)⟩^{2}$ and the variance term var($ϕ(T)$). Although more anchor points add more variance to the final angle (red curve), they achieve stronger turning $ϕ(T)≈0$ (black curve). (I) The evolution of $ϕ(t)$ over time, for the case of anchoring at regular intervals and no noise in the movement (ξ = 0). With more anchor points, $ϕ(t)$ also follows the power law but with steeper slope, meaning that $ϕ(t)→0$ at a faster rate than the case without anchor points.

## Discussion

Here, we presented a model of axon trajectories in gradients and helped resolve the mystery of why axon turning angles in gradients saturate over time in vitro, revealing an important factor limiting axon turning. We found that the movement of the growth cone was strongly influenced by the axon’s tendency to maintain a straight trajectory forward, limiting the directional effect of the gradient and preventing the axon from aligning with the gradient even after a long time. Our model predicted that, averaged over a large population of axons, the initial rate of turning drops rapidly over a short period of time (20–40 min). The model shows that adding more anchor points can give the growth cone more flexibility and produce larger average turning, but also increases the variability. Thus, we predict that different substrates, producing different densities of anchor points, could result in different trajectories for the same the gradient conditions.

The application of forces to axons can induce rapid elongation without axonal thinning, and thus stretch can stimulate growth (Suter and Miller, 2011). Furthermore, stretch can also regulate the mode of growth. When axons are tightly bound to a sticky substrate, stretching only happens at the tip and axons elongate by tip growth. In contrast, if axons grow relatively unattached to the substrate, they will lengthen by stretching due to the pull of the growth cone (Chang et al., 1998; O'Toole et al., 2008), which appears to be the case in our experimental condition. The tension along the axon will cause stimulation of growth in the existing direction producing straighter trajectories. The stiffness of axons is also important (Rajagopalan et al., 2010), and stiffer axons will likely have higher persistence due to their more limited ability to bend.

This tension results from cytoskeletal coupling with adhesive interactions to the substrate and is critical to growth cone migration (Heidemann et al., 1997; Spire, 2009). Although anchor points are an abstraction in our model, their biological implementation may be focal adhesions. Only at these points is the axon firmly attached to the substrate. There is a number of ways in which anchor points could be investigated experimentally in future work. Axons could be stained for proteins such as integrins (Kaverina et al., 2002) to test whether their distribution is strongly localized to particular points along the axon. We also predict that applying force orthogonal to the direction of axon growth, for instance by using a pipette to puff liquid at different locations along the axon, would cause a deflection of the axon of a size related to the distance from the nearest anchor point. A similar experiment was performed using a glass needle to tow axons (O'Toole et al., 2008). It was observed that the distal region of the axon was free of the substrate, while the proximal region was firmly attached. In addition, it could be possible to determine the internal stress field of an axon, as has been done for growth cones (Betz et al., 2011): we would expect the stress to in general be different on the two sides of an anchor point. The density of anchor points will depend on the components of the extracellular matrix (ECM). In our experiments, on laminin, they appeared to be rare. This might be because adhesion points are expensive to produce and the axon can grow faster when it is not attached to the substrate (Chang et al., 1998). However, the biological factors governing when new anchor points are generated are unknown.

Tension is also dependent on cell type and two main properties of the substrate: stiffness and ECM components. Our data comes from peripheral nervous system (PNS) neurons growing on a laminin substrate that is hard rather than gel-like, and other cell types of different substrates might have different behaviours. Central nervous system (CNS) and PNS neurons have different sensitivities to substrate stiffness due to adaptation to their natural environments (Koch et al., 2012), and traction force in vitro increased on stiffer substrates (Koch et al., 2012). Substrates with different ECM components differentially promote growth cone motility and point contact formation. For example, growth cones are more highly motile and neurites extend more rapidly on laminin than fibronectin because point contacts have higher turnover rate (Robles and Gomez, 2006).

Overall, our work suggests that without many anchor points, cues additional to gradients may be necessary for axons to reliably find their targets in vivo (unless the motility noise is for some reason much lower in vivo than in vitro). These could include mechanical cues and axon-axon interactions. To understand such interactions, it is important to generate assays with realistic substrates suitable for different cell types. Recent 3D culture models, in which cells are grown with a protein scaffold, can capture some aspects of the tissue environments instead of hard surfaces (Cullen et al., 2007). It will be interesting to see how different ECM properties lead to changes in trajectories and whether they can facilitate more reliable turning.

In conclusion, we have presented a simple mathematical model which gives accurate quantitative predictions of the properties of axonal trajectories in a microfluidics-based in vitro gradient assay. The model identifies the key importance of anchor points in controlling turning and provides an explanation for why axonal turning in gradients in vitro tend to saturate rapidly at small turning angles. This model provides a predictive framework which can be used to test whether axonal trajectories observed in vivo can be explained purely in terms of gradient guidance, or whether additional guidance mechanisms are also required.

## Materials and methods

### Microfluidics chamber fabrication

The device was designed in AutoCAD 2013 based on the pattern in (Dertinger et al., 2001). The microfluidic master molds were prepared by standard soft photolithography techniques. The silicon wafer (M.M.R.C. Pty Ltd) was coated with a 50 μm thick layer of SU-8 2100 relief (MicroChem, Westborough, MA) with a spincoater (EVG). The master was printed onto high-precision photoplates (Konica-Minolta) with a photoplotter (EVG). Before replica moulding, the silicon master was silanized with vapour phase silane, under vacuum for 1 hr at room temperature to prevent polydimethylsiloxane (PDMS) adhering to the master.

PDMS base elastomer (Sylgard 184, Dow Corning, Midland, MI) and silicon elastomer curing agent in a 10:1 (m/m) ratio were thoroughly mixed and poured on the master to a depth of about 4 mm. The mold with PDMS was degassed in a vacuum chamber for 2 hr and baked at 80°C for 2 hr. The PDMS replica was then peeled from the silicon wafer and cut into individual chambers. Holes were cored in the PDMS chambers using a 0.75 mm corer (Harris Uni-Core). To bond the PDMS chamber to a plastic tissue-culture petri dish, the dish and the chamber were plasma treated at 100W at a pressure of 380 mTorr for 40 s. The plate was then covered with (3-Aminopropyl)triethoxysilane (APTES, Sigma-Aldrich) solution (5% APTES in 70% ethanol). The plastic dish was washed thoroughly with water, air dried, and the chamber was pressed onto the dish. To avoid air bubbles forming, the dish was filled with distilled water and degassed in the vacuum chamber for 10 min before use.

### Primary superior cervical ganglion (SCG) cell culture

SCG neurons were harvested from postnatal day 1–3 Wistar rat pups. The SCGs were then cut into thirds, incubated in 0.25% trypsin (GIBCO) at 37°C for 30 min and then triturated through a flamed-polished Pasteur pipette for 5 min to dissociate individual cells. The growth solution was Opti-MEM solution (GIBCO) containing 1X penicillin/streptomycin, 10 μg/mL mouse laminin, 4% (v/v) fetal calf serum, 2% B-27 supplement (Life Technologies), and 0.3 nM NGF. The cells were suspended in the growth solution and injected in the microfluidic chamber using a 100-μL glass syringe (SGE Analytical Science).

### Gradient generation and measurement

Two syringes were filled with either the high (10 nM) or low (0 nM) NGF solution. The high solution contained 0.1% (v/v) 40 kDa-dextran fluorescently labelled with tetramethylrhodamine to visualize the gradient. After the cells were seeded, the syringes containing the high and low solutions were connected to the chamber using polyethylene tubings. The chamber was moved to an incubated inverted microscope (Zeiss AxioObserver). The syringes were attached to a Harvard PHD pump and the flow rate was set at 10 μL/hr. After the flow had been started, fluorescent images of the chamber were taken in Zen software. Background intensity outside the chamber was subtracted from the images. The average brightness intensity and variations over time were then calculated across the chamber. A gradient of fluorescence confirmed that the NGF gradient had formed in the growth chamber. To generate a repulsive gradient, KT5720 (Alexis Biochemicals), a specific inhibitor of protein kinase A (PKA), was added into both the high and low solutions at a concentration of 70 nM.

### Tracking growth cone trajectories

After the onset of the gradient, the axons were imaged every 5 min for 6 hr using Zeiss Zen software. After data acquisition, axons of 30 μm length, growing in all directions, that did not branch or retract in at least 80 min, were chosen for measurements. All axons were tracked manually using customized MATLAB software (The MathWorks) for as long as possible until they branched or retracted. A 5-min time interval was chosen because, for smaller intervals, variability in identifying the centre of the growth cone was larger than the net movement between frames. The point where the axon attaches to the cell body or the main branch was considered the anchor point.

### The straightness index

The straightness index S is the inverse of tortuosity, and compares the overall net displacement G of a path with the total path length T (Codling et al., 2008). Consider a walk that starts at location $(x_{0},y_{0})$, and after n steps of lengths lj (j = 1...n) finishes at $(x_{n},y_{n})$. The straightness index is given by:

$$
S = \frac{G}{T} = \frac{\sqrt{(x_{n} - x_{0})^{2}+ (y_{n} - y_{0})^{2}}}{\sum_{j=1 }^{n}l_{j}}
$$

This index is between 0 and 1, where 1 corresponds to movement in a straight line and 0 corresponds to a walk that returns to the origin. The closer this index is to 1, the straighter the trajectory is. Obviously, $S$ depends on the time interval used for tracing but can be used to compare conditions, which all have the same time interval.

### Modeling growth cone trajectories

All parameters of the model are summarized in Table 1. We consider a model which is a discretized random walk in which we separate the length and directions of the steps (Figure 1A). We discretized the axons at a timestep of 5 min, and, based on hypotheses we test later, only explicitly modelled the turning angles of the steps or ’bearing changes’. $Δ\theta(t)$, the ‘bearing change’ at time t depends on the current bearing of the growth cone $\theta(t)$, the angle $ϕ(t)$ of the vector connecting the growth cone to its anchor point, the gradient direction Ψ and the noise ξ according to Equation (1):

$$
Δ\theta(t)=a∠ (ϕ(t),\theta(t))+b∠ (Ψ,\theta(t))+ξ,
$$

where two parameters $a$ and $b$ scale the contributions of the first term representing persistence and the second term representing the bias due to the gradient. The symbol $∠(x,y)$ denotes the angle difference $x-y$ constrained to take values from −π to π. It is positive for an anticlockwise turn to get from $y$ to $x$. As the bearing is biased by the gradient direction, the overall growth cone angle $ϕ(t)$ will also be biased by the gradient, coupled through the above equation.

We first assume there is only one fixed anchor point where the axon initially grew out of the cell body or the main branch. We will later relax this assumption and allow the growth cone to put down new anchor points along its path. We denote the rate of anchor point deposition as r, which is the inverse of the average number of steps per new anchor point.

We first assume an initial direction of $ϕ(0)=\theta(0)=\pi∕2$, a gradient direction of Ψ = 0, and a fixed step size s every 5 min. In the idealized noiseless case (ξ = 0) as $t→∞$, the equation reaches a steady state when $Δ\theta=0$, that is:

$$
\Delta\theta(t)=a(ϕ(t)-\theta(t))+b(0-\theta(t)) = 0.
$$

This gives:

$$
\theta(t) = \frac{a}{a+b}ϕ(t)=\alphaϕ(t)
$$

with $\alpha=\frac{a}{a+b}$. Defining L to be the distance of the growth cone from its original position, and using the geometry in Figure 1A, we have:

$$
tan(ϕ(t+1))=\frac{L sin ϕ(t)+s sin(\alphaϕ(t))}{L cos ϕ(t)+s cos(\alphaϕ(t))}≈ tan(ϕ(t)) + \frac{s sin(\alphaϕ(t))}{L cosϕ(t)} - \frac{L sin ϕ(t)s cos(\alphaϕ(t)) }{L^{2}cos^{2}ϕ(t) }
$$

The approximation above is due to $s$ ≪ $L$ and ϕ(t) → Ψ = 0 as t → ∞. Using the Taylor expansion f(x0 + δx) ≈ f(x0) + δxf’(x0) and d tan−1(x)/dx = 1/(x2 + 1), we invert both sides of the above equation to obtain:

$$
ϕ(t+1)≈ tan^{-1}tan ϕ(t) + \frac{s sin(\alphaϕ(t))}{L cos ϕ(t)} - \frac{L sin ϕ(t)s cos(\alphaϕ(t))}{L^{2} cos^{2} ϕ(t)}                   ≈   ϕ(t) + \frac{s sin(\alphaϕ(t))}{L cosϕ(t)} - \frac{L sin ϕ(t)s cos(\alphaϕ(t)) }{L^{2} cos^{2} ϕ(t)}  cos^{2} ϕ(t)                  ≈ ϕ(t) + s/L (sin (\alphaϕ(t)) cos ϕ(t) - cos (\alphaϕ(t)) sin ϕ(t))                                           ≈ϕ(t) + s sin((\alpha-1) ϕ(t))/L
$$

At $t→∞$, $Δ\theta(t)→0$, meaning the growth direction aligns with the gradient, thus $ϕ(t) →0$ and $L≈st$ due to geometry (even for the $a$ = 0 case), so the above equation can be simplified as

$$
\frac{dϕ(t)}{dt}≈ \frac{(\alpha-1)ϕ(t)}{t}
$$

$$
\frac{dϕ(t)}{ϕ(t)}≈ \frac{(\alpha-1)dt}{t}
$$

$$
ln ϕ(t)=(\alpha-1) ln t+const
$$

Therefore, the long-term turning behaviour of axons in the model is given by the power law $ϕ(t)∝t^{(\alpha-1)}$.
