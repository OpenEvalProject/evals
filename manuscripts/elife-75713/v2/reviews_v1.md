# Peer review - Round 1

Editors:
- Muriel Thoby-Brisson, https://ror.org/057qpr032 CNRS Université de Bordeaux France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75713.sa0](https://doi.org/10.7554/eLife.75713.sa0)

This article is of significant interest to readers in the field of neural control of breathing and for researchers interested in the generation of neuronal rhythms in general. The study assembles a sophisticated computational modeling approach to test long-standing theories and emerging views in neural control of breathing and more specifically on biophysical mechanisms of burstlet generation in the respiratory network (the preBötzinger complex network). This work is an important contribution to a better understanding of the respiratory rhythm generation, will help validate (or not) running hypotheses and will guide future experiments.


---

# Peer review - Round 1

Editors:
- Muriel Thoby-Brisson, https://ror.org/057qpr032 CNRS Université de Bordeaux France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75713.sa1](https://doi.org/10.7554/eLife.75713.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Putting the theory into 'burstlet theory': A biophysical model of bursts and burstlets in the respiratory preBötzinger complex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Nicholas Mellen (Reviewer #2); Sharmila Venugopal (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Your paper has been examined by three reviewers and myself. Below are their detailed reviews, but find also here a quick summary of their main comments that must be addressed in a revised version in order for us to judge the potential suitability of your study to be published in eLife.

1) Model development is based on a few groups' work, (almost entirely) based on in vitro patch-clamp techniques in neonates and slice preparations. This is extremely important to acknowledge and authors should try and add some valuable discussion on translation to in vivo situations or including a more complete part of the central respiratory command (the RTN/pFRG, pontine structures,….).

2) It is necessary for the authors to make the model more general by showing qualitatively similar CICR-mediated burstlet-to-burst amplification when alternative rhythmogenic mechanisms are used (not exclusively based on INaP for instance, considering the role of intra-network connectivity, etc…), otherwise it narrows down the model's relevance and potential application in other systems.

3) More clarity is needed in the discussion of how model predictions could guide new experiments particularly since the model sets out to challenge prevailing and proposed views of breathing rhythm and pattern generation.

4) The model code must be made available for review and upon acceptance be shared widely on GitHub and not just upload on ModelDB where many models don't even work.

Reviewer #1 (Recommendations for the authors):

I think for the claim to provide unifying model for respiratory rhythm generation the modelling approach of Shao J, Tsao T-H & Butera R (2006). Bursting Without Slow Kinetics: A Role for a Small World? Neural Computation 18, 2029-2035 needs to be considered. In addition work using the perfused brainstem preparation further supports the notion of network connectivity for the emergence of burstlets and burst in the phrenic motor output. See: Jones SE, Dutschmann M. Testing the hypothesis of neurodegeneracy in respiratory network function with a priori transected arterially perfused brain stem preparation of rat. J Neurophysiol. 2016 May 1;115(5):2593-607. doi: 10.1152/jn.01073.2015. Epub 2016 Feb 17. PMID: 26888109; PMCID: PMC4922475.

While I understand that it might be not possible to extend the current modelling approach to consider the network connectivity beyond its current stage it is the bare minimum to discuss the above-mentioned model and experimental data.

Reviewer #2 (Recommendations for the authors):

In what follows, textual revisions are suggested.

Lines 108-112: "In this computational study, we put together and build upon these previous findings to show that periodic amplification of synaptically triggered ICAN transients by calcium induced calcium release (CICR) from intracellular stores provides a plausible mechanism that can produce the observed conversion of burstlets into bursts and can explain all of the key observations underlying the burstlet theory of respiratory rhythm generation, thus providing a sound mechanistic basis for this conceptual framework.”

– This is too strong: the mechanism by which burstlets are generated at a stable frequency is stipulated using generic methods for which experimental evidence is weak.

