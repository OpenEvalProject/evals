# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71263.sa0](https://doi.org/10.7554/eLife.71263.sa0)

Many brain circuits, particularly those found in mammalian sensory cortices, need to respond rapidly to stimuli while at the same time avoiding pathological, runaway excitation. Over several years, many theoretical studies have attempted to explain how cortical circuits achieve these goals through interactions between inhibitory and excitatory cells. This study adds to this literature by showing how synaptic short-term depression can stabilise strong positive feedback in a circuit under a variety of plausible scenarios, allowing strong, rapid and stimulus-specific responses.


---

# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71263.sa1](https://doi.org/10.7554/eLife.71263.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Nonlinear transient amplification in recurrent neural networks with short-term plasticity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The findings in this work need to be better contextualised with existing literature. Some of the claims and results are presaged in other work and the reviewers agreed that the manuscript would benefit from better acknowledgement and discussion of prior work – see reviewer comments for details.

2) There are concerns that the behaviour of the model violates experimental observations (Reviewer 1, comment 1). The authors should address this concern, with additional results or sound arguments that reconcile these observations with the model.

3) Greater depth in the intuition and analysis of the stabilisation mechanism in this network is needed to justify all of the conclusions (Reviewer 1, comments 3-4; Reviewer 2, comments 4-6). This will also elevate the contribution of the manuscript and allow new findings to be better appreciated in the context of previous work.

4) The reviewers provide detailed comments below for improving the clarity and depth of the presentation. The authors should consider and respond to these suggestions.

Reviewer #1 (Recommendations for the authors):

– Line 51. Results from [Bolding and Franks, Science 2018] have been explained in [Stern et al., eLife 2018], without the need of adaptation. This work should be cited here, as it provides an explanation of transient response that is alternative to the mechanism proposed by the authors.

– Line 55. Isn't coupling strength, rather than inhibition, the key factor that linearizes network responses (e.g. see [van Vreeswijk and Sompolinsky, Neural computation 1998]).

– Above line 101. I do not understand why strong E-E connectivity is consistent only with detJ<0. Strong E-E connectivity typically also requires strong E-I and I-E connectivity [Tsodyks et al., J neuroscience 1997]. The assumption of detJ<0 seems important for the behavior of the characteristic function F(z). How are the results of the paper modified in the case in which det J>0?

– Line 124-126. I am confused about the conclusion of this section. Results discussed in Pages 5 and 6 are relative to the stability of the network as a function of input strength; why is this relevant for the nonlinear amplification of inputs? Nonlinear amplification of inputs is a general property of the SSN, which emerges also for parameters that lead to stable dynamics [Ahmadian et al., Neural computation 2013]. The authors should also explain why they select parameters that lead to unstable responses for large inputs. On a related note, the fact that the supralinear input-output function leads to activity dependent coupling and, for certain parameters, to unstable dynamics has been shown in [Ahmadian et al., Neural computation 2013]; the authors should acknowledge this fact.

– Line 188. There are many more papers related to ISN in cortex to be cited; see [Sadeh and Clopath, Nat Rev Neurosci 2021] for a summary.

– Line 273-274. It would be useful to include citations of experiments supporting this claim.

– Line 407-409. What is the relation of this work with network criticality?

– The stability of a system with excitatory-inhibitory neurons and STD depends on the eigenvalues of a three dimensional matrix, why does the condition described after Equation (32) do not include the component given by the dynamics of x?

Reviewer #2 (Recommendations for the authors):

First a note about the model of Loebel et al.,: note that while single neurons in their models have a ReLU nonlinearity, they receive different external baseline inputs, and therefore the population has an effective input-output nonlinearity that is convex and supralinear as in the current manuscript.

Specific/detailed comments:

