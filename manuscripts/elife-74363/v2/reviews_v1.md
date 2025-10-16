# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74363.sa0](https://doi.org/10.7554/eLife.74363.sa0)

Morozova et al., describe potential mechanisms contributing to the flexibility of burst patterns and dynamic responses to perturbations within an isolated reciprocally inhibitory circuit derived from the stomatogastric ganglion of the crab. The authors use the dynamic clamp approach to study the interactions between pharmacologically isolated, intrinsically silent gastric mill neurons. The authors demonstrate that the mechanisms of oscillation of the half-center networks are not fixed and shift to favor a release or escape mechanism depending on the synaptic threshold, IH conductance, and synaptic conductance. They also show that the different mechanisms of oscillation are differentially sensitive to neuromodulation and temperature changes. This is a fundamentally important study because reciprocally organized networks are ubiquitous and found virtually in every organism.


---

# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74363.sa1](https://doi.org/10.7554/eLife.74363.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Reciprocally inhibitory circuits operating with distinct mechanisms are differently robust to perturbation and modulation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor and Reviewer #1. The following individuals involved in review of your submission have agreed to reveal their identity: Paul Katz (Reviewer #2); Jan Marino Ramirez (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Address concerns about the operational definition of robustness in the paper.

2. Clarify with new analyses questions about rhythm variability.

3. If conclusions are based on single or a few exemplars then either support them more fully with analyses of pooled data or scale back on the conclusions.

Reviewer #1:

This is a very careful and systematic hybrid system analysis of the mechanism underlying alternating bursting in mutually inhibitory neurons or half-center oscillators (HCOs). By clever use of dynamic clamp, the authors create HCOs between non-connected living neurons (from the crab stomatogastric ganglion) of the same type by adding artificial synapses and h-current. This hybrid system allows them to manipulate synaptic threshold as a control variable to engage different oscillatory mechanisms escape and release, which are based on a theoretical understanding of HCO operation. They also have control of synaptic and h-current conductance and dynamics (activation-deactivation) and manipulate these variables or as proxies for changes in temperature of circuit operation. Using the synaptic threshold control variable to set escape or release mode they discern difference of these manipulations on burst characteristics in escape vs release modes. In separate experiments, they also add a modulatory current (similar to a persistent Na current) in dynamic clamp and explore it effects on HCOs in escape and release modes. The end result is a thorough analysis of how oscillator mechanism in an HCO, a basic circuit building block, affects circuit responses to perturbation and modulation.

The experiments are well performed, and a deep and rich data set is generated that is appropriately analyzed. The findings are significant for all interested in oscillatory network function and its resilience to perturbation and modulation.

Concerns:

Robustness is often mentioned but is not precisely defined. Operationally robustness seems in this paper to stand for robustness to (1) activity regime change under parameter variation, (2) stability of burst characteristics with parameter variation, and (3) slow-wave amplitude, spiking strength (spike frequency), and symmetry of bursting. These are three very different things and should be clearly differentiated in the text so that when robustness is mentioned, the type of robustness is made clear. Perhaps robustness should be limited to the first, activity regime, and some other terms used for the other two.

On several occasion in the text the authors refer to irregularity in bursting of the hybrid HCOs, but this is not quantified beyond displaying exemplars that seem to have irregular bursting. Pooled data should be analyzed in the different modes and manipulations and analyzed for statistical difference in the CoV of cycle frequency (or period) and burst duration. Similarly, the authors cite changes in symmetry in bursting in exemplars but do not present pooled quantitative data in support of the claim, just visual inspection of exemplars.

In the stomatogastric networks, synaptic transmission is largely graded (based on release mediated by the slow wave of oscillation) and not so much spike-mediated, so it is reasonable that synaptic threshold should be a control variable in this system. Moreover, spikes, recorded in the cell bodies are not reflective of their amplitude at the SIZ. In other system transmission can be largely mediated by spikes. At the beginning of the paper (Figure 1), it is clear that release mode in their hybrid HCOs depends on spike-mediated transmission because synaptic threshold is above the slow-wave depolarization, thus spike frequency is a key feature determining the mechanism of oscillation. However, in escape mode the transmission is purely graded because synaptic threshold is so low that transmission is saturated by the slow-wave depolarization and spikes contribute little if anything, thus spike frequency is immaterial to the mechanism of oscillation. This situation should be addressed at the beginning of the paper in reference to Figure 1. How this spike-mediated vs. graded balance plays out in the mixed mechanism modes remains to be explored.

In Figure 1C, the authors show convincingly that there is a vast landscape where their hybrid HCO operate in a mixed mechanistic mode somewhere between escape and release corresponding to synaptic thresholds in the middle range. This mixed mode is addressed only with a single exemplar in Figure 8B as a case for how modulation affects mixed mode circuits. The Discussion should reflect plainly that this mixed mode is likely common in biological circuits and may go hand-in-hand with significant reliance on spike-mediated transmission.

