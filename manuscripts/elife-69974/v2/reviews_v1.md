# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69974.sa1](https://doi.org/10.7554/eLife.69974.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Variation in the modality of a yeast signaling pathway is mediated by a single regulator" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions, we regret to inform you that your work will not be considered further for publication in eLife.

Here is the consensus review:

This paper continues the lab's study of GAL1 induction in natural and laboratory strains of budding yeast. As previously shown, whether the induction is bimodal or unimodal depends upon the strain and the pre-induction carbon source. As the authors acknowledge in the Discussion section, we don't yet know the physiological significance of the phenomenon – i.e., is a unimodal response better under some environmental conditions and a bimodal response better under others – but still, working out how it arises is a nice test of our understanding of the system.

Here they present more data on the effects of strain background and pre-induction carbon source on the uni/bimodal nature of the response. They also present an ODE model of bistability and a much simpler phenomenological model that can account for many of the responses. This simpler model is based on Hill function (monostable) response curves with different thresholds for induced fraction and expression level of pathway output. And finally, they do gene swap experiments that argue that the uni vs. bimodal nature of a strain's response is largely determined by the sequence of the Gal3 gene.

This work could well be an interesting exercise in quantitative biology, but the reviewers found it so hard to understand what the authors were saying and showing that we are not really sure. For example, is the GAL system bistable (which is how the ODE model behaves) or not (as the phenomenological model assumes)? The reviewers were left confused about what the authors are concluding about the mechanism underpinning the phenomena they are describing.

We aim to publish work if revisions can be carried out in a couple of months. While required changes to the current work are too extensive to invite revision, we would likely be interested in a better-analyzed and better-presented take on this subject. It would be treated as a new submission, but we would try to recruit the same reviewers for evaluation.

Here are some specific aspects of the paper we had trouble with.

Data interpretation:

1. One of the core findings is that while all isolates are bimodal when galactose is titrated (in a background of raffinose), some are unimodal when glucose is titrated (in a background of an intermediate galactose (0.25%) + raffinose). One thing they did not mention, but can be seen comparing Figure S1 and Figure S2 is that some strains become more bimodal (in the sense that there is wide range of Glu/Gal mixtures in which two populations can clearly be detected). See for example the WashU strains or YJM981. (Does the ODE model also reproduce this?).

In general, this raises the question as to what is really going on. In my opinion, there might be a sort of misinterpretation of the data. Most strains seem to me to stay bimodal (comparing Figure S1 with S2), even if the statistical analysis they perform says otherwise. Let's take the case of the lab strain S288C as an example. The authors find that it is unimodal in Glu/Gal: however, what I see is that a group of uninduced cells persists as one moves from right to left (Figure S2), at the same time that the induced group starts to be induced in a graded fashion (again from right to left). So, in my view, that is a bimodal behavior: one mode corresponds to the group of uninduced yeast, and the other mode to the group of inducible cells, whose induction (or repression by glucose) is graded. The same behavior may be observed in other strains. My conclusion, comparing the galactose titration vs the glucose titration, is that the change in modality is (at least in most cases, maybe in all) apparent, not real; there is a change from a switch-like response to gradual induction (or repression) for those yeast that get induced, all in the context of a bimodal behavior. Thus, glucose is affecting only the inducible group.

In summary: the dose response to galactose (Figure S1) is switch-like (and bimodal), and the dose-response to glucose (Figure S2) (in a background of galactose) is graded (and bimodal).

If my interpretation is correct, the data in all the manuscript might need an overall change in interpretation.

Controls:

2. The Gal3 swap experiments are arguably the most interesting part of the paper (although, curiously, they are not mentioned in the abstract). And Gal3 was chosen for the swap for a good reason. However, it is quite possible that the other major regulators also affect strain behavior, and they could well be correlated with the allelic form of Gal3. As the authors know, previous work showed that simultaneous removal of the Gal3 and Gal1 positive feedbacks was required to truly eliminate bimodality. I wonder then what is the role of Gal1 and also Gal4 in strain to strain differences, since all these molecules have co-evolved in these strains. Thus, I think it would be important to show (a), considering that Gal1 serves a role very similar to Gal3, that Gal1 alleles are not important factors; (b) the result of a swap experiment using the Gal4 alleles, at least for a few interesting strains. Combining a joint swap of Gal3 and Gal4 and comparing with just Gal3 (already done with just Gal4). It would be important to see if the effect is reversed, or enhanced.

3. The authors need to present more than 'representative examples of at least two independent repeats'. Some assessment of experiment-to-experiment variability needs to be included.

The ODE model:

4. The ODE model needs to be written out. There is a parameter table, but without knowing what the rate equations are, the parameters are of little use. And as it is a reader can't really see what assumptions go into the model (e.g. Michaelis-Menten kinetics, which assume that the substrate is in huge excess over the enzyme?).

5. If I understand the ODE model correctly, it is a single-cell model; the authors are not trying to account for the cell-to-cell variability that makes the population level responses (sometimes) be bimodal. Why is this consideration included in the phenomenological model but not in the ODE model?

6. Finally, what is being measured is GAL1pr-YFP expression. What is being modeled in Figure 2 is various aspects of Gal4p and Gal3p. This is confusing.

The phenomenological model:

7. As mentioned above, this simpler model is based on Hill function (monostable) response curves (not bistable response curves, although I'm not sure how many readers will understand that the way this is written) with different thresholds for induced fraction and expression level of pathway output. And it accounts for much of the observed behavior. What does this mean? Is the point that the system is not bistable after all; or that the system may be bistable but you don't need bistability to account for the observed phenomena; or something else?

Clarity:

8. The authors need a more detailed cartoon than that shown in Figure 2A to give the uninitiated an idea of how the system works, and the scheme should include GAL1. The scheme also needs to be explained better.

9. If the authors are going to use the same figure panel more than once (e.g. Figure 7EF), the repetitions must be explicitly acknowledged.

10. Are the panels in Figure 6B flipped?

11. Throughout: Is it possible that 8 hours is too little to actually reach steady state after switching from pre-induced conditions? Could that explain the differences in strains? Maybe longer waiting needs to be tested.

12. Why are the GAL1pr-YFP fluorescence measurements normalized by dividing by SSC (a measure of cell texture) rather than FSC (a measure of cell size)?

13. Figure 2: Both Figure 2C and 2D are glucose titrations with constant galactose, so the labeling is confusing.

14. Line 171: '…determine whether a strain is bimodal' – bimodality is shown in many figures to depend on the pre-incubation conditions, not just the strain's identity. So what is meant by 'a strain is bimodal' – bimodal some of the time, all of the time, under some specific conditions compared across strains?

15. p. 9: The authors need to better explain why the fraction of active Gal3p should determine the fraction of cells in the induced state, whereas the amount of free Gal4p determines level of GAL1 induction in the induced cells. The logic is not apparent from Figure 2A. On p. 11 the authors do mention that they "previously showed that induced fraction and expression level are regulated by galactose/glucose ratio or the glucose concentration, respectively", but if "Pathway activation" is determined by Gal4p (Figure 2A) it is not clear how Gal3p and Gal4p could be determining different aspects of the response.
