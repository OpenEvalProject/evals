# Peer review - Round 1

Editors:
- Kenton Jon Swartz, National Institute of Neurological Disorders and Stroke, National Institutes of Health United States

Reviewers:
- Steve Jones, Case Western Reserve University United States
- Gilman Toombes, National Institute of Neurological Disorders and Strokes United States

## Review text

DOI: [10.7554/eLife.39575.029](https://doi.org/10.7554/eLife.39575.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Biophysical models reveal the relative importance of transporter proteins and impermeant anions in chloride homeostasis" for consideration by eLife. Your article has been reviewed by Kenton Swartz as Reviewing Editor and a Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Gilman Toombes (Reviewer #2); Steve Jones (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All three reviewers enjoyed reading your manuscript and praised your efforts to construct a mathematical model of cytoplasmic chloride regulation in neuronal cells with a focus on the cation-chloride cotransporters and the role of impermeant ions. There was also consensus that models like yours are essential for interpreting and understanding complex physiological experiments. However, the general consensus among the reviewers and Reviewing Editor is that the model would require considerable experimental testing to be appropriate for eLife.

Reviewer #1:

The current manuscript constructs a mathematical model of cytoplasmic chloride regulation in neuronal cells with a focus on the cation-chloride cotransporters and the role of impermeant ions. The authors give strong motivating factors for why chloride regulation is so important in electrical signaling. Personally, I find it very interesting how as central neurons mature they switch from KCC2 expression to NKCC1 expression (briefly touched on in the metanalysis figure) which then causes the cytoplasmic chloride to drop from ~20 mM to ~5 mM, and chloride channels then switch from being inhibitory rather than excitatory (with exception of medial habenular neurons and most other non-neuronal cell types in the body which do not undergo this switch). I especially like how this manuscript explores several different scenarios using the mathematical model to determine how Cl, membrane potential, cell volume, and other parameters would change under different conditions.

I personally believe that models like this one are essential for interpreting/understanding complex physiological experiments. However, I am concerned by the lack of experimental tests of the model. In Figure 3C it is shown that KCC2 expression does correlate with changes in chloride concentration, but this figure does not represent the level of correspondence that one would like to see for a quantitative model. I would expect to see fitting to time dependent traces recorded from cells in the presence of different pharmacological agents along with chloride dyes, voltage measurements, measurements of cell volume changes etc. The authors argue that there are no good chloride dyes or quantitative measures of chloride concentration, and I agree with this statement (in addition to sodium and potassium measurements); however, there are dyes out there that could be used to at least test some of these ideas in amore qualitative way, and it is possible to measure membrane potential changes (there are many graphs that suggest changes in voltage in the presence of pharmacological agents), and this would significantly strengthen the paper.

I have also become more and more interested in how we treat transporters and channels in these kinds of cell-based mathematical models. This work uses very generic fluxes for these terms, but it would be more more interesting if detailed kinetic models of the NaKATPase or the CCC transporters (if known) could be used to inform how their biophysical regulation impacts the ionic fluxes and then ultimately impacts cellular homeostasis. In many cases these details are not known for transporters because of a lack of the ability to perform detailed patch clamp on transporters, but the best, most detailed models should be used when they can be.

As it stands, I believe that this paper is ideally suited for Journal of Theoretical Biology or a similar journal – I don't even think that Biophysical Journal would be that interested in this manuscript without some connection/validation with experiment. Overall this manuscript lays out a series of predictions about how cellular homeostasis will be perturbed under different conditions, but the lack of experimental validation reduces my enthusiasm for this work.

Reviewer #2:

While it is well established that cells use active pumps and passive leak channels to regulate their membrane potential, cytosol composition and volume, it was recently proposed that the concentration and driving potential of Cl- ions might also be regulated by the impermeant ion concentration (Glykys et al., 2014). In this work, the authors use a conventional pump-leak model to examine how the Cl- concentration and driving potential are modulated by pump rates, leak conductances and impermeant anions. They conclude that while impermeant anions can modulate the intra-cellular chloride concentration, their effect on the driving potential is far smaller than the K+/Cl- cotransporter (KCC2). In addition, the authors present a meta-analysis linking KCC2 expression to [Cl-], and examine the ability of KCC2 and impermeant anions to locally modulate Cl- concentration and driving force.

The paper is clearly written and provides a thorough theoretical analysis of the controversial "impermeable anion" hypothesis (Voipio et al., 2014). However, there are several ways in which the paper could be strengthened:

1) Modelling choices: It would help to explain why particular ions (e.g. bicarbonate) and transporters (e.g. NKCC) did not need to be included model, provide experimental references for the model parameters listed in Table 1, and discuss whether the effects of the cytoskeleton on osmotic pressure (Sachs and Sivaselvan, 2015), coupled water and ion transport (Delpire and Staley, 2014), or other mechanisms could change the paper's key conclusions.

