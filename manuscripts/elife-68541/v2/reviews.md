# Peer review - Round 1

Editors:
- Joseph V Raimondo, https://ror.org/03p74gp79 University of Cape Town South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68541.sa0](https://doi.org/10.7554/eLife.68541.sa0)

In this manuscript the authors build a small-scale biophysically realistic network model to study seizure dynamics which incorporates Hodgkin Huxley mechanisms and ion dynamics. The model enhances our understanding of the mechanisms underlying the evolution and termination of focal seizures. In particular it demonstrates that intense activation of inhibitory interneurons, by driving changes in transmembrane ion dynamics are a possible mechanism for driving the initiation and prolongation of seizures.


---

# Peer review - Round 1

Editors:
- Joseph V Raimondo, https://ror.org/03p74gp79 University of Cape Town South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68541.sa1](https://doi.org/10.7554/eLife.68541.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Focal seizures are organized by feedback between neural activity and ion concentration changes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Joseph V Raimondo (Reviewer #1); Maxim Bazhenov (Reviewer #2).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that your work will not be considered further for publication by eLife.

Although there was certainly enthusiasm about the model, which was found to be generally thorough and broadly satisfying in its behaviour and predictions, there was ultimately collective concern from all 3 reviewers about whether there was the requisite level of novelty and advance over prior work to justify publication in eLife.

Please find the reviews below.

Reviewer #1 (Recommendations for the authors):

The model uses the NEURON framework and is well put together. On the whole its behaviour is both satisfying and reassuring. The model recapitulates the electrographic behaviour of animal model and human EEG recordings in particular the low-voltage fast activity preceding the tonic phase of a seizure, which transitions into bursting. The bursts then slow in frequency before postictal suppression of activity is observed. These dynamics emerge out of the model due to its inclusion of ion dynamics of K+, Na+ and Cl- and multiple cellular mechanisms including accounting for excitatory and inhibitory cell populations, dendritic and somatic compartments, diffusion, glial buffering, ion channels and ion transporters.

Whilst the work is very much worthy of publication, I am not convinced that it generates sufficiently novel findings and advances over previous work in the field (e.g. Krishnan 2011 and Krishnan 2015 and others) to be of sufficient interest to warrant publication in eLife. In my opinion the importance of K+, Cl- and Na+ dynamics for seizure evolution have been demonstrated before. (e.g. increases in K+ driving SLE initiation, transition between tonic and bursting activity and seizure cessation occurring due to enhanced Na+/K+ ATPase activity).

(1) I am concerned as to the applicability of the experimental data to this model. SLEs in the whole guinea pig brain were elicited using bicuculline, which blocks GABAaR transmission yet current from the IN to PYs via activated GABAaRs is presumably an important component of the computational model?

(2) Understandably the model cannot recapitulate all biological detail but there are some aspects about the model which seem odd and would need justification:

a. e.g. Intracellular HCO3- is higher than intracellular bicarbonate (15 mM) being higher than extracellular bicarbonate (11 mM). This suggests that intracellular pH is more alkaline than extracellular pH which is not the case. In addition, this would make the bicarb reversal +8 mV which is high and unrealistic.

b. In the neurons the Na+ leak conductance is 40% of the K+ leak conductance, this seems very high and not a typical ratio of permeabilities for neurons.

c. It wasn't clear whether the leak conductances for the various ions were actually contributing to the ion dynamics, e.g. was Cl- flux through the baseline Cl- leak conductance in neurons contributing to changes in [Cl-]i?

d. Ek = Ecl at rest, this is also not physiological, I understand why this was done so that KCC2 was at equilibrium at baseline, but this is not ideal. Rather there should be a tonic Cl- leak influx ensuring that "at baseline" Ecl>Ek as observed experimentally.

(3) Modelling of Cl- changes especially Cl- flux through GABAaRs. I am also not entirely sure that Cl- flux through GABAaRs was modelled correctly to capture the potential for biphasic/ depolarizing responses via intensely activated GABAaRs (the authors should note amongst others Ruusuvuori 2004). The calculation of Egaba included HCO3- (line 833) but how was Icl (Cl- flux) via activated GABAaRs calculated? Ie in the model if Vm is at the GABAaR reversal potential (Egaba) would Cl- ion flux into the cell via GABAaRs (Icl) be zero? Ie in the model if Icl calculated as 4/5 of Igaba and Igaba = Ggaba(Vm – Egaba), then when Vm = Egaba, Igaba and consequently Icl is 0. This shouldn't be the case. Rather Igaba = Icl + Ihco3 where Icl = gcl(Vm – Ecl) and Ihco3 = ghco3(Vm – Ehco3) and ggaba = 4/5xgcl +1/5xghco3. Seeing as Cl- accumulation is a fundamental part of the model this should have been made more clear. E.g. in Figure 5, could Icl via GABAaRs also be plotted? I worry as the Cl- influx in the model seemed to be coming predominantly via KCC2 (due to the raised extracellular K+) whereas experimentally this is likely also coming predominantly through GABAaRs. This is reflected in the time course of [Cl-]i changes in the model which are slower than [K+]o and continue increasing until the end of the SLE which is not typically what is observed experimentally (see intracellular Cl- recordings e.g. Raimondo 2013).

