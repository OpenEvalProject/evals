# Peer review - Round 1

Editors:
- Alicia Izquierdo, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74500.sa0](https://doi.org/10.7554/eLife.74500.sa0)

Dr. Yang and colleagues trained nonhuman primates (rhesus monkeys) to play a semi-controlled version of the video game Pac-Man. This novel experimental paradigm allowed the authors to analyze and model the kinds of heuristic behavioral strategies monkeys use to solve relatively complex problems. The results provide insight into higher cognition in primates.


---

# Peer review - Round 1

Editors:
- Alicia Izquierdo, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74500.sa1](https://doi.org/10.7554/eLife.74500.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Monkey Plays Pac-Man with Compositional Strategies and Hierarchical Decision-making" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bruno B Averbeck (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The authors report on a complex behavior paradigm together with sophisticated modeling to study higher cognition in primates. The key claims of the manuscript are mostly supported by the data, and the approaches are rigorous. The reviewers were overall enthusiastic about this work, yet identified three key ways in which the findings should be clarified and the report improved:

1) An identified weakness was a lack of comparison with other models and a need for better justification of the modeling strategy. This is especially important since the dataset is very complex. Rather than solely a quantitative comparison of model performance, which may dilute the argument, there could be some discussion of an account for non-hierarchical possibilities. For example, a large neural network (i.e., a non-hierarchical model) could be trained on these trials and produce equal performance or better prediction. The authors should in some way provide more of a rationale for their approach. This could be in discussion, presentation of converging evidence, and/or additional model comparison.

2) Also related to #1, the reviewers suggested that perhaps a way to better justify the choice of model would be to do a selective comparison within the data (i.e. one or two better-chosen baselines) to support the hierarchical claim.

3) The authors should acknowledge that monkeys do not always perform this task in the optimal way, and that monkeys perhaps use a more passive strategy, or use multiple strategies at the same time. The monkeys could obtain almost all the rewards by the end of the game as there is nothing to pressure or force them to optimize their choices. Authors should more fully account for this feature in the experimental design when interpreting their data.

Reviewer #1 (Recommendations for the authors):

1. What do you mean by saying "a reasonable level" (line 114)? You may want to show the criteria.

2. Although Clyde tends to keep a certain distance from Pac-Man, why does Pac-Man also chase it when they are close to each other? (figure 1C)

3. Essential references are needed when explaining the behavior or mentioning previous literature, for example, in lines 316 and 485.

4. More details about how you tweaked the task are needed, such as how the monkeys operated the joystick? Holding it to move the Pac-Man, I guess.

Reviewer #2 (Recommendations for the authors):

– I think there are potential problems with identifiability in the model as detailed. If, for instance, the authors used a model with known time-varying weights to play the game and then fit their model to these data, do they correctly recover the weights?

– I am unfamiliar with the sense of "hierarchical" behavioral models as used here. By contrast, hierarchical models in RL involve goals, subgoals, etc., with models nested inside one another. If the authors are borrowing this less common sense of the term from somewhere, it would be helpful to cite it. I am not sure in what sense a perceptron is a "flat" model.

– Figure 1B: I find it hard to distinguish the grayscale lines and match them with their corresponding choice types. Also, I don't see standard errors here, as indicated in the caption.

– Figure 2: I found the boxes around the figure panels visually unappealing. This occurs in a couple of other figures.

– Figure 2C-D: If I follow, these are violin plots, not histograms, as stated in the caption.

– Figure 2E: The authors might consider a radar chart as an alternative way of representing these proportion data. Such a chart would allow them to plot each column here as one line and might facilitate more direct comparisons across strategy proportions.

– ll. 206-210: Before having read the methods, this text does not make it clear to me what the authors have done. That is, I don't know what it means here to linearly combine basis strategies or to "pool predictions." More specific language would be helpful, even if just a few words.

– Figure 3C-D: I don't think the dotted magenta lines are necessary, and they make the numbers hard to read.

– I was not sure what to take away from Figure 4. As a conceptual description, perhaps it belongs earlier in the text? Perhaps with some schematic as to how models are combined?

– ll 748-749: Shouldn't utilities for impossible actions be -∞? That is, in any probabilistic action selection model, there will be a probability of selecting any action with a finite utility difference, so the difference would need to be infinite to rule out an action.

– ll. 918-920: Three standard deviations seems like a pretty drastic cutoff for outliers. Why not five or at least four? Does this make a difference?
