# Attentional modulation of neuronal variability in circuit models of cortex

## Authors

- Tatjana Kanashiro<sup>1</sup>
- Gabriel Koch Ocker<sup>2</sup>
- Marlene R Cohen<sup>3</sup> ([ORCID: 0000-0001-8583-4300](https://orcid.org/0000-0001-8583-4300))
- Brent Doiron<sup>2</sup> ([ORCID: 0000-0002-6916-5511](https://orcid.org/0000-0002-6916-5511)) †

### Affiliations

1. Program for Neural Computation Carnegie Mellon University and University of Pittsburgh Pittsburgh United States
2. Department of Mathematics University of Pittsburgh Pittsburgh United States
3. Center for the Neural Basis of Cognition Pittsburgh United States
4. Allen Institute for Brain Science Seattle United States
5. Department of Neuroscience University of Pittsburgh Pittsburgh United States

† Corresponding author

## Abstract

The circuit mechanisms behind shared neural variability (noise correlation) and its dependence on neural state are poorly understood. Visual attention is well-suited to constrain cortical models of response variability because attention both increases firing rates and their stimulus sensitivity, as well as decreases noise correlations. We provide a novel analysis of population recordings in rhesus primate visual area V4 showing that a single biophysical mechanism may underlie these diverse neural correlates of attention. We explore model cortical networks where top-down mediated increases in excitability, distributed across excitatory and inhibitory targets, capture the key neuronal correlates of attention. Our models predict that top-down signals primarily affect inhibitory neurons, whereas excitatory neurons are more sensitive to stimulus specific bottom-up inputs. Accounting for trial variability in models of state dependent modulation of neuronal activity is a critical step in building a mechanistic theory of neuronal cognition.

## Introduction

The behavioral state of the brain exerts a powerful influence on the cortical responses. For example, electrophysiological recordings from both rodents and primates show that the level of wakefulness (Steriade et al., 1993), active sensory exploration (Crochet et al., 2011), and attentional focus (Treue, 2001; Reynolds and Chelazzi, 2004; Gilbert and Sigman, 2007; Moore and Zirnsak, 2017) all modulate synaptic and spiking activity. Despite the diversity of behavioral contexts, in all of these cases an overall elevation and desynchronization of cortical activity accompanies heightened states of processing (Harris and Thiele, 2011). Exploration of the neuronal mechanisms that underly such state changes has primarily centered around how various neuromodulators shift the cellular and synaptic properties of cortical circuits (Hasselmo, 1995; Lee and Dan, 2012; Noudoost and Moore, 2011; Moore and Zirnsak, 2017) However, a coherent theory linking the modulation of cortical circuits to an active desynchronization of population activity is lacking. In this study we provide a circuit-based theory for the known attention-guided modulations of neuronal activity in the visual cortex of primates performing a stimulus change detection task.

The investigation of the neuronal correlates of attention has a rich history. Attention increases the firing rates of neurons engaged in feature- and spatial-based processing tasks (McAdams and Maunsell, 2000; Reynolds et al., 1999). Attentional modulation of the stimulus-response sensitivity (gain) of firing rates is more complicated, often depending on stimulus specifics such as the size and contrast of a visual image (Williford and Maunsell, 2006; Reynolds and Heeger, 2009; Sanayei et al., 2015). In recent years there has been increased focus on how brain states affect trial-to-trial spiking variability (Crochet et al., 2011; Lin et al., 2015; Doiron et al., 2016; Stringer et al., 2016). In particular, attention decreases the shared variability (noise correlations) of the firing rates from pairs of neurons (Cohen and Maunsell, 2009; Mitchell et al., 2009; Cohen and Maunsell, 2011; Herrero et al., 2013; Ruff and Cohen, 2014; Engel et al., 2016). The combination of a reduction in noise correlations and an increase in response gain has potentially important functional consequences through an improved population code (Cohen and Maunsell, 2009; Rabinowitz et al., 2015). In total, there is an emerging picture of the impact of attention on the trial-averaged and trial-variable spiking dynamics of cortical populations.

Phenomenological models of attentional modulation have been popular (Reynolds and Heeger, 2009; Navalpakkam and Itti, 2005; Gilbert and Sigman, 2007; Ecker et al., 2016); however, such analyses cannot provide insight into the circuit mechanics of attentional modulation. Biophysical models of attention circuits are difficult to constrain, due in large part to the diversity of mechanisms which control the firing rate and response gain of neurons (Silver, 2010; Sutherland et al., 2009). Nonetheless, several circuit models for attentional modulation have been proposed (Ardid et al., 2007; Deco and Thiele, 2011; Buia and Tiesinga, 2008), but analysis has been mostly confined to trial-averaged responses. Taking inspiration from these studies, mechanistic models of attentional modulation can be broadly grouped along two hypotheses. First, the circuit mechanisms that control trial-averaged responses may be distinct from those that modulate neuronal variability. This hypothesis has support from experiments in primate V1 showing that N-methyl-D-aspartate receptors have no impact on top-down attentional modulation of firing rates, yet have a strong influence of attentional control of noise correlations (Herrero et al., 2013). A second hypothesis is that the modulations of firing rates and noise correlations are reflections of a single biophysical mechanism. Support for this comes from pairs of V4 neurons that each show strong attentional modulation of firing rates, also show a strong attention mediated reductions in noise correlation (Cohen and Maunsell, 2011). In this study we provide novel analysis of the covariability of V4 population activity engaged in an attention-guided detection task (Cohen and Maunsell, 2009) that is consistent with the second hypothesis. Specifically, the modulation of spike count covariance between unattended and attended states has the same dimensionality as the firing rate modulation.

We use the results from our dimensionality analysis to show that an excitatory-inhibitory recurrent circuit model subject to global fluctuations is sufficient to capture both the increase in firing rate and response gain as well as population-wide decrease of noise correlations. Our model makes two predictions regarding neuronal modulation: (1) that attentional modulation favors inhibitory neurons, and (2) that stimulus drive favors excitatory neurons. Finally, we show that our model predicts increased informational content in the excitatory population, which would result in improved readout by potential downstream targets. In total, our study provides a simple, parsimonious, and biologically motivated model of attentional modulation in cortical networks.

## Results

### Attention decreases noise correlations primarily by decreasing covariance

Two rhesus monkeys (Macaca mulatta) with microelectrode arrays implanted bilaterally in V4 were trained in an orientation change detection task (Figure 1a; see Materials and methods: Data preparation). A display with oriented Gabor gratings on the left and right flashed on and off. The monkey was cued to attend to either the left or right grating before each block of trials, while keeping fixation on a point between the two gratings. After a random number of presentations, one of the gratings changed orientation. The monkey then had to saccade to that side to obtain a reward. The behavioral task and data collection have been previously reported (Cohen and Maunsell, 2009).

![Figure 1.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig1-v3.jpg)

**Figure 1.:** (a) Overview of orientation-change detection task; see (Cohen and Maunsell, 2009) for a full description. (b) Firing rates of neurons in the unattended (turquoise) and attended (orange) states, averaged over 3170 units. The slight oscillation in the firing rate was due to the monitor refresh rate. (c) Attention significantly decreased the spike count correlation and covariance and slightly increased variance. Error bars provide the SEM. (d) Histograms of changes in covariance for each unit pair (black) and variance for each unit (gray). In each case we consider the relative change $[X^{A}−X^{U}]/max(X^{A},X^{U})$, where $X$ is either $Cov(n_{i},n_{j})$ or $Var(n_{i})$. Data was collected from two monkeys over 21 and 16 recording sessions respectively. Signals were analyzed over a $200$ ms interval, starting $60$ ms after stimulus onset.

A neuron is considered to be in an 'attended state' when the attended stimulus is in the hemifield containing that neuron’s receptive field (contralateral hemifield), and in an 'unattended state' when it is in the other (ipsilateral) hemifield. The trial-averaged firing rates from both attended and unattended neurons displayed a brief transient rise ($∼$100 ms after stimulus onset), and eventually settled to an elevated sustained rate before the trial concluded (Figure 1b). During the sustained period the mean firing rate of attended neurons ($22.0$ sp/s) was greater than that of unattended neurons ($20.6$ sp/s) ($t$ test, $P < 10^{−5}$).

A major finding of Cohen and Maunsell (2009) was that the pairwise trial-to-trial noise correlations of the neuronal responses decreased with attention (Figure 1c, left, mean unattended 0.065, mean attended 0.045, $t$ test, $P < 10^{−5}$). The noise correlation between neurons $i$ and $j$ is a normalized measure, $ρ_{ij}=Cov(n_{i},n_{j})/\sqrt{Var(n_{i})Var(n_{j})}$, where Cov and Var denote spike count covariance and variance respectively. Both spike count variance and covariance significantly change with attention ($⟨Var^{U}⟩_{trials}=5.02⁢spikes^{2}$, $⟨Var^{A}⟩_{trials}=5.10⁢spikes^{2}$, $t$ test, $P < 10^{−3}$, $⟨Cov^{A}⟩_{trials}=0.252spikes^{2}$, $t$ test, $P < 10^{−5}$), but the decrease in covariance ($34.0%$) is much more pronounced than the increase in variance ($1.61%$; Figure 1c, middle and right). We therefore conclude that the attention mediated decrease in noise correlation is primarily due to decreased covariance.

To further validate this observation, we consider the distributions of pairwise changes in covariance (black) and variance (gray) with attention over the entire data set (Figure 1d). Covariance and variance are normalized by their respective maximal unattended or attended values (see Methods: Comparing change in covariance to change in variance). The change in covariance with attention is concentrated below zero with a large spread, whereas the change in variance is centered on zero with a narrower spread. Taken together these results suggest that to understand the mechanism by which noise correlations decrease it is necessary and sufficient to understand how spike count covariance decreases with attention.

### Attention is a low-rank modulation of noise covariance

A reasonable simplification of V4 neurons is that they receive a bottom-up stimulus alongside an attention-mediated top-down modulatory input. However, to properly model top-down attention we need to first understand the dimension of attentional modulation on the V4 circuit as a whole. Let Aϕ:ϕU ↦ ϕA denote the attentional modulation of measure ϕ from its value in the unattended state, ϕU, to its value in the attended state, ϕA. For example, the firing rate modulation Ar can be written as rA=Ar∘r𝐔, where rA is an N×1 vector of neural firing rates in the attended state, rU denotes the firing rate vector in the unattended state, Ar is a vector the same size as r, and ∘ denotes elementwise multiplication. In this case, the entries ai of Ar are the ratios of the firing rates: ai=riA/riU (Figure 2a).

![Figure 2.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig2-v3.jpg)

**Figure 2.:** (a) Attentional modulation of firing rate. Firing rates of neurons $i$ and $j$ (black circles are modulated by bottom-up stimulus and top-down attention. (b) Two possible models of attentional modulation of covariance. Left: High-rank covariance modulation, in which attention modulates the shared variability of each pair of neurons. Right: Low-rank covariance modulation, in which attention modulates each neuron individually rather than in a pairwise manner. (c–e) The measured covariance values plotted against those predicted by the rank-1 model for data collected in one recording session, for c, the actual data ($ρ=0.77$), d, shuffled data ($ρ_{shuf}=0.22$, 100 shuffles), and (e) artificial upper-bound data ($ρ_{ub}=0.90$, 10 realizations of the upper bound model). (f) Synthesis of c-e in a bar plot. The orange area represents the loss of model performance compared to the upper bound model, and the blue area represents the increase in model performance compared to model applied to shuffled data. (g) Rank-1 model performance reported for $21$ recording sessions from one monkey. Each bar represents one recording session. Recordings from a mean of $N=53.5$ units in the right-hemisphere were analyzed, with maximum and minimum $N$ of $80$ and $35$, respectively. Error bars denote standard error of the mean. (h) Mean normalized performance (relative to $ρ_{ub}$) for both hemispheres of two monkeys (M1 and M2). (i), Analysis as in (g), using leave-one-out cross-validation to test the predictive power of the model. (j) Mean normalized performance of the cross-validated data.

A less trivial aspect of attentional modulation is the modulation of covariance matrices:

$$
𝐂^{A}=A_{C}∘𝐂^{U}.
$$

Here $𝐂^{𝐀}$ is the attended spike count covariance matrix, $𝐂^{𝐔}$ the unattended spike count covariance matrix, and $A_{C}$ is a matrix the same size as $𝐂^{𝐔}$, consisting of entries $g_{i⁢j}$, which we will call covariance gains. Unlike firing rates, the transformation matrix $A_{C}$ can be of varying rank. On the one hand $A_{C}$ could be constructed from the ratios of the individual elements: $g_{i⁢j}=c_{i⁢j}^{A}/c_{i⁢j}^{U}$, with each pair of neurons $(i,j)$ receiving an individualized attentional modulation $g_{i⁢j}$ of their shared variability (Figure 2b, left). Under this modulation $A_{C}$ is a rank $N$ matrix. A rank $N A_{C}$ will always perfectly (and trivially) capture the matrix mapping in Equation (1). However, it is difficult to conceive of a top-down circuit mechanism that would allow attention to modulate each pair individually. On the other hand, $g_{i⁢j}$ could depend not on the specific pair $(i,j)$, but on the individual neurons of the pairing: $g_{i⁢j}=g_{i}⁢g_{j}$ (Figure 2b, right). In this case, only $N$ values are needed to characterize $A_{C}:A_{C}=gg^{T}$, where $𝐠$ is a $N\times1$ column vector, meaning $A_{C}$ has rank of $1$. This is a more parsimonious and biophysically plausible scenario for attentional modulation, since in this case the covariance gain $g_{i⁢j}$ of neurons $i$ and $j$ is simply emergent from the attentional modulation of the individual neurons. To test whether $A_{C}$ is low rank we analyzed the V4 population recordings during the visual attention task (Figure 1), specifically measuring $A_{C}$ under the assumption that $A_{C}$ is rank 1:

$$
𝐂^{A}=𝐠𝐠^{T}∘𝐂^{U}.
$$

Equation (2) is a system of $N⁢(N-1)/2$ equations of the form $c_{i⁢j}^{A}=g_{i}⁢g_{j}⁢c_{i⁢j}^{U}$ in $N$ unknowns $𝐠=[g_{1},…⁢g_{N}]^{T}$ (we only consider $i\neqj$ to exclude variance modulation from our analysis). For $N>3$ this is an overdetermined system, and we solve for $𝐠$ using a nonlinear equation solver. Let $𝐠^$ be the optimal solution obtained by the solver (measured as a minimization of the $L^{2}$-norm of the error; see Methods: objfxn). Then $C^^{A}:=𝐠^⁢𝐠^^{T}∘C^{U}$ provides an approximation to the attended covariance matrix. In an example data set from a single recording session with $N=39$ units, the correlation coefficient $ρ$ of the actual attended covariance values from $𝐂^{𝐀}$ versus the approximated attended covariance values from $C^^{A}$ was $0.77$ (Figure 2c). A shuffled $𝐂^{𝐀}$ matrix provides a reasonable null model, and the example data set produces the lower bound correlation $ρ_{shuf}=0.22$ (Figure 2d; see Materials and methods: Shuffled covariance matrices). Finally, a Poisson model that perfectly decomposes as Equation (2), yet sampled with the same number of trials as in the experiment, gives an upper bound for the rank one structure, the example data yields $ρ_{ub}=0.90$ (Figure 2e; see Materials and methods: Upper bound covariance matrices). In total, the combination of $ρ$, $ρ_{shuf}$, and $ρ_{ub}$ (Figure 2f) suggests that the rank one model of attention modulation of covariance $A_{C}$ is well justified.

We applied this analysis to 21 recording sessions from the right hemisphere of one monkey (Figure 2g). For most of the recording sessions ρ is closer to ρub than ρshuf. The averaged performance of all sessions for both hemispheres of two monkeys generally agreed with this trend (Figure 2h). We normalized ρ and ρshuf by ρub for each session to better compare different sessions that were subject to day-to-day variations outside of the experimenter’s control, such as the task performance or the internal state of the monkey. To further validate our model we show the distribution of gis computed from the entire data set (Figure 3a). The majority of gi values are less than one, consistent with ⟨CovA⟩trials < ⟨CovU⟩trials (Figure 1c). Further, there was little relation between the attentional modulation of firing rates, measured by riA/riU, and the attentional modulation of covariance through gi (Figure 3b). This indicates that the circuit modulation of firing rates and covariance are not trivially related to one another (Doiron et al., 2016).

![Figure 3.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig3-v3.jpg)

**Figure 3.:** (a) Distribution of covariance gains $g_{i}$ computed from the entire data set. (b) The relation between covariance $g_{i}$ and the attention mediated modulation of firing rates $r_{i}^{A}/r_{i}^{U}$. The correlation coefficients between the data sets were $0.036$ and $0.051$ for the right and left hemispheres, respectively.

We additionally tested the validity of our model in Equation (2) with a leave-one-out cross-validation analysis (see Materials and methods: Leave-one-out cross-validation). We accurately predicted an omitted covariance $C_{i⁢j}^{A}$ (Figure 2i and j), consistent with our original analysis (Figure 2g and h). The individual session-by-session performance values for both the standard and leave-one-out setups are provided (Appendix: Model performance for all monkeys and hemispheres).

Finally, we investigated to what extent the actual value of the covariance gain $g_{i}$ of neuron $i$ depends on the population of neurons in which it was computed. We solved the system of equations $C_{i⁢j}^{A}=g_{i}⁢g_{j}⁢C_{i⁢j}^{U}$ using covariance matrices computed from recordings from distinct sets of neurons, overlapping only by neuron $i$. This gives two estimates of $g_{i}$, that nevertheless agreed largely with one another (Appendix: Low-dimensional modulation is intrinsic to neurons). This supported the hypothesis that covariance gain $g_{i}$ is an intrinsic property of neuron $i$.

The standard and cross-validation tests verify that the low-rank model of attentional modulation defined in Equation (2) explains between $66$ and $82%$ (standard), or $56$ and $77%$ (cross-validation) of the data. Taking this to be a positive result, we conclude that the covariance gain modulation depends largely on the modulation of individual neurons.

### Network requirements for attentional modulation

Having described attentional modulation statistically our next goal is to develop a circuit model to understand the process mechanistically. Consider a network of $N$ coupled neurons, and let the spike count from neuron $i$ on a given trial be $y_{i}$. The network output has the covariance matrix $𝐂$ with elements $c_{i⁢j}=Cov⁢(y_{i},y_{j})$. In this section we identify the minimal circuit elements so that the attentional mapping $A_{C}:C^{U} ↦ C^{A}$ satisfies the following two conditions (on average):

C1: $c_{i⁢j}^{A}=g_{i}⁢g_{j}⁢c_{i⁢j}^{U}$ ; attentional modulation of covariance is rank one (Figure 2).

C2: $g_{i} < 1$ ; spike count covariance decreases with attention (Figure 1).

What follows is only a sketch of our derivation (a complete treatment is given in Appendix: Network requirements for attentional modulation).

If inputs are weak then $y_{i}$ can be described by a linear perturbation about a background state (Ginzburg and Sompolinsky, 1994; Doiron et al., 2004; Trousdale et al., 2012):

$$
y_{i}=y_{i⁢B}+L_{i}⁢(\sumk=1NJ_{i⁢k}⁢y_{k}+ξ_{i}).
$$

Here $y_{i⁢B}$ is the background activity of neuron $i$, $J_{i⁢k}$ is the coupling strength from neuron $k$ to $i$, and $L_{i}$ is the input-to-output gain of neuron $i$. In addition to internal coupling we assume a source of external fluctuations $ξ_{i}$ to neuron $i$. Here $y_{i}$, $y_{i⁢B}$, and $ξ_{i}$ are random variables that vary across trials. The trial-averaged firing rate of neuron $i$ is $r_{i}=⟨y_{i}⟩/T$ (where $⟨⋅⟩$ denotes averaging over trials of length $T$). The background state has variability $b_{i}=Var(y_{iB})$ which we assume to be independent across neurons, meaning the background network covariance is $B=diag(b_{i})$. Finally, the external fluctuations have covariance matrix $𝐗$ with element $x_{ij}=Cov(ξ_{i},ξ_{j})$.

Motivated by our analysis of population recordings (Figure 2) we study attentional modulations that target individual neurons. This amounts to considering only $A_{r}:r_{i}^{U} ↦ r_{i}^{A}$ and $A_{L}:L_{i}^{U} ↦ L_{i}^{A}$. Additionally, we assume that any model of attentional modulation must result in $r_{i}^{A} > r_{i}^{U}$ (Figure 1b). A widespread property of both cortical pyramidal cells and interneurons is that an increase of firing rate $r_{i}$ causes an increase of input-output gain $L$ (Cardin et al., 2007), thus we will also require $L^{A} > L^{U}$.

Spiking covariability in recurrent networks can be due to internal interactions (through $J_{i⁢k}$) or external fluctuations (through $ξ_{i}$), or both (Ocker et al., 2017). Networks with unstructured connectivity have internally generated covariability that vanishes as $N$ grows. This is true if the connectivity is sparse (van Vreeswijk and Sompolinsky, 1998), or dense having weak synapses where $J_{i⁢k}∼1/N$ (Trousdale et al., 2012) or strong synapses where $J_{i⁢k}∼1/\sqrt{N}$ combined with a balance between excitation and inhibition (Renart et al., 2010; Rosenbaum et al., 2017). In these cases spiking covariability requires external fluctuations to be applied and subsequently filtered by the network. We follow this second scenario and choose $𝐗$ so as to provide external covariability to our network.

Recent analysis of cortical population recordings show that the shared spiking variability across the population can be well approximated by a rank one model of covariability (Kelly et al., 2010; Ecker et al., 2014; Lin et al., 2015; Ecker et al., 2016; Rabinowitz et al., 2015; Whiteway and Butts, 2017) (we remark that Rabinowitz et al., 2015 analyzed the same data set that we have in Figures 1 and 2). Thus motivated we take the external fluctuations $𝐗$ to be rank one with $x_{i⁢j}=x_{i}⁢x_{j}$, reflecting a single source of global external variability $ξ$ with unit variance (neuron $i$ receives $ξ_{i}=x_{i}⁢ξ$). Combining this assumption with the linear ansatz in Equation (3) yields:

$$
𝐂≈((𝐈-𝐊)^{-1}⁢𝐋𝐱)⁢((𝐈-𝐊)^{-1}⁢𝐋𝐱)^{T}=𝐜𝐜^{T},
$$

where matrix $𝐊$ has element $K_{i⁢j}=L_{i}⁢J_{i⁢j}$ and $L=diag(L_{i})$. We have also defined the vectors $𝐱=[x_{1},…,x_{N}]^{T}$ and $𝐜=[c_{1},…,c_{N}]^{T}$ with $c_{i}=((𝐈-𝐊)^{-1}⁢𝐋𝐱)_{i}$. In total, the output covariability $𝐂$ will simply inherit the rank of the input covariability $𝐗$. Attentional modulation affects $c_{i}$ through $𝐊$ and $𝐋$ and we easily satisfy condition $𝐂𝟏$ with $g_{i}=c_{i}^{A}/c_{i}^{U}$.

What remains is to find constraints on $𝐉$ and the attentional modulation of $𝐋$ that satisfy condition $𝐂𝟐$. Let us consider the case where $c_{i}^{U},c_{i}^{A} > 0$ so that condition $𝐂𝟐$ is satisfied when $c_{i}^{A}−c_{i}^{U} < 0$. For the sake of mathematical simplicity let us separate the population into $q⁢N$ excitatory neurons and $(1-q)⁢N$ inhibitory neurons ($0 < q < 1$). Let all excitatory (inhibitory) neurons project with synaptic strength $J_{E}$ ($-J_{I}$), have gain $L_{E}$ ($L_{I}$), and receive the external inputs of strength $x_{E}$ ($x_{I}$). Finally, let the probability for all connections be $p$, and consider only weak connections ($J∝1/N$ and $N$ large) so that we can ignore the influence of polysynaptic paths in the network (Pernice et al., 2011; Trousdale et al., 2012). Then the attentional modulation of an excitatory neuron decomposes into:

$$
c_{E}^{A}−c_{E}^{U}=(L_{E}^{A}−L_{E}^{U})x_{E}⏟direct external input+(L_{E}^{A}−L_{E}^{U})qpNJ_{E}x_{E}⏟\frac{external input filtered}{through the excitatory population}−(L_{I}^{A}−L_{I}^{U})(1−q)pNJ_{I}x_{I}⏟\frac{external input filtered}{through the inhibitory population}.
$$

The first term is the direct transfer of the external fluctuations, and the second and third terms are indirect transfer of external fluctuations via the excitatory and inhibitory populations, respectively. Recall that $L^{A}−L^{U} > 0$, meaning that for $c_{E}^{A}−c_{E}^{U} < 0$ to be satisfied we require the third term to outweigh the combination of the first and second terms. In other words, the inhibitory population must experience a sizable attentional modulation. A similar cancelation of correlations by recurrent inhibition has been recently studied in a variety of cortical models (Renart et al., 2010; Tetzlaff et al., 2012; Ly et al., 2012; Doiron et al., 2016; Rosenbaum et al., 2017).

In the above we considered weak synaptic connections where $J_{i⁢j}∼1/N$. Rather, if we scale $J_{i⁢j}∼1/\sqrt{N}$, as would be the case for classical balanced networks (van Vreeswijk and Sompolinsky, 1998), then for very large $N$ the solution no longer depends upon the gain $L$. Finite $N$ or the inclusion of synaptic nonlinearities through short term plasticity (Mongillo et al., 2012) may be necessary to satisfy condition $𝐂𝟐$ with large synapses. Furthermore, the large synaptic weights associated with $J_{i⁢j}∼1/\sqrt{N}$ do not allows us to neglect polysynaptic paths, as is needed for Equation (5). Extending our analysis to networks with balanced scaling will be the focus of future work.

In summary our analysis has identified two circuit features that allow recurrent networks to capture conditions $𝐂𝟏$ and $𝐂𝟐$ for attentional modulation. First, the network must be subject to a global source of external fluctuations that dominates network covariability ($𝐂𝟏$). Second, the network must have recurrent inhibitory connections that are subject to a large attentional modulation ($𝐂𝟐$).

### Mean field model of attention

We next apply the intuition gained in the preceding section to propose a cortical model that captures key neural correlates of attentional modulation. We model V4 as a recurrently coupled network of excitatory and inhibitory leaky integrate-and-fire model neurons (Tetzlaff et al., 2012; Ledoux and Brunel, 2011; Trousdale et al., 2012; Doiron et al., 2004) (Figure 4a). In addition to recurrent synaptic inputs, each neuron receives private and global sources of external fluctuating input (Figure 4b). The global noise is an attention-independent source of input correlation that the network filters and transforms into network-wide output spiking correlations (Figure 4c).

![Figure 4.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig4-v3.jpg)

**Figure 4.:** (a) Recurrent excitatory-inhibitory network subject to private and shared fluctuations as well as top-down attentional modulation. (b) Example voltage trace from a LIF model neuron in the network. Top tick marks denote spike times. (c) Spike time raster plot of the spiking activity from the model network. (d) Population-averaged firing rate $r_{E}⁢(t)$ of the excitatory population. Left: frequency distribution of population-averaged firing rate. (e) Transfer function $f_{E}$ between the effective input and the firing rate for a model excitatory neuron. The red segment represents the attentional shift in effective input and hence firing rate. (f), Same as e, but for the inhibitory population. (g) Attention as a path through ($r¯_{E}$,$r¯_{I}$) space, and equivalently through ($I_{E}^{eff}$, $I_{I}^{eff})$ space.

While the linear response theory introduced in Equation (3) is well suited to study large networks of integrate-and-fire neurons driven by weakly correlated inputs (Tetzlaff et al., 2012; Ledoux and Brunel, 2011; Trousdale et al., 2012; Doiron et al., 2004), the analysis offers little analytic insight. Instead, we consider the instantaneous activity across population $\alpha:r_{a}(t)=\frac{1}{N_{\alpha}}\sumiyi\alpha(t)$, where $y_{i⁢\alpha}⁢(t)$ is the spike train from neuron $i$ of population $\alpha$ and $N_{\alpha}$ is the population size ($\alpha=E$ or $I$). This approach reduces the model to just the two dynamic variables, the excitatory population rate $r_{E}⁢(t)$ and the inhibitory population rate $r_{I}⁢(t)$ ($r_{E}⁢(t)$ is shown in Figure 4d). Despite this severe reduction the model retains the key ingredients for attentional modulation identified in the previous section – recurrent excitation and inhibition combined with a source of global fluctuations.

We take the population sizes to be large and consider a phenomenological dynamic mean field (Tetzlaff et al., 2012; Ledoux and Brunel, 2011) of the cortical network (see Materials and methods: Mean field model):

$$
\tau_{E}\frac{dr_{E}}{dt}=−r_{E}+f_{E}(\mu_{E}+J_{EE}r_{E}−J_{EI}r_{I}+\sigma_{E}ξ(t)),\tau_{I}\frac{dr_{I}}{dt}=−r_{I}+f_{I}(\mu_{I}+J_{IE}r_{E}−J_{II}r_{I}+\sigma_{I}ξ(t)).
$$

The function $f_{\alpha}$ is the input-output transfer of population $\alpha$, taken to be the mean firing rate for a fixed input (Figure 4e for the $E$ population and Figure 4f for the $I$ population). The parameter $J_{\alpha⁢\beta}$ is the coupling strength from population $\beta$ to population $\alpha$. Finally, $\mu_{\alpha}$ and $\sigma_{\alpha}$ are the respective strengths of the mean input and the global fluctuation $ξ⁢(t)$ to population $\alpha$ (throughout $ξ⁢(t)$ has a zero mean). To simplify our exposition we take symmetric coupling $J_{E⁢E}=J_{I⁢E}≡J_{E}$ and $J_{E⁢I}=J_{I⁢I}≡J_{I}$ and symmetric timescales $\tau_{E}=\tau_{I}(=1)$. We set the recurrent coupling so that the model has a stationary mean firing rate ($r¯_{E},r¯_{I}$), about which $ξ⁢(t)$ induces fluctuations in $r_{E}⁢(t)$ and $r_{I}⁢(t)$.

Attention is modeled as a top-down influence on the static input: $\mu_{\alpha}=\mu_{\alpha⁢B}+A⁢Δ⁢\mu_{\alpha}$. Here $\mu_{\alpha⁢B}$ is a background input, the parameter $A$ models attention with $A=0$ denoting the unattended state and $A=1$ the fully attended state, and $Δ\mu_{\alpha} > 0$ is the increase in $\mu_{\alpha}$ due to attention. We note that the choice of representing the unattended state by $A=0$ and the attended state by $A=1$ is only due to convenience, and is not meant to make any statement about particular bounds on these states. In this model attention simply increases the excitability of all of the neurons in the network (Figure 4a). This modulation is consistent with the rank one structure of attentional modulation in the data (Figure 2), since $\mu_{\alpha}$ is a single neuron property. The attention-induced increase in $(\mu_{E},\mu_{I})$ causes an increase in the mean firing rates $(r¯_{E},r¯_{I})$ (red paths in Figure 4e,f), consistent with recordings from putative excitatory (McAdams and Maunsell, 2000; Reynolds et al., 1999) and inhibitory neurons (Mitchell et al., 2007) in visual area V4. Since $f_{\alpha}$ is a simple rising function then there is a unique mapping of an attentional path in $(\mu_{E},\mu_{I})$ space to a path in $(r¯_{E},r¯_{I})$ space (Figure 4g).

In total, our population model has the core features required to satisfy Conditions C1 and C2 of the previous section. We next use our mean field model to investigate how attentional paths in $(r¯_{E},r¯_{I})$ space affect population spiking variability.

### Attention modulates population variability

The global input $ξ⁢(t)$ causes fluctuations about the network stationary state: $r_{\alpha}⁢(t)=r¯_{\alpha}+\delta⁢r_{\alpha}⁢(t)$. The fluctuations $\delta⁢r_{\alpha}⁢(t)$ are directly related to coordinated spiking activity in population $\alpha$. In particular, in the limit of large $N_{\alpha}$ we have that $V_{E}≡Var(r_{E})∝⟨Cov(y_{i},y_{j})⟩$, where the expectation is over $(i,j)$ pairs in the spiking network. Thus, in our mean field network we require attentional modulation to decrease population variance $V_{E}$.

For sufficiently small $\sigma_{\alpha}$ the fluctuations $\delta⁢r_{E}⁢(t)$ and $\delta⁢r_{I}⁢(t)$ obey linearized mean field equations (see Materials and methods: Mean field model, Equation (17)). The linear system is readily analyzed and we obtain the population variance $V_{E}$ computed over long time windows (see Materials and methods: Computing $V_{E}$):

$$
V_{E}=[\frac{L_{E}⁢(J_{I}⁢L_{I}⁢(\sigma_{E}-\sigma_{I})+\sigma_{E})}{1+J_{I}⁢L_{I}-J_{E}⁢L_{E}}]^{2}.
$$

Here $L_{\alpha}≡f_{\alpha}^{′}$ is the response gain of neurons in population $\alpha$. Equation (7) shows that $V_{E}$ depends directly on $L_{\alpha}$, and we recall that $L_{\alpha}$ changes with attention (the slope of $f_{\alpha}$ in Figure 4e,f). Thus, while the derivation of $V_{E}$ requires linear fluctuations about a steady state, attentional modulation samples the nonlinearity in the transfer $f_{\alpha}$ by changing the state about which we linearize. Any attention-mediated change in $V_{E}$ is not obvious since both $L_{I}^{A} > L_{I}^{U}$ and $L_{E}^{A} > L_{E}^{U}$, meaning that both the numerator and denominator in Equation (7) will change with attention.

We explore VE by sweeping over (r¯E, r¯I) space (Figure 5a). When the network has high r¯E and low r¯I then VE is large, while VE is low for the opposite case of high r¯I and low r¯E. Along our attention path rE increases while VE decreases (Figure 5b), satisfying our requirements for attentional modulation. The attention path that we highlight is just one potential path that reduces population variability, however all paths which reduce VE share a large attention-mediated recruitment of inhibition. If we start with the unattended state (turquoise dot in Figure 5c) we can label all (ΔμE > 0,ΔμI > 0) points that have a smaller population variance than the unattended point (light green region in Figure 5c). These modulations all share that ΔμI > ΔμE (Figure 5c, green region is below the Δ⁢μE=Δ⁢μI line). While the absolute comparison between Δ⁢μE and Δ⁢μI may depend on model parameters, a robust necessary feature of top-down attentional modulation is that it must significantly recruit the inhibitory population. This observation is a major circuit prediction of our model.

![Figure 5.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig5-v3.jpg)

**Figure 5.:** (a) An attentional path in excitatory-inhibitory firing rate space for which the population variance decreases. Colored contours define iso-lines of population variance in increments of $10$ (sp/s)$^{2}$. The attentional path links the unattended state ($A=0$; turquoise point) to the attended state ($A=1$, orange point). (b) Variance values as a function of the attentional path defined in a. (c) The modulation from an unattended state (origin) to an attended state over the input space ($Δ⁢\mu_{E},Δ⁢\mu_{I}$). Solid black line marks where $V_{E}$ remains unchanged, and the green region where $ΔV_{E}=Var^{A}(r_{E})−Var^{U}(r_{E})$ is less than zero. (d) The eigenvalue $(\lambda)$ along the attentional path. With increased attention it becomes more negative, indicating that the state $(r¯_{E}$, $r¯_{I})$ is more stable. e, Autocovariance function of the excitatory population rate $r_{E}⁢(t)$ in the attended and unattended state (computed using Equation (19)).

An intuitive way to understand inhibition’s role in the decrease in population variance is through the stability analysis of the mean field equations. The eigenvalues of the linearized system are $\lambda_{1}=−1−J_{I}L_{I}+J_{E}L_{E} < 0$ and $\lambda_{2}=-1$ (see Materials and methods: Mean field model, Equation (18)). Note that the denominator of the population variance (Equation 7) equals the square of the eigenvalue product $\lambda_{1}⁢\lambda_{2}=1+J_{I}⁢L_{I}-J_{E}⁢L_{E}$. The stability of the network activity is determined by $\lambda_{1}$; the more negative $\lambda_{1}$, the more stable the point $(r¯_{E},r¯_{I})$, and the better the network dampens the perturbations about the point due to input fluctuations $ξ⁢(t)$. The decrease of $\lambda_{1}$ along the example attention path is clear (Figure 5d), and overcomes the increase in the numerator of $V_{E}$ due to increases in $L_{E}$ and $L_{I}$. The enhanced damping is why $V_{E}$ decreases, explicitly seen in the steeper decline of the excitatory population autocovariance function in the attended compared to the unattended state (Figure 5e).

This enhanced stability due to recurrent inhibition is a reflection of inhibition canceling population variability provided by external fluctuations and recurrent excitation (Renart et al., 2010; Tetzlaff et al., 2012; Ozeki et al., 2009). Indeed, taking the coupling $J$ to be weak allows the expansion $(1+J_{I}⁢L_{I}-J_{E}⁢L_{E})^{-2}≈1+2⁢J_{E}⁢L_{E}-2⁢J_{I}⁢L_{I}$ in Equation (7), so that the attention mediated increase in $L_{I}$ reduces population variance through cancellation, as in Equation (5). However, this expansion is not formally required to compute the eigenvalues $\lambda_{1}$ and $\lambda_{2}$, and these measure the stability of the firing rate dynamics. We mention the expansion only to compare to the original motivation for inhibition.

The expression for VE given above (Equation 7) assumes a symmetry in the network coupling, namely that JE⁢E=JI⁢E≡JE and JE⁢I=JI⁢I≡JI. This allowed VE to be compactly written, facilitating the analysis of how attention affects both the numerator and denominator of Equation (7). However, the linearization of the mean field equations and the subsequent analysis of population variability do not require this assumption (see Materials and methods: Mean field model Equations (18–20)). To explore the robustness of our main result we let JI⁢E=α⁢JE and JI⁢I=β⁢JI, thereby breaking the coupling symmetry for α,β≠1. The reduction in VE with attention is robust over a large region of (α,β) (Figure 6a, green region). Focusing on selected (α,β) pairings within the region where VE decreases shows that the attentional path identified for the network with coupling symmetry produces qualitatively similar behavior in the more general network (compare Figure 5c to Figure 6b–e). In total, the inhibitory mechanism for attention mediated reduction in population variability is robust to changes in the recurrent coupling with the network.

![Figure 6.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig6-v3.jpg)

**Figure 6.:** (a) Sweep over $\alpha=J_{E⁢E}/J_{I⁢E}$ and $\beta=J_{E⁢I}/J_{I⁢I}$ space (with $J_{E⁢E}$ and $J_{E⁢I}$ fixed) labeling the region where $Δ⁢V_{E}=V_{E}^{U}-V_{E}^{A}$ is positive (grey) and negative (green). (b–e) Attentional path in excitatory-inhibitory firing rate space. The colored contours are as in Figure 5a. All calculations are done using Equations (18–20).

While the reduced mean field equations are straightforward to analyze, a similar attenuation of pairwise covariance $Cov(y_{i},y_{j})$ along the same attentional path occurs in the LIF model network (Appendix: Spiking network). Using linear response analysis for the spiking network we can relate the effect of inhibition to previous work in spiking networks (Renart et al., 2010; Tetzlaff et al., 2012; Ly et al., 2012; Doiron et al., 2016). In particular, the attention-mediated decrease of $Cov(y_{i},y_{j})$ occurs for a wide range of timescale, ranging as low as 20 ms. However, for short timescales that match the higher gamma frequency range (approximately 60–70 Hz) this attentional modulation increases $Cov(y_{i},y_{j})$ (Appendix 1—figure 6). This finding is consistent with reports of attention-mediated increases of neuronal synchrony on gamma frequency timescales(Fries et al., 2001; Buia and Tiesinga, 2008), particularly when inhibitory circuits are engaged (Kim et al., 2016).

### Attention can simultaneously increase stimulus gain and decrease noise covariance

An important neural correlate of attention is enhanced stimulus response gain (McAdams and Maunsell, 2000). The previous section outlines how the recruitment of recurrent inhibitory feedback by attention reduces response variability. However, inhibitory feedback is also a common gain control mechanism, and increased inhibition reduces response gain through the same mechanism that dampens population variability (Sutherland et al., 2009). Thus it is possible that the decorrelating effect of attention in our model may also reduce stimulus response gain as well, which would make the model inconsistent with experimental data.

To insert a bottom-up stimulus $s$ in our model we let the attention-independent background input have a stimulus term: $\mu_{\alpha⁢B}=k_{\alpha}⁢s+\mu^_{\alpha⁢B}$. Here $k_{\alpha}$ is the feedforward stimulus gain to population $\alpha$ and $\mu^_{\alpha⁢B}$ is the background input that is both attention and stimulus independent. Our model captures a bulk firing rate $r_{E}$ rather than a population model with distributed tuning. Because of this the stimulus $s$ should either be conceived as the contrast of an input, or the population conceived as a collection of identically-tuned neurons (i.e a single cortical column).

Straightforward analysis shows that the stimulus response gain of the excitatory population can be written as (Materials and methods: Computing stimulus response gain):

$$
G_{E}≡\frac{d⁢r¯_{E}}{d⁢s}=\frac{k_{E}⁢\sqrt{V_{E}}}{\sigma_{E}}+\frac{J_{I}⁢L_{E}⁢L_{I}}{1+J_{I}⁢L_{I}-J_{E}⁢L_{E}}⁢(k_{E}-k_{I}).
$$

If $k_{E}=k_{I}$ then $G_{E}∝\sqrt{V_{E}}$, and thus any attentional modulation that reduces population variability will necessarily reduce population stimulus sensitivity. However, for $k_{E} > k_{I}$ the second term in Equation (8) can counteract this effect and decouple stimulus sensitivity and variability modulations.

Consider the example attentional path (Figure 4g) with the extreme choice of kE=1 and kI=0. In this case attention causes an increase in GE (Figure 7a,b), while simultaneously causing a decrease in VE (Figure 5a,b). This is a robust effect, as seen by the region in (r¯E,r¯I) space for which the change in VE from the unattended state is negative, and the change in GE is positive (green region, Figure 7c). Further, for fixed kI the proportion of the gray rectangle that the green region occupies increases with kE > kI (Figure 7d). Thus, the decoupling of attentional effects on population variability and stimulus sensitivity is robust to both attentional path (Δ⁢μE,Δ⁢μI) and feedforward gain (kE,kI) choices. The condition that kE > kI implies that feedforward stimuli must directly target excitatory neurons to a larger degree than inhibitory neurons (or at least the inhibitory neurons subject to attentional modulation). This gives us a complementary prediction to the one from the previous section: while top-down attention favors inhibitory neurons, the bottom-up stimulus favors excitatory neurons.

![Figure 7.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig7-v3.jpg)

**Figure 7.:** Attention model can capture increase in stimulus response gain $G_{E}$ despite decrease in population variance $V_{E}$.(a) Attentional path through ($r¯_{E},r¯_{I}$) space shows an increase in stimulus response gain. The shown path is the same path as in Figure 5. (b) Values of $G_{E}$ along the path depicted in a. (c) The green region in ($r¯_{E},r¯_{I}$) space denotes where $ΔV_{E}=Var^{A}(r_{E})−Var^{U}(r_{E}) < 0$ and $ΔG_{E}=G_{E}^{A}−G_{E}^{U} > 0$. Black lines are iso-lines of covariance and gain, along which those quantities do not change. (d) Percent area of the green region in c out of a constant rectangle, as the feedforward stimulus gain $k_{E}$ increases, with $k_{I}=0.2$ held constant.

In total, our model of attentional modulation in recurrently coupled excitatory and inhibitory cortical networks subject to global fluctuations satisfies three main neural correlates of attention: (1) increase in excitatory firing rates and in (2) stimulus-response gain, with a (3) decrease in pairwise excitatory neuron co-variability.

### Impact of attentional modulation on neural coding

Attention serves to enhance cognitive performance, especially on discrimination tasks that are difficult (Moore and Zirnsak, 2017). Thus, it is expected that the attention-mediated reduction in population variability and increase in stimulus response gain subserve an enhanced stimulus estimation (Cohen and Maunsell, 2009; Ruff and Cohen, 2014). In this section we investigate how the attentional modulation outlined in the previous sections affects stimulus coding by the population.

As mentioned above our simplified mean field model (Equation 6) considers only a bulk response, where any individual neuron tuning is lost. As such a proper analysis of population coding is not possible. Nonetheless, our model has two basic features often associated with enhanced coding, decreased population variability (Figure 5) and increased stimulus-response gain (Figure 7).

Fisher information (Averbeck et al., 2006; Beck et al., 2011) gives a lower bound on the variance of a stimulus estimate constructed from noisy population responses, and is an often used metric for population coding. The linear Fisher information (Beck et al., 2011) $FI_{E⁢I}$ computed from our two-dimensional recurrent network is:

$$
FI_{EI}=[G_{E}G_{I}][V_{E}C_{EI}C_{EI}V_{I}]^{−1}[G_{E}G_{I}]=constant
$$

Here $V_{\alpha}=Var(r_{\alpha})$, $G_{\alpha}=d⁢r¯_{\alpha}/d⁢s$, and $C_{EI}=Cov(r_{E},r_{I})$. The important result is that $FI_{E⁢I}$ is invariant with attention, meaning that attention does not increase the network’s capacity to estimate the stimulus $s$.

While the proof of Equation (9) is straightforward and applies to our recurrent excitatory-inhibitory population (see Materials and methods: Fisher information), the invariance of the total information FE⁢I with attention is most easily understood by analogy with an uncoupled, one-dimensional excitatory population (Figure 8a). Without coupling, the input to the population is simply kE⁢s+σE⁢ξ⁢(t), which is then passed through the firing rate nonlinearity fE. In this case the gain is GE=kE⁢LE, and assuming a linear transfer the population variance is VE=σE2⁢LE2. In total the linear Fisher information from the uncoupled population is then:(10)F⁢IEuc=GE2VE=(kE⁢LE)2σE2⁢LE2=kE2σE2.

![Figure 8.](https://cdn.elifesciences.org/articles/23978/elife-23978-fig8-v3.jpg)

**Figure 8.:** Attention improves stimulus estimation by the excitatory population embedded within excitatory ($E$)-inhibitory ($I$) network.(a) Top: For a uncoupled excitatory population, the stimulus response gain $G_{E}$ increases with attention. Turquoise: unattended state; orange: attended state. Bottom: Population variance $V_{E}$ increases with attention. Stimulus-response curves same as above. Input variance is computed from all input to a population, including external noise and recurrent coupling. The Fisher information for the uncoupled $E$ population is constant with attention because the squared gain $G_{E}^{2}$ and variance $V_{E}$ increase proportionally (b) Same as (a) but for the $E$ population within the $E-I$ network. Top: $G_{E}$ increases with attention. Bottom: $V_{E}$ decreases with attention, because the net input variance of the $E$ population decreases with attention. (c) Total Fisher information for coupled E-I populations is constant with attention. By contrast, the Fisher information of the excitatory component $FI_{E}$ increases with attention.

The proportion $L_{E}^{2}$ by which attention increases the squared gain (Figure 8a, top) is exactly matched by the attention related increase in population variance (Figure 8a, bottom), resulting in cancellation of any attention-dependent terms in $FI_{E}$.

The majority of projection neurons in the neocortex are excitatory, so we now consider the stimulus estimation from a readout of only the excitatory population. Combining our previous results we obtain:

$$
FI_{E}=\frac{G_{E}^{2}}{V_{E}}=\frac{(J_{I}⁢L_{I}⁢(k_{E}-k_{I})+k_{E})^{2}}{\sigma_{E}^{2}-J_{I}^{2}⁢L_{I}^{2}⁢(\sigma_{E}⁢\sigma_{I}-\sigma_{E}^{2}-\sigma_{I}^{2})-2⁢J_{I}⁢L_{I}⁢\sigma_{E}⁢(\sigma_{I}-\sigma_{E})}.
$$

Restricting the readout to be from only the excitatory population drastically reduces the total information (compare $FI_{E⁢I}$ to $FI_{E}$ in Figure 8c). As with the uncoupled population the response gain $G_{E}$ of the excitatory neurons in the coupled population increases with attention (Figure 8b, top). Yet unlike the uncoupled population the net input variability to the $E$ population is reduced by attention through a cancelation of the external variability $ξ⁢(t)$ via inhibition (Figure 8b, bottom). These two components combine so that despite $FI_{E} < FI_{EI}$, we have that $FI_{E}$ does increase with attention (Figure 8c). In sum, even though the total stimulus information in the network does not change with attention, the amount of information extractable from the excitatory population increases, which could lead to improved downstream stimulus estimation in the attended state.

## Discussion

Using population recordings from visual area V4 we identified rank one structure in the mapping of population spike count covariability between unattended and attended states. We used this finding to motivate an excitatory-inhibitory cortical circuit model that captures both the attention-mediated increases in the firing rate and stimulus response gain, as well as decreases in noise correlations. Our model accomplishes this with only an attention dependent shift in the overall excitability of the cortical population, in contrast to a scheme where distinct biophysical mechanisms would be responsible for respective firing rate and noise correlations modulations. The model makes two key predictions about how stimulus and modulatory inputs are distributed over the excitatory-inhibitory cortical circuit. First, top-down attentional signals must affect inhibitory neurons more than excitatory neurons to allow a better damping of global fluctuations in the attended state. Second, bottom-up stimulus information must be biased towards excitatory cells to permit higher gain in the attended state. In total, the increased response gain and decreased correlations enhance the flow of information when the readout is confined to the excitatory population.

### Candidate physiological mechanisms for attentional modulation

Our model does not consider a specific type of inhibitory neuron, and rather models a generic recurrent excitatory-inhibitory circuit. However, inhibitory circuits in cortex are complex, with at least three distinct interneuron types being prominent in many areas: parvalbumin- (PV), somatostatin- (SOM), and vasointestinal peptide-expressing (VIP) interneurons (Rudy et al., 2011; Pfeffer et al., 2013; Kepecs and Fishell, 2014). In mouse visual cortex, both SOM and PV cells form recurrent circuits with pyramidal cells, with PV cells having stronger inhibitory projections to pyramidal cells than those of SOM cells (Pfeffer et al., 2013). Furthermore, PV and SOM neurons directly inhibit one another, with the SOM to PV connection being stronger than the PV to SOM connection (Pfeffer et al., 2013). Finally, VIP cells project strongly to SOM cells (Pfeffer et al., 2013) and are activated from inputs outside of the circuit (Lee et al., 2013; Fu et al., 2014), making them an attractive target for modulation. Recent studies in visual, auditory, and somatosensory cortical circuits show that VIP cell activation provides an active disinhibition of pyramidal cells via a suppression of SOM cells (Kepecs and Fishell, 2014). Basal forebrain (BF) stimulation modulates both muscarinic and nicotinic ACh receptors (mAChRs and nAChRs respectively) in a fashion that mimics attentional modulation (Alitto and Dan, 2012). In particular, the recruitment of VIP cell activity in vivo through BF stimulation is strongly dependent on both the muscarinic and nicotinic cholinergic pathways (Alitto and Dan, 2012; Kuchibhotla et al., 2017; Fu et al., 2014), and it has thus been hypothesized VIP cells activation could be an important component of attentional modulation (Alitto and Dan, 2012; Poorthuis et al., 2014).

If we consider the inhibitory population in our model to be PV interneurons then the recruitment of VIP cell activity via top-down cholinergic pathways is consistent with our attentional model in two ways. First, activation of the VIP $→$ SOM $→$ pyramidal cell pathway provides a disinhibition to pyramidal cells, modeled simply as an overall depolarization to pyramidal cells in the attended state (Figure 4). Second, the activation of the VIP $→$ SOM $→$ PV cell pathway disinhibits PV cells, and the strong SOM $→$ PV projection would suggest that the disinhibition is sizable as required by our model (Figure 5c). Finally, a recent study in mouse medial prefrontal cortex reports that identified PV interneurons show an attention related increase in activity, and that optogenetic silencing of PV neurons impairs attentional processing (Kim et al., 2016).

However, our logic is perhaps overly simplistic and neglects the direct modulation of SOM cells via muscarinic and nicotinic cholinergic pathways (Alitto and Dan, 2012; Kuchibhotla et al., 2017) that could compromise the disinhibitory pathways. Further, there is evidence of a direct ACh modulation of PV cells (Disney et al., 2014) as opposed to through a disinhibitory pathway. Finally, there may be important differences across both species (mouse vs. primate) and visual area (V1 vs. V4) that fundamentally change the pyramidal, PV, SOM, and VIP circuit that is understood from mouse V1 (Pfeffer et al., 2013). Future studies in the inhibitory to excitatory circuitry of primate visual cortex, and its attentional modulation via neuromodulation, are required to navigate these issues.

Finally, the simultaneous increase in response gain and decrease in noise correlations with attention requires excitatory neurons to be more sensitive to bottom-up visual stimulus than inhibitory neurons ($k_{E} > k_{I}$, Figure 7). In mouse visual cortex, GABAergic interneurons show overall less stimulus selectivity than pyramidal neurons (Sohya et al., 2007), however this involves both direct feedforward and recurrent contributions to stimulus tuning. While our model simplified the feedforward stimulus gain $k_{E}$ and $k_{I}$ to be constant with attention, it is known that attention also modulates feedforward gain through presynaptic nACh receptors (Disney et al., 2007). Notably, nAChRs are found at thalamocortical synapses onto layer 4 excitatory cells and not onto inhibitory neurons, suggesting that $k_{E}$ would increase with attention while $k_{I}$ would not. Thus, $k_{E}$ should also increase with attention while $k_{I}$ should not, further supporting that $k_{E} > k_{I}$.

### Modeling global network fluctuations and their modulation

Our model considered the source of global fluctuations as external to the network. This choice was due in part to difficulties in producing global, long timescale fluctuations through strictly internal coupling (Renart et al., 2010; Rosenbaum et al., 2017). Our model assumed that the intensity of these external input fluctuation were independent of attention. Rather, attention shifted the operating point of the network such that the transfer of input variability to population-wide output activity was attenuated in the attended state.

Recent analysis of population recordings show that generative models of spike trains that consider gain fluctuations in conjunction with standard spike emission variability capture much of the variability of cortical dynamics (Rabinowitz et al., 2015; Lin et al., 2015). Further, these gain fluctuations are well approximated by a one-dimensional, global stochastic process affecting all neurons in the population (Ecker et al., 2014; Rabinowitz et al., 2015; Lin et al., 2015; Ecker et al., 2016; Engel et al., 2016; Whiteway and Butts, 2017). When these techniques are applied to population recordings subject to attentional modulation, the global gain fluctuations are considerably reduced in the attended state (Rabinowitz et al., 2015; Ecker et al., 2016). Our assumption that external input fluctuations to our network are attention-invariant is consistent with this statistical analysis since it is necessarily constructed from only output activity. Nevertheless, another potential model is that the reduction in population variability is simply inherited from an attention-mediated suppression of the global input fluctuations. Unfortunately, it is difficult to distinguish between these two mechanisms when restricted to only output spiking activity.

However, a model where output variability reductions are simply inherited from external inputs suffers from two criticisms. First, it begs the question: what is the mechanism behind the shift in input variability? Second, our model requires only an increase in the external depolarization to excitatory and inhibitory populations to account for all attentional correlates. An inheritance model would necessarily decouple the attentional mechanisms behind increases in network firing rate (still requiring a depolarization) and the decrease in global input variability. Thus, our model offers a parsimonious and biologically motivated explanation of these neural correlates of attention. Further work dissecting the various external and internal sources of variability to cortical networks, and their attentional modulation, is needed to properly validate or refute these different models.

### Attentional modulation of neural coding through inhibition

Our network model assumed attention-invariant external fluctuations and weak recurrent inputs, permitting a linear analysis of network activity. As a consequence the linear information transfer by the entire population was attention-invariant (Figure 8), because attention modulated the network’s transfer of signal and noise equivalently. However, this invariance was only apparent if the decoder had access to both the excitatory and inhibitory populations. However, most of the neurons in cortex that project between areas are excitatory. When the decoder was restricted to only the activity of the excitatory population then our analysis uncovered two main results. First, the excitatory population carried less information than the combined excitatory-inhibitory activity, suggesting an inherently suboptimal coding scheme used by the cortex. Second, the attention-mediated modulation of the inhibitory neurons increased the information carried by the excitatory population. This agrees with the wealth of studies that show that attention improves behavioral performance on stimulus discrimination tasks.

Determining the impact of population-wide spiking variability on neural coding is complicated (Averbeck et al., 2006; Kohn et al., 2016). A recent theoretical study has shown that noise correlations that limit stimulus information must be parallel to the direction in which population activity encodes the stimulus (Moreno-Bote et al., 2014). The fluctuations in our network satisfy this criteria, albeit trivially since all neurons share the same stimulus input. Indeed, in our network the external inputs appear to the network as $s+x⁢(t)$, meaning that fluctuations from the noise source $x⁢(t)$ are indistinguishable from fluctuations in the stimulus $s$. This is an oversimplified view and assumes that the decoder treats the neurons as indistinguishable from one another, at odds with classic work in population coding (Pouget et al., 2000). Extending our network to include distributed tuning and feature-based recurrent connectivity is a natural next step (Ben-Yishai et al., 1995; Rubin et al., 2015). To do this the spatial scales of feedforward tuning, recurrent projections, external fluctuations, as well as attention modulation must all be specified. It is not clear how noise correlations will depend on these choices yet work in spatially distributed balanced networks shows that solutions can be complex (Rosenbaum et al., 2017).

The role of inhibition in shaping cortical function is a longstanding topic of study (Isaacson and Scanziani, 2011), including recent work showing inhibition can actively decorrelate cortical responses (Renart et al., 2010; Tetzlaff et al., 2012; Ly et al., 2012). Our work gives a concrete example of how this decorrelation can be gated and used to control the flow of information. Of interest are tasks that probe a distributed population where attention again decreases noise correlations between neurons with similar stimulus preference, yet increases noise correlations between cells with dissimilar stimulus preference (Ruff and Cohen, 2014). The circuit mechanisms underlying this neural correlate of attention are unclear. However, there is ample work in understanding how recurrent inhibition shapes cortical activity in distributed populations (Isaacson and Scanziani, 2011), including in models of attentional circuits (Ardid et al., 2007; Buia and Tiesinga, 2008). Adapting our model to include distributed tuning is an important next step and will be a better framework to discuss the coding consequences of the attentional modulation circuits proposed in our study.

## Methods and materials

### Data preparation

Data was collected by from two rhesus monkeys with microelectrode arrays implanted bilaterally in V4 as they performed an orientation-change detection task (Figure 1a) (Cohen and Maunsell, 2009). All animal procedures were in accordance with the Institutional Animal Care and Use Committee of Harvard Medical School. Two oriented Gabor stimuli flashed on and off several times, until one of them changed orientation. The task of the monkey was to then saccade to the stimulus that changed. Each recording session consisted of at least four blocks of trials in which the monkey’s attention was cued to the left or right. We excluded from the analysis instruction trials which occurred at the start of each block to cue the monkey to one side to attend to, catch trials in which the monkey was rewarded just for fixating, and trials in which the monkey did not perform the task correctly. Moreover, the first and last stimulus presentations in each trial were not analyzed, to prevent transients due to stimulus appearance or change from affecting the results. The total number of trials included in the analysis from all the recording sessions was $42,496$. Each trial consisted of between $3$ and $12$ stimulus presentations, of which all but the first and last were analyzed.

Recordings from the left and right hemispheres of each monkey were analyzed separately because the activities of the neurons in opposite hemispheres had near-zero correlations (Cohen and Maunsell, 2009). Neurons in the right hemisphere were considered to be in the attended state when the attentional cue was on the left, and vice-versa. We note that because our criteria for choosing which trials and units to analyze were based on different needs for data analysis compared to the original study (Cohen and Maunsell, 2009) the specific firing rates and covariances differ quantitatively from those previously reported.

In monkey 1, an average of $51.1$ (min $35$, max $80$) units were analyzed from the right hemisphere, and an average of $27.5$ (min $14$, max $56$) units were analyzed from the left hemisphere. From monkey 2, an average of $56.6$ (min $43$, max $71$) units from the right hemisphere, and an average of $37.7$ (min $32$, max $46$) units from the left hemisphere were analyzed. From each recording, spikes falling between $60$ and $260$ ms from stimulus onset were considered for the firing rate analysis, to account for the latency of neuronal responses in V4.

### Comparing change in covariance to change in variance

Let $S^{U}$ be the matrix containing spike counts of the neurons on trials in which they are in the unattended state, and $S^{A}$ the matrix containing spike counts of the neurons on trials in which they are in the attended state. Denote the unattended spike count covariance matrix by $C^{U}=Cov(S^{U})$, and the attended one by $C^{A}=Cov(S^{A})$. Attentional changes in covariance and variance were measured both on average (Figure 1c) and as distributions (Figure 1d). The distributions of the normalized differences

$$
\frac{Cov^{A}−Cov^{U}}{max(|Cov^{A}|,|Cov^{U}|)} and \frac{Var^{A}−Var^{U}}{max(|Var^{A}|,|Var^{U}|)}
$$

reveal a concentration of negative covariance changes, and a distribution of variance changes symmetric about zero. Here, $Cov^{A}$ and $Cov^{U}$ ($Var^{A}$ and $Var^{U}$) are vectors containing covariance (variance) values of the entire data set. Note that the distributions are bounded between $-2$ and $2$ by construction.

### Solving systems of equations by error minimization

When solving systems of the form of Equation (2) in order to quantify the fit of the model, a nonlinear equation solver (fminunc) in MATLAB was used. The solver found minima of an objective function which we defined as the Euclidean norm of the difference of the approximation of the attended covariance matrix and the original attended covariance matrix, in other words, the error of the approximation:

$$
f(g_{1},...,g_{N})=\sqrt{\sumi < j(g_{i}C^{U}(i,j)g_{j}−C^{A}(i,j))^{2}}.
$$

### Shuffled covariance matrices

For finite population sizes ($N < ∞$) we expect our algorithm to extract some low-rank structure between arbitrary covariance matrices. Let $\sqrt{C^{A}}$ be the principal square root of the attended covariance matrix, the unique positive-semidefinite square root of a positive-semidefinite matrix. Consider the symmetric matrix $D=perm(\sqrt{C^{A}})$ computed from the a random permutation of the upper-triangular entries of $\sqrt{C^{A}}$. Finally, let $C_{shuf}^{A}=real(DD)$. The square root-permutation-squaring procedure guarantees a positive-semidefinite matrix, as the square of any matrix is positive-semidefinite. Shuffling removes any relation between $𝐂^{𝐔}$ and $C_{shuf}^{A}$, and any remaining detected structure would be due to finite sampling. The shuffled covariance gain $g^_{shuf}$ provides the prediction $C^_{shuf}^{A}:=g^_{shuf}g^_{shuf}^{T}∘C^{U}$, and $ρ_{shuf}$ measures the relation between $C^_{shuf}^{A}$ and $C_{shuf}^{A}$. Synthetic data shows that as population size $N$ becomes large the coefficient $ρ_{shuf}$ approaches 0 (Appendix: Detected structure in random covariance matrices is a finite-size effect).

### Upper bound covariance matrices

The covariance matrices $𝐂^{𝐔}$ and $𝐂^{𝐀}$ are estimates obtained from a finite number of trials, and any estimation error will compromise the ability to detect rank one structure of $A_{C}$. Here we outline an upper bound for the model performance based on a finite number of trials over which the covariance matrices were originally estimated. Let $C^^{A}:=𝐠^⁢𝐠^^{T}∘C^{U}$ with $𝐠^$ minimizing the $L^{2}$ norm of $C^{A}:=𝐠𝐠^{T}∘C^{U}$. We remark that $C^^{A}$ perfectly decomposes according to the statistical model in Equation (2). We used $C^^{A}$ to generate an artificial set of $N$ correlated Poisson spike counts, using an algorithm based on a latent multivariate gaussian model (Macke et al., 2009). We sampled these population spike counts with a fixed number of trials ($M$) with $D$ be the resulting $M\timesN$ matrix of Poisson samples for each process. Let $C_{ub}^{A}=Cov(D)$ be the 'upper bound' covariance matrix: a finite trial sampling approximation to the perfectly decomposable matrix $C^^{A}$. Finally, we employ our algorithm to give $C^_{ub}^{A}:=g^_{ub}g^_{ub}^{T}C^{U}$, where the vector $g^_{ub}$ minimizes the $L^{2}$ norm of the error.

Since $C^^{A}$ is perfectly decomposable then for $M→∞$ we have $C^_{ub}^{A}=C_{ub}^{A}=C^^{A}$. Thus in the large $M$ limit the coefficient $ρ_{ub}$ between elements of $C^_{ub}^{A}$ and $C_{ub}^{A}$ converges to 1 (Appendix: Performance limited by available number of trials). However, for finite $M$ we have that $ρ_{ub} < 1$, solely due to inaccuracies in estimating $C^^{A}$ with $C_{ub}^{A}$. To account for the possibility of particular strings of realizations $D$ introducing random biases into $C_{ub}^{A}$, we performed the following analysis on $10$ independently generated upper-bound covariance matrices $C_{ub}^{A}$.

### Leave-one-out cross-validation

Instead of solving the system consisting of all Equations (2), we remove one of them. Denote the complete set of equations by $S$, an individual equation as $s_{i⁢j}:={C_{i⁢j}^{A}=g_{i}g_{j}C_{i⁢j}^{U}}$ and the set of equations with one of them removed as $S_{a⁢b}:=S-s_{a⁢b}$. We then solve the system $S_{a⁢b}$. Denote the solution by $𝐠_{a⁢b}$. We can then compare $C_{a⁢b}^{A}$ and $C^_{a⁢b}^{A}=𝐠_{a⁢b}⁢(a)⁢𝐠_{a⁢b}⁢(b)⁢C_{a⁢b}^{U}$. We do this for $max(1000,N(N-1)/2$ possible systems $S_{a⁢b}$. The $ρ$ of the vector of resulting $C_{a⁢b}^{A}$ vs $C^_{a⁢b}^{A}$ values is a measure of how well the system can predict one of its elements, or in other words, how well the structure holds together when one element is taken out. This leave-one-out cross-validation was performed for the shuffled and the upper-bound cases as well.

### Mean field model

The mean spiking activity over the population $\alpha (=E or I)$ is

$$
r_{\alpha}⁢(t)=⟨y_{i⁢\alpha}⁢(t)⟩_{i},
$$

where $y_{i⁢\alpha}⁢(t)=\sum_{j=1}^{n_{i⁢\alpha}}\delta⁢(t-t_{i⁢\alpha}^{j})$ is the spike train of excitatory neuron $i$ of population $\alpha$, $n_{i⁢\alpha}$ is the number of spikes from that neuron, and $t_{i⁢\alpha}^{j}$ is the time of spike $j$. We follow previous studies (Tetzlaff et al., 2012; Ozeki et al., 2009; Ledoux and Brunel, 2011) and consider the firing rate dynamics of the $E$ and $I$ populations given by the system in Equations (6):

$$
\tau_{E}⁢\frac{d⁢r_{E}}{d⁢t}=-r_{E}+f_{E}⁢(\mu_{E⁢B}+A⁢Δ⁢\mu_{E}+J_{E⁢E}⁢r_{E}-J_{E⁢I}⁢r_{I}+\sigma_{E}⁢[\sqrt{1-χ}⁢x_{E}⁢(t)+\sqrt{χ}⁢x⁢(t)]),\tau_{I}⁢\frac{d⁢r_{I}}{d⁢t}=-r_{I}+f_{I}⁢(\mu_{I⁢B}+A⁢Δ⁢\mu_{I}+J_{I⁢E}⁢r_{E}-J_{I⁢I}⁢r_{I}+\sigma_{I}⁢[\sqrt{1-χ}⁢x_{I}⁢(t)+\sqrt{χ}⁢x⁢(t)]).
$$

Here $\mu_{\alpha⁢B}$ is the attention independent drive to population $\alpha$, $A\in[0,1]$ is the attention variable, and $Δ⁢\mu_{\alpha}$ is the maximal drive to population $\alpha$ due to attention. The parameter $J_{\alpha⁢\beta}$ is the coupling from population $\beta$ to populations $\alpha$. The stochastic processes $x_{E}⁢(t)$, $x_{I}⁢(t)$, and $x⁢(t)$ are the global fluctuations applied to the network. The excitatory and inhibitory populations have private fluctuations $x_{\alpha}⁢(t)$ and also common fluctuations $x⁢(t)$ given to both populations; the parameter $χ$ scales the degree of private versus common fluctuations. We perform calculations for arbitrary $χ$ and then take $χ→1$ to match the system given in Equations (6). The total intensity of fluctuations to population $\alpha$ is set by $\sigma_{\alpha}$. These simplified rate equations give an accurate picture of the long-timescale dynamics of networks of coupled spiking neuron models that are in the fluctuation driven regime (Ledoux and Brunel, 2011). The operative timescale reflects a combination of synaptic and membrane integration; since we are interested in spiking covariance over time windows that are much longer than these, we take them to be unity for simplicity.

To give a quantitative match between the equilibrium statistics of the rate equations and the leaky integrate-and-fire (LIF) network simulations we take the transfer function $f$ to be the inverse first passage time of an LIF neuron driven by white noise (Ledoux and Brunel, 2011):

$$
f_{\alpha}(I)=(\tau_{\alpha}\sqrt{\pi}\int_{(−V_{T}+I)/η_{\alpha}}^{(−V_{R}+I)/η_{\alpha}}exp(z^{2})erfc(z)dz)^{−1}.
$$

The parameter ηα is the intensity of the external fluctuations given to the LIF neurons (Appendix: Spiking model). The membrane timescale τ gives the dimensions of 1/s to the firing rate rα. The parameter VT denotes spike threshold while VR is the reset potential. Model parameters are given in Table 1.

**Table 1.**
 Model Parameters.


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
      <td>τ</td>
      <td>Time constants for membrane dynamics</td>
      <td>0.01 s</td>
    </tr>
    <tr>
      <td>VT</td>
      <td>Spike Threshold</td>
      <td>1</td>
    </tr>
    <tr>
      <td>VR</td>
      <td>Spike Reset</td>
      <td>0</td>
    </tr>
    <tr>
      <td>μE</td>
      <td>Excitatory baseline bias</td>
      <td>0.6089</td>
    </tr>
    <tr>
      <td>μI</td>
      <td>Inhibitory baseline bias</td>
      <td>0.5388</td>
    </tr>
    <tr>
      <td>Δ⁢μE</td>
      <td>Attentional modulation of excitatory bias</td>
      <td>0.2624</td>
    </tr>
    <tr>
      <td>Δ⁢μI</td>
      <td>Attentional modulation of inhibitory bias</td>
      <td>0.3608</td>
    </tr>
    <tr>
      <td>JE</td>
      <td>Excitatory coupling constant</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>JI</td>
      <td>Inhibitory coupling constant</td>
      <td>3</td>
    </tr>
    <tr>
      <td>σE</td>
      <td>Amplitude of external noise to E population</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>σI</td>
      <td>Amplitude of external noise to I population</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>c</td>
      <td>Proportion of common noise to E and I populations</td>
      <td>1</td>
    </tr>
    <tr>
      <td>kE</td>
      <td>Sensitivity of E population to stimulus input</td>
      <td>1</td>
    </tr>
    <tr>
      <td>kI</td>
      <td>Sensitivity of I population to stimulus input</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

If the input fluctuations, $x⁢(t)$, $x_{E}⁢(t)$, and $x_{I}⁢(t)$ are white noise processes then the nonlinearity in $f$ makes the stochastic dynamics of $r_{E}⁢(t)$ and $r_{I}⁢(t)$ complicated (non-diffusive). To simply the analysis we consider $x⁢(t)$ as the limiting process from:

$$
\tau_{x}⁢\frac{d⁢x}{d⁢t}=-x+\sqrt{\tau_{x}}⁢ξ_{x}⁢(t),
$$

for $\tau_{x}→0$, with $⟨ξ_{x}⁢(t)⟩=0$ and $⟨ξ_{x}⁢(t)⁢ξ_{x}⁢(t^{′})⟩=\delta⁢(t-t^{′})$. This makes $x⁢(t)$ sufficiently smooth in time (the same is true for $x_{E}⁢(t)$ and $x_{I}⁢(t)$).

We restrict the coupling $J_{\alpha⁢\beta}$ such that for $\sigma_{\alpha}=0$ the equilibrium point $(r¯_{E},r¯_{I})$ is stable and given by:

$$
r¯_{E}=f_{E}(\mu_{EB}+AΔ\mu_{E}+J_{EE}r¯_{E}−J_{EI}r¯_{I}),(16)r¯_{I}=f_{I}(\mu_{IB}+AΔ\mu_{I}+J_{IE}r¯_{E}−J_{II}r¯_{I}).
$$

For sufficiently small $\sigma_{\alpha}$ the fluctuations in population activity about the equilibrium firing rate, $\delta⁢r_{\alpha}⁢(t)=r_{\alpha}⁢(t)-r¯_{\alpha}$, obey the linearized stochastic system:

$$
\tau_{E}\frac{d}{dt}\deltar_{E}=(−1+L_{E}J_{EE})\deltar_{E}−L_{E}J_{EI}\deltar_{I}+L_{E}\sigma_{E}(\sqrt{1−χ}x_{E}(t)+\sqrt{χ}x(t)),(17)\tau_{I}\frac{d}{dt}\deltar_{I}=L_{I}J_{IE}\deltar_{E}−(1+L_{I}J_{II})\deltar_{I}+L_{I}\sigma_{I}(\sqrt{1−χ}x_{I}(t)+\sqrt{χ}x(t)).
$$

Here $L_{\alpha}=\frac{df_{\alpha}}{dI}|_{I=I_{\alpha}^{eff}}$ is the slope of the transfer function $f_{\alpha}$ evaluated at the equilibrium point $I_{\alpha}^{eff}=\mu_{\alpha}+AΔ\mu_{\alpha}+J_{\alphaE}r¯_{E}−J_{\alphaI}r¯_{I}$. Equation (17) is a two dimensional Ornstein-Uhlenbeck process (Gardiner, 2004) that is readily amenable to analysis.

#### Computing VE

In matrix form the system Equation(17) is written as:

$$
\frac{d}{d⁢t}⁢\delta⁢r=M⁢\delta⁢r+D⁢𝐱.
$$

Here $\delta⁢r=[\delta⁢r_{E},\delta⁢r_{I}]$, $𝐱=[x_{E},x_{I},x]$, and

$M=[-1+L_{E}⁢J_{E⁢E}-L_{E}⁢J_{E⁢I}L_{I}⁢J_{I⁢E}-1-L_{I}⁢J_{I⁢I}]$ and $D=[L_{E}⁢\sigma_{E}⁢\sqrt{1-χ}0L_{E}⁢\sigma_{E}⁢\sqrt{χ}0L_{I}⁢\sigma_{I}⁢\sqrt{1-χ}L_{I}⁢\sigma_{I}⁢\sqrt{χ}]$.

The stationary autocovariance function is computed as:

$$
C~(s)=⟨\deltar(t),\deltar(t+s)⟩={exp⁡(Ms)Σ if s > 0Σexp⁡(−M^{T}s) if s\leq0,
$$

where $s$ is a time lag and $Σ=\frac{(DetM)DD^{T}+[M−(TrM)1]DD^{T}[M−(TrM)1]^{T}}{2(TrM)(DetM)}$ is the variance matrix (Det and Tr denote the determinant and trace operations, respectively). Here, $1$ is the $2\times2$ identity matrix.

The covariance between populations $\alpha$ and $\beta$ over long time scales is given by

$$
C⁢(\alpha,\beta)=\int_{-∞}^{∞}C~⁢(s;\alpha,\beta)⁢d⁢s,
$$

where the integration is performed over the appropriate element of the matrix $C~⁢(s)$. In particular, the long timescale variance of the excitatory population is given by (after some algebra):

$$
V_{E}=C⁢(E,E)=\frac{L_{E}^{2}}{(1+J_{I}⁢L_{I}-J_{E}⁢L_{E})^{2}}⁢(J_{I}⁢L_{I}⁢(\sigma_{E}-\sigma_{I})+\sigma_{E})^{2}.
$$

We remark that the long timescale covariance matrix can alternatively be computed from $C=M^{-1}⁢D⁢[M^{-1}⁢D]^{T}$ (Gardiner, 2004). To obtain the compact expression for $V_{E}$ we have assumed symmetric coupling: $J_{I}:=J_{E⁢I}=J_{I⁢I}$, $J_{E}:=J_{E⁢E}=J_{I⁢E}$, and $χ→1$. These are not required for the main results of our study and merely ease the analysis of equations.

#### Computing stimulus response gain

We decompose $\mu_{\alpha⁢B}=k_{\alpha}⁢s+\mu^_{\alpha⁢B}$ and define the gain of population $\alpha$ to stimulus $s$ as $G_{\alpha}=\frac{d⁢r¯_{\alpha}}{d⁢s}=L_{\alpha}⁢\frac{d⁢I_{\alpha}}{d⁢s}$. The term $\frac{d⁢I_{\alpha}}{d⁢s}$ is obtained by differentiating Equations (16)) with respect to $s$:

$$
\frac{d⁢I_{\alpha}}{d⁢s}=k_{\alpha}+J_{E}⁢G_{E}-J_{I}⁢G_{I}.
$$

Solving the system of two equations for $G_{E}$ yields:

$$
G_{E}=\frac{L_{E}⁢(k_{E}+J_{I}⁢L_{I}⁢(k_{E}-k_{I}))}{1+J_{I}⁢L_{I}-J_{E}⁢L_{E}}.
$$

For the sake of compactness we set $\sigma_{E}=\sigma_{I}$ to obtain the result in Equation (8).

### Fisher information

Linear Fisher Information depends on the stimulus response gains and covariance matrix of the excitatory and inhibitory populations:

$$
FI_{EI}=[G_{E}G_{I}][V_{E}C_{EI}C_{EI}V_{I}]^{−1}[G_{E}G_{I}](23)=\frac{G_{E}^{2}V_{I}+G_{I}^{2}V_{E}−2G_{E}G_{I}C_{EI}}{V_{E}V_{I}−C_{EI}^{2}},
$$

When the input correlation $0\leqχ < 1$ we have:

$$
V_{E}=(\frac{L_{E}}{1+J_{I}⁢L_{I}-J_{E}⁢L_{E}})^{2}⁢(J_{I}^{2}⁢L_{I}^{2}⁢(\sigma_{E}^{2}+\sigma_{I}^{2}-2⁢\sigma_{E}⁢\sigma_{I}⁢χ)+2⁢J_{I}⁢L_{I}⁢\sigma_{E}⁢(\sigma_{E}-\sigma_{I}⁢χ)+\sigma_{E}^{2}),
$$



$$
V_{I}=(\frac{L_{I}}{1+J_{I}⁢L_{I}-J_{E}⁢L_{E}})^{2}⁢(J_{E}^{2}⁢L_{E}^{2}⁢(\sigma_{E}^{2}+\sigma_{I}^{2}-2⁢\sigma_{E}⁢\sigma_{I}⁢χ)+2⁢J_{E}⁢L_{E}⁢\sigma_{I}⁢(\sigma_{I}-\sigma_{E}⁢χ)+\sigma_{I}^{2}),
$$

and

$$
C_{EI}=\frac{L_{E}L_{I}}{(1+J_{I}L_{I}−J_{E}L_{E})^{2}}(J_{E}J_{I}L_{E}L_{I}(\sigma_{E}^{2}+\sigma_{I}^{2}−2\sigma_{E}\sigma_{I}c)+J_{E}L_{E}\sigma_{E}(\sigma_{E}−\sigma_{I}χ)−J_{I}L_{I}\sigma_{I}(\sigma_{I}−\sigma_{E}χ)+\sigma_{E}\sigma_{I}χ).
$$

Inserting these expressions and those for $G_{E}$ and $G_{I}$ into Equation (23) and simplifying yields:

$$
FI_{E⁢I}=\frac{2⁢χ⁢k_{E}⁢k_{I}⁢\sigma_{E}⁢\sigma_{I}-k_{E}^{2}⁢\sigma_{I}^{2}-k_{I}^{2}⁢\sigma_{E}^{2}}{(χ^{2}-1)⁢\sigma_{I}^{2}⁢\sigma_{E}^{2}}.
$$

We remark that $FI_{E⁢I}$ is independent of $L_{E}$ and $L_{I}$ and thus independent of attentional modulation.

Notice that we have re-introduced the correlation constant $χ$ into the equations, rather than only considering the limit $χ→1$. If $χ=1$, the excitatory and inhibitory populations are receiving completely identical noise. If this is the case, the correlation cancellation would be perfect, leading to infinite informational content, as can be seen in Equation (27).
