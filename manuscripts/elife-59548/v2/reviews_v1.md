# Peer review - Round 1

Editors:
- Frances K Skinner, Krembil Research Institute, University Health Network Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59548.sa1](https://doi.org/10.7554/eLife.59548.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study effectively combines experimental and modeling work to show and explain the synergistic effects of blocking GABA transporters on thalamocortical oscillations. This is shown to be due to a dependence of T-type calcium channel gating on GABAB receptor activity.

Decision letter after peer review:

Thank you for submitting your article "Nonlinearities between inhibition and T-type calcium channel activity bidirectionally regulate thalamic oscillations" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Frances K Skinner as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Maxim Bazhenov (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional information is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper addresses the ability of thalamic relay neurons to generate low threshold spikes (and bursts) under conditions when GABA-A-receptors are blocked, and a GABA-B type conductance is applied. The GABA-B conductance has amplitude and kinetics determined by the presence or absence, alone or together, of 2 types of GABA transporter (GAT1 and GAT3). The authors examine effects of GAT1, GAT3 and combined GAT1+GAT3 blocking on thalamocortical bursting activity using combination of experimental techniques and computational modeling (single cell and network). They report when GAT1 or GAT3 is blocked, there was an increase in the thalamocortical oscillations and bursting, however when both GAT 1 and 3 are blocked, the oscillations and bursting were abolished. Based on dynamic-clamp techniques and fitting to the model, the authors identified that interaction of GABA-B with T-channel activation is critical for the differential effect. Specifically, the fast repolarization from a hyperpolarization state led to LTS and eventually to oscillations in case of GAT1/3 blocking. In contrast, blocking both GAT1 and 3 led to prolonged inhibition that prevented LTS. These finding suggests a careful balance between inhibition (GABA-A and B) and calcium currents determines the LTS properties, and bursting in the thalamocortical neurons. Overall, solid work that combines experiment and modeling.

Essential revisions:

While all of the reviewers thought that this was very good work, they all struggled with presentation clarity and a clear summary message about mechanisms involved. The authors are asked to distill and improve the presentation of their work which is very heavy in places.

It was thought that if authors have a clear understanding of principles and mechanisms, they should be able to express it in a clear way in the Abstract/Introduction/Discussion.

For some of the points raised by the reviewers it was decided that it would be at the authors' discretion whether to include them as part of the present revisions (referred to as optional below). The authors could consider them in subsequent work.

1) Experiments: There seem to be washout effect differences with the 2 different blockers. This would seem to potentially play a role on the synergistic abolition? Did you examine oscillations for longer with GAT1 or GAT3 blockers separately as done for the combination? Also, based on the raw recordings shown in Figure 1(iv), the “elimination” could potentially be lower amplitude oscillations? I wondered whether spectral/frequency analyses would be helpful and/or show something additional to PSTHs.

2) Single cell experiments: The dynamic clamp GABAB conductance “approach” would circumvent the experimental variability referred to, it does introduce a different issue in considering the biology – i.e., spatial aspects since one is only looking somatically. So, the comparison can be more “robust” but then the single neuron effect should perhaps be tempered? The authors should comment on how they expect that this would affect their results and interpretation. That is, the GAT3 blockage has an extended temporal effect which is further extended with the combination. I think this should be unpacked a bit more for interpretation purposes.

3) Once one sees Figure 2B, the rest of the aspects of the paper are pretty straightforward and then is mainly about heterogeneous responses moving forward. I am not sure if it is fair to so clearly link the thalamic oscillations directly to the rebound burst aspect (single cell) for these “bidirectional differences”. It then started to get a bit confusing about interpretation of it all (see above point). That is, I think that the authors are assuming an underlying mechanism about TC cells rebound and thalamic oscillations – presumably it is based on previous network modeling studies that they build on later – but the heterogeneous responses and 1 and 2 points above give me a bit of pause. At this stage, they have shown a correlation of network oscillations and single cell responses with GAT blockers.

4) Model: For the examples shown in Figure 3D, could the authors say which cases they are in 3E – presumably well-fit ones? I think that it would be helpful to show the non well-fit cases to see the difference (supplementary figures as in eLife structure could help with this presentation).

