# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79541.sa0](https://doi.org/10.7554/eLife.79541.sa0)

The authors show how high-dimensional neural signals can be reduced to low-dimensional models with variables that can be directly linked to behavior. The reduced model can account for long time scales of persistent activity that arise from transitions between metastable model states. The authors further show that the rate of these transitions is modulated by water temperature according to the classic Arrhenius law, although the results for different temperatures could not yet be unified into a single description based on real external temperature.


---

# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79541.sa1](https://doi.org/10.7554/eLife.79541.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Emergence of time persistence in a data-driven neural network model" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) Please follow suggestions from reviewing on cross-validating model fitting

(2) Fitting the model across temperature values and discussing the relationship between the physical and model temperatures

(3) Analysis of temporal alignments between changes in the swim direction and the onset of sign change in the difference between the mean population activities of left and right hemispheres

Reviewer #1 (Recommendations for the authors):

1. Temporal alignment between neural activity and fish behavior.

Line 101: "Impact of the bath temperature on the orientational persistence in freely swimming larvae".

The authors compare the statistics of their sign(m_L-m_R) to the statistics of swim bouts in a previous paper and show that the two variables are highly correlated. However, this is just an indirect observation since they didn't establish whether changes flips in sign(m_L-m_R) are temporally aligned to changes in the fish swimming direction when analyzed simultaneously. I believe this is an important missing link in the manuscript and I suggest that the authors show that this relationship holds at least in one example – although it'd be ideal to show this at different temperature, it is sufficient to show it for one particular temperature. The dataset in Figure 4 is appropriate for this extra analysis, which should be performed both during spontaneous and stimulated epochs.

Related to this issue: what is the probability of having a change in swim direction, without a flip of sign(m_L-m_R)? And vice versa, what is the probability of having a flip of sign(m_L-m_R) without a change in swim direction?

Also related, what is the distribution of intervals between changes in the swim bout directions? If these behavioral observable is faster than the temporal resolution of the calcium indicator dynamics, this might introduce some statistical biases in the analysis.

2. Cross-validation

Line 143: "Inference of an Ising model from functional recordings of the ARTR." The authors fit an Ising model to the data showing that it captures various observables in the data. However, the model is not cross-validated. The authors should use standard cross-validation procedures to establish the goodness of fit of the various observables on held-out data. In all plots in Figure 2C-F and Appendix 2 Figure 2B-E results should be replaced with a comparison with held-out data not used to fit the model.

Moreover, what is the null hypothesis here? The authors should compare the held-out performance of their model to shuffled models trained on surrogate datasets obtained eg by destroying pairwise correlations.

3. Definition of temperature in the model

It is not explained at all how the water temperature appears in the model. Is it a missing 1/T factor in Equation (1)? This is a central issue the authors should be very clear about. What's a bit confusing is that the authors define "inverse temperature" as the effective size K, but there's no mention of the actual water temperature at all.