The authors state "The modulatory current (IMI) restores oscillations in release circuits but has little effect in escape circuits." but this is supported by a single exemplar (Figure 8E) and no pooled data is presented.

1. Lines 130-131: make clear that h-current must also be added by dynamic clamp.

2. Line 158: the definition of VM-bar is not clear. I was confused by this in Figure 1B. My expectation from Methods is that with proper filtering at 1Hz that spikes would be eliminated (Does your filter integrate? This would seem problematic for calculating ERQ. What is the filter? Simple RC?) and then the smoothing would leave a slow wave that peaks near the dashed red line, so VM-bar would be slightly below the dashed red line. Please indicate VM-bar on each exemplar trace of Figure 1A and rationalize VM-bar determination explicitly.

3. Line 203: In the exemplar records shown in Figure 2 A, GM2 has a very low spike frequency in the escape mode and higher in mixed.

4. As synaptic threshold becomes more positive the importance of spike-mediated transmission appears to become more important. Are all releases in this system using purely spike mediate transmission as suggested by Figure 2 A and C?

5. Lines 220-223: Can you state explicitly what criteria you applied to determine to designate escape vs. release (ERQ?) for analysis, and especially how synaptic threshold varied among the HCOs within each group? This is especially important given this last sentence of this paragraph.

6. Lines 228-231: Can you provide data in support of these conclusions? Quantify h-current at the point of transition, for example? If such data are not available, these conclusions could be scaled back a bit.

7. Lines 236-238: If I understand Methods correctly, your definition of duty cycle is not appropriate for most or all of the designated escape circuits. In escape and near escape, synaptic transmission occurs while the cell still depolarized above synaptic threshold but is not spiking. Better to define duty cycle as time above threshold/cycle period; you are discussing the rhythm generating function here not the motor outflow.

8. Line 236: Figure 4A and B?

9. Lines 263-271: I am very confused by this paragraph. Remind the reader of the ERQ criteria for escape and release. (a) Are the extremes i and v escape and release both mixed?? "The ERQ threshold for escape is −0.038 {plus minus} 0.008, while the ERQ threshold for release is 0.105 {plus minus} 0.012." It is hard to tell from the color code of Figure 2A whether these criteria are ever met. (b) How is the mechanism changing? Can you state that explicitly? I interpret that the extremes of your HCO hybrid system as being escape and release with reality sitting in the middle, which is mixed. Are you postulating distinct mixed mechanisms? Can you define them? (c) I think that you are saying that the balance between release promoting ionic currents and escape promoting ionic currents are changing but you do not define these currents. In the mixed regime, one should speak about ionic currents if one is to speak of mechanism.

10. Lines 289-291: What about systems that rely on spike-mediated transmission?

11. Line 294: In what sense is bursting less regular? Can you define the criteria and present numerical data? Maybe Coefficient of Variation of the cycle period or frequency?

12. Lines 296-301: Can you provide evidence for these conclusions by analyzing each cell separately for ERQ? Are you saying that in mixed mode that one cell is escaping, and one is being released? What exactly are you thinking here?

13. Line 312: STAR methods?

14: Lines 320-323: Asymmetry in activity does not require asymmetry in excitability. You could have bistability or a (possibly even artifactual) difference in baseline membrane potential despite your attempts to equalize them with injected current. This statement requires more evidence to be firm.

15. Lines 327-341: What values were chosen for gh and gSyn in each case (escape vs release)? Are these the same throughout all experiments???? How about Vth, is this the same across experiments for each case?

16. Line 344: Can you quantify this irregularity as CoV? I see an exemplar that seems more variable but also a lot faster (higher frequency). Are there pooled data to support claims on cycle frequency and its variability?

17. Lines 346-348: Is this surprising? The exemplar is dependent solely on spike-mediated transmission and so is susceptible to changes in spiking.

18. Lines 385-388: This seems an understatement. This system at elevated Vth is operating in spike-mediated transmission mode and so spikes and spike frequency are all important.

19. Lines 394-395: I don't see this in the data. I see a distinct crossover at around 4 nA – 15Hz. Can you quantify slopes? Is there pooled data to support this conclusion?

20. Lines 402-411: You are here recognizing the distinct difference between HCOs that operate with graded vs spike-mediated inhibition. This should be thoroughly aired in relation to Figure 1; don't wait till here.

21. Lines 411-413: Can you support this conclusion with data?

22. Lines 418-421: There are real difference between a slow wave HCO intrinsic excitability and a spiking HCO. For one a weakly regenerative current like a INaP can lead to weak rebound, but robust spiking supporting an HCO based on spikes. I suspect in the case Figure 5B1 that you either have a very long lingering h-current or a LT relatively slowly inactivating Ca current that is fully inactivated when Vth is more positive and inhibition weaker. You do not measure rebound in the GM neurons.