(4) Perhaps the authors could make it more clear that the exact same experimental data was also presented in Gentilleti 2017.

Reviewer #2 (Recommendations for the authors):

Gentiletti et al. investigated potential role of non-synaptic mechanisms driving seizure-like event (SLE) generation. Using a detailed computational model of a small network of neurons, the authors demonstrate that the complex interaction between specific ion species may give rise to SLE. The detailed analysis of the computational model provides an interesting approach to developing a unifying framework for neural dynamics. The strength of this manuscript is in the direct validation of key aspects of the computational model using in vitro electrophysiology. Additionally, predictions made by the model such as the slowing of inter-burst intervals are subsequently validated in both human and mouse data. The conclusions made by the authors of this manuscript are supported by their results and are in line with previous work in the field. Finally, the manuscript does a good job relating the novel results of this new manuscript with established results in the field.

1. A strength of this manuscript is the direct validation of the computational model with experimental results. Given the multitude of methods available for inducing seizure-like events (SLE) in vitro, it is a bit surprising that the authors chose to use an arterial application of bicuculline (Figure 3). Bicuculline is a competitive antagonist of the GABA-A receptor resulting in the reduction of inhibitory GABAergic signaling. However, the SLE induced in the model is caused by an increase in inhibitory activity, through direct depolarization, rather than a decrease in GABAergic signaling. At first glance these methods for inducing SLE seem to be at odds with one another. Given the observed increase in extracellular K+ at SLE onset, this mismatch in the method for SLE generation in vitro and in silico may further highlight one of the primary claims of the manuscript specifically that disruption of ionic homeostasis rather than solely synaptic excitatory/inhibitory imbalance is a mechanism for SLE generation. Additional discussion of this observation and similar phenomena in other methods for SLE generation in vitro would further strengthen this interesting point.

2. Bifurcation analysis in figure 4A produces interesting results that are in line with and supported by previous work. As stated in the text, an assumption made by the authors is that the intracellular dendritic and somatic Na+ is equal. The authors further mention that this assumption may result in an overestimation of dendritic Na+ and Na/K pump activity but do not discuss how this might impact the results presented in the bifurcation diagrams. Please include.

3. It is striking that the time course of the extracellular dendritic K+ concentration is much slower than for the soma. It is not clear if the delayed increase in dendritic K+ is a prediction of the computational model or if it has been experimentally observed and incorporated into the model as such. Some discussion clarifying this point is needed. To that point, are the authors suggesting that the longitudinal diffusion of K+ from soma to dendrite is driving the delayed increase? If so, how might the observed dynamics change if the direction was reversed? The computational model contains an inhibitory neuron which seems to target specifically the soma. For this reason, it is not surprising that the somatic K+ increases first. However, peri-somatic inhibition is a characteristic of PV-inhibitory interneurons. Somatostatin (SOM) expressing inhibitory interneurons predominantly target dendrites. Given recent studies showing that stimulation of either SOM or PV interneurons can trigger seizure onset, how might this impact the bifurcation dynamics presented here?

4. The results pertaining to Cl concentration are interesting and extend a large number of recent studies examining the role of Cl in seizure dynamics. With regards to the KCC2 co-transporter this story becomes more interesting as it may have an impact on febrile seizures and seizures in children as the levels of KCC2 are lower and so the Cl concentration dynamics are not regulated in the same manner as in the adult brain. This may lead to age-related differences in seizure susceptibility between children and adults. Given the results presented in this manuscript some brief discussion on this topic may help highlight the impact of this finding.

5. Given the amount of detail in the computational model there remains a number of network parameters that would be interesting to explore. Of specific interest would be the volume dynamics as there is ample experimental data demonstrating substantial changes in interstitial volume prior to seizure onset.

1. In its current form, the schematic in figure 1 gives the impression that vasculature and astrocytic interactions are included in the model. I believe it is not. It might be useful to drop those cartoons from the schematic to prevent confusion regarding what is specifically being modeled.

2. Please show specific examples of each activity type (resting state, tonic spiking, and bursting), in figure 2 when they are first described.

3. The stimulation of IN was said to result in a firing rate of 270Hz. It does not seem to be very realistic. Is there experimental evidence to justify such an increase in firing rate of IN neuron prior to SLE? If the model would be changed to get a lower firing rate would this affect the results?

