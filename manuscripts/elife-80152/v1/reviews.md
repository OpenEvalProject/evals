# Peer review - Round 1

Editors:
- Mark CW van Rossum, https://ror.org/01ee9ar58 University of Nottingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80152.sa0](https://doi.org/10.7554/eLife.80152.sa0)

Synaptic plasticity is a ubiquitous but also highly complex phenomenon and developing a unifying description has been challenging. This study presents a realistic biophysical model of plasticity induction, with a novel read-out of CaMKII and Calcineurin. It is able to describe a wide range of experimental results and sets a new benchmark for realistic computational models.


---

# Peer review - Round 1

Editors:
- Mark CW van Rossum, https://ror.org/01ee9ar58 University of Nottingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80152.sa1](https://doi.org/10.7554/eLife.80152.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A stochastic model of hippocampal synaptic plasticity with geometrical readout of enzyme dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Mark van Rossum as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Overall, the reviewers saw substantial merit in the manuscript. Many of the revisions requested can be done without new simulations.

Essential revisions:

1) Regarding noise in the model.

a) Indicate the critical noise source in the model. Which of the various noise sources is most important?

b) The calcium-sensitive potassium (SK) channel has been modelled deterministically. Given that the same justification in terms of a small number of channels present in the small dendritic spine compartment applies to the SK channels as well as to the voltage-gated calcium channels and the AMPA and NMDA receptors, it is not clear why the authors have chosen a deterministic representation in the case of SK. The implications of these assumptions need to be investigated and discussed. It might be possible to rule out that SK noise matters from the first principles.

2) Many of the model parameters have been set to values previously estimated from synaptic physiology and biochemistry experiments, However, a significant number of important parameter values have been tuned to reproduce the plasticity experiments targeted in this study.

State which of the model parameters (eg Table 14) were considered to be free parameters adjusted to fit the LTP/LTD induction data, and which were assumed to be generic and therefore not adjusted when fitting experimental data.

Explain which of the plasticity outcomes have been reproduced because the parameters are chosen to do so. A clarification would have helped to substantiate the authors' conclusions. It could also form the basis for more predictions.

On a similar note, there is not much information given how the readout mechanism came about. How were the regions found?

How can experiments be used to more precisely define these regions?

3) Better explain the reason for the non-linear effects in Figure 4 and 5 and possible experimental predictions that follow from that.

Also, add experimental model predictions, for example, that firing variability can alter the rules of plasticity, in the sense that it is possible to add noise to cause LTP for protocols that did not otherwise induce plasticity.

4) Argue or show whether or not the detailed exocytosis model is needed (see below).

5) Discuss briefly why the multi-vesicular release is not considered in the presynaptic model.

6) Improve the writing (also see below). In particular, discuss the main hypotheses and assumptions underlying this work and clarify the main conclusions and goals of this modeling work. It is also important to tell the reader that 'geometric' does not imply a 'spatial' readout.

Reviewer #1 (Recommendations for the authors):

Regarding these points:

1. Noise. I like that the model produces realistic variability in plasticity. This is commendable. It is also interesting because the presence of noise neccessitates a more robust readout mechanism than a noise-free model.

What is the critical noise source in the model? It should be possible to determine this (I hope it is not in the readout mechanism, as that is to most unprincipled of all included noise sources).

Similarly, is the noise crucial for the model to work? Surely, as is shown the quantitative outcome of the model changes without noise, but could it have been re-adjusted? Or does the noise truly change it?

As a follow-up to the current study it might be of interest to study paired synapses as was done in Bartols and Sejnowski (eLife) or MOTTA and Helmstaedter (2019) and who quantified the correlation between them. This would be a further critical test of the model and could decide if the majority of the observed fluctuations in plasticity are due to heterogeneity or noise.

2. The readout. There is not much information given on how the readout mechanism came about. How were the regions found? How can experiments be used to more precisely define these regions? Related, what about the parameters in Table 14? It is fine if they were hand-tuned but just say so.