1 – In the abstract, intro and discussion it is claimed that nonnormal connectivity is in clash with symmetric connectivity the E-subnetwork (and thus with the Hebbian learning/doctrine). But non-normal transient amplification happens in E-I networks in which the E-E part of connectivity matrix is indeed symmetric, while the full matrix is necessarily asymmetric and nonnormal (due to Dale's law). So the symmetry of the E-E connectivity (the part that is affected by Hebbian plasticity in most models) is in fact consistent with non-normal TA.

2 – Similarly in lines 56-65 of Intro (and 438-454 of discussion) it is claimed that balanced amplification (due to feedback inhibition and recurrent excitation) cannot generate strong TA, because "several ensembles need to be chained together into a hidden feedforward structure" which the authors say is "at odds with the often observed symmetric excitatory connectivity". But again symmetric E-E connectivity is consistent with nonnormality of the full (E-I) connectivity matrix, and moreover the chains are hidden between patterns, and not anatomical between neuronal ensembles. Also long hidden chains are not necessary, and when recurrent E and I connections are strong, short chains (e.g. in the SSN model) can also yield strong enough TA to be consistent with those observed in sensory cortex – though probably not as strong as in NTA. This parts should thus be more accurately written and if the claim is maintained a more thorough comparison (e.g. in a supplementary figure) with a recurrent network with neural nonlinearity (e.g. the supralinear powerlaw as in the current model) but without STP (but possibly with different connectivity so that the instability in Figure 1 does not happen) should be provided.

3 – Given that property C is a main selling point, they should characterize it better. The only result plot about this is currently Figure 1F, in which activity actually diverges post-stimulus. The nonlinear threshold (for stimulus strength) should be quantified and shown in some plot (e.g. to be added to Figure 2) for the case in which STP re-stabilizes activity. In particular the dependence of NTA (e.g. as measured by the ratio of transient peak to steady-state response) on parameters such as stimulus strength (c.f. Figure 4B of Loebel and Tsodyks 2002) or JEE, can be characterised/plotted.

4 – The effect of co-tuning of E-I (feature G) is characterised in abstract and the corresponding sub-section (its title on p. 11 and Figure 3 title) as broadening the parameter regime of NTA. But Figure 3 in fact shows that NTA happens even in the bistable case and with global inhibition. So a more accurate characterization his that E/I co-tuning broadens the parameter regime in which activity is unistable and non-persistent (which is suitable for sensory processing), without adversely affecting NTA. Also given that NTA is weaker -though still strong- with co-tuned inhibition, perhaps the strength of NTA can be quantatively compared between the two cases of co-tuned vs global inhibition.

5 – In the parts where intuitive explanation of re-stabilization (or lack thereof) due to SFA or STP are given on pp. 7-8, I would first of all provide Equations. 20-26 right there, or at least refer to them. More importantly when referring to F(z) they should mention that they are employing a fast-slow approximation using the separation of timescales between fast neural activity and adaptation variables (a in SFA, x in STD, etc) are therefore fixing the slow variables to their value at the previous/baseline fixed point. At least I believe this is what they are doing and showing in Figure 2D, but again I'm suggesting they should write this more clearly. In particular, it seems to me that while Equation 30 (with x assumed to be fixed at its value at the preceding fixed point) is consistent with the above interpretation (which I believe is the right thing to do), Equation 28 is not, as it is obtained by setting a equal to its value at its fixed point corresponding to the dynamical value of rE, and this is the right thing to do if "a" was a fast variable, not a slow one (as it presumably is). So, I believe, the correct F(z) for the SFA model should be rederived by assuming treating "a" in equation 20 as a constant independent of rE (rather solving the steady state from 21 and plugging it in Equation 20).

6 – Switching to ISN with stimulus from a non-ISN baseline is presumably parameter dependent, and this dependence should be characterized better (at least give examples of networks in which this is not the case, in a supplementary figure, and correspondingly weaken the absolute statement in lines 192-194 so that it says this transition "can" happen, which would avoid implying that this is necessarily the case, assuming it's not). Also in the ISN index (Equation 13) shouldn't JEE be multiplied by x (depression variable) at the fixed point?

7 – I found the part about pattern separation (p. 14) not clearly written and motivated. In fact I think the term "pattern separation" should be replaced with "stimulus selectivity". Pattern separation is the appropriate term when a networks output patterns are more separable than the patterns at the input-level. However, in the current case in which the external input is given only to E1 (only to one of the two E populations), the input is fully separable, so the network is potentially only capable of reducing separation. At any rate the pattern separation would be meaningful if they had compared separation at input-level (distance from decision boundary in gE1 – gE2 plane) with separation at output-level (distance from decision boundary in rE1 – rE2 plane). I think what is currently shown and charcterized is stimulus selectivity and the result is that transient onset responses are more selective than fixed point responses. So this section (and corresponding parts in intro/discussion) should be rewritten to convey this.

7a – On the other hand, this finding (stronger selectivity at onset, vs steady-state or sustained response) is presented as a desired outcome. This may be so, but it seems inconsistent with empirical findings on orientation selectivity in (mouse) visual cortex in which orientation selectivity is much stronger for sustained responses compared to onset transients. This should be mentioned (e.g. in lines 290, 326, and 418-420).

7b – The distance to decision boundary used to characterize "pattern separation" is not clearly described in lines 280-282. The description in the Methods section was also somewhat ambiguous, but giving a formula there would solve this issue. What I understood is that the measure is basically rE1 – rE2 where rE1 and rE2 are population mean activities of the E neurons in ensembles 1 and 2. If so, why not use the normalized measure (rE1 – rE2)/(rE1 + rE2)?

8 – The property B is depicted in various places (e.g. line 410) by saying NTA requires or relies on symmetric E-E connections. While NTA clearly relies on the destabilizing effect of recurrent EE connections, it is not clear that the symmetry (at least exact symmetry) of these connections is necessary. Indeed their LIF spiking net has random connectivity, so the EE part of connectivity at the level of single neurons in that network is actually not symmetric. These sentences could thus be more accurately written to clarify this point.

9 – In the current study, external stimulus was only given to excitatory neurons, with authors saying the study of feedforward input to inhibition is beyond the scope of this work, yet they also say (lines 429-432) that "we are confident that our main findings remain unaffected in the presence of substantial feedforward inhibition", and cite supplementary figure 1, which however was for the case without STP. I think it would be easy to provide a supplementary figure characterizing NTA in a network with STP in which gI is nonzero for stimulus (e.g. gI = gE).
