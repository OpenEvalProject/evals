# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49257.sa1](https://doi.org/10.7554/eLife.49257.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Previous work in Drosophila has shown that apparently equivalent dopaminergic neurons can act on the same postsynaptic odor-coding cells to encode memories that differ in terms of valence and duration as well as learning rules required for their induction. These discoveries have important implications for diverse functions and effects of dopaminergic modulation in the mammalian brain. In this paper, Aso, Rubin and colleagues further explore cellular mechanisms that confer different properties to modulation mediated by different types of dopaminergic neurons. The key general insight is dopaminergic neurons can differ in cotransmitters released and that the difference in rules of timescales of learning and memory supported by dopamine can be ascribed to the effect of cotransmitter released. This broad idea is specifically documented here for dopaminergic neurons that co-release the gaseous transmitter nitric oxide. Beautifully precise experiments show that nitric oxide and dopamine co-released from certain dopaminergic neurons respectively write memories of opposite valence with different timescales. While dopamine induces plasticity relatively rapidly, nitric oxide induces an opposite form of plasticity over a slightly slower time scale. In this manner, the action of the gaseous transmitter nitric oxide not only reduces memory retention in wild type flies, but also fosters faster memory updating (e.g. in reversal learning). Thus, the work: (a) directly explains differences in memory encoding between specific distinct dopaminergic neurons; (b) provides new information on nitric oxide function in the brain; and (c) provides a potential general model in which cotransmitters confer unique modulatory properties to otherwise equivalent dopaminergic neurons.

Decision letter after peer review:

Thank you for submitting your article "Nitric oxide acts as a cotransmitter in a subset of dopaminergic neurons to diversify memory dynamics" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Mani Ramaswami as Reviewing Editor and K VijayRaghavan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Roland H. Strauss (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a wonderful study that demonstrates how in different compartments of the mushroom body, individual Kenyon cells can associate different valences with an odor using different learning rules with different timing. It also importantly demonstrates how different subtypes of superficially equivalent dopaminergic neurons can both encode different types of reinforcement and induce memories of different duration. The specific finding is that nitric oxide and dopamine co-released from certain dopaminergic neurons respectively write memories of opposite valence with different timescales. This finding is very well supported by behavioral studies combined with highly precise labeling and manipulation of dopaminergic subtypes as well as cell-type specific RNA-Seq analyses. Action of the gaseous transmitted nitric oxide not only reduces memory retention in wild type flies, but also fosters faster memory updating (e.g. in reversal learning). Using a computational model, the authors propose that dopamine and nitric oxide's effects on Kenyon cell output synapses might combine multiplicatively, not additively. This work demonstrates a diversity of dopaminergic neuron function and mechanisms, provides new insight into NO function in the brain and further extends the increasing parallels between the insect mushroom body and vertebrate cerebellum.

Essential revisions:

1) It may be worth acknowledging that the work (understandably) stops short of demonstrating that NO itself is the key messenger. Given the rigor of the rest of the work, perhaps it is worth considering a formal possibility that NOS1 signals to KCs via sGC in flies via a messenger different from NO?

2) The authors note in the legend to Figure 5 that the reduced inverted memory in MB-switch>Gycβ100B-RNAi flies without RU486 is probably due to leaky expression. A similar effect is seen in Figure 1 of Ferris et al. (Nat. Neurosci., 2006) and Figure 1 of Liu et al. (eLife, 2016). It is true that in previous papers, MB-switch without RU486 did not induce expression of GFP (Liu et al.) or lacZ (Mao et al., 2004 – original description of MB-switch). But maybe it depends on the UAS construct (e.g., perhaps GFP fluorescence is more sensitive than X-gal staining) or even the fly food. The authors may consider imaging some MB-switch>GFP brains with and without RU486. This should be very easy, would benefit the field by clarifying if MB-switch is leaky, and could support the authors' explanation for reduced inverted memory in the no-RU486 control for MB-switch>Gycβ100B-RNAi.

3) NO diffuses through membranes, so how is compartmentation kept up? Are NO-sensitive compartments interspaced with NO-insensitive compartments? Is a spill-over eventually meaningful? After all, "sGC [is] present in all MB compartments". The authors should discuss these conceptual issues given that NO is a diffusible gas. How is NO prevented from simply diffusing from the g1 compartment (NOS-positive) to the g2 compartment (NOS-negative) next door?

4) Is it surprising that TH-Gal4>shi[ts] does not cause inverted memory like the TH-null mutant (since NO signaling shouldn't require vesicle release)? Would the authors predict that TH-Gal4>shi[ts] would not block inverted memory in a TH-null mutant?

5) The narrative leading up to the discovery of NO as cotransmitter is probably historically accurate. However, given that the cotransmitter eventually discovered is a gas that isn't packaged into vesicles at all, the lead up describing how the presence of both clear and dense-core vesicles argues for a cotransmitter could be modified in a way that better prepares the reader for the final discoveries.

6) Subsection “Soluble guanylate cyclase in Kenyon cells is required to form NO-dependent memories”, last paragraph: The authors find that L-DOPA feeding in adults restores "normal" memory in TH mutants with MB>Gycβ100B-RNAi, and use this to argue that the lack of inverted memory in TH-null + MB>Gycβ100B-RNAi flies is not a developmental effect. Perhaps what the authors meant to write is that this control (like Figure 4A) shows that Gycβ100B-RNAi flies don't have a general defect in learning (as opposed to a specific defect in inverted learning)?

7) The model is very nice but the reader could use a bit more hand-holding in developing an intuition behind the results. Why exactly is it that the additive model "incorrectly predicts a reduction in memory strength after repeated pairings"? The stated explanation, "because of the slower accumulation of NO-dependent facilitation after DA-dependent potentiation has saturated" makes sense but doesn't give a very clear picture. Would it help to create a figure panel illustrating the time courses of D and N in the additive and multiplicative models and how these combine to affect w? Why (both practically and conceptually) isn't it possible to change the parameters for the additive model to allow the model to match the data in Figure 8D? The authors explain in the Materials and methods that the models were fit to the DA-only and NO-only data in Figure 6B, but the Results section would be easier to follow if this was also stated in the Results.

8) Does the additive model also fail to match experimentally measured memory decay/reversal? If so, that would help convince the reader that the close match between the data and model in Figure 8E-F isn't just an artefact from overfitting.

9) In reference to the second paragraph of the Discussion: Cell-autonomous NO signalling is also found in cerebellum Purkinje cells. Given the evidence for cell autonomy in two other systems, it could be useful to perform one additional experiment to test whether sGC is also required in DAN neurons. While appreciating that negative observations are hard to definitively interpret, this seems to be an issue worth addressing experimentally. If not, then the fact that dual targets for NO have not been excluded should be acknowledged. (This is also pertinent to comments 1 and 3).
