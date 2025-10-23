# Peer review - Round 1

Editors:
- Marlene Bartos, University of Freiburg , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27756.019](https://doi.org/10.7554/eLife.27756.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Sequential neuromodulation of Hebbian plasticity offers mechanism for effective reward-based navigation" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hitoshi Morikawa (Reviewer #1); Guoqiang Bi (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This work is a follow-up of the authors' previous work on the modulation of spike time dependent plasticity by dopamine. The authors found that the neuromodulator, acetylcholine, facilitates synaptic depression when applied prior to pairing stimulation apparently through muscarinic receptor activation. This depression can be reversed to long-term potentiation by subsequent application of dopamine, very likely via cAMP signaling. Implementing this bi-directionally modulated spike time dependent plasticity rule in a computational model yielded flexible learning of navigation towards changing target locations.

Both reviewers judged the study as interesting, linking synaptic plasticity rules with behavioral learning. Following the reviewers' comments the BRE would like to ask you to provide evidence that the timing of ACh and DA application is important for the observed changes in plasticity (ACh needs to be present during pairing and DA needs to be present after pairing; see reviewer #1). Reviewer #1 asked for additional figures and data analysis, which are described below in a point-by-point manner. The second reviewer wishes that you compare the effectiveness of the new learning rule with the classic STDP-based learning rule from e.g. Gerstner and Abbott 1997. This reviewer also asked for some direct predictions, e.g. the consequences of manipulating ACh receptors, which can be tested experimentally. We are including those reviews in their entirety in case this is helpful to you.

Reviewer #1:

1) The entire timing of STDP in the presence of ACh is not characterized. For example, plasticity induction in the presence of ACh could lead to LTD regardless of the pre-post timing.

2) The significance of the timing of ACh and DA application should be examined. It is assumed that ACh needs to be present during pairing and DA needs to be present after pairing but this necessity has not been explicitly examined (e.g., ACh present only after pairing).

3) STDP timing curves under basal condition, in DA alone, in ACh alone, and in DA + ACh in the model should be illustrated as a figure. These timing curves should be discussed with respect to those demonstrated in the field (e.g., see Figure 2 in Feldman DE, Neuron 75, 556-571, 2012).

4) Eligibility traces with decay kinetics should also be illustrated as a figure and discussed in comparison to DA action on STDP in brain slice. This will clearly illustrate the two timing rules, msec order timing for STDP and slower timing for DA action.

Reviewer #2:

The experiments were well designed and carried out. My main question is about their computational implications. The effects of ACh and dopamine on STDP are certainly interesting. However, they also "disable" the temporal asymmetry of STDP (as suggested in Figure 3A), a feature that was used in earlier modeling studies to accomplish learning of temporal sequences and navigational tasks.

1) Can the authors compare the effectiveness of this new learning rule with classic STDP-based learning (e.g. Gerstner and Abbott 1997 as subsequent models)?

2) Furthermore, can the authors offer some direct predictions, e.g. the consequences of manipulating ACh receptors, which can be tested by experiments?
