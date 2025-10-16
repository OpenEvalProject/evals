# Peer review - Round 1

Editors:
- Vivek Malhotra, The Barcelona Institute of Science and Technology , Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10167.010](https://doi.org/10.7554/eLife.10167.010)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "A reanalysis of the stochastic model of organelle production" for peer review at eLife. Your submission has been favorably evaluated by Vivek Malhotra (Senior Editor) and two reviewers.

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Specifically, the reviewers have raised a concern that your arguments are too aggressive and it would be best to tone down your statements. For example, you refer to "a number of errors" in the previous paper. The reviewers feel that this is incorrect or at least overstates the case. The reviewers agree that there was a major error in the O'Shea paper, namely the use of the shifted rather than the truncated Poisson distribution. Other than this, the mathematical results reported in the previous paper are correct as far as they go. Your manuscript shows that certain expressions in the Mukherji and O'Shea paper are exact, even though O'Shea and colleagues had reported them as approximate. This cannot be considered an error. The use of the word "dominant" is misleading, but is not a mathematical error. An abbreviated summary of the reviews follows.

A) Assessment of the manuscript:

First, I can find nothing mathematically incorrect about the present manuscript. The arguments are sound. Unlike the Mukherji and O'Shea paper, results are explicitly derived and all steps are detailed so readers are convinced of the correctness of these results. The paper is written in a rather pedagogical manner, the various results presented here are basically textbook material. For instance, deriving the detailed balance condition, explaining the stochastic simulation code, deriving the Poisson distribution, etc. would be standard graduate-level material typically not reported in a physics paper.

I do think a good point made in the present manuscript is the issue of identifiability, i.e. is it possible to identify an underlying microscopic model based on certain macroscopic measurements? It is clear from the new analysis that many combinations of parameter values can "mix together" to produce indistinguishable Fano factors, etc. However, on its own I don't think this analysis would have been considered a strong contribution. It is only as a critique of the Mukherji and O'Shea paper that this manuscript might be considered.

B) The contribution of the Mukherji and O'Shea paper:

The Mukherji and O'Shea paper made three major contributions:

1) It put forward the idea that heterogeneity in organelle number could be used to distinguish competing models of organelle biogenesis.

2) It made predictions from different models of biogenesis.

3) It reported experiments and compared them with predictions.

C) The critique of the Mukherji and O'Shea paper:

There are two major concerns raised about the Mukherji and O'Shea paper:

1) Were the simulations and the experiments truly done so the equilibrium assumption is correct?

2) The use of the shifted rather than the truncated Poisson distribution.

There are also two minor concerns:

3) What is the basis for various approximate Fano factors reported in the Mukherji and O'Shea paper?

4) The use of the term "dominance" in many places gives the reader the wrong impression.

Let's analyse each of these in turn.

1) During the review of the Mukherji and O'Shea paper, the issue of cell division as a confounding factor was explicitly raised. The authors' response was to provide more detailed simulations in which they showed that the Fano factors did not vary greatly when partitioning of organelles during division was taken into account, and was approximately as observed when the only mode of organelle reduction was a first-order decay term. This argument was convincing, assuming that equilibrium had truly been reached. I will add that the idea mentioned in the present manuscript (subsection “Does the SMOP analysis imply equilibrium distributions?”) that only if the time to equilibrium is short compared to the cell cycle time will the limiting distribution be valid, is a matter of scope. If the model explicitly includes cell division as one of the processes, that larger model will itself reach a limiting distribution. I agree that Mukherji and O'Shea provided no evidence that equilibrium had been reached, either in the simulations or the experiments, and were not requested to by the reviewers. This condition is typically assumed to be correct, and rarely are authors asked for evidence.

2) Is there any evidence that the simulations of the Mukherji and O'Shea paper had not reached equilibrium? I would assume that Mukherji and O'Shea would have done the correct validation steps, and there is some evidence of that in their Figure 1 for example. However, it is then difficult to understand how the error about the truncated vs. the shifted Poisson distribution could have arisen. I admit that this point could have been discovered by the reviewers if they had explicitly repeated some of the reported calculations in the Mukherji and O'Shea paper, and I for one overlooked it. It is unclear how the exact stochastic simulations could be in agreement with an incorrect shifted Poisson prediction. In the Mukherji and O'Shea paper no simulation matching the shifted Poisson prediction is given. Perhaps this simulation was never done, otherwise Mukherji and O'Shea would have discovered the discrepancy.

3) For certain expressions in the Mukherji and O'Shea paper, which arise out of an approximate calculation using the fluctuation-dissipation theorem (subsection “Incorrect analysis of cases with kfusion ≠ 0” of this manuscript), it is not explained how they were derived. This is a valid but minor concern; Mukherji and O'Shea would likely be able to provide the derivation. The point that the approximations were not necessary given the existence of an exact result is worth reporting but does not on its own detract from the original findings. In particular, many expressions derived in the Mukherji and O'Shea paper are correct, as shown in the present manuscript.

4) The misleading use of the word "dominant". There are scientific contexts where "dominance" is interchangeable with "greater than". E.g. in game theory, the word "dominance" is applied when the payoff from one strategy is just greater than from other strategy. Mukherji and O'Shea used the word "dominance" or "dominates" throughout their paper, but "contributed greater than" or some such term might have been more appropriate. I agree that this gives the reader the wrong impression, but does not, on its own, invalidate the results of Mukherji and O'Shea.

D) Is the critique valid?

I had said in my original review and I reiterate there: the ideas in the Mukherji and O'Shea paper were worth reporting, and I had hoped the original Mukherji and O'Shea paper would stimulate discussion and be improved upon with new analyses and measurements. The present manuscript in a sense validates this hope: discussion has indeed been stimulated. However, it is true that the original paper contained one major error not caught in the review process: use of the shifted rather than the truncated Poisson distribution. The present author argues that this weakens the central attraction of the previous paper, which was the strong agreement of theory and experiment. I would argue that the agreement itself, which was admittedly a striking feature, was not the central point on which the Mukherji and O'Shea paper stood. If the original paper had reported the correct distribution and highlighted the discrepancy with measured data, that would have also been food for thought.

Overall, I feel this is a more accessible and comprehensive theoretical analysis than the Mukherji and O'Shea paper provided, and serves to continue the original discussion.
