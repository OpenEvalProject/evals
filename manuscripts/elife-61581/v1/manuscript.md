# Binocular rivalry reveals an out-of-equilibrium neural dynamics suited for decision-making

## Authors

- Robin Cao<sup>1</sup>
- Alexander Pastukhov<sup>1</sup> ([ORCID: 0000-0002-8738-8591](https://orcid.org/0000-0002-8738-8591))
- Stepan Aleshin<sup>1</sup>
- Maurizio Mattia<sup>3</sup> ([ORCID: 0000-0002-2356-4509](https://orcid.org/0000-0002-2356-4509))
- Jochen Braun<sup>1</sup> ([ORCID: 0000-0002-8886-078X](https://orcid.org/0000-0002-8886-078X)) †

### Affiliations

1. Cognitive Biology, Center for Behavioral Brain Sciences Magdeburg Germany
2. Gatsby Computational Neuroscience Unit London United Kingdom
3. Istituto Superiore di Sanità Rome Italy

† Corresponding author

## Abstract

In ambiguous or conflicting sensory situations, perception is often ‘multistable’ in that it perpetually changes at irregular intervals, shifting abruptly between distinct alternatives. The interval statistics of these alternations exhibits quasi-universal characteristics, suggesting a general mechanism. Using binocular rivalry, we show that many aspects of this perceptual dynamics are reproduced by a hierarchical model operating out of equilibrium. The constitutive elements of this model idealize the metastability of cortical networks. Independent elements accumulate visual evidence at one level, while groups of coupled elements compete for dominance at another level. As soon as one group dominates perception, feedback inhibition suppresses supporting evidence. Previously unreported features in the serial dependencies of perceptual alternations compellingly corroborate this mechanism. Moreover, the proposed out-of-equilibrium dynamics satisfies normative constraints of continuous decision-making. Thus, multistable perception may reflect decision-making in a volatile world: integrating evidence over space and time, choosing categorically between hypotheses, while concurrently evaluating alternatives.

## Introduction

In deducing the likely physical causes of sensations, perception goes beyond the immediate sensory evidence and draws heavily on context and prior experience (von Helmholtz, 1867; Barlow et al., 1972; Gregory, 1980; Rock, 1983). Numerous illusions in visual, auditory, and tactile perception – all subjectively compelling, but objectively false – attest to this extrapolation beyond the evidence. In natural settings, perception explores alternative plausible causes of sensory evidence by active readjustment of sensors (‘active perception,’ Mirza et al., 2016; Yang et al., 2018; Parr and Friston, 2017a). In general, perception is thought to actively select plausible explanatory hypotheses, to predict the sensory evidence expected for each hypothesis from prior experience, and to compare the observed sensory evidence at multiple levels of scale or abstraction (‘analysis by synthesis,’ ‘predictive coding,’ ‘hierarchical Bayesian inference,’ Yuille and Kersten, 2006, Rao and Ballard, 1999, Parr and Friston, 2017b, Pezzulo et al., 2018). Active inference engages the entire hierarchy of cortical areas involved in sensory processing, including both feedforward and feedback projections (Bar, 2009; Larkum, 2013; Shipp, 2016; Funamizu et al., 2016; Parr et al., 2019).

The dynamics of active inference becomes experimentally observable when perceptual illusions are ‘multistable’ (Leopold and Logothetis, 1999). In numerous ambiguous or conflicting situations, phenomenal experience switches at irregular intervals between discrete alternatives, even though the sensory scene is stable (Necker, 2009; Wheatstone, 1838; Rubin, 1958; Attneave, 1971; Ramachandran and Anstis, 2016; Pressnitzer and Hupe, 2006; Schwartz et al., 2012). Multistable illusions are enormously diverse, involving visibility or audibility, perceptual grouping, visual depth or motion, and many kinds of sensory scenes, from schematic to naturalistic. Average switching rates differ greatly and range over at least two orders of magnitude (Cao et al., 2016), depending on sensory scene, perceptual grouping (Wertheimer, 1912; Koffka, 1935; Ternus, 1926), continuous or intermittent presentation (Leopold and Logothetis, 2002; Maier et al., 2003), attentional condition (Pastukhov and Braun, 2007), individual observer (Pastukhov et al., 2013c; Denham et al., 2018; Brascamp et al., 2019), and many other factors.

In spite of this diversity, the stochastic properties of multistable phenomena appear to be quasi-universal, suggesting that the underlying mechanisms may be general. Firstly, average dominance duration depends in a characteristic and counterintuitive manner on the strength of dominant and suppressed evidence (‘Levelt’s propositions I–IV,’ Levelt, 1965; Brascamp et al., 2006; Klink et al., 2016; Kang, 2009; Brascamp et al., 2015; Moreno-Bote et al., 2010). Secondly, the statistical distribution of dominance durations shows a stereotypical shape, resembling a gamma distribution with shape parameter $r≃3-4$ (‘scaling property,’ Cao et al., 2016; Fox and Herrmann, 1967; Blake et al., 1971; Borsellino et al., 1972; Walker, 1975; De Marco et al., 1977; Murata et al., 2003; Brascamp et al., 2005; Pastukhov and Braun, 2007; Denham et al., 2018; Darki and Rankin, 2021). Thirdly, the durations of successive dominance periods are correlated positively, over at least two or three periods (Fox and Herrmann, 1967; Walker, 1975; Van Ee, 2005; Denham et al., 2018).

Here, we show that these quasi-universal characteristics are comprehensively and quantitatively reproduced, indeed guaranteed, by an interacting hierarchy of birth-death processes operating out of equilibrium. While the proposed mechanism combines some of the key features of previous models, it far surpasses their explanatory power.

Several possible mechanisms have been proposed for perceptual dominance, the triggering of reversals, and the stochastic timing of reversals. That a single, coherent interpretation typically dominates phenomenal experience is thought to reflect competition (explicit or implicit) at the level of explanatory hypotheses (e.g., Dayan, 1998), sensory inputs (e.g., Lehky, 1988), or both (e.g., Wilson, 2003). That a dominant interpretation is occasionally supplanted by a distinct alternative has been attributed to fatigue processes (e.g., neural adaptation, synaptic depression, Laing and Chow, 2002), spontaneous fluctuations (‘noise,’ e.g., Wilson, 2007, Kim et al., 2006), stochastic sampling (e.g., Schrater and Sundareswara, 2006), or combinations of these (e.g., adaptation and noise, Shpiro et al., 2009; Seely and Chow, 2011; Pastukhov et al., 2013c). The characteristic stochasticity (gamma-like distribution) of dominance durations has been attributed to Poisson counting processes (e.g., birth-death processes, Taylor and Ladridge, 1974; Gigante et al., 2009; Cao et al., 2016) or stochastic accumulation of discrete samples (Murata et al., 2003; Schrater and Sundareswara, 2006; Sundareswara and Schrater, 2008; Weilnhammer et al., 2017).

‘Dynamical’ models combining competition, adaptation, and noise capture well the characteristic dependence of dominance durations on input strength (‘Levelt’s propositions’) (Laing and Chow, 2002; Wilson, 2007; Ashwin and Aureliu, 2010), especially when inputs are normalized (Moreno-Bote et al., 2007; Moreno-Bote et al., 2010; Cohen et al., 2019), and when the dynamics emphasize noise (Shpiro et al., 2009; Seely and Chow, 2011; Pastukhov et al., 2013c). However, such models do not preserve distribution shape over the full range of input strengths (Cao et al., 2016; Cohen et al., 2019). On the other hand, ‘sampling’ models based on discrete random processes preserve distribution shape (Taylor and Ladridge, 1974; Murata et al., 2003; Schrater and Sundareswara, 2006; Sundareswara and Schrater, 2008; Cao et al., 2016; Weilnhammer et al., 2017), but fail to reproduce the dependence on input strength. Neither type of model accounts for the sequential dependence of dominance durations (Laing and Chow, 2002).

Here, we reconcile ‘dynamical’ and ‘sampling’ approaches to multistable perception, extending an earlier effort (Gigante et al., 2009). Importantly, every part of the proposed mechanism appears to be justified normatively in that it may serve to optimize perceptual choices in a general behavioral situation, namely, continuous inference in uncertain and volatile environments (Bogacz, 2007; Veliz-Cuba et al., 2016). We propose that sensory inputs are represented by birth-death processes in order to accumulate sensory information over time and in a format suited for Bayesian inference (Ma et al., 2006; Pouget et al., 2013). Further, we suggest that explanatory hypotheses are evaluated competitively, with a hypothesis attaining dominance (over phenomenal experience) when its support exceeds the alternatives by a certain finite amount, consistent with optimal decision-making between multiple alternatives (Bogacz, 2007). Finally, we assume that a dominant hypothesis suppresses its supporting evidence, as required by ‘predictive coding’ implementations of hierarchical Bayesian inference (Pearl, 1988; Rao and Ballard, 1999; Hohwy et al., 2008). In contrast to many previous models, we do not require a local mechanisms of fatigue, adaptation, or decay.

Based on these assumptions, the proposed mechanism reproduces dependence on input strength, as well as distribution of dominance durations and positive sequential dependence. Additionally, it predicts novel and unsuspected dynamical features confirmed by experiment.

## Results

Below we introduce each component of the mechanism and its possible normative justification, before describing out-of-equilibrium dynamics resulting from the interaction of all components. Subsequently, we compare model predictions with multistable perception of human observers, specifically, the dominance statistics of binocular rivalry (BR) at various combinations of left- and right-eye contrasts (Figure 1a).

![Figure 1.](https://cdn.elifesciences.org/articles/61581/elife-61581-fig1-v1.jpg)

**Figure 1.:** (a) When the left and right eyes see incompatible images in the visual field, phenomenal appearance reverses at irregular intervals, sometimes being dominated by one image and sometimes by the other (gray and white regions). Sir Charles Wheatstone studied this multistable percept with a mirror stereoscope (not as shown!). (b) Spiking neural network implementation of a ‘local attractor.’ An assembly of 150 neurons (schematic, dark gray circle) interacts competitively with multiple other assemblies (light gray circles). Population activity of the assembly explores an effective energy landscape (right) with two distinct steady states (circles), separated by a ridge (diamond). Driven by noise, activity transitions occasionally between ‘on’ and ‘off’ states (bottom), with transition rates $ν^{\pm}$ depending sensitively on external input to the assembly (not shown). Here, $ν^{+}=ν^{−}≈1Hz$. Spike raster shows 10 representative neurons. (c) Nested attractor dynamics (central schematic) that quantitatively reproduces the dynamics of binocular rivalry (left and right columns). Independently bistable variables (‘local attractors,’ small circles) respond probabilistically to input, transitioning stochastically between on- and off-states (red/blue and white, respectively). The entire system comprises four pools, with 25 variables each, linked by excitatory and inhibitory projections. Phenomenal appearance is decided by competition between decision pools $R$ and $R^{′}$ forming ‘non-local attractors’ (cross-inhibition $w_{comp}$ and self-excitation $w_{coop}$). Visual input $c$ and $c^{′}$ accumulates, respectively, in evidence pools $E$ and $E^{′}$ and propagates to decision pools (feedforward selective excitation $w_{exc}$ and indiscriminate inhibition $w_{inh}$). Decision pools suppress associated evidence pools (feedback selective suppression $w_{supp}$). The time course of the number of active variables (active count) is shown for decision pools (top left and right) and evidence pools (bottom left and right), representing the left eye (red traces) and the right eye image (blue traces). The state of individual variables (black horizontal traces in left and middle columns) and of perceptual dominance (gray and white regions) is also shown. In decision pools, almost all variables become active (black trace) or inactive (no trace) simultaneously. In evidence pools, only a small fraction of variables is active at any given time. (d) Fractional activity dynamics of decision pools $R$ and $R^{′}$ (top, red and blue traces) and evidence pools $E$ and $E^{′}$ (bottom, red and blue traces). Reversals of phenomenal appearance are also indicated (gray and white regions).

### Hierarchical dynamics

#### Bistable assemblies: ‘local attractors’

As operative units of sensory representation, we postulate neuronal assemblies with bistable ‘attractor’ dynamics. Effectively, assembly activity moves in an energy landscape with two distinct quasi-stable states – dubbed ‘on’ and ‘off’ – separated by a ridge (Figure 1b). Driven by noise, assembly activity mostly remains near one quasi-stable state (‘on’ or ‘off’), but occasionally ‘escapes’ to the other state (Kramers, 1940; Hanggi et al., 1990; Deco and Hugues, 2012; Litwin-Kumar and Doiron, 2012; Huang and Doiron, 2017).

An important feature of ‘attractor’ dynamics is that the energy of quasi-stable states depends sensitively on external input. Net positive input destabilizes (i.e., raises the potential of) the ‘off’ state and stabilizes (i.e., lowers the potential of) the ‘on’ state. Transition rates $ν^{\pm}$ are even more sensitive to external input as they depend approximately exponentially on the height of the energy ridge (‘activation energy’).

Figure 1b illustrates ‘attractor’ dynamics for an assembly of 150 spiking neurons with activity levels of approximately $7Hz$ and $21Hz$ per neuron in the ‘off’ and ‘on’ states, respectively. Full details are provided in Appendix 1, section Metastable population dynamics, and Appendix 1—figure 2.

#### Binary stochastic variables

Our model is independent of neural details and relies exclusively on an idealized description of ‘attractor’ dynamics. Specifically, we reduce bistable assemblies to discretely stochastic, binary activity variables $x(t)\in{0,1}$, which activate and inactivate with Poisson rates $ν^{+}$ and $ν^{−}$, respectively. These rates $ν^{\pm}(s)$ vary exponentially and anti-symmetrically with increments or decrements of activation energy $Δu=u(s)+u^{0}$:

$$
ν^{+}=\frac{ν}{2}exp⁡(\frac{Δu}{2}),ν^{−}=\frac{ν}{2}exp⁡(−\frac{Δu}{2})
$$

where $u^{0}$ and $ν$ are baseline potential and baseline rate, respectively, and where the input-dependent part $u(s)=ws$ varies linearly with input $s$, with synaptic coupling constant $w$ (see Appendix 1, section Metastable population dynamics and Appendix 1—figure 2e).

#### Pool of N binary variables

An extended network, containing $N$ individually bistable assemblies with shared input $s$, reduces to a ‘pool’ of $N$ binary activity variables $x_{i}(t)\in{0,1}$ with identical rates $ν_{\pm}(s)$. Although all variables are independently stochastic, they are coupled through their shared input $s$. The number of active variables $n(t)=\sumix_{i}(t)$ or, equivalently, the active fraction $x⁢(t)$=$n(t)/N$, forms a discretely stochastic process (‘birth-death’ or ‘Ehrenfest’ process; Karlin and McGregor, 1965).

#### Relaxation dynamics

While activity $x(t)$ develops discretely and stochastically according to Equation 5 (Materials and methods), its expectation $⟨x(t)⟩$ develops continuously and deterministically,

$$
⟨x˙⟩=(1−⟨x⟩)ν^{+}−⟨x⟩ν^{−}
$$

relaxing with characteristic time $\tau_{x}=\frac{1}{ν^{+}+ν^{−}}$ towards asymptotic value $x_{∞}=\frac{ν^{+}}{ν^{+}+ν^{−}}$. As rates $ν^{\pm}$ change with input $s$ (Equation 1), we can define the functions $\tau_{s}=Υ(s)$ and $x_{∞}=Φ(s)$ (see Materials and methods). Characteristic time $\tau_{x}$ is longest for small input $s≃0$ and shortens for larger positive or negative input $|s|≫0$. The asymptotic value $x_{∞}$ ranges over the interval (0, 1) and varies sigmoidally with input $s$, reaching half-activation for $s=−u^{0}/w$.

### Quality of representation

Pools of bistable variables belong to a class of neural representations particularly suited for Bayesian integration of sensory information (Beck et al., 2008; Pouget et al., 2013). In general, summation of activity is equivalent to optimal integration of information, provided that response variability is Poisson-like, and response tuning differs only multiplicatively (Ma et al., 2006; Ma et al., 2008). Pools of bistable variables closely approximate these properties (see Appendix 1, section Quality of representation: Suitability for inference).

The representational accuracy of even a comparatively small number of bistable variables can be surprisingly high. For example, if normally distributed inputs drive the activity of initially inactive pools of bistable variables, pools as used in the present model ($N=25$, $w=2.5$) readily capture 90% of the Fisher information (see Appendix 1, section Quality of representation: Integration of noisy samples).

### Conflicting evidence

Any model of BR must represent the conflicting evidence from both eyes (e.g., different visual orientations), which supports alternative perceptual hypotheses (e.g., distinct grating patterns). We assume that conflicting evidence accumulates in two separate pools of $N=25$ bistable variables, $E$ and $E^{′}$, (‘evidence pools,’ Figure 1c). Fractional activations $e(t)$ and $e^{′}(t)$ develop stochastically following Equation 5 (Materials and methods). Transition rates $ν_{e}^{\pm}$ and $ν_{e^{′}}^{\pm}$ vary exponentially with activation energy (Equation 1), with baseline potential $u_{e}^{0}$ and baseline rate $ν_{e}$. The variable components of activation energy, $u_{e}$ and $u_{e^{′}}$, are synaptically modulated by image contrasts, $c$ and $c^{′}$:

$$
u_{e}=w_{vis}I,u_{e^{′}}=w_{vis}I^{′}
$$

where $w_{vis}$ is a coupling constant and $I=f(c)\in[0,1]$ is a monotonic function of image contrast $c$ (see Materials and methods).

### Competing hypotheses: ‘non-local attractors’

Once evidence for, and against, alternative perceptual hypotheses (e.g., distinct grating patterns) has been accumulated, reaching a decision requires a sensitive and reliable mechanism for identifying the best supported hypothesis and amplifying the result into a categorical read-out. Such a winner-take-all decision (Koch and Ullman, 1985) is readily accomplished by a dynamical version of biased competition (Deco and Rolls, 2005; Wang, 2002; Deco et al., 2007; Wang, 2008).

We assume that alternative perceptual hypotheses are represented by two further pools of $N=25$ bistable variables, $R$ and $R^{′}$, forming two ‘non-local attractors’ (‘decision pools,’ Figure 1c). Similar to previous models of decision-making and attentional selection (Deco and Rolls, 2005; Wang, 2002; Deco et al., 2007; Wang, 2008), we postulate recurrent excitation within pools, but recurrent inhibition between pools, to obtain a ‘winner-take-all’ dynamics. Importantly, we assume that ‘evidence pools’ project to ‘decision pools’ not only in the form of selective excitation (targeted at the corresponding decision pool), but also in the form of indiscriminate inhibition (targeting both decision pools), as suggested previously (Ditterich et al., 2003; Bogacz et al., 2006).

Specifically, fractional activations $r(t)$ and $r^{′}(t)$ develop stochastically according to Equation 5 (Materials and methods). Transition rates $ν_{s}^{\pm}$ and $ν_{s^{′}}^{\pm}$ vary exponentially with activation energy (Equation 1), with baseline difference $u_{r}^{0}$ and baseline rate $ν_{r}$. The variable components of activation energy, $u_{r}$ and $u_{r^{′}}$, are synaptically modulated by evidence and decision activities:

$$
u_{r}=w_{exc}e−w_{inh}(e+e^{′})+w_{coop}r−w_{comp}r^{′}u_{r^{′}}=w_{exc}e^{′}−w_{inh}(e+e^{′})+w_{coop}r^{′}−w_{comp}r
$$

where coupling constants $w_{exc}$, $w_{inh}$, $w_{coop}$, $w_{comp}$ reflect feedforward excitation, feedforward inhibition, lateral cooperation within decision pools, and lateral competition between decision pools, respectively.

This biased competition circuit expresses a categorical decision by either raising $r$ towards unity (and lowering $r^{′}$ towards zero) or vice versa. The choice is random when visual input is ambiguous, $I≃I^{′}$, but becomes deterministic with growing input bias $|I−I^{′}|§gt;0$ . This probabilistic sensitivity to input bias is reliable and robust under arbitrary initial conditions of $e$, $e^{′}$, $r$ and $r^{′}$ (see Appendix 1, section Categorical choice with Appendix 1—figure 3).

### Feedback suppression

Finally, we assume feedback suppression, with each decision pool selectively targeting the corresponding evidence pool. A functional motivation for this systematic bias against the currently dominant appearance is given momentarily. Its effects include curtailment of dominance durations and ensuring that reversals occur from time to time. Specifically, we modify Equation 3 to

$$
u_{e}=w_{vis}f(c)−w_{supp}ru_{e^{′}}=w_{vis}f(c^{′})−w_{supp}r^{′}
$$

where $w_{supp}$ is a coupling constant.

Previous models of BR (Dayan, 1998; Hohwy et al., 2008) have justified selective feedback suppression of the evidence supporting a winning hypothesis in terms of ‘predictive coding’ and ‘hierarchical Bayesian inference’ (Rao and Ballard, 1999; Lee and Mumford, 2003). An alternative normative justification is that, in volatile environments, where the sensory situation changes frequently (‘volatility prior’), optimal inference requires an exponentially growing bias against evidence for the most likely hypothesis (Veliz-Cuba et al., 2016). Note that feedback suppression applies selectively to evidence for a winning hypothesis and is thus materially different from visual adaptation (Wark et al., 2009), which applies indiscriminately to all evidence present.

### Reversal dynamics

A representative example of the joint dynamics of evidence and decision pools is illustrated in Figure 1c,d, both at the level of pool activities $e(t)$, $e^{′}(t)$, $r(t)$, $r^{′}(t)$, and at the level of individual bistable variables $x(t)$. The top row shows decision pools $R$ and $R^{′}$, with instantaneous active counts, $Nr(t)$ and $Nr^{′}(t)$ and active/inactive states of individual variables $x(t)$. The bottom row shows evidence pools $E$ and $E^{′}$, with instantaneous active counts, $Ne(t)$ and $Ne^{′}(t)$ and active/inactive states of individual variables $x(t)$. Only a small fraction of evidence variables is active at any one time.

Phenomenal appearance reverses when the differential activity $Δe=e−e^{′}$ of evidence pools, $E$ and $E^{′}$, contradicts sufficiently strongly the differential activity $Δr=r−r^{′}$ of decision pools, $R$ and $R^{′}$, such that the steady state of decision pools is destabilized (see further below and Figure 4). As soon as the reversal has been effected at the decision level, feedback suppression lifts from the newly non-dominant evidence and descends upon the newly dominant evidence. Due to this asymmetric suppression, the newly non-dominant evidence recovers, whereas the newly dominant evidence habituates. This opponent dynamics progresses, past the point of equality $s≃s^{′}$, until differential evidence activity $Δe$ once again contradicts differential decision activity $Δr$. Whereas the activity of decision pools varies in phase (or counterphase) with perceptual appearance, the activity of evidence pools changes in quarterphase (or negative quarterphase) with perceptual appearance (e.g., Figures 1c,d,2a), consistent with some previous models (Gigante et al., 2009; Albert et al., 2017; Weilnhammer et al., 2017).

![Figure 2.](https://cdn.elifesciences.org/articles/61581/elife-61581-fig2-v1.jpg)

**Figure 2.:** Exponential development of evidence activities is governed by input-dependent asymptotic values and characteristic times. (a) Fractional activities $e$ (blue traces) and $e^{′}$ (red traces) of evidence pools $E$ and $E$, respectively, over several dominance periods for unequal stimulus contrast ($c=\frac{7}{8},c^{′}=\frac{1}{8}$). Stochastic reversals of finite system ($N=25$ units per pool, left) and deterministic reversals of infinite system ($N$, right). Perceptual dominance (decision activity) is indicated along the upper margin (red or blue stripe). Dominance evidence habituates (dom), and non-dominant evidence recovers (sup), until evidence contradicts perception sufficiently (black vertical lines) to trigger a reversal (gray and white regions). (b) Development of stronger-input evidence $e$ (blue) and weaker-input evidence $e^{′}$ (red) over two successive dominance periods ($c=\frac{15}{16},c^{′}=\frac{1}{16}$). Activities recover, or habituate, exponentially until reversal threshold $Δ_{rev}$ is reached. Thin curves extrapolate to the respective asymptotic values, $e_{∞}$ and $e^{′}_{∞}$. Dominance durations depend on distance $Δ_{∞}$ and on characteristic times $\tau_{e}$ and $\tau_{e^{′}}$. Left: incrementing non-dominant evidence $e$ (dashed curve) raises upper asymptotic value $e_{∞}$ and shortens dominance $T^{′}$ by $ΔT^{′}$. Right: incrementing dominant evidence $e$ (dashed curve) raises lower asymptotic value $e_{∞}$ and shortens dominance $T$ by $ΔT$. (c) Increasing asymptotic activity difference $Δ_{∞}$ accelerates the development of differential activity and curtails dominance periods $T$, $T^{′}$ (and vice versa). As the dependence is hyperbolic, any change to $Δ_{∞}$ disproportionately affects longer dominance periods. If $T§gt;T^{′}$, then $ΔT§gt;ΔT^{′}$ (and vice versa).

#### Binocular rivalry

To compare predictions of the model described above to experimental observations, we measured spontaneous reversals of BR for different combinations of image contrast. BR is a particularly well-studied instance of multistable perception (Wheatstone, 1838; Diaz-Caneja, 1928; Levelt, 1965; Leopold and Logothetis, 1999; Brascamp et al., 2015). When conflicting images are presented to each eye (e.g., by means of a mirror stereoscope or of colored glasses, see Materials and methods), the phenomenal appearance reverses from time to time between the two images (Figure 1a). Importantly, the perceptual conflict involves also representations of coherent (binocular) patterns and is not restricted to eye-specific (monocular) representations (Logothetis et al., 1996; Kovács et al., 1996; Bonneh et al., 2001; Blake and Logothetis, 2002).

Specifically, our experimental observations established reversal sequences for $5\times5$ combinations of image contrast, $c_{dom},c_{sup}\in{\frac{1}{16},\frac{1}{8},\frac{1}{4},\frac{1}{2},1}$. During any given dominance period, $c_{dom}$ is the contrast of the phenomenally dominant image and $c_{sup}$ the contrast of the other, phenomenally suppressed image (see Materials and methods). We analyzed these observations in terms of mean dominance durations $⟨T⟩$, higher moments $c_{V}$ and $\gamma_{1}/c_{V}$ of the distribution of dominance durations, and sequential correlation $cc_{1}$ of successive dominance durations.

Additional aspects of serial dependence are discussed further below.

As described in Materials and methods, we fitted 11 model parameters to reproduce observations with more than 50 degrees of freedom: $5\times5$ mean dominance durations $⟨T⟩$, $5\times5$ coefficients of variation $c_{V}$, one value of skewness $\gamma_{1}/c_{V}=2$, and one correlation coefficient $cc_{1}=0.06$. The latter two values were obtained by averaging over $5\times5$ contrast combinations and rounding. Importantly, minimization of the fit error, by random sampling of parameter space with a stochastic gradient descent, resulted in a three-dimensional manifold of suboptimal solutions. This revealed a high degree of redundancy among the 11 model parameters (see Materials and methods). Accordingly, we estimate that the effective number of degrees of freedom needed to reproduce the desired out-of-equilibrium dynamics was between 3 and 4. Model predictions and experimental observations are juxtaposed in Figures 3 and 4.

![Figure 3.](https://cdn.elifesciences.org/articles/61581/elife-61581-fig3-v1.jpg)

**Figure 3.:** (a) Mean dominance duration $⟨T⟩$ (color scale), as a function of dominant contrast $c_{dom}$ and suppressed contrast $c_{sup}$, in model (left) and experiment (right). (b) Model prediction (solid traces) and experimental observation (dashed traces and symbols) compared. Levelt I and II: weak increase of $⟨T⟩$ with $c_{dom}$ when $c_{sup}=1$ (red traces and symbols), and strong decrease with $c_{sup}$ when $c_{dom}=1$ (brown traces and symbols). Levelt III: symmetric increase of $⟨T⟩$ with $c_{dom}$ (orange traces and symbols) and decrease with $c_{sup}$ (brown traces and symbols), when $c_{dom}+c_{dom}=1$. Alternation rate (green traces and symbols) peaks at equidominance and decreases symmetrically to either side. (c) Levelt IV: decrease of $⟨T⟩$ with image contrast, when $c_{sup}=c_{dom}$. (d) Predicted dependence of sequential correlation $cc_{1}$ (color scale) on $c_{dom}$ and $c_{sup}$. (e) Model prediction (black trace, $N=25$) and experimental observation (blue trace and symbols, mean ± SEM, Spearman’s rank correlation ρ), when $c_{sup}=c_{dom}$. Also shown is a second model prediction (red trace, $N=40$).

![Figure 4.](https://cdn.elifesciences.org/articles/61581/elife-61581-fig4-v1.jpg)

**Figure 4.:** Distribution shape is parametrized by coefficient of variation cv and relative skewness $\gamma_{1}/c_{V}$. (a) Coefficient of variation cv (color scale), as a function of dominant contrast $c_{dom}$ and suppressed contrast $c_{sup}$, in model (left) and experiment (right). (b) Model prediction (solid traces) and experimental observation (dashed traces and symbols) compared. Left: increase of cv with $c_{dom}$ (red traces and symbols), and symmetric decrease with $c_{sup}$ (brown traces and symbols), when $c_{sup}=1$. Right: weak dependence when $c_{dom}=c_{sup}$ (black traces and symbols). (c) Predicted dependence of relative skewness $\gamma_{1}/c_{V}$ (gray scale) on $c_{dom}$ and $c_{sup}$. (d) Model prediction (solid traces), when $c_{dom}=c_{sup}$ (black) and $c_{dom}=1−c_{sup}$ (orange and brown) and experimental observation when $c_{dom}=c_{sup}$ (blue dashed trace and symbols, mean ± SEM).

The complex and asymmetric dependence of mean dominance durations on image contrast — aptly summarized by Levelt’s ‘propositions’ I to IV (Levelt, 1965; Brascamp et al., 2015) — is fully reproduced by the model (Figure 3). Here, we use the updated definition of Brascamp et al., 2015: increasing the contrast of one image increases the fraction of time during which this image dominates appearance (‘predominance,’ Levelt I). Counterintuitively, this is due more to shortening dominance of the unchanged image than to lengthening dominance of the changed image (Levelt II, Figure 3b, left panel). Mean dominance durations grow (and alternation rates decline) symmetrically around equal predominance as contrast difference $c_{dom}−c_{sup}$ increases (Levelt III, Figure 3b, right panel). Mean dominance durations shorten when both image contrasts $c_{dom}=c_{sup}$ increase (Levelt IV, Figure 3c).

Successive dominance durations are typically correlated positively (Fox and Herrmann, 1967; Walker, 1975; Pastukhov et al., 2013c). Averaging over all contrast combinations, observed and fitted correlation coefficients were comparable with $cc_{1}=0.06\pm0.06$ (mean and standard deviation). Unexpectedly, both observed and fitted correlations coefficients increased systematically with image contrast ($ρ=0.9$, $p§lt;.01$), growing from $c⁢c_{1}=0.02\pm0.05$ at $c_{dom}=c_{sup}=\frac{1}{16}$ to $0.21\pm0.06$ at $c_{dom}=c_{dom}=1$ (Figure 3e, blue symbols). It is important to that this dependence was not fitted. Rather, this previously unreported dependence constitutes a model prediction that is confirmed by observation.

The distribution of dominance durations typically takes a characteristic shape (Cao et al., 2016; Fox and Herrmann, 1967; Blake et al., 1971; Borsellino et al., 1972; Walker, 1975; De Marco et al., 1977; Murata et al., 2003; Brascamp et al., 2005; Pastukhov and Braun, 2007; Denham et al., 2018), approximating a gamma distribution with shape parameter $r≃3−4$, or coefficient of variation $c_{V}=1/\sqrt{r}≃0.5−0.6$. The fitted model fully reproduces this ‘scaling property’ (Figure 4). The observed coefficient of variation remained in the range $c_{V}≃0.05−0.06$ for nearly all contrast combinations (Figure 4b). Unexpectedly, both observed and fitted values increased above, or decreased below, this range at extreme contrast combinations (Figure 4b, left panel). Along the main diagonal $c_{dom}=c_{sup}$ , where observed values had smaller error bars, both observed and fitted values of skewness were $\gamma_{1}/c_{V}≃2$ and thus approximated a gamma distribution (Figure 4d, blue symbols).

#### Specific contribution of evidence and decision levels

What are the reasons for the surprising success of the model in reproducing universal characteristics of multistable phenomena, including the counterintuitive input dependence (‘Levelt’s propositions’), the stereotypical distribution shape (‘scaling property’), and the positive sequential correlation (as detailed in Figures 3 and 4)? Which level of model dynamics is responsible for reproducing different aspects of BR dynamics?

Below, we describe the specific contributions of different model components. Specifically, we show that the evidence level of the model reproduces ‘Levelt’s propositions I–III’ and the ‘scaling property,’ whereas the decision level reproduces ‘Levelt’s proposition IV.’ A non-trivial interaction between evidence and decision levels reproduces serial dependencies. Additionally, we show that this interaction predicts further aspects of serial dependencies – such as sensitivity to image contrast – that were not reported previously, but are confirmed by our experimental observations.

### Levelt’s propositions I, II, and III

The characteristic input dependence of average dominance durations emerges in two steps (as in Gigante et al., 2009). First, inputs and feedback suppression shape the birth-death dynamics of evidence pools $E$ and $E^{′}$ (by setting disparate transition rates $ν^{\pm}$, following Equation 3’ and Equation 1). Second, this sets in motion two opponent developments (habituation of dominant evidence activity and recovery of non-dominant evidence activity, both following Equation 2) that jointly determine dominance duration.

To elucidate this mechanism, it is helpful to consider the limit of large pools ($N→∞$) and its deterministic dynamics (Figure 2), which corresponds to the average stochastic dynamics. In this limit, periods of dominant evidence $E$ or $E^{′}$ start and end at the same levels ($e_{start}=e_{start}^{′}$ and $e_{end}=e^{′}_{end}$), because reversal thresholds $Δ_{rev}$ are the same for evidence difference $e−e^{′}$ and $e^{′}−e$ (see section Levelt IV below).

The rates at which evidence habituates or recovers depend, in the first instance, on asymptotic levels $e_{∞}$ and $e^{′}_{∞}$ (Equation 1 and 2, Figure 2b and Appendix 1—figure 4). In general, dominance durations depend on distance $Δ_{∞}$ between asymptotic levels: the further apart these are, the faster the development and the shorter the duration. As feedback suppression inverts the sign of the opponent developments, dominant evidence decreases (habituates) while non-dominant evidence increases (recovers). Due to this inversion, $Δ_{∞}$ is roughly proportional to $e_{∞}^{non−dom}−e_{∞}^{dom}+w_{supp}$. It follows that the distance $Δ_{∞}$ is smaller and the reversal dynamics slower when dominant input is stronger, and vice versa. It further follows that incrementing one input (and raising the corresponding asymptotic level) speeds up recovery or slows down habituation, shortening or lengthening periods of non-dominance and dominance, respectively (Levelt I).

In the second instance, rates of habituation or recovery depend on characteristic times $\tau_{e}$ and $\tau_{e^{′}}$ (Equation 1 and 2). When these rates are unequal, dominance durations depend more sensitively on the slower process. This is why dominance durations depend more sensitively on non-dominant input (Levelt II): recovery of non-dominant evidence is generally slower than habituation of dominant evidence, independently of which input is weaker or stronger. The reason is that the respective effects of characteristic times $\tau_{e}$ and $\tau_{e^{′}}$ and asymptotic levels $e_{∞}$ and $e^{′}_{∞}$ are synergistic for weaker-input evidence (in both directions), whereas they are antagonistic for stronger-input evidence (see Appendix 1, section Deterministic dynamics: Evidence pools and Appendix 1—figure 4).

In general, dominance durations depend hyperbolically on $Δ_{∞}$ (Figure 2c and Equation 7 in Appendix 1). Dominance durations become infinite (and reversals cease) when $Δ_{∞}$ falls below the reversal threshold $Δ_{rev}$. This hyperbolic dependence is also why alternation rate peaks at equidominance (Levelt III): increasing the difference between inputs always lengthens longer durations more than it shortens shorter durations, thus lowering alternation rate.

### Distribution of dominance durations

For all combinations of image contrast, the mechanism accurately predicts the experimentally observed distributions of dominance durations. This is owed to the stochastic activity of pools of bistable variables.

Firstly, dominance distributions retain nearly the same shape, even though average durations vary more than threefold with image contrast (see also Appendix 1—figure 6a,b). This ‘scaling property’ is due to the Poisson-like variability of birth-death processes (see Appendix 1, section Stochastic dynamics). Generally, when a stochastic accumulation approaches threshold, the rates of both accumulation and dispersion of activity affect the distribution of first-passage-times (Cao et al., 2014; Cao et al., 2016). In the special case of Poisson-like variability, the two rates vary proportionally and preserve distribution shape (see also Appendix 1—figure 6c,d).

Secondly, predicted distributions approximate gamma distributions with scale factor $r≃3−4$. As shown previously (Cao et al., 2014; Cao et al., 2016), this is due to birth-death processes accumulating activity within a narrow range (i.e., evidence difference $Δe\leq0.2$). In this low-threshold regime, the first-passage-times of birth-death processes are both highly variable and gamma distributed, consistent with experimental observations.

Thirdly, the predicted variability (coefficients of variation) of dominance periods varies along the $c+c^{′}=1$ axis, being larger for longer than for shorter dominance durations (Figure 4a,b). The reason is that stochastic development becomes noise-dominated. For longer durations, stronger-input evidence habituates rapidly into a regime where random fluctuations gain importance (see also Appendix 1—figure 4a,b).

### Levelt’s proposition IV

The model accurately predicts how dominance durations shorten with higher image contrast $c=c^{′}$ (Levelt IV). Surprisingly, this reflects the dynamics of decision pools $R$ and $R^{′}$ (Figure 5).

![Figure 5.](https://cdn.elifesciences.org/articles/61581/elife-61581-fig5-v1.jpg)

**Figure 5.:** (a) The joint stable state of decision pools (here $r^{′}≃1$ and $r≃0$) can be destabilized by sufficiently contradictory evidence, $e§gt;e^{′}$. (b) Effective potential $U(e,e^{′},r,r^{′})$ (colored curves) and steady states $r_{∞}$ (colored dots) for different levels of contradictory input, $Δe=e−e^{′}$. Increasing $Δe$ destabilizes the steady state and shifts $r_{∞}$ rightward (curved arrow). The critical value $r_{crit}$ (dotted vertical line), at which the steady state turns unstable, is reached when $Δe$ reaches the reversal threshold $Δ_{rev}$. At this point, a reversal ensues with $r→1$ and $r^{′}→0$. (c) The reversal threshold $Δ_{rev}$ diminishes with combined evidence $e+e^{′}$. In the deterministic limit, $Δ_{rev}$ decreases linearly with $e¯=(e+e^{′})/2$ (dashed red line). In the stochastic system, the average evidence bias $⟨Δe⟩$ at the time of reversals decreases similarly with the average evidence mean $⟨e¯⟩$ (black dots). Actual values of $Δe$ at the time of reversals are distributed around these average values (gray shading). (d) Average evidence mean $⟨e¯⟩$ (left) and average evidence bias $⟨Δe⟩$ (middle) at the time of reversals as a function of image contrast $c$ and $c^{′}$. Decrease of average evidence bias $⟨Δe⟩$ with contrast shortens dominance durations (Levelt IV). At low contrast (blue dot), higher reversal thresholds $Δ_{rev}$ result in less frequent reversals (bottom right, gray and white regions) whereas, at high contrast (red dot), lower reversal thresholds lead to more frequent reversals (top right).

Here again it is helpful to consider the deterministic limit of large pools ($N→∞$). In this limit, a dominant decision state $r^{′}≃1$ is destabilized when a contradictory evidence difference $Δe=e−e^{′}$ exceeds a certain threshold value $Δ_{rev}$ (Figure 5b and Appendix 1, section Deterministic dynamics: Decision pools). Due to the combined effect of excitatory and inhibitory feedforward projections, $w_{exc}$ and $w_{inh}$ (Equation 4 and Figure 5a), this average reversal threshold decreases with mean evidence activity $e¯=(e+e^{′})/2$. Simulations of the fully stochastic model ($N=25$) confirm this analysis (Figure 5c). As average evidence activity $⟨e¯⟩$ increases with image contrast, the average evidence bias $⟨Δe⟩$ at the time of reversals decreases, resulting in shorter dominance periods (Figure 5d).

#### Serial dependence

The proposed mechanism predicts positive correlations between successive dominance durations, a well-known characteristic of multistable phenomena (Fox and Herrmann, 1967; Walker, 1975; Van Ee, 2005; Denham et al., 2018). In addition, it predicts further aspects of serial dependence not reported previously.

In both model and experimental observations, a long dominance period tends to be followed by another long period, and a short dominance period by another short period (Figure 6). In the model, this is due to mean evidence activity $e¯=(e+e^{′})/2$ fluctuating stochastically above and below its long-term average. The autocorrelation time of these fluctuations increases monotonically with image contrast and, for high contrast, spans multiple dominance periods (see Appendix 1, section Characteristic times and Appendix 1—figure 7). Note that fluctuations of $e¯$ diminish as the number of bistable variables increases and vanishe in the deterministic limit $N→∞$.

![Figure 6.](https://cdn.elifesciences.org/articles/61581/elife-61581-fig6-v1.jpg)

**Figure 6.:** (a) Conditional expectation of dominance duration $⟨T_{\pmn}⟩$ (top) and of average mean evidence activity, $⟨e¯_{\pmn}⟩$ (bottom), in model simulations with maximal stimulus contrast ($c=c^{′}=1$). Dominance periods T0 were grouped into octiles, from longest (yellow) to shortest (black). For each octile, the average duration $⟨T_{\pmn}⟩$ of preceding and following dominance periods, as well as the average mean evidence activity $⟨e¯_{\pmn}⟩$ at the end of each period, is shown. All times in multiples of the overall average duration, $⟨T⟩$, and activities in multiples of the overall average activity $⟨e¯⟩$. (b) Example reversal sequence from model. Bottom: stochastic development of evidence activities $e$ and $e^{′}$ (red and blue traces), with large, joint fluctuations raising or lowering mean activity $e¯=(e+e^{′})/2$ above or below long-term average (dashed line). Top left: episode with $e¯$ above average, lower $Δ_{rev}$, and shorter dominance periods. Top right: episode with $e¯$ below average, higher $Δ_{rev}$, and longer dominance durations. (c) Examples of reversal sequences from human observers ($c=c^{′}=1$ and $c=c^{′}=1/2$). (d) Positive lagged correlations predicted by model (mean, middle) and confirmed by experimental observations (mean ± std, top). Alternative model (Laing and Chow, 2002) with adaptation and noise (mean, bottom), fitted to reproduce the values of $⟨T⟩$, cv, $\gamma_{1}$, and $cc_{1}$ predicted by the present model (blue stars).

Crucially, fluctuations of mean evidence $e¯$ modulate both reversal threshold $Δ_{rev}$ and dominance durations $T$, as illustrated in Figure 6a,b. To obtain Figure 6a, dominance durations were grouped into quantiles and the average duration $⟨T_{0}⟩$ of each quantile was compared to the conditional expectation of preceding and following durations $⟨T_{\pmn}⟩$ (upper graph). For the same quantiles (compare color coding), average evidence activity $⟨e¯_{0}⟩$ was compared to the conditional expectation $⟨e¯_{\pmn}⟩$ at the end of preceding and following periods (lower graph). Both the inverse relation between $⟨T_{\pmn}⟩$ and $⟨e¯_{\pmn}⟩$ and the autocorrelation over multiple dominance periods are evident.

This source of serial dependency – comparatively slow fluctuations of $e¯$ and $Δ_{rev}$ – predicts several qualitative characteristics not reported previously and now confirmed by experimental observations. First, sequential correlations are predicted (and observed) to be strictly positive at all lags (next period, one-after-next period, and so on) (Figure 6d). In other words, it predicts that several successive dominance periods are shorter (or longer) than average.

Second, due to the contrast dependence of autocorrelation time, sequential correlations are predicted (and observed) to increase with image contrast (Figure 6d). The experimentally observed degree of contrast dependence is broadly consistent with pool sizes between $N=25$ and $N=40$ (black and red curves in Figure 3e). Larger pools with hundreds of bistable variables do not express the observed dependence on contrast (not shown).

Third, for high image contrast, reversal sequences are predicted (and observed) to contain extended episodes with dominance periods that are short or extended episodes with periods that are long (Figure 6c). When quantified in terms of a ‘burstiness index,’ the degree of inhomogeneity in predicted and observed reversal sequences is comparable (see Appendix 1, section Burstiness and Appendix 1—figure 8).

Many previous models of BR (e.g., Laing and Chow, 2002) postulated selective adaptation of competing representations to account for serial dependency. However, selective adaptation is an opponent process that favors positive correlations between different dominance periods, but negative correlations between same dominance periods. To demonstrate this point, we fitted such a model to reproduce our experimental observations ($T$, $c_{V}$, $\gamma_{1}$, and $cc_{1}$) for five image contrasts $c=c^{′}$. As expected, the alternative model predicts negative correlations $cc_{2}$ for same dominance periods (Figure 6d, right panel), contrary to what is observed.

## Discussion

We have shown that many well-known features of BR are reproduced, and indeed guaranteed, by a particular dynamical mechanism. Specifically, this mechanism reproduces the counterintuitive input dependence of dominance durations (‘Levelt’s propositions’), the stereotypical shape of dominance distributions (‘scaling property’), and the positive sequential correlation of dominance periods. The explanatory power of the proposed mechanism is considerably higher than that of previous models. Indeed, the observations explained exhibited more effective degrees of freedom (approximately 14) than the mechanism itself (between 3 and 4).

The proposed mechanism is biophysically plausible in terms of the out-of-equilibrium dynamics of a modular and hierarchical network of spiking neurons (see also further below). Individual modules idealize the input dependence of attractor transitions in assemblies of spiking neurons. All synaptic effects superimpose linearly, consistent with extended mean-field theory for neuronal networks (Amit and Brunel, 1997; Van Vreeswijk and Sompolinski, 1996). The interaction between ‘rivaling’ sets of modules (‘pools’) results in divisive normalization, which is consistent with many cortical models (Carandini and Heeger, 2011; Miller, 2016).

It has long been suspected that multistable phenomena in visual, auditory, and tactile perception may share a similar mechanistic origin. As the features of BR explained here are in fact universal features of multistable phenomena in different modalities, we hypothesize that similar out-of-equilibrium dynamics of modular networks may underlie all multistable phenomena in all sensory modalities. In other words, we hypothesize that this may be a general mechanism operating in many perceptual representations.

### Dynamical mechanism

Two principal alternatives have been considered for the dynamical mechanism of perceptual decision-making: drift-diffusion models (Luce, 1986; Ratcliff and Smith, 2004) and recurrent network models (Wang, 2008; Wang, 2012). The mechanism proposed here combines both alternatives: at its evidence level, sensory information is integrated, over both space and time, by ‘local attractors’ in a discrete version of a drift-diffusion process. At its decision level, the population dynamics of a recurrent network implements a winner-take-all competition between ‘non-local attractors.’ Together, the two levels form a ‘nested attractor’ system (Braun and Mattia, 2010) operating perpetually out of equilibrium.

A recurrent network with strong competition typically ‘normalizes’ individual responses relative to the total response (Miller, 2016). Divisive normalization is considered a canonical cortical computation (Carandini and Heeger, 2011), for which multiple rationales can be found. Here, divisive normalization is augmented by indiscriminate feedforward inhibition. This combination ensures that decision activity rapidly and reliably categorizes differential input strength, largely independently of total input strength.

Another key feature of the proposed mechanism is that a ‘dominant’ decision pool applies feedback suppression to the associated evidence pool. Selective suppression of evidence for a winning hypothesis features in computational theories of ‘hierarchical inference’ (Rao and Ballard, 1999; Lee and Mumford, 2003; Parr and Friston, 2017b; Pezzulo et al., 2018), as well as in accounts of multistable perception inspired by such theories (Dayan, 1998; Hohwy et al., 2008; Weilnhammer et al., 2017). A normative reason for feedback suppression arises during continuous inference in uncertain and volatile environments, where the accumulation of sensory information is ongoing and cannot be restricted to appropriate intervals (Veliz-Cuba et al., 2016). Here, optimal change detection requires an exponentially rising bias against evidence for the most likely state, ensuring that even weak changes are detected, albeit with some delay.

The pivotal feature of the proposed mechanism are pools of bistable variables or ‘local attractors.’ Encoding sensory inputs in terms of persistent ‘activations’ of local attractors assemblies (rather than in terms of transient neuronal spikes) creates an intrinsically retentive representation: sites that respond are also sites that retain information (for a limited time). Our results are consistent with a few tens of bistable variables in each pool. In the proposed mechanism, differential activity of two pools accumulates evidence against the dominant appearance until a threshold is reached and a reversal ensues (see also Barniv and Nelken, 2015; Nguyen et al., 2020). Conceivably, this discrete non-equilibrium dynamics might instantiate a variational principle of inference such as ‘maximum caliber’ (Pressé et al., 2013; Dixit et al., 2018).

### Emergent features

The components of the proposed mechanism interact to guarantee the statistical features that characterize BR and other multistable phenomena. Discretely stochastic accumulation of differential evidence against the dominant appearance ensures sensitivity of dominance durations to non-dominant input. It also ensures the invariance of relative variability (‘scaling property’) and gamma-like distribution shape of dominance durations. Due to a non-trivial interaction with the competitive decision, discretely stochastic fluctuations of evidence-level activity express themselves in a serial dependency of dominance durations. Several features of this dependency were unexpected and not reported previously, for example, the sensitivity to image contrast and the ‘burstiness’ of dominance reversals (i.e., extended episodes in which dominance periods are consistently longer or shorter than average). The fact that these predictions are confirmed by our experimental observations provides further support for the proposed mechanism.

### Relation to previous models

How does the proposed mechanism compare to previous ‘dynamical’ models of multistable phenomena? It is of similar complexity as previous minimal models (Laing and Chow, 2002; Wilson, 2007; Moreno-Bote et al., 2010) in that it assumes four state variables at two dynamical levels, one slow (accumulation) and one fast (winner-take-all competition). It differs in reversing their ordering: visual input impinges first on the slow level, which then drives the fast level. It also differs in that stochasticity dominates the slow dynamics (as suggested by van Ee, 2009), not the fast dynamics. However, the most fundamental difference is discreteness (pools of bistable variables), which shapes all key dynamical properties.

Unlike many previous models (e.g., Laing and Chow, 2002; Wilson, 2007; Moreno-Bote et al., 2007; Moreno-Bote et al., 2010; Cohen et al., 2019), the proposed mechanism does not include adaptation (stimulation-driven weakening of evidence), but a phenomenologically similar feedback suppression (perception-driven weakening of evidence). Evidence from perceptual aftereffects supports the existence of both stimulation- and perception-driven adaptation, albeit at different levels of representation. Aftereffects in the perception of simple visual features – such as orientation, spatial frequency, or direction of motion (Blake and Fox, 1974; Lehmkuhle and Fox, 1975; Wade and Wenderoth, 1978) – are driven by stimulation rather than by perceived dominance, whereas aftereffects in complex features – such as spiral motion, subjective contours, rotation in depth (Wiesenfelder and Blake, 1990; Van der Zwan and Wenderoth, 1994; Pastukhov et al., 2014a) – typically depend on perceived dominance. Several experimental observations related to BR have been attributed to stimulation-driven adaptation (e.g., negative priming, flash suppression, generalized flash suppression; Tsuchiya et al., 2006). The extent to which a perception-driven adaptation could also explain these observations remains an open question for future work.

Multistable perception induces a positive priming or ‘sensory memory’ (Pearson and Clifford, 2005; Pastukhov and Braun, 2008; Pastukhov et al., 2013a), which can stabilize a dominant appearance during intermittent presentation (Leopold et al., 2003; Maier et al., 2003; Sandberg et al., 2014). This positive priming exhibits rather different characteristics (e.g., shape-, size- and motion-specificity, inducement period, persistence period) than the negative priming/adaptation of rivaling representations (de Jong et al., 2012; Pastukhov et al., 2013a; Pastukhov and Braun, 2013b; Pastukhov et al., 2014a; Pastukhov et al., 2014b; Pastukhov, 2016). To our mind, this evidence suggest that sensory memory is mediated by additional levels of representation and not by self-stabilization of rivaling representations, as has been suggested (Noest et al., 2007; Leptourgos, 2020). To incorporate sensory memory, the present model would have to be extended to include three hierarchical levels (evidence, decision, and memory), as previously proposed by Gigante et al., 2009.

BR arises within local regions of the visual field, measuring approximately $0.25^{∘}$ to $0.5^{∘}$ in the fovea (Leopold, 1997; Logothetis, 1998). No rivalry ensues when the stimulated locations in the left and right eye are more distant from each other. The computational model presented here encompasses only one such local region, and therefore cannot reproduce spatially extended phenomena such as piecemeal rivalry (Blake et al., 1992) or traveling waves (Wilson et al., 2001). To account for these phenomena, the visual field would have to be tiled with replicant models linked by grouping interactions (Knapen et al., 2007; Bressloff and Webber, 2012).

A particularly intriguing previous model (Wilson, 2003) postulated a hierarchy with competing and adapting representations in eight state variables at two separate levels, one lower (monocular) and another higher (binocular) level. This ‘stacked’ architecture could explain the fascinating experimental observation that one image can continue to dominate (dominance durations $∼2s$) even when images are rapidly swapped between eyes (period $1/3 s$) (Kovács et al., 1996; Logothetis et al., 1996). We expect that our hierarchical model could also account for this phenomenon if it were to be replicated at two successive levels. It is tempting to speculate that such ‘stacking’ might have a normative justification in that it might subserve hierarchical inference (Yuille and Kersten, 2006; Hohwy et al., 2008; Friston, 2010).

Another previous model (Li et al., 2017) used a hierarchy with 24 state variables at three separate levels to show that a stabilizing influence of selective visual attention could also explain slow rivalry when images are swapped rapidly. Additionally, this rather complex model reproduced the main features of Levelt’s propositions, but did not consider scaling property and sequential dependency. The model shared some of the key features of the present model (divisive inhibition, differential excitation-inhibition), but added a multiplicative attentional modulation. As the present model already incorporates the ‘biased competition’ that is widely thought to underlie selective attention (Sabine and Ungerleider, 2000; Reynolds and Heeger, 2009), we expect that it could reproduce attentional effects by means of additive modulations.

### Continuous inference

The notion that multistable phenomena such as BR reflect active exploration of explanatory hypotheses for sensory evidence has a venerable history (von Helmholtz, 1867; Barlow et al., 1972; Gregory, 1980; Leopold and Logothetis, 1999). The mechanism proposed here is in keeping with that notion: higher-level ‘explanations’ compete for control (‘dominance’) of phenomenal appearance in terms of their correspondence to lower-level ‘evidence.’ An ‘explanation’ takes control if its correspondence is sufficiently superior to that of rival ‘explanations.’ The greater the superiority, the longer control is retained. Eventually, alternative ‘explanations’ seize control, if only briefly. This manner of operation is also consistent with computational theories of ‘analysis by synthesis’ or ‘hierarchical inference,’ although there are many differences in detail (Rao and Ballard, 1999; Parr and Friston, 2017b; Pezzulo et al., 2018).

Interacting with an uncertain and volatile world necessitates continuous and concurrent evaluation of sensory evidence and selection of motor action (Cisek and Kalaska, 2010; Gold and Stocker, 2017). Multistable phenomena exemplify continuous decision-making without external prompting (Braun and Mattia, 2010). Sensory decision-making has been studied extensively, mostly in episodic choice-task, and the neural circuits and activity dynamics underlying episodic decision-making – including representations of potential choices, sensory evidence, and behavioral goals – have been traced in detail (Cisek and Kalaska, 2010; Gold and Shadlen, 2007; Wang, 2012; Krug, 2020). Interestingly, there seems to be substantial overlap between choice representations in decision-making and in multistable situations (Braun and Mattia, 2010).

Continuous inference has been studied extensively in auditory streaming paradigms (Winkler et al., 2012; Denham et al., 2014). The auditory system seems to continually update expectations for sound patterns on the basis of recent experience. Compatible patterns are grouped together in auditory awareness, and incompatible patterns result in spontaneous reversals between alternatives. Many aspects of this rich phenomenology are reproduced by computational models driven by some kind of ‘prediction error’ (Mill et al., 2013). The dynamics of two recent auditory models (Barniv and Nelken, 2015; Nguyen et al., 2020) are rather similar to the model presented here: while one sound pattern dominates awareness, evidence against this pattern is accumulated at a subliminal level.

### Relation to neural substrate

What might be the neural basis of the bistable variables/‘local attractors’ proposed here? Ongoing activity in sensory cortex appears to be low-dimensional, in the sense that the activity of neurons with similar response properties varies concomitantly (‘shared variability,’ ‘noise correlations,’ Ponce-Alvarez et al., 2012, Mazzucato et al., 2015, Engel et al., 2016, Rich and Wallis, 2016, Mazzucato et al., 2019). This shared variability reflects the spatial clustering of intracortical connectivity (Muir and Douglas, 2011; Okun et al., 2015; Cossell et al., 2015; Lee et al., 2016; Rosenbaum et al., 2017) and unfolds over moderately slow time scales (in the range of $100 ms$ to $500 ms)$ both in primates and rodents (Ponce-Alvarez et al., 2012; Mazzucato et al., 2015; Cui et al., 2016; Engel et al., 2016; Rich and Wallis, 2016; Mazzucato et al., 2019).

Possible dynamical origins of shared and moderately slow variability have been studied extensively in theory and simulation (for reviews, see Miller, 2016; Huang and Doiron, 2017; La Camera et al., 2019). Networks with weakly clustered connectivity (e.g., 3% rewiring) can express a metastable attractor dynamics with moderately long time scales (Litwin-Kumar and Doiron, 2012; Doiron and Litwin-Kumar, 2014; Schaub et al., 2015; Rosenbaum et al., 2017). In a metastable dynamics, individual (connectivity-defined) clusters transition spontaneously between distinct and quasi-stationary activity levels (‘attractor states’) (Tsuda, 2001; Stern et al., 2014).

Evidence for metastable attractor dynamics in cortical activity is accumulating steadily (Mattia et al., 2013; Mazzucato et al., 2015; Rich and Wallis, 2016; Engel et al., 2016; Marcos et al., 2019; Mazzucato et al., 2019). Distinct activity states with exponentially distributed durations have been reported in sensory cortex (Mazzucato et al., 2015; Engel et al., 2016), consistent with noise-driven escape transitions (Doiron and Litwin-Kumar, 2014; Huang and Doiron, 2017). And several reports are consistent with external input modulating cortical activity mostly indirectly, via the rate of state transitions (Fiser et al., 2004; Churchland et al., 2010; Mazzucato et al., 2015; Engel et al., 2016; Mazzucato et al., 2019).

The proposed mechanism assumes bistable variables with noise-driven escape transitions, with transition rates modulated exponentially by external synaptic drive. Following previous work (Cao et al., 2016), we show this to be an accurate reduction of the population dynamics of metastable networks of spiking neurons.

Unfortunately, the spatial structure of the ‘shared variability’ or ‘noise correlations’ in cortical activity described above is poorly understood. However, we estimate that the cortical representation of our rivaling display involves approximately $400 mm^{2}$ and $200 mm^{2}$ of cortical surface in cortical areas V1 and V4, respectively (Winawer and Witthoft, 2015; Winawer and Benson, 2021). Accordingly, in each of these two cortical areas, the neural representation of rivaling stimulation can comfortably accommodate several thousand recurrent local assemblies, each capable of expressing independent collective dynamics (i.e., ‘classic columns’ comprising several ‘minicolumns’ with distinct stimulus selectivity Nieuwenhuys R, 1994, Kaas, 2012). Thus, our model assumes that the representation of two rivaling images engages approximately 1–2% of the available number of recurrent local assemblies.

### Neurophysiological correlates of BR

Neurophysiological correlates of BR have been studied extensively, often by comparing reversals of phenomenal appearance during binocular stimulation with physical alternation (PA) of monocular stimulation (e.g., Leopold and Logothetis, 1996; Scheinberg and Logothetis, 1997; Logothetis, 1998; Wilke et al., 2006; Aura et al., 2008; Keliris et al., 2010; Panagiotaropoulos et al., 2012; Bahmani et al., 2014; Xu et al., 2016; Kapoor et al., 2020; Dwarakanath et al., 2020). At higher cortical levels, such as inferior temporal cortex (Scheinberg and Logothetis, 1997) or prefrontal cortex (Panagiotaropoulos et al., 2012; Kapoor et al., 2020; Dwarakanath et al., 2020), BR and PA elicit broadly comparable neurophysiological responses that mirror perceptual appearance. Specifically, activity crosses its average level at the time of each reversal, roughly in phase with perceptual appearance (Scheinberg and Logothetis, 1997; Kapoor et al., 2020). In primary visual cortex (area V1), where many neurons are dominated by input from one eye, neurophysiological correlates of BR and PA diverge in an interesting way: whereas modulation of spiking activity is weaker during BR than PA (Leopold and Logothetis, 1996; Logothetis, 1998; Wilke et al., 2006; Aura et al., 2008; Keliris et al., 2010), measures thought to record dendritic inputs are modulated comparably under both conditions (Aura et al., 2008; Keliris et al., 2010; Bahmani et al., 2014; Yang et al., 2015; Xu et al., 2016). A stronger divergence is observed at an intermediate cortical level (visual area V4), where neurons respond to both eyes. Whereas some units modulate their spiking activity comparably during BR and PA (i.e., increased activity when preferred stimulus becomes dominant), other units exhibit the opposite modulation during BR (i.e., reduced activity when preferred stimulus gains dominance) (Leopold and Logothetis, 1996; Logothetis, 1998; Wilke et al., 2006). Importantly, at this intermediate cortical level, activity crosses its average level well before and after each reversal (Leopold and Logothetis, 1996; Logothetis, 1998), roughly in quarter phase with perceptual appearance.

Some of these neurophysiological observations are directly interpretable in terms of the model proposed here. Specifically, activity modulation at higher cortical levels (inferotemporal cortex, prefrontal cortex) could correspond to ‘decision activity,’ predicted to vary in phase with perceptual appearance. Similarly, activity modulation at intermediate cortical levels (area V4) could correspond to ‘evidence activity,’ which is predicted to vary in quarter phase with perceptual appearance. This identification would also be consistent with the neurophysiological evidence for attractor dynamics in columns of area V4 (Engel et al., 2016). The subpopulation of area V4 with opposite modulation could mediate feedback suppression from decision levels. If so, our model would predict this subpopulation to vary in counterphase with perceptual appearance. Finally, the fascinating interactions observed within primary visual cortex (area V1) are well beyond the scope of our simple model. Presumably, a ‘stacked’ model with two successive levels of competitive interactions at monocular and binocular levels or representation (Wilson, 2003; Li et al., 2017) would be required to account for these phenomena.

### Conclusion

As multistable phenomena and their characteristics are ubiquitous in visual, auditory, and tactile perception, the mechanism we propose may form a general part of sensory processing. It bridges neural, perceptual, and normative levels of description and potentially offers a ‘comprehensive task-performing model’ (Kriegeskorte and Douglas, 2018) for sensory decision-making.

## Materials and methods

### Psychophysics

Six practiced observers participated in the experiment (four males, two females). Informed consent, and consent to publish, was obtained from all observers, and ethical approval Z22/16 was obtained from the Ethics Commission of the Faculty of Medicine of the Otto-von-Guericke University, Magdeburg. Stimuli were displayed on an LCD screen (EIZO ColorEdge CG303W, resolution $2560\times1600$ pixels, viewing distance was 104 cm, single pixel subtended $0.014^{∘}$, refresh rate 60 Hz) and were viewed through a mirror stereoscope, with viewing position being stabilized by chin and head rests. Display luminance was gamma-corrected and average luminance was $50 cd/m^{2}$.

Two grayscale circular orthogonally oriented gratings ($+45^{∘}$ and $−45^{∘}$) were presented foveally to each eye. Gratings had diameter of $1.6^{∘}$, spatial period $2 cyc/deg$. To avoid a sharp outer edge, grating contrast was modulated with Gaussian envelope (inner radius $0.6^{∘}$, $\sigma=0.2^{∘}$). Tilt and phase of gratings was randomized for each block. Five contrast levels were used: 6.25, 12.5, 25, 50, and 100%. Contrast of each grating was systematically manipulated, so that each contrast pair was presented in two blocks (50 blocks in total). Blocks were $120s$ long and separated by a compulsory 1 min break. Observers reported on the tilt of the visible grating by continuously pressing one of two arrow keys. They were instructed to press only during exclusive visibility of one of the gratings, so that mixed percepts were indicated by neither key being pressed (25% of total presentation time). To facilitate binocular fusion, gratings were surrounded by a dichoptically presented square frame (outer size 9.8°, inner size 2.8°).

Dominance periods of ‘clear visibility’ were extracted in sequence from the final $90s$ of each block and the mean linear trend was subtracted from all values. Values from the initial $30s$ were discarded. To make comparable the dominance periods of different observers, values were rescaled by the ratio of the all-condition-all-observer average ($2.5s$) and the all-condition average of each observer ($2.5\pm1.3s$). Finally, dominance periods from symmetric conditions $(c_{left},c_{right})$ with $c_{left}=c_{right}$ were combined into a single category $(c_{dom},c_{sup})$, where $c_{dom}$ ($c_{sup}$) was the contrast viewed by the dominant (suppressed) eye. The number of observed dominance periods ranged from 900 to 1700 per contrast combination ($1300\pm240$).

For the dominance periods $T$ observed in each condition, first, second, and third central moments were computed, as well as coefficient of variation $c_{V}$ and skewness $\gamma_{1}$ relative to coefficient of variation:

$$
\mu_{1}=⟨T⟩,\mu_{2}=⟨T^{2}⟩−⟨T⟩,\mu_{3}=⟨T^{3}⟩−3⟨T⟩⟨T^{2}⟩+2⟨T⟩^{3}
$$



$$
c_{V}=\frac{\sqrt{\mu_{2}}}{\mu_{1}},\frac{\gamma_{1}}{c_{V}}=\frac{\mu_{3}\mu_{1}}{\mu_{2}^{2}}
$$

The expected standard error of the mean for distribution moments is 2% for the mean, 3% for the coefficient of variation, and 12% for skewness relative to coefficient of variation, assuming 1000 gamma-distributed samples.

Coefficients of sequential correlations were computed from pairs of periods $(T_{i},T_{j})$ with opposite dominance (first and next: ‘lag’ $j−i=1$), pairs of periods with same dominance (first and next but one: ‘lag’ $j−i=2$), and so on,

$$
cc_{k}=\frac{⟨T_{i}−⟨T_{i}⟩⟩⟨T_{j}−⟨T_{j}⟩⟩}{\sqrt{(⟨T_{i}^{2}⟩−⟨T_{i}⟩^{2})(⟨T_{j}^{2}⟩−⟨T_{j}⟩^{2})}}
$$

where $⟨T⟩$ and $⟨T^{2}⟩$ are mean duration and mean square duration, respectively. The expected standard deviation of the coefficient of correlation is 0.03, assuming 1000 gamma-distributed samples.

To analyze ‘burstiness,’ we adapted a statistical measure used in neurophysiology (Compte et al., 2003). First, sequences of dominance periods were divided into all possible subsets of $k\in{2,3,…,16}$ successive periods and mean durations computed for each subset. Second, heterogeneity was assessed by computing, for each size $k$, the coefficient of variation cV over mean durations, compared to the mean and variance of the corresponding coefficient of variation for randomly shuffled sequences of dominance periods. Specifically, a ‘burstiness index’ was defined for each subset size $k$ as.

$$
BI(k)=\frac{c_{V}−⟨c_{V}⟩_{shuffle}}{\sqrt{⟨c_{V}^{2}⟩_{shuffle}−⟨c_{V}⟩_{shuffle}^{2}}}
$$

where $c_{V}$ is the coefficient of variation over subsets of size $k$ and where $⟨c_{V}⟩_{shuffle}$ and $⟨c_{V}^{2}⟩_{shuffle}$ are, respectively, mean and mean square of the coefficients of variation from shuffled sequences.

### Model

The proposed mechanism for BR dynamics relies on discretely stochastic processes (‘birth-death’ or generalized Ehrenfest processes). Bistable variables $x\in{0,1}$ transition between active and inactive states with time-varying Poisson rates $ν^{+}(t)$ (activation) and $ν^{−}(t)$ (inactivation). Two ‘evidence pools’ of $N$ such variables, $E$ and $E^{′}$, represent two kinds visual evidence (e.g., for two visual orientations), whereas two ‘decision pools,’ $R$ and $R^{′}$, represent alternative perceptual hypotheses (e.g., two grating patterns) (see also Appendix 1—figure 1). Thus, instantaneous dynamical state is represented by four active counts $n_{e},n_{e^{′}},n_{r},n_{r^{′}}\in[0,N]$ or, equivalently, by four active fractions $e,e^{′},r,r^{′}\in[0,1]$.

The development of pool activity over time is described by a master equation for probability $P_{n}(t)$ of the number $n(t)\in[0,N]$ active variables.

$$
∂_{t}P_{n}(t)=(N−n+1)ν^{+}P_{n−1}(t)+(n+1)ν^{−}P_{n+1}(t)−[(N−n)ν^{+}+nν^{−}]P_{n}(t)
$$

For constant $ν^{\pm}$, the distribution $P_{n}(t)$ is binomial at all times Karlin and McGregor, 1965, van Kampen, 1981. The time development of the number of active units $n_{X}(t)$ in pool $X$ is an inhomogeneous Ehrenfest process and corresponds to the count of activations, minus the count of deactivations,

$$
Δn_{X}(t)=B(N−n_{X},ν^{+}Δt)⏟activations−B(n_{X},ν^{−}Δt)⏟inactivations
$$

where $B(n,νΔt)$ is a discrete random variable drawn from a binomial distribution with trial number $n$ and success probability $νΔt$.

All variables of a pool have identical transition rates, which depend exponentially on the ‘potential difference’ $Δu=u+u^{0}$ between states, with a input-dependent component $u$ and a baseline component $u^{0}$:

$$
ν_{s}^{\pm}=\frac{ν_{s}}{2}e^{\pm(u_{e}+u_{e}^{0})/2},ν_{s^{′}}^{\pm}=\frac{ν_{s}}{2}e^{\pm(u_{e^{′}}+u_{e}^{0})/2}ν_{r}^{\pm}=\frac{ν_{r}}{2}e^{\pm(u_{r}+u_{r}^{0})/2},ν_{r^{′}}^{\pm}=\frac{ν_{r}}{2}e^{\pm(u_{r^{′}}+u_{r}^{0})/2}
$$

where $ν_{e}$ and $ν_{r}$ are baseline rates and $u_{e}^{0}$ and $u_{r}^{0}$ baseline components. The input-dependent components of effective potentials are modulated linearly by synaptic couplings

$$
u_{s}=w_{vis}f(c)−w_{supp}ru_{s^{′}}=w_{vis}f(c^{′})−w_{supp}r^{′}u_{r}=w_{exc}e−w_{inh}(e+e^{′})+w_{coop}r−w_{comp}r^{′}u_{r^{′}}=w_{exc}e−w_{inh}(e+e^{′})+w_{coop}r^{′}−w_{comp}r
$$

Visual inputs are $I=f(c)$ and $I^{′}=f(c^{′})$, respectively, where

$$
f(c)=\frac{ln⁡(1+c/\gamma)}{ln⁡(1+1/\gamma)}\in{0,1}
$$

is a monotonically increasing, logarithmic function of image contrast, with parameter γ.

### Degrees of freedom

The proposed mechanism has 11 independent parameters – 6 synaptic couplings, 2 baseline rates, 2 baseline potentials, 1 contrast nonlinearity – which were fitted to experimental observations. A 12th parameter – pool size – remained fixed.

<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Description</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>N</td>
      <td>Pool size</td>
      <td>25</td>
    </tr>
    <tr>
      <td>1/ve</td>
      <td>Baseline rate, evidence</td>
      <td>1.95 ± 0.10 s</td>
    </tr>
    <tr>
      <td>1/vr</td>
      <td>Baseline rate, decision</td>
      <td>0.018 ± 0.010 s</td>
    </tr>
    <tr>
      <td>ue0</td>
      <td>Baseline potential, evidence</td>
      <td>-1.65 ± 0.24</td>
    </tr>
    <tr>
      <td>ur0</td>
      <td>Baseline potential, decision</td>
      <td>-4.94 ± 0.67</td>
    </tr>
    <tr>
      <td>wvis</td>
      <td>Visual input coupling</td>
      <td>1.780 ± 0.092</td>
    </tr>
    <tr>
      <td>wexc</td>
      <td>Feedforward excitation</td>
      <td>152.2 ± 3.7</td>
    </tr>
    <tr>
      <td>winh</td>
      <td>Feedforward inhibition</td>
      <td>32.10 ± 2.3</td>
    </tr>
    <tr>
      <td>wcomp</td>
      <td>Lateral competition</td>
      <td>33.4 ± 1.2</td>
    </tr>
    <tr>
      <td>wcoop</td>
      <td>Lateral cooperation</td>
      <td>15.21± 0.59</td>
    </tr>
    <tr>
      <td>wsupp</td>
      <td>Feedback suppression</td>
      <td>2.34 ± 0.14</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>Contrast nonlinearity</td>
      <td>0.071 ± 0.011</td>
    </tr>
  </tbody>
</table>

### Fitting procedure

The experimental dataset consisted of two 5 × 5 arrays $X_{i}^{exp}$ for mean $⟨T⟩$ and coefficient of variation $c_{V}$, plus two scalar values for skewness $\gamma_{1}=2$ and correlation coefficient $cc_{1}=0.06$. The two scalar values corresponded to the (rounded) average values observed over the 5 × 5 combinations of image contrast. In other words, the fitting procedure prescribed contrast dependencies for the first two distribution moments, but not for correlation coefficients.

The fit error $E_{fit}$ was computed as a weighted sum of relative errors

$$
E_{fit}=\sumi=14w_{i}\delta_{i}/\sumi=14w_{i},\delta_{i}=|\frac{X_{i}^{mod}−X_{i}^{exp}}{X¯_{i}^{exp}}|
$$

with weighting $w=[1,1,1,1/4]$ emphasizing distribution moments.

Approximately 400 minimization runs were performed, starting from random initial configurations of model parameters. For the optimal parameter set, the resulting fit error for the mean observer dataset was approximately 13%. More specifically, the fit errors for mean dominance $⟨T⟩$, coefficient of variation $c_{V}$, relative skewness $\gamma_{1}/c_{V}$, and correlation coefficients $cc_{1}$ and $c⁢c_{2}$ were 9.8, 7.9, 8.7, 70, and 46%, respectively. Here, fit errors for relative skewness and correlation coefficients were computed for the isocontrast conditions, where experimental observations were least noisy.

To confirm that resulting fit was indeed optimal and could not be further improved, we studied the behavior of the fit error in the vicinity of the optimal parameter set. For each parameter $\alpha_{i}$, 30 values $\alpha_{i}^{(j)}$ were picked in the direct vicinity of the optimal parameter $\alpha_{i}^{opt}$ (Appendix 1—figure 9). The resulting scatter plot of value pairs $\alpha_{i}^{(j)}$ and fit error $E_{fit}^{(j)}$ was approximated by a quadratic function, which provided 95% confidence intervals for $\alpha_{i}^{(j)}$. For all parameters except $ν_{r}$, the estimated quadratic function was convex and the coefficient of the Hessian matrix associated with the fit error was positive. Additionally, the estimated extremum of each parabola was close to the corresponding optimal parameter, confirming that the parameter set was indeed optimal (Appendix 1—figure 9).

To minimize fit error, we repeated a stochastic gradient descent from randomly chosen initial parameter. Interestingly, the ensemble of suboptimal solutions found by this procedure populated a low-dimensional manifold of the parameter space in three principal components accounted for 95% of the positional variance. Thus, models that reproduce experimental observations with varying degrees of freedom exhibit only 3–4 effective degrees of freedom. We surmise that this is due, on the one hand, to the severe constraints imposed by our model architecture (e.g., discrete elements, exponential input dependence of transition rates) and, on the other hand, by the requirement that the dynamical operating regime behaves as a relaxation oscillator.

In support of this interpretation, we note that our 5 × 5 experimental measurements of $⟨T⟩$ and $c_{V}$ were accurately described by ‘quadric surfaces’ ($z=a_{1}+a_{2}x+a_{3}y+a_{4}x^{2}+a_{5}xy+a_{6}y^{2}$) with six coefficients each. Together with the two further measurements of $\gamma_{1}/c_{V}$ and $cc_{1}$, our experimental observations accordingly exhibited approximately $6\times2+2=14$ effective degrees of freedom. This number was sufficient to constrain the 3–4 dimensional manifold of parameters, where the model operated as a relaxation oscillator with a particular dynamics, specifically, a slow-fast dynamics associated, respectively, with the accumulation and reversal phases of BR.

### Alternative model

As an alternative model (Laing and Chow, 2002), a combination of competition, adaptation, and image-contrast-dependent noise was fitted to reproduce four 5 × 5 arrays $X_{i}^{exp}$ for mean $⟨T⟩$, coefficient of variation $c_{V}$, skewness $\gamma_{1}$, and correlation coefficient $cc_{1}$. Fit error $E_{fit}$ was computed as the average of relative errors

$$
E_{fit}=\frac{1}{n}\sumi=1n\delta_{i},\delta_{i}=|\frac{X_{i}^{mod}−X_{i}^{exp}}{X¯_{i}^{exp}}|
$$

For purposes of comparison, a weighted fit error with weighting $w=[1,1,1,1/4]$ was computed, as well.

The model comprised four state variables and independent colored noise:

$$
\tau_{r} r˙_{1,2}=−r_{1,2}+F(−\betar_{2,1}−ϕ_{a}a_{1,2}+I_{1,2}+n_{1,2})\tau_{a} a˙_{1,2}=−a_{1,2}+r_{1,2}\tau_{n} n˙_{1,2}=−n_{1,2}+\sigma_{1,2}\sqrt{2\tau_{n}}ξ(t)
$$

where $F(x)=[1+exp⁡(−x/κ)]^{−1}$ is a nonlinear activation function and $ξ(t)$ is white noise.

Additionally, both input $I_{1,2}$ and noise amplitude $\sigma_{1,2}$ were assumed to depend nonlinearly on image contrast $c_{1,2}$:

$$
I_{1,2}=f(c_{1,2})=b_{I}c_{1,2}^{k_{I}},\sigma_{1,2}=g(c_{1,2})=b_{\sigma}c_{1,2}^{k_{\sigma}}
$$

This coupling between input and noise amplitude served stabilizes the shape of dominance distributions over different image contrasts (‘scaling property’).

Parameters for competition β = 10, activity time constant $\tau_{r}=50 ms$, noise time constant $\tau_{n}=500 ms$, and activation function $k=0.1$ were fixed. Parameters for adaptation strength $ϕ_{a}\in[1,100]$, adaptation time constant $\tau_{a}\in[1,00]$, contrast dependence of input $b_{I}\in[1,5]$, $k_{I}\in[0.1,5]$, and contrast dependence of noise amplitude $b_{\sigma}\in[0.1,1]$, $k_{\sigma}\in[0.1,1]$ were explored within the ranges indicated.

The best fit (determined with a genetic algorithm) was as follows: $ϕ_{a}=18.39$, $\tau_{a}=22.78$, $k_{I}=1.52$, $b_{I}=2.92$, $k_{\sigma}=0.57$, $b_{\sigma}=0.19$. The fit errors for mean dominance $⟨T⟩$, coefficient of variation $c_{V}$, skewness $\gamma_{1}$, and correlation coefficient $cc_{1}$ were, respectively, 11.3, 8.3, 20, and 55%. The fit error for correlation coefficient $cc_{2}$ was 180% (because the model predicted negative values). The combined average for $⟨T⟩$, $c_{V}$, and $\gamma_{1}$ was 13.2%. The fit error obtained with weighting $w=(1,1,1,1/4)$ was 16.4%.

For Figure 6d, the alternative model was fitted only to observations at equal image contrast, $c=c^{′}$: mean dominance $⟨T⟩$, coefficient of variation $c_{V}$, skewness $\gamma_{1}$, and correlation coefficient $cc_{1}$. The combined average fit error for $⟨T⟩$, $c_{V}$, and $\gamma_{1}$ was 11.2%. The combined average for all four observables was 22%.

### Spiking network simulation

To illustrate a possible neural realization of ‘local attractors,’ we simulated a competitive network with eight identical assemblies of excitatory and inhibitory neurons, which collectively expresses a spontaneous and metastable dynamics (Mattia et al., 2013). One assembly (denoted as ‘foreground’) comprised 150 excitatory leaky-integrate-and-fire neurons, which were weakly coupled to the 1050 excitatory neurons of the other assemblies (denoted as ‘background’), as well as 300 inhibitory neurons. Note that background assemblies are not strictly necessary and are included only for the sake of verisimilitude. The connection probability between any two neurons was $c=2/3$. Excitatory synaptic efficacy between neurons in the same assembly and in two different assemblies was $J_{intra}=0.612mV$ and $J_{inter}=0.403mV$, respectively. Inhibitory synaptic efficacy was $J_{I}=−1.50mV$, and the efficacy of excitatory synapses onto inhibitory neurons was $J_{IE}=0.560mV$. Finally, ‘foreground’ neurons, ‘background neurons,’ and ‘inhibitory neurons’ each received independent Poisson spike trains of $2400Hz$, $2280Hz$ and $2400Hz$, respectively. Other settings were as in Mattia et al., 2013. As a result of these settings, ‘foreground’ activity transitioned spontaneously between an ‘off’ state of approximately $4Hz$ and an ‘on’ state of approximately $40Hz$.
