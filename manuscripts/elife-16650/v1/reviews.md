# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16650.009](https://doi.org/10.7554/eLife.16650.009)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Breaking down hierarchies in perceptual decision-making" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

These two papers present an enlightened and useful discussion about the interpretation of results previously published by Lorteije and colleagues. In that prior study, monkeys performed a task that required them to make a saccadic eye movement to the appropriate endpoint of a visual branching pattern with three bifurcations: one at the top, then two others under each branch, resulting in four distinct endpoints. Each bifurcation had a modulating luminance cue at each branch that determined the correct path: always choose the brighter (on average) branch. Through analyses of behavior and the activity of neurons in cortical areas V1 and V4 whose receptive fields corresponded to the locations of the luminance cues, a primary conclusion from that study was that the monkeys solved the task in a hierarchical manner, with decisions about the top- and lower-level branches first occurring in parallel, then combined for a final choice.

That landmark paper spawned several interesting discussions in the field. Hyafil and Moreno-Bote's technical comment encapsulates one of the critical lines of discussion about whether it is possible to truly distinguish a hierarchical decision-making process from a flat process based on the experimental data of Lorteije and colleagues. It is a critical and complex question. The reply by Zylerberg and colleagues adds further to the discussion, presenting several counter-arguments to the claims of Hyafil and Moreno-Bote.

All three reviewers were impressed by the tone and content of the submissions and agree that both represent worthwhile contributions to the literature. As noted by one of the reviewers, this kind of debate is "very valuable and generally underappreciated."

The above comments are included, verbatim, in our decision letters to both groups of submitting authors. We also will now make both initial submissions available to both groups, so that any potential revisions can fully take into account the claims made in the other submission. We will then allow for one more iteration: if and when we receive revised submissions and deem them appropriate, we will then again make each available to the other group for further revisions and clarifications.

Below are summaries of the discussions among the reviewers that are specific to your submission.

Essential revisions:

The reviewers agreed with the key point, that a "flat" mechanism that includes mutual inhibition can account for many features of the data and generally act like a hierarchical process. However, they also raised several concerns that should be addressed:

1) It would be useful to provide more intuitions about the specific assumptions and parameter values in the flat model that give rise to key types of output. It is critical to note that only some instantiations of the flat model are compatible with the data. The explanation in the legend of Figure 2E is useful but inadequate. Dedicating one or two paragraphs of the main text to model parameters and predictions will make the technical comment much more accessible. For example, why and under what parameter regimes inhibition in a flat model makes the accuracy of L2 decision independent of L1 stimulus strength? Likewise, can you provide better intuitions for the effect of scaling of noise with stimulus strength and rectification of the accumulators? Finally, the flat model explains the late influence of L1 on L2 and L2' choices, removing the need for complex interactions imposed by the hierarchical model. However, it also predicts that different L1 stimulus strengths should cause different magnitudes of suppression on TD neural responses, a prediction that does not match the data, as pointed out by Lorteije et al. It will be useful for readers to know that this prediction stems from Hyafil and Moreno-Bote's assumption that each accumulator equally suppresses the other accumulators. It is likely that suppression is not uniform, causing a TT choice to suppress TD less than DD because TD is a closer option to TT in the decision space than DD. Non-uniform suppression has been reported in various sensory processes and is quite likely to apply to multi-choice decisions.

2) A figure that recapitulates the task and the flat race-mode would also be useful.

3) The authors should be clearer on how they think their model relates to sensory and/or decision circuits. A race-model with mutual inhibition seems plausible in a decision-making area, but in a sensory area? Or do the authors assume the dynamics to play out in higher area and then feed back to V1 and V4? Making their argument explicit in the context of a model like that by Wimmer et al. 2015 would be very helpful. This point also seems strongly related to their claim that Figure 4 in Lorteije et al. argues against the hierarchical model because "localized selection signals merge information provided at different levels." Perhaps these sensory neurons are getting decision-related feedback?

4) The conclusion that the flat model is a "more parsimonious" explanation for the data than the model proposed by Lorteije et al. might be reconsidered, or at least clarified in the context of other lines of evidence from other studies that relate to flat versus hierarchical processing.

5) Zylberberg et al. argue that the RTs produced by the flat model presented by Hyafil and Moreno-Bote were unrealistic (although note that the task did not have a true RT design, and the measured RTs had only a weak dependence on signal strength). Can any version of the flat model (e.g., with collapsing bounds) produce the reported RTs?

6) It would be useful if both model code and relevant data files could be made available.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Breaking down hierarchies of decision-making in visual cortex" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior Editor) and Joshua Gold (Reviewing Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. We also note that our plan is as follows: once we receive an acceptable response to these issues, we will send the updated manuscript to Zylberberg and colleagues, so they have an opportunity to revise their manuscript accordingly. We then will share both papers with both groups, but at that point, if any further changes are desired, they have to be essential and very well justified.

1) Both papers discuss the new analysis by Zylberberg et al. showing that the strength of evidence at L1 affects V4 activity elicited by the L2 and L2' branches. They are in agreement with the finding but disagree with the interpretation. Part of the disagreement appears to stem from misunderstandings from some comments in the Hyafil and Moreno Bote manuscript. Specifically, as quoted by Zylberberg et al., Hyafil and Moreno Bote state in Appendix A that the flat model predicts that "selection signals at levels 2 are only influenced by information provided at level 2 branches […] and not by information provided at level 1." The new analyses by Zylberberg et al. clearly contradict this prediction. However, in their main text, Hyafil and Moreno Bote state that "this observation is most compatible with the flat model and by itself rules out the hierarchical model that relies on complete neural segregation of integration of L1 and L2 evidence." At the very least, please reconcile their statements in the Appendix and the main text.

2) Figure 2 vs. Figure 2—figure supplement 2: why not just show the Figure 2—figure supplement 2 panels in the main figure? Panels H and I could be relegated to the supplement.