2) Mechanistic explanation: The idea that changing [A-] must impact [Cl-] and thus the Cl- driving force is simple and appealing. The authors convincingly demonstrate issues with this "impermeant anion hypothesis", but do not explicitly illustrate how the flow of K+, Na+, and water effectively decouples changes in [A-] from the Cl- driving force. To help readers, the authors could display the concentrations, potentials and net fluxes of all ions (including Na+ and water) in time-dependent simulations (e.g. Figure 1C, Figure 3A, Figure 4A,C,D, Figure 5A/5C, Figure 6A/6C). For example, in Figure 5A, the increasing impermeant anion charge lowers the membrane potential which then drives a larger inflow of K+ and Na+ than the outflow of Cl- (because gCl < gK + gNa). This clearly conflicts with the assumption of the "impermeant anion hypothesis" that [A-] + [Cl-] is constant, since most of change in A- is compensated by cations.

3) Experimental Testing: The study would be even more valuable if the authors discussed potential experimental tests of their conclusions. For example, how could one distinguish to what extent cells modulate CCCs (gKCC2) rather than the chloride leak conductance (gCl)?

Reviewer #3:

This paper presents a pump-leak model including ion conductances and transporters to explore the basis of chloride gradients in cells with KCC2 chloride-potassium transporter. The model is simple (in the most basic case, analytically solvable) yet sufficient to produce realistic ion gradients and voltages. It concludes that KCC2 plays a critical role, and impermeant ions have interesting but quite minor effects (as expected from equilibrium considerations but opposed to a controversial Science paper). This will be of interest both for those interested in how neurons produce chloride gradients (which can vary substantially physiologically), and for broader questions of maintenance of ion homeostasis.

I should admit that I am not an expert in the specific modeling methodology used in this paper, but it looks good as far as I can tell. I have no serious concerns.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Biophysical models reveal the relative importance of transporter proteins and impermeant anions in chloride homeostasis" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Aldrich (Senior Editor), Kenton Swartz (Reviewing Editor), and three reviewers.

This manuscript describes thorough mathematical modelling of the physical mechanisms controlling chloride homeostasis. Concerns raised in an earlier review have been thoroughly addressed, and the additional experiments nicely complement the authors' model. We think this is a careful and valuable study, and at this point our main concern would be the need for clearer explanations of the experimental design and controls. The following are issues the authors should address in revision.

1) Why doesn't EK change in Figure 2 panels? Is it overwhelmed by the Na/K-ATPase flux, and the transporter is set to an EK of -100 mV (Addressed in Figure 3H?)? Actually, in the caption for Figure 2B you say that EK does change:

"Increasing Na+ conductance gNa resulted in a progressive increase in steady state ECl, EK and Vm with accompanying cell swelling"

However, EK does not change. You do not show ENa, but is it also being pegged at about +40 mV for all gNa values?

2) In Figure 3D, can't you just subtract off the drug sensitive current so that it passes through zero to see the reversal potential? We had to look at this way of plotting the currents several times before we got it. Labels near the grey/black/pink curves may help too. Does this value of ~ 4 mV in Figure 3D seem small given the theory predictions in Figure 3B? Does Figure 3H belong in this figure? It isn't clear that it should be here, unless we didn't read this carefully.

3) In subsection “Altering the concentration of intracellular or extracellular impermeant anions, without changing the average charge of impermeant anions, does not affect the steady state gradient or driving force for chloride”, define average charge. It is confusing. In subsection “Changing the average charge of impermeant anions can drive substantial shifts in the reversal potential for chloride, but has negligible effects on chloride driving force”, what is the physical reason why changes to impermeant anions have different effects on Cl- than changing the average charge?

4) Data in Figure 5E, F nicely shows that this manipulation of adding the charged dextrans gives an undetectable shift in the Cl- driving force. That said in Figure 5F some of the DF changes are pretty big (negative) but is offset from others that are positive giving an average that is closer to zero. Not sure what to think about this.

5) For the impermeant anion experiment (Figure 5D-F), the authors have elegantly confirmed the addition of impermeable anions to each neuron via fluorescence microscopy. However, fluorescence microscopy can detect very low concentrations of fluorophores, and so the observation of fluorescence from a neuron might not ensure there has been a meaningful change in average anion charge. Furthermore, while the shift in Vm is certainly consistent with an increase in average anion charge, it would be nice to discuss, or better still, experimentally exclude any unintended effects of electroporation. For example, the author's model seems to predict there would be no change in Vm after adding a neutral (e.g. dextran-Texas Red) polymer, and that neurons would depolarize after adding a cationic (e.g. FITC-DEAE-Dextran) polymer.

6) For the furosemide experiments (Figure 3D-F), the authors have previously (Wright et al., 2017) described a "within cell" approach in which each neuron serves as its own control. If this study is using this same approach, it would be good to report these controls (e.g. Vm, EGABA and DF 5 or 15 minute prior to addition of furosemide) to quantify how precisely changes in voltage can be measured. These controls would be especially valuable as the measurements appear to be made in a challenging regime where the access resistance is comparable to the membrane resistance. For example, in Figure 3D, the series resistance (~ 60MOhms baseline, ~ 40 MOhms +Furosemide) is comparable to the resting membrane+leak resistance (~120 MOhms), and so the series resistance correction for EGABA (~ +9mV baseline, +6mV + Furosemide) is comparable to the driving force.
