# Peer review - Round 1

Editors:
- Albert Compte, https://ror.org/054vayn55 IDIBAPS Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79352.sa0](https://doi.org/10.7554/eLife.79352.sa0)

This valuable modeling study proposes a local circuit mechanism based on a network of recurrently connected excitatory and inhibitory neurons for the recently reported effect that NMDA receptor antagonists cause a drastic reduction of prefrontal neural synchronization in preparation for motor responses in a cognitive task. This mechanism is convincingly supported by simulations of spiking networks and a thorough analysis of the parameter dependency of network dynamics using mean-field theory. The work will be of general interest to computational neuroscientists, and especially for those interested in computational psychiatry.


---

# Peer review - Round 1

Editors:
- Albert Compte, https://ror.org/054vayn55 IDIBAPS Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79352.sa1](https://doi.org/10.7554/eLife.79352.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A prefrontal network model operating near steady and oscillatory states links spike desynchronization and synaptic deficits in schizophrenia" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Albert Compte as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by John Huguenard as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Yashar Ahmadian (Reviewer #2).

The manuscript is currently not suitable for publication in eLife, but we are willing to consider a revised version that would fully address all concerns of the reviewers. The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers consider that the manuscript has potential but it requires extensive revisions and new simulations to support its claims. Because these are substantial revisions, a revised manuscript will be critically reviewed in depth again and sent back out to the original reviewers.

The interest in the computational results depends critically on the ability of the model to provide a convincing explanation of the experimental data (Zick et al. 2018, 2021). For this, it is essential to:

1) consider not only the dynamics of synchronization (Figure 1) but also the dynamics of firing rate, and not only the period immediately preceding motor action but also the dynamics of the effects following motor action and around the stimulus cue. The mechanisms of the computational model make specific predictions as to how the dynamics of firing rate and oscillatory synchronization will be associated, and this should be specifically validated against the experimental data.

2) consider how the model accommodates a U-shape relationship between NMDAR modulation and network synchrony. Existing evidence shows that 0-lag synchrony in prefrontal networks is affected by manipulations that reduce NMDAR function (Zick et al. 2018) and by manipulations that enhance NMDAR function (Zick et al. 2021). The computational model presented in this manuscript does not show this U-shape behavior and the discussion does not mention this.

In addition, the theoretical understanding of the model should be enhanced by:

3) expanding the theoretical analysis to provide more intuition on the way NMDA works the way it does, and clarification of its distinct role in synchronization (in contrast to AMPA).

4) investigating how synchrony in the model reacts to transient external inputs and how the model can produce weakly oscillatory synchrony.

Finally, all reviewers were concerned about the emphasis on the association with schizophrenia, so we recommend:

5) moving speculative links to schizophrenia to the Discussion section. Also, please broaden the scope of this discussion with available literature on how synchrony and STDP interact in computational models, and with alternative explanations based on changes in NMDAR-dependent synaptic plasticity irrespective of synchronization.

Reviewer #1 (Recommendations for the authors):

Here are some specific recommendations for improvement of the manuscript:

1) The last two paragraphs in the introduction are largely discussional in spirit. The paragraph before last does not make much sense here, at a point where the reader is not yet familiar with the details of the model proposed. The very last paragraph is also mostly speculative in how the results in this manuscript would be important for schizophrenia and would appear more natural in the Discussion section.

2) The data presented in Figure 1 could be presented more fully in order to provide more constraints for the model so as to enhance its biological plausibility. For instance, it would be most interesting to have a parallel plot of the firing rate in these same neurons to see how neuronal activity evolves through the task. Neurons show a response to the cue stimulus (Zick et al. 2018), which may be similar to the response at the time of the response, and that is something that the model would have to explain: how does the control network react with strong synchronization when it receives inputs prior to the response but instead does not show any synchronization when it receives inputs at the time of the cue? Also, it would be good to show panel b extended for a time window after motor response time t=0 to compare the time course of firing rate and synchrony increases. This could also constrain further the network model.