3. I thought the nonlinear effects in Figure 4 and 5 were pretty cool, but the reason behind them could be explained better, as that would help these predictions further in experiments.

While the paper is easy to read, I have quite a few -suggestions- for further improvement.

I thought the Introduction and Discussion were rather long. In particular, the Introduction is quite philosophical. After reading it, I was actually doubtful that the paper was going to show some novelty.

The J of Neurosc has 500 words for introduction and 1500 for Discussion. I think that works well.

On the other hand, some of the text is not explicit enough (the Methods, in particular, see below).

– It would help to replot the Tigaret data and the protocols.

– Some figures are better in the main text. I would suggest to move Figure 3S1 to the main text, as it is so crucial. Fig22 would also be good in the main text given the complexity of the dynamics; I was happy when I found it, but that was already pretty/too late.

– The coloring used in Fig3e is confusing.

– l372. 'pulse dependent amplification' Not quite sure what that means.

– Formatting in Table 1 is ambiguous, e.g. '100 positive delays' and '200 negative delays' belong to Inglebert , but this is hard to parse.

– l 758 onwards is somewhat typical for the confusion in the Methods. THe text does not mention the D→R transition, but it is in the table.

Then, the release is mentioned in l761, but then again in l764 ("In addition…").

The Methods section is full of such inconsistencies.

– Another example: l792 "Later we incorporate a higher number of.. parameters … with our.. model". That is poor English.

– Fig8 Caption "Our model also does not cover the aboslishing of release probability". Apart from poor English, it is confusing as it is unclear how this relates to the figure.

– Fig8. Why is there such a very sudden drop in the 50Hz curve? It looks odd to me given the dynamics.

– p24 Note that one also needs to specify the units of the alphas and betas. It is also somewhat in conflict with the common convention to call \tau_\infty m_\tau.

– Table4. The spine and dendrite have time constant of 1.5 s. That is very, very long. Why is this necessary?

– Table4. 10th line dendritic leak reversal should read differently.

– Equation1 uses square brackets to denote a concentration for outside Ca, but not for CaPre which is presumably also a concentration.

– Was spontaneous release included in the synapse?

Reviewer #2 (Recommendations for the authors):

The model proposed in this study is complex and multi scale combining elements from previous work and grounding the choice of many parameter values on experimental measurements and estimates. As such the tables summarising the modelling details in the Materials and methods section use different units:

1) For time – ms and s;

2) Electrical currents conductance – nS/um^2, nS and pS.

3) Concentration – μm and M.

I would suggest that the authors unify the presentation by using consistent units for all modelling components.

I have some further specific recommendation regarding the modelling description:

1) Please provide details regarding the threshold function in Equation (1).

2) Please clarify if Equation (7) has been fitted to data.

3) Please justify the calcium buffer and dye model assumptions that both bind one claim ion only. This is important as calcium indicators such as calmodulin are know to bind 4 calcium ions.

4) Could you please justify Equation (19).

Reviewer #3 (Recommendations for the authors):

1) Page 22, Equations. 1-2: Biologically, the effect of [Ca]_0 is certainly to increase the size of [ca2+] jump during an action potential. However, the size of the ca2+ jump in the model is normalized to 1, so the external [ca2+] is assumed to directly affect the dependence of release probability on [ca2+], without affecting the [ca2+] dynamics directly. This shows that the model is purely phenomenological and that the [ca2+]pre variable does not represent [ca2+] in any meaningful way. This makes it very hard to understand the model presented in Equations. 1-2, which is quite distracting, particularly since this bears a minimal impact on the main part of this work. Moreover, there are as many as 4 free parameters in the "half-activation" function h([Ca]). Including the value of cooperativity "s", the total number of parameters is equal to 5. This equals the number of data points in Figure 8e which is presumably used to calibrate the presynaptic model. The number of parameters seems very large, and the presynaptic model appears unnecessarily complicated. Even the most comprehensive, realistic biophysical models of Ca-triggered exocytosis from the calyx of Held literature do not have as many parameters. I highly suggest replacing the model with a simpler model, whose variables are biologically interpretable.