23. Figure 6: I find the logic of this figure unclear. The purpose is to study the effect of temperature on the hybrid HCOs in different oscillation modes. So, you present HCOs with the added h and synaptic conductances at standard temperature for a comparison group (Panel A), but then Panel B is simply to illustrate changes associated with changes in h and synaptic conductances at a different temperature, and finally in Panel C you explore a simulated change in temperature. I understand why you have Panel B included (to parse mechanism) but shouldn't the order be ACB?

24. Lines 451-453: Do you have data to support this conclusion?

25. Line 456: '…temperature-independent synapse…' This is getting confusing. It is temperature insensitive h-current and synapses; please make it clear.

26. Line 460: '…release or escape…'

27. Lines 479-480: Here it would be good to remind the reader that the deactivation rate is as important as the activation rate and that in fact they are two sides of the same coin. From Methods I think you just changed Tau0s (2X or 1.5X) (τH0 2000 or 3000 msec, τsyn 50 or 100 msec) with temperature so both activation and deactivation are affected. I suggest that you plot the Taus of the synapses and the h-current on the plots of Figure 1B. You do provide the equations in Methods, but I think a visualization would help.

28. Lines 486-489: Any data to support these conclusions? Change activations rates without affecting deactivation?

29. Lines 491-492: Can you provide more evidence in support here? I would like to know what is causing the rebound in the GM neurons before I can fully accept this conclusion. If the rebound is due to lingering h, maybe emphasize the deactivation.

30. Lines 518-521: Please put the numbers here in the text, at least for the Q10 g and k case. The Table is pretty tough to isolate on.

31. Lines 521-525, Figure S2: This exemplar in Figure S2 is not convincingly escape at 10 C. Pure escape should transition to the depolarized state when threshold is reached. This is a good place for me to comment on the ERQ criterion for designating escape and release. I appreciate the need for an automatable algorithm to designate escape vs. release but I have two caveats. (1) Classically escape is designated by transition when the inhibited cell reaches synaptic threshold (or maybe in spike-mediated transmission spiking threshold) and release is designated by transition when the depolarized cell crosses the synaptic threshold (or stops spiking). The case in Figure S2 clearly violates this classical designation. (2) ERQ is determined by averaging across the two neurons in the HCO, this hides asymmetries and allows for the two cells to have different mechanism, e.g., one escape and one mixed. ERQs must be calculated independently for the two neurons if you wish to reveal asymmetries.

32. Lines 547-550: Only one prep is illustrated in Figure 8C. Is the CoV of bursting in mixed mode different across pooled data to support this statement?

33. Line 590: '…vastly…'

34. Lines 593-597: Only one prep is illustrated in Figure 8E. Are there pooled data that can support this conclusion?

35. Lines 650-653: Because asymmetry is not directly assessed in this paper this conclusion should be scaled back.

36. Lines 653-656: Only one prep is assessed in mixed mode, so this statement should be scaled back.

37. Lines 687-689: Please be careful here and designate modes precisely and state exactly what you mean by stable cycle frequency. Does this mean regularity of bursting or period constancy? Ditto for living preparations with intact networks. Line 693: does temperature compensation in intact STG networks involve a constant period of just constant phase?

38. Lines 626-628: Are there modeling studies involving more realistic neurons specifically ones that spike and use spike-mediated transmission.

Reviewer #2:

This manuscript provides a very detailed and thorough examination of an important issue in neural circuit research, namely how the mechanisms underlying neural activity relate to robustness in the face of perturbations. It examines the simplest neural circuit possible, one involving just two neurons that reciprocally inhibit each other, which is capable of producing rhythmic alternating activity. The research shows that there is a continuum of mechanisms based on synaptic and membrane properties of the two neurons that can generate a robust output. At one end of the continuum, each neuron escapes from the inhibition of the other. At the other end, each neuron releases the other from inhibition. In the middle, both mechanisms contribute to generation of rhythmic activity. The effects that perturbations such as temperature and neuromodulators have on the circuit depend upon where the mechanism of oscillation lies along this continuum.

This paper has several important strengths:

It uses dynamic clamp technique to artificially couple two real neurons and provide them with a membrane conductance that they don't normally have. This is a powerful technique that merges experimental and theoretical neuroscience because the researchers are able to systematically alter parameter values such as synaptic strength and ionic conductance that are not feasible to modify biologically. Yet they are also monitoring the activity of real neurons.

The manuscript thoroughly represents the results and convincingly demonstrates how release and escape mechanisms are differentially affected by perturbations. The method of data visualization is very effect at summarizing complex results.