3) In Figure 1 it would be good to have a dashed horizontal line at y=0 to separate correlated (y>0) from anti-correlated (y<0) activity more clearly. I would also recommend changing the x-axis label ("time lag") because this is now used in cross-correlation functions in Figure 4 and they are intrinsically different. The synchrony plot should also include error bars and proper inference about differences between the two conditions at different time points. For clarity, it would be nice to indicate with a shaded area or horizontal bar the period of cue stimulus presentation, too.

4) Briefly mention in line 167 what spiking neuron model you are using

5) Mention of "GABA receptors" in line 173 suggests that the model includes both GABA_A and GABA_B receptors.

6) Verb missing in "and mediated" in line 174.

7) In Figure 3 the color code red/blue means two different things: excitatory vs. inhibitory neurons, and steady vs. critical networks. This is confusing and should be clarified with different color codes for each thing.

Reviewer #2 (Recommendations for the authors):

1) I assume elucidation of the precise mechanism by which external inputs or NMDA affect synchrony can be achieved by analytically inspecting the direct and indirect dependence of the real part of the relevant complex eigenvalue on the synaptic conductances and external inputs, either directly or indirectly via the dependence of linearized neural gains in the background operating point (which itself depends on the external input and the synaptic parameters).

2) The authors do refer to the Compte et al. 2000 study that found that when the total strength of excitatory connectivity is fixed, tilting the relative strength of NMDAR and AMPAR towards the former disfavors synchronous oscillations (with relatively high frequency in or near the γ band). Previous studies (e.g. Wang and Brunel 2003, Tsodyks et al. 1997, and Compte et al. 2000) have pointed out the role of the negative feedback loop between excitatory and inhibitory populations mediated by the fast receptors AMPA and GABA in γ-band oscillations. Again I think the mean-field theory and the stability analysis based on it could be used to elucidate the differences and similarities in the pathways by which NMDAR and AMPAR affect the transition to synchrony. For example, the role of NMDAR could be via the explicit dependence of the growth rate of oscillations (the eigenvalue real part) on g_NMDA, or (most likely) via the effect of NMDAR-based excitation on background rates (which indirectly affect the eigenvalue).

3) Regarding the link to "disconnection" via STDP. Various studies have found that STDP in (initially randomly connected) networks in the asynchronous state can maintain random connectivity (Morrison et al. 2007 – DOI: 10.1162/neco.2007.19.6.1437) or even lead to the emergence of structured connectivity (Izhikevich et al. 2004, Babadi and Abbott 2013, and Litwin-Kumar and Doiron 2014 -- DOIs: 10.1093/cercor/bhh053, 10.1371/journal.pcbi.1002906, 10.1038/ncomms6319). In lieu of evidence (either previous studies or new simulations/modeling by the authors) for this claim, I suggest weakening the claim to saying that the NMDAR-related reduction in synchrony, as a specific disruption in the patterns of precise spike timing, can lead to abnormal changes in patterns of synaptic connectivity via STDP. I also suggest citing the above-mentioned (or similar) studies on previous studies of STDP in asynchronous (or synchronous) states, or any other studies that support specific claims by the authors in this regard.

Other suggestions:

– Figure 6 top: here the cross-correlation plot based on monkey data (as in the model) exhibits nonzero lag "γ" peaks. But these seem to be absent in the data shown in the Neuron paper (e.g. Figure 4D therein). Can the authors comment on this seeming discrepancy? Is this because data only from one of the monkeys (showing stronger effects) was included in the current paper? Can the authors also comment on the flatness of the CCH in the "initial probe period" in the monkey data in contrast to the small 0-lag peak in the model CCH?

– Lines 104-105: I found the meaning of *balance between* in this sentence vague/unclear. What does the balance between NMDA inputs and oscillatory activity mean?

– I suggest the authors also mention (e.g. around lines 476-477 where they discuss their assumption 1, and as further support for this assumption) that in their empirical data (Neuron paper) they do find an increase in PFC neural firing rates in the pre-response period, which will presumably also arise in their model from the increase in external inputs.