Line 234-236: In the Langevin formalism, the diffusion constant D usually appears in the noise autocorrelation function = 2*D*δ(t-t'). This is usually taken to be equal to the temperature (inverse β) in the partition function (which is missing from its definition!). How are the statistical mechanical temperature and the actual water temperature entering here? This is very confusing, I strongly urge the authors to clarify this point.

Reviewer #2 (Recommendations for the authors):

This is a beautiful study that combines physics with biology, treating a biological network as an inorganic system, by minimizing its free energy and maximizing entropy. It answers a lot of questions and hints at a valuable wider applicability of this approach. At the same time I am somewhat confused about the approach the authors have taken to fitting the models, explained below, and it would be good to have a conversation about that and possibly adjust some details of the approach, or to clarify. With appropriate revisions or clarifications this work would be a strong candidate for the journal.

Comments, questions, suggestions, and concerns:

1. I am puzzled why the authors fit the Ising model (and the mean field model) separately for every temperature. There are ways to include temperature directly into the model – for example, Ising models have an intrinsic dependence on (an abstracted) temperature, that is not included in equation 1 (line 157), where in typical formulations P(σ) = exp(-β*H(σ)) / Z, where β = 1/(k_b * T), so that the couplings J and biases h get naturally scaled by the temperature T, and the distribution over configurations σ becomes flatter with higher T. Of course the correspondence between the real ARTR and the real temperature, and the Ising model and the model temperature, should not be taken too literally. But qualitatively there may be an analogous effect, namely a reduction of effective couplings and a reduction in biases with increasing T, and a resulting flattening of the distribution over configurations (σ), producing a more "disordered" network with less coherence and shorter time constants. An alternative would be to treat temperature, or a function of temperature, as an input to the model, for example through the modified bias term h in the energy hamiltonian. Either of these seems more systematic than re-estimating the couplings and biases for every temperature, can the authors explain why they did it that way?

(I could not spot a systematic dependence on T of the parameters in Appendix 2 table 2 but as the authors explain, fitting the couplings and the biases can be hard to disentangle, however their comment "This owes to a progressive change in the values of both the couplings and the biases" suggests a systematic change, which I could not spot. However it could still work to incorporate a 1/T dependence explicitly.)

2. Then the traces in Figure 2A-D seem consistent with a loss of correlation amongst individual neurons in ARTR clusters, because the average becomes smaller (suggesting less coherence), but it is unclear because the Y units are "a.u.". We would need to know that the Y axis units in A is the same as that in B, and that the Y axis in C is the same as in D. Since the Y axes are labeled "a.u." so I am not sure whether this is the case. There is no reason not to provide true units (∆F/F for A,B, and average value for C,D) so that this comparison is possible.

3. Assuming my understanding of the above is correct, then, if the temperature dependence is incorporated in the model through for example the 1/T dependence or through the biases, it should be possible to fit the model at one temperature and then predict model behavior at all other temperatures. With this interpretation, the inclusion of multiple temperatures serves more as a "cross validation" of the model. I would find this a more convincing demonstration of the utility of the Ising model for network dynamics than what is currently demonstrated (i.e. more convincing than training on all temperatures and testing on all temperatures). This is analogous to the other strength of the model touted by the authors, namely that training on low-order statistics reproduces the higher-order statistics.

I realize that the temperature parameter T may not only reflect bath temperature, but also other factors like neuromodulatory inputs from the rest of the brain that depend on temperature, as the authors describe in the Discussion. Nevertheless, I think this should be attempted, even if the model T ends up scaling for example supralinearly with bath temperature, for example, T = bath-temperature + other-influences-that-are-a-function-of-T.

The same comments generalize to the mean field model. That is, I think it should be attempted to fit both the Ising and the mean field models to all temperatures and have the couplings and biases scale with 1/T (or 1/f(T) with f describing a combined dependence on bath temperature and other influences) or incorporate T into the biases as an external drive, instead of fitting the parameters separately for every temperature (of course individual fish should be fit separately). Then the held-out temperatures can serve for cross validation.

4. The way the Ising model is turned into something from which temporal dynamics can be read off is through the Monte Carlo sampler. This seems reasonable and elegant given what I understand about MC samplers and I trust it makes sense, but the paper explains the workings of the MC sampler poorly. There is a reference to some code online, but text providing the reader with a good intuition, or pseudocode, is missing. Given the importance of the MC sampler, the explanation of it, and why it can be interpreted as time evolution on long timescales, should be much more central.

5. Thus the interpretation of the Ising-ARTR correspondence seems to be first, that in both cases, less "coherence" between the units leads to longer time constants (under MC sampling in the model), and second, that increasing temperatures lead to less "coherence", thus linking temperature to time constants. If this is right, it would be useful to spell this out more clearly.

6. The Ising model is proposed to be a good model of ARTR network dynamics, and the model neurons (let's call these particles, for clarity, and call ARTR neurons, neurons) are fit to individual ARTR neurons. For readers, it would be very useful to see a graphical comparison of the dynamics of the particles, at the population level, and the dynamics of individual neurons, also at the population level. The Methods state that the mean and variance of each is fit but readers need a more personalized intuition for what the model looks like in comparison to the biological network. Although Appendix 2 Figure 1 and Appendix 2 Figures 2A(5) goes some way to depict the Ising particles and the real neurons, I think that having an elaborated population representation comparison figure in the main text would be useful, just for readers to visualize.

7. Line 165 "contralateral couplings vanish on average", also mentioned in the Discussion, seems strange because I would expect that contralateral couplings are on average negative. How does this fit in with contralateral inhibition? (As an aside, for biologists, the word vanish might be unclear and a different way of describing it might be better.) The discussion also says that the couplings are almost null but drive a subtle interplay. It seems to me that readers need to know if they are small but overall negative, or whether they can be small and overall positive; the latter would be hard to interpret but the former would be more straightforward to interpret. Why is the significance not quantified statistically?

8. The ARTR consists of excitatory and inhibitory clusters, as the authors describe, and refer to the Ising couplings, but I did not see a clear depiction or quantification of whether these couplings segregate, only a passing mention in the Discussion (lines 409-415). Can the authors depict the network connectivity accordingly, as particles with signed weights between them, and compared to their location in the brain?

9. In some ways, it is surprising that the behavior changes so much with temperature, because the field has learned from Eve Marder's group that network dynamics tend to be surprisingly robust to "crude" perturbations of the entire network. It is possible that it was difficult for evolution to compensate for the temperature dependence of ARTR, but it is also worth thinking about whether there might be an ethological purpose for the temperature dependence. Could it be useful for the animal to alternate turn direction more often when it's warm?

10. The phrasing "orientational persistence" came across as a bit of a misnomer to me, though I might be wrong – orientation typically means the angle of the animal in its environment, whereas this is about the change in angle, so orientation persistence might be interpreted by a casual reader as the fish swimming in a straight line at a fixed angle. I am not sure what else to call it though – "turn direction persistence" is probably more accurate but also clumsier. Is there a better term? If you decide to keep using "orientational persistence" it would be useful to very carefully and explicitly explain what you mean by it.

11. Cold-blooded animals have a body temperature that quickly converges to that of their surroundings (especially tiny fish). Their neural populations will likely experience a wider range of temperature fluctuation and therefore follow certain thermal dynamics laws unlike any warm-blooded animals (such that the flipping rate increases with temperature following Arrhenius law). It is important to discuss if the time persistence that emerges from the network model is a special case for cold-blooded animals experiencing different temperatures (through the 1/(kB*T) scaling of the couplings and biases), a direct thermal effect, rather than "purposeful" neural network computation (through external inputs that could be modeled by making the biases depend on T).

12. It is therefore good to discuss how applicable this free energy landscape description of a neural network is to other neural networks with persistent activities in other animal models, with different sensory inputs, in order to reach a larger audience and have wider potential applications. What types of time persistence can this interpretation address and what are its limitations?

13. Line 9: "networks" should probably be "network".

14. Figure 1 C and G: labeling the colors by their temperature in the figure would be helpful.

15. Line 246, it is Figure 3B showing the energy landscape, not 3C.