An important conclusion drawn from the results is that half-center oscillators using a release mechanism are more robust to variations in synaptic and membrane conductance.

Another important conclusion is that the same circuit can produce a similar output using different mechanisms and that it is not possible to know which mechanism is used without looking at the effect of perturbation.

I would encourage the authors to not start the abstract with a question, but rather use a standard topic sentence that gets right to the problem.

The introduction could be firmed up more. For example, the sentence "Lateral inhibition is important in many sensory systems, and reciprocal inhibition between individual neurons or groups of neurons is the 'building block' of many half-center oscillators that generate antiphase and multiphase activity patterns." Is a run-on referring to lateral inhibition in sensory systems and then going into detail about reciprocal inhibition in HCOs. The concluding sentence of the introductory paragraph does not follow from the content of the paragraph.

Figure 3A. If I understand this correctly, 10 models were made with each of the 49 combinations of gH and gSyn. The percentages then are going to limited to 0,10,20,30,40…100%. To make that clear, change the continuous gray scale "%oscillators" to the 10 discrete gray values (as was done in Figure S1A). That will provide the reader with more information about the values. Same with Figure 3F.

Figure 3C, the red boxes are nearly invisible and I imagine that Figure 3D is not color-blind friendly.

Figure S1A, I found the colors difficult to distinguish. The trends did not pop out at me.

Figure 7 refers to 'cases' that are also in Figure 6, but not referred to as cases. It took me a while to recognize that they were the same. It would be helpful to label case 1, case 2, and case 3 in Figure 6 A1, B1, C1 and in Figure 7 A-D in the Figure It would also help to refer the cases in the text for consistency such as line 438, Case 2 and line 475 Case 3.

Also, recognizing color equivalence in Figure 7 A-F lines and E-H boxes is really hard. I think it's because the box plots have a contrast-enhancing black border. I'm starting to think that I may be color-impaired.

Line 546-550: "I-MI made oscillations less stable and irregular for circuits operating with a mixture of mechanisms." Stating "This is obvious…" is not an explanation; although it may be obvious to the authors, it needs to be explained to the readers.

Regarding the 2nd point, "an increase in the standard deviation of the cycle frequency", I don't see documentation of this; the error bars in Figure 8C are larger at the release end of the graph than in the middle.

Reviewer #3:

The authors demonstrate that the mechanisms of switching between components of the reciprocally organized half-center network are not fixed and may shift to favor a release or escape mechanism depending on factors such as the synaptic threshold, Ih conductance, and synaptic conductance. This is a fundamentally important study because reciprocally organized networks are ubiquitous and found virtually in every organism.

This study leads to the important conclusion that a given rhythmic output alone does not reveal the underlying rhythmogenic mechanisms. A rhythmic output is not based on one "fixed" mechanism, but on the interplay between different rhythmogenic modes. Moreover, because of this interplay it is impossible to predict how this network will respond to perturbations.

The study is an important reminder that even a small two neuron network with a well defined, extremely simple "connectome" is strikingly flexible and complex: an important lessons for those aspiring to obtain complete connectomes in mammals in the hope to reveal the secrets of the brain.

The authors use the dynamic clamp approach to study the interactions between pharmacologically isolated, intrinsically silent gastric mill neurons, an approach pioneered by Andrew Sharp in the 1990's. Because of individual differences in the intrinsic properties from neuron to neuron, which is very characteristic for numerous networks, the authors introduce the escape to release quotient (ERQ) to be able to pool the responses of different neurons and demonstrate that changing the synaptic threshold can transform the network in a sigmoid manner from one dependent on an escape to one relying on the release mechanisms. Additionally, the authors demonstrate a network favoring a release mediated mechanism of switching responds differently to perturbation and modulation in H-current and synaptic conductances, compared to a network favoring an escape mechanism, despite similar patterns at rest. This is a fascinating finding, since a given rhythmic output alone does not reveal whether it is favoring one or the other switching mechanism and therefore also does not reveal how it will respond to perturbation. The differences can be striking: increasing an Ih current can lead to an increase or decrease in frequency, which could explain why blockade of the Ih current may yield inconsistent results. Similarly, bursting can be more or less regular dependent on the synaptic threshold. Overall, the manuscript is very comprehensive, and elegantly mechanistic. Because the dynamic clamp approach allows the investigators to carefully dissect the contributions of each of these cellular parameters it serves as a fundamental framework for understanding rhythmogenesis in general, which has always been the strength of the stomatogastric ganglion. Additionally, the difficulty in performing these elegant studies should be commended. It is striking how flexible and complex a simple two-neuron network can be: take that for those believing that a complete connectome will reveal the secrets of the brain. But it is also an important reminder that it is impossible to explain network functions based on characterizing firing patterns alone.