– Line 781: "themes" → "times".

– Line 838: I would explain where this equation comes from (I understand it accounts for the effect of reset on mean membrane potential), and also what v_α denotes.

Reviewer #3 (Recommendations for the authors):

Here are issues that I believe the authors should address before the paper can be published:

1. In Figure 1, the authors only show the synchrony before the motor response. I believe it would be instructive to show also what happens after motor response, to visualize how temporally precise is this increase. It would also be useful to show the time course of average firing rates. The explanation of the authors relies on an increase in external input to generate an increase in synchrony – this increase in external input should be reflected in an increase in the average firing rate as well.

2. Figure 6 shows a strong difference between the network model and data – side peaks in spike correlations are much more prominent in the model than in the data. Thus, synchronization in the data is much less oscillatory than in the model. Is there a way in the model to get such weakly oscillatory synchrony? If not, can the authors speculate as to what additional mechanisms would lead to a reduction of γ power, preserving zero lag synchrony?

3. In the data, the increase in synchrony is transient. In the simulations, the author considers the case of stationary external inputs. I believe the authors should also investigate the case of transient increases of external inputs leading to a more realistic time course of synchrony. Such a scenario could also help in solving

the issue mentioned in 2.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A prefrontal network model operating near steady and oscillatory states links spike desynchronization and synaptic deficits in schizophrenia" for further consideration by eLife. Your revised article has been evaluated by John Huguenard (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The dynamics of average firing rates in Figure 1 should mark clearly the various relevant periods of the task on the time axis: probe interval, motor response, etc.

2. The new theoretical analyses in this revision have greatly extended the length of the main text, but the additional insight provided is not clearly explained and in its current form it can lead to confusion. It is suggested that most of this material is moved to a supplementary document and a more concise and clearly delineated section in the main text provides the fundamental message of how NMDARs influence network synchronization.

Reviewer #3 (Recommendations for the authors):

The paper has been considerably improved and I would like to congratulate the authors for their hard work. There are still a couple of issues though that I think should be addressed to improve the paper further.

1. In response to one of the main concerns of the reviewers, the authors have expanded Figure 1 to include the dynamics of average firing rates in the data and the effect of NMDAR blockade on this dynamic. This is a welcome addition, but I think this figure could be improved to better understand the time course of the task. Currently, there is no discussion at all about when the motor response is happening and so the left and right panels seem totally disconnected. One has to go back to the original paper by Zick et al. to understand when the motor response happens. I would suggest extending the left panels to include the whole trial (including the `probe' interval), adding where the mean response time is similar to Figure 4 in the Zick et al. 2018 paper. Or at the very least indicate when is the mean response time (time 0 in right panels) with respect to the time axis of the left panels.

2. In response to another concern, the authors have considerably expanded their theoretical analysis with a detailed description of an approximation for the instability growth rate. However, while the approximation itself represents an interesting new derivation, I did not find that it brings much insight, and in fact in some ways introduces additional confusion, for the following reasons. (i) The main new result of this new analysis is the new Equation (1). In this equation, the LambdaRs play critical roles and are the subject of much of the later discussion, however, their meaning is not really explained in the main text and one has to go to the Methods to understand what they really are. (ii) The new Figure (10) indicates that the growth rate is primarily determined by the AMPA term and that the GABA term plays little role. This is quite confusing as oscillations in such networks relies on GABAR mediated negative feedback. How can the authors explain this fact? (iii) After reading the new part, I ended up not having much more insight about mechanisms. My guess at this point is that NMDAR influences the synchronisation properties of the network by providing an additional excitatory drive, thereby playing a similar role as the external excitatory input. I have the feeling that is what the authors are trying to say when they say that the NMDAR term acts through changes in phiprime (the slope of the transfer function), which is exactly how the external inputs act, but it feel like it could be explained in a much clearer way.
