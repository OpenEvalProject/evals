# Peer review - Round 1

Editors:
- Ranulfo Romo, Universidad Nacional Autonoma de Mexico , Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04220.011](https://doi.org/10.7554/eLife.04220.011)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Maximally informative foraging by Caenorhabditis elegans” for consideration at eLife. Your article has been favorably evaluated by a Senior editor, a Reviewing editor, and 2 reviewers.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The authors studied the foraging behavior of the C. elegans worm and found that the transitions from a local (search intensive) to a global (less turns, larger area) search strategy can be explained by a drift diffusion model that effectively maximizes information about the location of the food source. This infotaxis model has greater explanative value as compared to a chemotaxis mechanism that only follows the gradient of odorant concentration and the authors demonstrate that is could be implemented by a three-neuron circuit.

1) However, there are some few issues that the reviewers did not fully understand, and I agree: is the drift-diffusion model described by Equation (3) connected to the worm's sensory data in some way? In particular, decisions are reached when x reaches a value of zero, but is this initial value of x at the start of the local search? One of the reviewers thinks this is not clearly stated, and that might not be true, and I agree.

2) One of the reviewers thinks that the qualitative features (e.g., the abrupt change from local to global search; food concentration independence of optimal infotaxic search) show that this model is distinct from chemotaxis, and that it would be helpful to make direct comparisons with best fits from situations of chemotaxis in the figures (Figures 4a,b, 5B and 6b).

Minor comments/questions:

1) How similar are the foraging behaviors in other invertebrate species mentioned, and are there any other instances of infotaxis/mutual information searching in animal behaviors other than visual saccades and bacteria?

2) It would be interesting if the authors could describe an intuitively appealing rationale for why infotaxis as a method should be predicted to work. For example, when considering foraging behavior and various possible mathematical descriptions, is there a good a priori reason to expect that mutual information search would be favored?

3) The model contains three independent parameters that are fitted to reproduce the experimental distribution of the animal's positions at the end of the local search. Then the authors write, “Importantly, the same set of parameters can also account for the cumulative distribution of the durations of local search (Figure 4b).” Do they mean that the same set of parameters can be used to do this or that the same numerical values of the parameters account for the optimal durations?

4) “Predictions of the infotaxis model are based on the relative distribution of food across space, rather than on its absolute concentration.” Sounds a bit confusing; chemotaxis is based on a gradient, not an absolute concentration.

5) “At first glance, these calculations require the ability to maintain and update such “mental maps”, which may seem too computationally demanding to be implemented in a small neural circuit, such as the one found in C. elegans. Therefore, one may wonder whether the animals approximate the maximally informative foraging strategies.” This reference to a “mental map” in C. elegans is striking: does this model predict that as a result of this search strategy, the neuronal network acquires an internal representation of the environment?

6) “The temporal dynamics of this probability, and the fact that it represents the accumulating evidence, suggests that a drift-diffusion model may be able to approximate this log-probability.” An immediate jump to a drift-diffusion model might not occur to me. What are the arguments for using this model (other than that it seems to work post factum, e.g., reproduce the linear slope, etc.)? This model serves as a basis of approximation, so what exactly is being “approximated” in this approach, i.e., what is disregarded and what is kept? The authors say “Ultimately, maximally informative trajectories could potentially exhibit a much greater degree of diversity than can be accounted for by the simpler drift-diffusion model.” So what do we sacrifice to get the approximation?

7) “Invariance properties that characterize the maximally informative foraging trajectories” – what is meant by “invariance” here?

8) “Although initial descriptions of the model suggested that the reduction in entropy associated with each discrete number of odorant hits should be computed, in our experience any approximation of this results in unwanted behavior. Therefore, we limited the maximal number of odorants that can be simultaneously detected to 1”. This paragraph is hard to parse, please explain more clearly.

9) Am I correct in understanding that optimal infotaxis results are shown in both Figures 5a and 5b?

10) I assume the red and black curves in Figure 6b follow the same convention as Figure 5a (but not of later panels in this figure) but it would be helpful to explicitly state what the color convention is in the caption for Figure 6b.
