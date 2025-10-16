# Peer review - Round 1

Editors:
- K VijayRaghavan, Tata Institute for Fundamental Research , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15504.015](https://doi.org/10.7554/eLife.15504.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Continuous lateral oscillations as a core mechanism for taxis in Drosophila larvae" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Eduardo J Izquierdo (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Wystrach et al. present a simple model for navigation and show that simulations of this model produce trajectories that are consistent with those observed in some measurements of larval Drosophila chemotaxis. The paper is clear and well-written, and it is relatively easy to follow the authors' main arguments. The paper provides support for the hypothesis that taxis behavior in Drosophila larva is the result of modulation of a single behavior (i.e., a continuous lateral oscillation in the anterior body). Some claims are overstated and there needs to be some work on the Discussion (see below).

The authors provide experimental evidence through analysis of the larva's body bends showing the presence of continuous lateral oscillation. They then use an idealized computational model to test the hypothesis that modulation of such oscillation in the head is sufficient to reproduce the different orientation strategies observed in the larva (weathervaning, klinotaxis, and klinokinesis). This result is significant because larval taxis has been typically characterized as transitions between multiple behaviors, and this computational model shows a proof of concept that such an assumption is not necessary – and that a simpler strategy is sufficient to account for the observed behavior. The authors present a second model that is continuous in time, to further validate their hypothesis. One of the interesting insights is that the descending sensory signals that control the behavior do not need to be stronger on the different sides of the body. This result echoes the model presented by Izquierdo and Lockery, 2009, as the authors acknowledge.

Strengths: Overall, the goal, assumptions and insights from the model are rather well presented and easy to follow. Both a discrete and continuous time model are presented. Both make testable predictions that can be compared to existing or easily acquired data. The authors also explain some quantitative measures made in other experiments through the lens of their model.

Essential revisions:

Weaknesses and important suggestions for improvement:

The paper could do a better job of enumerating and consolidating these predictions and especially that the authors would emphasize where their model makes different predictions from existing models of taxis. Instead the emphasis seems to be on showing that their model can produce agreement with existing data. There are two problems with this approach: first, just because a simulation can reproduce an experimental result does not prove the simulation to be correct. Second, the authors have made some odd choices of experimental results with which to compare their model, with emphasis seeming to be on making very broad claims about the model's power, rather than stringently testing its powers of predictions (see technical discussion). Some attention needs to be paid to the citations, which are incomplete and sometimes off-target.

The authors should be clearer how it is that the model addresses klinokinesis. It is not clear how modulation of the oscillatory pattern can modulate the probability to run/stop. Also, typically klinokinesis involves random reorientation of the heading – is this also accounted for by the modulation of the oscillatory pattern?

One minor issue with the paper is that it might be lengthier than necessary. While eLife does not have a length limit, the authors could do one more pass at the writing to find suitable places to make the wording more succinct. The Discussion section is particularly lengthy.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Continuous lateral oscillations as a core mechanism for taxis in Drosophila larvae" for further consideration at eLife. Your revised article has been favorably evaluated by K VijayRaghavan as Senior Editor, a Reviewing Editor, and one reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Many of these could have been addressed as they were clearly mentioned in the first set of reviews.

While we appreciate that the authors have made an effort towards improving this paper, we cannot recommend that it be published in eLife as currently written, because it still contains significant flaws that were not corrected in revision. The authors still need to do the following:

a) Fix notation.

\nabla s is universally understood to be the gradient of s – a vector of the spatial derivatives of s. Writing (section “4.2 Agent-based simulation in discrete time steps”) "\nabla s_{n-1} = s_{n-1} – s_{n-2} represents the change in the sampled stimulus between time steps n-1 and n-2" is to equate this vector with a scalar difference in the value at two time points. Were it to be published in this form, it would cause great confusion and possibly cause readers to question the mathematical competency of the authors. It is astounding that after this basic error was pointed out gently to the authors, they failed to correct it.

Equation 1 on the same section is open to misinterpretation, because of confusing notation – H(…) is a function, but g(…) represents multiplication by a scalar. The authors put a note below, but it would me much more effective to place a symbol (e.g. g*(…)) to indicate multiplication.

b) Shorten the manuscript, focusing on significant new results and testable predictions that differentiate the model from existing ones.

The strengths of this paper are first the novelty of the suggestion that small continuous lateral head movements and larger "head-sweeps" or "head-casts" are in fact the same basic behavior and that modulation of the amplitude of these oscillations is the sole computation underlying navigational behaviors and second the presentation of two numerical model that embody this suggestion. This hypothesis leads to a number of testable predictions about the movements of larvae performing chemotaxis, and publication of this work will likely provoke interesting experimental work to test these predictions. This is why I support publication of the paper in eLife.