5) While the cellular heterogeneity modeling and importance is interesting, and the authors' use of 3 compartment models seems reasonable, the general statements about commonalities of T channel/A channel densities need to be tempered and/or explained a bit more, especially given the limited nature of the models. Figure 3F are where the various parameters are shown but hard to appreciate/understand them in light of the statements. A statement about negative correlation is mentioned as an example. The authors go on to fully explore T-type calcium channels, and bring about the temporal aspects which make sense given kinetic differences noted from the experimental work.

However, I did wonder what one would get if a thorough exploration was done with h-channels to understand the differential effects? Or was this clear already? (this latter point is optional to address in the revised manuscript).

6) The network oscillation modeling and heterogeneous aspects claimed seemed to leave out a lot without mention (see points 1 and 2 above for example). I was also not sure why and whether it was “fair” to add and consider the trial-to-trial variability via the leak reversal potential (given the different TC models)? For example, did it matter which TC model one chose (Figure 3E) to use for the homogeneous networks to compare with heterogeneous? Was some aspect from the 2-cell network used as guidance in the choice for the larger networks? (I may have missed that?)

7) Figure 1C: Why do oscillations seem much shorter "before" drug application in NO and SNAP conditions compare to Control? In fact, in NO condition oscillations seem to be lasting as long as in Control.

8) In both slice experiments and the model, the GABA-A synapse was blocked by bicuculline. However, in-vivo condition would involve the interaction of both GABA-A and GABA-B channels. While this may be difficult to examine in the slice work, it is feasible to examine in the computational model. It would be important to understand how the GABA-A fast acting time scale impacts the effect of slower changing GABA-B synapse, especially in network simulations.

9) Based on the fitting of dynamic-clamp data to the model, the authors' predict high density of T-channel in dendrites and A-channel density in soma. While the rest of the work, especially the computational modeling, has focused on T-channel, the changes to A-channel have not been examined. Similar to the findings in Figure 5-6 on T-channel, it would be helpful to examine the effect of A-channel (this last point is optional to addressed in a revised manuscript).

10) Given that the T-channel is involved in the generation of spindle activity during sleep, it would be helpful to include some discussion about the impact of the findings on sleep spindles.

11) While the authors have developed an interesting measure called the T-channel open channel discrepancy, I feel that the effect could be well captured using conventional phase-plane or phase-space projections. It seems that the membrane voltage, T-channel activation and inactivation variables pass through a critical region in phase-space which is required for the LTS; the failure of this dynamics leads to the lack of LTS. Possibly 3D phase-space analysis of these variables could identify the critical region?

(this point is optional to address in a revised manuscript).

12) The section "Interplay between GABAB receptors and T-type calcium channels " is extremely long and difficult to follow. I am sure some readers will follow all the details there but for many others the message may be lost. I suggest some rewriting to include summaries and highlight the main results.

13) In the network simulations (Figure 8), for TC-homogeneous case, oscillations seem to be more synchronized in control vs GAT1 or GAT3 block conditions. Why is this so?

14) The way the manuscript is written, it is somewhat difficult to learn what is actually a precise mechanism behind the differences between effects of individual GAT1/3 blocking vs dual blocking. E.g., the Summary in discussion says: "…respectively, can be recapitulated by varying the GABAB receptor activation waveform." but it does not provide a needed summary of the mechanisms discovered in the study.

15) Consequences of the GABA-B conductance properties are reflected in the behavior of individual cells, and of oscillating networks of TCR and nRT (nucleus reticularis) neurons. Details of the GABA-B conductances to be used were determined in prior publications. Experimental and numerical experiments were performed in thalamocortical slices, in dynamic clamp applied to single TCR neurons, and in simulations of 3-compartment TCR neurons alone, paired with an nRT cell, and in a TCR/nRT network. The main finding is that excessively large and prolonged GABA-B conductances interfere with LTS generation; detailed analysis shows that the specific kinetic properties of T-channels are responsible, in that LTS requires an epoch where inward current is regenerative (increasing m) at the same time as inactivation is not too developed, and the latter in turn depends on instantaneous inactivation (h) being larger than would occur at equilibrium. Such large slow conductances develop when both transport blockers are applied together, but not separately. The authors provide some discussion of possible relations to spike-wave seizures, and the effects and contrary side-effects of certain anticonvulsants.

I suspect that the mathematics involved is more general than discussed here for T-type calcium channels, and depends at heart (no pun intended) on the slowness of inactivation vs activation. An example might be the inability of a squid axon to fire at low frequencies, even in the presence of a low calcium buffer. The authors may, at their discretion, want to consider this larger issue (optional to address in a revised manuscript).