4. Does blocking or reducing GABA-A conductance in the model without additional IN stimulation result in SLE? It is not clear if that is the case. If it does, this would be an interesting result to show or reference as it is a more one-to-one comparison with the experimental model of SLE.

5. In figure 3, a better comparison might be to apply the same or similar depolarization to the model PY as was done in the experiment. This could better highlight the match between the experimental and modelling results.

6. When discussing the bifurcation diagrams, it might be beneficial to discuss the types of bifurcations that occur at the specific transitions between activity regimes.

7. Did the authors consider the effects of HCO3- in GABAergic currents? Since it was included as part of the GABA current and the fact the HCO3- concentrations are crucial for maintaining GABA-A receptor reversal potentials some discussion on the role of HCO3- in this regard would be needed.

8. Volume dynamics were included in this model and have been previously explored in other models (e.g., Schiff lab). How did volume change during the course of the simulation? How does volume impact the bifurcation diagrams for dendritic vs somatic K concentration?

Reviewer #3 (Recommendations for the authors):

Gentiletti et al. uses a computational model to investigate the mechanism underlying focal seizures. The small-network model consists of one interneuron and four pyramidal cells with various active and passive currents, and detailed ion concentration dynamics. The main focus of the study is to validate the hypothesis and previous results about the interneuronal origin of focal seizures. Specifically, in the model seizures are induced by stimulating the interneuron, which then raises the extracellular potassium ([K]o) levels, leading to high-frequency spiking in pyramidal cells. Detailed analysis of the pre-ictal, ictal, and post-ictal periods during seizures is also offered.

While technically sound, the study does not offer any major new innovations to warrant publication in eLife. I believe that the analysis presented is similar, in many ways, to previous modeling studies, but with a slightly different view. As detailed below, in some places it feels that the model parameters are selected so that a desired result is produced. The idea that interneurons can cause seizures by itself is not entirely new. There is extensive experimental (some cited by authors) and some modeling data supporting this hypothesis. Thus, I feel that the paper is more suitable for a specialized journal in computational neuroscience.

Following are some specific concerns about the study.

Figure 2 and related text: The experimental data shown for comparison is confusing. It is not clear if these are new experiments done for this study or data from three different previous studies are combined for comparison with the model. Another confusion about the experimental data is that in the beginning, it is mentioned that seizures are induced by bicuculine in the isolated guinea pig brain (Figure 3A), but later it is mentioned that "The strong preictal firing of the PY cells was artificially triggered by the injection of a steady depolarizing current via the intracellular recording electrode to analyze the intracellular firing correlates during the SLE (Gnatkovsky et al., 2008)." This gives the impression that the experimental traces shown for comparison are from three different experiments where the seizures are induced by different mechanisms, and are selected because they match what the model does.

Figure 6. In some places, it seems that the model is made to behave like the experiment. For example, in Figure 6, no reason is given for why the pyramidal cells are stimulated with 6 pA current. What would be the circumstances in the tissue or intact brain where the pyramidal cells would receive such input?

Lines 413 – 419: The paper claims that the previous modeling studies induced seizures by either stimulating pyramidal cells or increasing [K]o, whereas in this study, seizure is induced in the model by stimulating the interneuron. On the surface, this is true. But in reality, the approach adopted by this study is an indirect method of raising extracellular potassium of pyramidal cells. Stimulating interneurons leads to higher [K]o and hence seizures. This is also acknowledged by the authors. However, what is not clear is that why in the network only interneurons would receive strong depolarizing stimulus but not pyramidal cells. It should also be noted that the interplay between interneurons and pyramidal cells during seizures under normal [K]o in a modeling study was first reported by Wei et al. (2014) (PMID: 24671540).

Line 437-439: "This suggests that in our model, a change in the concentrations of either [K+]o or [Cl-]i was not sufficient to initiate an SLE and that an increase in both is necessary." This seems to be a model-specific effect because several modeling studies have shown that raising [K]o alone can cause the network to enter seizure-like state.

Line 250: [Na+]I should be [Na+]i.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Focal seizures are organized by feedback between neural activity and ion concentration changes" for consideration by eLife. We apologise for the delay in assessing your revised manuscript, this was caused by our inability to secure one of the original reviewers which required finding an additional reviewer. This version of your article has now been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Joseph V Raimondo (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In general, the reviewers were positive about the manuscript and the changes made.

Essential revisions:

We ask that you focus specifically on addressing the following

1. Clarify the specific novel contributions of this work in the abstract. The role of Na+, Na+/K+ pump on termination and Cl- on seizure initiation have been previously shown.