Lines 148, 149: Increasing IAPP increases the burst frequency in neuron 1 and decreases the number of spikes per neuron 1 burst (Figure 2A3,A4), consistent with past literature (Butera et al., 1999).

– This doesn't seem to be the case for traces shown in 2C2-2C4. Also, this is same result is shown to be the case in (9).

Lines 240-244: The decrease in amplitude in the case of ICAN block is due to derecruitment of neurons from the pattern forming subpopulation and a decrease in the firing rate of the neurons that remain active, whereas in the case of ca2+ block the decrease in amplitude results primarily from derecruitment (Figure 5E & F). These simulations provide mechanism-specific predictions that can be experimentally tested.

– This appears to have been experimentally tested in a study cited later in your paper (lines 434-438): "In a separate study, however, block of the SERCA pump by bath application of thapsigargin (2-20 uM) or cyclopiazonic acid (CPA) (30 – 50 uM) did not significantly affect the amplitude or frequency of hypoglossal motor output in in vitro slice preparations containing the preBötC. It is possible that the negative results presented by the latter work occur due to the failure of pharmacological agents to fully penetrate the slice and diffuse across the cell membranes to reach their intracellular targets." This isn't supported by Figure 5 D, which shows that burst amplitude decreases in a graded manner with I(CAN) blockade. Thus, even if the pharmacological agents only partially penetrated the tissue, you would nonetheless expect an attenuation of amplitude.

Lines 276-278: These elicited bursts occur with delays of several hundred milliseconds relative to the stimulation time, which is longer than would be expected from existing models. Interestingly, in the current model, due to the dynamics of CICR, there is a natural delay between the onset of burstlets and the recruitment of the follower population that underlies the transition to a burst.

– For me at least, identifying model components with slower time-constants is key to developing intuitions about how models work. It might be useful to add some text to the part of the paper where you describe this component of the model (starting roughly at line 647), providing a description of the different rates of the processes that follow.

Lines 290, 291: Moreover, the probability of elicting (typo in the text) a burst increases and the delay decreases as the time after an endogenous burst increases (Figure 7G,H).

– This result seems to have little to do with CICR-related processes, and instead be due to the dynamics of your I(NaP) bursters. As such, at least some of what you report here is in fact determined by your choice of rhythmogenic mechanism, which seems to be stipulated rather than empirically grounded. This goes against the claim made in lines 605-607 quoted above.

Lines 301-303: These simulations were conducted with fixed network synaptic strength, defined as S = N(P) * P(PP)* W(PP), where W(P)P is adjusted to compensate for changes in P(PP) to keep S constant.

– What is the motivation for keeping synaptic strength fixed? Is it motivated by the biology, or for computational efficiency? Whatever the motivation, the findings you report in lines 311-319 seem to flow directly from this choice.

Lines 372-374: Our simulations support an alternative view that builds directly from previous computational studies (Jasinski et al., 2013; Phillips et al., 2019; Phillips and Rubin, 2019; Phillips et al., 2021), which robustly reproduce a wide array of experimental observations.

– The fly in the ointment here is that there was a period when endogenous bursters were presented as the mechanism for respiratory rhythmogenesis, and everyone went looking for them, and they just weren't found in sufficient numbers to carry the story. This may have been due to technical limitations, since most groups were using single-unit recording methods. Currently, the inducible dbx1-cre mouse, when crossed with a genetically encoded ca2+ indicator (GECI) lox mouse, will generate mice in whom most glutamatergic preBotC neurons will express the GECI. If your collaborator has access to a 2-photon electrophysiology rig (Jeff Smith has one, Chris del Negro has one), you can look for these endogenous bursters under synaptic blockade in a way that will generate robust positive or negative results, and will settle this issue (please publish regardless of outcome). In my optical recordings, under synaptic blockade, any neuron that remains active is really salient, and I'm restricted to widefield recording methods (I almost never see stationary rhythmicity in neurons that remain active), so with a 2-photon rig and a 600 μm slice, a relatively small number of experiments will give you a really robust result. Unlike the percolation model, which is probably pretty difficult to test experimentally, because it isn't really a model at all, models that assume the existence of a population of endogenous bursters are eminently testable using optical recording methods.