As an example of the testable predictions that I hope would be emphasized in a revised paper, consider lines 210-214: The agent tends to spend more time with the odour on its sides. Is this true only for radially symmetric odorant distributions created by diffusion from droplets (in which case this may be a geometric effect), or in a linear gradient would we expect that larvae would also be more likely to orient at angles to the direction of highest concentration? Run and tumble models would predict that in a linear gradient, the most probable orientation would be directly towards higher concentration, so this is a significant prediction that differentiates this model from others.

The second paragraph of the section “4.2 Agent-based simulation in discrete time steps” details another prediction that can test the model: if you provide a sharp stimulus change at a particular point in the oscillatory cycle, you should evoke a particular pattern of movement that is different from what would be predicted by the head-sweep acceptance model. I think this prediction could be extended or amplified – does it imply a resonant frequency at which an applied stimulus would evoke the greatest changes?

The third paragraph of the section “4.2 Agent-based simulation in discrete time steps” on the other hand does not present a test of the model: although lateralized sensing is not required for the model to function, it does not follow that the larva cannot have a lateralized internal representation of body posture, any more than the fact that the model does not include cessation of forward movement means that the larva cannot stop. So being able to condition a larva to turn left would not falsify the model; conversely the failure of lateralized operant conditioning could indeed be due to a lack of lateralized internal representation but also to a number of other causes (to my knowledge, no one has demonstrated that larvae can be operantly conditioned in any context). It is also not clear that the competing "run and tumble" model based on state transitions requires a lateralized internal representation.

c) Greatly reduce discussion of effects of changing gain and eliminate speculation about circuit function.

The simple model presented here – response to odor is linear in odor change with rectification and saturation – is not a complete description of chemotaxis. For instance, invariant response to odor over orders of magnitude concentration requires that the gain be a function of concentration, but this is not incorporated in mathematical description of the model in section 4. Further, current research indicates that olfactory receptor neurons do not respond linearly to odor concentrations (or to changes in odor concentration) and that behavioral responses to olfactory neuron activity are also nonlinear. It's completely fine to present a simplified model, especially if it makes it easier to understand the main features, but too much of the paper then focuses on the trivial results of adjusting these simplified model parameters.

Any model of olfaction necessarily has a "gain," a conversion from odor concentration (measured in number or mass per volume) to sensory neuron activity (measured in spikes per second, membrane voltage, inward current, etc.). For reduced models that do not attempt to represent the full neural pathway, the "gain" may instead represent a transformation from odor concentration to activity in some downstream neuron or a more generalized neural representation of odor quality and quantity. In the case, as presented here, that the gain simply multiplies the input stimulus, inverting the gain is mathematically equivalent to inverting the input stimulus, with the effect that taxis towards high concentration becomes taxis towards low concentration and vice versa. It is a completely trivial result that a switch from attraction to aversion can be effected by inverting the gain; to understand learning the interesting research question, not addressed in this work, is how this inversion is accomplished, especially in an odor-specific manner.

To be clear, "gain" is a model fit parameter. It has a well-defined meaning only in the context of section 4.2, Equation 1 and section 4.3 Equation 23. Discussion about learning changing gain, olfactory receptor neurons summing gain, motivation or habituation modifying gain, etc. are simply repeating the fact that changing this model parameter changes the behavior of the model. The authors should go back over their manuscript and remove (or shorten to at most a few sentences of discussion in total) any part that discusses the effect of changing the gain, unless they also present a testable, quantitative, and mechanistic explanation of how this change is accomplished.

The authors should also remove the discussion of neuroanatomical circuit elements. Nothing in the model as written directly represents any part of the larva's nervous system (even the continuous time model uses a simplified CPG model adapted from lamprey, with no evidence that such a system actually exists in Drosophila larvae). Attempting to place abstract and generalized model features into specific circuit contexts only leads to confusion and contradiction.

As an example, in section 3.5, it is proposed that ORNs respond with an ORN-odor-specific gain and that these gains are summed together to produce the overall response to an odor. (This is not entirely consistent with the existing understanding of Drosophila's olfactory system, which includes mutual inhibition mediated by local interneurons in the (larval) antennal lobe.) In section 2.6, learning is modeled as a change in gain. Taken together, 2.6 and 3.5 imply learning results from changes in responses of ORNs to odors. This contradicts both the current consensus of the field and the discussion in the later parts of section 3, which place learning at the mushroom bodies.

We recommend that section(s) 2.5 be shortened significantly, 2.6-2.8 eliminated entirely, 3.5 and 3.6 eliminated entirely, and 3.8 refocused on testable behavioral predictions, not on circuit architecture. In the rest of the manuscript, the authors should take the opportunity presented by another round of revision to consider what is most essential about this work and shorten the manuscript so that these important features are not lost. The Discussion currently occupies 10 manuscript pages (1/3 of the paper excluding Methods). I would recommend that it be shortened to at the very most 5 pages, and preferably 3.