2. The bifurcation analysis that suggests soma and dendrite differences for K+ concentration resulting in different regimes is interesting. Could you add to the discussion whether there is any experimental evidence for such significant differences in the concentrations for soma and dendrite?

3. With reference to the bicuculline model, could you add to the discussion in order to explain your mechanistic reasoning for how this “recruits the interneuronal network”

4. As the slowing of the interburst interval is one of the novel aspects of this work, it would be helpful to show that ion changes influence the inter-burst interval variations observed during the course of the seizure. Specifically, could you identify the bursting frequencies from the bifurcation analysis and confirm the role of Na+ accumulation in the slowing of burst interval.

Please find the full reviews below:

Reviewer #1 (Recommendations for the authors):

In this much revised manuscript the authors have improved several features of how ion dynamics were modelled enhancing the validity of their findings. The authors have gone to great lengths to address my concerns. In my opinion the manuscript enhances our understanding of the mechanisms underlying seizure dynamics.

Novelty

[Interneurons driving seizure onset] The authors have generated a thorough model of how intense activity of interneurons can drive K+ build-up and the initiation of seizures. This is certainly the most thorough and biophysically realistic model which recapitulates the electrographic feature of human seizures in a satisfying manner.

[Increased Na+/K+-pump driving the SLE termination and the post-ictal state]. The authors state that “We show for the first time that seizure termination and postictal state may be generated by the same mechanism mediated by increased activity of the Na+/K+-pump. It is an alternative mechanism of the postictal state, which previously has been suggested to depend on potassium undershoot (Krishnan and Bazhenov, 2011).” I disagree with the authors’ interpretation and insistence that this is novel. In Krishnan and Bazhenov, they explicitly describe essentially the same mechanism. Their potassium undershoot is caused by increased activity of the Na+/K+-pump (the show and state this explicitly).

“In our model extracellular potassium decays to baseline after an SLE offset, hence it cannot account for the postictal state.” This is also what (Krishnan and Bazhenov, 2011) show (see their Figure 8). I can’t see any fundamental difference between your interpretation and theirs, which is certainly satisfying, but not new as far as I can tell.

[Exponential IBI distribution]. I agree that the model satisfyingly shows how accounting for ion concentration changes can generate an exponential IBI distribution toward the end of the seizure.

Other responses:

I thank the authors for clarifying that in their model bicuculline does not block all of GABAergic inhibition, but is likely a transient perturbation which somewhat counterintuitively recruits the interneuronal network.

The authors have gone to great lengths to improve how Cl- flux through GABAaRs and the Cl- leak conductance was modelled. Figure 5 is a wonderful figure (along with Appendix – Figure 3). I am now satisfied that the ion dynamics were modelled in a suitable way which gives me much increased confidence in the authors’ findings.

Reviewer #4 (Recommendations for the authors):

In this work, the authors use a computational model to examine the role of ion dynamics in inhibition-mediated TLE seizures. Of significance, the seizure activity precisely matched the experimental data, specifically the time course of the inter-burst interval. The study also replicates previous experimental and computational observations on the role of K+ on seizure initiation, Na+, Na+/K+ pump on seizure termination. Further, the findings from this work suggest additional contributions of Na+/K+ pump to post-ictal depression and K+ influence on KCC2 pump promote seizure initiation.

While the paper’s findings are a significant contribution that emphasizes the importance of ion dynamics on seizure, the novel contribution highlighted by authors seems only as slight variations of previously proposed mechanisms. Nevertheless, the manuscript is definitely worthy of publication, perhaps in a more specialized journal.

Few suggestions that could improve the manuscript:

1. Bicuculline, a GABA antagonist induced the seizure in the experimental condition, but in the computational model, seizure was induced by increasing the inhibitory neurons’ activity. While the increase in inhibitory neuron’s activity is observed following bicuculline in the experiment, there is a missing network mechanism that results in this increase of inhibitory neurons activity following the application of bicuculline. It would be more compelling if the authors could identify this mechanism and demonstrate the onset of a seizure by bicuculline in the computational model.

2. It would be very helpful to clarify the specific novel contributions of this work in the abstract. The role of Na+, Na+/K+ pump on termination and Cl- on seizure initiation have been previously shown. Also, it would be helpful ’or authors to note that K+ influenced the KCC2 pump time constant in Gonzalez et al., 2018.

3. The bifurcation analysis that suggests soma and dendrite differences for K+ concentration resulting in different regimes is interesting. It would be helpful to expand on this finding, and the report is one of the novel contributions. Is there any experimental evidence for such significant differences in the concentrations for soma and dendrite?

4. It would be helpful to show that ion changes influence the inter-burst interval variations observed during the course of the seizure. Specifically, the authors could identify the bursting frequencies from the bifurcation analysis and confirm the role of Na+ accumulation in the slowing of burst interval.
