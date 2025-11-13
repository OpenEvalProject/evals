# A stochastic neuronal model predicts random search behaviors at multiple spatial scales in C. elegans

## Authors

- William M Roberts<sup>1</sup>
- Steven B Augustine<sup>2</sup>
- Kristy J Lawton<sup>3</sup>
- Theodore H Lindsay<sup>4</sup>
- Tod R Thiele<sup>5</sup>
- Eduardo J Izquierdo<sup>6</sup>
- Serge Faumont<sup>1</sup>
- Rebecca A Lindsay<sup>7</sup>
- Matthew Cale Britton<sup>8</sup>
- Navin Pokala<sup>9</sup>
- Cornelia I Bargmann<sup>10</sup> ([ORCID: 0000-0002-8484-0618](https://orcid.org/0000-0002-8484-0618))
- Shawn R Lockery<sup>1</sup> ([ORCID: 0000-0001-8535-7989](https://orcid.org/0000-0001-8535-7989)) †

### Affiliations

1. Institute of Neuroscience University of Oregon Eugene United States
2. School of Nursing University of Pennsylvania Philadelphia United States
3. Biology Department Reed College Portland United States
4. Division of Biology and Biological Engineering California Institute of Technology Pasadena United States
5. Department of Biological Sciences University of Toronto Toronto Canada
6. Cognitive Science Program Indiana University Bloomington United States
7. Department of Ophthalmology, The Vision Center Children's Hospital Los Angeles Los Angeles United States
8. Department of Neurology University of Minnesota Minneapolis United States
9. Department of Life Sciences New York Institute of Technology Old Westbury United States
10. Howard Hughes Medical Institute, Rockefeller University New York United States

† Corresponding author

## Abstract

Random search is a behavioral strategy used by organisms from bacteria to humans to locate food that is randomly distributed and undetectable at a distance. We investigated this behavior in the nematode Caenorhabditis elegans, an organism with a small, well-described nervous system. Here we formulate a mathematical model of random search abstracted from the C. elegans connectome and fit to a large-scale kinematic analysis of C. elegans behavior at submicron resolution. The model predicts behavioral effects of neuronal ablations and genetic perturbations, as well as unexpected aspects of wild type behavior. The predictive success of the model indicates that random search in C. elegans can be understood in terms of a neuronal flip-flop circuit involving reciprocal inhibition between two populations of stochastic neurons. Our findings establish a unified theoretical framework for understanding C. elegans locomotion and a testable neuronal model of random search that can be applied to other organisms.

## Introduction

Random search is an evolutionarily ancient set of foraging strategies that evolved as an adaptation to environments in which prey items are undetectable at a distance and occur at unpredictable locations. Rather than attempting to exhaustively search a region of interest, the organism samples the environment at randomly selected points. This is achieved by executing a series of straight-line movements, called 'runs,' terminated at random intervals by sampling episodes during which the organism may or may not find prey. Sampling ends in a reorientation event, called a 'turn,' such that the next run is usually in a different direction from the preceding one. In optimal random foraging strategies the probability distribution of run length is matched to the statistical distribution of isolated food patches or prey items (Viswanathan, 2011), with power law distributions predominating when resources are sparsely distributed and exponential distributions predominating when resources are densely distributed (Humphries et al., 2010; Sims et al., 2012; Humphries et al., 2012).

Random search has been documented in a wide range of species including microorganisms, nematodes, insects, mollusks, fish, birds, and mammals including humans (Viswanathan, 2011; Berg and Brown, 1972; Pierce-Shimomura et al., 1999). In humans this strategy is observed in diverse contexts, from traditional hunter-gatherer societies (Brown et al., 2007; Humphries and Sims, 2014) to technologically enhanced fishing industries (Bertrand et al., 2007). The formal similarities between random search across widely diverse phyla and spatial scales (Viswanathan, 2011) may point to a common mechanism, even in organisms that are highly cognitive. Despite the universality of random search, little is known about its neuronal basis, in part because of the difficulty of recording and manipulating activity in the brain of an unrestrained animal while it explores a large region of space.

The relatively small spatial scale of random search behavior in C. elegans, coupled with the simplicity of its nervous system, provides a unique opportunity to identify the neuronal basis of random search in this species. To the unaided eye, C. elegans search behavior consists of forward runs, each terminated after a variable interval by a briefer period of reverse locomotion, which is also variable in duration (Pierce-Shimomura et al., 1999; Zhao et al., 2003; Wakabayashi et al., 2004), with apparently stochastic switching between these two behavioral states. Reversals are followed by resumption of forward movement that frequently begins with a deep body bend. These bends are highly variable in amplitude and lead to movement in a new direction. Thus, the sequence reverse–forward–deep bend, called a 'pirouette' (Pierce-Shimomura et al., 1999) is the fundamental turning event in C. elegans random search, with functional analogies to tumbles in bacterial chemotaxis (Berg and Brown, 1972). Careful inspection reveals a third state, called “pause,” in which locomotion ceases for a fraction of a second or more (Croll, 1975; Shingai, 2000; Stephens et al., 2008; Rakowski et al., 2013; Salvador et al., 2014). Thus, C. elegans locomotion consists of three main behavioral states – forward, reverse, and pause – together with the transitions between them.

C.  elegans subsists on a diet of bacteria that it finds mainly in rotting plant material (Frézal and Félix, 2015). In the laboratory, search behavior is studied in worms foraging on agar plates containing one or more dense bacterial lawns, analogous to food patches in the ethological literature. Like many other organisms, C. elegans can tune the spatial scale of random search to its physiological state, the availability of food (Wakabayashi et al., 2004; Gray et al., 2005), and prior knowledge of its distribution (Calhoun et al., 2014). The lowest values of search scale are observed during “cropping,” (Jander, 1975) the exploitation of a dense food patch. In C. elegans, two substates of cropping have been described: "dwelling," characterized by especially low crawling speed and frequent (presumably short) reversals, and "roaming," characterized by somewhat higher speeds and less frequent reversals. Transitions between dwelling and roaming, like the transitions between forward and reverse locomotion, are stochastic (Ben Arous et al., 2009; Fujiwara et al., 2002; Flavell et al., 2013). Intermediate values of search scale are observed during "local search" (Wakabayashi et al., 2004; Hills et al., 2004) when, for example, the animal is suddenly transferred from a bacterial lawn to a foodless region of the plate. The highest values of search scale are observed during “ranging,” when food is exhausted, starvation sets in, and the need to find a new food patch becomes urgent (Wakabayashi et al., 2004; Gray et al., 2005). Worms sometimes spontaneously leave a food patch well before it is exhausted, with leaving rate inversely related to food quality and food density (Shtonda and Avery, 2006; Harvey, 2009), which may reflect a trade-off between exploitation and exploration (Bendesky et al., 2011).

At the heart of the C. elegans locomotion circuit are five pairs of premotor 'command' interneurons organized into two functional groups that promote forward and reverse locomotion, respectively (Chalfie et al., 1985; Zheng et al., 1999; Stirman et al., 2010; Schmitt et al., 2012). The two groups are reciprocally connected, and make output synapses onto distinct, non-overlapping sets of motor neurons that control body-wall muscle. The locomotory state (forward or reverse) is believed to be determined mainly by whichever set of motor neurons is more highly activated by input from the command neurons (Kawano et al., 2011; Xie et al., 2013; Gao et al., 2015; Liu et al., 2014). Command neuron activation depends upon influences that are both external and intrinsic to the command neuron network, and appears to have a strong stochastic component that underlies switching between forward and reverse locomotion. Some command neurons are tightly linked both functionally and synaptically to upstream interneurons that also switch state stochastically in concert and counterpoint to them (Gordus et al., 2015), providing a potential additional source of the stochasticity on which random search depends. At least nine classes of chemosensory neurons and twelve classes of upstream interneurons are required for normal regulation of the duration of forward locomotion (Wakabayashi et al., 2004; Gray et al., 2005; Tsalik and Hobert, 2003; Fang-Yen et al., 2015). Input from these neurons onto the command neuron network modulates the mean run length and, thereby, the spatial scale of random search. Search scale also appears to be modulated by neurons that release biogenic amines (serotonin, dopamine, and tyramine) (Flavell et al., 2013; Hills et al., 2004; Bendesky et al., 2011) or peptides (Ben Arous et al., 2009; Flavell et al., 2013; Gloria-Soria and Azevedo, 2008; Styer et al., 2008; Reddy et al., 2009; Bhattacharya et al., 2014). These diverse signaling pathways may provide the means by which the worm optimizes its search strategy in response to feeding history (Gray et al., 2005), the quality, density and spatial distribution of food (Shtonda and Avery, 2006; Calhoun et al., 2015), and other factors that constrain survival and reproduction (Gloria-Soria and Azevedo, 2008; Pujol et al., 2001; Pradel et al., 2007; Lipton et al., 2004).

Although the neural circuitry for local search has been described in considerable detail, our understanding of the system remains limited, partly for lack of key physiological data, but also for lack of a model in which to interpret the data. Common sense suggests that the forward and reverse command neurons should inhibit each other to minimize simultaneous occurrences of neuronal states for incompatible behaviors (Zheng et al., 1999). A plausible anatomical substrate for such reciprocal inhibitory connections between command neurons exists in the C. elegans connectome (White et al., 1986), but anatomical data do not specify the signs or strengths of synaptic connections. A quantitative model that incorporates physiological properties of the command neurons and their synaptic connections is needed to interpret experimental results, such as the unexpected observation that silencing some of the reverse command neurons causes a reduction in forward dwell time, and conversely for forward command neurons (Rakowski et al., 2013; Zheng et al., 1999). It is also needed to explain complex patterns of changes in dwell times observed across the three locomotory states caused by introducing or eliminating tonic membrane conductances in the command neurons, and to answer basic mechanistic questions about the control of C. elegans locomotion.

At present, the experimental data are insufficient for creating a neuron-by-neuron model of the command network that incorporates biophysical details such as synaptic and membrane conductances without introducing a heavy load of unconstrained parameters (Rakowski et al., 2013). Nor would such a mechanistically detailed model necessarily provide the appropriate level of abstraction in which to intuitively understand C. elegans search behaviors, including their strong stochastic component. Instead, we have kept the level of biological detail to the minimum needed to predict the statistical distributions of dwell times in forward, reverse and pause states, and other fundamental aspects of the behavior. Each of the model's three main assumptions remains within the bounds of widely accepted experimental results; our mathematical analysis simply shows what follows necessarily from these assumptions.

To provide an empirical basis for the model we quantified C. elegans search behavior in terms of tangential velocity, defined as the speed and direction of worm's movement along its sinuous trajectory, which we recorded at higher resolution than previously possible. Behavioral data were then fit to a four-state hidden Markov model in which each state corresponds to a unique pattern of activation across the command neurons. Importantly, rate constants governing probabilistic transitions between states in the Markov model are expressed in terms of synaptic weights in an analytically tractable version of the model. We were therefore able to validate the model by showing that it correctly predicts phenomena on which it was not fit, such as reciprocal inhibition between forward and reverse command neurons in the biological network and the behavioral effects of perturbations introduced by laser ablations and genetic mutations. Although the model is inherently probabilistic, we found that it also makes accurate predictions concerning deterministic behaviors in C. elegans, indicating a potentially high level of generality. The present findings thus establish a simple theory of C. elegans locomotory control and provide a testable model of random search that can be applied to other organisms.

## Results

A neuronal model of random search in C. elegans is a theory of the relationship between activation states of the command neurons and foraging behavior. Methods presently available for observing neuronal activity in freely behaving C. elegans utilize calcium-sensitive probes that have insufficient temporal resolution to observe the changes in neuronal activity associated with the rapidly changing behavioral states, especially the frequent brief pauses that are an integral part of the behavior. Therefore, as a proxy for command neuron state, we used the worm's tangential velocity, defined as the speed and direction of worm's movement along its sinuous trajectory. We focused on tangential velocity because in sinusoidal locomotion the net reactive forces produced by body-wall muscle contractions acting against the substrate are tangential to the body surface (Gray et al., 2005). Tangential velocity therefore provides the most direct readout of which group of motor neurons and command neurons (forward or reverse) is more active (Qi et al., 2013). Alternative measures of the rate of translation such as centroid velocity (Pierce-Shimomura et al., 1999) or postural phase velocity (Stephens et al., 2011) have a less direct relationship to command neuron state because these measures either depend in complex ways on the shape of the worm, or rely on a representation of posture that ignores some of the thrust-generating components of the worm’s shape that come into play unless the worm is moving along a fairly linear trajectory. To monitor tangential velocity as directly as possible, we painted a microscopic black spot on the worm and used a motorized stage controlled by a computer to keep the spot in the field of view (Figure 1A). The most common alternative method for measuring tangential velocity, tracking virtual points obtained by segmenting the worm’s centerline, is subject to segmentation errors introduced by low contrast images of the worm's head and tail (see Cronin et al., 2005 ) which changes the distance between virtual points. This method can also be compromised by dropped frames when the worm's centerline crosses itself during tight turns.

![Figure 1.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig1-v2.jpg)

**Figure 1.:** (A) $(x,y)$-coordinates of a worm during 10 min of foraging. Inset: Image of a worm showing the black spot (arrow) used for optical tracking (scale bar = 200 µm). (B) The speed distribution computed from the distance moved between successive video frames had a peak at 180 µm/s, which includes both forward and reverse locomotion. A second peak at 14 µm/s corresponds to pauses. The decreased probability of observing speeds <14 µm/s (<0.47 μm/frame) is due to noise in the position measurement. (C) At least three time constants were required to fit (red) the speed autocovariance function (black; grey shading shows ± 1 sem). (D) The worm’s heading remained nearly constant for ~10 s except for a transient peak at 1.4 s (▼), which corresponds to the period of one half cycle of undulation during sinusoidal locomotion. The dashed line shows random reorientation; shading shows ± 1 sem. (E) Example of $v(t)$ showing periods of forward locomotion, reverse locomotion and pauses of various durations. Upward triangles (▲) mark forward-pause-forward (FPF) events; the downward triangle (▼) marks a reverse-pause-reverse (RPR) event. (F) Velocity distributions for the 5 wild type cohorts (5 colors) analyzed in this study. (G) Ensemble-averaged velocity during FPR transitions. All FPR transitions in all wild type cohorts were aligned at the end of forward movement, grouped according to the duration of the pause (2–9 frames), and averaged. Such transitions were defined using a threshold criterion of $v$ < 50 μm/s to identify state P (Rakowski et al., 2013). Pauses lasting ≤ 1 frame are not shown because of ambiguity in state identification; pauses lasting ≥ 10 frames are omitted for clarity. (H) Identical to G except RPF transitions are shown. (I) Cumulative probability distributions for dwell time in the pause state defined as in G and H for all FPR and RPF transitions of duration >1 frame in wild type worms.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Position data recorded for 1 min each from 4 dead worms spotted by the usual procedure. Under these conditions the stage is stationary. Data from each worm are shown in a different color. The circle encloses 1 standard deviation of the combined 2-D distribution. Optical tracking is more precise than the resolution of the stage position encoder, and thus does not limit the overall resolution of the position measurement.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) the velocity autocorrelation function ($A_{V}$) averaged across the 5 wild-type cohorts shows that movements become uncorrelated after ~10 s, primarily as a result of random reorientation during transitions from reverse to forward motion. The period of the damped oscillations in $A_{V}$ corresponds to the period of sinusoidal undulations during locomotion. (B) The observed linear increase in mean-squared distance travelled with time (black; mean ± sem, averaged data from all wild-type worms) shows that on this time scale search behavior approximates a Brownian random walk. (C) At shorter times the observed (black) relation curves upward because worms travel in relatively straight lines during runs. Assuming that the behavior is stationary over the 10 min observation period, the dependence of $r^{2}¯$ on $t$ can be calculated from the velocity autocorrelation function (red curves in B and C):

$$
r^{2}¯t≅r^{2}t=2\int_{0}^{t}(t−\tau)A_{v}(\tau)d\tau=2\int_{0}^{t}(t−\tau)V\tau·V^{t}0d\tau
$$

where $·$ denotes statistical expectation (eq. 2.5.12 of Boon and Yip, 1980). Thus, the worm’s movements approximate Brownian motion on a time scale that is longer than the persistence of the velocity autocorrelation, but not at shorter times.

At the start of a 10 min observation period an individual worm was transferred from a food-laden culture plate to a bare agar surface devoid of overt sensory cues, thereby inducing a period of intensive local search behavior (Jander, 1975; Hills et al., 2004). The (x, y)-coordinates of the centroid of the spot were recorded with a temporal resolution of 33 ms (i.e., frame rate = 30 Hz) and a spatial resolution of 0.5 μm that was limited mainly by the precision of the stage position encoder; the optical tracking error was much smaller (Figure 1—figure supplement 1). A spatial resolution of approximately 0.5 μm amounts to an approximately 10-fold improvement over previously published tracking systems (Kocabas et al., 2012); thus worm speed (Figure 1B) could be extracted with unprecedented accuracy. For statistical analysis, worms were grouped into cohorts having the same genotype or neurons ablated (17–31 worms per cohort), which had been reared together and tested in parallel as young adults within the same 2–3 day period. This approach yielded a comprehensive data set containing a total of 8.3 million position measurements from 501 individuals in 20 cohorts.

### Model-independent identification of locomotory states

Figure 1A– D describes important features of search behavior obtained by regarding the worm as a point moving in an external reference frame (allocentric coordinates) without regard to the orientation of the body axis. The speed distribution was bimodal (Figure 1B) with a broad peak around 180 µm/s that includes both forward and reverse motion, and a narrower peak near zero that corresponds to pauses. The speed autocovariance function had multiple exponential components (Figure 1C), suggesting at least three locomotory states. The average change in heading angle ($|\Delta\phi|¯$), plotted as a function of the intervening time interval (Figure 1D), showed that worms maintained a nearly constant heading for up to 10 s (Stephens et al., 2010; Peliti et al., 2013), but reoriented randomly within ~30 s, establishing the shortest time scale over which the behavior can be considered a Brownian random walk (Figure 1—figure supplement 2), the simplest form of random search. On shorter time scales the path takes on the character of a truncated Lévy flight (Mantegna and Stanley, 1994).

For more detailed analysis we distinguished forward from reverse movement by visual inspection of the recorded videos, and defined velocity, v(t), to be a signed scalar value that denotes the speed of movement along the worm’s track in the direction of the head (+) or tail (-) (Figure 1E; see Materials and methods). The probability distribution of v(t) (Figure 1F) showed two broad peaks that correspond to forward and reverse movement, and a narrow third peak centered at zero that corresponds to pauses. For the initial analysis we defined pauses using a fixed speed threshold of 0.05 mm/sec (Rakowski et al., 2013). Pauses occurred most frequently as transient interruptions of forward locomotion, causing the worm to stutter as it moves (Figure 1E; Video 1); stuttering also occurred, albeit less frequently, during reverse locomotion (Figure 1E; Video 2). Distinct pauses were also observed during transitions from forward to reverse (Figure 1G; Video 3) and from reverse to forward (Figure 1H; Video 4). Most pauses lasted longer than one video frame, indicating the presence of a locomotory state having a detectable dwell time; thus pauses were not merely zero crossings in plots of velocity versus time. We found that pauses during forward to reverse transitions were on average longer in duration than pauses during reverse to forward transitions (Figure 1I; p<10–5 ; Mann-Whitney U-test). These findings are consistent with the predictions of the model presented below, which uses a probabilistic criterion rather than a fixed velocity threshold to identify pauses.

![Video 1.](https://cdn.elifesciences.org/articles/12572/elife-12572-media1.mp4.jpg)

**Video 1.:** The worm is crawling on a foodless agar plate. The microscope stage moves continuously to keep the tracking spot near the center of the frame. Stage movement can be assessed by monitoring the white streaks in the background, which are segments of the worm's track at earlier times. Behavioral state is indicated in the upper left corner of the frame. The indicated behavioral transition is shown at normal speed, and slowed down by a factor of 5. The worm is paused when the tracking spot is stationary relative to the streaks.

![Video 2.](https://cdn.elifesciences.org/articles/12572/elife-12572-media2.mp4.jpg)

![Video 3.](https://cdn.elifesciences.org/articles/12572/elife-12572-media3.mp4.jpg)

![Video 4.](https://cdn.elifesciences.org/articles/12572/elife-12572-media4.mp4.jpg)

### The stochastic switch model

Based on the results presented in Figure 1 and previous studies noted below, we propose a minimal model for the control of random search behavior that involves two opposing neuron-like “units” that can exist in four distinct states corresponding to forward locomotion, reverse locomotion, and two pause states. This model differs from a previous model that represents the worm as a point in “shape space” (Stephens et al., 2008) in that here velocity is measured directly by observing the motion of a point on the body surface relative to the substrate, rather than indirectly by the temporal progression of shape changes. It also differs from previous models (Rakowski et al., 2013; Zheng et al., 1999; Wicks et al., 1996; Kunert et al., 2014) by representing changes in locomotory state as probabilistic transitions in a Markov process.

Ablation of individual premotor interneurons (Chalfie et al., 1985) has led to the hypothesis that the direction of locomotion is controlled by a network comprising five pairs of premotor command interneurons organized into two functional groups that promote forward and reverse locomotion, respectively. Although the anatomical pattern of synaptic connectivity among these interneurons has been established (White et al., 1986) (Figure 2A), this information does not yield an intuitive explanation of how the direction of locomotion is regulated. Nor, in our view, does the present state of the anatomical connectivity provide the basis for a neuron-by-neuron simulation of the network (but see Rakowski et al., 2013), as neither signs nor physiological strengths (weights) of synapses in C. elegans can be inferred reliably from anatomical structure or neurotransmitter type, and almost nothing is known about the intrinsic membrane currents of these neurons or how they shape the input-output function of individual command neurons.

![Figure 2.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig2-v2.jpg)

**Figure 2.:** (A) Connectivity of forward and reverse command neurons. Arrows with single heads are monosynaptic connections inferred from the C. elegans connectome (White et al., 1986; Varshney et al., 2011) line thickness is proportional to the number of presynaptic specializations seen in the reconstruction of each pairwise connection. Open, double-headed arrows indicate synaptic pathways from or to the indicated pool of neurons outside the network. (B) Voltage recording from the command neuron AVA in the absence of injected current. In this neuron, quasi-stable membrane potentials are seen at -17 and -32 mV. These results differ from previously published AVA recordings, which were made in the presence of hyperpolarizing current (5–10 pA) that kept the membrane potential near -55 mV (Lindsay et al., 2011). (C) Neuronal representation of the Stochastic Switch Model. Forward and reverse command neurons are represented as single binary neuron-like units $ℱ$ and $ℛ$, respectively. Arrows depicting cross connections ($w_{ℱℛ}$, $w_{ℛℱ}$) represent functional (net mono- and polysynaptic) connections between forward and reverse units. Self-connections ($w_{ℱℱ}$, $w_{ℛℛ}$) represent synaptic connections between neurons comprising a given unit, voltage dependent currents in these neurons, and polysynaptic recurrent pathways involving non-command neurons. Downward arrows ($h_{ℱ}$, $h_{ℛ}$) represent the combined effects of input from presynaptic neurons, including sensory neurons, and neuromodulation. (D) Markov model representation of the command neuron network. The color of a unit indicates its state of activation (red on, white off). In addition to the forward state F and the reverse state R, there are two pause states, X and Y. Arrows, with their associated rate constants, indicate transitions in which a single unit changes state. Transitions in which two units change state simultaneously have probability zero because single-unit transitions are assumed to be statistically independent. (E) The most likely sequence of states in the hidden Markov model (computed using the Viterbi algorithm) for a representative data segment.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Effects of synaptic input on transition rates in stochastic units $ℱ$ and $ℛ$.Rate constants are exponential functions of the unit’s net synaptic input S. Excitatory input increases the on rate and decreases the off rate, whereas inhibitory input has the opposite effect. When synaptic input equals zero, the unit switches stochastically between on and off states with rate constant A.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** For each cohort, the velocity distribution $g(v)$ (black; binwidth 2 µm/s) was smoothed by 10 passes of a 1-2-1 binomial smoothing algorithm, then separated into three overlapping velocity distributions: $g_{F}(v)$ (dashed green), $g_{R}(v)$ (dashed blue), $g_{P}(v)$ (dashed red).For $g_{P}(v)$ we used a Cauchy distribution (half width 18 µm/s) scaled to fit $g(0)$. We estimated $g_{F}(v)$ and $g_{R}(v)$ by subtracting $g_{P}(v)$ from $g(v)$ and restricting the F and R distributions to positive and negative velocities, respectively. The sum $g_{F}(v)+g_{R}(v)+g_{P}(v)$ is shown in solid orange.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Comparisons between cumulative dwell time distributions (solid lines) and the exponential distributions predicted by the hidden Markov model ($1−exp(−t/d_{S})$, where $d_{S}$ is the mean dwell time in state $S$; Table 1). The observed dwell times were tabulated from the most likely sequence of states obtained using the Viterbi algorithm. The origin on the time axis corresponds to one frame.

To establish a mathematically tractable framework for understanding how the command network functions during search behavior, we created a minimal model based on three simplifying assumptions, each of which was biologically motivated. (i) Command neurons act like binary units (Hopfield, 1982). This assumption was based on voltage recordings from command neurons in which we regularly observed two stable membrane potentials with rapid transitions between them (Figure 2B; also see Kato et al., 2015). It is also supported by the observation of a bimodal distribution of calcium activity in AVA neurons and their upstream partners AIB and RIM (Gordus et al., 2015), and the report of distinct up and down states in voltage recordings from motor neruons (Liu et al., 2014). (ii) Command neurons switch state stochastically. This assumption was based on the observation that C. elegans locomotory behavior has a strong stochastic component, with exponentially distributed dwell times in forward and reverse states (Pierce-Shimomura et al., 1999; Zhao et al., 2003; Flavell et al., 2013; Gordus et al., 2015; Stephens et al., 2011). (iii) Command neurons within the forward pool are co-active, as are command neurons in the reverse pool. This assumption is based on simultaneous calcium imaging data from multiple command neurons in freely moving animals which suggest that the activity of neurons within the reversal pool is tightly correlated (Schrödel et al., 2013; Prevedel et al., 2014). Additionally, neurons in opposing groups are likely to be reciprocally active, as indicated by simultaneous calcium imaging from AVA and AVB (Prevedel et al., 2014; Faumont et al., 2011), as well as AVE and AVB (Kawano et al., 2011). A fourth assumption, concerning the relationship between neuronal states and behavioral states, is introduced below.

The three simplifying assumptions, together with the anatomical data (White et al., 1986), lead to a model that has two binary stochastic elements, $ℱ$ and $ℛ$, and six synaptic weights (Figure 2C). Each type of weight has a specific interpretation. The cross-connections ($w_{ℱℛ}$, $w_{ℛℱ}$) represent mono- and polysynaptic connections between command neurons in different groups. The self-connections ($w_{ℱℱ}$, $w_{ℛℛ}$) represent connections between command neurons in the same group, including recurrent polysynaptic pathways involving neurons outside the command network. Self-connections also represent possible intrinsic voltage dependent currents within the command neurons, such as C. elegans plateau currents (Mellem et al., 2008). The pair of connections originating from an $ℱ$or $ℛ$ unit can have either the same sign or different signs. Allowing a single unit to have opposing effects on different postsynaptic targets is justified by the fact that synaptic weights in the model represent polysynaptic pathways, the effects of which can be excitatory or inhibitory, and by the observation that some C. elegans neurons can monosynpatically excite some postsynaptic neurons while inhibiting others (Chalasani et al., 2007). Two additional weights, $h_{ℱ}$ and $h_{ℛ}$, represent inputs from sensory neurons, interneurons, neural modulators, and any other sources outside the network (Gray et al., 2005; Fry et al., 2014), plus intrinsic membrane conductances that produce sustained effects on membrane potential (Zheng et al., 1999; Gao et al., 2015). The summed synaptic inputs onto $ℱ$ and $ℛ$ are, respectively, $S_{ℱ}t=h_{ℱ}+w_{ℱℱ}b_{ℱ}t+w_{ℛℱ}b_{ℛ}(t)$ and $S_{ℛ}(t)=h_{ℛ}+w_{ℛℛ}b_{ℛ}(t)+w_{ℱℛ}b_{ℱ}(t)$, where $b_{ℱ}(t)$ and $b_{ℛ}(t)$ are the states of $ℱ$ and $ℛ$ at time $t$ (1 = ON, 0 = OFF). The quantities $h_{ℱ}$ and $h_{ℛ}$ were assumed to be constant during the 10 min observation period of local search behavior on a bare agar surface.

State transitions of $ℱ$ and $ℛ$ were modeled as independent non-homogeneous Poisson processes in which the transition rates are exponential functions of the summed synaptic input to the units, as shown in Figure 2—figure supplement 1. Changes of the state of $ℱ$ and $ℛ$ can be regarded as thermally-driven transitions across energy barriers of height proportional to $S_{ℱ}(t)$ and $S_{ℛ}(t)$, respectively. Inhibitory synaptic input increased the height of the barrier for OFF→ON transitions while decreasing the height of the barrier for ON→OFF transitions by the same amount; excitatory synaptic inputs had the opposite effect. The variable $A$ (Materials and methods, Equations 26, 27) represents the fundamental timescale of the system, defined as the rate at which units $ℱ$ and $ℛ$ change state when the summed synaptic input is zero. The present model is distinct from deterministic models of the command neuron network (Rakowski et al., 2013; Zheng et al., 1999; Wicks et al., 1996; Kunert et al., 2014) in that it is inherently stochastic, like the behavior it is meant to predict. In particular, the synaptic input to a unit does not immediately determine its state, but instead modifies the transition rates between ON and OFF states.

The two binary units of the model can exist in four states (F, R, X, Y; Figure 2D), and provide the basis for a hidden Markov model having eight transitions in which a single unit changes state. The model was further constrained by the synaptic model, which allows the eight transition rate constants to be specified by only six synaptic weights as shown in Equations 31–35 (Materials and methods). A Markov model was adopted to represent the biological system because dwell times in Markov states, like the observed dwell times in forward and reverse states (Zhao et al., 2003; Wakabayashi et al., 2004), are exponentially distributed. A hidden Markov model was required because, as noted above, states of command neurons cannot be observed directly in freely moving animals, even using optical recording methods.

The fourth assumption is a particular mapping between the states of the two command units and behavioral states of the worm. The command units, $ℱ$ and $ℛ$, are intended to represent the two pools of forward and reverse command neurons, respectively, such that the worm moves forward when $ℱ$ is ON and $ℛ$ is OFF (state F), backwards when $ℛ$ is ON and $ℱ$ is OFF (state R), and pauses when both $ℱ$ and $ℛ$ are OFF (state X). These associations between states of the model and activation states of the command neurons are well supported by previous experimental evidence, including studies showing that genetic ablation or silencing of all command interneurons induces prolonged pauses (Zheng et al., 1999; Kawano et al., 2011), but they also assume the major simplification that all command neurons in a given pool act together as a unit.

The model also permits a fourth state, in which $ℱ$ and $ℛ$ are simultaneously ON (state Y). Whether the corresponding co-activation state of forward and reverse command neurons normally exists with any significant probability remains to be shown, but it has been observed that their downstream targets, the forward and reverse motor neurons, can be active simultaneously, causing the worm to pause (Kawano et al., 2011). Given the existence of gap junction synapses between the main forward and reverse command neurons and their respective sets of forward and reverse motor neurons, it is reasonable to suppose that forward and reverse command neurons are co-active when their motor neurons are co-active. Thus, there is some evidence to designate state Y as a second pause state, which we consider to be a working hypothesis. Together, states X and Y comprise the phenomenological pause state denoted P. In what follows, we explore the logical consequences of the model’s four assumptions; it remains to be shown experimentally how closely the states of the model correspond to activity states of the command neurons.

We used a maximum likelihood method (Colquhoun and Hawkes, 1995) (Materials and methods) to estimate the set of transition rate constants that had the highest probability of generating the observed time series $v(t)$. Direct transitions between F and R, and between X and Y, were disallowed because the assumed statistical independence of the two command units implies that the probability of simultaneous transitions in $ℱ$ and $ℛ$ is vanishingly small. (Note, however, that the model does allow transitions between any two states during the interval between successive video frames by making two or more non-simultaneous transitions; see Equation 21). We first fit the velocity distribution for each cohort with three overlapping probability distributions corresponding to forward, reverse and pause states (Figure 2—figure supplement 2), then searched for the set of transition rate constants that maximized the likelihood of the observed $v(t)$ given the velocity distributions. The resulting rate constants were used to compute the most likely sequence of states via the Viterbi algorithm (Rabiner, 1989; Viterbi, 1967). The agreement between observed velocity data and the sequence of states shown in Figure 2E was typical of the entire data set.

### Wild type locomotion

The maximum likelihood rate constants for 5 wild-type cohorts, together with the predicted state probabilities and mean dwell times computed from them, are given in column A of Table 1. The model’s predicted mean dwell time in the reverse state (dR= 1.94 ± 0.04 s) agreed with previously reported values (Zheng et al., 1999; Kawano et al., 2011). In contrast, the predicted mean dwell time in the forward state (dF= 5.33 ± 0.25 s) was smaller than previously reported when dwell time was measured by eye (13–35 sec) (Zhao et al., 2003; Zheng et al., 1999; Brockie et al., 2001; Ryu and Samuel, 2002) or by velocity threshold crossings (9–16 sec) (Rakowski et al., 2013; Stephens et al., 2011). To determine whether this difference arose because we used a hidden Markov model rather than a fixed velocity threshold, we also identified states based on a fixed velocity threshold of 0.05 mm/s, and calculated the resulting mean dwell times: dF,0.05= 1.86 ± 0.03 s; dR,0.05= 1.23 ± 0.02 s; dP,0.05= 0.14 ± 0.001 s. We attribute the short mean dwell times in state F that we observed using either the hidden Markov model or a fixed velocity threshold to the fact that our tracking system is capable of revealing briefer visits to state P, which interrupt forward runs, than previous methods. Ignoring transient interruptions of forward locomotion (i.e., FPF transitions) and using the fixed velocity threshold of 0.05 mm/s yielded longer a mean forward dwell time of 9.13 ± 0.15 s, which matches the value obtained by others using the same threshold (8.98 ± 0.57 s) (Rakowski et al., 2013). Predicted mean dwell times in the two pause states differed substantially from each other (dX=0.44 ± 0.03 s, dY= 0.21 ± 0.02). We assigned the long and short pause states to X and Y, respectively, based on the idea that the energetically expensive state in which both units are on should be relatively short-lived.

**Table 1.**
 Maximum likelihood fits of transition rates in wild type C. elegans. Each cohort was fitted separately; values are expressed as mean ± sem (n = 5 cohorts). Data from wild type cohorts were obtained on the same days as the experimental cohorts for which they served as controls (Tables 3 and 4), but experimental cohorts in this study were separated by weeks to months. All transition rates were constrained to be ≥0. Transition rates that were calculated using the synaptic constraints (Equation 35) are shaded orange; other constrained values are shaded grey. Mean dwell times and state probabilities were calculated from the transition rates. Column A shows fits using the standard model, which has 8 rate constants with two synaptic constraints, resulting in 6 free parameters that determine the 6 synaptic weights (Figure 2C,D; Materials and methods Equations 31–35). Column B shows fits to a model that has only one pause state (X); this model was derived from the standard model by imposing two more constraints: $a_{FY}=a_{RY}≅0$, yielding 4 free parameters. To allow comparison of models A and B by the likelihood ratio test, which requires that model B be a special case of model A, $a_{RY}$ and $a_{FY}$ were set slightly >0 (10-10 s-1), thereby avoiding infinite values for $a_{YF}$ and $a_{YR}$ when applying the synaptic constraints, while maintaining a vanishingly small probability of being in state Y ($p_{Y}<$ 10-18). The loge likelihood (summed over the 5 cohorts) for model B was 1854 less than for model A, with 30 degrees of freedom for model A (6 per cohort × 5 cohorts) and 20 degrees of freedom for model B (4 per cohort × 5 cohorts). Applying the likelihood ratio test, the difference was highly significant (p<10-100; p=Chi-squared(2L, df), where L  = 1854 and df  = 30–20 =10. Model C is the most general 3-state (F, R, P) model, which allows all six transitions between the three states. The fitted transition rates for model C were nearly identical to model B. Likelihood values are relative to model A.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>2 pause states6 free parameters</th>
      <th>1 pause state4 free parameters</th>
      <th>1 pause state6 free parameters</th>
    </tr>
    <tr>
      <th>Δ loge likelihood</th>
      <th>0</th>
      <th>-1854</th>
      <th>-1836</th>
    </tr>
    <tr>
      <th>Degrees of freedom</th>
      <th>30</th>
      <th>20</th>
      <th>30</th>
    </tr>
    <tr>
      <th></th>
      <th>mean ± sem (n  = 5)</th>
      <th>mean ± sem (n  = 5)</th>
      <th>mean ± sem (n  = 5)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>aXR (s-1)</td>
      <td>1.201 ± 0.099</td>
      <td>1.019 ± 0.085</td>
      <td>1.008 ± 0.090</td>
    </tr>
    <tr>
      <td>aXF (s-1)</td>
      <td>1.115 ± 0.087</td>
      <td>1.915 ± 0.152</td>
      <td>1.914 ± 0.152</td>
    </tr>
    <tr>
      <td>aRX (s-1)</td>
      <td>0.025 ± 0.008</td>
      <td>0.507 ± 0.013</td>
      <td>0.507 ± 0.013</td>
    </tr>
    <tr>
      <td>aRY (s-1)</td>
      <td>0.490 ± 0.015</td>
      <td>10-10</td>
      <td></td>
    </tr>
    <tr>
      <td>aFX (s-1)</td>
      <td>0.182 ± 0.007</td>
      <td>0.198 ± 0.009</td>
      <td>0.196 ± 0.008</td>
    </tr>
    <tr>
      <td>aFY (s-1)</td>
      <td>0.007 ± 0.002</td>
      <td>10-10</td>
      <td></td>
    </tr>
    <tr>
      <td>aYR (s-1)</td>
      <td>0.411 ± 0.019</td>
      <td>&gt;109</td>
      <td></td>
    </tr>
    <tr>
      <td>aYF (s-1)</td>
      <td>4.575 ± 0.533</td>
      <td>&gt;109</td>
      <td></td>
    </tr>
    <tr>
      <td>aFR (s-1)</td>
      <td></td>
      <td></td>
      <td>0.001 ± 0.001</td>
    </tr>
    <tr>
      <td>aRF (s-1)</td>
      <td></td>
      <td></td>
      <td>0.000 ± 0.000</td>
    </tr>
    <tr>
      <td>dF (s)</td>
      <td>5.329 ± 0.245</td>
      <td>5.096 ± 0.235</td>
      <td>5.135 ± 0.227</td>
    </tr>
    <tr>
      <td>dR (s)</td>
      <td>1.945 ± 0.043</td>
      <td>1.975 ± 0.049</td>
      <td>1.976 ± 0.049</td>
    </tr>
    <tr>
      <td>dX (s)</td>
      <td>0.441 ± 0.032</td>
      <td>0.349 ± 0.026</td>
      <td>0.351 ± 0.027</td>
    </tr>
    <tr>
      <td>dY (s)</td>
      <td>0.208 ± 0.019</td>
      <td>&lt;10-9</td>
      <td></td>
    </tr>
    <tr>
      <td>pF</td>
      <td>0.762 ± 0.015</td>
      <td>0.7641 ± 0.015</td>
      <td>0.764 ± 0.014</td>
    </tr>
    <tr>
      <td>pR</td>
      <td>0.158 ± 0.007</td>
      <td>0.158 ± 0.007</td>
      <td>0.155 ± 0.007</td>
    </tr>
    <tr>
      <td>pX</td>
      <td>0.063 ± 0.006</td>
      <td>0.081 ± 0.008</td>
      <td>0.080 ± 0.008</td>
    </tr>
    <tr>
      <td>pY</td>
      <td>0.017 ± 0.002</td>
      <td>&lt;10-18</td>
      <td></td>
    </tr>
  </tbody>
</table>

In previous work, transitions between locomotory states in C. elegans have been analyzed by choosing a speed threshold to distinguish pause states from the movement states (Rakowski et al., 2013; Salvador et al., 2014; Stephens et al., 2011). The choice of threshold is important because it affects the measured dwell times, yet is necessarily arbitrary because the velocity distributions of the states overlap (Figure 1F). The hidden Markov model used here replaces arbitrary thresholds with empirically determined state transition rates (i.e., the set of rates that maximizes the probability of the observed velocity time series), from which one can determine the sequence of states that is most likely to have generated the data (the Viterbi algorithm). The hidden Markov model thus offers two advantages: (1) it provides a statistical criterion for selecting the best parameter values and (2) it takes into account the uncertainties in identifying the state of the system from velocity data.

Under the assumptions of the hidden Markov model the state of the system cannot be observed directly because the velocity distributions overlap, making it impossible to test directly whether the predicted state probabilities agree with the observed velocity data. Nevertheless, an important test of the model can be obtained using the Viterbi algorithm to identify the most likely sequence of states given the observed velocity data, from which the histogram of dwell times in each state can be computed and compared to the exponential distribution predicted by the Markov model (Figure 2—figure supplement 3). The degree of agreement between the distributions shows that our model provides a good description of the system.

The initial rationale for including two pause states in the hidden Markov model came from our model-independent analysis of the tracking data (Figure 1I), which showed different dwell time distributions for pauses at FPR and RPF transitions. To test whether having two pause states yielded a statistically significant improvement in the ability of the model to fit the data, we eliminated one of the pause states and asked whether the resulting reduction in likelihood was greater than could be attributed to the reduction in the number of free parameters (see Table 1). For this comparison we constrained the transition rates into state Y to be extremely small (aFY=aRY= 10-10 s-1), effectively eliminating state Y and reducing the number of free parameters from six to four. The reduction in likelihood caused by eliminating one of the pause states was highly significant, and cannot be attributed simply to the elimination of two parameters (p<10-100; likelihood ratio test). Separately, we considered the most general one-pause state model, which allows direct transitions between states F and R and has no constraints on the 6 transition rates other than that they are all ≥0. The fit of this model (Table 1 column C) converged to nearly the same set of transition rates as the one-state model described above (Model B). These comparisons show that our model with two pause states and six free parameters (the six synaptic weights) provides a much better fit to the data than models with only one pause state. We conclude that the tracking data contain a statistically significant signature of two distinct pause states. The model explains the observation that the pause dwell times during FPR transitions are longer than during RPF transitions (Figure 1I) in terms of the different dwell times in states X and Y (dX>dY), and the strong tendency to cycle clockwise through state space, exiting from state F to state X and from state R to state Y as shown by the fate diagram (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig3-v2.jpg)

**Figure 3.:** The system typically cycles clockwise through states F, X, R, Y, with state F frequently interrupted by FXF transitions, leading to state sequences of the form …(FX)nRY(FX)nRY…. Nearly unidirectional transitions out of a given state are shown by red arrows; blue arrows indicate nearly equiprobable transitions. The width of the arrows and the numbers beside them show the probability that the transition out of the state at the tail of the arrow is into the state at the head. The area of each circle is proportional to the probability of the corresponding state (Table 1, column A).

It has been reported that pauses in C. elegans locomotion occur at specific points in “shape space” (Stephens et al., 2011), suggesting the worm pauses in preferred postures. To investigate this possibility, we analyzed worm tracks before and after pauses, inferring posture from the path of the tracking spot. This inference is justified by the fact that on an agar surface the worm moves without slipping, such that each segment of the body traces the trajectory of the one before it. Thus, the path of the tracking spot leading up to the pause reveals the worm’s posture posterior to the spot during forward locomotion, and anterior to the spot during reverse locomotion (Figure 4).

![Figure 4.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig4-v2.jpg)

**Figure 4.:** (A) Average track curvature upon entry in to the pause state in wild type worms. Prior to computing curvature, tracks of individual worms were mirror-imaged as needed such that positive curvature corresponds to a ventral bend. Tracks in the vicinity of pause events were aligned according to the location of the tracking spot in the pause state, converted to curvature, then averaged over all FX transitions (solid blue line; n = 1907), and all RY transitions (red; n = 295) for which the track length was >1.5 mm; shading shows ± 1 S.D. The trace depicts the curvature of the worm posterior to the tracking spot at the end of forward movement (FX transitions) and anterior to the tracking spot at the end of reverse movement (RY transitions). The dashed blue line shows the average curvature at FXR transitions (i.e., excluding FXF stutters). (B) Locomotory phases at which FX transitions occurred, plotted as blue dots on the unit circle. The phase at each FX transition was computed as $\phi=2\piz_{1}/(z_{2}−z_{1})$, where $z_{1}$ and $z_{2}$ are the positions of the two downward zero crossings of curvature preceding the pause as indicated in panel A, right. The uniform distribution of points around the circle, and therefore the small magnitude of the vector strength ($r=0.14$; arrow), shows that there was only a small (but statistically significant) phase preference at the end of forward motion ($p<10^{−16}$; Rayleigh test). (C) Same as B, but for RY transitions. Vector strength is large ($r=0.71$), indicating a strong tendency to end reverse runs at a particular phase ($p<10^{−63}$), with a ventral bend in the middle of the body. (D) Average posture at FXR transitions, calculated by integrating the average curvature, computed over all tracks that persisted for >1.5 mm in state F before the pause and >1 mm in state R after the pause. Arrows indicate direction of motion along the track (blue, forward; red, reverse). FXR transitions were typically a simple reversal along the same track. (E) Same as D but for RYF transitions that persisted for >1.5 mm in state R before the pause and >1 mm in state F after the pause. RYF transitions at the end of reverse runs that persisted for >1.5 mm were usually associated with a ventral bend that resulted in a ~180° change of direction as previously described (Gray et al., 2005).

Plotting mean curvature versus distance along the track (Figure 4A) reveals only a weak tendency to stop in a particular posture in state X (r = 0.14; Figure 4B). Nearly all of the transitions into state X were either stutters during forward locomotion (FXF transitions) or reversals (FXR transitions); when these were analyzed separately, similarly weak postural preferences were found at FXF transitions (r = 0.14) and FXR transitions (r = 0.14). A nearly identical result (r = 0.14 ) was obtained using a fixed velocity threshold of 0.05 mm/s rather than the hidden Markov model to determine state. For the latter case, in which there is only one pause state, we analyzed the posture at all FP transitions, which almost always correspond to FX transitions in the hidden Markov model because FY transitions are extremely rare (see Figure 3 ).To test whether the failure to find a strong postural preference at FX transitions was due to including very short pauses in the analysis, we repeated the analysis after reclassifying all pauses shorter than a minimum duration as a continuation of the previous state, and obtained the same result; we found no strong postural preference at FX transitions for minimum pause durations up to 2 s (r = 0.16, 0.19, 0.23, 0.3 for X dwell times > 0.33 s, 0.67 s, 1 s, and 2 s, respectively); longer dwells in state X were too rare to analyze. Thus, FX transitions can occur at any locomotory phase and do not occur preferentially at a particular posture (Figure 4D); in the case of FXR transitions the worm generally retreats along the same track. In contrast, we found a strong tendency to stop in a particular posture in state Y (Figure 4A,C,E; r = 0.71). Almost all entries into state Y were RYF transitions and these were associated with a ventral bend in the middle of the worm (Figure 4E). These results suggest fundamental differences between the control of forward and reverse locomotion. In our model, forward locomotion terminates when forward command neurons turn OFF, and this can happen at any phase, whereas reverse locomotion terminates when forward neurons turn ON, and this is most likely to happen at a particular phase. The latter could be explained by phasic feedback from the locomotory pattern generator to the forward neurons (Li et al., 2006).

### Ablation of command neurons

To determine the contributions of individual command neurons to the overall function of the command network, we separately ablated the pair of neurons that comprises each command neuron class, then tracked ablated and sham operated animals during local search. Mean velocities in F and R, if significantly changed, were reduced (Pokala et al., 2014) (Figure 5A; ⋆⋆), as was the frequency of undulations during forward and reverse locomotion (Table 3). In many organisms, the frequency of rhythmic behaviors is regulated by the amplitude of tonic excitatory drive to the associated pattern generator (Weeks, 1978; Satterlie and Norekian, 2001; Böhm and Schildberger, 1992; Deliagina et al., 2000; Dembrow et al., 2003; Hedwig, 2000; Sirota et al., 2000). To explain our results we propose that ablation of the locomotory command neurons reduces tonic drive to the presumptive locomotory pattern generator (Xie et al., 2013; Gao et al., 2015).

![Figure 5.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig5-v2.jpg)

**Figure 5.:** (A) Velocity distribution of ablated cohorts (red) compared to sham operated controls (grey) when the indicated command neuron was killed. Stars indicate significant reduction in velocity for the indicated peak (p<0.05 without ($⋆$) or with ($⋆⋆$) correction for multiple comparisons; Table 3). (B) Dwell times in F, R, and P in ablated (red) and sham operated animals (grey). Stars indicate significant differences from sham (as defined in Table 4). Horizontal lines indicate the estimated range of $d_{0}$, the dwell time in the uncoupled state. Each group of ablated animals was tested in parallel with a distinct set of sham operated controls to minimize the effects of variation between populations. Error bars for dwell times are not shown because statistical significance was calculated using the likelihood ratio test (see Table 4 legend), which does not generate sem estimates, and calculation of confidence intervals would have required an excessive amount of computation time. Stars indicate p<0.05 without ($⋆$) or with ($⋆⋆$) correction for multiple comparisons (Table 4).

**Table 2.**
 Synaptic weights derived from the transition rate constants. The rate constants were taken from Table 1, column A. Two values of the fundamental switching time, A, corresponding to the minimum (0.40 Hz) and maximum (0.86 Hz) values consistent with the ablation results were used in Materials and methods, Equations 36–38 to calculate the corresponding synaptic weights.


<table>
  <thead>
    <tr>
      <th></th>
      <th>A= 0.4 Hzmean ± sem (n = 5)</th>
      <th>A= 0.86 Hzmean ± sem (n = 5)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>hℱ</td>
      <td>1.01 ± 0.08</td>
      <td>0.25 ± 0.08</td>
    </tr>
    <tr>
      <td>hℛ</td>
      <td>1.09 ± 0.08</td>
      <td>0.32 ± 0.08</td>
    </tr>
    <tr>
      <td>wℱℛ</td>
      <td>-5.40 ± 0.43</td>
      <td>-5.40 ± 0.43</td>
    </tr>
    <tr>
      <td>wℛℱ</td>
      <td>-0.81 ± 0.06</td>
      <td>-0.81 ± 0.06</td>
    </tr>
    <tr>
      <td>wℱℱ</td>
      <td>-0.22 ± 0.06</td>
      <td>1.31 ± 0.06</td>
    </tr>
    <tr>
      <td>wℛℛ</td>
      <td>1.90 ± 0.33</td>
      <td>3.43 ± 0.33</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Effects of command neuron ablations on undulation frequency, forward velocity and reverse velocity. Values were computed separately for each worm and are shown as mean ± sem (n = 19–29 ). Undulation frequency was estimated as one-half of the reciprocal of the time of the first local minimum in the heading autocorrelation function. All p-values are from two-tailed t-tests and are shown without correction for multiple comparisons. Blue denotes significance at p<0.05. Red denotes significance at p<0.05 after Bonferroni correction for 15 comparisons.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3">Undulation frequency (Hz)</th>
      <th colspan="3">Forward velocity (μm/s)</th>
      <th colspan="3">Reverse velocity (μm/s)</th>
    </tr>
    <tr>
      <th>Neuron</th>
      <th>Class</th>
      <th>Sham</th>
      <th>Ablated</th>
      <th>p &lt;</th>
      <th>Sham</th>
      <th>Ablated</th>
      <th>p &lt;</th>
      <th>Sham</th>
      <th>Ablated</th>
      <th>p &lt;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AVB</td>
      <td>Forward</td>
      <td>0.355 ± 0.009</td>
      <td>0.230 ± 0.007</td>
      <td>7x10-11</td>
      <td>236 ± 6</td>
      <td>109 ± 4</td>
      <td>5x10-20</td>
      <td>-327 ± 7</td>
      <td>-302 ± 8</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>PVC</td>
      <td>Forward</td>
      <td>0.283 ± 0.011</td>
      <td>0.290 ± 0.010</td>
      <td>0.5</td>
      <td>187 ± 7</td>
      <td>192 ± 7</td>
      <td>0.7</td>
      <td>-253 ± 8</td>
      <td>-248 ± 6</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>AVD</td>
      <td>Reverse</td>
      <td>0.270 ± 0.008</td>
      <td>0.236 ± 0.008</td>
      <td>0.009</td>
      <td>173 ± 6</td>
      <td>141 ± 5</td>
      <td>0.0002</td>
      <td>-243 ± 4</td>
      <td>-229 ± 5</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>AVA</td>
      <td>Reverse</td>
      <td>0.302 ± 0.005</td>
      <td>0.254 ± 0.009</td>
      <td>4x10-5</td>
      <td>195 ± 5</td>
      <td>155 ± 7</td>
      <td>4x10-5</td>
      <td>-293 ± 7</td>
      <td>-69 ± 3</td>
      <td>3x10-22</td>
    </tr>
    <tr>
      <td>AVE</td>
      <td>Reverse</td>
      <td>0.264 ± 0.007</td>
      <td>0.256 ± 0.008</td>
      <td>0.6</td>
      <td>165 ± 4</td>
      <td>160 ± 5</td>
      <td>0.5</td>
      <td>-235 ± 4</td>
      <td>-211 ± 6</td>
      <td>0.003</td>
    </tr>
  </tbody>
</table>

A previous study found that ablating a subset of the reverse command neurons (AVAL and AVAR) reduces dwell time in the reverse state but also paradoxically reduces dwell time in the forward state (Zheng et al., 1999). Similarly paradoxical effects have been reported following ablation of the reciprocally connected brain stem nuclei that regulate sleep and wakefulness (Saper et al., 2010). The stochastic switch model predicts and explains such effects. In principle, the ablation of a subset of neurons in a pool of co-active neurons can have widespread effects on the pool’s overall input and output connectivity. Widespread effects can be expected because ablation removes not only the outgoing synaptic connections from the ablated neurons, but also the targets of incoming synaptic connections. In the C. elegans command neuron network, ablating a reverse command neuron such as AVA potentially reduces four of the six weights in the network: $h_{ℛ}$, $w_{ℛℛ}$, $w_{ℛℱ}$, and $w_{ℱℛ}$. Thus, a single ablation can move the system a considerable distance in weight space toward the uncoupled state in which all weights are zero. In the limiting case of a fully uncoupled network, all dwell times approach a value of $1/2A$, where $A$ is the intrinsic switching time of the stochastic units (see Materials and methods, equations 31–34); henceforth we will use $d_{0}$ to denote the uncoupled dwell time. Dwell times that in intact animals are greater than $d_{0}$ will be reduced by ablation, whereas dwell times that are less than $d_{0}$ will be increased. In particular, if $d_{F}$ and $d_{R}$ are both greater than $d_{0}$, ablation of a reverse command neuron is expected to reduce both dwell times; the same is true for ablation of a forward command neuron. Thus the observed paradoxical effects of ablations are to be expected if $d_{0}$ is below $d_{F}$ and $d_{R}$.

To determine the actual relationship between d0 and dwell times in the forward and reverse state, we estimated the rate constants in ablated animals and sham operated controls, and computed the corresponding dwell times (Figure 5B; Table 4). Dwell times in F and R, if significantly altered by the ablation (⋆⋆), were reduced, indicating that d0 is indeed below dF and dR. Additionally, dwell times in the pause states dX and dY were increased, with one exception (dY, AVB). Thus, the observed pattern of dwell time changes is consistent, overall, with a value of d0 that is between the dwell times of the movement states and the dwell times of the pause states. This finding allowed us to place bounds on d0. Specifically, d0 must be less than or equal to the lowest post-ablation value of dR, and greater than or equal to the largest post-ablation value of dX; thus, 0.58 ≤ d0 ≤ 1.24 sec. Furthermore, because A=1/2d0, we can infer that 0.40 Hz ≤ A ≤ 0.86 Hz. This inequality provides an estimate of the fundamental time scale of stochastic switching in C. elegans locomotion. For subsequent analysis, we defined Amin= 0.40 Hz and Amax= 0.86 Hz.

**Table 4.**
 Effects of command neuron ablations on model parameters. The sign of the change (Δ) caused by the ablation is shown as “+” if the value moved away from 0, “–” if the value moved towards 0. Significance was determined using the likelihood ratio test (Weisstein, Eric W. "Likelihood Ratio." From MathWorld--A Wolfram Web Resource. http://mathworld.wolfram. com/LikelihoodRatio.html), which is based on the reduction in likelihood caused by constraining one of the parameters to have the same value in both the ablated cohort and the corresponding sham cohort. The unconstrained fit thus had 12 free parameters (6 for each of the 2 cohorts being compared), while the constrained fit had 11 free parameters. For example, to test the significance of the change in the mean dwell time in the pause state ($d_{P}=(p_{X}d_{X}+p_{Y}d_{Y})/(p_{X}+p_{Y})$) caused by ablation of the AVA neuron pair, two cohorts (ablated and sham) were grown and tested under identical conditions. The ln likelihood with 12 free parameters was found to be 894794.075. When $d_{P}$ was constrained to be the same for both cohorts, the ln likelihood for the 11 parameter fit was found to be 894784.676. The test statistic $D=2\times(894794.075−894784.676)=18.798$ was assumed to come from a chi-squared distribution with one degree of freedom, which yielded $p=1.45\times10^{−5}$ (shown in the table as $p<10^{−4}$). The constrained fitting process was repeated in turn for each ablation/sham pair for each of the 9 rows shown in the table. All p-values are shown without correction for multiple comparisons. Blue denotes significance at p<0.05. Red denotes significance at p<0.05 after Bonferroni correction for 27 comparisons


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="12">REVERSE</th>
      <th colspan="8">FORWARD</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="4">AVE</th>
      <th colspan="4">AVD</th>
      <th colspan="4">AVA</th>
      <th colspan="4">AVB</th>
      <th colspan="4">PVC</th>
    </tr>
    <tr>
      <th></th>
      <th>Sham</th>
      <th>Ablate</th>
      <th>∆</th>
      <th>p&lt;</th>
      <th>Sham</th>
      <th>Ablate</th>
      <th>∆</th>
      <th>p&lt;</th>
      <th>Sham</th>
      <th>Ablate</th>
      <th>∆</th>
      <th>p&lt;</th>
      <th>Sham</th>
      <th>Ablate</th>
      <th>∆</th>
      <th>p&lt;</th>
      <th>Sham</th>
      <th>Ablate</th>
      <th>∆</th>
      <th>p&lt;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>dF (s)</td>
      <td>5.455</td>
      <td>5.221</td>
      <td>–</td>
      <td>0.2</td>
      <td>5.158</td>
      <td>4.081</td>
      <td>–</td>
      <td>10-15</td>
      <td>6.730</td>
      <td>3.143</td>
      <td>–</td>
      <td>10-99</td>
      <td>7.289</td>
      <td>2.642</td>
      <td>–</td>
      <td>10-99</td>
      <td>6.058</td>
      <td>6.558</td>
      <td>+</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>dR (s)</td>
      <td>3.019</td>
      <td>2.436</td>
      <td>–</td>
      <td>10-6</td>
      <td>2.540</td>
      <td>2.367</td>
      <td>–</td>
      <td>0.05</td>
      <td>2.359</td>
      <td>1.243</td>
      <td>–</td>
      <td>10-41</td>
      <td>2.127</td>
      <td>1.681</td>
      <td>–</td>
      <td>10-6</td>
      <td>2.842</td>
      <td>2.396</td>
      <td>–</td>
      <td>0.0005</td>
    </tr>
    <tr>
      <td>dX (s)</td>
      <td>0.548</td>
      <td>0.548</td>
      <td>–</td>
      <td>1</td>
      <td>0.514</td>
      <td>0.520</td>
      <td>+</td>
      <td>0.6</td>
      <td>0.480</td>
      <td>0.582</td>
      <td>+</td>
      <td>10-7</td>
      <td>0.370</td>
      <td>0.437</td>
      <td>+</td>
      <td>10-6</td>
      <td>0.457</td>
      <td>0.508</td>
      <td>+</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>dY (s)</td>
      <td>0.229</td>
      <td>0.263</td>
      <td>+</td>
      <td>0.002</td>
      <td>0.229</td>
      <td>0.241</td>
      <td>+</td>
      <td>0.07</td>
      <td>0.214</td>
      <td>0.331</td>
      <td>+</td>
      <td>10-7</td>
      <td>0.197</td>
      <td>0.144</td>
      <td>–</td>
      <td>10-7</td>
      <td>0.220</td>
      <td>0.226</td>
      <td>+</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>dP (s)</td>
      <td>0.495</td>
      <td>0.496</td>
      <td>+</td>
      <td>1</td>
      <td>0.460</td>
      <td>0.468</td>
      <td>+</td>
      <td>0.5</td>
      <td>0.437</td>
      <td>0.510</td>
      <td>+</td>
      <td>10-4</td>
      <td>0.331</td>
      <td>0.416</td>
      <td>+</td>
      <td>10-11</td>
      <td>0.410</td>
      <td>0.457</td>
      <td>+</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>pF</td>
      <td>0.720</td>
      <td>0.747</td>
      <td>+</td>
      <td>0.004</td>
      <td>0.723</td>
      <td>0.689</td>
      <td>–</td>
      <td>0.0005</td>
      <td>0.809</td>
      <td>0.704</td>
      <td>–</td>
      <td>10-24</td>
      <td>0.818</td>
      <td>0.745</td>
      <td>–</td>
      <td>10-15</td>
      <td>0.749</td>
      <td>0.787</td>
      <td>+</td>
      <td>0.0002</td>
    </tr>
    <tr>
      <td>pR</td>
      <td>0.192</td>
      <td>0.158</td>
      <td>–</td>
      <td>10-4</td>
      <td>0.188</td>
      <td>0.203</td>
      <td>+</td>
      <td>0.05</td>
      <td>0.122</td>
      <td>0.137</td>
      <td>+</td>
      <td>0.04</td>
      <td>0.129</td>
      <td>0.120</td>
      <td>–</td>
      <td>0.2</td>
      <td>0.181</td>
      <td>0.139</td>
      <td>–</td>
      <td>10-9</td>
    </tr>
    <tr>
      <td>pX</td>
      <td>0.073</td>
      <td>0.078</td>
      <td>+</td>
      <td>0.07</td>
      <td>0.072</td>
      <td>0.088</td>
      <td>+</td>
      <td>10-7</td>
      <td>0.058</td>
      <td>0.113</td>
      <td>+</td>
      <td>10-9</td>
      <td>0.041</td>
      <td>0.125</td>
      <td>+</td>
      <td>10-99</td>
      <td>0.056</td>
      <td>0.061</td>
      <td>+</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>pY</td>
      <td>0.014</td>
      <td>0.017</td>
      <td>+</td>
      <td>0.02</td>
      <td>0.017</td>
      <td>0.020</td>
      <td>+</td>
      <td>0.005</td>
      <td>0.011</td>
      <td>0.046</td>
      <td>+</td>
      <td>10-23</td>
      <td>0.012</td>
      <td>0.010</td>
      <td>–</td>
      <td>0.01</td>
      <td>0.014</td>
      <td>0.013</td>
      <td>–</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>

### Synaptic weights in the stochastic switch model

Having placed bounds on A, we were able to compute synaptic weights in the model (Table 2). This was done by deriving expressions for the weights in terms of the rate constants (Materials and methods, Equations 36–38) and substituting into these equations our estimates of rate constants together with the values of Amin and Amax. We found that input weights, hℱ and hℛ, are small and positive, suggesting that these inputs may provide modest but steady excitation to the system (Figure 6A). The self-connections wℱℱ and wℛℛ are also mainly positive, indicating that the ON states may be stabilized by intrinsic or extrinsic positive feedback. The cross-connections wℱℛ and wℛℱ are negative, indicating reciprocal inhibition, as expected for neurons that activate opposing behavioral states. Furthermore, the magnitude of wℱℛ is greater than the magnitude of wℛℱ, suggesting that the animal spends more time in the forward state than the reverse state in part because the forward neurons inhibit the reverse neurons more strongly than the reverse neurons inhibit the forward neurons.

![Figure 6.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig6-v2.jpg)

**Figure 6.:** (A) Synaptic weights (mean ± sem, n = 5 cohorts) from maximum likelihood fits to velocity data from wild type worms. (B, C) Left, synaptic current in AVB or AVA when the indicated presynaptic neuron was photoactivated (blue line). Right, mean synaptic current during the first 100 ms of the stimulus plotted against holding potential in the postsynaptic neuron (I-V curve). Lines show linear fits to the data at negative holding potentials which were used to estimate $v_{Rev}$. (D), Zero-current holding potential and reversal potential of synaptic currents (mean ± sem) in the indicated postsynaptic neuron (paired t-tests: AVA to AVB, p= 0.043, n = 9; AVB to AVA, p= 0.019, n = 17). (E), Scatter plot of synaptic currents recorded at a holding potential of -15 mV (unpaired t-test: p= 0.010, n ≥ 25).

Synaptic weights in an abstract network model such as this one, where neuronal state is activation rather than voltage, are not generally interpretable as synaptic conductances. Rather, they represent the functional effects of one neuron on another, such as the degree of excitation or inhibition produced by a unit change in activation. Thus, synaptic weights in the Stochastic Switch model cannot be said to predict the magnitude of synaptic conductances, but they can be said to predict aspects of functional connectivity in certain cases. For example, as command neurons AVA and AVB are behaviorally much more important than the others (Chalfie et al., 1985) (see also Figure 5A,B), it is reasonable to assume that the signs of their functional synaptic connections match the signs of the net functional connections in the biological network. Thus, the model predicts reciprocal inhibition (Qi et al., 2012) between AVA and AVB under this assumption. We tested this prediction by photoactivating either AVA or AVB with channelRhodopsin-2 and recording electrophysiologically from AVB or AVA, respectively (Figure 6B,C). We found that the reversal potential of optically induced synaptic currents in AVA and AVB was more negative than the zero-current potential in these neurons (Figure 6B,C,D), indicating synaptic inhibition as predicted by the model. This inhibition is likely to be monosynaptic as C. elegans command neurons are cholinergic and express inhibitory postsynaptic receptors that respond to acetylcholine (Pereira et al., 2015). Additionally, the connection from AVB to AVA appeared to be stronger than the connection from AVA to AVB (Figure 6E), measured in terms of the amplitude of the synaptic current at a holding potential approximately equal to the membrane potential when command neurons are in their depolarized state (Figure 2B). However, we do not exclude the possibility that AVB was more strongly activated than AVA as a result of differential expression of the photoprobe. These findings demonstrate the feasibility of using the worm’s velocity, $v(t)$, a simple behavioral measure, to predict functional synaptic connections between populations of neurons in a biological neural network, at least under certain assumptions concerning the relationship between model network weights and physiological synaptic strengths.

### Genetic effects on command neuron function

Two classes of ion channel mutants that affect membrane conductances in the command neurons are also known to alter locomotory behavior in systematic ways, thus providing key insights into command neuron function (Zheng et al., 1999). The hyperpolarizing class (“HYP”) comprises three genotypes in which release of the excitatory neurotransmitter glutamate, presumed to be tonic, is disrupted by mutations that affect either presynaptic (eat-4(ad572), eat-4(ky5)) or postsynaptic mechanisms (glr-1(n2461)). These mutations are hypothesized to cause chronic hyperpolarization of the command neurons by reducing depolarizing currents. The depolarizing class (“DEP”) comprises two genotypes in which a constitutively activated glutamate receptor is expressed in the command neurons (glr-1::glr-1(A/T), nmr-1::glr-1(A/T)). These mutants are hypothesized to chronically depolarize the command neurons.

We found that the frequency of locomotory undulations was decreased in HYP mutants and increased in DEP mutants compared to wild-type controls (Table 5), consistent with the likely effects of respectively increasing and decreasing tonic drive to the presumptive pattern generator for locomotion. Importantly, however, it is possible that both classes of mutation also alter the input resistance of the command neurons. The closure or removal of glutamate receptors in HYP mutants should increase input resistance whereas the introduction of constitutively active glutamate receptors in DEP mutants should decrease it. Thus, the previously observed effects of these mutations on locomotory state transitions (Zheng et al., 1999) could be the result of changes in membrane potential (ΔV), input resistance (Δr), or both.

**Table 5.**
 Effects of mutations on mean undulation frequency, mean forward velocity and mean reverse velocity.Values were computed separately for each worm and are shown as mean ± sem (n = 25–31). Undulation frequency was estimated as one-half of the reciprocal of the time of the first local minimum in the heading autocorrelation function. All p-values are from two-tailed t-tests and are shown without correction for multiple comparisons. Blue denotes significance at p<0.05. Red denotes significance at p<0.05 after Bonferroni correction for 15 comparisons.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3">Undulation frequency (Hz)</th>
      <th colspan="3">Forward velocity (μm/s)</th>
      <th colspan="3">Reverse velocity (μm/s)</th>
    </tr>
    <tr>
      <th>Genotype</th>
      <th>Class</th>
      <th>Wild type</th>
      <th>Mutant</th>
      <th>p &lt;</th>
      <th>Wild type</th>
      <th>Mutant</th>
      <th>p &lt;</th>
      <th>Wild type</th>
      <th>Mutant</th>
      <th>p &lt;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>eat-4(ad572)</td>
      <td>HYP A</td>
      <td>0.272 ± 0.011</td>
      <td>0.222 ± 0.007</td>
      <td>4x10-4</td>
      <td>156 ± 5</td>
      <td>122 ± 4</td>
      <td>1x10-5</td>
      <td>-228 ± 5</td>
      <td>-236 ± 9</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>eat-4(ky5)</td>
      <td>HYP B</td>
      <td>0.317 ± 0.011</td>
      <td>0.256 ± 0.009</td>
      <td>2x10-4</td>
      <td>184 ± 7</td>
      <td>143 ± 6</td>
      <td>5x10-5</td>
      <td>-262 ± 10</td>
      <td>-271 ± 7</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>glr-1(n2461)</td>
      <td>HYP C</td>
      <td>0.294 ± 0.008</td>
      <td>0.291 ± 0.010</td>
      <td>0.9</td>
      <td>158 ± 5</td>
      <td>166 ± 6</td>
      <td>0.3</td>
      <td>-236 ± 6</td>
      <td>-236 ± 5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>glr-1::glr-1(A/T)</td>
      <td>DEP A</td>
      <td>0.272 ± 0.011</td>
      <td>0.642 ± 0.029</td>
      <td>6x10-13</td>
      <td>156 ± 5</td>
      <td>112 ± 5</td>
      <td>3x10-7</td>
      <td>-228 ± 5</td>
      <td>-143 ± 5</td>
      <td>2x10-15</td>
    </tr>
    <tr>
      <td>nmr-1::glr-1(A/T)</td>
      <td>DEP B</td>
      <td>0.294 ± 0.008</td>
      <td>0.695 ± 0.037</td>
      <td>2x10-12</td>
      <td>158 ± 5</td>
      <td>138 ± 5</td>
      <td>0.011</td>
      <td>-236 ± 6</td>
      <td>-144 ± 5</td>
      <td>7x10-15</td>
    </tr>
  </tbody>
</table>

Changes in membrane potential and input resistance can both be represented in the stochastic switch model by changes in synaptic weights. We modeled the effects of ΔV by adding an increment $\Deltah$ ($−1\leq\Deltah\leq$ 1) to wild type $h$ values, with negative $\Deltah$ for HYP mutations and positive $\Deltah$ for DEP mutations. We modeled the effect of Δr as a change in the magnitude of synaptic weights ($h$ and $w$ quantities). This representation of Δr is appropriate because changes in input resistance alter the magnitude of the voltage change that would be produced by a fixed postsynaptic current. All weights were scaled by a common factor $z$ (1 < $z$ < 2 for HYP mutants; 0 < $z$ < 1 for DEP mutants).

Here we consider the effects of ΔV and Δr on dwell times in the stochastic switch model to enable direct comparison with the original study of HYP and DEP strains (Zheng et al., 1999). Dwell times can be written as functions of weights:

$$
d_{X}=a_{XF}+a_{XR}^{-1}=[A exp(h_{ℱ})+A exp(h_{ℛ})]^{−1}                                                           
$$

$$
d_{F}=a_{FX}+a_{FY}^{-1}=[A exp(−h_{ℱ}−w_{ℱℱ})+A exp(h_{ℛ}+w_{ℱℛ})]^{−1}                             
$$

$$
d_{R}=a_{RX}+a_{RY}^{-1}=[A exp(−h_{ℛ}−w_{ℛℛ})+A exp(h_{ℱ}+w_{ℛℱ})]^{−1}                              
$$

$$
d_{Y}=a_{YR}+a_{YF}^{-1}=[A exp(−h_{ℱ}−w_{ℱℱ}−w_{ℛℱ})+A exp(−h_{ℛ}−w_{ℛℛ}−w_{ℱℛ})]^{−1}
$$

These equations show that the ΔV and Δr hypotheses make qualitatively distinct predictions. The simplest case is dwell dX, which depends only on hℱand hℛ. Equation 1 shows that dX rises and falls as h terms are made more negative or positive, respectively. Thus, under the ΔV hypothesis, dX should rise in HYP mutants and fall in DEP mutants (Figure 7A, row 4). In contrast, under the Δr hypothesis, in which weight magnitudes (w and h) decrease in DEP mutants and increase in HYP mutants, dX should rise in DEP mutants and fall in HYP. To distinguish between these hypotheses, we measured dwell times in mutants and wild type animals during local search. The pattern of observed changes in dX matched the pattern predicted by the ΔV hypothesis but not the Δr hypothesis (Figure 7C, row 4). Thus, the effects of membrane potential appear to dominate the effects of changes in synaptic strength in the case of mutant values of dX.

![Figure 7.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig7-v2.jpg)

**Figure 7.:** (A) Predicted effects of changes in membrane potential. (B ) Predicted effects of changes in input resistance. (C) Dwell times in F, R, and P for cohorts of HYP mutants, DEP mutants, and wild type animals. Stars indicate significant change in dwell time (p<0.05 without ($⋆$) or with ($⋆⋆$) correction for multiple comparisons; Table 6). In A-C wild type dwell times are indicated by gray bars. Horizontal lines indicate the estimated range of $d_{0}$, the dwell time in the uncoupled state. In the ΔV model, $h$ terms were made more negative to model HYP mutants and more positive to model DEP mutants by subtracting or adding a constant $\Deltah$ = 0.6; qualitatively similar results were obtained for 0 < $\Deltah$ ≤ 0.8. In the Δr model, $h$ and $w$ terms were scaled by (1 + f) to model HYP mutants and by (1 - f) to model DEP mutants, with f = 0.6; qualitatively similar results were obtained for 0 < f ≤ 1. Strains, HYP A: DA572 eat-4(ad572); HYP B: MT6308 eat-4(ky5); HYP C: KP4 glr-1(n2461); DEP A: VM1136 lin-15(n765); akIs9 [lin-15(+), Pglr-1::GLR-1(A/T)]; DEP B: VM188 lin-15(n765); akEx52[lin-15(+), Pnmr-1::GLR-1(A/T)].

**Table 6.**
 Effects of mutations on model parameters. Significance was determined using the likelihood ratio test as described in Table 4. The sign of the change (Δ) caused by the mutation is shown as “+” if the value moved away from 0, “–” if the value moved towards 0. All p-values are shown without correction for multiple comparisons. Blue denotes significance at p<0.05. Red denotes significance at p<0.05 after Bonferroni correction for 27 comparisons.


<table>
  <thead>
    <tr>
      <th rowspan="3"></th>
      <th colspan="12">HYP</th>
      <th colspan="8">DEP</th>
    </tr>
    <tr>
      <th colspan="4">HYP A: eat-4(ad572)</th>
      <th colspan="4">HYP B: eat-4(ky5)</th>
      <th colspan="4">HYP C: glr-1(n2461)</th>
      <th colspan="4">DEP A: glr-1::glr-1(A/T)</th>
      <th colspan="4">DEP B: nmr-1::glr-1(A/T)</th>
    </tr>
    <tr>
      <th>Control</th>
      <th>Mutant</th>
      <th>∆</th>
      <th>p &lt;</th>
      <th>Control</th>
      <th>Mutant</th>
      <th>∆</th>
      <th>p&lt;</th>
      <th>Control</th>
      <th>Mutant</th>
      <th>∆</th>
      <th>p&lt;</th>
      <th>Control</th>
      <th>Mutant</th>
      <th>∆</th>
      <th>p&lt;</th>
      <th>Control</th>
      <th>Mutant</th>
      <th>∆</th>
      <th>p&lt;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>dF (s)</td>
      <td>4.771</td>
      <td>9.564</td>
      <td>+</td>
      <td>10-87</td>
      <td>4.956</td>
      <td>8.643</td>
      <td>+</td>
      <td>10-64</td>
      <td>5.181</td>
      <td>7.871</td>
      <td>+</td>
      <td>10-33</td>
      <td>4.771</td>
      <td>0.940</td>
      <td>–</td>
      <td>10-99</td>
      <td>5.181</td>
      <td>0.742</td>
      <td>–</td>
      <td>10-99</td>
    </tr>
    <tr>
      <td>dR (s)</td>
      <td>2.043</td>
      <td>2.821</td>
      <td>+</td>
      <td>10-7</td>
      <td>1.910</td>
      <td>2.769</td>
      <td>+</td>
      <td>10-12</td>
      <td>2.018</td>
      <td>3.004</td>
      <td>+</td>
      <td>10-16</td>
      <td>2.045</td>
      <td>0.875</td>
      <td>–</td>
      <td>10-99</td>
      <td>2.018</td>
      <td>0.709</td>
      <td>–</td>
      <td>10-9 9</td>
    </tr>
    <tr>
      <td>dX (s)</td>
      <td>0.481</td>
      <td>1.040</td>
      <td>+</td>
      <td>0.005</td>
      <td>0.529</td>
      <td>0.844</td>
      <td>+</td>
      <td>10-43</td>
      <td>0.459</td>
      <td>0.727</td>
      <td>+</td>
      <td>10-39</td>
      <td>0.482</td>
      <td>0.328</td>
      <td>–</td>
      <td>10-49</td>
      <td>0.460</td>
      <td>0.235</td>
      <td>–</td>
      <td>10-99</td>
    </tr>
    <tr>
      <td>dY (s)</td>
      <td>0.247</td>
      <td>0.382</td>
      <td>+</td>
      <td>10-5</td>
      <td>0.238</td>
      <td>0.290</td>
      <td>+</td>
      <td>0.005</td>
      <td>0.221</td>
      <td>0.164</td>
      <td>–</td>
      <td>10-5</td>
      <td>0.247</td>
      <td>0.097</td>
      <td>–</td>
      <td>10-93</td>
      <td>0.221</td>
      <td>0.079</td>
      <td>–</td>
      <td>10-99</td>
    </tr>
    <tr>
      <td>dP (s)</td>
      <td>0.428</td>
      <td>0.982</td>
      <td>+</td>
      <td>10-99</td>
      <td>0.466</td>
      <td>0.793</td>
      <td>+</td>
      <td>10-52</td>
      <td>0.409</td>
      <td>0.677</td>
      <td>+</td>
      <td>10-43</td>
      <td>0.428</td>
      <td>0.286</td>
      <td>–</td>
      <td>10-61</td>
      <td>0.409</td>
      <td>0.204</td>
      <td>–</td>
      <td>10-99</td>
    </tr>
    <tr>
      <td>pF</td>
      <td>0.729</td>
      <td>0.839</td>
      <td>+</td>
      <td>10-27</td>
      <td>0.734</td>
      <td>0.832</td>
      <td>+</td>
      <td>10-26</td>
      <td>0.755</td>
      <td>0.785</td>
      <td>+</td>
      <td>0.003</td>
      <td>0.728</td>
      <td>0.410</td>
      <td>–</td>
      <td>10-99</td>
      <td>0.755</td>
      <td>0.407</td>
      <td>–</td>
      <td>10-99</td>
    </tr>
    <tr>
      <td>pR</td>
      <td>0.177</td>
      <td>0.062</td>
      <td>–</td>
      <td>10-37</td>
      <td>0.167</td>
      <td>0.079</td>
      <td>–</td>
      <td>10-29</td>
      <td>0.161</td>
      <td>0.135</td>
      <td>–</td>
      <td>10-4</td>
      <td>0.177</td>
      <td>0.389</td>
      <td>+</td>
      <td>10-99</td>
      <td>0.161</td>
      <td>0.404</td>
      <td>+</td>
      <td>10-99</td>
    </tr>
    <tr>
      <td>pX</td>
      <td>0.073</td>
      <td>0.090</td>
      <td>+</td>
      <td>10-5</td>
      <td>0.077</td>
      <td>0.081</td>
      <td>+</td>
      <td>0.3</td>
      <td>0.067</td>
      <td>0.073</td>
      <td>+</td>
      <td>0.03</td>
      <td>0.073</td>
      <td>0.164</td>
      <td>+</td>
      <td>10-99</td>
      <td>0.067</td>
      <td>0.151</td>
      <td>+</td>
      <td>10-99</td>
    </tr>
    <tr>
      <td>pY</td>
      <td>0.022</td>
      <td>0.009</td>
      <td>–</td>
      <td>10-13</td>
      <td>0.021</td>
      <td>0.008</td>
      <td>–</td>
      <td>10-25</td>
      <td>0.018</td>
      <td>0.007</td>
      <td>–</td>
      <td>10-27</td>
      <td>0.022</td>
      <td>0.037</td>
      <td>+</td>
      <td>10-21</td>
      <td>0.018</td>
      <td>0.037</td>
      <td>+</td>
      <td>10-41</td>
    </tr>
  </tbody>
</table>

In contrast to $d_{X}$, $d_{F}$ and $d_{R}$ depend on $w$ terms as well as $h$ terms. Under the ΔV hypothesis, the $h$ terms but not the $w$ terms would be affected by the mutations. Positive and negative increments in $h$ have the effects shown in Figure 7A, rows 1 and 2; $d_{F}$ and $d_{R}$ are predicted to shift in opposite directions. Changes in $d_{F}$ are dominated by the effects of $h_{ℱ}$ on the first term in Equation 2 (which represents $a_{FX}$) because the second term in the equation (which represents $a_{FY}$) remains close to zero in the mutants. Analogously, changes in $d_{R}$ are dominated by the effects of $h_{ℱ}$ on the second term in Equation 3 ($a_{RY}$) because the first term in the equation ($a_{RX}$) remains close to zero in the mutants.

The Δr hypothesis makes a distinctly different prediction. In this version of the model, $w$ terms and $h$ terms would both be affected by the mutations. Now, the predicted pattern of dwell time changes across both $d_{F}$ and $d_{R}$ is such the both dwell times shift in the same direction (Figure 7B, rows 1 and 2); specifically, dwell times in DEP and HYP mutants move toward or away from their uncoupled dwell times, respectively. Taken together, the pattern of observed changes in $d_{F}$ and $d_{R}$ matched the pattern predicted by the Δr hypothesis (Figure 7C, rows 1 and 2) but not the ΔV hypothesis. We conclude that changes in synaptic strength may dominate the effects of changes in membrane potential on mutant values of $d_{F}$ and $d_{R}$.

Neither hypothesis predicts the observed changes in $d_{Y}$ (Figure 7C, row 5) which resembled the pattern of changes in $d_{X}$ (Figure 7C, row 4). However, the ΔV hypothesis correctly predicts observed dwell times in the overall pause state $d_{P}$ (Figure 7C row 3). This is because $d_{P}$ is dominated by $d_{X}$ and changes in $d_{X}$ are well-predicted by the ΔV model as noted above. Overall, our analysis of the effects of HYP and DEP mutations in terms of the Stochastic Switch Model points to a role for changes in both membrane potential and input resistance in regulating dwell times.

### Regulation of search scale

The Stochastic Switch Model immediately suggests a family of models for the regulation of the spatial scale of random search in response to the availability of food and the worm’s physiological state. The scale of random search is determined primarily by $m_{F}$, the mean distance traveled during a forward run. In C. elegans, a run begins with a transition from state R (via P) into state F and continues until the next transition into state R. Any run may include one or more visits to state P, but FPF transitions are not usually associated with changes in heading. In terms of the Stochastic Switch Model, $m_{F}=v_{F}¯p_{F}/f_{RPF}$, where $v_{F}¯$ is the average velocity in state F, $p_{F}$ is the probability of being in state F, and $f_{RPF}$ is the frequency of RPF transitions (Materials and methods, Equation 39), which coincide with random reorientations. Importantly, under the approximation $a_{FY}≅0$ (Table 1, column A), $m_{F}$ is can be expressed as a function of just three of the six weights in the network:

$$
m_{F}≅\frac{v_{F}}{A}¯·\frac{exp(h_{ℱ})+exp(h_{ℛ})}{exp(h_{ℛ}−h_{ℱ}−w_{ℱℱ})}
$$

We refer to these weights as potential control points in the network. In a minimal model of search scale regulation, mF could be controlled by sensory inputs represented by hℱ and hℛ (Figure 8A).

![Figure 8.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig8-v2.jpg)

**Figure 8.:** (A) Plot of mean forward run length versus the weights $h_{ℱ}$ and $h_{ℛ}$, illustrating a minimal model of search-scale regulation. (B-H) Calculated effects on search mode of the weights indicated in parentheses. The frequency of reversals ($f_{FPR}$) is plotted against $m_{F}$ while these three weights are scanned from -6 to 6 weight units in steps of 0.4. Each point was categorized as cropping (magenta), local search (green), ranging (blue), or indeterminate (grey) according to value of $f_{FPR}$ and $m_{F}$, and whether or not the associated value of $m_{R}$ (not shown) indicated a short or long reversal; see Materials and methods for definitions of search modes. Yellow diamonds mark the scanned points modeled in Figure 8—figure supplement 1. $A$ = 1 Hz; similar results were obtained for $A=A_{max}$ and $A=A_{min}$ (Table 7).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** ( A-C ) Simulated time is 600 sec with four replicated per panel, each in a different color. $A=A_{max}$; similar results were obtained for $A=A_{min}$.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** (A) Circuitry. Behavioral state (F, R, or P) was determined by a modified version of the Stochastic Switch Model in which on and off chemosensory neurons regulated the values of the inputs to the network. During movement up the gradient, the activation states of the on and off cells were set to 1 and 0, respectively, such that $h_{ℱ}(t)=h_{ℱ}+\Deltah_{ℱ}$ and $h_{ℛ}(t)=h_{ℛ}−\Deltah_{ℛ}$, where $h_{ℱ}$ and $h_{ℛ}$ are the values of the inputs to the network during local search (Table 2). Conversely, during movement down the gradient, the on and off activation states, and the signs of $\Deltah$, were reversed. In the tracks shown, $\Deltah_{ℱ}$ and $\Deltah_{ℛ}$ were $\pm$ 2.6, the value that optimized chemotaxis performance given the speed of the model worm and standard deviation of the gradient. (B) Simulated chemotaxis. The concentration gradient of chemical attractant was modeled as a two dimensional Gaussian (std. dev. = 1.6 cm) originating at the center of a circular arena. Similar tracks were obtained across the full range of values of A, the fundamental time scale of the model.

Search scale ($m_{F}$) together with the frequency of reversals (FPR transitions), have been used to define the three search modes commonly recognized in C. elegans: cropping, local search, and ranging. To find minimal models for regulation of search mode, we performed exhaustive searches of subregions of network’s six-dimensional weight space. Subspaces, defined by one, two, or three weights, were scanned across a wide range of values (-6 ≤ $w$ ≤ 6) while other weights remained fixed at their wild type levels (Figure 7B–H). The performance of each configuration of the network was scored according to whether it matched the range of $m_{F}$ magnitudes and reversal frequencies characteristic of each mode (see Materials and methods). Another consideration was the number of distinct search modes available; accordingly, we also noted the density with which the plane defined by reversal frequency and $m_{F}$ was covered in the scan (Figure. 8B-H, gray symbols).

All three search modes were available in the subspace defined by the control points (hℱ,hℛ,wℱℱ) (Figure 8B, Figure 8—figure supplement 1). However, only cropping and local search were available in the complementary subspace (wℛℛ,wℱℛ,wℛℱ) (Figure 8C); thus, to achieve the full set of search modes, at least one of the weights in equation 5 must be free to change. None of the control-point weights was sufficient on its own to produce all three search modes (Figure 8D–F). Scanning the subspaces (hℱ, wℛℛ) and (hℛ, wℱℛ) showed these pairs of weights to be sufficient for all modes (Figure 8G,H), but a three-dimensional subspace containing at least one of the control-point weights was a necessary condition for both dense coverage of this plane and the presence of all three search modes (Table 7). We suggest that these three-weight subspaces constitute the most likely minimal models for the regulation of search in C. elegans. They could be tested by chronic manipulation of control-point weights utilizing a variety of approaches, such as chemical or optical probes that alter tonic inputs to the command network from sensory neurons and interneurons represented by the parameters hℱ and hℛ.

**Table 7.**
 Regulation of search mode. The weights in each subspace were scanned from -6 to 6 weight units in steps of 0.4 with $A=A_{min}$ or $A=A_{max}$. The letter x means that the indicated search mode was present for at least one point in the subspace when $A=A_{min}$ and when $A=A_{max}$; the letters y and z mean that the mode was present only when $A=A_{min}$ or $A=A_{max}$, respectively. See Materials and methods for definitions of search modes. Control-point weights as defined by the theoretical relationship between weights and search scale (Equation 5) are shown in bold. Only the three-weight subspaces are sufficient for producing all three search modes and full coverage of the plane defined by reversal frequency and $m_{F}$ plane as shown in Figure 8.


<table>
  <thead>
    <tr>
      <th>Subspace</th>
      <th>Cropping</th>
      <th>Dwelling</th>
      <th>Ranging</th>
      <th>Coverage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>hℱ</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>⋅ ⋅ ⋅</td>
    </tr>
    <tr>
      <td>hℛ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>⋅ ⋅ ⋅</td>
    </tr>
    <tr>
      <td>wFF</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>⋅ ⋅ ⋅</td>
    </tr>
    <tr>
      <td>wℛℛ</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>wℛℱ</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>wℱℛ</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℱ, wℛℛ</td>
      <td>y</td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℱ, wℱℛ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℱ, wℛℱ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℛ, wℛℛ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℛ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℛ, wℛℱ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>wFF, wℛℱ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>wFF, wℱℛ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>wFF, wℛℛ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℛ, wℱℱ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℱ, hℛ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>hℱ, wℱℱ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>wℛℛ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>.......</td>
    </tr>
    <tr>
      <td>wℛℛ, wℛℱ</td>
      <td></td>
      <td>y</td>
      <td></td>
      <td>. . .</td>
    </tr>
    <tr>
      <td>wℱℛ, wℛℱ</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, wℛℱ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℛ, wℛℱ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>wFF, wℛℱ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, wℛℛ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℛ, wℛℛ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>wFF, wℛℛ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, wℛℛ, wℛℱ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℛ, wℛℛ, wℛℱ</td>
      <td>z</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>wFF, wℛℛ, wℛℱ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, hℛ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, hℛ, wℛℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, hℛ, wℛℱ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, wFF, wℛℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, wFF, wℱℛ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, wFF, wℛℱ</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℛ, wFF, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℛ, wFF, wℛℱ</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℛ, wFF, wℛℛ</td>
      <td>y</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>hℱ, hℛ, wFF</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>.......</td>
    </tr>
    <tr>
      <td>wℛℛ, wℛℱ, wℱℛ</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>.......</td>
    </tr>
  </tbody>
</table>

### Biased random walks

Mean forward run length is also modulated during biased random walks, increasing or decreasing when the animal is moving in a favorable or unfavorable direction, respectively (Pierce-Shimomura et al., 1999; Block et al., 1982; Iino and Yoshida, 2009; Luo et al., 2014). When C. elegans is engaged in chemotaxis toward an attractive substance, the direction of motion relative to the gradient is represented by specialized chemosensory neurons that respond either to increases (ON cells) or decreases in concentration (OFF cells) (Thiele et al., 2009) ; moreover, interventions that activate ON cells or OFF cells promote runs and pirouettes, respectively (Suzuki et al., 2008). Thus, in one simple model of random-walk chemotaxis, ON cells increase $h_{ℱ}$ and decrease $h_{ℛ}$, whereas OFF cells do the opposite. Simulations show that this model is sufficient to generate realistic chemotaxis in a point model of search behavior in C. elegans (Figure 8—figure supplement 2) when the worm is below the target concentration of attractant. Similar circuitry can explain biased random walks in response to other physical gradients (Lockery, 2011).

### The Stochastic Switch Model and deterministic behaviors

In addition to random search, the command neurons in C. elegans are required for a variety of escape responses (Hart et al., 1995) that are deterministic in that pR closely approaches unity for strong stimuli (Wittenburg and Baumeister, 1999; Tobin et al., 2002; Liu et al., 2012; Mohammadi et al., 2013). C. elegans escape responses can be produced by two pathways, one that requires the reverse command neurons (Chalfie et al., 1985) and one that does not (Piggott et al., 2011). Three distinct circuit motifs for the functional connectivity underlying escape responses requiring reverse command neurons are conceivable (Figure 9A). In the Push motif, nociceptive neurons excite reverse command neurons via hℛ thereby increasing the rate constants for transitions in which ℛ turns ON (aXR and aFY), and decreasing the rate constants for transitions in which ℛ turns OFF (aRX and aYF). In the limit where hℛ→ ∞, both aXR and aFY→ ∞, whereas aRX and aYF→ 0 (Figure 9B). The system now inhabits only states R and Y, and pR=aYR/(aYR+aRY). In the Pull motif, nociceptive neurons inhibit the forward command neurons via hℱ. In the limit where hℱ→ -∞, the system switches only between states R and X and pR=aXR/(aXR+aRX). In the third motif, in which Push and Pull are combined, R becomes an absorbing state (pR=1). Using the rate constants shown in column A of Table 1 to compute limiting values of pR in each motif, we found that the Pull and Push-Pull motifs are sufficient for deterministic escape, whereas the Push motif is not (Figure 9B). Thus, inhibition of forward command neurons is required for deterministic escape, predicting that nociceptive neurons functionally inhibit these neurons.

![Figure 9.](https://cdn.elifesciences.org/articles/12572/elife-12572-fig9-v2.jpg)

**Figure 9.:** (A) Three functional circuit motifs for deterministic escape behavior initiated by the nociceptive neuron ASH. (B) Predicted steady-state probability of reversal behavior in the resting state and the activated state of the three motifs shown in A. Plotted values are means across the five wild type cohorts shown in Figure 1F. Error bars are ± sem. Numbers in parenthesis are predicted mean first latency to a reversal response. (C) Left, synaptic current in AVB when ASH was photoactivated (blue line). Right, mean synaptic current during the first 100 ms of the stimulus plotted against holding potential in AVB. The line is fit to the data at negative holding potentials. (D) Mean zero-current holding potential and mean reversal potential of synaptic currents (± sem) in AVB (paired t-test: p= 0.013, n = 4).

To test this prediction we examined the ASH neurons, a pair of nociceptive sensory neurons required for the majority of escape responses in C. elegans. ASH neurons have anatomically defined monosynaptic and polysynaptic connections to both the behaviorally dominant command neurons AVB and AVA (Chalfie et al., 1985; White et al., 1986). We have previously shown that the functional connection from ASH to AVA is excitatory (Lindsay et al., 2011). To test whether the functional connection from ASH to AVB is inhibitory, we photoactivated ASH neurons while recording from AVB (Figure 9C,D). The reversal potential of this connection was more negative than the zero current potential, indicating inhibition as predicted by the model. Thus, ASH-mediated escape may be controlled by a Push-Pull motif, further demonstrating the feasibility of using behavioral data to predict population-level synaptic connectivity. The source of the AVB inhibition could be the inhibitory connection from AVA, polysynaptic pathways from ASH to AVB, or both.

Notably, the Pull and Push-Pull motifs are equally effective in driving $p_{R}$ to 1.0 (Figure 9B). Nevertheless, computation of the expected latency to the first reversal event when a forward moving animal suddenly encounters a strong nociceptive stimulus indicates a 2.3-fold reduction in latency for the Push-Pull motif (Figure 9B, parenthetical values). We conclude that the ASH mediated escape circuit in C. elegans may be specialized for short latency escape responses.

## Discussion

The Stochastic Switch Model is cast at a level of biological detail that is minimally sufficient to capture the stochastic dynamics of C. elegans locomotion in neuronal terms. Despite its simplicity, the model predicts the unexpected effects of neuronal ablations and genetic manipulations. It also predicts the sign and strengths of key synaptic connections, which were confirmed by combining optogenetics with electrophysiology. The model is immediately extensible to random search at a variety of spatial scales, biased random walks such as chemotaxis, and deterministic escape behaviors. The predictive success of the model indicates that random search in C. elegans can be understood in terms of a neuronal flip-flop circuit involving reciprocal inhibition between two populations of stochastic neurons. Two likely sources of stochastic state transitions are quantal synaptic transmission and ion channel gating. Both of these sources derive their randomness from thermal fluctuations at the molecular level, a phenomenon that is common to all nervous systems. The stochasticity underlying search behavior in C. elegans could be intrinsic to the command neurons, their presynaptic neurons (Gordus et al., 2015), or both.

The simplifying assumptions of the model introduce several limitations worth noting. (i) By representing the ten command neurons as only two functional units, the model ignores possible functional differences between individual neurons within each group. (ii) By design, the model predicts exponentially distributed dwell times, but Figure 2—figure supplement 3 shows that this relationship is only approximate. (iii) The model also has no provision to explain the strong correlation between locomotory phase and entry into state Y (Figure 4), although this could be added by modeling feedback from the pattern generator as a time-varying component of $h_{ℱ}$ and $h_{ℛ}$. (iv) The model does not take into account temporal correlations in velocity, but instead uses only the present velocity, along with the present state, to compute transition probabilities. For example, the fact that locomotion gradually slows before the worm enters the pause state (Figure 1G,H) suggests that transition probabilities might be more reliably calculated by including the recent velocity history, rather than just the present velocity. (v) Finally, the model does not attempt to explain the observation that the number of command neurons that are present and the degree of command neuron activation has an effect on velocity and undulation frequency (Figure 5A, Table 3, Table 5). Velocity modulation could be incorporated by relaxing the assumptions that command neurons within pools are co-active and have a single non-zero level of activation.

Although the model correctly predicts several unexpected and even paradoxical observations at the behavioral and electrophysiological levels, it would be premature to conclude that the biological system functions as assumed. This caution extends to all of the model's assumptions, including the mapping relationship between pause states X and Y and their behavioral correlates. We view the pause states as theoretical constructs having an epistemological status akin to theoretical constructs in many widely accepted models, such as the gating particles that were proposed in the Hodgkin-Huxley model of the squid action potential to explain the voltage sensitivity of ion channels.

An altogether different method for analyzing locomotory states in C. elegans also proposed the existence of two pause states (Stephens et al., 2008). In that work, each pause state was associated with a particular locomotory phase. In contrast, we found that only state Y occurred in association with a particular posture (a ventral bend in the middle of the body), whereas state X occurred with essentially no postural preference. The reason for this discrepancy may be that pauses are identified in different ways in the two studies. Here pauses are identified in terms of tangential velocity. In Stephens et al. (Stephens et al., 2008; 2011; 2010), however, pauses are identified in the phase space defined by the amplitudes of first two principle components of the worm's instantaneous shape. For the two approaches to yield the same result, minima in the magnitudes of tangential and phase velocity would have to be coincident at all times. We believe this outcome is unlikely because the third and fourth principle shape components, which account for approximately 30% of the shape variance (Stephens et al., 2008), meet the necessary and sufficient conditions for generating tangential thrust: a gradient of curvature along the worm’s centerline (Gray, 1946; Gray, 1953; Gray and Lissmann, 1964); this is one way thrust is believed to be generated during omega turns (Stephens et al., 2008). Thus, the worm can be moving with respect to the substrate even when phase velocity is zero. Overall, we speculate that pauses in phase velocity are a subset of pauses in tangential velocity. The extent to which this is true could be determined by performing spot tracking and shape analysis on the same individual worms.

It will be interesting to test several additional predictions of Stochastic Switch Model:

Like the Stochastic Switch Model, a previous model of the command neuron circuit by Rakowski et al. (Rakowski et al., 2013) predicts reciprocal inhibition between command neurons. Although the two models analyze locomotion behavior in terms of the same three behavioral states – forward, reverse, and pause – the models have essentially no points of mathematical contact. In the Rakowski model, neurons are deterministic electrical compartments and only the long-term average state probabilities of the network are computed. In the Stochastic Switch Model, by contrast, neurons are inherently stochastic and instantaneous state is computed. These disparities are significant because only the Stochastic Switch Model can predict temporal phenomena including such fundamental quantities as transition rates and mean dwell times. The fact that the both models predict reciprocal inhibition may reflect that fact that the behavioral signal of reciprocal inhibition is strong enough to transcend large differences between models.

Mammalian sleep, like C. elegans locomotion, is composed of numerous abrupt alternations between opposing behavioral states. Sleep is punctuated frequently by brief periods of wakefulness, and dwell time distributions in sleep and wake states indicate that switching between them is a stochastic process (Lo et al., 2004). Sleep and wakefulness are controlled by mutually inhibitory brain-stem nuclei, implying a reciprocal inhibition motif. In a significant parallel to the effects of command neuron ablations on dwell times in C. elegans locomotion (Figure 5B), lesions of sleep-related nuclei simultaneously reduce the dwell times in both sleep and wake states, as do lesions of wakefulness nuclei (Saper et al., 2010). Thus the relationship between synaptic uncoupling of the circuit and changes in dwell times may be a general principle of reciprocal inhibition in stochastic neuronal networks. Further study of invertebrate models of this circuit motif would be a productive means of identifying the genetic and physiological underpinnings of such circuits.

The debut of the essentially complete wiring diagram of the C. elegans nervous system raised the prospect of the first account of the entire behavioral repertoire of an organism at single-neuron resolution (White et al., 1986; Varshney et al., 2011). To date, the repertoire of behaviors commonly recognized in C. elegans can be divided into three main functional categories, subsuming 23 different elementary actions (Faumont et al., 2012). Because the command neurons considered here are required for almost half of this repertoire, the Stochastic Switch Model is a significant step toward a comprehensive understanding of the neuronal basis of behavior in this animal, bringing us closer to the goal of computing the behavior of an entire organism. Though abstract by design in its representation of individual neurons and synapses, the model accommodates not only random search at multiple spatial scales (Figure 8), but also biased random walks (Figure 8—figure supplement 1) and deterministic escape behaviors (Figure 9). We propose, therefore, that the Stochastic Switch Model could serve as a multipurpose module for computing C. elegans behavior. Combining this mathematically tractable module with others representing sensory inputs, modulatory states, and the presumptive pattern generators for forward and reverse locomotion, could lead to essentially complete models of the C. elegans nervous system that are at once predictive and intuitively comprehensible (Abbott, 2008).

## Materials and methods

### Strains

All strains were cultivated at 22.5°C on low-density NGM (nematode growth medium) agar plates seeded with the E. coli bacteria (OP50) as described by Brenner (Brenner, 1974). Transgenic lines were made using standard protocols (Mello and Fire, 1995).

### Physiological solutions

External saline for electrophysiology (mM): 5 KCl, 10 HEPES, 8 CaCl2, 143 NaCl, 30 glucose, pH 7.2 (NaOH); internal saline for electrophysiology (mM): 125K-gluconate, 1 CaCl2, 18 KCl, 4 NaCl, 1 MgCl2, 10 HEPES, 10 EGTA, pH 7.2 (KOH). Medium for behavioral assays (mM): NH4Cl 2, CaCl2 1, MgSO4 1, and KPO4 25, pH 6.5; M9 Buffer (grams): 3 KH2PO4, 6 Na2HPO4, 5 NaCl, 1 ml 1 M MgSO4, H2O to 1 liter.

### Behavior and tracking system

Prior to each assay, an individual adult hermaphrodite was picked to a bacteria-free agar transfer plate by means of a platinum-wire pick. The worm was then washed in M9 to remove excess bacteria, then transferred in a pipette filled with assay medium to a 10 cm petri plate containing 1.7% agarose in assay medium. A black dot approximately 40 microns in diameter was applied to the center of the body as shown in Figure 1A (see Spotting procedure). The worm was allowed to recover from transfer and handling for 2 min., then recorded for 10 min. The assay plate rested on a motorized microscope stage (Applied Scientific Instrumentation MS-2000, Eugene, OR USA) fitted with position encoders (Gurely Precision Instruments LE-1800, Troy, NY USA) having a resolution of 0.5 μm. Behavior was recorded using an analog video camera (CCD Sony XC-ST70, 29.97 frames per second) fitted with a 12× zoom lens (Navitar 50486D, Rochester, NY USA). For tracking purposes, video was analyzed in real time by custom software to calculate the eccentricity of the ink spot relative to the center of the field of view, and to compute the stage movements required to re-center the spot. Motion blur was minimized by making stage speed during corrective movements an increasing exponential function of target eccentricity such that small corrections were made more slowly than large corrections. Position encoders were read in synchrony with the video stream and this information was stored for off-line analysis. The overall trajectory of the worm was computed by combining the location of the spot in the field of view with stage position in each video frame. The direction of movement (forward or reverse) at the start of each recording was keyed by the observer and subsequent assignments were made automatically by computer. Each recording was spot-checked for correct assignments at four or more points during the recording. In experiments involving neuronal ablations or genetic mutations, recordings of sham operated controls or wild type worms, respectively, were interleaved with worms in each treatment group.

### Spotting procedure

The animal was immobilized by a stream of humidified CO2 emitted by a 1.5 mm diameter glass pipette positioned near the worm. The spotting ink was comprised of petroleum jelly (1 ml), mineral oil (1 ml), and black iron oxide (3 g). Ink was applied by means of 1.5 mm diameter glass rod that had been pulled to a fine point, fire polished to produce a bulbous tip, and dipped in the ink. The rod was positioned by means of a micromanipulator. To control for the effects of the spotting procedure, we compared the speed of locomotion of worms that had been immobilized, or immobilized and spotted, to untreated worms. There were no significant differences between these three groups.

### Electrophysiology

Worms were glued to an agarose coated coverslip using cyanoacrylate adhesive as previously described (Lindsay et al., 2011). The coverslip formed the bottom of the recording chamber, which was filled with external saline. The cell body of the neuron to be recorded was exposed by making a small slit in the cuticle using a finely drawn glass rod. Recording pipettes had resistances of 10–20 MΩ when filled with internal saline. Voltage- and current-clamp recordings were made with a modified Axopatch 200A amplifier (Lockery and Goodman, 1998). In reversal potential measurements, recordings of photostimulation-evoked synaptic currents were filtered at 2 kHz and sampled at 10 kHz. Postsynaptic neurons (AVA, AVB) were identified using a combination of fluorescent markers and distinctive voltage clamp currents as described (Lindsay et al., 2011). Presynaptic neurons (AVA, AVB, and ASH) were activated by expression of ChannelRhodopsin-2 expressed under the control of neuron-specific promoters as described (see “Strains”). Worms were photostimulated in electrophysiological experiments using the blue channel (470 nm) of a dual-wavelength LED module (Rapp OptoElectronic, Wedel, Germany) that was focused by a 63×, 1.4 NA oil immersion objective lens (Zeiss, part number 440762–9904). Irradiance (12.5 mW/mm2) was determined by measuring the power emitted from the objective using an optical power meter placed above the front lens of the objective and dividing by the area of the field of illumination at the focal plane of the preparation.

### Ablations

Neurons were ablated using a laser as described previously (Bargmann and Avery, 1995). L1 larvae were mounted on 2.5% agarose pads containing 5–7 mM of the immobilizing agent NaN3. AVA and AVB neurons were ablated in N2 animals and identified by position. AVD, AVE and PVC were ablated in animals expressing nmr-1::GFP and identified by a combination of position and GFP expression. To limit potential behavioral differences in the two strains, we outcrossed (4×) the nmr-1::GFP strain to the N2 strain used for AVA and AVB ablations. All animals were remounted 1–3 hr after surgery to confirm the ablation; those with collateral damage were discarded. Sham-operated animals were treated in the same manner except that the laser was not fired.

### Statistical tests

Statistical significance for the results shown in Figures 4B and 6C, and in Tables 4 and 6 were obtained using the likelihood ratio test (see Table 1 and 4 legends). Otherwise, two-tailed t-tests or 2-tailed Mann-Whitney U tests were used.

### Descriptive statistics

The worm’s position in video frame $k$ is represented as the row vector:

$$
R(t_{k})=xt_{k}, yt_{k}              k=1, 2, …, N
$$

where $x(t_{k})$ and $y(t_{k})$ are the coordinates of centroid of the tracking spot in the frame of reference of the agar plate, $t_{k}=k\Deltat$, $\Deltat=$33 ms, and $N≅$18000 is the number of video frames analyzed in a continuous recording of one worm. We made the following definitions:

#### Row vectors

Velocity:

$$
V(t_{k})= \frac{R(t_{k+1})−R(t_{k}) }{\Deltat}
$$

Heading:

$$
H(t_{k})=\frac{V(t_{k})}{s(t_{k})}
$$

#### Scalar quantities

Speed:

$$
s(t_{k})=Vt_{k}=\sqrt{Vt_{k}·V^{t}t_{k}}            V^{t}≡transpose of V
$$

Mean speed:

$$
s¯=\frac{1}{N-1}\sumk=1N-1st_{k}
$$

Instantaneous turn rate:

$$
\frac{\Delta\phi}{\Deltat}(t_{k})=\frac{cos^{−1}Ht_{k-1}·H^{t}t_{k}}{\Deltat}            (0\leq\Delta\phi\leq\pi)
$$

Mean heading change:

$$
\Delta\phi_____t_{j}=\frac{1}{N−j−1}\sumk=1N−j−1cos^{−1}Ht_{k}+t_{j}·H^{t}t_{k}        (0\leq\Delta\phi\leq\pi)
$$

Speed autocovariance:

$$
A_{s}(t_{j})=\frac{1}{N−j−1}\sumK=1N−j−1(s(t_{k}+t_{j})−s¯)·(s(t_{k}) -s¯)
$$

Velocity autocorrelation:

$$
A_{V}(t_{j})=\frac{1}{N−j−1}\sumK=1N−j−1V(t_{k}+t_{j})·V^{t}(t_{k})
$$

Heading autocorrelation:

$$
A_{H}(t_{j})=\frac{1}{N−j−1}\sumK=1N−j−1H(t_{k}+t_{j})·H^{t}(t_{k})
$$

Mean squared displacement:

$$
r^{2}___(t_{j})=\frac{1}{N−j−1}\sumk=1N−j−1 ||R(t_{k}+t_{j})−R(t_{k})||^{2}
$$

### Maximum likelihood estimation of state transition rates in a hidden Markov model

To analyze locomotory states we converted the velocity vector, $V(t)$, into a signed scalar quantity $v(t)$ that represents the component of velocity in the direction of the worm’s track, with positive values indicating forward movement. We first smoothed $x(t)$ and $y(t)$ using an 11 frame window, assigned a direction to the smoothed track with respect to the head/tail orientation of the worm, and projected $V(t)$ onto the smoothed track to obtain $v(t)$. For each cohort of worms we collected all $v(t)$ values into a single velocity distribution $g(v)$. The central peak of $g(v)$ was fit by a Cauchy distribution with median 0 and half-width $b$ = 18 µm/s (Figure 2—figure supplement 2), which we used to approximate the pause velocity distribution for states X and Y for all worms:

$$
g_{X}(v)=g_{Y}(v)=g_{P}(v)=\frac{b}{\pi(b^{2}+v^{2})} 
$$

We used a Cauchy distribution because it has long tails that describe the pause velocity distribution better than a Gaussian distribution (i.e., the worm does not stop instantaneously when it switches from forward or reverse locomotion into one of the pause states). We estimated the forward and reverse velocity distributions $g_{F}(v)$ and $g_{R}(v)$ by scaling $g_{P}(v)$ to fit the peak at $v=0$, subtracting it from the overall distribution and splitting the remaining distribution into $g_{F}(v)$ for $v>0$ and $g_{R}(v)$ for $v<0$. Velocity distributions were scaled to be probability densities (area =1) and collected into a row vector:

$$
G(v)= [g_{F}(v), g_{R}(v),  g_{X}(v),  g_{Y}(v)]
$$

where $g_{i}(v)$ is the estimated probability density that worms move at velocity $v$ when in state $i$.

The goal of the maximum likelihood fitting procedure is to find the set of state transition rates ${a_{XF},a_{FX},a_{XR},a_{RX},a_{FY},a_{YF},a_{RY},a_{YR}}$ that maximize the probability of the observed velocity time series $v(t)$ given the velocity distribution $G(v)$. All transition rates were constrained to be $\geq0$, and usually were additionally constrained to correspond to valid synaptic weights as described below$.$ The likelihood is most conveniently calculated using matrix notation as follows; see Colquhoun and Hawkes, 1995 for a more complete explanation of these computations. Let:

$$
Q=−(a_{FX}+a_{FY})0a_{XF}a_{YF}0    −(a_{RX}+a_{RY})a_{XR}a_{YR}a_{FX}a_{RX}    −(a_{XF}+a_{XR})0a_{FY}a_{RY}0    −(a_{YF}+a_{YR})
$$

Element $q_{ij}$ ($i\neqj)$ of matrix $Q$ is the transition rate from state $i$ to state $j$ (i.e., the instantaneous probability per unit time that the system in state $i$ will make a transition to state $j$, and element $q_{ii}$ is the negative of the total transition rate out of state $i$, which is related to the mean dwell time in state $i$ by:

$$
d_{i}=−1/q_{ii}
$$

Matrix $Q$ is composed of instantaneous transition rates, which can be converted into the matrix of transition probabilities during a brief time interval of duration $\epsilon$ by multiplying $Q$ by $\epsilon$ and adding 1 to each diagonal element (i.e., by calculating $\epsilon·Q+I$, where $I$ is the 4×4 identity matrix). If $\epsilon$ is sufficiently small that multiple state transitions can be ignored, then element $ij$ of matrix $\epsilon·Q+I$ is the probability that the system is in state $j$ at the end of a time interval of duration $\epsilon$ given that it was in state $i$ at the beginning of the interval. For longer time intervals during which multiple state transitions may occur, transition probabilities can be calculated by repeatedly multiplying matrix $\epsilon·Q+I$ by itself. Thus, if

$$
M=(\epsilon·Q+I)^{K}
$$

then $M$ is the matrix of transition probabilities during a time interval of duration $K\epsilon$. If $K$ and $\epsilon$ are chosen such that $\Deltat=K\epsilon$, then element $ij$ of matrix $M$ is the transition probability from state $i$ to state $j$ during one video frame of duration $\Deltat$. We chose $K=2^{30}$ and let $\epsilon=\Deltat/K=30.7$ picoseconds, a time interval during which multiple state transitions can safely be ignored. Since $K$ was chosen to be a power of 2, $M$ could be rapidly and accurately calculated by 30 serial multiplications using 64-bit floating point arithmetic.

Let $P(t)$ be the row vector of history-dependent state probabilities:

$$
P(t)= [ p_{F}(t), p_{R}(t), p_{X}(t),  p_{Y}(t)]
$$

where $p_{i}(t)$ is the probability of being in state i at time $t$ given $v(u)$ for all $u$ up to and including the present time ($u\leqt$). The matrix product $P(t)·M$ is the state probability vector at time $t+\Deltat$ prior to accounting for the observed velocity at time $t+\Deltat$. To account for $v(t+\Deltat)$ we used the information contained in $G(v(t+\Deltat))$ and applied Bayes theorem:

$$
P(t+\Deltat)=l·P(t)·M·diagG(v(t+\Deltat))
$$

where $diagG(v(t+\Deltat))$ is the 4×4 matrix with the elements of $G(v(t+\Deltat))$ along the diagonal, and $l$ is the scalar multiplicative factor required for the sum of the four elements of $P(t+\Deltat)$ to equal 1 (i.e., $P(t+\Deltat)$ is a vector of probabilities). Initially ($t=0$) we set $P(0)$ equal to the steady-state probability vector $P_{∞}$, which is given by:

$$
P_{∞}·Q=0      ⇒         P_{∞}=U_{4}·(Q_{a}·Q_{a}^{t})^{−1}
$$

where $U_{4}$ is the $1\times4$ row vector of ones and $Q_{a}$ is the $4\times5$ matrix constructed by appending a column of ones to $Q$. To break the symmetry between the behaviorally indistinguishable states X and Y, we identified X as the state with higher steady-state probability.

We then calculated the log-likelihood, summed over all worms in the cohort:

$$
lnL=\sumt,w ln(P_{w}(t)·G^{t}(v_{w}(t)))
$$

where $v_{w}(t)$ is the velocity and $P_{w}(t)$ is the history-dependent state probability vector of worm $w$ at time $t$.

We used a random optimization algorithm to find the set of transition rates that maximized $lnL$. Initial guesses for 6 of the 8 rates were chosen independently from log uniform distribution between 0.01 Hz and 10 Hz. The remaining 2 rates were calculated to satisfy the constraints needed to generate valid synaptic weights (see below). At each iteration, each of the 6 independently chosen rates was altered by adding a random number chosen from a Cauchy distribution with median 0 and width $b_{random}$ (initially $b_{random}=$ 0.01 Hz), and the remaining 2 rates were recalculated. To avoid getting trapped in local likelihood maxima, the new rates were rejected and another set was calculated if any of the new rates were <0.01 Hz. If the new rates generated an increased likelihood, the new rates were accepted and $b_{random}$ was increased by 3%. Otherwise the old rates were retained and $b_{random}$ was decreased by 0.5%. The procedure was iterated until $b_{random}<$ 0.001 Hz. The random optimization procedure was replicated 10 times for each cohort using different randomly chosen initial guesses. In 71% of the replicates the procedure converged on a set of transition rates in which none of the transition rates differed from the best set by more than 5%. The best set of transition rates was then refined by applying the optimization procedure using a success criterion of $b_{random}<$ 10-5 and constraining transition rates to be ≥ 10–4 Hz.

The likelihood calculations described above use only past and present velocity observations to calculate $P(t)$, but once the optimal transition rates were determined, the Forward-Backward algorithm (Rabiner, 1986) can be used to yield a better estimate of the state probabilities based on past, present and future velocity observations, and the Viterbi Algorithm can be used to find the sequence of states with the highest probability of producing the observed velocities (Figure 2E).

### Stochastic model neurons

We expressed the effect of synaptic inputs to command units $ℱ$ and $ℛ$ by equations of the form:

$$
a_{ON}=A·e^{S}
$$

$$
a_{OFF}=A·e^{-S}
$$

where $a_{OFF}$ is the transition rate from ON to OFF, $a_{ON}$ is the transition rate from OFF to ON, and $S$ is the total synaptic input to the unit. We do not attach any mechanistic significance to these equations, but note that they are analogous to the Arrhenius Equation (Stiller, 1989) an approximation commonly used to describe the rates of chemical reactions in terms of an activation energy, $E$:

$$
a=A·e^{- \frac{E}{k_{B}T}}
$$

where a is the reaction rate constant, $A$ is an empirically determined constant, $k_{B}$ is the Boltzmann constant, and $T$ is the absolute temperature. Under this interpretation, $S$ is analogous to activation energy expressed in units of $k_{B}T$. Thus, $ℱ$ and $ℛ$ are assumed to be symmetrical bi-stable units that change state at rate $A$ when $S=0$. Deviations from this baseline condition are modelled as external synaptic inputs $h_{ℱ}$ and $h_{ℛ}$.

We represented the total synaptic input onto units $ℱ$ and $ℛ$, respectively, by:

$$
S_{ℱ}=h_{ℱ}+b_{ℱ}tw_{ℱℱ}+b_{ℛ}tw_{ℛℱ}
$$

$$
S_{ℛ}=h_{ℛ}+b_{ℛ}tw_{ℛℛ}+b_{ℱ}tw_{ℱℛ}
$$

where $b_{ℱ}t$ and $b_{ℛ}t$ are the states of $ℱ$ and $ℛ$ (1 = ON, 0 = OFF), $w_{ℛℱ}$ and $w_{FR}$ are the synaptic weights from $ℛ$ onto $ℱ$ and from $ℱ$ onto $ℛ$, respectively, and $w_{ℱℱ}$ and $w_{RR}$ represent synaptic interactions among command neurons of the same class, plus any intrinsic membrane properties that may promote bistability. Applying these definitions to the rate constants in Figure 2C gives:

$$
a_{XF}=A exp(h_{ℱ})                                          a_{XR}=A exp(h_{ℛ})                              
$$

$$
a_{FX}=A exp(−h_{ℱ}−w_{ℱℱ})                         a_{RX}=A exp(−h_{ℛ}−w_{ℛℛ})             
$$

$$
a_{RY}=A exp(h_{ℱ}+w_{ℛℱ})                             a_{FY}=A exp(h_{ℛ}+w_{ℱℛ})                 
$$

$$
a_{YR}=A exp(−h_{ℱ}−w_{ℱℱ}−w_{ℛℱ})             a_{YF}=A exp(−h_{ℛ}−w_{ℛℛ}−w_{ℱℛ})
$$

In these experiments the sensory environment was kept constant (e.g., no chemical or temperature gradients). Therefore $h_{ℱ}$ and $h_{ℛ}$ were assumed to be constant. For simulations of chemotaxis $h_{ℱ}$ and $h_{ℛ}$ varied with position in the chemical gradient.

Equations 31–34 express the 8 transition rates in terms of 6 parameters and yield the following two constraints on the transition rates:

$$
a_{FX} a_{XF} = a_{RY}  a_{YR}                               a_{FY} a_{YF}=a_{RX} a_{XR}
$$

The inverse relations between transition rates and synaptic parameters are:

$$
h_{ℱ}=ln(a_{XF})−lnA                              h_{ℛ} =ln(a_{XR})−lnA              
$$

$$
w_{ℛℱ}=ln(a_{RY}/a_{XF})                                 w_{ℱℛ}=ln(a_{FY}/a_{XR})                  
$$

$$
w_{ℱℱ}=−ln(a_{XF} a_{FX})+2·lnA               w_{ℛℛ}=−ln(a_{XR} a_{RX})+2·lnA
$$

### Derivation of the mean distance traveled during a forward run

The time series of the worm’s locomotory states can be divided into forward runs, during which the worm is in either the F or P state, and reverse runs, during which the worm is in either the R or P state. Forward runs always begin with an RPF transition and end with the next FPR transition, which marks the beginning of a reverse run. Thus forward runs and reverse runs occur in strict alternation, such that the number of forward runs equals the number of reverse runs.

Let $m_{F}$ denote the mean distance traveled during a single forward run, assuming that forward runs are straight. The value of $m_{F}$ is most easily calculated by dividing time into non-overlapping epochs, each of which begins with an RPF transition and ends immediately before the next RPF transition. Each epoch thus contains exactly one forward run, which includes all visits to state F during the epoch. Therefore, $m_{F}$ is also equal to the mean distance travelled while in the forward state during a single epoch:

$$
m_{F}=\frac{v_{F}¯p_{F}}{f_{RPF}}
$$

where $v_{F}¯$ is the mean velocity in the forward state and $f_{RPF}$ is the frequency of RPF transitions. Since FPR and RPF transitions occur in strict alternation they must occur in equal numbers: $f_{RPF}=f_{FPR}$. Thus, eq. 39 can also be written with $f_{FPR}$ in the denominator, which is more useful for the calculation that follows, although the form shown above is more directly interpreted in terms of the frequency of random reorientations, which occur at the RPF transitions. It is straightforward to calculate $f_{FPR}$ given $p_{F}$, $a_{FX}$, $a_{FY}$, and the probabilities that the transitions out of states X and Y will be into state R:

$$
prob(X→R)=a_{XR}/(a_{XF}+a_{XR})
$$

$$
prob(Y→R)=a_{YR}/(a_{YF}+a_{YR})
$$

$$
f_{FPR}=p_{F}(a_{FX}\frac{a_{XR}}{a_{XF}+a_{XR}}+a_{FY}\frac{a_{YR}}{a_{YF}+a_{YR}})
$$

Combining eqns. 39 and 42 yields:

$$
m_{F}=v_{F}¯ (\frac{(a_{XF}+a_{XR})(a_{YF}+a_{YR})}{a_{FX}a_{XR}(a_{YF}+a_{YR})+a_{FY}a_{YR}(a_{XF}+a_{XR})})
$$

An approximation to $m_{F}$ in terms of synaptic weights is obtained by noting that transitions from F to Y were extremely rare ($a_{FY}=$0.007 s-1; Table 1). Setting $a_{FY}≅0$ yields:

$$
m_{F}≅v_{F}___(\frac{a_{XF}+a_{XR}}{a_{FX}a_{XR}})=\frac{v_{F}___}{A}(\frac{exp(h_{ℱ})+exp(h_{ℛ})}{exp(h_{ℛ}−h_{ℱ}−w_{ℱℱ})})
$$

### Simulations of worm behavior

In Figure 8—figure supplement 1 and 2, the worm was represented as a point that moved forward or backward at speeds of 0.2 and 0.3 mm/sec, respectively, and was stationary during the pause state. Rate constants were calculated according to equations 31–34 based on the weights that pertain under random search or chemotaxis, using either $A=A_{min}$ or $A=A_{max}$. Weights were used to compute the state transition matrix $M$. At each time step (∆t = 33 ms), the next state was selected randomly according to the state probabilities given by $M$. When an RPF transition occurred, a new direction of movement (heading) was selected from a uniform distribution. The random component of the heading was modeled as Gaussian noise having a standard deviation of 0.001 degrees. In the case of chemotaxis simulations, the values of $h_{ℱ}$and $h_{ℛ}$ were updated at every time step according to the direction in which the worm was heading, leading to an updated set of weights and a new $M$ matrix.

### Definition of modes of random search in C. elegans

To date, these behaviors have been defined mainly in operational terms. Following the terminology of Jander 1975: (i) cropping is the locomotory behavior exhibited by well-fed worms on plates with densely populated patches of bacteria; (ii) local search (also “area restricted search” (Hills et al., 2004) or “pivoting” (Wakabayashi et al., 2004) is exhibited by well-fed worms within about 10 min after being transferred to a foodless plate; and (iii) ranging (“dispersal” (Gray et al., 2005) or “traveling” (Wakabayashi et al., 2004) is exhibited by well-fed worms tens of minutes after being transferred to a foodless plate. Each mode can be associated with approximate ranges of three parameters: mean forward run length ($m_{F}$), mean frequency of reversals ($f_{FPR}$), and mean reverse run length ($m_{R}$). Local search serves as a useful reference point. During cropping, $m_{F}$ is greatly reduced, $f_{FPR}$ is greatly increased, and $m_{R}$ is also reduced, being limited to “short reversals” (the distance traveled in one or two head sweeps, or about 0.5 mm (Gray et al., 2005); during local search, reverse runs are almost always “long” (the distance traveled in at least three head sweeps). During ranging, $m_{F}$ is greatly increased, $f_{RPF}$ is reduced, and reversals are long. Cutoff values for search modes, inferred from behavioral data (Wakabayashi et al., 2004; Gray et al., 2005; Fujiwara et al., 2002; Hills et al., 2004) were: Dwelling – short forward run length ($m_{F}$ < 0.5 mm), high reversal frequency ($f_{FPR}$ > 6.0/min), short reversals ($m_{R}$ < 0.5 mm); Local search – moderate forward run length (0.5 mm ≤ $m_{F}$ < 5.0 mm), moderate reversal frequency (2.0/min ≤ $f_{FPR}$ < 6.0/min), non-short reversals ($m_{R}$ ≥ 0.5 mm); Ranging – long forward run length ($m_{F}$ ≥ 5.0 mm), low reversal frequency ($f_{FPR}$< 2/min), non-short reversals ($m_{R}$ ≥ 0.5 mm).

### Data archive

All data and the analysis program are publicly available at doi:10.5061/dryad.35qv6.