2) Given the large number of parameters in the model (with 14 Tables in the main part of the manuscript), it would be of value to clearly summarize which of the model parameters were considered to be free parameters that were adjusted to fit the LTP/LTD induction data, apart from the geometric read-out parameters, and which of the model parameters (e.g. the ionic conductances) were assumed to be generic and therefore not adjusted when fitting experimental data.

3) I suggest explaining in one sentence why the possibility of multi-vesicular release is not considered in the presynaptic model.

4) Throughout the manuscript, the verbs "predicted", "found", "hypothesized" are used very loosely when discussing the behavior of the model and its elements, rather than in describing experimentally verifiable predictions. Moreover, when used in the past tense, verbs "predicted" and "found" is suggestive of predictions that have been experimentally verified. This makes the manuscript hard to read since in some places it is hard to distinguish statements about model behavior from statements about past experimental results or verifiable predictions. Concrete comments related to this confusing phrasing follow below.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A stochastic model of hippocampal synaptic plasticity with geometrical readout of enzyme dynamics" for further consideration by eLife. Your revised article has been evaluated by John Huguenard (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors have addressed all my issues.

Regarding the contribution of the various noises, it would be nice to have the figure from the reply letter in the paper.

(Of course, it would have been a bit cleaner to switch the noises ON one by one, but this figure is already informative).

Reviewer #2 (Recommendations for the authors):

I do appreciate the amount of work done by the authors in addressing reviews comments and suggestions. The manuscript has been improved and most of my comments have been addressed satisfactorily except for the following points:

1) Regarding SK deterministic modelling and justification – it is simply not true that:

(1.1) There is "a lack of single-channel recordings of SK channels", please see

Hirschberg, B., Maylie, J., Adelman, J., and Marrion, N. (1998). Gating of recombinant small-conductance Ca-activated K+ channels by calcium. The Journal of General Physiology, 111(4), 565.

Hirschberg, B., Maylie, J., Adelman, J., and Marrion, N. (1999). Gating properties of single SK channels in hippocampal CA1 pyramidal neurons. Biophysical Journal, 77(4), 1905-1913.

(1.2) There is "a lack of published stochastic models of SK channel", please see

Stanley, D.A., Bardakjian, B.L., Spano, M.L. et al. Stochastic amplification of calcium-activated potassium currents in ca2+ microdomains. J Comput Neurosci 31, 647-666 (2011). https://doi.org/10.1007/s10827-011-0328-x

(available at https://link.springer.com/article/10.1007/s10827-011-0328-x#Equ6)

The above needs to be addressed.

2) The units for the various model parameters are still inconsistent, eg. Table 6. uses M for concentration and s for time while Table 7. – μm for concentration and ms for time. There are other instances along the lines of the above in the rest of the tables presenting model parameters throughout the manuscript.

I do know this is a matter of simple scaling but the parameter units used throughout should be consistent to avoid reproducibility issues that could be faced by other researchers and especially early career researchers studying this work in the future.

Reviewer #3 (Recommendations for the authors):

The authors have made a significant update to their manuscript in order to address the Reviewers' comments, adding a couple more simulation results to explain different features of the model. In general, I find this update sufficiently complete.

The only point I am still not fully satisfied with is the model describing the dependence of vesicle release probability on extracellular [ca2+] (Equations. 1-2, p. 23), retained from the original version of the manuscript since it appears both cumbersome and unphysiological. However, I completely agree with the Authors that correcting this would not affect the main conclusions while requiring additional but unnecessary simulations.

Therefore, with respect to the latter, I would be fully satisfied if the Authors added a single sentence on page 23, reiterating their response to this point, namely: (1) the presynaptic model for p_rel is purely phenomenological, (2) in principle, the [Ca] jump parameter δ_Ca should depend on [Ca]_0, but (3) replacing the model with a more physiological model would not affect the results, since the measured dependence of release probability on [Ca]_0 is already satisfied by this phenomenological model.
