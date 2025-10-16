# Peer review - Round 1

Editors:
- Brice Bathellier, https://ror.org/02feahw73 CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89151.sa0](https://doi.org/10.7554/eLife.89151.sa0)

Large populations of neurons are capable of entering pathological synchronous oscillations under a variety of conditions and work over many decades has found ways to disrupt such oscillations using stimulation in both open loop and closed loop configurations. This study adds useful results and methodology to this line of research, by providing solid evidence that delayed feedback control via electrical stimulation can, under certain conditions, terminate network level oscillations in cultured hippocampal neurons. The study provides analyses and simulation results that shed light on why some networks respond to such feedback control while others do not.


---

# Peer review - Round 1

Editors:
- Brice Bathellier, https://ror.org/02feahw73 CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89151.sa1](https://doi.org/10.7554/eLife.89151.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Disrupting abnormal neuronal oscillations with adaptive delayed feedback control" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Panayiota Poirazi as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Reviewer #1 (Recommendations for the authors):

Suggestions for improved or additional experiments, data or analyses, especially those directed at increasing the impact of the work and making it suitable for eLife:

Page 4:

In the text, the Figure 1C middle part is never mentioned, indeed the "mixed" is also not explained and its meaning is not fully clear.

"In all algorithms, stimulation was provided as monophasic negative voltage pulses at controlled timings."

Why was this type of stimulation chosen? Was it based on current literature? What is the advantage of this type of stimulation vs a biphasic pulse?

Section 2.1:

It was not clear to me the advantage of representing the neuronal dynamics using the wavelet transform of the firing rate, since in the rest of the article this is represented by the DFT. Could you elucidate this choice?

"Consistent inter-burst intervals will appear as a low frequency horizontal line" – Why? If the ISI is constant but the firing rate is high, shouldn't it appear as a higher frequency horizontal line?

Figure 2:

I missed seeing the same analysis performed in the random stimulation condition – it could be included as a supporting figure just for completeness.

Section 2.2:

The definition of firing rate should appear before, since it is one of the main variables used in the previous section.

Defining the oscillation frequency and intensity based on the main peak does not seem to make sense for the aDFC condition. Your premise is that this treatment disrupts periodicity (which it appears to do) then, in theory, there should not be a defined "peak" in the frequency domain. This identified peak will rest within the noise levels, rendering it "random". Maybe a threshold could be set, i.e., if the signal-to-noise ratio of a peak is X, then it is considered, otherwise the frequency and intensity of the oscillation are respectively none and zero. Furthermore, the "randomness" of this oscillation frequency can be seen in Figure 3, where the trials with aDFC show a very large range of main frequencies.

Figure 3:

How is the z-score calculated?

Section 2.3:

Figure 4A show oscillation intensity yet, in the main text, you claim that "standard DFC led to more consistent oscillations". How does intensity relate to consistency? DFC shows a higher inter-trial variance than the other conditions (less consistent?)

Figure 4:

All variables are studied in four different conditions, yet the authors use t-tests to evaluate statistical significance. This is the wrong statistical test to use – an ANOVA should be used. In this situation, multiple t-tests will lead to an increase in false positives.

Section 2.4:

Did you quantify the excitatory/inhibitory balance in your MEA cultures? Could be interesting to compare to the simulation results.

Section 2.5:

The authors state that multiple trials were conducted in the same network but do not mention how long the network was allowed to recover in between trials, which is necessary information.

Furthermore, the authors state that only one network showed this effect (spontaneous AS time prior to stimulation). If only one network showed this among 14, how biologically relevant is this? How can you be sure that this is not a consequence of a confounding variable (not properly developed network, etc). How old was this network? Was it also used in other DIVs?

Figure 7:

The effect of the Poisson stimulation appears to be more similar to aDFC than random. A more in depth discussion would be helpful to better understand how a "random" stimulation could cause such a "block-type" effect.

The comparison between OFF-ON-OFF states refers to a comparison of the same object in different timepoints. Thus, t-tests are not the correct statistical test here, but rather a repeated measures ANOVA (or non-parametric equivalent) must be used.

Methods:

The authors state that experiments were performed between 13 and 55 DIV. When considering cultured neuron networks, this range makes a gigantic difference in their behavior, since the culture will not be fully mature at DIV 13, and the neuronal health at DIV 55 will already have declined. Only cultures at equivalent maturity levels should be compared.

Authors define "network as a neuronal culture in a given day in vitro". This needs to be clarified for statistical analysis. With this definition, does it mean that if two experiments are performed in the same neuronal culture but in two different days, they are considered two independent networks? While the network behavior might change throughout days in vitro (and network maturity), it is not possible to state that the behavior of the network is independent from its previous state. Extra care should be had when performing statistical analysis on those data – they should be handled as the same "object" at different timepoints, NOT independent networks.

The method used to determine the main frequency and intensity of the oscillation ASSUMES that there is a peak frequency, which may not be true and lead to erroneous results and conclusions.

Reviewer #2 (Recommendations for the authors):

This was a clear, well-written study. I only have a few suggestions/comments to the authors:

0) Can you discuss whether you expect brain networks to operate in uncontrollable vs. controllable regimes? Is there evidence that brain networks should be controllable?

1) Can you establish a correspondence between the controllable subspace in the in silico model in Figure 5 and the controllable network properties in Figure 3? For example, can you make Figure 5B left (change in synchrony as a function of synaptic weight vs. excitatory neurons) into a synchrony as a function of firing rate vs. synchrony plot? Then superimpose data from Figure 3E so that one can see whether the in silico network properties are similarly predictive of controllable vs. uncontrollable networks as the in vitro network properties. If there isn't a clear correspondence between the in silico and in vitro networks, please discuss.

2) Could you either provide experimental data or a discussion of previous studies that have tested conventional high frequency stimulation (~100-120 Hz) and studied its effects on neural synchronization? How might you expect your aDFC results to compare to conventional high frequency stimulation? There is some mention in the discussion of a study that uses 10-50 Hz and is able to prevent synchronous states from forming at the cost of a high firing rate. Why is the high firing rate a problem? Might this be the source of undesirable side effects of stimulation? Please discuss this in more detail in the discussion as it directly sheds light on how useful your algorithm may be compared to conventional stimulation.

3) Please discuss in the discussion the limits of the in vitro model, particularly in reference to the low frequency synchrony that the populations exhibit (~1 hz) compared to the pathological oscillatory activity thought to be relevant to PD (15-30 hz) or ET (5-7 Hz). Do you expect your algorithm to have difficulties suppressing these higher frequency oscillations ? Are there in vitro models that exhibit higher frequency oscillations that could be used to test this algorithm?

4) Can the authors comment on how many units must be monitored from in order to make an accurate estimate of the underlying neural population's oscillatory frequency? Can LFP features be used instead of multiple single neuron recordings? This has a direct bearing on how readily translatable this technology is to current neurostimulation devices.

5) During aDFC how often were the frequency (w) and period time (T) updated?

6) Where was the ground for the stimulation electrode? Does your stimulation better mimic bipolar or monopolar stimulation in current therapeutic DBS therapies? What was the impedance of the stimulation electrode? Some neuromodulation fields use current (not volts) to report their stimulation amplitude and it would be helpful for those building on this study to have both quantities reported. In addition, please report the electrode surface area so that current density calculations can be made.

7) Why was stimulation frequency the metric that was updated by DFC and aDFC as opposed to stimulation amplitude?