Reviewer #3 (Recommendations for the authors):

Lines 203 – 204: "In this case, the frequency of the postsynaptic ca2+ oscillation is again controlled by Kbath and the ca2+ amplitude is determined by the burstlet amplitude and PSynCa. "

Could the authors clarify which figure panel demonstrates the above statement? From the current Figures4B,C, increasing Kbath increased both frequency and amplitude. From Figure 4E-G, it is not clear what the specific contribution of PSynCa alone would be since Kbath and PSynCa are co-varied in those simulations. Also is this Figure 4 missing panel D?

Figure 6: In panel A, it seems like uOR is activated in all rhythmogenic neurons by both rhythmogenic and pattern generating neurons, whereas uOR is activated on pattern generating neurons only due to inputs from rhythmogenic neurons. This would mean that uOR is expressed throughout the preBotz abundantly in contrast with the stated references with 8-50% expression. This needs clarification. In panels B, C, what is changed from trace to trace? Is the GIRK conductance progressively increasing in B and similarly synaptic block in C? The legend does not clarify this. Could the authors also elaborate on the basis for IGIRK equation 9?

Figure 7: Can the authors comment on whether there could be a network burst if hypothetically only pattern forming neurons were stimulated?

Lines 77 – 79: "The small number of neurons required to evoke a network burst and the extended duration of the delays both differ from what would be predicted by existing computational preBötC models. "

The above is stated but not clarified why and by which models.

Lines 378 – 381: "Importantly, we find that the burstlet fraction is determined by the probability that a burstlet will trigger CICR in the pattern forming subpopulation. In the model, this probability is determined by the magnitude of postsynaptic calcium transients as well as the activation dynamics of the IP3 receptor and the SERCA pump."

Need clarification of direct/indirect evidence to support this assumption.

Lines 404 – 407: "As Kbath is increased, however, increases in the membrane potential of pattern-forming neurons and EPSP magnitude are predicted to increase the magnitude of EPSPs triggered by postsynaptic calcium transients. This is exactly the effect that is captured in the model by an increase in PSynCa."

The above statements need refinement. The parameter PsynCa is not linked to Kbath in the model. Therefore, the proposition that PsynCa 'captures' two distinct processes: (1) Increase in RMP caused by increased Kbath, (2) secondary to that, an increase in EPSP magnitude does not seem right. If they are linked to K_bath in the model, then it is justified that the model indeed tested the link between K_bath changes and EPSP amplitudes. Currently this is not the case.

Lines 431 – 438: "For example, Mironov (2008) showed that the transmission of calcium waves that travel from the dendrites to the soma is blocked by local application of thapsigargin, a SERCA pump inhibitor. In a separate study, however, block of the SERCA pump by bath application of thapsigargin (2 – 20 uM) or cyclopiazonic acid (CPA) (30 – 50 uM) did not significantly affect the amplitude or frequency of hypoglossal motor output in in vitro slice preparations containing the preBötC. It is possible that the negative results presented by the latter work occur due to the failure of pharmacological agents to fully penetrate the slice and diffuse across the cell membranes to reach their intracellular targets."

Here, the authors speculate that lack of an effect of THIP or CPA is due to lack of sufficient drug penetration and no reference has been cited. Without an appropriate experimental validation using suitable concentrations, drug perfusion durations and slice thickness, such a proposal seems conjectural to suggest in a purely modeling study. Lack of an effect could also be due to low sample size, small effect size among other possible differences in experimental conditions.

Lines 462 – 470: Not entirely certain what the authors are trying to compare here with exact values of Kbath across model and experiments. This seems irrelevant as the model does not have all the biological attributes and experimental conditions. It would instead be reasonable to discuss whether there were qualitative differences in the model behavior compared to experiments in the range of Kbath values which represent concentrations similar to those used in experiments.
